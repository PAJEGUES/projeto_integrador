from app import db 

class User (db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    id = db.Column (db.Integer, primary_key = True)

    def to_json(self):
        return {
            'id':self.id,
            'email':self.email  
        }
    
    @staticmethod
    def from_json(json_data):
        id = json_data.get('id')
        email = json_data.get('email')
        password  = json_data.get('password') 

        return User (id=id, email=email, password=password)


class Token (db.Model):
    __tablename__ = 'tokens'
    token = db.Column(db.String(255), primary_key = True)
    expiration = db.Column(db.DateTime, nullable = False)
    user_id = db.Column (db.Integer, nullable = False)