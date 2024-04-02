from app import db

class Sector (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    neighborhood_name = db.Column(db.String(255), nullable=False)
    sector_name = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return {
            'id':self.id,
            'neighborhood_name':self.neighborhood_name,
            'sector_name': self.sector_name
           
        }
    
    @staticmethod
    def from_json(json_data):
        id = json_data.get('id')
        neighborhood_name = json_data.get('neighborhood_name')
        sector_name  = json_data.get('sector_name') 

        return Sector (id=id, neighborhood_name=neighborhood_name, sector_name=sector_name)
        


