"""fix for INSTRM-1955

Revision ID: ddeb04402bbc
Revises: 1a6070b36cbb
Create Date: 2023-07-25 23:19:40.621113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddeb04402bbc'
down_revision = '1a6070b36cbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tel_status', sa.Column('inst_pa', sa.REAL(), nullable=True, comment='The INST_PA at which the exposure started [deg]'))
    op.add_column('tel_status', sa.Column('caller', sa.String(), nullable=True, comment='Which sub-system calls (e.g., mcs, agcc, etc.)'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tel_status', 'caller')
    op.drop_column('tel_status', 'inst_pa')
    # ### end Alembic commands ###