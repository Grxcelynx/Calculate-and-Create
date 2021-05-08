"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db
import crud
import json

# from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
# app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


#You also need get methods for your front end to get data from tables to present to the user
#paint, canvase, and weather GET methods. You will use these GET endpoints on the frontend to 
# display this info from your databse on the forms (as dropdowns)

@app.route('/get_paint_types')
def get_paint_types():
    """ Returns object of PaintTypes from database"""
    paint_types = crud.get_paint_types()
    all_paint_info= []
    for paint in paint_types:
        all_paint_info.append(paint.paint_type)
    # return json.dumps(paint_types)
    return jsonify(all_paint_info)


@app.route('/get_weather')
def get_weather():
    """ Returns object of Weather conditions from database"""
    weather_types = crud.get_weather_types()
    all_weather_info = []
    for weather in weather_types:
        all_weather_info.append(weather.weather_type)

    return jsonify(all_weather_info)



@app.route('/get_canvas_sizes')
def get_canvas_sizes():
    """ Returns object of Canvas sizes from database"""
    canvas_sizes = crud.get_canvas_sizes()
    all_canvas_info = []
    for canvas in canvas_sizes:
        all_canvas_info.append(canvas.canvas_size)

    return jsonify(all_canvas_info)

    
# POst methods gather info from the front end to give eto the datbase
@app.route('/creation_form', methods=["POST"])
def collect_painting_input():
    """Gathering info from the creation form for the user to create a dry time"""

    painting_name = request.form.get("painting_name")
    canvas_type = request.form.get("canvas_id")
    weather_condition = request.form.get("weather_id")
    paint_type = request.form.get("paint_id")

    creation_form = crud.create_creation_form(painting_name, canvas_type, weather_condition, paint_type)

    return jsonify(creation_form)   

@app.route('/creation_form')
def show_creation_form():
        """Showing creation_form.html template"""
        return render_template("creation_form.html")



# from flask import render_template

# @app.route('/hello')
# def say_hello():
#     """Show hello.html template."""

#     return render_template("hello.html")

if __name__ == '__main__': 
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)





