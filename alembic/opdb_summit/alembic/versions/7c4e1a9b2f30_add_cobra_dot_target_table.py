"""add cobra_dot_target and cobra_dot_cmd tables

Per-cobra black-dot targeting.

The geometric dot model places every cobra's dot from the black_dots table, but the
depth at which a cobra actually hides best differs from that model by a median 0.1 in
dot fraction (~150 um of tip travel), with an intrinsic per-cobra scatter of 0.051 and
a coherent field-dependent term.  A single global target therefore leaves a large part
of the fleet off the obscuration optimum.

Two tables:

  cobra_dot_cmd     where each cobra was COMMANDED to sit at each flat of a scan.
                    dot_roach_flux supplies the y axis of the obscuration curve; this
                    supplies the x axis.  Until now the fraction was implicit -- a
                    global start plus a fixed increment -- which only works while
                    every cobra shares one fraction.  Once the blind move sends each
                    cobra to its own target, x becomes a value per (cobra, visit) and
                    cannot be reconstructed from scan parameters at all.

  cobra_dot_target  the fitted optimum per cobra, derived from a join of the two.

Written by different actors: fps knows where it sent the cobras, drp knows what the
flux was, and they join on (pfs_visit_id, cobra_id).

Revision ID: 7c4e1a9b2f30
Revises: 23d91515dead
Create Date: 2026-07-29 14:20:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c4e1a9b2f30'
down_revision = '23d91515dead'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('cobra_dot_cmd',
                    sa.Column('pfs_visit_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='Visit of the flat this commanded position corresponds to'),
                    sa.Column('cobra_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='Cobra identifier (1..2394)'),
                    sa.Column('cmd_fraction', sa.REAL(), nullable=True,
                              comment='Dot fraction the cobra was COMMANDED to at that flat -- not a '
                                      'measurement: 0 = entry edge, 0.5 = dot centre, 1 = exit edge'),
                    sa.ForeignKeyConstraint(['cobra_id'], ['cobra.cobra_id']),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id']),
                    sa.PrimaryKeyConstraint('pfs_visit_id', 'cobra_id'),
                    sa.UniqueConstraint('pfs_visit_id', 'cobra_id'),
                    )

    op.create_table('cobra_dot_target',
                    sa.Column('pfs_visit_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='First flat visit of the scan this calibration was fitted '
                                      'from, as recorded in dot_roach_flux'),
                    sa.Column('cobra_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='Cobra identifier (1..2394)'),
                    sa.Column('visit0', sa.Integer(), nullable=True,
                              comment='moveToPfsDesign convergence visit of the same calibration '
                                      'run -- where dot_edge is measured, while dot_target comes '
                                      'from the flats that follow it'),
                    sa.Column('dot_target', sa.REAL(), nullable=True,
                              comment='Commanded dot fraction of maximum obscuration: the centre '
                                      'of the flux plateau, not the noisy argmin. Measured by the '
                                      'spectrograph'),
                    sa.Column('dot_target_err', sa.REAL(), nullable=True,
                              comment='Uncertainty on dot_target from the fit, in dot fraction'),
                    sa.Column('min_flux', sa.REAL(), nullable=True,
                              comment='Residual flux ratio at dot_target'),
                    sa.Column('dot_edge', sa.REAL(), nullable=True,
                              comment='Commanded dot fraction at which the MCS loses this cobra on '
                                      'its own approach arc; 0 means the modelled entry edge. '
                                      'Measured by the MCS -- a different boundary from dot_target, '
                                      'since observability ends before obscuration is complete, so '
                                      'neither column can stand in for the other'),
                    sa.Column('dot_edge_err', sa.REAL(), nullable=True,
                              comment='Uncertainty on dot_edge, in dot fraction'),
                    sa.Column('is_valid', sa.Boolean(), nullable=True,
                              comment='False where the fit did not meet its acceptance criterion; '
                                      'consumers must fall back to the defaults rather than use a '
                                      'fitted-but-rejected number'),
                    sa.Column('dot_catalog', sa.String(), nullable=True,
                              comment='Black-dot catalogue this calibration was fitted against '
                                      '(e.g. black_dots_mm.csv). Both columns are fractions of a '
                                      'theoretical dot, so replacing the catalogue invalidates '
                                      'them'),
                    sa.ForeignKeyConstraint(['cobra_id'], ['cobra.cobra_id']),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id']),
                    sa.PrimaryKeyConstraint('pfs_visit_id', 'cobra_id'),
                    sa.UniqueConstraint('pfs_visit_id', 'cobra_id'),
                    )


def downgrade():
    op.drop_table('cobra_dot_target')
    op.drop_table('cobra_dot_cmd')
