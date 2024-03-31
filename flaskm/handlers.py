from flask import render_template, Blueprint


bp = Blueprint("users", __name__, url_prefix="")


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/distribution")
def distribution():
    team = ["Ридди", "Петя", "Коля", "Маша", "Иван", "Гриша", "Саша", "Миша"]
    return render_template("list_prof.html", team=team)
