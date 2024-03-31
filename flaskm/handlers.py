from flask import render_template, Blueprint


bp = Blueprint("users", __name__, url_prefix="")


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/table/<male>/<int:age>")
def table(male, age):
    key = male + ["", "_child"][age > 21]
    color = {"male": "#0080FF", "male_child": "#0000FF",
                  "female": "#FF9933", "female_child": "#FF8000"}[key]
    scr = "img/" + key + ".jpg"
    print(scr)
    return render_template("table.html", color=color, scr=scr)
