from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'clavesecreta'  


usuarios = {'administrador': 'contraseña147', 'usuario1': 'mi contraseña'}

@app.route('/')
def home():
   
    if 'usuario' in session:
        return redirect(url_for('bienbenido'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        
        # Verificación del nombre de usuario y contraseña
        if usuario in usuarios and usuarios[usuario] == contraseña:
            session['usuario'] = usuario  # Almacenar el nombre de usuario en la sesión
            return redirect(url_for('bienvenida'))
        else:
            flash('Nombre de usuario o contraseña incorrectos')
    
    return render_template('login.html')

@app.route('/bienvenida')
def bienvenida():
    if 'usuario' in session:
        usuario = session['usuario']
        return render_template('bienvenido.html', usuario=usuario)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)  # Cerrar sesión
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)
