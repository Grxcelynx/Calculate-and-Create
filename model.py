from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class CreationForm(db.Model):
    """Creation form - How a user will be selecting their desired values for their calculated dry time"""

    __tablename__ = "creation_form"

    creation_form_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    painting_name = db.Column(db.Text)
    canvas_id = db.Column(db.Integer,
                        db.ForeignKey('canvas_size.canvas_id'))
    weather_id = db.Column(db.Integer,
                            db.ForeignKey('weather.weather_id'))
    paint_id = db.Column(db.Integer,
                            db.ForeignKey('paint_type.paint_id'))
    final_dry_time = db.Column(db.Float)
    
    canvas_size = db.relationship("CanvasSize", back_populates="creation_form")
    weather = db.relationship("Weather", back_populates="creation_form")
    paint_type = db.relationship("PaintType", back_populates="creation_form")
    # final_result = db.relationship('FinalResult', back_populates='creation_form') -NOT USING RELATIONSHIP ANYMORE

    def __repr__(self):
        return f'<CreationForm creation_form_id ={self.creation_form_id} painting_name={self.painting_name}>'  


class CanvasSize(db.Model):
    """All canvas sizes with dry times to add into the final dry time"""

    __tablename__ = "canvas_size"

    canvas_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    canvas_size = db.Column(db.Text, unique=True)
    canvas_time = db.Column(db.Integer)

    creation_form = db.relationship('CreationForm', back_populates='canvas_size')

    def __repr__(self):
        return f'<CanvasSize canvas_id ={self.canvas_id} size={self.canvas_size}>'


class Weather(db.Model):
    """the weather/climate that will affect the dry time"""

    __tablename__ = "weather"

    weather_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    weather_type = db.Column(db.Text, unique=True)
    weather_time = db.Column(db.Integer)

    creation_form = db.relationship('CreationForm', back_populates='weather')

    def __repr__(self):
        return f'<Weather weather_id ={self.weather_id} weather_type={self.weather_type}>'


class PaintType(db.Model):
    """user can select the kind of paint they're using to determine final dry time"""

    __tablename__ = "paint_type"

    paint_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    paint_type = db.Column(db.Text, unique=True)
    paint_time = db.Column(db.Integer)
    # paint_photo = db.Column(db.Text, unique=True)

    creation_form = db.relationship('CreationForm', uselist=False, back_populates='paint_type')


    def __repr__(self):
        return f'<PaintType paint_id ={self.paint_id} paint_type={self.paint_type}>'



def connect_to_db(flask_app, db_uri='postgresql:///calculate_n_create', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')
  


if __name__ == '__main__':
    from server import app

    connect_to_db(app)