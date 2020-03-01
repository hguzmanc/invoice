from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello'})


if __name__ == '__main__':
    app.run(debug=True)
