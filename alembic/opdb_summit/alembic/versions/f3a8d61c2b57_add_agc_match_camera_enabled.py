"""add agc_match.camera_enabled

The AG actor can disable a camera (INSTRM-2919): its detections are still matched and
given a residual, but do not drive the fit.  Until now only the actor's log recorded
which; agc_match rows from a disabled camera looked like any other.

agc_match.camera_enabled
    False for a match whose camera was disabled for the fit.  NULL for rows written
    before this revision.

Revision ID: f3a8d61c2b57
Revises: c7e5f7e07143
Create Date: 2026-10-24 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'f3a8d61c2b57'
down_revision = 'c7e5f7e07143'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('agc_match',
                  sa.Column('camera_enabled', sa.Boolean(), nullable=True,
                            comment='False if the camera was disabled for the fit'))


def downgrade():
    op.drop_column('agc_match', 'camera_enabled')
