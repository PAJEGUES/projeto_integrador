from flask import Flask, request
from controllers.controller_administrators import set_administrators
from controllers.controller_neighborhood import get_neighborhoods_by_id
from controllers.controller_nightguards import post_nightguards, get_nightguards
from controllers.controller_sectors import put_sectors

app = Flask(__name__)

# --- JOSÉ --- Rota POST para a criação de um ADMINISTRADOR
app.route("/administrators", methods=["POST"])(set_administrators)

# --- ROGÉRIO --- Rota POST Nightguard
app.route("/post_nightguard", methods=["POST"])(post_nightguards)

# --- JOSÉ --- Rota GET para a leitura geral dos guardas noturnos
app.route("/get_nightguard", methods=["GET"])(get_nightguards)

# --- JOSÉ --- Rota GET de um UNICO bairro 
app.route("/neighborhoods/<int:id>", methods = ["GET"])(get_neighborhoods_by_id)

 # --- JOSÉ --- Rota UPDATE para o setor
app.route("/sectors/<int:id>", methods=["PUT"])(put_sectors)

app.run(debug=True)