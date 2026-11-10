"""keep blind-move runs by their phi start rather than their distance from target

cobra_blind_move.dot_approach
    Depth the closed-loop ramp was commanded to stop at before the landing, not measured;
    NULL on rows written before, which were commanded to -0.075.
blind_move_calib.ramp_residual_cut
    Dropped: a fit keeps a run by its start depth, recorded in parameters.

Revision ID: a4c01e4f1877
Revises: 7742971bf6d9
Create Date: 2026-11-10 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'a4c01e4f1877'
down_revision = '7742971bf6d9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('cobra_blind_move',
                  sa.Column('dot_approach', sa.REAL(), nullable=True,
                            comment='Depth the closed-loop ramp was commanded to stop at before the '
                                    'landing [dot fraction], not measured; NULL means -0.075'))
    op.drop_column('blind_move_calib', 'ramp_residual_cut')


def downgrade():
    # The cuts are gone with the column: NaN on every calibration.
    op.add_column('blind_move_calib',
                  sa.Column('ramp_residual_cut', sa.REAL(), nullable=False, server_default=sa.text("'NaN'"),
                            comment='Largest ramp_residual a move is fitted with [mm]'))
    op.drop_column('cobra_blind_move', 'dot_approach')
