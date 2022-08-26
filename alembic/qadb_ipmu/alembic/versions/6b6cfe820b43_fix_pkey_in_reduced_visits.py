"""fix pkey in reduced_visits

Revision ID: 6b6cfe820b43
Revises: bcba4b86aebf
Create Date: 2022-08-24 16:55:12.504106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b6cfe820b43'
down_revision = 'bcba4b86aebf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'data_processing', ['run_id'])
    op.create_unique_constraint(None, 'data_processing_results', ['run_id', 'pfs_visit_id', 'arm'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'data_processing_results', type_='unique')
    op.drop_constraint(None, 'data_processing', type_='unique')
    # ### end Alembic commands ###
