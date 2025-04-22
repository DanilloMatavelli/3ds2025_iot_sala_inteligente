import hashlib
from flask import Flask, jsonify, render_template, request, redirect, session, flash
import datetime
import mysql.connector
from data.conexao import Conexao

app = Flask(__name__)

situacao_lampada = ""

# Para abrir a página HTML
@app.route("/")
@app.route("/lampada")
def pagina_dashboard():
    return render_template("pagina_lampada.html")

# Rota post para o fotoressitor acessar e nela aparecer que a Lâmpada está ligada no HTML
@app.route("/post/lampada/ligada"  , methods = ["POST"])
def post_lampada_ligada():
    return render_template("pagina_lampada.html", situacao_lampada = "Lampada Está Ligada")

# Rota post para o fotoressitor acessar e nela aparecer que a Desligada está ligada no HTML
@app.route("/post/lampada/desligada"  , methods = ["POST"])
def post_lampada_desligada():
    return render_template("pagina_lampada.html", situacao_lampada = "lampada_desligada")

# Para iniciar o app
app.run()