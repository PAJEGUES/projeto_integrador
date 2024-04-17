from app import db 

class Token (db.Model):
    __tablename__ = 'tokens'
    token = db.Column(db.String(255), primary_key = True)
    expiration = db.Column(db.DateTime, nullabçe = False)
    user_id = db.Column (db.Integer, db.Foreignkey('class_user.id'))