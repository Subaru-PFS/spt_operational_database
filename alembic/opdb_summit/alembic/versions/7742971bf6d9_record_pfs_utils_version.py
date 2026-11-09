"""record the pfs_utils version of each MCS frame

mcs_exposure.version_pfs_utils
    Version of the pfs_utils that measured the frame, which defines the MCS to PFI transform;
    NULL on rows written before.

Revision ID: 7742971bf6d9
Revises: a4d2f8c61b37
Create Date: 2026-11-09 15:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '7742971bf6d9'
down_revision = 'a4d2f8c61b37'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('mcs_exposure', sa.Column('version_pfs_utils', sa.String(), nullable=True,
                                            comment='Version of the pfs_utils'))


def downgrade():
    op.drop_column('mcs_exposure', 'version_pfs_utils')
