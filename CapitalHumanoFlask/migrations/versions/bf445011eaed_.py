"""empty message

Revision ID: bf445011eaed
Revises: 560595770581
Create Date: 2020-12-07 22:00:28.291963

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bf445011eaed'
down_revision = '560595770581'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Empleado',
    sa.Column('dni', sa.Integer(), nullable=True),
    sa.Column('legajo', sa.Integer(), nullable=False),
    sa.Column('telefono', sa.Integer(), nullable=True),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido', sa.String(length=250), nullable=True),
    sa.Column('domicilio', sa.String(length=250), nullable=True),
    sa.Column('fecha_ingreso', sa.DateTime(), nullable=True),
    sa.Column('fecha_salida', sa.DateTime(), nullable=True),
    sa.Column('fecha_nacimiento', sa.DateTime(), nullable=True),
    sa.Column('fecha_cese', sa.DateTime(), nullable=True),
    sa.Column('estado_general', sa.String(length=250), nullable=True),
    sa.Column('sexo', sa.String(length=250), nullable=True),
    sa.Column('foto', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('legajo')
    )
    op.create_table('Aptitud',
    sa.Column('idAptitud', sa.Integer(), nullable=False),
    sa.Column('nombreAptitud', sa.String(length=250), nullable=False),
    sa.Column('descripcionAptitud', sa.String(length=250), nullable=True),
    sa.Column('Empleado_Legajo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Empleado_Legajo'], ['Empleado.legajo'], ),
    sa.PrimaryKeyConstraint('idAptitud')
    )
    op.drop_table('empleado')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empleado',
    sa.Column('dni', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('legajo', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('telefono', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nombre', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('apellido', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('domicilio', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('fecha_ingreso', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('fecha_salida', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('fecha_nacimiento', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('fecha_cese', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('estado_general', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('sexo', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('foto', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('legajo', name='empleado_pkey')
    )
    op.drop_table('Aptitud')
    op.drop_table('Empleado')
    # ### end Alembic commands ###
