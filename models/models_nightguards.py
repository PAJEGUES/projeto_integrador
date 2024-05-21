from app import db

class Nightguard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    vehicle = db.Column(db.String(255), nullable=False)
    licenseplate = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable = False)
    dateofbirth = db.Column(db.Date, nullable=False)
    formofpayment = db.Column(db.String(255), nullable=False) 

    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'vehicle':self.vehicle,
            'licenseplate':self.licenseplate,
            'dateofbirth':self.dateofbirth,
            'email': self.email,
            'cpf':self.cpf,
            'dateofbirth':self.dateofbirth,
            'formofpayment':self.formofpayment
        }

    @staticmethod
    def from_json(json_data):
        id = json_data.get('id')
        name = json_data.get('name')
        email = json_data.get('email')
        vehicle = json_data.get('vehicle')
        cpf = json_data.get('cpf')
        licenseplate = json_data.get('licenseplate')
        dateofbirth = json_data.get('dateofbirth')
        formofpayment = json_data.get('formofpayment')
        password = json_data.get('password')
        return Nightguard(id=id,name=name, password=password, vehicle=vehicle,licenseplate=licenseplate,dateofbirth=dateofbirth,formofpayment=formofpayment, email=email, cpf=cpf)

    
    
    
    
    
    
    
    
    