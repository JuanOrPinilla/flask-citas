from flask import Flask, redirect, render_template, request, flash, url_for
from config import config 
from database import db
import psycopg2.extras
import re
import requests

#Routes
from routes import citas


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"

conn = db.get_db_connection()

@app.route("/")
def index():
     return render_template('index.html')



@app.route("/health-check/")
def health():
    return "OK!"


def page_not_found(error):
     return "<h1> Not found page :( </h1>",404

def unauthorized(error):
     return "<h1> No tienes permisos >:( </h1>",401

if __name__ == "__main__":
      app.config.from_object(config['development'])

      #Blueprints
      app.register_blueprint(citas.main, url_prefix='/api/citas/')

      #ErrorHandlers
      app.register_error_handler(404, page_not_found)
      app.register_error_handler(401, unauthorized)
      app.run(host='0.0.0.0', port=8080, debug=True)
