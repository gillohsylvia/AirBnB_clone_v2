#!/usr/bin/python3
"""
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """displays html page for states, cities and their amenities"""
    data = {
        "states": storage.all('State').values(),
        "amenities": storage.all('Amenity').values()
    }

    return render_template('10-hbnb_filters.html', models=data)


@app.teardown_appcontext
def remove_session(self):
    """close the db"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
