from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()
# model.py 
# test psql like movie ratings
# Make reltionships to other tables - DONE
#figure out f strings - DONE 



class CreationForm(db.Model):
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
    
    canvas_size = db.relationship("CanvasSize", back_populates="creation_form")
    weather = db.relationship("Weather", back_populates="creation_form")
    paint_type = db.relationship("PaintType", back_populates="creation_form")

    dry_time = db.relationship('DryTime', back_populates='creation_form_id')



    # creation_form = a list of creation objects 

    def __repr__(self):
        return f'<CreationForm creation_form_id ={self.creation_form_id} painting_name={self.painting_name}>'  


class CanvasSize(db.Model):
    """picking the size of canvas"""

    __tablename__ = "canvas_size"

    canvas_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    size = db.Column(db.Integer)
    canvas_time = db.Column(db.Integer)

    creation_form = db.relationship('CreationForm', back_populates='canvas_size')

    # child = relationship("Child", uselist=False, back_populates="parent")

    # canvas = options for user to select canvas type that will add to dry time

    def __repr__(self):
        return f'<CanvasSize canvas_id ={self.canvas_id} size={self.size}>'


class Weather(db.Model):
    """selecting their weather/climate that will affect the dry time"""

    __tablename__ = "weather"

    weather_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    weather_type = db.Column(db.String)
    weather_time = db.Column(db.Integer)

    creation_form = db.relationship('CreationForm', back_populates='weather')
    # weather = options for the user to select the climate they are in that will determine the dry time

    def __repr__(self):
        return f'<Weather weather_id ={self.weather_id} weather_type={self.weather_type}>'


class PaintType(db.Model):
    """user can select up to 3 kinds of paint they're using to determine final dry time"""

    __tablename__ = "paint_type"

    paint_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type_of_paint = db.Column(db.String, unique=True)
    #not sure if i need unique for the different paint type nanes
    paint_time = db.Column(db.Integer)
    #will i need unique for paint dry time too?

    # paint_type = options of paint the user can select 
    creation_form = db.relationship('CreationForm', uselist=False, back_populates='paint_type')


    def __repr__(self):
        return f'<PaintType paint_id ={self.paint_id} type_of_paint={self.type_of_paint}>'


class DryTime(db.Model):
    """takes in all factors from creation form and adds together for final dry time"""

    __tablename__ = "dry_time"

    dry_time_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    creation_form_id = db.Column(db.Integer,
                                  db.ForeignKey('creation_form.creation_form_id')  )

    # dry_time = populating final dry time for the result table

    creation_form = db.relationship("CreationForm", back_populates="dry_time")

    # final_result = db.relationship('FinalResult', uselist=False, back_populates='dry_time_id')

    def __repr__(self):
        return f'<DryTime dry_time_id ={self.dry_time_id} creation_form_id={self.creation_form_id}>'



class FinalResult(db.Model):
    """produces the final result for user"""

    __tablename__ = "final_result"

    final_result_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dry_time_id = db.Column(db.Integer,
                            db.ForeignKey('dry_time.dry_time_id'))

# final_result = user's full calculation 

    # dry_time = db.relationship('DryTime', back_populates='final_result')


def __repr__(self):
    return f'<FinalResult final_result_id ={self.final_result_id} dry_time_id={self.dry_time_id}>'

def connect_to_db(flask_app, db_uri='postgresql:///creation_form', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')
  


if __name__ == '__main__':
    from server import app

    connect_to_db(app)