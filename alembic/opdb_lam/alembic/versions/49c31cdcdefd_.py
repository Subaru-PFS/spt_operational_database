"""empty message

Revision ID: 49c31cdcdefd
Revises: 8b95935b1eb9
Create Date: 2022-09-01 15:26:49.537024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49c31cdcdefd'
down_revision = '8b95935b1eb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cobra_status',
    sa.Column('mcs_frame_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('cobra_id', sa.Integer(), autoincrement=False, nullable=False, comment='Fiber identifier'),
    sa.Column('spot_id', sa.Integer(), nullable=True, comment='Corresponding MCS image spot identifier '),
    sa.Column('pfs_config_id', sa.BigInteger(), nullable=True),
    sa.Column('iteration', sa.Integer(), nullable=True, comment='Iteration number for this frame'),
    sa.Column('pfi_target_x_mm', sa.REAL(), nullable=True, comment='Target x-position on the PFI as determined from the  pfs_design_fiber table [mm]'),
    sa.Column('pfi_target_y_mm', sa.REAL(), nullable=True, comment='Target y-position on the PFI as determined from the  pfs_design_fiber table [mm]'),
    sa.Column('pfi_center_x_mm', sa.REAL(), nullable=True, comment='Actual x-position on the PFI [mm]'),
    sa.Column('pfi_center_y_mm', sa.REAL(), nullable=True, comment='Actual y-position on the PFI [mm]'),
    sa.ForeignKeyConstraint(['mcs_frame_id', 'spot_id'], ['mcs_data.mcs_frame_id', 'mcs_data.spot_id'], ),
    sa.PrimaryKeyConstraint('mcs_frame_id', 'cobra_id'),
    sa.UniqueConstraint('mcs_frame_id', 'cobra_id')
    )
    op.create_index(op.f('ix_cobra_status_mcs_frame_id'), 'cobra_status', ['mcs_frame_id'], unique=False)
    op.create_table('cobra_movement',
    sa.Column('mcs_frame_id', sa.Integer(), autoincrement=False, nullable=False, comment='MCS frame identifier. Provided by Gen2'),
    sa.Column('cobra_id', sa.Integer(), autoincrement=False, nullable=False, comment='Fiber identifier'),
    sa.Column('cobra_motor_calib_id', sa.Integer(), nullable=True),
    sa.Column('motor_num_step_theta', sa.Integer(), nullable=True, comment='the number of steps the theta motor has undertaken'),
    sa.Column('motor_on_time_theta', sa.REAL(), nullable=True, comment='the theta motor ontime value'),
    sa.Column('motor_num_step_phi', sa.Integer(), nullable=True, comment='the number of steps the phi motor has undertaken'),
    sa.Column('motor_on_time_phi', sa.REAL(), nullable=True, comment='the phi motor ontime value'),
    sa.ForeignKeyConstraint(['cobra_motor_calib_id'], ['cobra_motor_calib.cobra_motor_calib_id'], ),
    sa.ForeignKeyConstraint(['mcs_frame_id', 'cobra_id'], ['cobra_status.mcs_frame_id', 'cobra_status.cobra_id'], ),
    sa.PrimaryKeyConstraint('mcs_frame_id', 'cobra_id'),
    sa.UniqueConstraint('mcs_frame_id', 'cobra_id')
    )
    op.create_index(op.f('ix_cobra_movement_mcs_frame_id'), 'cobra_movement', ['mcs_frame_id'], unique=False)
    op.drop_index('ix_cobra_match_mcs_frame_id', table_name='cobra_match')
    op.drop_table('cobra_match')
    op.drop_table('cobra_target')
    op.add_column('pfs_design_fiber', sa.Column('pfi_target_x_mm', sa.REAL(), nullable=True, comment='Target x-position on the PFI [mm]'))
    op.add_column('pfs_design_fiber', sa.Column('pfi_target_y_mm', sa.REAL(), nullable=True, comment='Target y-position on the PFI [mm]'))
    op.drop_column('pfs_design_fiber', 'pfi_nominal_x_mm')
    op.drop_column('pfs_design_fiber', 'pfi_nominal_y_mm')
    op.drop_constraint('sps_annotation_annotation_id_key', 'sps_annotation', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('sps_annotation_annotation_id_key', 'sps_annotation', ['annotation_id'])
    op.add_column('pfs_design_fiber', sa.Column('pfi_nominal_y_mm', sa.REAL(), autoincrement=False, nullable=True, comment='Nominal y-position on the PFI [mm]'))
    op.add_column('pfs_design_fiber', sa.Column('pfi_nominal_x_mm', sa.REAL(), autoincrement=False, nullable=True, comment='Nominal x-position on the PFI [mm]'))
    op.drop_column('pfs_design_fiber', 'pfi_target_y_mm')
    op.drop_column('pfs_design_fiber', 'pfi_target_x_mm')
    op.create_table('cobra_target',
    sa.Column('pfs_visit_id', sa.INTEGER(), autoincrement=False, nullable=False, comment='PFS visit identifier'),
    sa.Column('iteration', sa.INTEGER(), autoincrement=False, nullable=False, comment='Iteration number for this frame'),
    sa.Column('cobra_id', sa.INTEGER(), autoincrement=False, nullable=False, comment='Fiber identifier'),
    sa.Column('pfs_config_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('pfi_nominal_x_mm', sa.REAL(), autoincrement=False, nullable=True, comment='Nominal x-position on the PFI as determined from the  pfs_design_fiber table [mm]'),
    sa.Column('pfi_nominal_y_mm', sa.REAL(), autoincrement=False, nullable=True, comment='Nominal y-position on the PFI as determined from the  pfs_design_fiber table [mm]'),
    sa.Column('pfi_target_x_mm', sa.REAL(), autoincrement=False, nullable=True, comment='Target x-position on the PFI for each iteration'),
    sa.Column('pfi_target_y_mm', sa.REAL(), autoincrement=False, nullable=True, comment='Target y-position on the PFI for each iteration'),
    sa.Column('cobra_motor_model_id_theta', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('motor_target_theta', sa.REAL(), autoincrement=False, nullable=True, comment='the target angle of the theta motor'),
    sa.Column('motor_num_step_theta', sa.INTEGER(), autoincrement=False, nullable=True, comment='the number of steps the theta motor has undertaken'),
    sa.Column('motor_on_time_theta', sa.REAL(), autoincrement=False, nullable=True, comment='the theta motor ontime value'),
    sa.Column('cobra_motor_model_id_phi', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('motor_target_phi', sa.REAL(), autoincrement=False, nullable=True, comment='the target angle of the phi motor'),
    sa.Column('motor_num_step_phi', sa.INTEGER(), autoincrement=False, nullable=True, comment='the number of steps the phi motor has undertaken'),
    sa.Column('motor_on_time_phi', sa.REAL(), autoincrement=False, nullable=True, comment='the phi motor ontime value'),
    sa.Column('flags', sa.INTEGER(), autoincrement=False, nullable=True, comment='flags for movement etc.'),
    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id'], name='cobra_target_pfs_visit_id_fkey'),
    sa.PrimaryKeyConstraint('pfs_visit_id', 'iteration', 'cobra_id', name='cobra_target_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('cobra_match',
    sa.Column('mcs_frame_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('spot_id', sa.INTEGER(), autoincrement=False, nullable=False, comment='Corresponding MCS image spot identifier '),
    sa.Column('pfs_visit_id', sa.INTEGER(), autoincrement=False, nullable=True, comment='PFS visit identifier'),
    sa.Column('iteration', sa.INTEGER(), autoincrement=False, nullable=True, comment='Iteration number for this frame'),
    sa.Column('cobra_id', sa.INTEGER(), autoincrement=False, nullable=True, comment='Fiber identifier'),
    sa.Column('pfi_center_x_mm', sa.REAL(), autoincrement=False, nullable=True, comment='Actual x-position on the PFI [mm]'),
    sa.Column('pfi_center_y_mm', sa.REAL(), autoincrement=False, nullable=True, comment='Actual y-position on the PFI [mm]'),
    sa.Column('flags', sa.INTEGER(), autoincrement=False, nullable=True, comment='flags for movement etc.'),
    sa.ForeignKeyConstraint(['mcs_frame_id', 'spot_id'], ['mcs_data.mcs_frame_id', 'mcs_data.spot_id'], name='cobra_match_mcs_frame_id_fkey'),
    sa.ForeignKeyConstraint(['pfs_visit_id', 'iteration', 'cobra_id'], ['cobra_target.pfs_visit_id', 'cobra_target.iteration', 'cobra_target.cobra_id'], name='cobra_match_pfs_visit_id_fkey'),
    sa.PrimaryKeyConstraint('mcs_frame_id', 'spot_id', name='cobra_match_pkey')
    )
    op.create_index('ix_cobra_match_mcs_frame_id', 'cobra_match', ['mcs_frame_id'], unique=False)
    op.drop_index(op.f('ix_cobra_movement_mcs_frame_id'), table_name='cobra_movement')
    op.drop_table('cobra_movement')
    op.drop_index(op.f('ix_cobra_status_mcs_frame_id'), table_name='cobra_status')
    op.drop_table('cobra_status')
    # ### end Alembic commands ###
