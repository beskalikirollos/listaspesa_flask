@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all() #COMMENTA
return render_template('home.html', lista=lista_spesa)