from app import db
from flask import Flask ,request , jsonify 
from models_sector import sector

class Sectors (db.Model):
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
        neighborhood_name = json_data.get('bairro')
        sector_name  = json_data.get('setor') 
        
        return Sectors (id=id, neighborhood_name=neighborhood_name, sector_name=sector_name)
        


