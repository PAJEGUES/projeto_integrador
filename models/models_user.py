from app import db 

class User (db.Model):
    __tablename__ = 'users'
    email =
    password = db.Column(db.String(255))
    id = db.Column (db.Integer, primary_key = True)


class Token (db.Model):
    __tablename__ = 'tokens'
    token = db.Column(db.String(255), primary_key = True)
    expiration = db.Column(db.DateTime, nullabe = False)
    user_id = db.Column (db.Integer, db.Foreignkey('users.id'))