""" CRUD operations. """
from model import db, FinalResult, DryTime, CreationForm, CanvasSize, Weather, PaintType, connect_to_db


# def create_movie(title, overview, release_date, poster_path):
#     """Create and return a new movie."""

#     movie = Movie(title=title,
#                   overview=overview,
#                   release_date=release_date,
#                   poster_path=poster_path)

#     db.session.add(movie)
#     db.session.commit()

#     return movie
def create_creation_form(painting_name, canvas_id, weather_id, paint_id):
    """Creating the calculation """
    
    creation_form = CreationForm(painting_name=painting_name,
                                    canvas_id=canvas_id,
                                    weather_id=weather_id,
                                    paint_id=paint_id)

    db.session.add(creation_form)
    db.session.commit()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)