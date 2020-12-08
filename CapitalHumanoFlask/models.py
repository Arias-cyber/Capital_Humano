from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Empleado(db.Model):
    __tablename__="Empleado"
    dni = db.Column(db.Integer)
    legajo = db.Column(db.Integer, primary_key=True)
    telefono = db.Column(db.Integer)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    domicilio = db.Column(db.String(250))
    fecha_ingreso = db.Column(db.DateTime)
    fecha_salida = db.Column(db.DateTime)
    fecha_nacimiento = db.Column(db.DateTime)
    fecha_cese = db.Column(db.DateTime)
    estado_general = db.Column(db.String(250))
    sexo = db.Column(db.String(250))
    foto = db.Column(db.LargeBinary,nullable=True)

    def __str__(self):
        return (

            f'Nombre: {self.nombre}, '
            f'Apellido: {self.apellido}, '
            f'Domicilio: {self.domicilio}'
            f'Legajo: {self.legajo}'
            f'DNI: {self.dni}'
        )


class Aptitud (db.Model):
    __tablename__='Aptitud'
    idAptitud= db.Column(db.Integer,primary_key=True)
    nombreAptitud=db.Column(db.String(250),nullable=False)
    descripcionAptitud=db.Column(db.String(250))
    Empleado_Legajo= db.Column(db.Integer,ForeignKey('Empleado.legajo'),nullable=True)
    empleado= relationship("Empleado",backref='Aptitud')

    def __str__(self):
        return(
            f'Nombre Aptitud:{self.nombreAptitud},'
            f'Descripcion: {self.descripcionAptitud},'
        )




class Formacion_Academica(db.Model):
    __tablename__='Formacion_Academica'
    idFormacion_Academica=db.Column(db.Integer,primary_key=True)
    titulo= db.Column(db.String(250))
    descripcion=db.Column(db.String(250))
    institucion=db.Column(db.String(250))
    Empleado_Legajo= db.Column(db.Integer,ForeignKey('Empleado.legajo'),nullable=True)
    empleado= relationship("Empleado",backref='Formacion_Academica')

    def __str__(self):
        return(
            f'Titulo:{self.titulo},'
            f'Descripcion: {self.descripcion},'
            f'Institucion: {self,institucion}'
        )

