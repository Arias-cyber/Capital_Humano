"""empty message

Revision ID: 560595770581
Revises: 09a6fac56dd2
Create Date: 2020-12-06 16:27:34.336251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '560595770581'
down_revision = '09a6fac56dd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empleado',
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('empleado')
    # ### end Alembic commands ###
