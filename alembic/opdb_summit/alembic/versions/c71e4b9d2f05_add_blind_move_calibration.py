"""add blind-move calibration tables

blind_move_calib
    A per-cobra calibration of the two blind moves, fitted from cobra_blind_move.
cobra_blind_move_gain
    Its gains, one row per cobra.
blind_move_calib_validation
    A calibration judged good on aimed runs; the default is the one of the newest row.

All three are written once and never updated.

Revision ID: c71e4b9d2f05
Revises: b3f0d2a6c914
Create Date: 2026-11-04 18:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'c71e4b9d2f05'
down_revision = 'b3f0d2a6c914'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('blind_move_calib',
                    sa.Column('blind_move_calib_id', sa.Integer(), autoincrement=True, nullable=False,
                              comment='Calibration identifier'),
                    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False,
                              comment='Time the calibration was fitted'),
                    sa.Column('visits', sa.ARRAY(sa.Integer()), nullable=False,
                              comment='Visits of cobra_blind_move it was fitted on'),
                    sa.Column('ramp_residual_cut', sa.REAL(), nullable=False,
                              comment='Largest ramp_residual a move is fitted with [mm]'),
                    sa.Column('min_runs', sa.Integer(), nullable=False,
                              comment='Passing runs a cobra needs to be calibrated'),
                    sa.Column('model', sa.String(), nullable=False,
                              comment='Fitted model, e.g. gain-lsq'),
                    sa.Column('model_version', sa.Integer(), nullable=False,
                              comment='Version of the model'),
                    sa.Column('n_calibrated', sa.Integer(), nullable=False,
                              comment='Number of calibrated cobras'),
                    sa.Column('loo_bias', sa.REAL(), nullable=True,
                              comment='Leave-one-out median of reached minus wanted depth [dot fraction]'),
                    sa.Column('loo_spread', sa.REAL(), nullable=True,
                              comment='Leave-one-out 16-84% half-width of that error [dot fraction]'),
                    sa.Column('loo_within_05', sa.REAL(), nullable=True,
                              comment='Leave-one-out fraction of cobras within 0.05 of the depth wanted'),
                    sa.PrimaryKeyConstraint('blind_move_calib_id'))

    op.create_table('cobra_blind_move_gain',
                    sa.Column('blind_move_calib_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='Calibration identifier'),
                    sa.Column('cobra_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='Cobra identifier (1..2394)'),
                    sa.Column('landing_gain', sa.REAL(), nullable=True,
                              comment='Gain of the landing; NULL if not fitted'),
                    sa.Column('target_gain', sa.REAL(), nullable=True,
                              comment='Gain of the push; NULL if not fitted'),
                    sa.Column('n_runs', sa.Integer(), nullable=True,
                              comment='Passing runs fitted'),
                    sa.Column('landing_scatter', sa.REAL(), nullable=True,
                              comment='Standard deviation of the per-run landing gain'),
                    sa.Column('target_scatter', sa.REAL(), nullable=True,
                              comment='Standard deviation of the per-run push gain'),
                    sa.Column('calibrated', sa.Boolean(), nullable=False,
                              comment='Whether the gains are used'),
                    sa.ForeignKeyConstraint(['blind_move_calib_id'], ['blind_move_calib.blind_move_calib_id']),
                    sa.ForeignKeyConstraint(['cobra_id'], ['cobra.cobra_id']),
                    sa.PrimaryKeyConstraint('blind_move_calib_id', 'cobra_id'))

    op.create_table('blind_move_calib_validation',
                    sa.Column('blind_move_calib_validation_id', sa.Integer(), autoincrement=True,
                              nullable=False, comment='Validation identifier'),
                    sa.Column('blind_move_calib_id', sa.Integer(), nullable=False,
                              comment='Calibration validated'),
                    sa.Column('validated_at', sa.DateTime(timezone=True), nullable=False,
                              comment='Time of the validation'),
                    sa.Column('visits', sa.ARRAY(sa.Integer()), nullable=False,
                              comment='Aimed visits of cobra_blind_move it was checked on'),
                    sa.Column('n_cobras', sa.Integer(), nullable=True, comment='Cobras checked'),
                    sa.Column('bias', sa.REAL(), nullable=True,
                              comment='Median of reached minus wanted depth [dot fraction]'),
                    sa.Column('spread', sa.REAL(), nullable=True,
                              comment='16-84% half-width of that error [dot fraction]'),
                    sa.Column('within_05', sa.REAL(), nullable=True,
                              comment='Fraction of cobras within 0.05 of the depth wanted'),
                    sa.Column('within_10', sa.REAL(), nullable=True,
                              comment='Fraction of cobras within 0.10 of the depth wanted'),
                    sa.Column('coverage', sa.REAL(), nullable=True,
                              comment='Fraction of the dot cobras aimed and measured'),
                    sa.Column('reason', sa.String(), nullable=False,
                              comment='validation, or rollback and why'),
                    sa.ForeignKeyConstraint(['blind_move_calib_id'], ['blind_move_calib.blind_move_calib_id']),
                    sa.PrimaryKeyConstraint('blind_move_calib_validation_id'))


def downgrade():
    op.drop_table('blind_move_calib_validation')
    op.drop_table('cobra_blind_move_gain')
    op.drop_table('blind_move_calib')
