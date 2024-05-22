"""Atualizando tabelas.

Revision ID: 83e9a3e671cf
Revises: 7391bf4a7213
Create Date: 2024-05-21 20:40:52.345313

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '83e9a3e671cf'
down_revision = '7391bf4a7213'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('client', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(length=1024), nullable=False))
        batch_op.add_column(sa.Column('housenumber', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('telephone', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('dateofpayment', sa.Integer(), nullable=False))
        batch_op.alter_column('formofpayment',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.drop_column('dateofbirth')
        batch_op.drop_column('contact')
        batch_op.drop_column('number')
        batch_op.drop_column('road')

    with op.batch_alter_table('nightguard', schema=None) as batch_op:
        batch_op.alter_column('dateofbirth',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('nightguard', schema=None) as batch_op:
        batch_op.alter_column('dateofbirth',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=False)

    with op.batch_alter_table('client', schema=None) as batch_op:
        batch_op.add_column(sa.Column('road', mysql.VARCHAR(length=1024), nullable=False))
        batch_op.add_column(sa.Column('number', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('contact', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('dateofbirth', mysql.DATETIME(), nullable=False))
        batch_op.alter_column('formofpayment',
               existing_type=sa.String(length=255),
               type_=mysql.INTEGER(),
               existing_nullable=False)
        batch_op.drop_column('dateofpayment')
        batch_op.drop_column('telephone')
        batch_op.drop_column('housenumber')
        batch_op.drop_column('address')

    # ### end Alembic commands ###
