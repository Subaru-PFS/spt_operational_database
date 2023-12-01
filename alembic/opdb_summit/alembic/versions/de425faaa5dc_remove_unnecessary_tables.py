"""remove unnecessary tables

Revision ID: de425faaa5dc
Revises: 77d27b6d1431
Create Date: 2023-12-01 11:36:59.890014

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'de425faaa5dc'
down_revision = '77d27b6d1431'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('guide_stars_obj_type_id_fkey', 'guide_stars', type_='foreignkey')
    op.drop_constraint('drp1d_obj_type_id_fkey', 'drp1d', type_='foreignkey')
    op.drop_table('drp_ga')
    op.drop_table('drp1d_line')
    op.drop_table('drp1d_redshift')
    op.drop_table('drp1d')
    op.drop_table('pfs_arm')
    op.drop_table('line_list')
    op.drop_table('star_type')
    op.drop_table('pfs_object')
    op.drop_table('obs_fiber')
    op.drop_table('processing_status')
    op.drop_table('visits_to_combine')
    op.drop_table('pfs_arm_obj')
    op.drop_table('psf_model')
    op.drop_table('target')
    op.drop_table('target_type')
    op.drop_table('tile')
    op.drop_table('program')
    op.drop_table('proposal')
    op.drop_table('sky_model')
    op.drop_table('qa_type')
    op.drop_table('visit_hash')
    op.drop_table('flux_calib')
    op.drop_table('obj_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drp1d',
                    sa.Column('pfs_object_id', sa.BIGINT(), autoincrement=False, nullable=False),
                    sa.Column('z_best', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('z_best_err', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('z_best_reliability', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('obj_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('flags', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('processed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
                    sa.Column('drp1d_version', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['obj_type_id'], ['obj_type.obj_type_id'], name='drp1d_obj_type_id_fkey'),
                    sa.ForeignKeyConstraint(['pfs_object_id'], ['pfs_object.pfs_object_id'], name='drp1d_pfs_object_id_fkey'),
                    sa.PrimaryKeyConstraint('pfs_object_id', 'processed_at', name='drp1d_pkey'),
                    sa.UniqueConstraint('pfs_object_id', 'processed_at', name='drp1d_pfs_object_id_processed_at_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('sky_model',
                    sa.Column('sky_model_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('pfs_visit_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('sps_camera_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id'], name='sky_model_pfs_visit_id_fkey'),
                    sa.ForeignKeyConstraint(['sps_camera_id'], ['sps_camera.sps_camera_id'], name='sky_model_sps_camera_id_fkey'),
                    sa.PrimaryKeyConstraint('sky_model_id', name='sky_model_pkey'),
                    sa.UniqueConstraint('sky_model_id', name='sky_model_sky_model_id_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('target',
                    sa.Column('target_id', sa.BIGINT(), server_default=sa.text("nextval('target_target_id_seq'::regclass)"), autoincrement=True, nullable=False),
                    sa.Column('program_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('obj_id', sa.BIGINT(), autoincrement=False, nullable=True),
                    sa.Column('ra', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
                    sa.Column('decl', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
                    sa.Column('tract', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('patch', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('priority', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('target_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('cat_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('cat_obj_id', sa.BIGINT(), autoincrement=False, nullable=True),
                    sa.Column('fiber_mag_g', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('fiber_mag_r', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('fiber_mag_i', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('fiber_mag_z', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('fiber_mag_y', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('fiber_mag_j', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('fiducial_exptime', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('photz', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('is_medium_resolution', sa.BOOLEAN(), autoincrement=False, nullable=True),
                    sa.Column('qa_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('qa_lambda_min', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('qa_lambda_max', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('qa_threshold', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('qa_line_flux', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('completeness', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('is_finished', sa.BOOLEAN(), autoincrement=False, nullable=True),
                    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['cat_id'], ['input_catalog.cat_id'], name='target_cat_id_fkey'),
                    sa.ForeignKeyConstraint(['program_id'], ['program.program_id'], name='target_program_id_fkey'),
                    sa.ForeignKeyConstraint(['qa_type_id'], ['qa_type.qa_type_id'], name='target_qa_type_id_fkey'),
                    sa.ForeignKeyConstraint(['target_type_id'], ['target_type.target_type_id'], name='target_target_type_id_fkey'),
                    sa.PrimaryKeyConstraint('target_id', name='target_pkey'),
                    sa.UniqueConstraint('target_id', name='target_target_id_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('psf_model',
                    sa.Column('psf_model_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('pfs_visit_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('sps_camera_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id'], name='psf_model_pfs_visit_id_fkey'),
                    sa.ForeignKeyConstraint(['sps_camera_id'], ['sps_camera.sps_camera_id'], name='psf_model_sps_camera_id_fkey'),
                    sa.PrimaryKeyConstraint('psf_model_id', name='psf_model_pkey'),
                    sa.UniqueConstraint('psf_model_id', name='psf_model_psf_model_id_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('tile',
                    sa.Column('tile_id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('program_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('tile', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('ra_center', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
                    sa.Column('dec_center', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
                    sa.Column('pa', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('is_finished', sa.BOOLEAN(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['program_id'], ['program.program_id'], name='tile_program_id_fkey'),
                    sa.PrimaryKeyConstraint('tile_id', name='tile_pkey'),
                    sa.UniqueConstraint('tile_id', name='tile_tile_id_key')
                    )
    op.create_table('pfs_arm_obj',
                    sa.Column('pfs_visit_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('cobra_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('flags', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('qa_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('qa_value', sa.REAL(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['cobra_id'], ['cobra.cobra_id'], name='pfs_arm_obj_cobra_id_fkey'),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id'], name='pfs_arm_obj_pfs_visit_id_fkey'),
                    sa.ForeignKeyConstraint(['qa_type_id'], ['qa_type.qa_type_id'], name='pfs_arm_obj_qa_type_id_fkey'),
                    sa.PrimaryKeyConstraint('pfs_visit_id', 'cobra_id', name='pfs_arm_obj_pkey'),
                    sa.UniqueConstraint('pfs_visit_id', 'cobra_id', name='pfs_arm_obj_pfs_visit_id_cobra_id_key')
                    )
    op.create_table('visits_to_combine',
                    sa.Column('pfs_visit_hash', sa.BIGINT(), autoincrement=False, nullable=False),
                    sa.Column('pfs_visit_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['pfs_visit_hash'], ['visit_hash.pfs_visit_hash'], name='visits_to_combine_pfs_visit_hash_fkey'),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id'], name='visits_to_combine_pfs_visit_id_fkey'),
                    sa.UniqueConstraint('pfs_visit_id', 'pfs_visit_hash', name='visits_to_combine_pfs_visit_id_pfs_visit_hash_key')
                    )
    op.create_table('target_type',
                    sa.Column('target_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('target_type_name', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('target_type_description', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('target_type_id', name='target_type_pkey'),
                    sa.UniqueConstraint('target_type_id', name='target_type_target_type_id_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('drp1d_redshift',
                    sa.Column('pfs_object_id', sa.BIGINT(), autoincrement=False, nullable=False),
                    sa.Column('z', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('z_err', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('zrank', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('reliability', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('spec_class', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('spec_subclass', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('processed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['pfs_object_id', 'processed_at'], ['drp1d.pfs_object_id', 'drp1d.processed_at'], name='drp1d_redshift_pfs_object_id_fkey'),
                    sa.PrimaryKeyConstraint('pfs_object_id', 'processed_at', name='drp1d_redshift_pkey'),
                    sa.UniqueConstraint('pfs_object_id', 'processed_at', name='drp1d_redshift_pfs_object_id_processed_at_key')
                    )
    op.create_table('processing_status',
                    sa.Column('status_id', sa.INTEGER(), autoincrement=False, nullable=False, comment='Unique processing status identifier'),
                    sa.Column('visit_set_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('pfs_visit_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('are_data_ok', sa.BOOLEAN(), autoincrement=False, nullable=True, comment='The result of the quality assessment'),
                    sa.Column('comments', sa.VARCHAR(), autoincrement=False, nullable=True, comment='Detailed comments on the QA results'),
                    sa.Column('drp2d_version', sa.VARCHAR(), autoincrement=False, nullable=True, comment='2D-DRP version used in the processing'),
                    sa.Column('qa_version', sa.VARCHAR(), autoincrement=False, nullable=True, comment='QA version used in the processing (TBD)'),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id'], name='processing_status_pfs_visit_id_fkey'),
                    sa.PrimaryKeyConstraint('status_id', name='processing_status_pkey')
                    )
    op.create_table('drp1d_line',
                    sa.Column('pfs_object_id', sa.BIGINT(), autoincrement=False, nullable=False),
                    sa.Column('line_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('line_name', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('line_wave', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_z', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_z_err', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_sigma', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_sigma_err', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_vel', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_vel_err', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_flux', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_flux_err', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_ew', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_ew_err', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_cont_level', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('line_cont_level_err', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('processed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['line_id'], ['line_list.line_id'], name='drp1d_line_line_id_fkey'),
                    sa.ForeignKeyConstraint(['pfs_object_id', 'processed_at'], ['drp1d.pfs_object_id', 'drp1d.processed_at'], name='drp1d_line_pfs_object_id_fkey'),
                    sa.PrimaryKeyConstraint('pfs_object_id', 'line_id', 'processed_at', name='drp1d_line_pkey'),
                    sa.UniqueConstraint('pfs_object_id', 'processed_at', 'line_id', name='drp1d_line_pfs_object_id_processed_at_line_id_key')
                    )
    op.create_table('program',
                    sa.Column('program_id', sa.INTEGER(), autoincrement=False, nullable=False, comment='Unique program identifier'),
                    sa.Column('program_name', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('program_description', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('proposal_id', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('is_filler', sa.BOOLEAN(), autoincrement=False, nullable=True),
                    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.proposal_id'], name='program_proposal_id_fkey'),
                    sa.PrimaryKeyConstraint('program_id', name='program_pkey'),
                    sa.UniqueConstraint('program_id', name='program_program_id_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('flux_calib',
                    sa.Column('flux_calib_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('flux_calib_type', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('flux_calib_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('flux_calib_star_teff', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('flux_calib_star_logg', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('flux_calib_star_z', sa.REAL(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('flux_calib_id', name='flux_calib_pkey'),
                    sa.UniqueConstraint('flux_calib_id', name='flux_calib_flux_calib_id_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('obs_fiber',
                    sa.Column('pfs_visit_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('cobra_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('target_id', sa.BIGINT(), autoincrement=False, nullable=True),
                    sa.Column('exptime', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('cum_nexp', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('cum_texp', sa.REAL(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['cobra_id'], ['cobra.cobra_id'], name='obs_fiber_cobra_id_fkey'),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id'], name='obs_fiber_pfs_visit_id_fkey'),
                    sa.PrimaryKeyConstraint('pfs_visit_id', 'cobra_id', name='obs_fiber_pkey'),
                    sa.UniqueConstraint('pfs_visit_id', 'cobra_id', name='obs_fiber_pfs_visit_id_cobra_id_key')
                    )
    op.create_table('visit_hash',
                    sa.Column('pfs_visit_hash', sa.BIGINT(), autoincrement=False, nullable=False),
                    sa.Column('n_visit', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('pfs_visit_hash', name='visit_hash_pkey'),
                    sa.UniqueConstraint('pfs_visit_hash', name='visit_hash_pfs_visit_hash_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('pfs_object',
                    sa.Column('pfs_object_id', sa.BIGINT(), server_default=sa.text("nextval('pfs_object_pfs_object_id_seq'::regclass)"), autoincrement=True, nullable=False),
                    sa.Column('target_id', sa.BIGINT(), autoincrement=False, nullable=True),
                    sa.Column('tract', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('patch', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('cat_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('obj_id', sa.BIGINT(), autoincrement=False, nullable=True),
                    sa.Column('n_visit', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('pfs_visit_hash', sa.BIGINT(), autoincrement=False, nullable=True),
                    sa.Column('cum_texp', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('processed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('drp2d_version', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('flux_calib_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('flags', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('qa_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('qa_value', sa.REAL(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['flux_calib_id'], ['flux_calib.flux_calib_id'], name='pfs_object_flux_calib_id_fkey'),
                    sa.ForeignKeyConstraint(['pfs_visit_hash'], ['visit_hash.pfs_visit_hash'], name='pfs_object_pfs_visit_hash_fkey'),
                    sa.ForeignKeyConstraint(['qa_type_id'], ['qa_type.qa_type_id'], name='pfs_object_qa_type_id_fkey'),
                    sa.ForeignKeyConstraint(['target_id'], ['target.target_id'], name='pfs_object_target_id_fkey'),
                    sa.PrimaryKeyConstraint('pfs_object_id', name='pfs_object_pkey'),
                    sa.UniqueConstraint('pfs_object_id', name='pfs_object_pfs_object_id_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('star_type',
                    sa.Column('star_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('star_type_name', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('star_type_description', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('star_type_id', name='star_type_pkey'),
                    sa.UniqueConstraint('star_type_id', name='star_type_star_type_id_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('qa_type',
                    sa.Column('qa_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('qa_type_name', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('qa_type_description', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('qa_type_id', name='qa_type_pkey'),
                    sa.UniqueConstraint('qa_type_id', name='qa_type_qa_type_id_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('line_list',
                    sa.Column('line_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('line_name', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('line_wavelength', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('line_id', name='line_list_pkey'),
                    sa.UniqueConstraint('line_id', name='line_list_line_id_key')
                    )
    op.create_table('drp_ga',
                    sa.Column('pfs_object_id', sa.BIGINT(), autoincrement=False, nullable=False),
                    sa.Column('star_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('velocity', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('metallicity', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('logg', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('teff', sa.REAL(), autoincrement=False, nullable=True),
                    sa.Column('flags', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('processed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
                    sa.Column('drp_ga_version', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['pfs_object_id'], ['pfs_object.pfs_object_id'], name='drp_ga_pfs_object_id_fkey'),
                    sa.ForeignKeyConstraint(['star_type_id'], ['star_type.star_type_id'], name='drp_ga_star_type_id_fkey'),
                    sa.PrimaryKeyConstraint('pfs_object_id', 'processed_at', name='drp_ga_pkey'),
                    sa.UniqueConstraint('pfs_object_id', 'processed_at', name='drp_ga_pfs_object_id_processed_at_key')
                    )
    op.create_table('proposal',
                    sa.Column('proposal_id', sa.VARCHAR(), autoincrement=False, nullable=False, comment='Unique identifier for proposal'),
                    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True, comment='Creation time [YYYY-MM-DDThh:mm:ss]'),
                    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True, comment='Update time [YYYY-MM-DDThh:mm:ss]'),
                    sa.PrimaryKeyConstraint('proposal_id', name='proposal_pkey'),
                    sa.UniqueConstraint('proposal_id', name='proposal_proposal_id_key')
                    )
    op.create_table('obj_type',
                    sa.Column('obj_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('obj_type_name', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('obj_type_description', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('obj_type_id', name='obj_type_pkey'),
                    sa.UniqueConstraint('obj_type_id', name='obj_type_obj_type_id_key')
                    )
    op.create_table('pfs_arm',
                    sa.Column('pfs_visit_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('calib_set_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('sky_model_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('psf_model_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('flags', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('processed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('drp2d_version', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['calib_set_id'], ['calib_set.calib_set_id'], name='pfs_arm_calib_set_id_fkey'),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id'], name='pfs_arm_pfs_visit_id_fkey'),
                    sa.ForeignKeyConstraint(['psf_model_id'], ['psf_model.psf_model_id'], name='pfs_arm_psf_model_id_fkey'),
                    sa.ForeignKeyConstraint(['sky_model_id'], ['sky_model.sky_model_id'], name='pfs_arm_sky_model_id_fkey'),
                    sa.PrimaryKeyConstraint('pfs_visit_id', name='pfs_arm_pkey'),
                    sa.UniqueConstraint('pfs_visit_id', name='pfs_arm_pfs_visit_id_key')
                    )
    op.create_foreign_key('guide_stars_obj_type_id_fkey', 'guide_stars', 'obj_type', ['obj_type_id'], ['obj_type_id'])
    # ### end Alembic commands ###
