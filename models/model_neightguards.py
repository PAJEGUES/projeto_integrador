from app import db

class guard(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    vehicle = db.Column(db.String(1024))
    licenseplate = db.Column(db.String(255))
    email = db.Column(db.String(255))
    cpf = db.Column(db.String(11))
    dateofbirth = db.Column(db.String(10))
    formofpayment = db.Column(db.String(10))
    neighborhood = db.Column(db.String(255))   



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
        return guard(id=id,name=name,vehicle=vehicle,licenseplate=licenseplate,dateofbirth=dateofbirth,formofpayment=formofpayment,neighborhood=neighborhood)
    
    
    
    
    
    
    
    
    
    