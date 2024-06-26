"""client

Revision ID: 7391bf4a7213
Revises: 19d1905f4981
Create Date: 2024-05-08 21:37:54.642351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7391bf4a7213'
down_revision = '19d1905f4981'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('road', sa.String(length=1024), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('neighborhood', sa.String(length=255), nullable=False),
    sa.Column('contact', sa.Integer(), nullable=False),
    sa.Column('paymentamount', sa.Integer(), nullable=False),
    sa.Column('dateofbirth', sa.DateTime(), nullable=False),
    sa.Column('formofpayment', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('client')
    # ### end Alembic commands ###
