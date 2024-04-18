from flask_http_middleware import MiddlewareManager, BaseHTTPMiddleware
from flask import jsonify
from models.models_user import Token
from datetime import datetime, timedelta

class MetricsMidleware(BaseHTTPMiddleware):
    def __init__(self, secured_routers = []):
        super().__init__()
        self.secured_routers = secured_routers


    def dispatch(self, request, call_next):
        if not (request.path in self.secured_routers):
            jtoken = request.headers.get('token')
            otoken = Token.query.filter(Token.expiration > datetime.now()).filter_by(token=jtoken).first()
            if(otoken != None):
                return call_next(request)
            else:
                return jsonify({"Error": "Usuario nao autenticado"})
        else:
            return call_next(request) 
        

