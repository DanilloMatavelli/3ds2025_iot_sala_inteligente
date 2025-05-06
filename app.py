import hashlib
from flask import Flask, jsonify, render_template, request, redirect, session, flash
import datetime

app = Flask(__name__)

situacao_lampada = ""
situacao_led = ""



# Para abrir a página HTML
@app.route("/")
@app.route("/lampada")
def pagina_lampada():
    return render_template("pagina_lampada.html")
    

# Para abrir a página led
@app.route("/led")
def pagina_dashboard():
    return render_template("pagina_led.html")

# Rota post para o fotoressitor acessar e nela aparecer que a Lâmpada está ligada no HTML
@app.route("/post/lampada/ligada")
def post_lampada_ligada():
    global situacao_lampada
    situacao_lampada = "LIGADO"
    return jsonify ({"mensagem": "Alterado para LIGADO"})

# Rota post para o fotoressitor acessar e nela aparecer que a Desligada está ligada no HTML
@app.route("/post/lampada/desligada")
def post_lampada_desligada():
    global situacao_lampada
    situacao_lampada = "DESLIGADO"
    return jsonify ({"mensagem": "Alterado para DESLIGADO"})

@app.route("/get/estado_lampada")
def get_estado_lampada():
    global situacao_lampada
    return jsonify({"ESTADO_LAMPADA" : situacao_lampada})

# Rota para acender ou desligar o led

# Rota led ligado
@app.route("/post/led/ligado")
def led_ligado():
    global situacao_led
    situacao_led = "LIGADO"
    return jsonify({"ESTADO_LED" : situacao_led})

# Rota Led Desligado
@app.route("/post/led/desligado")
def led_desligado():
    global situacao_led
    situacao_led = "DESLIGADO"
    return jsonify({"ESTADO_LED" : situacao_led})

# Estado Do Led
@app.route("/post/estado_led")
def get_estado_lampada():
    return render_template('pagina_led.html')

@app.route("/api/estado_led", methods = ["GET", "POST"])
def situacao_led_api():
    return jsonify({"o estado é": situacao_led})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)