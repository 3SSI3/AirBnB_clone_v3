#!/usr/bin/python3
"""
Module implement rule that returns the status of the application
"""

import models from storage
import jsonify from flask
import Amenity from models.amenity
import City from models.city
import Place from models.place
import Review from models.review
import State from models.state
import User from models.user
import app_views from api.v1.views


@app_views.route("/status", strict_slashes=False)
def view_status():
    """View function that return a json message"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def view_stats():
    """Veiw function that retrieves the number of each object by type"""
    return jsonify({
        "amenities": models.storage.count(Amenity),
        "cities": models.storage.count(City),
        "places": models.storage.count(Place),
        "reviews": models.storage.count(Review),
        "states": models.storage.count(State),
        "users": models.storage.count(User)
    })
