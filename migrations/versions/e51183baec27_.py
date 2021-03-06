"""empty message

Revision ID: e51183baec27
Revises: 
Create Date: 2017-03-08 16:45:36.139131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e51183baec27'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('userid', sa.String(length=9), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('firstname', sa.String(length=30), nullable=False),
    sa.Column('lastname', sa.String(length=30), nullable=False),
    sa.Column('image', sa.String(length=30), nullable=False),
    sa.Column('sex', sa.String(length=6), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('profile_added_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('userid'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
