import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "change-this-in-production",
    )

    DATABASE_URL = os.environ.get(
        "DATABASE_URL",
        "sqlite:///smartlead.db",
    )

    GROQ_API_KEY = os.environ.get(
        "GROQ_API_KEY",
        "",
    )

    AI_PROVIDER = os.environ.get(
        "AI_PROVIDER",
        "groq",
    )

    CORS_ORIGINS = os.environ.get(
        "CORS_ORIGINS",
        "*",
    )

    # Yönerge gereği konuya özel backend içeriği yalnızca burada.
    BUSINESS_CONTEXT = """
    Sen ENCORE'un yapay zekâ destekli kültür-sanat asistanısın.

    Kullanıcının kültür-sanat ve etkinliklerle ilgili genel
    sorularını Türkçe, samimi ve yönlendirici bir dille yanıtla.

    Kullanıcı uygun olduğunda ENCORE hakkında daha fazla bilgi
    almak için iletişim bilgisi bırakabilir.

    Kullanıcıdan iletişim bilgisi bırakmasını isterken
    baskıcı olma.

    Bilmediğin bilgileri uydurma.
    Kesin olmayan konularda bunu açıkça belirt.
    """


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}