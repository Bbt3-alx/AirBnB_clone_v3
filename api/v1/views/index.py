#!/usr/bin/python3
"""Start api"""


from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Return status"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats')
def get_stats():
    """Number of object"""
    stats = {
           "Amenity": storage.count("Amenity"),
           "City": storage.count("City"),
           "Place": storage.count("Place"),
           "Review": storage.count("Review"),
           "State": storage.count("State"),
           "User": storage.count("User")
           }
    return jsonify(stats)
