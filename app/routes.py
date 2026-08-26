from flask import Blueprint, jsonify, render_template, request

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import AIServiceError, ai_service


pages = Blueprint("pages", __name__)
api = Blueprint("api", __name__)


# --------------------------------------------------
# SAYFA ROTALARI
# --------------------------------------------------

@pages.route("/")
def index():
    return render_template("index.html")


@pages.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# --------------------------------------------------
# API ROTALARI
# --------------------------------------------------

@api.route("/sohbet", methods=["POST"])
def sohbet():
    data = request.get_json(silent=True) or {}

    mesaj = str(
        data.get("mesaj", "")
    ).strip()

    gecmis = data.get(
        "gecmis",
        [],
    )

    if not mesaj:
        return jsonify(
            {
                "basari": False,
                "hata": "Mesaj alanı zorunludur.",
            }
        ), 400

    if not isinstance(gecmis, list):
        gecmis = []

    try:
        yanit = ai_service.yanit_uret(
            mesaj=mesaj,
            gecmis=gecmis,
        )

        return jsonify(
            {
                "basari": True,
                "yanit": yanit,
            }
        ), 200

    except AIServiceError as error:
        return jsonify(
            {
                "basari": False,
                "hata": str(error),
            }
        ), 503


@api.route("/leads", methods=["POST"])
def lead_olustur():
    data = request.get_json(silent=True) or {}

    isim = str(
        data.get("isim", "")
    ).strip()

    telefon = str(
        data.get("telefon", "")
    ).strip()

    mesaj = str(
        data.get("mesaj", "")
    ).strip()

    if not isim or not telefon:
        return jsonify(
            {
                "basari": False,
                "hata":
                    "İsim ve telefon alanları zorunludur.",
            }
        ), 400

    try:
        lead_id = lead_ekle(
            isim=isim,
            telefon=telefon,
            mesaj=mesaj or None,
        )

        return jsonify(
            {
                "basari": True,
                "mesaj":
                    "Bilgileriniz başarıyla kaydedildi.",
                "lead_id": lead_id,
            }
        ), 201

    except Exception:
        return jsonify(
            {
                "basari": False,
                "hata":
                    "Bilgiler kaydedilirken bir sorun oluştu.",
            }
        ), 500


@api.route("/leads", methods=["GET"])
def leadleri_getir():
    try:
        leadler = tum_leadler()

        return jsonify(
            {
                "basari": True,
                "leads": leadler,
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "basari": False,
                "hata":
                    "Lead kayıtları şu anda alınamıyor.",
            }
        ), 500