#!/usr/bin/python3
"""
"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)
#app.url_map.strict_slashes = False

@app.route('/states_list', strict_slashes = False)
def state_list():
    """render list of states"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(self):
    """closes storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
