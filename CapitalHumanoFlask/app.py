from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from werkzeug.utils import redirect

from database import db
from forms import EmpleadoForm
from models import Empleado

app = Flask(__name__)

# configuracion de la bd
USER_DB = 'postgres'
PASS_DB = '1234'
URL_DB = 'localhost'
NAME_DB = 'capital_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicializacion del objeto db de sqlalchemy
db.init_app(app)


# configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

# configuracon de flask-wtf
app.config['SECRET_KEY'] = 'llave_secrete'


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    # Listado de empleados
    empleados = Empleado.query.all()
    #personas = Persona.query.order_by('id')
    total_empleados = Empleado.query.count()
    app.logger.debug(f'Listado Empleados: {empleados}')
    app.logger.debug(f'Total Empleados: {total_empleados}')
    return render_template('index.html', empleados=empleados, total_empleados=total_empleados)


@app.route('/ver/<int:legajo>')
def ver_detalle(legajo):

    # recuperamos la persona segun el id proporcionado
    #persona = Persona.query.get(id)
    empleado = Empleado.query.get_or_404(legajo)
    app.logger.debug(f'Ver Empleado: {empleado}')
    return render_template('detalle.html', empleado=empleado)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():

    empleado = Empleado()
    # indico el modelo a que asociado
    empleadoForm = EmpleadoForm(obj=empleado)
    if request.method == 'POST':
        if empleadoForm.validate_on_submit():
            empleadoForm.populate_obj(empleado)
            app.logger.debug(f'empleado a insertar: {empleado}')
            # Insertamos el nuevo registro
            db.session.add(empleado)

            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html', forma=empleadoForm)


@app.route('/editar/<int:legajo>', methods=['POST', 'GET'])
def editar(legajo):
    # recuoeramos el objeto personaa editar
    empleado = Empleado.query.get_or_404(legajo)
    empleadoForma = EmpleadoForm(obj=empleado)
    if request.method == 'POST':
        if empleadoForma.validate_on_submit():
            empleadoForma.populate_obj(empleado)
            app.logger.debug(f'Empleado a actualizar: {empleado}')
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html', forma=empleadoForma)


@app.route('/eliminar/<int:legajo>')
def eliminar(legajo):
    empleado = Empleado.query.get_or_404(legajo)
    app.logger.debug(f'Empleado a eliminar: {empleado}')
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('inicio'))
