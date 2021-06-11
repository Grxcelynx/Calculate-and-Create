"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db
import crud
import json
import os
from twilio.rest import Client

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_PHONE_NUMBER']

client = Client(account_sid, auth_token)

@app.route('/send_sms', methods=["POST"])
def send_sms_twilio():
    dry_time_min = float(request.form.get("dry_time"))
    dry_time_hour = dry_time_min / 60.0
    painting_name = request.form.get("painting_name")
    phone_number = request.form.get('phone_number')
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    msg = f"Hi {fname} {lname}, here is your total dry time for your creation: In Minutes: {dry_time_min:.1f} In Hours: {dry_time_hour:.1f} "


    message = client.messages \
                .create(
                     body=msg,
                     from_=twilio_number,
                     to=phone_number
                 )

    # print(message.sid)
    # return message.sid
    return render_template("sms_sent.html", dry_time_min=dry_time_min, dry_time_hour=dry_time_hour, painting_name=painting_name,fname=fname,lname=lname, phone_number=phone_number)

@app.route('/')
def enterpage():
    """View opening page"""
    return render_template('open.html')


@app.route('/homepage')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route("/paint_info.html")
def grab_all_paint_info():
	"""Show all info about paint options for users to select to learn more about what they're creating with."""

	return render_template("homepage.html")


@app.route("/paint_info")
def show_all_paint_info():
	"""Show all info about paint options for users to select to learn more about what they're creating with."""

	return render_template("paint_info.html")


@app.route('/example')
def examples():
    """Grabbing all example calculations to view"""
    calc_examples = crud.get_examples()
    all_examples = []
    for ex in calc_examples:
        example_obj = {}
        example_obj['id'] = ex.example_id
        example_obj['paint'] = ex.paint_used
        example_obj['canvas'] = ex.canvas_selected
        example_obj['weather'] = ex.weather_condition
        example_obj['total'] = ex.total_dry_time
        
        all_examples.append(example_obj)

    return jsonify(all_examples)


@app.route('/get_paint_types')
def get_paint_types():
    """ Returns object of PaintTypes from database"""
    paint_types = crud.get_paint_types()
    all_paint_info= []
    for paint in paint_types:
        paint_objects = {}
        paint_objects["id"] = paint.paint_id
        paint_objects["type"] = paint.paint_type

        all_paint_info.append(paint_objects)
    # return json.dumps(paint_types)
    return jsonify(all_paint_info)
    # return render_template("creation_form.html", paints=all_paint_info)


@app.route('/get_weather')
def get_weather():
    """ Returns object of Weather conditions from database"""
    weather_types = crud.get_weather_types()
    all_weather_info = []
    for weather in weather_types:
        weather_objects = {}
        weather_objects["id"] = weather.weather_id
        weather_objects["type"] = weather.weather_type

        all_weather_info.append(weather_objects)

    return jsonify(all_weather_info)


@app.route('/get_canvas_sizes')
def get_canvas_sizes():
    """ Returns object of Canvas sizes from database"""
    canvas_sizes = crud.get_canvas_sizes()
    all_canvas_info = []
    for canvas in canvas_sizes:
        canvas_objects = {}
        canvas_objects["id"] = canvas.canvas_id
        canvas_objects["size"] = canvas.canvas_size

        all_canvas_info.append(canvas_objects)

    return jsonify(all_canvas_info)
    # return canvas_sizes

@app.route('/render_form')
def render_form():
    """renders creation form - grabs all json objects"""
    canvas_sizes = crud.get_canvas_sizes()
    paint_types = crud.get_paint_types()
    weather_types = crud.get_weather_types()

    return render_template("creation_form.html", canvas_sizes=canvas_sizes, paint_types=paint_types, weather_types=weather_types)

@app.route('/creation_form.html')
def go_to_form():
        
    return render_template("homepage.html")

@app.route('/calc_examples')
def go_to_examples():

    return render_template("calc_examples.html")
 


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
    app.run(host='0.0.0.0', debug=True, port=5005)





