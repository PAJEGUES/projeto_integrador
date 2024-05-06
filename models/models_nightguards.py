from app import db

class Nightguard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    vehicle = db.Column(db.String(1024), nullable=False)
    licenseplate = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(255), nullable = False)
    dateofbirth = db.Column(db.DateTime, nullable=False)
    formofpayment = db.Column(db.Integer, nullable=False)
    neighborhood = db.Column(db.String(255), nullable=False)   

    def to_json(self):
        {
            'id':self.id,
            'name':self.name,
            'vehicle':self.vehicle,
            'licenseplate':self.licenseplate,
            'dateofbirth':self.dateofbirth,
            'cpf':self.cpf,
            'dateofbirth':self.dateofbirth,
            'formofpayment':self.formofpayment,
            'neighborhood':self.neighborhood
        }

    @staticmethod
    def from_jason(jason_data):
        id = jason_data.get('id')
        name = jason_data.get('name')
        vehicle = jason_data.get('vehicle')
        licenseplate = jason_data.get('licenseplate')
        dateofbirth = jason_data.get('dateofbirth')
        formofpayment = jason_data.get('formofpayment')
        neighborhood = jason_data.get('neighborhood')
        password = jason_data.get('password')
        return guard(id=id,name=name, password=password, vehicle=vehicle,licenseplate=licenseplate,dateofbirth=dateofbirth,formofpayment=formofpayment,neighborhood=neighborhood)

    
    
    
    
    
    
    
    
    