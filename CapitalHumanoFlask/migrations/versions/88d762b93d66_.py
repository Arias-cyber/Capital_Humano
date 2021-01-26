"""empty message

Revision ID: 88d762b93d66
Revises: f6b666fc5086
Create Date: 2021-01-11 16:56:40.411229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88d762b93d66'
down_revision = 'f6b666fc5086'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('im',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('mimetype', sa.Text(), nullable=False),
    sa.Column('emp_legajo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['emp_legajo'], ['emp.legajo'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('im')
    # ### end Alembic commands ###
