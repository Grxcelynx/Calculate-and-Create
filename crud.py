""" CRUD operations. """
from model import db, FinalResult, DryTime, CreationForm, CanvasSize, Weather, PaintType, connect_to_db

# IN order for these tables to be pouplated, you need functions to create them (Crud)
#Create functions for each  type that creates those paint/canvas/weather rows
#Read json file - insert to database

###EXAMPLE####
# def create_bank(bank_name, approval_rule_num_accounts,    approval_rule_time_months, max_accounts):
#     """Create and return a new bank."""

#     bank = Bank(bank_name=bank_name, approval_rule_num_accounts=approval_rule_num_accounts, approval_rule_time_months=approval_rule_time_months, max_accounts=max_accounts)

#     db.session.add(bank)
#     db.session.commit()

#     return bank

def create_paint_types(paint_type, dry_time):
    """Creating and returning paint types that user selects """

    paint = Paint(paint_type=paint_type, dry_time=dry_time)

    db.session.add(paint)
    db.session.commit()

    return paint

def create_weather_type(weather_type, weather_time):
    """Creating and returning all weather conditions user selects"""

    weather = Weather(weather_type=weather_type, weather_time=weather_time)

    db.session.add(weather)
    db.commit()

def create_canvas_type(canvas_size, canvas_time):
    """Creating and returning all canvas sizes user selects"""

    canvas = Canvas(canvas_size=canvas_size, canvas_time=canvas_time)

    db.session.add(canvas)
    db.commit()

#READ functions for paint/canvas/weather
def get_weather_types():
    """Return all types of weather"""
    return Weather.query.all()


def get_canvas_sizes():
    """Return all possible canvas sizes for users"""
    return CanvasSize.query.all()


def get_paint_types():
    """Return all paint types."""

    return PaintType.query.all()


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