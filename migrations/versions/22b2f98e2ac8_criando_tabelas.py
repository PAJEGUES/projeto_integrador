"""Criando tabelas.

Revision ID: 22b2f98e2ac8
Revises: 34f750747a40
Create Date: 2024-05-06 20:19:38.858749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22b2f98e2ac8'
down_revision = '34f750747a40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('neighborhood',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('neighborhood_name', sa.String(length=255), nullable=False),
    sa.Column('sector_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nightguard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('vehicle', sa.String(length=1024), nullable=False),
    sa.Column('licenseplate', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('dateofbirth', sa.DateTime(), nullable=False),
    sa.Column('formofpayment', sa.Integer(), nullable=False),
    sa.Column('neighborhood', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sector',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('neighborhood_name', sa.String(length=255), nullable=False),
    sa.Column('sector_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tokens',
    sa.Column('token', sa.String(length=255), nullable=False),
    sa.Column('expiration', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tokens')
    op.drop_table('users')
    op.drop_table('sector')
    op.drop_table('nightguard')
    op.drop_table('neighborhood')
    # ### end Alembic commands ###