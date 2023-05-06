#!/usr/bin/python3
"""
A new view for state objects that handles all RESTFUL API actions
"""

import storage from models
import Amenity from models.amenity
import app_views from api.v1.views
import jsonify from flask
import abort from flask
import request from flask
import swag_from from flasgger.utils


@app_views.route('/amenities', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/amenity/all_amenities.yml')
def amenities():
    """Get all Amenities"""
    res = [
        amenity.to_dict() for amenity in storage.all(Amenity).values()
    ]
    return jsonify(res)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/amenity/get_amenity.yml', methods=['GET'])
def amenity_by_id(amenity_id):
    """Get Amenity filter by id"""
    res = storage.get(Amenity, amenity_id)
    if res is None:
        abort(404)
    return jsonify(res.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/amenity/delete_amenity.yml', methods=['DELETE'])
def delete_amenity(amenity_id):
    """Delete an Amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({})


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/amenity/post_amenity.yml', methods=['POST'])
def insert_amenity():
    """Insert new Amenity"""
    body = request.get_json()
    if type(body) != dict:
        return abort(400, {'message': 'Not a JSON'})
    if 'name' not in body:
        return abort(400, {'message': 'Missing name'})
    new_amenity = Amenity(**body)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/amenity/put_amenity.yml', methods=['PUT'])
def update_amenity_by_id(amenity_id):
    """Update an Amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    body = request.get_json()
    if type(body) != dict:
        return abort(400, {'message': 'Not a JSON'})
    for key, value in body.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
