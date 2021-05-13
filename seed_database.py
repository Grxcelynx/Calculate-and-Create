"""Script to seed database."""

import os
import json

import crud
import model
import server

os.system('dropdb calculate_n_create')
os.system('createdb calculate_n_create')

model.connect_to_db(server.app)
model.db.create_all()


# Load paint data from JSON file
with open('./data/paints.json') as p:
    paint_types = json.loads(p.read()) 
#Create paint types, store them in list
paints_in_db = []
for paints in paint_types:
    paint_type = paints['paint_type']
    paint_time = paints['paint_time']
    paint_photo = paints['paint_photo']

 
    db_paint= crud.create_paint_types(paint_type, paint_time)  #<---this is the crud function for creating the table row of painttype

    paints_in_db.append(db_paint)  ### maybe irrelevant? Not sure if needed?

with open('./data/weather.json') as w:
    weather_conditions = json.loads(w.read()) 
#Create weather conditions, store them in list
weather_in_db = []
for weather in weather_conditions:
    weather_type = weather['weather_type']
    weather_time = weather['weather_time']

 
    db_weather= crud.create_weather_type(weather_type, weather_time) 

    weather_in_db.append(db_weather)  ### maybe irrelevant? Not sure if needed?


with open('./data/canvas.json') as c:
    canvas_sizes = json.loads(c.read()) 
#Create canvas sizes, store them in list
canvas_in_db = []
for canvas in canvas_sizes:
    canvas_size = canvas['canvas_size']
    canvas_time = canvas['canvas_time']

  
    db_canvas= crud.create_canvas_type(canvas_size, canvas_time) 

    canvas_in_db.append(db_canvas)  ### maybe irrelevant? Not sure if needed?


