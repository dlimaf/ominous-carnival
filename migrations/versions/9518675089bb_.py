"""empty message

Revision ID: 9518675089bb
Revises: eb15bf27733e
Create Date: 2023-04-21 00:34:27.094411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9518675089bb'
down_revision = 'eb15bf27733e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('climate',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('population',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('starships', schema=None) as batch_op:
        batch_op.alter_column('model',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('starship_class',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('starships', schema=None) as batch_op:
        batch_op.alter_column('starship_class',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('model',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('population',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('climate',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)

    # ### end Alembic commands ###
