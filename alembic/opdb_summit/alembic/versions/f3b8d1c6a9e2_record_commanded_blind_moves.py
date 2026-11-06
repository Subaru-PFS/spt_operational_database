"""record the commanded blind moves and operating-point calibrations

cobra_blind_move.phi_landing_command, phi_push_start, phi_push_command
    The phi the landing was commanded to, the phi the push was sized from and the phi its
    steps reach at gain 1, so a gain is measured against what was commanded however the
    move was aimed; NULL on rows written before, which mean phi_landing_target,
    phi_landing_target and phi_push_target.
cobra_blind_move.blind_move_calib_id
    The calibration that aimed the cobra; NULL if none did.
blind_move_calib.prior_calib_id, dot_landing, dot_target, parameters
    The calibration an operating-point fit started from, the landing and target depth it
    was tuned at, and the parameters and fleet terms of the fit as JSON.
cobra_blind_move_gain.reason
    Why a cobra is not calibrated.
cobra_blind_move.dot_command
    Comment: dot_target on rows with phi_push_command, which holds the aim.

Revision ID: f3b8d1c6a9e2
Revises: e7c3a9b2d5f1
Create Date: 2026-11-06 03:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'f3b8d1c6a9e2'
down_revision = 'e7c3a9b2d5f1'
branch_labels = None
depends_on = None

DOT_COMMAND_COMMENT = ('Depth the push was aimed at [dot fraction]: dot_target, or on rows without '
                       'phi_push_command the depth aimed through a calibration')
DOT_COMMAND_COMMENT_BEFORE = ('Depth the push was commanded to [dot fraction]; '
                              'dot_target unless aimed through a calibration')


def upgrade():
    op.add_column('cobra_blind_move',
                  sa.Column('phi_landing_command', sa.REAL(), nullable=True,
                            comment='Phi the landing was commanded to [rad]; NULL means '
                                    'phi_landing_target'))
    op.add_column('cobra_blind_move',
                  sa.Column('phi_push_start', sa.REAL(), nullable=True,
                            comment='Phi the push was sized from, the estimate after the landing '
                                    '[rad]; NULL means phi_landing_target'))
    op.add_column('cobra_blind_move',
                  sa.Column('phi_push_command', sa.REAL(), nullable=True,
                            comment='Phi the steps of the push reach at gain 1 from '
                                    'phi_push_start [rad]; NULL means phi_push_target'))
    op.add_column('cobra_blind_move',
                  sa.Column('blind_move_calib_id', sa.Integer(), nullable=True,
                            comment='Blind-move calibration that aimed this cobra; NULL if '
                                    'none did'))
    op.create_foreign_key('cobra_blind_move_blind_move_calib_id_fkey', 'cobra_blind_move',
                          'blind_move_calib', ['blind_move_calib_id'], ['blind_move_calib_id'])

    op.add_column('blind_move_calib',
                  sa.Column('prior_calib_id', sa.Integer(), nullable=True,
                            comment='Calibration an operating-point fit started from; NULL if none'))
    op.create_foreign_key('blind_move_calib_prior_calib_id_fkey', 'blind_move_calib',
                          'blind_move_calib', ['prior_calib_id'], ['blind_move_calib_id'])
    op.add_column('blind_move_calib',
                  sa.Column('dot_landing', sa.REAL(), nullable=True,
                            comment='Landing depth the gains were tuned at [dot fraction]; '
                                    'NULL for a fit over several depths'))
    op.add_column('blind_move_calib',
                  sa.Column('dot_target', sa.REAL(), nullable=True,
                            comment='Push target the gains were tuned at [dot fraction]; '
                                    'NULL for a fit over several depths'))
    op.add_column('blind_move_calib',
                  sa.Column('parameters', sa.String(), nullable=True,
                            comment='Parameters and fleet terms of the fit, JSON'))

    op.add_column('cobra_blind_move_gain',
                  sa.Column('reason', sa.String(), nullable=True,
                            comment='Why the cobra is not calibrated; NULL if it is'))
    op.alter_column('cobra_blind_move', 'dot_command', existing_type=sa.REAL(),
                    comment=DOT_COMMAND_COMMENT, existing_comment=DOT_COMMAND_COMMENT_BEFORE)


def downgrade():
    op.alter_column('cobra_blind_move', 'dot_command', existing_type=sa.REAL(),
                    comment=DOT_COMMAND_COMMENT_BEFORE, existing_comment=DOT_COMMAND_COMMENT)
    op.drop_column('cobra_blind_move_gain', 'reason')
    op.drop_column('blind_move_calib', 'parameters')
    op.drop_column('blind_move_calib', 'dot_target')
    op.drop_column('blind_move_calib', 'dot_landing')
    op.drop_constraint('blind_move_calib_prior_calib_id_fkey', 'blind_move_calib', type_='foreignkey')
    op.drop_column('blind_move_calib', 'prior_calib_id')
    op.drop_constraint('cobra_blind_move_blind_move_calib_id_fkey', 'cobra_blind_move',
                       type_='foreignkey')
    op.drop_column('cobra_blind_move', 'blind_move_calib_id')
    op.drop_column('cobra_blind_move', 'phi_push_command')
    op.drop_column('cobra_blind_move', 'phi_push_start')
    op.drop_column('cobra_blind_move', 'phi_landing_command')
