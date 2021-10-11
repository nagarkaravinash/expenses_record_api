from flask import Flask
from flask_cors import CORS
app = Flask("src")
CORS(app, resources={r"/*": {"origins": "*"}}, send_wildcard=True)
from src.controler import *
    