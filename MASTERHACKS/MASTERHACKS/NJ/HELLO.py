from flask import Flask, render_template, request, json, url_for, redirect,send_from_directory,  g, session 
from flaskext.mysql import MySQL
import Modelo as Modelo
import os


app = Flask(__name__)

app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL']= False
app.config['MAIL_USE_TLS']= True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.before_request
def before_request():
   g.user = None
   if 'user' in session:
      g.user = Modelo.buscarU(session['user'])

@app.route("/",methods=['POST','GET'])
def index():
    try:
        return render_template("index.html")
    except:
        return "<h1>algo salió mal</h1>"

@app.route("/quintanaroo",methods=['POST','GET'])
def quin():
    try:
        return render_template("quintanaroo.html")
    except:
        return "<h1>algo salió mal</h1>"

@app.route("/yucatan",methods=['POST','GET'])
def yuca():
    try:
        return render_template("yucatan.html")
    except:
        return "<h1>algo salió mal</h1>"

@app.route("/baja",methods=['POST','GET'])
def baja():
    try:
        return render_template("baja.html")
    except:
        return "<h1>algo salió mal</h1>"

@app.route("/destinos",methods=['POST','GET'])
def destinos():
    try:
        return render_template("destinos.html")
    except:
        return "<h1>algo salió mal</h1>"


@app.route("/login",methods=['POST','GET'])
def mainn():
    try:
        return render_template("main.html")
    except:
        return "<h1>algo salió mal</h1>"






@app.route('/login',methods=['GET','POST'])
def lo():
    try:
        if g.user:
            session.pop('user', None)

        if request.method=='POST':
           
            user = request.form['correoL']
            _contrasenaL = request.form['contrasenaL']
            _bool=Modelo.validar(user, _contrasenaL)
            session['user'] = user
   
        if _bool == True:
            session['user'] = user
            print ("contraseña correcta")
            return redirect(url_for('principall'))
            

        if _bool == False:
            session['user'] = user
            print ("contraseña incorrecta")
            return render_template('main.html', alert='Tu contraseña o usuario es incorrecto') 
    except:
        return redirect(url_for('mainn')) 
            
    finally:
            print("Lets go!")

if __name__ == "__main__":
    app.run()
