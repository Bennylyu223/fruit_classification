import os

from flask import Flask, request


#  创建app，并设定其config属性
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

#   如果没有config
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import classis
    app.register_blueprint(classis.bp)

    return app
