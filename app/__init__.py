from flask import Flask
from app.config import Config
from app.models import db
import os

def create_app():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 
".."))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static")
    )

    app.config.from_object(Config)

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
