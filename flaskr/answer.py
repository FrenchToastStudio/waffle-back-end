from flask import current_app, flash, jsonify, make_response, redirect, request, url_for

class answer:
    def succes(response):
        theAnswer = {
            'statut': 'succes',
            'response': response
        }
        return make_response(jsonify(theAnswer)), 200
    def fail(response):
        theAnswer = {
            'statut': 'succes',
            'response': response
        }
        return make_response(jsonify(theAnswer)), 412
