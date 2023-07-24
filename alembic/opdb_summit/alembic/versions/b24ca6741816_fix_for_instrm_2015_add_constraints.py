"""fix for INSTRM-2015 add constraints

Revision ID: b24ca6741816
Revises: dfe39841eb0c
Create Date: 2023-07-07 15:00:39.585689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b24ca6741816'
down_revision = 'dfe39841eb0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'cobra_move', 'cobra_match', ['pfs_visit_id', 'iteration', 'cobra_id'], ['pfs_visit_id', 'iteration', 'cobra_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cobra_move', type_='foreignkey')
    # ### end Alembic commands ###