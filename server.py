from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def table():

    users = [
        {'Nombre' : 'Michael', 'Apellido' : 'Choi'},
        {'Nombre' : 'John', 'Apellido' : 'Supsupin'},
        {'Nombre' : 'Mark', 'Apellido' : 'Guillen'},
        {'Nombre' : 'KB', 'Apellido' : 'Tonel'}
    ]
    
    return render_template('index.html', personas = users)



if __name__== "__main__":
    app.run(debug=True)