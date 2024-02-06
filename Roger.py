from flask import Flask, request, jsonify

app = Flask(__name__)

night_guards = [
    {
    "name": "ROGER",
    "vehicle": "CB-500",
    "licenseplate": "RMR-1909",
    "email": "roger.rocha@gmail.com",
    "password": "cb123",
    "cpf": "987.654.321.00",
    "dateofbirth": "03/02/1980",
    "formofpayment": "dinheiro",
    "dateofpayment": "20",
    "district": "Azulville"
    }    
]


neighborhoods = [
    {

    }
]

@app.route("/night_guard", methods=["POST"]) # Rota POST
def night_guard ():
    new_night_guard = request.get_json()
            
    if ('name' not in new_night_guard) or (new_night_guard ['name'] == ""):
        return jsonify ("Erro: Incorrect login."), 400
    
    if ('vehicle' not in new_night_guard) or (new_night_guard ['vehicle'] == ""):
        return jsonify ("Erro: Incorrect vehicle."), 400
    
    if ('licenseplate' not in new_night_guard) or (new_night_guard ['licenseplate'] == ""):
        return jsonify ("Erro: Incorrect licenseplate."), 400
    
    if ('email' not in new_night_guard) or (new_night_guard ['password'] == ""):
        return jsonify ("Erro: Incorrect password."), 400
    
    if ('password' not in new_night_guard) or (new_night_guard ['name'] == ""):
        return jsonify ("Erro: Incorrect login."), 400
    
    if ('cpf' not in new_night_guard) or (new_night_guard ['cpf'] == ""):
        return jsonify ("Erro: Incorrect cpf."), 400
    
    if ('dateofbirth' not in new_night_guard) or (new_night_guard ['dateofbirth'] == ""):
        return jsonify ("Erro: Incorrect dateofbirth."), 400
    
    if ('formofpayment' not in new_night_guard) or (new_night_guard ['formofpayment'] == ""):
        return jsonify ("Erro: Incorrect formofpayment."), 400
    
    if ('dateofpayment' not in new_night_guard) or (new_night_guard ['dateofpayment'] == ""):
        return jsonify ("Erro: Incorrect dateofpayment."), 400
    
    if ('neighborhood' not in new_night_guard) or (new_night_guard ['district'] == ""):
        return jsonify ("Erro: Incorrect neighborhood."), 400
    
    
    for night_guard in night_guards:
        if (new_night_guard['id'] == night_guards['id']):
            return jsonify("Erro, um guarda noturno com esse id ja esta cadastrado!"), 409 

    night_guards.append(new_night_guard)

    return jsonify(night_guards)

@app.route("/neighborhood", methods=["GET"]) 
def get_neighborhood ():

    name = request.args.get("name", None)
    page = int(request.args.get("page", None))
    limit = int(request.args.get("limit", None))
    vehicle = request.args.get("vehicle", None)
    licenseplate = request.args.get("licenseplate", None)
    email = request.args.get("email", None)
    cpf = request.args.get("cpf", None)
    dateofbirth = request.args.get("dateofbirth", None)
    formofpayment = request.args.get("formofpayment", None)
    dateofpayment = request.args.get("dateofpayment", None)
    district = request.args.get("district", None)
    page = int(request.args.get("page", None))
    limit = int(request.args.get("limit", None))

    start = limit * (page - 1)
    end = start + limit 

    retorno = []

    for neighborhood in neighborhoods:
        if name and name == neighborhood ["name"]:
            retorno.append(neighborhoods)
        elif not name:
            retorno.append(neighborhoods)

    return jsonify (retorno[start:end])  

@app.route("/students/<int:id>", methods=["PUT"]) 
def put_students (id):

    update_neighborhood = request.get_json()

    i = 0

    for neighborhood in neighborhoods: # Outra maneira de usar o contador seria: for x in enumerate(students):
        if (id == neighborhood["id"]):
            neighborhood[i].update(update_neighborhood)
            return jsonify(update_neighborhood)
        i+=1
    return jsonify("Erro: Bairro não encontrado", 404) 

@app.route("/neighborhood/<int:id>", methods = ["DELETE"]) # Rota DELETE   
def del_neighborhood (id):

    for x in enumerate(neighborhoods):
        if(id == neighborhoods["id"]):
            del neighborhoods[id]
            return jsonify(neighborhoods)
    return ("Erro, Bairro não encontrado"), 404

@app.route("//<int:id>", methods = ["GET"]) # Rota GET de um UNICO aluno 
def get_students_by_id (id):

    i = 0
    for neighborhood in neighborhoods:
        if(id == neighborhoods["id"]):
            return jsonify(neighborhoods[i])
        i+=1
    return ("Erro, Bairro não encontrado"), 404

app.run(debug=True)

