"""empty message

Revision ID: 056c2fd219f3
Revises: d869cce9a13d
Create Date: 2021-01-22 08:28:07.565507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '056c2fd219f3'
down_revision = 'd869cce9a13d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('syndicate', sa.Column('empleado_legajo', sa.Integer(), nullable=True))
    op.drop_constraint('syndicate_sind_legajo_fkey', 'syndicate', type_='foreignkey')
    op.create_foreign_key(None, 'syndicate', 'emp', ['empleado_legajo'], ['legajo'])
    op.drop_column('syndicate', 'sind_legajo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('syndicate', sa.Column('sind_legajo', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'syndicate', type_='foreignkey')
    op.create_foreign_key('syndicate_sind_legajo_fkey', 'syndicate', 'emp', ['sind_legajo'], ['legajo'])
    op.drop_column('syndicate', 'empleado_legajo')
    # ### end Alembic commands ###
