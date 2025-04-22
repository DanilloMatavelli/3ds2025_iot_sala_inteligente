import hashlib
from flask import Flask, jsonify, render_template, request, redirect, session, flash
import datetime
import mysql.connector
from data.conexao import Conexao

app = Flask(__name__)

@app.route("/")
@app.route("/dashboard")
def pagina_dashboard():
    return render_template("dashboard.html")

@app.route("/lampada/ligada")
def post_lampada_ligada():
    return render_template("dashboard.html")


# Para iniciar o app
app.run()