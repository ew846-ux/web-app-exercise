import random
from flask import Blueprint, request, render_template, redirect, flash

from app.rps import VALID_OPTIONS, determine_winner

rps_routes = Blueprint("rps_routes", __name__)


@rps_routes.route("/rps/form")
def rps_form():
    print("RPS FORM...")
    return render_template("rps_form.html", options=VALID_OPTIONS)


@rps_routes.route("/rps/results", methods=["GET", "POST"])
def rps_results():
    print("RPS RESULTS...")

    if request.method == "POST":
        request_data = dict(request.form)
    else:
        request_data = dict(request.args)
    print("REQUEST DATA:", request_data)

    user_choice = (request_data.get("user_choice") or "").lower()

    # if user_choice not in VALID_OPTIONS:
    #     return render_template("rps_form.html", options=VALID_OPTIONS,
    #                            error="Please choose rock, paper, or scissors."), 400
    if user_choice not in VALID_OPTIONS:
        flash("Invalid choice. Please choose rock, paper, or scissors!", "danger")
        return redirect("/rps/form")
    computer_choice = random.choice(VALID_OPTIONS)
    winner = determine_winner(u=user_choice, c=computer_choice)

    flash("Game played successfully!", "success")
    return render_template("rps_results.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        winner=winner
    )
   