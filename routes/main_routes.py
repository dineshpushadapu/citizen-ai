from flask import Blueprint, redirect, url_for, session

main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/about")
def about():
    if not session.get("user_name"):
        return redirect(url_for("auth_bp.login"))
    return redirect(url_for("about"))
