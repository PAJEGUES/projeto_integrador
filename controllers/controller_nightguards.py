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