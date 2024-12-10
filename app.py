from Flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template,request,url_for
#inizializza l'app Flask
app = Flask(__name__)

#rotta principale
@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all() #recupera tutti i dati dalle query 
return render_template('home.html', lista=lista_spesa) #li passa all'html per visualizzarli 

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
        nuovo_elemento = ListaSpesa(elemento=elemento) #crea un nuovo elemento a lista spesa 
        db.session.add(nuovo_elemento) #lo aggiunge al server sqlalchemy
        db.session.commit() #salva
    return redirect(url_for('home'))


@app.route('/rimuovi/<int:indice>', methods=['POST'])
@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    elemento = ListaSpesa.query.get_or_404(indice) #prende un elemento dalla lista spesa 
    db.session.delete(elemento) #cancella l'elemento dal server sqlalchemy
    db.session.commit() #salva
return redirect(url_for('home'))    

@app.route('/svuota_lista', methods=['POST'])
def svuota_lista():
     lista_spesa.clear()
return redirect(url_for('home'))

