"""add pfs_config.blind_move_calib_id

pfs_config.blind_move_calib_id
    The blind-move calibration the convergence aimed its dot cobras through, from the
    pfsConfig convergence parameter blindMoveCalibId; NULL if none.

Revision ID: d4a8e2f1b6c3
Revises: c71e4b9d2f05
Create Date: 2026-11-04 20:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'd4a8e2f1b6c3'
down_revision = 'c71e4b9d2f05'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('pfs_config',
                  sa.Column('blind_move_calib_id', sa.Integer(), nullable=True,
                            comment='Blind-move calibration aiming the dot cobras; NULL if none'))
    op.create_foreign_key('pfs_config_blind_move_calib_id_fkey', 'pfs_config', 'blind_move_calib',
                          ['blind_move_calib_id'], ['blind_move_calib_id'])


def downgrade():
    op.drop_constraint('pfs_config_blind_move_calib_id_fkey', 'pfs_config', type_='foreignkey')
    op.drop_column('pfs_config', 'blind_move_calib_id')
