from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()
# model.py 
# test psql like movie ratings
# Make reltionships to other tables 
#figure out f strings 



class Creation(db.Model):
    """Creation form - How a user will start their project"""

    __tablename__ = "creation_form"

    creation_form_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    painting_name = db.Column(db.String, unique=True)
    canvas_id = db.Column(db.Integer,
                        db.ForeignKey('canvas_size.canvas_id'))
    weather_id = db.Column(db.Integer,
                            db.ForeignKey('weather.weather_id'))
    paint_id = db.Column(db.Integer,
                            db.ForeignKey('paint_type.paint_id'))

    # creation_form = a list of creation objects 

    def __repr__(self):
        return f'<Creation creation_form_id ={self.creation_form_id} email={self.email}>'  


class Canvas(db.Model):
    """picking the size of canvas"""

    __tablename__ = "canvas_size"

    canvas_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    size = db.Column(db.Integer)
    canvas_time = db.Column(db.Integer)

    creation_form = db.relationship('Creation')

    # canvas = options for user to select canvas type that will add to dry time

    def __repr__(self):
        return f'<Creation creation_form_id ={self.creation_form_id} email={self.email}>'

class Weather(db.Model):
    """selecting their weather/climate that will affect the dry time"""

    __tablename__ = "weather"

    weather_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    weather_type = db.Column(db.String)
    weather_time = db.Column(db.Integer)

    # weather = options for the user to select the climate they are in that will determine the dry time

    def __repr__(self):
        return f'<Creation creation_form_id ={self.creation_form_id} email={self.email}>'


class Paint(db.Model):
    """user can select up to 3 kinds of paint they're using to determine final dry time"""

    __tablename__ = "paint_type"

    paint_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type_of_paint = db.Column(db.String, unique=True)
    #not sure if i need unique for the different paint type nanes
    paint_time = db.Column(db.Integer)
    #will i need unique for paint dry time too?

    # paint_type = options of paint the user can select 

     def __repr__(self):
        return f'<Creation creation_form_id ={self.creation_form_id} email={self.email}>'

class Drying(db.Model):
    """takes in all factors from creation form and adds together for final dry time"""

    __tablename__ = "dry_time"

    dry_time_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    creation_form_id = db.Column(db.Integer,
                                  db.ForeignKey('creation_form.creation_form_id')  )

    # dry_time = populating final dry time for the result table

    def __repr__(self):
        return f'<Creation creation_form_id ={self.creation_form_id} email={self.email}>'



class Results(db.Model):
    """produces the final result for user"""

    __tablename__ = "final_result"

    final_result_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dry_time_id = db.Column(db.Integer,
                            db.ForeignKey('dry_time.dry_time_id'))

# final_result = user's full calculation 

 def __repr__(self):
        return f'<Creation creation_form_id ={self.creation_form_id} email={self.email}>'

    


if __name__ == '__main__':
    from server import app

    connect_to_db(app)