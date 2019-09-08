# modules
import datetime

# Packages
from flask import Flask, jsonify, request
import pytz

# Files
from env import Env

env = Env('Api')

# __name__ is '__main_' if run as the main program
# else __name__ will be the file name
app = Flask(__name__)

@app.route('/', methods=['GET'])
def landing():
    return jsonify({'success': True})

@app.route('/show/<name>', methods=['GET'])
def show(name):
    return jsonify({'machine': name})

# It's as if the interpreter inserts this at the top
# of your module when run as the main program.
if __name__ == '__main__':
    print(f' * Starting {env.name} API on {datetime.datetime.now(tz=pytz.utc)}')
    app.run(host=env.host , port=env.port, debug=env.debug)