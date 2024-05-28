from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_http_middleware import MiddlewareManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():

    from routes.route_administrators import bp_administrators
    from routes.route_neighborhoods import bp_neighborhoods
    from routes.route_night_guards import bp_night_guards
    from routes.route_sectors import bp_sectors 
    from routes.route_client import bp_client
    from routes.route_user import bp_users
    from middleware import MetricsMidleware
    from flask_cors import CORS

    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*", "allow_headers": ["Content-Type", "Token"]}})

    app.register_blueprint(bp_administrators)
    app.register_blueprint(bp_neighborhoods)
    app.register_blueprint(bp_night_guards)
    app.register_blueprint(bp_sectors)
    app.register_blueprint(bp_client)

    app.register_blueprint(bp_users)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://adm:Adm12345!@10.60.46.36/projetoDesktop'

    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)

    secured_routers = ["/login"]            
    app.wsgi_app = MiddlewareManager(app)
    app.wsgi_app.add_middleware(MetricsMidleware ,secured_routers = secured_routers)

    return app






 

