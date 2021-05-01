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