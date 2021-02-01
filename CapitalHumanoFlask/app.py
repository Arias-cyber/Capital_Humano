import os

from flask import Flask, render_template, request, url_for, Response, send_from_directory
from flask_migrate import Migrate
from werkzeug.utils import redirect, secure_filename

from database import db
from forms import EmpleadoForm, SindicatoForm, ObraSocialForm, ChoiceSindForm, ChoiceOSForm, AptitudForm, FormacionForm
from models import Empleado, Img, Sindicato, ObraSocial, Aptitud, Formacion_Academica

app = Flask(__name__)

#configuracion de la bd
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'CHumano'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['UPLOAD_FOLDER'] = 'C:/Cursos/Flask/CapitalHumanoFlask/FotosEmpleados'

# inicializacion del objeto db de sqlalchemy
db.init_app(app)


#configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

#configuracon de flask-wtf
app.config['SECRET_KEY']='llave_secrete'





@app.route('/')
@app.route('/index')
@app.route('/index.html')

def inicio():
    #Listado de empleados
    empleados = Empleado.query.all()
    #personas = Persona.query.order_by('id')
    total_empleados = Empleado.query.count()
    app.logger.debug(f'Listado Empleados: {empleados}')
    app.logger.debug(f'Total Empleados: {total_empleados}')
    return  render_template('index.html', empleados= empleados, total_empleados= total_empleados)

@app.route('/ver/<int:legajo>')
def ver_detalle(legajo):

    #recuperamos la persona segun el id proporcionado
    #persona = Persona.query.get(id)
    empleado = Empleado.query.get_or_404(legajo)
    app.logger.debug(f'Ver Empleado: {empleado}')

    cant = db.session.query(Sindicato).filter(
        Sindicato.subscribers.any(Empleado.legajo == legajo)
    ).all()

    can = db.session.query(ObraSocial).filter(
        ObraSocial.subscriber.any(Empleado.legajo == legajo)
    ).all()

   # print (f"Todos los departamentos donde trabaja {legajo}")
    #for n in cant:
        #print("Sindicato: {}".format(n.nombre))

    #print (f"Todos los todos las Obras sociales donde se encuentra: {legajo}")
    #for c in can:
        #print("ObraSocial: {}".format(c.nombre))

    return  render_template('detalle.html', empleado = empleado, cant=cant, can = can)

@app.route('/agregar', methods=['GET','POST'])
def agregar():
    empleado = Empleado()
    empleadoForm = EmpleadoForm(obj=empleado) #indico el modelo a que asociado
    print('Esto es antes del if')
    if request.method == 'POST':
        if empleadoForm.validate_on_submit():
           empleadoForm.populate_obj(empleado)
           app.logger.debug(f'empleado a insertar: {empleado}')
           #Insertamos el nuevo registro
           db.session.add(empleado)
           db.session.commit()
           return redirect(url_for('inicio'))
    return render_template('agregar.html', forma = empleadoForm)




@app.route('/editar/<int:legajo>', methods=['POST','GET'])
def editar(legajo):
    #recuoeramos el objeto personaa editar
    empleado = Empleado.query.get_or_404(legajo)
    empleadoForma = EmpleadoForm(obj=empleado)
    if request.method == 'POST':
        if empleadoForma.validate_on_submit():
            empleadoForma.populate_obj(empleado)
            app.logger.debug(f'Empleado a actualizar: {empleado}')
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html', forma = empleadoForma)

@app.route('/eliminar/<int:legajo>')
def eliminar(legajo):
    empleado = Empleado.query.get_or_404(legajo)
    app.logger.debug(f'Empleado a eliminar: {empleado}')
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route("/upload/<int:legajo>", methods=['POST', 'GET'])
def uploader(legajo):
     if request.method == 'POST':
      # obtenemos el archivo del input "archivo"
      f = request.files['pic']
      filename = secure_filename(f.filename)
      # Guardamos el archivo en el directorio "Archivos PDF"
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


      pic = request.files['pic']
      if not pic:
          return 'No pic uploaded!', 400

      filename = secure_filename(pic.filename)
      mimetype = pic.mimetype
      if not filename or not mimetype:
          return 'Bad upload!', 400

      img = Img(name=filename, mimetype=mimetype, emp_legajo=legajo)
      db.session.add(img)
      db.session.commit()
      return "<h1>Archivo subido exitosamente</h1>"

     return render_template('formulario.html')

@app.route('/ver/imagen/<int:legajo>')
def get_img(legajo):
    img = Img.query.filter_by(emp_legajo=legajo).first()
    if not img:
        return 'Img Not Found!', 404

    return render_template('mostrarImagen.html', name = img.name)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("FotosEmpleados", filename)

#Todo lo relacionado con clase sindicato

@app.route('/cargarSindicato', methods=['GET','POST'])
def up_sind():
    sindicato = Sindicato()
    sindicatoForm = SindicatoForm(obj=sindicato)
    if request.method == 'POST':
        if sindicatoForm.validate_on_submit():
            sindicatoForm.populate_obj(sindicato)
            app.logger.debug(f'Sindicato a insertar: {sindicato}')
            db.session.add(sindicato)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarSindicato.html', forma = sindicatoForm)

@app.route('/editarSindicato/<int:id>', methods=['POST','GET'])
def editarSin(id):
    #recuoeramos el objeto personaa editar
    sindicato = Sindicato.query.get_or_404(id)
    sindicatoForma = SindicatoForm(obj=sindicato)
    if request.method == 'POST':
        if sindicatoForma.validate_on_submit():
            sindicatoForma.populate_obj(sindicato)
            app.logger.debug(f'Empleado a actualizar: {sindicato}')
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarSindicato.html', forma = sindicatoForma)

@app.route('/eliminarSindicato/<int:id>')
def eliminarSin(id):
    sindicato = Sindicato.query.get_or_404(id)
    app.logger.debug(f'Empleado a eliminar: {sindicato}')
    db.session.delete(sindicato)
    db.session.commit()
    return redirect(url_for('inicio'))


#Todo lo relacionado con clase obra social

@app.route('/cargarObraSocial', methods=['GET','POST'])
def up_obra_soc():
    obra_social = ObraSocial()
    obraSocialForm = ObraSocialForm(obj=obra_social)
    if request.method == 'POST':
        if obraSocialForm.validate_on_submit():
            obraSocialForm.populate_obj(obra_social)
            app.logger.debug(f'Sindicato a insertar: {obra_social}')
            db.session.add(obra_social)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarObraSocial.html', forma = obraSocialForm)

@app.route('/editarObraSocial/<int:id>', methods=['POST','GET'])
def editar_obra_soc(id):
    #recuoeramos el objeto personaa editar
    obra_social = ObraSocial.query.get_or_404(id)
    obraSocialForm = ObraSocialForm(obj=obra_social)
    if request.method == 'POST':
        if obraSocialForm.validate_on_submit():
            obraSocialForm.populate_obj(obra_social)
            app.logger.debug(f'Empleado a actualizar: {obra_social}')
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarObraSocial.html', forma = obraSocialForm)

@app.route('/eliminarObraSocial/<int:id>')
def eliminar_obra_social(id):
    obra_social = ObraSocial.query.get_or_404(id)
    app.logger.debug(f'Empleado a eliminar: {obra_social}')
    db.session.delete(obra_social)
    db.session.commit()
    return redirect(url_for('inicio'))


#todo lo relacionado con sindicato



@app.route('/ver/prueba/<int:legajo>', methods=['GET', 'POST'])
def selectSind(legajo):
    form = ChoiceSindForm()

#    form.opts.query = Sindicato.query.filter(Sindicato.id > 1)


    if request.method == 'POST':
        if form.validate_on_submit():
          #return '<html><h1>{}</h1></html>'.format(form.opts.data)
          name = request.form['opts']
          nom = request.form['optos']
          sindicato = Sindicato.query.get_or_404(name)
          obrasocial= ObraSocial.query.get_or_404(nom)
          emple = Empleado.query.get_or_404(legajo)
          sindicato.subscribers.append(emple)
          obrasocial.subscriber.append(emple)
          #sindicato = Sindicato(nombre=sindicato.nombre, telefono=sindicato.telefono, domicilio=sindicato.domicilio, sind_legajo=legajo)
          #db.session.update(sindicato)
          db.session.commit()


          return "<h1>Cargado con exito</h1>"

    return render_template('pruebaSelect.html', form=form)


#Todo sobre aptitudes
### Llegue a la conclusion de que se debe cambiar la relacion entre aptitud y empleado a una de muchos a muchos

@app.route('/aptitudes/listarAptitudes')
def listadoDeAptitudes():
    aptitudes = Aptitud.query.all()
    total_aptitudes = Aptitud.query.count()
    app.logger.debug(f'Listado aptitudes: {aptitudes}')
    app.logger.debug(f'Total Empleados: {total_aptitudes}')
    return  render_template('listarAptitudes.html', aptitudes= aptitudes, total_aptitudes= total_aptitudes)

@app.route('/aptitudes/agregarAptitud',methods=['GET','POST']) 
def cargar_aptitud():
    aptitud = Aptitud()
    aptitudForm= AptitudForm(obj=aptitud)
    if request.method == 'POST':
        if aptitudForm.validate_on_submit():
            aptitudForm.populate_obj(aptitud)
            app.logger.debug(f'Aptitud a cargar: {aptitud}')
            db.session.add(aptitud)
            db.session.commit()
            return redirect(url_for('listadoDeAptitudes'))
    return render_template('agregarAptitud.html',form = AptitudForm())


@app.route('/aptitudes/editarAptitud/<int:id>', methods=['POST','GET'])
def editarAptitud(id):
    aptitud = Aptitud.query.get_or_404(id)
    aptitudForma = AptitudForm(obj=aptitud)
    if request.method == 'POST':
        if aptitudForma.validate_on_submit():
            aptitudForma.populate_obj(aptitud)
            app.logger.debug(f'Aptitud a actualizar: {aptitud}')
            db.session.commit()
            return redirect(url_for('listadoDeAptitudes'))
    return render_template('editarAptitud.html', form = aptitudForma)



@app.route('/aptitudes/eliminar/<int:id>')
def eliminarAptitud(id):
    aptitud = Aptitud.query.get_or_404(id)
    app.logger.debug(f'Aptitud a eliminar: {aptitud}')
    db.session.delete(aptitud)
    db.session.commit()
    return redirect(url_for('listadoDeAptitudes'))



@app.route('/aptitudes/ver/<int:id>')
def verAptitud(id):
    aptitud = Aptitud.query.get_or_404(id)
    app.logger.debug(f'Ver Aptitud: {aptitud}')
    return  render_template('verAptitud.html', aptitud = aptitud)



#Todo sobre formacion academica

@app.route('/formacion/listarFormaciones')
def listadoDeFormaciones():
    formaciones = Formacion_Academica.query.all()
    total_formaciones = Formacion_Academica.query.count()
    app.logger.debug(f'Listado formaciones: {formaciones}')
    app.logger.debug(f'Total Empleados: {total_formaciones}')
    return  render_template('listarFormaciones.html', formaciones= formaciones, total_formaciones= total_formaciones)


@app.route('/formacion/agregarFormacion',methods=['GET','POST']) 
def cargar_formacion():
    formacion_academica = Formacion_Academica()
    formacionForm= FormacionForm(obj=formacion_academica)
    if request.method == 'POST':
        if formacionForm.validate_on_submit():
            formacionForm.populate_obj(formacion_academica)
            app.logger.debug(f'Formacion a cargar: {formacion_academica}')
            db.session.add(formacion_academica)
            db.session.commit()
            return redirect(url_for('listadoDeFormaciones'))
    return render_template('agregarFormacion.html',form = FormacionForm())


@app.route('/formacion/editarFormacion/<int:id>', methods=['POST','GET'])
def editarFormacion(id):
    formacion_academica = Formacion_Academica.query.get_or_404(id)
    formacionForm = FormacionForm(obj=formacion_academica)
    if request.method == 'POST':
        if formacionForm.validate_on_submit():
            formacionForm.populate_obj(formacion_academica)
            app.logger.debug(f'Formacion a actualizar: {formacion_academica}')
            db.session.commit()
            return redirect(url_for('listadoDeFormaciones'))
    return render_template('editarFormacion.html', form = formacionForm)


@app.route('/formacion/eliminar/<int:id>')
def eliminarFormacion(id):
    formacion_academica = Formacion_Academica.query.get_or_404(id)
    app.logger.debug(f'Formacion a eliminar: {formacion_academica}')
    db.session.delete(formacion_academica)
    db.session.commit()
    return redirect(url_for('listadoDeFormaciones'))



@app.route('/formacion/ver/<int:id>')
def verFormacion(id):
    formacion_academica = Formacion_Academica.query.get_or_404(id)
    app.logger.debug(f'Ver Formacion: {formacion_academica}')
    return  render_template('verFormacion.html', formacion = formacion_academica)
