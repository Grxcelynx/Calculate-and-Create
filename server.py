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


@app.route('/get_paint_types')
def get_paint_types():
    """ Returns object of PaintTypes from database"""
    paint_types = crud.get_paint_types()
    all_paint_info= []
    for paint in paint_types:
        p = {}
        p["id"] = paint.paint_id
        p["type"] = paint.paint_type
        all_paint_info.append(p)
    # return json.dumps(paint_types)
    return jsonify(all_paint_info)
    # return render_template("creation_form.html", paints=all_paint_info)


@app.route('/get_weather')
def get_weather():
    """ Returns object of Weather conditions from database"""
    weather_types = crud.get_weather_types()
    all_weather_info = []
    for weather in weather_types:
        w = {}
        w["id"] = weather.weather_id
        w["type"] = weather.weather_type
        all_weather_info.append(w)

    return jsonify(all_weather_info)


@app.route('/get_canvas_sizes')
def get_canvas_sizes():
    """ Returns object of Canvas sizes from database"""
    canvas_sizes = crud.get_canvas_sizes()
    all_canvas_info = []
    for canvas in canvas_sizes:
        c = {}
        c["id"] = canvas.canvas_id
        c["size"] = canvas.canvas_size
        all_canvas_info.append(c)

    return jsonify(all_canvas_info)
    # return canvas_sizes

@app.route('/render_form')
def render_form():
    """renders creation form - grabs all json objects"""
    canvas_sizes = crud.get_canvas_sizes()
    paint_types = crud.get_paint_types()
    weather_types = crud.get_weather_types()

    return render_template("creation_form.html", canvas_sizes=canvas_sizes, paint_types=paint_types, weather_types=weather_types)


    
@app.route('/creation_post', methods=["POST"])
def collect_painting_input():
    """Gathering info from the creation form for the user to create a dry time"""

    painting_name = request.form.get("painting_name")
    canvas_size = request.form.get("canvas_size")
    weather_type = request.form.get("weather_type")
    paint_type = request.form.get("paint_type")
    
    creation_form = crud.create_creation_form(painting_name, canvas_size, weather_type, paint_type)

    # return jsonify(creation_form.painting_name)   
    return render_template("result.html", creation_form=creation_form)


@app.route('/creation_form')
def show_creation_form():
        """Showing creation_form.html template"""
        return render_template("creation_form.html")




if __name__ == '__main__': 
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)





