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
    return f"A LÂMPADA ESTÁ {situacao_lampada}"

# Rota post para o fotoressitor acessar e nela aparecer que a Lâmpada está ligada no HTML
@app.route("/post/lampada/ligada")
def post_lampada_ligada():
    global situacao_lampada
    situacao_lampada = "LIGADO"
    return f"A lampada está {situacao_lampada}"

# Rota post para o fotoressitor acessar e nela aparecer que a Desligada está ligada no HTML
@app.route("/post/lampada/desligada")
def post_lampada_desligada():
    global situacao_lampada
    situacao_lampada = "DESLIGADO"
    return f"A lampada está {situacao_lampada}"


# Para iniciar o app
app.run()