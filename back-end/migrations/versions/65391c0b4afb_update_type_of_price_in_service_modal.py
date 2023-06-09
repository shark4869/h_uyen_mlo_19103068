"""Update type of price in Service  modal

Revision ID: 65391c0b4afb
Revises: 3248bd5c9d8f
Create Date: 2023-05-08 00:04:02.227405

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '65391c0b4afb'
down_revision = '3248bd5c9d8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=mysql.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Integer(),
               type_=mysql.FLOAT(),
               existing_nullable=False)

    # ### end Alembic commands ###
