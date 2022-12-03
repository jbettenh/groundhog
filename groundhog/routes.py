from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
)
from groundhog.helpers import login_required

bp = Blueprint("routes", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
@login_required
def index():
    """Show homepage"""
    return render_template("index.html")


@bp.route("/about", methods=["GET"])
@login_required
def add_page():
    return render_template("about.html")


@bp.route("/tracking", methods=["GET"])
@login_required
def tracking():
    return render_template("tracking.html")


@bp.route("/history", methods=["GET"])
@login_required
def history():
    return render_template("history.html")


@bp.route("/map", methods=["GET"])
@login_required
def map_page():
    return render_template("map.html")


@bp.route("/zoo", methods=["GET"])
@login_required
def zoo():
    return render_template("zoo.html")
