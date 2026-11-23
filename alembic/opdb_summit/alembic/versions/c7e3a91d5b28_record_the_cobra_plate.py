"""record where the cobra plate was in each MCS frame

cobra_plate_transformation
    The anchor cobras' similarity carrying the frame of the XML centres into PFI mm, one row
    per MCS frame: the fit on the frame alone (frame_*) and the plate applied to the cobra
    centres.

Revision ID: c7e3a91d5b28
Revises: b81e5c2d4f90
Create Date: 2026-11-23 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'c7e3a91d5b28'
down_revision = 'b81e5c2d4f90'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('cobra_plate_transformation',
                    sa.Column('mcs_frame_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='MCS frame identifier as generated from Gen2'),
                    sa.Column('frame_x0', sa.REAL(), nullable=True,
                              comment='Shift x of the fit on this frame [mm]'),
                    sa.Column('frame_y0', sa.REAL(), nullable=True,
                              comment='Shift y of the fit on this frame [mm]'),
                    sa.Column('frame_scale', sa.REAL(), nullable=True,
                              comment='Scale of the fit on this frame'),
                    sa.Column('frame_theta', sa.REAL(), nullable=True,
                              comment='Rotation of the fit on this frame [rad]'),
                    sa.Column('frame_n_anchors', sa.Integer(), nullable=True,
                              comment='Anchors kept in the fit on this frame'),
                    sa.Column('frame_rms', sa.REAL(), nullable=True,
                              comment='Rms residual of the anchors kept in the fit on this frame [um]'),
                    sa.Column('x0', sa.REAL(), nullable=True, comment='Shift x of the plate applied [mm]'),
                    sa.Column('y0', sa.REAL(), nullable=True, comment='Shift y of the plate applied [mm]'),
                    sa.Column('scale', sa.REAL(), nullable=True, comment='Scale of the plate applied'),
                    sa.Column('theta', sa.REAL(), nullable=True, comment='Rotation of the plate applied [rad]'),
                    sa.Column('n_frames', sa.Integer(), nullable=True,
                              comment='Frames of the visit the plate applied was fitted on; 0 for the identity'),
                    sa.Column('n_anchors', sa.Integer(), nullable=True,
                              comment='Anchors kept in the fit of the plate applied'),
                    sa.Column('rms', sa.REAL(), nullable=True,
                              comment='Rms residual of the anchors kept in the fit of the plate applied [um]'),
                    sa.ForeignKeyConstraint(['mcs_frame_id'], ['mcs_exposure.mcs_frame_id']),
                    sa.PrimaryKeyConstraint('mcs_frame_id'),
                    sa.UniqueConstraint('mcs_frame_id'))


def downgrade():
    op.drop_table('cobra_plate_transformation')
