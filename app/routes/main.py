from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    # return render_templete("index", title="home")
    return render_template("index.html")

@bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")