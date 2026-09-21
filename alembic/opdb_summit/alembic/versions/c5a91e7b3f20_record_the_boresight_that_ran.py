"""record the boresight each transform ran about

The boresight the MCS uses is not a constant: PfiTransform.setParams recomputes it for
every iteration as the nominal centre plus a coefficient times that frame's altitude.
Only the iteration-0 value was ever written down, and mcs_boresight is keyed by visit,
so it cannot hold the rest.  A transform recorded for iteration 1 or later therefore
could not be rebuilt without re-deriving the boresight from a calibration file that may
have changed since.

mcs_pfi_transformation.mcs_boresight_x_pix / mcs_boresight_y_pix
    The boresight the stored parameters were applied about.  With these the row
    determines the transform on its own.  NULL for frames taken before this revision.

Revision ID: c5a91e7b3f20
Revises: d7f3a5b21c04
Create Date: 2026-09-11 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'c5a91e7b3f20'
down_revision = 'd7f3a5b21c04'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('mcs_pfi_transformation',
                  sa.Column('mcs_boresight_x_pix', sa.REAL(), nullable=True,
                            comment='Boresight x the transform was applied about [pixel]'))
    op.add_column('mcs_pfi_transformation',
                  sa.Column('mcs_boresight_y_pix', sa.REAL(), nullable=True,
                            comment='Boresight y the transform was applied about [pixel]'))


def downgrade():
    op.drop_column('mcs_pfi_transformation', 'mcs_boresight_y_pix')
    op.drop_column('mcs_pfi_transformation', 'mcs_boresight_x_pix')
