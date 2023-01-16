#!/usr//bin/python3
"""
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def state():
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>')
def state_id(id):
    states = storage.all('State')
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def remove_session(self):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
