"""empty message

Revision ID: 471a04403465
Revises: 30a1e027aefa
Create Date: 2017-10-30 20:11:03.078000

"""

# revision identifiers, used by Alembic.
revision = '471a04403465'
down_revision = '30a1e027aefa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nazev', sa.String(length=64), nullable=False),
    sa.Column('rok', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_hry')
    )
    op.create_index('ix_hry_nazev', 'hry', ['nazev'], unique=True)
    op.drop_table('sqlite_sequence')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    op.drop_index('ix_hry_nazev', table_name='hry')
    op.drop_table('hry')
    ### end Alembic commands ###
