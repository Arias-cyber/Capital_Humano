from app import db


class Empleado(db.Model):

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
    foto = db.Column(db.LargeBinary)

    def __str__(self):
        return (

            f'Nombre: {self.nombre}, '
            f'Apellido: {self.apellido}, '
            f'Domicilio: {self.domicilio}'
            f'Legajo: {self.legajo}'
            f'DNI: {self.dni}'
        )