import os

from flask import Flask, jsonify
from flask_cors import CORS

from config import config_by_name
from app.database import init_db
from app.routes import api, pages


def create_app(config_name=None):
    """
    Uygulama fabrikası.
    Ayarları, CORS'u, veritabanını ve blueprint'leri birleştirir.
    """

    app = Flask(__name__)

    selected_config = (
        config_name
        or os.environ.get(
            "FLASK_CONFIG",
            "development",
        )
    )

    config_class = config_by_name.get(
        selected_config,
        config_by_name["development"],
    )

    app.config.from_object(config_class)

    CORS(
        app,
        origins=app.config["CORS_ORIGINS"],
    )

    init_db(app)

    app.register_blueprint(pages)

    app.register_blueprint(
        api,
        url_prefix="/api",
    )

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify(
            {
                "basari": True,
                "durum": "aktif",
                "servis": "SmartLead AI",
            }
        ), 200

    return app