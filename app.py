from flask import Flask, request, jsonify
from controllers.controller_administrators import set_administrators
from controllers.controller_neighborhood import get_neighborhoods_by_id
from controllers.controller_nightguards import get_nightguards
from controllers.controller_sectors import put_sectors

app = Flask(__name__)

# --- JOSÉ --- Rota POST para a criação de um ADMINISTRADOR
app.route("/administrators", methods=["POST"])(set_administrators)

# --- JOSÉ --- Rota GET para a leitura geral dos guardas noturnos
app.route("/nightguard", methods=["GET"])(get_nightguards)

# --- JOSÉ --- Rota GET de um UNICO bairro 
app.route("/neighborhoods/<int:id>", methods = ["GET"])(get_neighborhoods_by_id)

 # --- JOSÉ --- Rota UPDATE para o setor
app.route("/sectors/<int:id>", methods=["PUT"])(put_sectors)


@app.route("/neighborhood/<int:id>", methods = ["DELETE"]) # Rota DELETE   
def del_neighborhood (id):

    for x in enumerate(neighborhoods):
        if(id == neighborhoods["id"]):
            del neighborhoods[id]
            return jsonify(neighborhoods)
    return ("Erro, Bairro não encontrado"), 404

app.run(debug=True)