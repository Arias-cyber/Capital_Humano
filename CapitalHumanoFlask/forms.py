from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, DateTimeField, FileField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField

from models import Sindicato, ObraSocial, Aptitud, Formacion_Academica


class EmpleadoForm(FlaskForm):
    dni = IntegerField('DNI')
    legajo = IntegerField('Legajo')
    telefono = IntegerField('Telefono')
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido')
    domicilio = StringField('Domicilio')
    fecha_ingreso = DateTimeField('Fecha de ingreso',format='%d/%m/%Y')
    fecha_salida = DateTimeField('Fecha de salida',format='%d/%m/%Y')
    fecha_nacimiento = DateTimeField('Fecha de nacimiento',format='%d/%m/%Y')
    fecha_cese = DateTimeField('Fecha de cese',format='%d/%m/%Y')
    estado_general = StringField('Estado general')
    sexo = StringField('Sexo')
    enviar = SubmitField('Enviar')

class ImgForm(FlaskForm):
    pic = FileField('Foto')
    name = StringField("Nombre")
    mimetype = StringField("Mimetype")
    emp_legajo = IntegerField("Legajo")
    enviarF = SubmitField('Enviar Foto')

class SindicatoForm(FlaskForm):
    nombre = StringField("Sindicato")
    domicilio = StringField("Domicilio")
    telefono = IntegerField('Telefono')
    enviar = SubmitField('Enviar')

class ObraSocialForm(FlaskForm):
    nombre = StringField("Sindicato")
    cuit = IntegerField('CUIT')
    telefono = IntegerField('Telefono')
    domicilio = StringField("Domicilio")
    enviar = SubmitField('Enviar')


def sindicato_query():
    return Sindicato.query

def obra_query():
    return ObraSocial.query


class ChoiceSindForm(FlaskForm):
    opts = QuerySelectField(query_factory=sindicato_query, allow_blank=False, get_label='nombre')
    optos = QuerySelectField(query_factory=obra_query, allow_blank=False, get_label='nombre')

class ChoiceOSForm(FlaskForm):
    optos = QuerySelectField(query_factory=obra_query, allow_blank=False, get_label='nombre')




class AptitudForm(FlaskForm):
    aptitud = StringField("Nombre de la Aptitud")
    descripcion = StringField("Descripcion")
    enviar = SubmitField('Enviar')

class FormacionForm(FlaskForm):
    titulo = StringField("Titulo")
    descripcion = StringField("Descripcion")
    institucion= StringField("Institucion")
    enviar = SubmitField('Enviar')



def sindicato_query():
    return Aptitud.query

def obra_query():
    return Formacion_Academica.query
