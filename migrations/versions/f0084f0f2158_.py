"""empty message

Revision ID: f0084f0f2158
Revises: 0033ef6d348f
Create Date: 2022-03-22 11:58:27.271576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0084f0f2158'
down_revision = '0033ef6d348f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('logs', sa.Column('ip', sa.String(length=500), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('logs', 'ip')
    # ### end Alembic commands ###
