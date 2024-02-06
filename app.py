from flask import Flask, request
from controllers.controller_administrators import set_administrators, del_administrators
from controllers.controller_neighborhood import get_neighborhood, get_neighborhoods_by_id
from controllers.controller_nightguards import post_nightguards, get_nightguards
from controllers.controller_sectors import get_sectors_by_id, put_sectors

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


app.run(debug=True)