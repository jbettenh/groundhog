from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
)
import folium
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
    start_coords = (42.375890, -71.114685)
    folium_map = folium.Map(location=start_coords, zoom_start=17)

    # Add layer for habitat
    folium.raster_layers.WmsTileLayer(
        url="https://www.sciencebase.gov:443/geoserver/CONUS_HabMap_2001/wms?SERVICE=WMS&",
        name="Habitat",
        fmt="image/png",
        layers="Woodchuck (Marmota monax) mWOODx v1",
        attribute="U.S. Geological Survey (USGS) - Gap Analysis Project (GAP), 2018, Woodchuck (Marmota monax) mWOODx_CONUS_2001v1 Habitat Map: U.S. Geological Survey data release, https://doi.org/10.5066/F7BG2MD4.",
        transparent=True,
        opacity=0.2,
        overlay=True,
        control=True,
    ).add_to(folium_map)

    # Add layer for range
    folium.raster_layers.WmsTileLayer(
        url="https://www.sciencebase.gov:443/geoserver/CONUS_Range_2001/wms?SERVICE=WMS&",
        name="Range",
        fmt="image/png",
        layers="Woodchuck (Marmota monax) mWOODx v1",
        attribute="U.S. Geological Survey (USGS) - Gap Analysis Project (GAP), 2018, Woodchuck (Marmota monax) mWOODx_CONUS_2001v1 Range Map: U.S. Geological Survey data release, https://doi.org/10.5066/F70864GK.",
        transparent=True,
        opacity=0.2,
        overlay=True,
        control=True,
        show=False,
    ).add_to(folium_map)

    # Add a legend to hide/show layers
    folium.LayerControl().add_to(folium_map)

    return render_template("map.html", folium_map=folium_map._repr_html_())


@bp.route("/zoo", methods=["GET"])
@login_required
def zoo():
    return render_template("zoo.html")
