from flask_http_middleware import MiddlewareManager, BaseHTTPMiddleware
from flask import jsonify



class MetricsMidleware(BaseHTTPMiddleware):
    def __init__(self, secured_routers = []):
        super().__init__()
        self.secured_routers = secured_routers


    def dispatch(self, request, call_next):
        if not(request.path in self.secured_routers):
            if(request.headers.get('token') == "senac123"):
                return call_next(request)
            else:
                return jsonify({"Error": "Usuario não autenticado"})
        else:
            return call_next(request) 
        

