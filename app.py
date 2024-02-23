from flask import Flask, request
from routes.route_administrators import bp_administrators
from routes.route_neighborhoods import bp_neighborhoods
from routes.route_night_guards import bp_night_guards
from routes.route_sectors import bp_sectors

app = Flask(__name__)

app.register_blueprint(bp_administrators)
app.register_blueprint(bp_neighborhoods)
app.register_blueprint(bp_night_guards)
app.register_blueprint(bp_sectors)

app.run(debug=True)

## Rotas Ailson

# Rota GET para a leitura geral dos administradores



    
# Rota GET de um UNICO Guarda



 # Rota UPDATE para o bairro



# Rota DELETE para o setor


 

