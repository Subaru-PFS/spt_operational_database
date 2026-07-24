"""clarifying dot_roach_flux columns

Revision ID: 23d91515dead
Revises: 8d61df7ba4ca
Create Date: 2026-07-24 16:13:18.136246

Rename the two existing dot_roach_flux flux columns to say exactly what they are,
and add the lamp-normalized ratio:
    flux      -> flux_abs         raw absolute flux [ADU] (lamp-dependent)
    flux_norm -> flux_ratio       flux / reference-spectra (per-cobra hide ratio; NOT lamp-corrected)
    + flux_ratio_norm             flux_ratio / lamp factor (monitor-corrected)

Renames (not drop+add) so the existing rows are preserved.  Only dot_roach_flux is
touched here; the unrelated diffs alembic autogenerate produced (test table, agc/pfs
comments and constraints) are pre-existing DB<->model drift and are intentionally left out.
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '23d91515dead'
down_revision = '8d61df7ba4ca'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('dot_roach_flux', 'flux', new_column_name='flux_abs',
                    existing_type=sa.REAL(),
                    existing_comment='Raw extracted flux [ADU]',
                    comment='Raw extracted flux [ADU]')
    op.alter_column('dot_roach_flux', 'flux_norm', new_column_name='flux_ratio',
                    existing_type=sa.REAL(),
                    existing_comment='Flux normalized by lamp response',
                    comment='Extracted flux divided by the extracted reference spectra')
    op.add_column('dot_roach_flux',
                  sa.Column('flux_ratio_norm', sa.REAL(), nullable=True,
                            comment='Flux ratio normalized by lamp response'))


def downgrade():
    op.drop_column('dot_roach_flux', 'flux_ratio_norm')
    op.alter_column('dot_roach_flux', 'flux_ratio', new_column_name='flux_norm',
                    existing_type=sa.REAL(),
                    existing_comment='Extracted flux divided by the extracted reference spectra',
                    comment='Flux normalized by lamp response')
    op.alter_column('dot_roach_flux', 'flux_abs', new_column_name='flux',
                    existing_type=sa.REAL(),
                    existing_comment='Raw extracted flux [ADU]',
                    comment='Raw extracted flux [ADU]')
