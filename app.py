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


# Rota POST Nightguard
app.route("/post_nightguard", methods=["POST"])(post_nightguards)

# Rota DELETE para o guarda noturno
app.route("/night_guards/<int:id>", methods=["DELETE"])

# Rota POST Bairros
app.route("/neighborhoods", methods=["POST"])

# Rota GET para todos os bairros
app.route("/get_neighborhood", methods=["GET"])(get_neighborhood)

# Rota GET para a leitura geral dos setores
app.route("/sector", methods=["GET"]) # Rota GET

# Rota GET para um UNICO setor
app.route("/sectors/<int:id>", methods = ["GET"])(get_sectors_by_id)

