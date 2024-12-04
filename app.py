from Flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template,request,url_for
#inizializza l'app Flask
app = Flask(__name__)

#rotta principale
@app.route('/')
def home():
    return render_template('index.html')

#avvio dell'app Flask
if __name__ == '__main__':
   app.run(debug=True) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()
   
lista_spesa = []
global lista_spesa

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))


@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice)
    return redirect(url_for('home'))    

@app.route('/svuota_lista', methods=['POST'])
def svuota_lista():
     lista_spesa.clear()
return redirect(url_for('home'))

