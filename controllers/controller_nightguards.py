from flask import Flask, request, jsonify

night_guards = [
    
    {
        "id": 1,
        "name": "Jose",
        "vehicle": "Titan 150",
        "licenseplate": "ABC-1234",
        "email": "victormconsolaro18@gmail.com",
        "password": "caixadeuva",
        "cpf": "123.456.789-00",
        "dateofbirth": "12/12/2002",
        "formofpayment": "PIX",
        "dateofpayment": "05",
        "neighborhood": "Maria Estella Faga"
    },

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

def get_nightguards ():

    name = request.args.get("name", None)
    vehicle = request.args.get("vehicle", None)
    licenseplate = request.args.get("licenseplate", None)
    email = request.args.get("email", None)
    cpf = request.args.get("cpf", None)
    dateofbirth = request.args.get("dateofbirth", None)
    formofpayment = request.args.get("formofpayment", None)
    dateofpayment = request.args.get("dateofpayment", None)
    neighborhood = request.args.get("neighborhood", None)
    page = int(request.args.get("page", None))
    limit = int(request.args.get("limit", None))
    id = request.args.get("id", None)

    if id:
        id = int(id)

    start = limit * (page - 1)
    end = start + limit 

    vector_name = []
    vector_vehicle = []
    vector_licenseplate = []
    vector_email = []
    vector_cpf = []
    vector_dateofbirth = []
    vector_formofpayment = []
    vector_dateofpayment = []
    vector_neighborhood = []
    vector_id = []

    for night_guard in night_guards:

        if name and name == night_guard ["name"]:
            vector_name.append(night_guard)
        elif not name:
            vector_name.append(night_guard)

    for night_guard in vector_name:

        if vehicle and vehicle == vector_name ["vehicle"]:
            vector_vehicle.append(night_guard)
        elif not vehicle:
            vector_vehicle.append(night_guard)
    
    for night_guard in vector_vehicle:

        if licenseplate and licenseplate == vector_vehicle ["licenseplate"]:
            vector_licenseplate.append(night_guard)
        elif not licenseplate:
            vector_licenseplate.append(night_guard)

    for night_guard in vector_licenseplate:

        if email and email == vector_licenseplate ["email"]:
            vector_email.append(night_guard)
        elif not email:
            vector_email.append(night_guard)

    for night_guard in vector_email:

        if cpf and cpf == vector_email ["cpf"]:
            vector_cpf.append(night_guard)
        elif not cpf:
            vector_cpf.append(night_guard)

    for night_guard in vector_cpf:

        if dateofbirth and dateofbirth == vector_cpf ["dateofbirth"]:
            vector_dateofbirth.append(night_guard)
        elif not dateofbirth:
            vector_dateofbirth.append(night_guard)

    for night_guard in vector_dateofbirth:

        if formofpayment and formofpayment == vector_dateofbirth ["formofpayment"]:
            vector_formofpayment.append(night_guard)
        elif not formofpayment:
            vector_formofpayment.append(night_guard)

    for night_guard in vector_formofpayment:

        if dateofpayment and dateofpayment == vector_formofpayment ["dateofpayment"]:
            vector_dateofpayment.append(night_guard)
        elif not dateofpayment:
            vector_dateofpayment.append(night_guard)

    for night_guard in vector_dateofpayment:

        if neighborhood and neighborhood == vector_dateofpayment ["neighborhood"]:
            vector_neighborhood.append(night_guard)
        elif not neighborhood:
            vector_neighborhood.append(night_guard)
    
    for night_guard in vector_neighborhood:

        if id and id == vector_neighborhood ["id"]:
            vector_id.append(night_guard)
        elif not neighborhood:
            vector_id.append(night_guard)

    return jsonify (vector_id[start:end])  # Os dois pontos indicam "até", nesse caso, retorno do início até o fim 


def post_nightguards ():
    post_nightguards = request.get_json()
            
    if ('name' not in post_nightguards) or (post_nightguards ['name'] == ""):
        return jsonify ("Erro: Incorrect login."), 400
    
    if ('vehicle' not in post_nightguards) or (post_nightguards ['vehicle'] == ""):
        return jsonify ("Erro: Incorrect vehicle."), 400
    
    if ('licenseplate' not in post_nightguards) or (post_nightguards ['licenseplate'] == ""):
        return jsonify ("Erro: Incorrect licenseplate."), 400
    
    if ('email' not in post_nightguards) or (post_nightguards ['password'] == ""):
        return jsonify ("Erro: Incorrect password."), 400
    
    if ('password' not in post_nightguards) or (post_nightguards ['name'] == ""):
        return jsonify ("Erro: Incorrect login."), 400
    
    if ('cpf' not in post_nightguards) or (post_nightguards ['cpf'] == ""):
        return jsonify ("Erro: Incorrect cpf."), 400
    
    if ('dateofbirth' not in post_nightguards) or (post_nightguards ['dateofbirth'] == ""):
        return jsonify ("Erro: Incorrect dateofbirth."), 400
    
    if ('formofpayment' not in post_nightguards) or (post_nightguards ['formofpayment'] == ""):
        return jsonify ("Erro: Incorrect formofpayment."), 400
    
    if ('dateofpayment' not in post_nightguards) or (post_nightguards ['dateofpayment'] == ""):
        return jsonify ("Erro: Incorrect dateofpayment."), 400
    
    if ('neighborhood' not in post_nightguards) or (post_nightguards ['district'] == ""):
        return jsonify ("Erro: Incorrect neighborhood."), 400
    
    
    for night_guard in night_guards:
        if (post_nightguards['id'] == night_guards['id']):
            return jsonify("Erro, um guarda noturno com esse id ja esta cadastrado!"), 409 

    night_guards.append(post_nightguards)

    return jsonify(night_guards)

def put_night_guards (id):

    update_night_guards = request.get_json()

    i = 0

    for night_guard in night_guards: 
        if (id == night_guard["id"]):
            night_guards[i].update(update_night_guards)
            return jsonify(update_night_guards)
        i+=1
    return jsonify("Erro: Setor não encontrado"), 404

