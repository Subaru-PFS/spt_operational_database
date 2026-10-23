"""create mcs_boresight_meas

mcs_boresight_meas
    Boresights measured by MCS from frames of one visit taken at several rotator angles,
    one row per measurement; mcs_boresight keeps the boresight used per visit.

Revision ID: e2b7c4d91a36
Revises: c5a91e7b3f20
Create Date: 2026-10-23 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'e2b7c4d91a36'
down_revision = 'c5a91e7b3f20'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('mcs_boresight_meas',
                    sa.Column('pfs_visit_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('mcs_boresight_x_pix', sa.REAL(), nullable=True,
                              comment='Measured boresight x [pixel]'),
                    sa.Column('mcs_boresight_y_pix', sa.REAL(), nullable=True,
                              comment='Measured boresight y [pixel]'),
                    sa.Column('calculated_at', sa.DateTime(), nullable=False,
                              comment='When the measurement was made (HST)'),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id']),
                    sa.PrimaryKeyConstraint('pfs_visit_id', 'calculated_at'))


def downgrade():
    op.drop_table('mcs_boresight_meas')
