from flask import jsonify, request
from datetime import datetime, timedelta
from models.models_user import User, Token
from app import db, bcrypt
import time

def login_user():
    body = request.get_json()
    jemail =  body.get('email')
    password = body.get('password')
    ouser = User.query.filter_by(email=jemail).first_or_404(description="Usuario nao encontrado!")
    if (bcrypt.check_password_hash(ouser.password, password)):
        user_id = ouser.id
        token = bcrypt.generate_password_hash(password + str(time.time()))
        expiration = datetime.now() + timedelta(hours=1)
        otoken = Token(user_id = user_id, token = token, expiration = expiration)
        db.session.add(otoken)
        db.session.commit()
        return jsonify({"Message": "Usuario Logado ", "token": str(token)})
    else:
        return jsonify({"Erro": "Senha Incorreta"}), 401