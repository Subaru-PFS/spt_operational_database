"""record the uncertainty and altitude of each boresight measurement

mcs_boresight_meas.mcs_boresight_x_err_pix, mcs_boresight_y_err_pix
    Uncertainty of the boresight within its visit, from the frame-to-frame displacement its
    frames show; NULL on rows written before.
mcs_boresight_meas.altitude
    Mean telescope altitude of the frames; NULL on rows written before.

Revision ID: b81e5c2d4f90
Revises: a4c01e4f1877
Create Date: 2026-11-09 18:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'b81e5c2d4f90'
down_revision = 'a4c01e4f1877'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('mcs_boresight_meas',
                  sa.Column('mcs_boresight_x_err_pix', sa.REAL(), nullable=True,
                            comment='Uncertainty of x within the visit [pixel]; NULL if not measured'))
    op.add_column('mcs_boresight_meas',
                  sa.Column('mcs_boresight_y_err_pix', sa.REAL(), nullable=True,
                            comment='Uncertainty of y within the visit [pixel]; NULL if not measured'))
    op.add_column('mcs_boresight_meas',
                  sa.Column('altitude', sa.REAL(), nullable=True,
                            comment='Mean telescope altitude of the frames [deg]'))


def downgrade():
    op.drop_column('mcs_boresight_meas', 'altitude')
    op.drop_column('mcs_boresight_meas', 'mcs_boresight_y_err_pix')
    op.drop_column('mcs_boresight_meas', 'mcs_boresight_x_err_pix')
