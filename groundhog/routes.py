from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
import folium
from groundhog.chances import chances
from groundhog.helpers import login_required
from groundhog.models import db, Sightings, Zoos


bp = Blueprint("routes", __name__, url_prefix="/")


@bp.route("/history", methods=["GET"])
@login_required
def history():
    sightings = Sightings.query.all()
    return render_template("history.html", sightings=sightings)


@bp.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        flash(chances(request.form.get("country")))
        return render_template("index.html")
    else:
        return render_template("index.html")


@bp.route("/map", methods=["GET"])
@login_required
def map_page():

    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")

    if latitude is None or longitude is None:
        geo_location = (42.375890, -71.114685)
    else:
        geo_location = (
            latitude,
            longitude,
        )

    folium_map = folium.Map(location=geo_location, zoom_start=17)

    # Add layer for habitat
    folium.raster_layers.WmsTileLayer(
        url="""https://www.sciencebase.gov:443/geoserver/CONUS_HabMap_2001/wms?SERVICE=WMS&""",  # noqa E501
        name="Habitat",
        fmt="image/png",
        layers="Woodchuck (Marmota monax) mWOODx v1",
        attribute="""U.S. Geological Survey (USGS) - Gap Analysis
         Project (GAP), 2018, Woodchuck (Marmota monax)
         mWOODx_CONUS_2001v1 Habitat Map: U.S. Geological Survey data
         release, https://doi.org/10.5066/F7BG2MD4.""",
        transparent=True,
        opacity=0.2,
        overlay=True,
        control=True,
    ).add_to(folium_map)

    # Add layer for range
    folium.raster_layers.WmsTileLayer(
        url="""https://www.sciencebase.gov:443/geoserver/CONUS_Range_2001/wms?SERVICE=WMS&""",  # noqa E501
        name="Range",
        fmt="image/png",
        layers="Woodchuck (Marmota monax) mWOODx v1",
        attribute="""U.S. Geological Survey (USGS) - Gap Analysis
         Project (GAP), 2018, Woodchuck (Marmota monax)
         mWOODx_CONUS_2001v1 Range Map: U.S. Geological Survey data
         release, https://doi.org/10.5066/F70864GK.""",
        transparent=True,
        opacity=0.2,
        overlay=True,
        control=True,
        show=False,
    ).add_to(folium_map)

    # Add a legend to hide/show layers
    folium.LayerControl().add_to(folium_map)

    # Add a markers
    markers = Sightings.query.all()

    for marker in markers:
        folium.Marker(
            location=(marker.latitude, marker.longitude), popup=marker.name
        ).add_to(folium_map)

    return render_template("map.html", folium_map=folium_map._repr_html_())


@bp.route("/sighting", methods=["GET", "POST"])
@login_required
def sighting():
    if request.method == "POST":
        lat = request.form.get("latitude")
        lon = request.form.get("longitude")

        sighting = Sightings(
            request.form.get("name"), lat, lon, request.form.get("description")
        )
        db.session.add(sighting)
        db.session.commit()
        return redirect(
            url_for("routes.map_page", latitude=lat, longitude=lon)
        )
    else:
        return render_template("sighting.html")


@bp.route("/zoo", methods=["GET"])
@login_required
def zoo():
    zoos = Zoos.query.all()
    return render_template("zoo.html", zoos=zoos)
