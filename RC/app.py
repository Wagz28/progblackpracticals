from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import os
import json

app = Flask(__name__, template_folder='./', static_folder='./')
CORS(app)

MAIN_FOLDER = os.path.join(os.path.dirname(__file__))

@app.route('/')
def home():
    print("Rendering styling-lists.html")
    return render_template('styling-lists.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
