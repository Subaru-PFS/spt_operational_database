"""add pfs_config_sps_observed

pfs_config_sps is inserted before the exposure, so it cannot hold the mid-exposure time,
which is only known once the shutters close.

pfs_config_sps.observed_at -> pfs_config_sps.requested_at
    The time the pfsConfig of the visit was made, before the exposure.

pfs_config_sps_observed
    One row per visit whose pfsConfig was written, inserted once with it.
    observed_at: the mid-exposure time of the visit, as the pfsConfig obstime records it.

Revision ID: 7397aa474666
Revises: f3a8d61c2b57
Create Date: 2026-10-27 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '7397aa474666'
down_revision = 'f3a8d61c2b57'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('pfs_config_sps_observed',
                    sa.Column('pfs_visit_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='PFS visit identifier'),
                    sa.Column('observed_at', sa.DateTime(timezone=True), nullable=True,
                              comment='Mid-exposure time of this visit (pfsConfig obstime)'),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id']),
                    sa.PrimaryKeyConstraint('pfs_visit_id'))

    op.alter_column('pfs_config_sps', 'observed_at', new_column_name='requested_at',
                    comment='Time the pfsConfig of this visit was made, before the exposure',
                    existing_type=sa.DateTime(timezone=True), existing_nullable=True)


def downgrade():
    op.alter_column('pfs_config_sps', 'requested_at', new_column_name='observed_at',
                    comment='Mid-exposure time of this visit (pfsConfig obstime)',
                    existing_type=sa.DateTime(timezone=True), existing_nullable=True)

    op.drop_table('pfs_config_sps_observed')
