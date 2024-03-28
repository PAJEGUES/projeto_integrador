from app import db 

class Administrator (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return {
            'id':self.id,
            'login':self.login,
            'password':self.password
        }
    
    @staticmethod
    def from_json(json_data):
        id = json_data.get('id')
        login = json_data.get('login')
        password = json_data.get('password')
        return Administrators (id=id, login=login, password=password)


