""" CRUD operations. """
from model import db, CreationForm, CanvasSize, Weather, PaintType, connect_to_db



def create_paint_types(paint_type, paint_time):
    """Creating and returning paint types that user selects """

    paint = PaintType(paint_type=paint_type, paint_time=paint_time)

    db.session.add(paint)
    db.session.commit()

    return paint

def create_weather_type(weather_type, weather_time):
    """Creating and returning all weather conditions user selects"""

    weather = Weather(weather_type=weather_type, weather_time=weather_time)

    db.session.add(weather)
    db.session.commit()

    return weather

def create_canvas_type(canvas_size, canvas_time):
    """Creating and returning all canvas sizes user selects"""

    canvas = CanvasSize(canvas_size=canvas_size, canvas_time=canvas_time)

    db.session.add(canvas)
    db.session.commit()

    return canvas


def get_weather_types():
    """Return all types of weather"""
    return Weather.query.all()


def get_canvas_sizes():
    """Return all possible canvas sizes for users"""
    return CanvasSize.query.all()


def get_paint_types():
    """Return all paint types."""

    return PaintType.query.all()



def get_creation_form_id(creation_form_id):
    """Grabbing all information from a specfifc creation form ID 
    to send the user their dry time info through Twilio SMS API """
    return query.filter_by(creation_form_id=creation_form_id).first()


def create_creation_form(painting_name, canvas_id, weather_id, paint_id):
    """Taking in user's input/selections to return their selections of all given columns """
    
    creation_form = CreationForm(painting_name=painting_name,
                                    canvas_id=canvas_id,
                                    weather_id=weather_id,
                                    paint_id=paint_id)

    db.session.add(creation_form)
    db.session.commit()

    return creation_form




if __name__ == '__main__':
    from server import app
    connect_to_db(app)