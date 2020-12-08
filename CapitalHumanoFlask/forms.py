from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, DateTimeField, FileField
from wtforms.validators import DataRequired
from wtforms import validators


class EmpleadoForm(FlaskForm):
    dni = IntegerField('DNI')
    legajo = IntegerField('Legajo')
    telefono = IntegerField('Telefono')
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido',validators=[validators.length(min=4,max=25,message="Ingrese un apellido con entre 4 y 25 caracteres")])
    domicilio = StringField('Domicilio')
    fecha_ingreso = DateTimeField('Fecha de ingreso', format='%d/%m/%Y')
    fecha_salida = DateTimeField('Fecha de salida', format='%d/%m/%Y')
    fecha_nacimiento = DateTimeField('Fecha de nacimiento', format='%d/%m/%Y')
    fecha_cese = DateTimeField('Fecha de cese', format='%d/%m/%Y')
    estado_general = StringField('Estado general')
    sexo = StringField('Sexo')
    foto = FileField('Foto')
    enviar = SubmitField('Enviar')
