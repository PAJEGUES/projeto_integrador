from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_http_middleware import MiddlewareManager, BaseHTTPMiddleware
from middleware import MetricsMidleware

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    from routes.route_administrators import bp_administrators
    from routes.route_neighborhoods import bp_neighborhoods
    from routes.route_night_guards import bp_night_guards
    from routes.route_sectors import bp_sectors 

    app = Flask(__name__)

    app.register_blueprint(bp_administrators)
    app.register_blueprint(bp_neighborhoods)
    app.register_blueprint(bp_night_guards)
    app.register_blueprint(bp_sectors)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://adm:Adm12345!@10.60.46.36/projetoDesktop'

    db.init_app(app)
    migrate.init_app(app,db)

    secured_routers = ["/login"]        
        
    app.wsgi_app = MiddlewareManager(app)
    app.wsgi_app.add_middleware(MetricsMidleware ,secured_routers = secured_routers)

    return app






 

