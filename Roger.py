from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/neighborhood", methods=["GET"]) 
def get_neighborhood ():

    name = request.args.get("name", None)
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

