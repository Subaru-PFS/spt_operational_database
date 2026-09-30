"""add pfs_config_sps.observed_at

pfs_config_sps.observed_at
    The mid-exposure time of the visit, as the pfsConfig obstime records it.  NULL for
    visits taken before this revision, and until the pfsConfig of the visit is written.

pfs_config.to_be_observed_at keeps the time the fiber positions were computed for, the
convergence of visit0, which every visit of the set shares.

Revision ID: c7e5f7e07143
Revises: e2b7c4d91a36
Create Date: 2026-09-25 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'c7e5f7e07143'
down_revision = 'e2b7c4d91a36'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('pfs_config_sps',
                  sa.Column('observed_at', sa.DateTime(timezone=True), nullable=True,
                            comment='Mid-exposure time of this visit (pfsConfig obstime)'))


def downgrade():
    op.drop_column('pfs_config_sps', 'observed_at')
