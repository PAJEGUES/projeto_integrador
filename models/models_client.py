from app import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    road = db.Column(db.String(1024), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    neighborhood = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    paymentamount = db.Column(db.Integer, nullable=False)
    dateofbirth = db.Column(db.DateTime, nullable=False)
    formofpayment = db.Column(db.String(255), nullable=False)
       



    def to_json(self):
        {
            'id':self.id,
            'name':self.name,
            'road':self.road,
            'number':self.number,
            'neighborhood':self.neighborhood,
            'contact':self.contact,
            'paymentamount':self.paymentamount,
            'dateofbirth':self.dateofbirth,
            'formofpayment':self.formofpayment
            
        }

    @staticmethod
    def from_json(json_data):
        id = json_data.get('id')
        name = json_data.get('name')
        road = json_data.get('road')
        number = json_data.get('number')
        neighborhood = json_data.get('neighborhood')
        contact = json_data.get('contact')
        paymentamount = json_data.get('paymentamount')
        dateofbirth = json_data.get('dateofbirth')
        formofpayment = json_data.get('formofpayment')
        
        return Client(id=id,name=name,road=road,number=number,neighborhood=neighborhood,contact=contact,paymentamount=paymentamount,dateofbirth=dateofbirth,formofpayment=formofpayment)