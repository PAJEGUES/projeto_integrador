from flask import Flask, request
from controllers.controller_administrators import set_administrators, del_administrators
from controllers.controller_neighborhood import get_neighborhood, get_neighborhoods_by_id
from controllers.controller_nightguards import post_nightguards, get_nightguards
from controllers.controller_sectors import get_sectors_by_id, put_sectors

from routes.route_administrators import bp_administrators
from routes.route_neighborhoods import bp_neighborhoods
from routes.route_night_guards import bp_night_guards
from routes.route_sectors import bp_sectors

app = Flask(__name__)

# ROTAS ADMINISTRATORS

# Rota POST para a criação de um ADMINISTRADOR
app.route("/administrators", methods=["POST"])(set_administrators)

# Rota DELETE de um ADMINISTRADOR
app.route("/administrators/<int:id>", methods = ["DELETE"])(del_administrators)

# ROTAS NIGHTGUARDS

# Rota GET para a leitura geral dos guardas noturnos
app.route("/get_nightguard", methods=["GET"])(get_nightguards)

# Rota POST Nightguard
app.route("/post_nightguard", methods=["POST"])(post_nightguards)


# ROTAS NEIGHBORHOODS

# Rota GET para todos os bairros
app.route("/get_neighborhood", methods=["GET"])(get_neighborhood)


# Rota GET de um UNICO bairro 
app.route("/neighborhoods/<int:id>", methods = ["GET"])(get_neighborhoods_by_id)


# ROTAS SECTORS

# Rota GET para um UNICO setor
app.route("/sectors/<int:id>", methods = ["GET"])(get_sectors_by_id)

# Rota UPDATE para o setor
app.route("/sectors/<int:id>", methods=["PUT"])(put_sectors)

### vinicius tem que fazer controller e router


app.register_blueprint(bp_administrators)
app.register_blueprint(bp_neighborhoods)
app.register_blueprint(bp_night_guards)
app.register_blueprint(bp_sectors)





# Rota UPDATE para o administrador
@app.route("/administrators/<int:id>", methods=["PUT"])
def put_administrators (id):

    update_administrators = request.get_json()

    i = 0

    for administrator in administrators: 
        if (id == administrator["id"]):
            administrators[i].update(update_administrators)
            return jsonify(update_administrators)
        i+=1
    return jsonify("Erro:administrador não encontrado"), 404



# Rota DELETE para o guarda noturno
@app.route("/night_guards/<int:id>", methods=["DELETE"])
def delete_night_guards_by_id (id):
 
    i = 0
    for night_guard in night_guards:
        if(id == night_guard["id"]):
            del night_guards[i]
            return jsonify(night_guards)
        i+=1
    return ("Erro, Guarda Noturno não encontrado"), 404

## Rota Bairros 
@app.route("/neighborhoods", methods=["POST"])
def set_neighborhoods():
 
    new_neighborhood  = request.get_json()
 
    if ('neighborhood_name' not in new_neighborhood ) or (not new_neighborhood ['neighborhood_name']):
          return jsonify({"error":"Não tem neighborhood_name"}), 400
   
    for neighborhood in neighborhoods :
        if (new_neighborhood ['id'] == neighborhood['id']):
            return jsonify("Erro, um bairro com esse id ja esta cadastrado!"), 409
 
    neighborhoods.append(new_neighborhood)
 
    return jsonify(neighborhoods)


# Rota GET para a leitura geral dos setores
 
@app.route("/sector", methods=["GET"]) # Rota GET
def get_sectors ():
    nightguard_name = request.args.get("nightguard_name", None)
    sector_name = request.args.get("sector_name", None)
    id = request.args.get("id", None)

    page = request.args.get("page", None)
    limit = request.args.get("limit", None)
 
    if id: id = int(id)
    if page: page = int(page)
    if limit: limit = int (limit)

    if page and limit:
        start = limit * (page - 1)
        end = start + limit
 
    vector_sector_name = []
    vector_nightguard_name = []
    vector_id = []
 
 
    for sector in sectors:
 
        if nightguard_name and nightguard_name == sector ["nightguard_name"]:
            vector_nightguard_name.append(sector)
        elif not nightguard_name:
            vector_nightguard_name.append(sector)
 
    for sector in vector_nightguard_name:
 
        if sector_name and sector_name == sector ["sector_name"]:
            vector_sector_name.append(sector)
        elif not sector_name:
            vector_sector_name.append(sector)
 
    for sector in vector_sector_name:
 
        if id and id == sector ["id"]:
            vector_id.append(sector)
        elif not id:
            vector_id.append(sector)
 
    if page and limit:
        return jsonify (vector_id[start:end])
    else: 
        return jsonify (vector_id)

## Rotas Ailson

# Rota GET para a leitura geral dos administradores

@app.route("/administrator", methods=["GET"]) # Rota GET
def get_administrators ():

    login = request.args.get("login", None)
    password = request.args.get("password", None)
    page = request.args.get("page", None)
    limit = request.args.get("limit", None)
    id = request.args.get("id", None)

    if id: id = int(id)
    if page: page = int(page)
    if limit: limit = int (limit)

    if page and limit:
        start = limit * (page - 1)
        end = start + limit 

    vector_login = []
    vector_password = []
    vector_id = []


    for administrator in administrators:

        if login and login == administrator ["login"]:
            vector_login.append(administrator)
        elif not login:
            vector_login.append(administrator)

    for administrator in vector_login:

        if password and password == administrator ["password"]:
            vector_password.append(administrator)
        elif not password:
            vector_password.append(administrator)

    for administrator in vector_password:

        if id and id == administrator ["id"]:
            vector_id.append(administrator)
        elif not id:
            vector_id.append(administrator)
    if page and limit:
        return jsonify (vector_id[start:end])  # Os dois pontos indicam "até", nesse caso, retorno do início até o fim 
    else:
        return jsonify (vector_id)
    
# Rota GET de um UNICO Guarda
@app.route("/night_guards/<int:id>", methods = ["GET"]) 
def get_night_guards_by_id (id):

    i = 0
    for night_guard in night_guards:
        if(id == night_guard["id"]):
            return jsonify(night_guards[i])
        i+=1
    return ("Erro, Guarda noturno não encontrado"), 404

 # Rota UPDATE para o bairro
@app.route("/neighborhoods/<int:id>", methods=["PUT"])
def put_neighborhoods (id):

    update_neighborhoods = request.get_json()

    i = 0

    for neighborhood in neighborhoods: 
        if (id == neighborhood["id"]):
            neighborhoods[i].update(update_neighborhoods)
            return jsonify(update_neighborhoods)
        i+=1
    return jsonify("Erro: Bairro não encontrado"), 404

# Rota DELETE para o setor
@app.route("/sectors/<int:id>", methods=["DELETE"])
def delete_sectors_by_id (id):
 
    i = 0
    for sector in sectors:
        if(id == sector["id"]):
            del sectors[i]
            return jsonify(sectors)
        i+=1
    return ("Erro, Setor não encontrado"), 404
 
app.run(debug=True)