import numpy as np
import io
from sqlalchemy import create_engine
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
import pandas as pd
from . import models


class OpDB(object):
    url = 'postgresql://pfs@db-ics:5432/opdb'

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
        #print('connection to {0} started'.format(self.dbinfo))

    def close(self):
        self.session.close()
        #print('connection to {0} closed'.format(self.dbinfo))

    def reset(self, full=True):
        self.session.query(models.drp1d_redshift).delete()
        self.session.query(models.drp1d_line).delete()
        self.session.query(models.drp1d).delete()
        self.session.query(models.drp_ga).delete()
        self.session.query(models.guide_stars).delete()
        self.session.query(models.tel_condition).delete()
        self.session.query(models.visits_to_combine).delete()
        self.session.query(models.tel_visit).delete()
        self.session.query(models.pfs_arm_obj).delete()
        self.session.query(models.pfs_arm).delete()
        self.session.query(models.pfs_object).delete()
        self.session.query(models.obs_fiber).delete()
        self.session.query(models.visit_hash).delete()
        self.session.query(models.flux_calib).delete()
        self.session.query(models.calib_set).delete()
        self.session.query(models.calib).delete()
        self.session.query(models.sps_exposure).delete()
        self.session.query(models.sps_condition).delete()
        self.session.query(models.processing_status).delete()
        self.session.query(models.sps_annotation).delete()
        self.session.query(models.sps_visit).delete()
        self.session.query(models.visit_set).delete()
        self.session.query(models.sky_model).delete()
        self.session.query(models.psf_model).delete()
        self.session.query(models.cobra_convergence_test).delete()
        self.session.query(models.cobra_motor_map).delete()
        self.session.query(models.cobra_motor_model).delete()
        self.session.query(models.cobra_movement).delete()
        self.session.query(models.cobra_status).delete()
        self.session.query(models.pfs_config_fiber).delete()
        self.session.query(models.pfs_config).delete()
        self.session.query(models.pfs_design_fiber).delete()
        self.session.query(models.pfs_design).delete()
        self.session.query(models.mcs_boresight).delete()
        self.session.query(models.mcs_data).delete()
        self.session.query(models.mcs_exposure).delete()
        self.session.query(models.pfs_visit).delete()
        self.session.query(models.tile).delete()
        self.session.execute("ALTER SEQUENCE pfs_object_pfs_object_id_seq RESTART WITH 1")
        self.session.execute("ALTER SEQUENCE calib_set_calib_set_id_seq RESTART WITH 1")
        self.session.execute("ALTER SEQUENCE cobra_motor_model_cobra_motor_model_id_seq RESTART WITH 1")
        self.session.execute("ALTER SEQUENCE cobra_motor_calib_cobra_motor_calib_id_seq RESTART WITH 1")
        self.session.execute("ALTER SEQUENCE pfs_config_pfs_config_id_seq RESTART WITH 1")
        self.session.execute("ALTER SEQUENCE tile_tile_id_seq RESTART WITH 1")
        if full:
            self.session.query(models.cobra_geometry).delete()
            self.session.query(models.cobra_motor_calib).delete()
            self.session.query(models.cobra_motor_axis).delete()
            self.session.query(models.cobra_motor_direction).delete()
            self.session.query(models.star_type).delete()
            self.session.query(models.line_list).delete()
            self.session.query(models.obj_type).delete()
            self.session.query(models.cloud_condition).delete()
            self.session.query(models.beam_switch_mode).delete()
            self.session.query(models.cobra).delete()
            self.session.query(models.sps_camera).delete()
            self.session.query(models.sps_module).delete()
            self.session.query(models.fiducial_fiber_geometry).delete()
            self.session.query(models.fiducial_fiber).delete()
            self.session.query(models.target).delete()
            self.session.query(models.target_type).delete()
            self.session.query(models.input_catalog).delete()
            self.session.query(models.qa_type).delete()
            self.session.query(models.program).delete()
            self.session.query(models.proposal).delete()
            self.session.execute("ALTER SEQUENCE target_target_id_seq RESTART WITH 1")
        self.session.commit()

    def reset_qa(self):
        self.session.query(models.target).filter(models.target.is_finished == True).update({models.target.is_finished: False})
        self.session.commit()

    def reset_completeness(self):
        self.session.query(models.target).filter(models.target.completeness > 0.0).update({models.target.completeness: 0.0})
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    '''
        ############################################################
        functionality to insert/update information into the database
        ############################################################
    '''

    def insert_mappings(self, tablename, mappings):
        '''
            Description
            -----------
                Insert information into a table

            Parameters
            ----------
                tablename : `string`
                mappings : `dictionnary list`

            Returns
            -------
                None
        '''
        model = getattr(models, tablename)
        try:
            self.session.bulk_insert_mappings(model, mappings)
            self.session.commit()
        except:
            self.session.rollback()
            raise

    def insert(self, tablename, dataframe):
        '''
            Description
            -----------
                Insert information into a table

            Parameters
            ----------
                tablename : `string`
                dataframe : `pandas.DataFrame`

            Returns
            -------
                None

            Note
            ----
                Column labels of `dataframe` should be exactly the same as those of the table
        '''
        self.insert_mappings(tablename, dataframe.to_dict(orient="records"))


    def update(self, tablename, dataframe):
        '''
            Description
            -----------
                Update information of a table

            Parameters
            ----------
                tablename : `string`
                dataframe : `pandas.DataFrame`

            Returns
            -------
                None

            Note
            ----
                Column labels of `dataframe` should be exactly the same as those of the table
        '''
        model = getattr(models, tablename)
        try:
            self.session.bulk_update_mappings(model, dataframe.to_dict(orient="records"))
            self.session.commit()
        except:
            self.session.rollback()
            raise

    '''
        ##################################################
        functionality to get information from the database
        ##################################################
    '''

    def fetch_all(self, tablename):
        '''
            Description
            -----------
                Get all records from a table

            Parameters
            ----------
                tablename : `string`

            Returns
            -------
                df : `pandas.DataFrame`

            Note
            ----
        '''
        model = getattr(models, tablename)
        try:
            df = pd.read_sql(self.session.query(model).statement, self.session.bind)
        except:
            self.session.rollback()
            raise

        return df

    def fetch_by_id(self, tablename, **kwargs):
        '''
            Description
            -----------
                Get records from a table where the keyword identifier is matched

            Parameters
            ----------
                tablename : `string`
                **kwargs  :          (e.g., pfs_visit_id=12345)

            Returns
            -------
                df : `pandas.DataFrame`

            Note
            ----
        '''
        model = getattr(models, tablename)
        query = self.session.query(model)
        for k, v in kwargs.items():
            query = query.filter(getattr(model, k) == v)
        try:
            df = pd.read_sql(query.statement, self.session.bind)
        except:
            self.session.rollback()
            raise

        return df

    def fetch_query(self, query):
        '''
            Description
            -----------
                Get all records from SQL query

            Parameters
            ----------
                query : `string`

            Returns
            -------
                df : `pandas.DataFrame`

            Note
            ----
        '''
        try:
            df = pd.read_sql(query, self.session.bind)
        except:
            self.session.rollback()
            raise

        return df

    def fetch_sps_exposures(self, pfs_visit_id):
        '''
            Description
            -----------
                Get SpS exposure information for a given `pfs_visit_id`

            Parameters
            ----------
                pfs_visit_id : `int`

            Returns
            -------
                df : `pandas.DataFrame`

            Note
            ----
        '''
        sps_exposure = models.sps_exposure
        sps_visit = models.sps_visit
        sps_camera = models.sps_camera
        query = self.session \
            .query(sps_exposure.pfs_visit_id, sps_visit.exp_type, sps_camera.sps_module_id, sps_camera.arm, sps_exposure.sps_camera_id) \
            .join(sps_visit, sps_exposure.pfs_visit_id == sps_visit.pfs_visit_id) \
            .join(sps_camera, sps_exposure.sps_camera_id == sps_camera.sps_camera_id) \
            .filter(sps_exposure.pfs_visit_id == pfs_visit_id).statement
        df = pd.read_sql(query, self.session.bind)
        return df
