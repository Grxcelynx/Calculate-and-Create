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
with open('<FILE NAME>) as f:
    paint_types = json.loads(f.read()) 
#Create banks, store them in list
cc_in_db = []
for cc in paint_types:
    paint_type = cc['paint_type']
    dry_time = cc['"dry_time"']

 
    db_paint= crud.create_paint  <---this is the crud function for creating the table row of painttype

    cc_in_db.append(db_credit_card)  ### maybe irrelevant?