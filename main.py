from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'comentariospython'
mysql = MySQL(app)
app.secret_key = 'TDg2nuhrssñkos'

@app.route('/', methods = ['GET', 'POST'])
def principal():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM comentarios')
    dato = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return render_template('index.html', dato = dato)

# app.route('/delete/<id>')
# def delete(id):
#     cursor = mysql.connection.cursor()
#     cursor.execute('DELETE FROM comentarios WHERE id = 0',(id))
#     mysql.connection.commit()
#     cursor.close()
#     return render_template('index.html')


@app.route("/delete/<string:id>")
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM comentarios WHERE id = {0}'.format(id))
    mysql.connection.commit()
    return redirect(url_for('principal'))

@app.route('/comentar', methods = ['GET', 'POST'])
def comentar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        comentario = request.form['comentariousuario']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO comentarios (nombre, correo, comentario) VALUES (%s,%s,%s)',(nombre, correo, comentario))
        mysql.connection.commit()
    return redirect(url_for("principal"))

if __name__ == '__main__':
    app.run(debug=True)