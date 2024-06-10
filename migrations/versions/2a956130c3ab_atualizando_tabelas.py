"""atualizando tabelas.

Revision ID: 2a956130c3ab
Revises: 25f5220ad1a1
Create Date: 2024-06-10 19:57:44.876971

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2a956130c3ab'
down_revision = '25f5220ad1a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tokens', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.drop_constraint('tokens_ibfk_1', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tokens', schema=None) as batch_op:
        batch_op.create_foreign_key('tokens_ibfk_1', 'users', ['user_id'], ['id'])
        batch_op.alter_column('user_id',
               existing_type=mysql.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
