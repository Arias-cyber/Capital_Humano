"""empty message

Revision ID: 61180e0d9a19
Revises: 
Create Date: 2021-01-07 19:53:32.379234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61180e0d9a19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emp',
    sa.Column('dni', sa.Integer(), nullable=True),
    sa.Column('legajo', sa.Integer(), nullable=False),
    sa.Column('telefono', sa.BigInteger(), nullable=True),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido', sa.String(length=250), nullable=True),
    sa.Column('domicilio', sa.String(length=250), nullable=True),
    sa.Column('fecha_ingreso', sa.DateTime(), nullable=True),
    sa.Column('fecha_salida', sa.DateTime(), nullable=True),
    sa.Column('fecha_nacimiento', sa.DateTime(), nullable=True),
    sa.Column('fecha_cese', sa.DateTime(), nullable=True),
    sa.Column('estado_general', sa.String(length=250), nullable=True),
    sa.Column('sexo', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('legajo')
    )
    op.create_table('im',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.LargeBinary(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('mimetype', sa.Text(), nullable=False),
    sa.Column('emp_legajo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['emp_legajo'], ['emp.legajo'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('img')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('im')
    op.drop_table('emp')
    # ### end Alembic commands ###
