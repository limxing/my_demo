from flask import Flask
from flask_uploads import configure_uploads

from settings import load_config
from .core import db, migrate, ma, photos
from apps.main.view import mod as main_mod


def create_app():
    # app配置
    app = Flask(__name__, instance_relative_config=True)
    config = load_config()
    app.config.from_object(config)

    #数据库
    db.init_app(app)
    migrate.init_app(app, db=db)

    app.register_blueprint(main_mod)
    #解析json
    ma.init_app(app)
    #上传图片配置
    configure_uploads(app, photos)
    return app
