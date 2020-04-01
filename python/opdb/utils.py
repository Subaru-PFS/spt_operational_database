import io
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import models


class OpDB(object):

    def __init__(self, hostname='localhost', port='5432', dbname='test', username='test', passwd='ask someone', dialect='postgresql'):
        self.dbinfo = "{0}://{1}:{2}@{3}:{4}/{5}".format(dialect,
                                                         username,
                                                         passwd,
                                                         hostname,
                                                         port,
                                                         dbname)

    def connect(self):
        self.engine = create_engine(self.dbinfo)
        SessionClass = sessionmaker(self.engine)
        self.session = SessionClass()
        print('connecting to {0}'.format(self.dbinfo))

    def close(self):
        self.session.close()

    def reset(self):
        self.session.query(models.drp1d_redshift).delete()
        self.session.query(models.drp1d_line).delete()
        self.session.query(models.drp1d).delete()
        self.session.query(models.drp_ga).delete()
        self.session.query(models.star_type).delete()
        self.session.query(models.line_list).delete()
        self.session.query(models.guide_stars).delete()
        self.session.query(models.tel_condition).delete()
        self.session.query(models.cloud_condition).delete()
        self.session.query(models.visits_to_combine).delete()
        self.session.query(models.tel_visit).delete()
        self.session.query(models.pfs_arm_obj).delete()
        self.session.query(models.pfs_arm).delete()
        self.session.query(models.pfs_object).delete()
        self.session.query(models.obs_fiber).delete()
        self.session.query(models.visit_hash).delete()
        self.session.query(models.flux_calib).delete()
        self.session.query(models.obj_type).delete()
        self.session.query(models.calib_set).delete()
        self.session.query(models.calib).delete()
        self.session.query(models.sps_exposure).delete()
        self.session.query(models.sps_condition).delete()
        self.session.query(models.processing_status).delete()
        self.session.query(models.sps_annotation).delete()
        self.session.query(models.sps_visit).delete()
        self.session.query(models.sps_camera).delete()
        self.session.query(models.visit_set).delete()
        self.session.query(models.sky_model).delete()
        self.session.query(models.psf_model).delete()
        self.session.query(models.cobra_convergence_test).delete()
        self.session.query(models.cobra_motor_map).delete()
        self.session.query(models.cobra_motor_model).delete()
        self.session.query(models.cobra_movement).delete()
        self.session.query(models.cobra_status).delete()
        self.session.query(models.cobra_geometry).delete()
        self.session.query(models.cobra_motor_calib).delete()
        self.session.query(models.cobra_motor_axis).delete()
        self.session.query(models.cobra_motor_direction).delete()
        self.session.query(models.pfs_config_fiber).delete()
        self.session.query(models.pfs_config).delete()
        self.session.query(models.pfs_design_fiber).delete()
        self.session.query(models.pfs_design).delete()
        self.session.query(models.mcs_boresight).delete()
        self.session.query(models.mcs_data).delete()
        self.session.query(models.mcs_exposure).delete()
        self.session.query(models.pfs_visit).delete()
        self.session.query(models.cobra).delete()
        self.session.query(models.sps_camera).delete()
        self.session.query(models.sps_module).delete()
        self.session.query(models.fiducial_fiber_geometry).delete()
        self.session.query(models.fiducial_fiber).delete()
        self.session.query(models.target).delete()
        self.session.query(models.target_type).delete()
        self.session.query(models.input_catalog).delete()
        self.session.query(models.qa_type).delete()
        self.session.query(models.tile).delete()
        self.session.query(models.program).delete()
        self.session.query(models.proposal).delete()
        self.session.execute("ALTER SEQUENCE pfs_object_pfs_object_id_seq RESTART WITH 1")
        self.session.execute("ALTER SEQUENCE calib_set_calib_set_id_seq RESTART WITH 1")
        self.session.execute("ALTER SEQUENCE cobra_motor_model_cobra_motor_model_id_seq RESTART WITH 1")
        self.session.execute("ALTER SEQUENCE cobra_motor_calib_cobra_motor_calib_id_seq RESTART WITH 1")
        self.session.execute("ALTER SEQUENCE pfs_config_pfs_config_id_seq RESTART WITH 1")
        self.session.execute("ALTER SEQUENCE target_target_id_seq RESTART WITH 1")
        self.session.execute("ALTER SEQUENCE tile_tile_id_seq RESTART WITH 1")
        self.session.commit()

    '''
        #####################################################
        functionality to insert information into the database
        #####################################################
    '''

    def insert_proposal(self, data):
        '''
            Description
            -----------
                Insert information into `proposal`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `proposal_id` : `str`
                    `created_at` : `datetime`
                    `updated_at` : `datetime`
        '''
        self.session.execute(models.proposal.__table__.insert(), data)
        self.session.commit()

    def insert_program(self, data):
        '''
            Description
            -----------
                Insert information into `program`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `program_id` : `int`
                    `program_name` : `str`
                    `program_description` : `str`
                    `proposal_id` : `str`
                    `is_filler` : `bool`
                    `created_at` : `datetime`
                    `updated_at` : `datetime`
        '''
        self.session.execute(models.program.__table__.insert(), data)
        self.session.commit()

    def insert_tile(self, data):
        '''
            Description
            -----------
                Insert information into `tile`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `tile_id` : `int`
                    `program_id` : `int`
                    `tile` : `int`
                    `ra_center` : `float`
                    `dec_center` : `float`
                    `pa` : `float`
                    `is_finished` : `bool`
        '''
        self.session.execute(models.tile.__table__.insert(), data)
        self.session.commit()

    def insert_target_type(self, data):
        '''
            Description
            -----------
                Insert information into `target_type`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `target_type_id` : `int`
                    `target_type_name` : `str`
                    `target_type_description` : `str`
                    `created_at` : `datetime`
                    `updated_at` : `datetime`
        '''
        self.session.execute(models.target_type.__table__.insert(), data)
        self.session.commit()

    def insert_input_catalog(self, data):
        '''
            Description
            -----------
                Insert information into `input_catalog`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `cat_id` : `int`
                    `input_catalog_name` : `str`
                    `input_catalog_description` : `str`
                    `created_at` : `datetime`
                    `updated_at` : `datetime`
        '''
        self.session.execute(models.input_catalog.__table__.insert(), data)
        self.session.commit()

    def insert_qa_type(self, data):
        '''
            Description
            -----------
                Insert information into `qa_type`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `qa_type_id` : `int`
                    `qa_type_name` : `str`
                    `qa_type_description` : `str`
                    `created_at` : `datetime`
                    `updated_at` : `datetime`
        '''
        self.session.execute(models.qa_type.__table__.insert(), data)
        self.session.commit()

    def insert_target_from_buffer(self, data):
        '''
            Description
            -----------
                Insert information into `target`

            Parameters
            ----------
                data : io.StringIO (comma-separated)

            Returns
            -------
                None

            Note
            ----
                `data` list should include the following columns:
                    `program_id` : `int`
                    `obj_id` : `bigint`
                    `ra` : `float`
                    `decl` : `float`
                    `tract` : `int`
                    `patch` : `str`
                    `priority` : `float`
                    `target_type_id` : `int`
                    `cat_id` : `int`
                    `cat_obj_id` : `bigint`
                    `fiber_mag_g` : `float`
                    `fiber_mag_r` : `float`
                    `fiber_mag_i` : `float`
                    `fiber_mag_z` : `float`
                    `fiber_mag_y` : `float`
                    `fiber_mag_j` : `float`
                    `fiducial_exptime` : `float`
                    `photz` : `float`
                    `is_medium_resolution` : `bool`
                    `qa_type_id` : `int`
                    `qa_lambda_min` : `float`
                    `qa_lambda_max` : `float`
                    `qa_threshold` : `float`
                    `qa_line_flux` : `float`
                    `completeness` : `float`
                    `is_finished` : `bool`
                    `created_at` : `datetime`
                    `updated_at` : `datetime`
        '''
        colnames = ('program_id', 'obj_id', 'ra', 'decl', 'tract', 'patch', 'priority', 'target_type_id', 'cat_id', 'cat_obj_id', 'fiber_mag_g', 'fiber_mag_r', 'fiber_mag_i', 'fiber_mag_z', 'fiber_mag_y', 'fiber_mag_j', 'fiducial_exptime', 'photz', 'is_medium_resolution', 'qa_type_id', 'qa_lambda_min', 'qa_lambda_max', 'qa_threshold', 'qa_line_flux', 'completeness', 'is_finished', 'created_at', 'updated_at')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.copy_from(data, 'target', ',', columns=colnames)
        conn.commit()
        cur.close()
        conn.close()

    def insert_beam_switch_mode(self, data):
        '''
            Description
            -----------
                Insert information into `beam_switch_mode`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `beam_switch_mode_id` : `int`
                    `beam_switch_mode_name` : `str`
                    `beam_switch_mode_description` : `str`
        '''
        self.session.execute(models.beam_switch_mode.__table__.insert(), data)
        self.session.commit()

    def insert_pfs_design(self, data):
        '''
            Description
            -----------
                Insert information into `pfs_design`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `pfs_design_id` : `bigint`
                    `tile_id` : `int`
                    `ra_center_designed` : `float`
                    `dec_center_designed` : `float`
                    `pa_designed` : `float`
                    `num_sci_designed` : `int`
                    `num_cal_designed` : `int`
                    `num_sky_designed` : `int`
                    `num_guide_stars` : `int`
                    `exptime_tot` : `float`
                    `exptime_min` : `float`
                    `ets_version` : `str`
                    `ets_assigner` : `str`
                    `designed_at` : `datetime`
                    `to_be_observed_at` : `datetime`
                    `is_obsolete` : `bool`
        '''
        self.session.execute(models.pfs_design.__table__.insert(), data)
        self.session.commit()

    def insert_pfs_design_fiber(self, data):
        '''
            Description
            -----------
                Insert information into `pfs_design_fiber`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `pfs_design_id` : `bigint`
                    `cobra_id` : `int`
                    `target_id` : `bigint`
                    `pfi_target_x_mm` : `float`
                    `pfi_target_y_mm` : `float`
                    `ets_priority` : `int`
                    `ets_cost_function` : `float`
                    `ets_cobra_motor_movement` : `str`
                    `is_on_source` : `bool`
        '''
        self.session.execute(models.pfs_design_fiber.__table__.insert(), data)
        self.session.commit()

    def insert_pfs_design_fiber_from_buffer(self, data):
        '''
            Description
            -----------
                Insert information into `pfs_design_fiber`

            Parameters
            ----------
                data : io.StringIO (comma-separated)

            Returns
            -------
                None

            Note
            ----
                `data` list should include the following columns:
                    `pfs_design_id` : `bigint`
                    `cobra_id` : `int`
                    `target_id` : `bigint`
                    `pfi_target_x_mm` : `float`
                    `pfi_target_y_mm` : `float`
                    `ets_priority` : `int`
                    `ets_cost_function` : `float`
                    `ets_cobra_motor_movement` : `str`
                    `is_on_source` : `bool`
        '''
        colnames = ('pfs_design_id', 'cobra_id', 'target_id', 'pfi_target_x_mm', 'pfi_target_y_mm', 'ets_priority', 'ets_cost_function', 'ets_cobra_motor_movement', 'is_on_source')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.copy_from(data, 'pfs_design_fiber', ',', columns=colnames)
        conn.commit()
        cur.close()
        conn.close()

    def insert_pfs_config(self, data):
        '''
            Description
            -----------
                Insert information into `pfs_config`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `pfs_design_id` : `bigint`
                    `visit0` : `int`
                    `ra_center_config` : `float`
                    `dec_center_config` : `float`
                    `ra_config` : `float`
                    `converg_num_iter` : `int`
                    `converg_elapsed_time` : `float`
                    `alloc_rms_scatter` : `float`
                    `allocated_at` : `datetime`
                    `was_observed` : `bool`
        '''
        res = self.session.execute(models.pfs_config.__table__.insert(), data)
        self.session.commit()
        # get primary_keys
        primary_keys = res.inserted_primary_key
        return primary_keys

    def insert_pfs_config_fiber(self, data):
        '''
            Description
            -----------
                Insert information into `pfs_config_fiber`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `pfs_config_id` : `bigint`
                    `cobra_id` : `int`
                    `target_id` : `bigint`
                    `pfi_center_final_x_mm` : `float`
                    `pfi_center_final_y_mm` : `float`
                    `motor_map_summary` : `str`
                    `config_elapsed_time` : `float`
                    `is_on_source` : `bool`
        '''
        self.session.execute(models.pfs_config_fiber.__table__.insert(), data)
        self.session.commit()

    def insert_pfs_config_fiber_from_buffer(self, data):
        '''
            Description
            -----------
                Insert information into `pfs_config_fiber`

            Parameters
            ----------
                data : io.StringIO (comma-separated)

            Returns
            -------
                None

            Note
            ----
                `data` list should include the following columns:
                    `pfs_config_id` : `bigint`
                    `cobra_id` : `int`
                    `target_id` : `bigint`
                    `pfi_center_final_x_mm` : `float`
                    `pfi_center_final_y_mm` : `float`
                    `motor_map_summary` : `str`
                    `config_elapsed_time` : `float`
                    `is_on_source` : `bool`
        '''
        colnames = ('pfs_config_id', 'cobra_id', 'target_id', 'pfi_center_final_x_mm', 'pfi_center_final_y_mm', 'motor_map_summary', 'config_elapsed_time', 'is_on_source')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.copy_from(data, 'pfs_config_fiber', ',', columns=colnames)
        conn.commit()
        cur.close()
        conn.close()

    def insert_sps_module(self, data):
        '''
            Description
            -----------
                Insert information into `sps_module`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `sps_module_id` : `int`
                    `description` : `str`
        '''
        self.session.execute(models.sps_module.__table__.insert(), data)
        self.session.commit()

    def insert_sps_camera(self, data):
        '''
            Description
            -----------
                Insert information into `sps_camera`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `sps_camera_id` : `int`
                    `sps_module_id` : `int`
                    `arm` : `str`
                    `arm_num` : `int`
        '''
        self.session.execute(models.sps_camera.__table__.insert(), data)
        self.session.commit()

    def insert_fiducial_fiber(self, data):
        '''
            Description
            -----------
                Insert information into `fiducial_fiber`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `fiducial_fiber_id` : `int`
                    `field_on_pfi` : `int`
                    `ff_in_field` : `int`
                    `ff_type` : `str`
                    `ff_id_in_type` : `int`
                    `version` : `str`
        '''
        self.session.execute(models.fiducial_fiber.__table__.insert(), data)
        self.session.commit()

    def insert_fiducial_fiber_geometry(self, data):
        '''
            Description
            -----------
                Insert information into `fiducial_fiber_geometry`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `fiducial_fiber_id` : `int`
                    `ff_center_on_pfi_x_mm` : `float`
                    `ff_center_on_pfi_y_mm` : `float`
        '''
        self.session.execute(models.fiducial_fiber_geometry.__table__.insert(), data)
        self.session.commit()

    def insert_cobra(self, data):
        '''
            Description
            -----------
                Insert information into `cobra`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `cobra_id` : `int`
                    `field_on_pfi` : `int`
                    `cobra_in_field` : `int`
                    `module_in_field` : `int`
                    `cobra_in_module` : `int`
                    `module_name` : `str`
                    `sps_camera_id` : `int`
                    `slit_hole_sps` : `int`
                    `cobra_id_sps` : `int`
                    `cobra_id_lna` : `str`
                    `version` : `str`
        '''
        self.session.execute(models.cobra.__table__.insert(), data)
        self.session.commit()

    def insert_cobra_from_buffer(self, data):
        '''
            Description
            -----------
                Insert information into `cobra`

            Parameters
            ----------
                data : io.StringIO (comma-separated)

            Returns
            -------
                None

            Note
            ----
                `data` list should include the following columns:
                    `cobra_id` : `int`
                    `field_on_pfi` : `int`
                    `cobra_in_field` : `int`
                    `module_in_field` : `int`
                    `cobra_in_module` : `int`
                    `module_name` : `str`
                    `sps_camera_id` : `int`
                    `slit_hole_sps` : `int`
                    `cobra_id_sps` : `int`
                    `cobra_id_lna` : `str`
                    `version` : `str`
        '''
        colnames = ('cobra_id', 'field_on_pfi', 'cobra_in_field', 'module_in_field', 'cobra_in_module', 'module_name', 'sps_camera_id', 'slit_hole_sps', 'cobra_id_sps', 'cobra_id_lna', 'version')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.copy_from(data, 'cobra', ',', columns=colnames)
        conn.commit()
        cur.close()
        conn.close()

    def insert_pfs_visit(self, data):
        '''
            Description
            -----------
                Insert information into `pfs_visit`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `pfs_visit_id` : `int`
                    `pfs_visit_description` : `str`
        '''
        self.session.execute(models.pfs_visit.__table__.insert(), data)
        self.session.commit()

    def insert_mcs_exposure(self, data):
        '''
            Description
            -----------
                Insert information into `mcs_exposure`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `mcs_frame_id` : `int`
                    `pfs_visit_id` : `int'
                    `mcs_exptime` : `float`
                    `altitude` : `float`
                    `azimuth` : `float`
                    `insrot` : `float`
                    `adc_pa` : `float`
                    `dome_temperature` : `float`
                    `dome_pressure` : `float`
                    `dome_humidity` : `float`
                    `outside_temperature` : `float`
                    `outside_pressure` : `float`
                    `outside_humidity` : `float`
                    `mcs_cover_temperature` : `float`
                    `mcs_m1_temperature` : `float`
                    `taken_at` : `datetime`
                    `taken_in_hst_at : `datetime`
        '''
        self.session.execute(models.mcs_exposure.__table__.insert(), data)
        self.session.commit()

    def insert_mcs_data(self, data):
        '''
            Description
            -----------
                Insert information into `mcs_data`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `mcs_frame_id` : `int`
                    `spot_id` : `int'
                    `mcs_center_x_pix` : `float`
                    `mcs_center_y_pix` : `float`
                    `mcs_second_moment_x_pix` : `float`
                    `mcs_second_moment_y_pix` : `float`
                    `mcs_second_moment_xy_pix` : `float`
                    `bgvalue` : `float`
                    `peakvalue` : `float`
        '''
        self.session.execute(models.mcs_data.__table__.insert(), data)
        self.session.commit()

    def insert_mcs_data_from_buffer(self, data):
        '''
            Description
            -----------
                Insert information into `mcs_data`

            Parameters
            ----------
                data : io.StringIO (comma-separated)

            Returns
            -------
                None

            Note
            ----
                `data` list should include the following columns:
                    `mcs_frame_id` : `int`
                    `spot_id` : `int'
                    `mcs_center_x_pix` : `float`
                    `mcs_center_y_pix` : `float`
                    `mcs_second_moment_x_pix` : `float`
                    `mcs_second_moment_y_pix` : `float`
                    `mcs_second_moment_xy_pix` : `float`
                    `bgvalue` : `float`
                    `peakvalue` : `float`
        '''
        colnames = ('mcs_frame_id', 'spot_id', 'mcs_center_x_pix', 'mcs_center_y_pix', 'mcs_second_moment_x_pix', 'mcs_second_moment_y_pix', 'mcs_second_moment_xy_pix', 'bgvalue', 'peakvalue')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.copy_from(data, 'mcs_data', ',', columns=colnames)
        conn.commit()
        cur.close()
        conn.close()

    def insert_cobra_motor_axis(self, data):
        '''
            Description
            -----------
                Insert information into `cobra_motor_axis`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `cobra_motor_axis_id` : `int'    (1, 2)
                    `cobra_motor_axis_name` : `str`  (theta, phi)
        '''
        self.session.execute(models.cobra_motor_axis.__table__.insert(), data)
        self.session.commit()

    def insert_cobra_motor_direction(self, data):
        '''
            Description
            -----------
                Insert information into `cobra_motor_direction`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `cobra_motor_direction_id` : `int'    (0, 1)
                    `cobra_motor_direction_name` : `str`  (forward, reverse)
        '''
        self.session.execute(models.cobra_motor_direction.__table__.insert(), data)
        self.session.commit()

    def insert_cobra_motor_calib(self, data):
        '''
            Description
            -----------
                Insert information into `cobra_motor_calib`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `calibrated_at` : `datetime'
                    `comments` : `str`
        '''
        res = self.session.execute(models.cobra_motor_calib.__table__.insert(), data)
        self.session.commit()
        # get primary_keys
        primary_keys = res.inserted_primary_key
        return primary_keys

    def insert_cobra_motor_model(self, data):
        '''
            Description
            -----------
                Insert information into `cobra_motor_model`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `cobra_motor_calib_id` : `int`
                    `cobra_id` : `int`
                    `cobra_motor_axis_id` : `int`
                    `cobra_motor_direction_id` : `int`
                    `cobra_motor_on_time` : `float`
                    `cobra_motor_step_size` : `float`
                    `cobra_motor_frequency` : `float`
        '''
        res = self.session.execute(models.cobra_motor_model.__table__.insert(), data)
        self.session.commit()
        # get primary_keys
        query = self.session.query(models.cobra_motor_model.cobra_motor_model_id,
                                   models.cobra_motor_model.cobra_motor_calib_id,
                                   models.cobra_motor_model.cobra_id,
                                   models.cobra_motor_model.cobra_motor_axis_id,
                                   models.cobra_motor_model.cobra_motor_direction_id).filter(
            models.cobra_motor_model.cobra_motor_calib_id == data[0]['cobra_motor_calib_id']
        ).all()
        return query

    def insert_cobra_motor_model_from_buffer(self, data):
        '''
            Description
            -----------
                Insert information into `cobra_motor_model`

            Parameters
            ----------
                data : io.StringIO (comma-separated)

            Returns
            -------
                None

            Note
            ----
                `data` list should include the following columns:
                    `cobra_motor_calib_id` : `int`
                    `cobra_id` : `int`
                    `cobra_motor_axis_id` : `int`
                    `cobra_motor_direction_id` : `int`
                    `cobra_motor_on_time` : `float`
                    `cobra_motor_step_size` : `float`
                    `cobra_motor_frequency` : `float`
        '''
        colnames = ('cobra_motor_calib_id', 'cobra_id', 'cobra_motor_axis_id', 'cobra_motor_direction_id', 'cobra_motor_on_time', 'cobra_motor_step_size', 'cobra_motor_frequency')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.copy_from(data, 'cobra_motor_model', ',', columns=colnames)
        conn.commit()
        cur.close()
        conn.close()
        # get primary_keys
        cobra_motor_calib_id = data.getvalue().split(',')[1]
        query = self.session.query(models.cobra_motor_model.cobra_motor_model_id,
                                   models.cobra_motor_model.cobra_motor_calib_id,
                                   models.cobra_motor_model.cobra_id,
                                   models.cobra_motor_model.cobra_motor_axis_id,
                                   models.cobra_motor_model.cobra_motor_direction_id).filter(
            models.cobra_motor_model.cobra_motor_calib_id == cobra_motor_calib_id
        ).all()
        return query

    def insert_cobra_convergence_test(self, data):
        '''
            Description
            -----------
                Insert information into `cobra_convergence_test`

            Parameters
            ----------
                data : `list` of `dict`

            Returns
            -------
                None

            Note
            ----
                `data` list should include `dict` with the following keys:
                    `cobra_motor_model_id` : `int`
                    `iteration` : `int`
                    `cobra_motor_angle_target_id` : `int`
                    `cobra_motor_angle_target` : `float`
                    `cobra_motor_angle_difference` : `float`
                    `signal_to_noise_ratio` : `float`
        '''
        res = self.session.execute(models.cobra_convergence_test.__table__.insert(), data)
        self.session.commit()

    def insert_cobra_convergence_test_from_buffer(self, data):
        '''
            Description
            -----------
                Insert information into `cobra_convergence_test`

            Parameters
            ----------
                data : io.StringIO (comma-separated)

            Returns
            -------
                None

            Note
            ----
                `data` list should include the following columns:
                    `cobra_motor_model_id` : `int`
                    `iteration` : `int`
                    `cobra_motor_angle_target_id` : `int`
                    `cobra_motor_angle_target` : `float`
                    `cobra_motor_angle_difference` : `float`
                    `signal_to_noise_ratio` : `float`
        '''
        colnames = ('cobra_motor_model_id', 'iteration', 'cobra_motor_angle_target_id', 'cobra_motor_angle_target', 'cobra_motor_angle_difference', 'signal_to_noise_ratio')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.copy_from(data, 'cobra_convergence_test', ',', columns=colnames)
        conn.commit()
        cur.close()
        conn.close()

    def insert_cobra_motor_map_from_buffer(self, data):
        '''
            Description
            -----------
                Insert information into `cobra_motor_map`

            Parameters
            ----------
                data : io.StringIO (comma-separated)

            Returns
            -------
                None

            Note
            ----
                `data` list should include the following columns:
                    `cobra_motor_model_id` : `int`
                    `cobra_motor_move_sequence` : `int`
                    `cobra_motor_angle` : `float`
                    `cobra_motor_speed` : `float`
        '''
        colnames = ('cobra_motor_model_id', 'cobra_motor_move_sequence', 'cobra_motor_angle', 'cobra_motor_speed')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.copy_from(data, 'cobra_motor_map', ',', columns=colnames)
        conn.commit()
        cur.close()
        conn.close()

    def insert_cobra_geometry_from_buffer(self, data):
        '''
            Description
            -----------
                Insert information into `cobra_geometry`

            Parameters
            ----------
                data : io.StringIO (comma-separated)

            Returns
            -------
                None

            Note
            ----
                `data` list should include the following columns:
                    `cobra_motor_calib_id` : `int`
                    `cobra_id` : `int`
                    `cobra_center_on_pfi_x_mm` : `float`
                    `cobra_center_on_pfi_y_mm` : `float`
                    `cobra_distance_from_center_mm` : `float`
                    `cobra_motor_theta_limit0` : `float`
                    `cobra_motor_theta_limit1` : `float`
                    `cobra_motor_theta_length` : `float`
                    `cobra_motor_phi_limit_in` : `float`
                    `cobra_motor_phi_limit_out` : `float`
                    `cobra_motor_phi_length` : `float`
                    `cobra_status` : `str`
        '''
        colnames = ('cobra_motor_calib_id', 'cobra_id', 'cobra_center_on_pfi_x_mm', 'cobra_center_on_pfi_y_mm', 'cobra_distance_from_center_mm', 'cobra_motor_theta_limit0', 'cobra_motor_theta_limit1', 'cobra_motor_theta_length', 'cobra_motor_phi_limit_in', 'cobra_motor_phi_limit_out', 'cobra_motor_phi_length', 'cobra_status')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.copy_from(data, 'cobra_geometry', ',', columns=colnames)
        conn.commit()
        cur.close()
        conn.close()

    def insert_cobra_status_from_buffer(self, data):
        '''
            Description
            -----------
                Insert information into `cobra_status`

            Parameters
            ----------
                data : io.StringIO (comma-separated)

            Returns
            -------
                None

            Note
            ----
                `data` list should include the following columns:
                    `mcs_frame_id` : `int`
                    `cobra_id` : `int`
                    `spot_id` : `int`
                    `pfs_config_id` : `int`
                    `iteration` : `int`
                    `pfi_target_x_mm` : `float`
                    `pfi_target_y_mm` : `float`
                    `pfi_center_x_mm` : `float`
                    `pfi_center_y_mm` : `float`
        '''
        colnames = ('mcs_frame_id', 'cobra_id', 'spot_id', 'pfs_config_id', 'iteration', 'pfi_target_x_mm', 'pfi_target_y_mm', 'pfi_center_x_mm', 'pfi_center_y_mm')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.copy_from(data, 'cobra_status', ',', columns=colnames)
        conn.commit()
        cur.close()
        conn.close()

    def insert_cobra_movement_from_buffer(self, data):
        '''
            Description
            -----------
                Insert information into `cobra_movement`

            Parameters
            ----------
                data : io.StringIO (comma-separated)

            Returns
            -------
                None

            Note
            ----
                `data` list should include the following columns:
                    `mcs_frame_id` : `int`
                    `cobra_id` : `int`
                    `cobra_motor_calib_id` : `int`
                    `motor_num_step_theta` : `int`
                    `motor_on_time_theta` : `float`
                    `motor_num_step_phi` : `int`
                    `motor_on_time_phi` : `float`
        '''
        colnames = ('mcs_frame_id', 'cobra_id', 'cobra_motor_calib_id', 'motor_num_step_theta', 'motor_on_time_theta', 'motor_num_step_phi', 'motor_on_time_phi')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.copy_from(data, 'cobra_movement', ',', columns=colnames)
        conn.commit()
        cur.close()
        conn.close()
