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

### look at example from CS https://github.com/canjelica/churnNburn/blob/master/seed_database.py
#first func - load bank data from json file 

# Load paint data from JSON file
with open('<paints>) as p:
    paint_types = json.loads(p.read()) 
#Create paint types, store them in list
paints_in_db = []
for paints in paint_types:
    paint_type = paints['paint_type']
    dry_time = paints['"dry_time"']

 
    db_paint= crud.create_paint_types(paint_type, dry_time)  <---this is the crud function for creating the table row of painttype

    cc_in_db.append(db_credit_card)  ### maybe irrelevant?

with open('<weather>) as w:
    weather_conditions = json.loads(w.read()) 
#Create paint types, store them in list
weather_in_db = []
for weather in weather_conditions:
    weather_type = weather['weather_type']
    weather_time = weather['"weather_time"']

 
    db_weather= crud.create_weather_types(weather_type, weather_time) 


