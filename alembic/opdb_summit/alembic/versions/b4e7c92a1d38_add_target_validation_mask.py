"""add target_validation_mask and the convergence parameters

Why fps refused a cobra's target, and the parameters the per-fiber columns were
computed under.  Both already reach the pfsConfig FITS file; these columns make them
queryable across visits, which is what opdb is for -- "how many science targets did we
lose to instrument geometry this semester, and to what" should be one query, not a walk
over FITS files.

pfs_config_fiber.target_validation_mask
    TargetValidation bits.  Non-zero means the cobra was designed to converge and was
    refused; zero elsewhere, including for cobras the design never asked to converge.

pfs_config.converg_distance_threshold
    The threshold that decides fiber_status: GOOD iff the fiber landed within it.  Not
    the same number as converg_tolerance, which is what the convergence loop aimed for
    per iteration and is floored well below this.  Without it, fiber_status can be read
    but not reproduced.

pfs_config.target_fallback_invalid / target_fallback_unassigned
    Where a refused cobra was sent.  A policy rather than a law, and it cannot be
    backfilled once rows exist.

pfs_config.fiducial_check_skipped
    Whether the operator disabled the fiducial interference test, which changes what a
    zero mask means: no interference, or never looked.

pfs_config.inst_status_flag
    InstrumentStatusFlag, carrying CONVERGENCE_FAILED among others.  Already in the
    FITS; here so "which visits failed convergence" is answerable in SQL.

Revision ID: b4e7c92a1d38
Revises: 23d91515dead
Create Date: 2026-08-04 18:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'b4e7c92a1d38'
down_revision = '23d91515dead'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('pfs_config_fiber',
                  sa.Column('target_validation_mask', sa.Integer(), nullable=True,
                            comment='TargetValidation bits: why fps refused this target, 0 if it did not'))

    op.add_column('pfs_config',
                  sa.Column('converg_distance_threshold', sa.REAL(), nullable=True,
                            comment='Distance within which a science fiber counts as converged [mm]; '
                                    'decides fiber_status, unlike converg_tolerance'))
    op.add_column('pfs_config',
                  sa.Column('target_fallback_invalid', sa.String(), nullable=True,
                            comment='Where a cobra with an invalid target was sent'))
    op.add_column('pfs_config',
                  sa.Column('target_fallback_unassigned', sa.String(), nullable=True,
                            comment='Where a cobra with no assigned target was sent'))
    op.add_column('pfs_config',
                  sa.Column('fiducial_check_skipped', sa.Boolean(), nullable=True,
                            comment='True if the fiducial interference check was disabled for this visit'))
    op.add_column('pfs_config',
                  sa.Column('inst_status_flag', sa.Integer(), nullable=True,
                            comment='InstrumentStatusFlag bitmask, e.g. CONVERGENCE_FAILED'))

    # Both tables carried the same comment, which hid the distinction: the design says
    # whether a fiber is healthy, the config says whether it reached its target.
    op.alter_column('pfs_design_fiber', 'fiber_status',
                    comment='Fiber health: GOOD, BROKENFIBER, BLOCKED, BROKENCOBRA')
    op.alter_column('pfs_config_fiber', 'fiber_status',
                    comment='Outcome this visit: GOOD, NOTCONVERGED, BLACKSPOT, UNKNOWN')


def downgrade():
    op.drop_column('pfs_config', 'inst_status_flag')
    op.drop_column('pfs_config', 'fiducial_check_skipped')
    op.drop_column('pfs_config', 'target_fallback_unassigned')
    op.drop_column('pfs_config', 'target_fallback_invalid')
    op.drop_column('pfs_config', 'converg_distance_threshold')
    op.drop_column('pfs_config_fiber', 'target_validation_mask')
