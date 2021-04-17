from flask import Flask, render_template, request, json, url_for, redirect
from flaskext.mysql import MySQL
import hashlib
import random
app = Flask(__name__)

app.config["DEBUG"] = True
app.config['MYSQL_DATABASE_USER'] = 'sepherot_jonathan'
app.config['MYSQL_DATABASE_PASSWORD'] = 'fL9WD0vDyZ'
app.config['MYSQL_DATABASE_DB'] = 'sepherot_jonathanBD'
app.config['MYSQL_DATABASE_HOST'] = 'nemonico.com.mx'
mysql = MySQL(app)



def validar(_correoL, _contrasenaL):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlvalidarProcedure = "SELECT email FROM USERS where email= ""'"+_correoL+"'"
        cursor.execute(sqlvalidarProcedure)
        data = cursor.fetchall()
        sqlvalidar2Procedure = "SELECT password FROM USERS where email= ""'"+_correoL+"'"
        cursor.execute(sqlvalidar2Procedure)
        data2 = cursor.fetchall()
        
        data2 =str(data2)
        _contrasenaL= str("(('"+_contrasenaL+"',),)")
        print (data2)
        print (_contrasenaL)

        if data2 == _contrasenaL:
            print("bien")
            return True

        else:
            print("mal")
            return False

    except:
        return "<h1>algo salió mal</h1>"
        
    finally:
        cursor.close()
        conn.close()



def insertaruser( _nombre, _apellido, _correo, _celular, _contraseña):
    try: 
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA="USERS"

        contraseña_cifrada = hashlib.sha512(_contraseña.encode())
        print("ya hizo el hash")
        _salt=str(random.randrange(10000, 99999))
        _contraseña=(contraseña_cifrada.hexdigest()+_salt)
        
        sqlDropProcedure="DROP PROCEDURE IF EXISTS Insertaruser;"
        cursor.execute(sqlDropProcedure)
        sqlCreateSP="CREATE PROCEDURE Insertaruser(IN name VARCHAR(60), IN last_name VARCHAR(60), IN email VARCHAR(60), IN cellphone int(100), IN password VARCHAR(400),IN SALT VARCHAR(100), IN sessions int(100)) INSERT INTO "+_TABLA+" (name, last_name, email, cellphone, password, SALT, sessions) VALUES( ""'"+_nombre+"'""," "'"+_apellido+"'" "," "'"+_correo+ "'""," "'"+_celular+"'"","  "'"+_contraseña+ "'"","  "'"+_salt+ "'"", 1)"
        print(sqlCreateSP)
        cursor.execute(sqlCreateSP)
        cursor.callproc('Insertaruser',(_nombre, _apellido, _correo, _celular, _contraseña, _salt, "1"))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return True
        else:
            return False
      

    except:
        return "<h1>algo salió mal</h1>"
    finally:
       cursor.close() 
       conn.close()
  




def SelectAll(_p):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure =" SELECT p.id_post, p.name, p.email, p.age, p.address, p.career, p.school, p.average, p.languages, p.experience, p.courses, p.cellphone, p.aptitudes, c.tittle, p.estatus, p.cv, p.coments, p.compatibility, p.wordskey FROM POSTULANT p INNER JOIN CREATE_EMP c ON p.vacancy=c.id_cemp WHERE p.vacancy = '"+_p+"' AND (p.estatus = 'Registrado' OR p.estatus = 'Entrevistado')"
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        return data
    except:
        return "<h1>algo salió mal</h1>" 
    finally:
        cursor.close()
        conn.close()


def buscarU(_user):
    if _user:
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM USERS WHERE email = '"+_user+"'"
        try: 
            cursor.execute(query,(_user))
            data = cursor.fetchall()
            if data:
                return data[0][2]
            else:
                return False
        except:
            cursor.close()
            conn.close()
            return "<h1>algo salió mal</h1>" 
            
    else: 
            return "<h1>algo salió mal</h1>"  



