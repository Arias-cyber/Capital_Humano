from sqlalchemy.orm import relationship

from app import db

subs = db.Table('subs',
    db.Column('legajo', db.Integer, db.ForeignKey('emp.legajo')),
    db.Column('id', db.Integer, db.ForeignKey('syndicate.id'))
)

subsc = db.Table('subsc',
    db.Column('legajo', db.Integer, db.ForeignKey('emp.legajo')),
    db.Column('id', db.Integer, db.ForeignKey('obra_social.id'))
)


formacion_empleado = db.Table('formacion_empleado',
    db.Column('empleado_legajo',db.Integer,db.ForeignKey('emp.legajo')),
    db.Column('formacion_id',db.Integer,db.ForeignKey('formacion_academica.id'))
)

aptitud_empleado= db.Table('aptitud_empleado',
    db.Column('empleado_legajo',db.Integer,db.ForeignKey('emp.legajo')),
    db.Column('aptitud_id',db.Integer,db.ForeignKey('aptitud.id'))
)


class Empleado(db.Model):
    __tablename__ = 'emp'

    dni = db.Column(db.Integer)
    legajo = db.Column(db.Integer, primary_key=True)
    telefono = db.Column(db.BigInteger)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    domicilio = db.Column(db.String(250))
    fecha_ingreso = db.Column(db.DateTime)
    fecha_salida = db.Column(db.DateTime)
    fecha_nacimiento = db.Column(db.DateTime)
    fecha_cese = db.Column(db.DateTime)
    estado_general = db.Column(db.String(250))
    sexo = db.Column(db.String(250))
    im = relationship("Img", uselist=False, back_populates="emp")
    #syndicate = relationship("Sindicato")
    suscripcion = db.relationship('Sindicato', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))
    suscription = db.relationship('ObraSocial', secondary=subsc, backref=db.backref('subscriber', lazy='dynamic'))
    formaciones_academicas= db.relationship('Formacion_Academica', secondary=formacion_empleado, backref=db.backref('formacion', lazy='dynamic'))
    #aptitudes = db.relationship('Aptitud',backref='emp',lazy=True)
    aptitudes= db.relationship('Aptitud',secondary=aptitud_empleado,backref=db.backref('aptitud_empleado',lazy='dynamic'))


    def __str__(self):
        return (

            f'Nombre: {self.nombre}, '
            f'Apellido: {self.apellido}, '
            f'Domicilio: {self.domicilio}'
            f'Legajo: {self.legajo}'
            f'DNI: {self.dni}'
        )

class Img(db.Model):
    __tablename__ = 'im'
    id = db.Column(db.Integer, primary_key=True)
#    img = db.Column(db.Text, unique=True, nullable=True)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    emp_legajo = db.Column(db.Integer, db.ForeignKey('emp.legajo'))
    emp = relationship("Empleado", back_populates="im")

class Sindicato(db.Model):
    __tablename__ = 'syndicate'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250))
    telefono = db.Column(db.BigInteger)
    domicilio = db.Column(db.String(250))
   # empleado_legajo = db.Column(db.Integer, db.ForeignKey('emp.legajo'), nullable=True)
   # emp = relationship("Empleado", back_populates="syndicate")


    def __repr__(self):
        return '[{}]'.format(self.nombre)

class ObraSocial(db.Model):
    __tablename__ = 'obra_social'
    id = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(250))
    cuit = db.Column(db.BigInteger)
    telefono = db.Column(db.BigInteger)
    domicilio = db.Column(db.String(250))


class Formacion_Academica(db.Model):
    __tablename__ = 'formacion_academica'
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    institucion = db.Column(db.String(45))
    #empleado_dni= db.Column(db.Integer, db.ForeignKey('emp.legajo'),nullable=True)

class Aptitud(db.Model):
    __tablename__ = 'aptitud'
    id = db.Column(db.Integer, primary_key = True)
    aptitud = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    #empleado_dni= db.Column(db.Integer, db.ForeignKey('emp.legajo'),nullable=True)


