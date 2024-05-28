from app import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)
    address = db.Column(db.String(1024), nullable=False)
    housenumber = db.Column(db.Integer, nullable=False)
    neighborhood = db.Column(db.String(1024), nullable=False)
    telephone = db.Column(db.Integer, nullable=False)
    paymentamount = db.Column(db.Integer, nullable=False)
    dateofpayment = db.Column(db.Integer, nullable=False)
    formofpayment = db.Column(db.String(1024), nullable=False)
       
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'address':self.address,
            'housenumber':self.housenumber,
            'neighborhood':self.neighborhood,
            'telephone':self.telephone,
            'paymentamount':self.paymentamount,
            'dateofpayment':self.dateofpayment,
            'formofpayment':self.formofpayment
        }

    @staticmethod
    def from_json(json_data):
        id = json_data.get('id')
        name = json_data.get('name')
        address = json_data.get('address')
        housenumber = json_data.get('housenumber')
        neighborhood = json_data.get('neighborhood')
        telephone = json_data.get('telephone')
        paymentamount = json_data.get('paymentamount')
        dateofpayment = json_data.get('dateofpayment')
        formofpayment = json_data.get('formofpayment')
        
        return Client(id=id,name=name,address=address,housenumber=housenumber,neighborhood=neighborhood,telephone=telephone,paymentamount=paymentamount,dateofpayment=dateofpayment,formofpayment=formofpayment)