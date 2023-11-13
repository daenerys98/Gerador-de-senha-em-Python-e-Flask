from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tamanho = int(request.form.get("tamanho", 8))  # Se não for escolhido a senha, por padrão fica 8
        
        if "gerador" in request.form:
            caracteres = string.ascii_letters + string.digits
            sequencia = ''.join(random.choice(caracteres) for _ in range(tamanho))
            return render_template("index.html", sequencia=sequencia)

    return render_template("index.html", sequencia=None)

if __name__ == "__main__":
    app.run(debug=True)