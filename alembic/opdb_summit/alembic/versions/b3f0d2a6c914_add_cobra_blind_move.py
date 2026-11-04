"""add cobra_blind_move

cobra_blind_move
    The two open-loop phi moves of a black-dot convergence, measured on turned dots: one
    row per (visit, cobra) sent to a dot, with the measured phi before and after each move
    and the depths they were commanded to.

Revision ID: b3f0d2a6c914
Revises: 7397aa474666
Create Date: 2026-11-04 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'b3f0d2a6c914'
down_revision = '7397aa474666'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('cobra_blind_move',
                    sa.Column('pfs_visit_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='PFS visit identifier'),
                    sa.Column('cobra_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='Cobra identifier (1..2394)'),
                    sa.Column('dot_landing', sa.REAL(), nullable=True,
                              comment='Depth the ramp landed at [dot fraction]'),
                    sa.Column('dot_target', sa.REAL(), nullable=True,
                              comment='Depth wanted for the push [dot fraction]'),
                    sa.Column('dot_command', sa.REAL(), nullable=True,
                              comment='Depth the push was commanded to [dot fraction]; '
                                      'dot_target unless aimed through a calibration'),
                    sa.Column('phi_landing_target', sa.REAL(), nullable=True,
                              comment='Phi at dot_landing [rad]'),
                    sa.Column('phi_push_target', sa.REAL(), nullable=True,
                              comment='Phi at dot_command [rad]'),
                    sa.Column('phi_start', sa.REAL(), nullable=True,
                              comment='Measured phi before the landing [rad]; NULL if unseen'),
                    sa.Column('phi_landed', sa.REAL(), nullable=True,
                              comment='Measured phi after the landing [rad]; NULL if unseen'),
                    sa.Column('phi_pushed', sa.REAL(), nullable=True,
                              comment='Measured phi after the push [rad]; NULL if unseen'),
                    sa.Column('ramp_residual', sa.REAL(), nullable=True,
                              comment='Distance from its target before the landing [mm]'),
                    sa.ForeignKeyConstraint(['cobra_id'], ['cobra.cobra_id']),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id']),
                    sa.PrimaryKeyConstraint('pfs_visit_id', 'cobra_id'))


def downgrade():
    op.drop_table('cobra_blind_move')
