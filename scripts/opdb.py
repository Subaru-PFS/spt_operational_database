from builtins import object
import numpy as np
import time

import psycopg2
from psycopg2 import extras


class OpDB(object):

    def __init__(self, hostname='localhost', port='5432', dbname='test', username='test', passwd='ask someone'):
        self.hostname = hostname
        self.port = port
        self.dbname = dbname
        self.username = username
        self.passwd = passwd
        return None

    def connect(self):
        '''
            Description
            -----------
                Start a connection to the database

            Parameters
            ----------
                None

            Returns
            -------
                None
        '''
        self.conn = psycopg2.connect(host=self.hostname,
                                     port=self.port,
                                     database=self.dbname,
                                     user=self.username,
                                     password=self.passwd)
        # self.cur = self.conn.cursor(cursor_factory=extras.DictCursor)
        self.cur = self.conn.cursor()
        print('connected %s' % (self.dbname))
        return None

    def close(self):
        '''
            Description
            -----------
                Close the connection

            Parameters
            ----------
                None

            Returns
            -------
                None
        '''
        self.cur.close()
        self.conn.close()
        print('closed %s' % (self.dbname))

    def reset(self):
        '''
            Description
            -----------
                Reset contents in the database

            Parameters
            ----------
                None

            Returns
            -------
                None
        '''
        print("resetting ...")
        # print("resetting mcsData ...")
        self.cur.execute("TRUNCATE \"mcsData\" CASCADE;")
        # self.conn.commit()
        # print("resetting CobraConfig ...")
        self.cur.execute("TRUNCATE \"CobraConfig\" CASCADE;")
        # self.conn.commit()
        # print("resetting ObsFiber ...")
        self.cur.execute("TRUNCATE \"ObsFiber\" CASCADE;")
        # self.conn.commit()
        # print("resetting pfsArmObj ...")
        self.cur.execute("TRUNCATE \"pfsArmObj\" CASCADE;")
        # self.conn.commit()
        # print("resetting pfsArm ...")
        self.cur.execute("TRUNCATE \"pfsArm\" CASCADE;")
        # self.conn.commit()
        # print("resetting Calib ...")
        self.cur.execute("TRUNCATE \"Calib\" CASCADE;")
        # self.conn.commit()
        # print("resetting Exposure ...")
        self.cur.execute("TRUNCATE \"Exposure\" CASCADE;")
        # self.conn.commit()
        # print("resetting Visit ...")
        self.cur.execute("TRUNCATE \"Visit\" CASCADE;")
        # self.conn.commit()
        # print("resetting pfsConfigFiber ...")
        self.cur.execute("TRUNCATE \"pfsConfigFiber\" CASCADE;")
        # self.conn.commit()
        # print("resetting pfsConfig ...")
        self.cur.execute("TRUNCATE \"pfsConfig\" CASCADE;")
        # self.conn.commit()
        # print("resetting pfsDesignFiber ...")
        self.cur.execute("TRUNCATE \"pfsDesignFiber\" CASCADE;")
        # self.conn.commit()
        # print("resetting pfsDesign ...")
        self.cur.execute("TRUNCATE \"pfsDesign\" CASCADE;")
        # self.conn.commit()
        # print("resetting Tile ...")
        self.cur.execute("TRUNCATE \"Tile\" CASCADE;")
        # self.conn.commit()
        # print("resetting FluxCalib ...")
        self.cur.execute("TRUNCATE \"FluxCalib\" CASCADE;")
        # self.conn.commit()
        # print("resetting VisitHash ...")
        self.cur.execute("TRUNCATE \"VisitHash\" CASCADE;")
        # self.conn.commit()
        # print("resetting VisitsToCombine ...")
        self.cur.execute("TRUNCATE \"VisitsToCombine\" CASCADE;")
        # self.conn.commit()
        # print("resetting pfsObject ...")
        self.cur.execute("TRUNCATE \"pfsObject\" CASCADE;")
        # self.conn.commit()
        # print("resetting Tile ...")
        self.cur.execute("TRUNCATE \"Tile\" CASCADE;")
        # self.conn.commit()
        # print("resetting Program ...")
        self.cur.execute("TRUNCATE \"Program\" CASCADE;")
        # self.conn.commit()
        # print("resetting Proposal ...")
        self.cur.execute("TRUNCATE \"Proposal\" CASCADE;")
        # self.conn.commit()
        # print("resetting Target ...")
        self.cur.execute("UPDATE \"Target\" SET (\"finished\") = (%s) WHERE \"finished\" = (%s)", (False, True))
        # self.conn.commit()
        self.conn.commit()
        print("... done")
        return 0

    '''
        ##################################################
        functionality to get information from the database
        ##################################################
    '''

    def get_all_fiber_position(self):
        '''
            Description
            -----------
                Get the information of all fibers from "FiberPosition"

            Parameters
            ----------
                None

            Returns
            -------
                fiberPositions : `dict` of `numpy.ndarray`

                    dictionary keys: fiberId
                                     ftype
                                     x
                                     y
        '''
        self.cur.execute("SELECT * FROM \"FiberPosition\";")
        rows = self.cur.fetchall()
        dat = np.array(rows, dtype=[('fiberId', 'i4'),
                                    ('ftype', 'U5'),
                                    ('x', 'f4'),
                                    ('y', 'f4')]
                       )
        keys = ['fiberId', 'ftype', 'x', 'y']
        self.fiberPositions = {}
        for key in keys:
            self.fiberPositions[key] = dat[key]
        return self.fiberPositions

    def get_all_cobra_position(self):
        '''
            Description
            -----------
                Get the information of all cobras from "CobraPosition"

            Parameters
            ----------
                None

            Returns
            -------
                cobraPositions : `dict` of `numpy.ndarray`

                    dictionary keys: cobraId
                                     fiberId
                                     fld
                                     cf
                                     mf
                                     cm
                                     mod
                                     x
                                     y
                                     r
                                     sp
                                     fh
                                     sfib
                                     fiberIdLNA
                                     version
                    see details in https://github.com/Subaru-PFS/pfs_utils/blob/master/data/fiberids/cobras.pdf
        '''
        self.cur.execute("SELECT * FROM \"CobraPosition\";")
        rows = self.cur.fetchall()
        dat = np.array(rows, dtype=[('cobraId', 'i4'),
                                    ('fiberId', 'i4'),
                                    ('fld', 'i4'),
                                    ('cf', 'i4'),
                                    ('mf', 'i4'),
                                    ('cm', 'i4'),
                                    ('mod', 'U5'),
                                    ('x', 'f4'),
                                    ('y', 'f4'),
                                    ('r', 'f4'),
                                    ('sp', 'i4'),
                                    ('fh', 'i4'),
                                    ('sfib', 'i4'),
                                    ('fiberIdLNA', 'U10'),
                                    ('version', 'U10')
                                    ]
                       )
        keys = ['cobraId', 'fiberId', 'fld', 'cf', 'mf', 'cm', 'mod', 'x', 'y', 'r', 'sp', 'fh', 'sfib', 'fiberIdLNA', 'version']
        self.cobraPositions = {}
        for key in keys:
            self.cobraPositions[key] = dat[key]
        return self.cobraPositions

    def get_all_fiducial_fiber_position(self):
        '''
            Description
            -----------
                Get the information of all fiducial fibers from "FiducialFiberPosition"

            Parameters
            ----------
                None

            Returns
            -------
                fiducialFiberPositions : `dict` of `numpy.ndarray`

                    dictionary keys: ffId
                                     fiberId
                                     ff
                                     fff
                                     fftype
                                     fft
                                     x
                                     y
                                     version
                    see details in https://github.com/Subaru-PFS/pfs_utils/blob/master/data/fiberids/cobras.pdf
        '''
        self.cur.execute("SELECT * FROM \"FiducialFiberPosition\";")
        rows = self.cur.fetchall()
        dat = np.array(rows, dtype=[('ffId', 'i4'),
                                    ('fiberId', 'i4'),
                                    ('ff', 'i4'),
                                    ('fff', 'i4'),
                                    ('fftype', 'U10'),
                                    ('fft', 'i4'),
                                    ('x', 'f4'),
                                    ('y', 'f4'),
                                    ('version', 'U10')
                                    ]
                       )
        keys = ['ffId', 'fiberId', 'ff', 'fff', 'fftype', 'fft', 'x', 'y', 'version']
        self.fiducialFiberPositions = {}
        for key in keys:
            self.fiducialFiberPositions[key] = dat[key]
        return self.fiducialFiberPositions

    def get_fiber_position(self, fiberIds):
        '''
            Description
            -----------
                Get the information of selected fibers from "FiberPosition" using `fiberId`

            Parameters
            ----------
                fiberId : `list`

            Returns
            -------
                x : `list`
                    X positions on PFI
                y : `list`
                    Y positions on PFI
                ftype: `list`
                    Fiber type: cobra / ff
            Note
            ----
                If fiberId is not in the table, x = numpy.nan, y = numpy.nan, ftype = 'none' are returned for the fiberId
        '''
        self.cur.execute("SELECT * FROM \"FiberPosition\";")
        rows = self.cur.fetchall()
        dat = np.array(rows, dtype=[('fiberId', 'i4'),
                                    ('ftype', 'U5'),
                                    ('x', 'f4'),
                                    ('y', 'f4')]
                       )
        fp_fiberId = dat['fiberId']
        fp_ftype = dat['ftype']
        fp_x = dat['x']
        fp_y = dat['y']
        x = []
        y = []
        ftype = []
        for fiberId in fiberIds:
            ''' check fiberIds '''
            if fiberId not in fp_fiberId:
                print('Warning: fiberId %d is not in FiberPosition' % (fiberId))
                x.append(np.nan)
                y.append(np.nan)
                ftype.append('none')
            else:
                idx = np.where(fp_fiberId == fiberId)[0]
                x.append(fp_x[idx][0])
                y.append(fp_y[idx][0])
                ftype.append(fp_ftype[idx][0])
        return x, y, ftype

    def get_targetId(self, programId, objIds):
        '''
            Description
            -----------
                Get `targetIds` from "Target" using `programId` and `objIds`

            Parameters
            ----------
                programId : `int`
                objIds : `list` of `int`

            Returns
            -------
                targetIds : `list` of `int`

            Note
            ----
        '''
        self.cur.execute("SELECT \"targetId\",\"objId\" FROM \"Target\" WHERE \"programId\" = (%s);", (programId,))
        rows = self.cur.fetchall()
        dat = np.array(rows, dtype=[('targetId', 'i8'), ('objId', 'i8')])
        targetIds_db = dat['targetId']
        objIds_db = dat['objId']
        targetIds = []
        for objId in objIds:
            try:
                msk = objIds_db == objId
                targetIds.append(targetIds_db[msk][0])
            except Exception as e:
                print(e)
                targetIds.append(np.nan)
        return targetIds

    def get_pfsConfigId(self, pfsDesignId, visit0):
        '''
            Description
            -----------
                Get `pfsConfigId` from "pfsConfig" using `pfsDesignId` and `visit0`

            Parameters
            ----------
                pfsDesignId : `int`
                visit0 : `int`

            Returns
            -------
                pfsConfigId : `int`

            Note
            ----
        '''
        self.cur.execute("SELECT \"pfsConfigId\" FROM \"pfsConfig\" WHERE \"pfsDesignId\" = (%s) AND \"visit0\" = (%s);", (pfsDesignId, visit0))
        rows = self.cur.fetchall()
        dat = np.array(rows, dtype=[('pfsConfigId', 'i8')])
        pfsConfigId = int(dat['pfsConfigId'][0])
        return pfsConfigId

    def get_mcsCenter(self, frameId, fiberIds):
        '''
            Description
            -----------
                Get `centroidx` and `centroidy` from "mcsData" using `frameId` and `fiberIds`

            Parameters
            ----------
                frameId : `int`
                fiberIds : `list` of `int`

            Returns
            -------
                mcsIds : `list` of `int`
                centroidx : `list` of of `int`
                centroidy : `list` of of `int`

            Note
            ----
        '''
        self.cur.execute("SELECT \"mcsId\",\"fiberId\",\"centroidx\",\"centroidy\" FROM \"mcsData\" WHERE \"frameId\" = (%s);", (int(frameId),))
        rows = self.cur.fetchall()
        dat = np.array(rows, dtype=[('mcsId', 'i4'), ('fiberId', 'i4'), ('centroidx', 'f4'), ('centroidy', 'f4')])
        mcsIds_db = dat['mcsId']
        fiberIds_db = dat['fiberId']
        centroidx_db = dat['centroidx']
        centroidy_db = dat['centroidy']
        mcsIds = []
        centroidx = []
        centroidy = []
        for fiberId in fiberIds:
            try:
                msk = fiberIds_db == fiberId
                mcsIds.append(mcsIds_db[msk][0])
                centroidx.append(centroidx_db[msk][0])
                centroidy.append(centroidy_db[msk][0])
            except Exception as e:
                print(e)
                mcsIds.append(np.nan)
                centroidx.append(np.nan)
                centroidy.append(np.nan)
        return mcsIds, centroidx, centroidy

    '''
        #####################################################
        functionality to insert information into the database
        #####################################################
    '''

    def insert_proposal(self, proposalId):
        '''
            Description
            -----------
                Insert information into "Proposal"

            Parameters
            ----------
                proposalId : `str`

            Returns
            -------
                None

            Note
            ----
        '''
        __tablename__ = 'Proposal'
        try:
            self.cur.execute("INSERT INTO \"Proposal\" (\"proposalId\") VALUES (%s)", (proposalId,))
            print('insert into %s' % (__tablename__))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            try:
                self.cur.execute("UPDATE \"Proposal\" SET (\"proposalId\") = (%s) WHERE \"proposalId\" = (%s)", (proposalId, proposalId, ))
                self.conn.commit()
                print('update %s' % (__tablename__))
            except Exception as e:
                print(e)
        return None

    def insert_program(self, programId, name, description, proposalId, filler):
        '''
            Description
            -----------
                Insert information into "Program"

            Parameters
            ----------
                programId : `int`
                name : `str`
                description : `str`
                proposalId : `int`
                filler : `bool`

            Returns
            -------
                None

            Note
            ----
        '''
        __tablename__ = 'Program'
        try:
            self.cur.execute("INSERT INTO \"Program\" (\"programId\",\"name\",\"description\", \"proposalId\", \"filler\") VALUES (%s,%s,%s,%s,%s)", (programId, name, description, proposalId, filler, ))
            self.conn.commit()
            print('insert into %s' % (__tablename__))
        except Exception as e:
            self.conn.rollback()
            try:
                self.cur.execute("UPDATE \"Program\" SET (\"programId\",\"name\",\"description\", \"proposalId\", \"filler\") = (%s,%s,%s,%s,%s) WHERE \"programId\" = (%s)", (programId, name, description, proposalId, filler, programId, ))
                self.conn.commit()
                print('update %s' % (__tablename__))
            except Exception as e:
                print(e)
        return None

    def insert_tile(self, tileId, programId, tile, raCenter, decCenter, pa, finished):
        '''
            Description
            -----------
                Insert information into "Tile"

            Parameters
            ----------
                tileId : `int`
                programId : `int`
                tile : `int`
                raCenter : `float`
                decCenter : `float`
                pa : `float`
                finished : `bool`

            Returns
            -------
                None

            Note
            ----
        '''
        __tablename__ = "Tile"
        try:
            self.cur.execute("INSERT INTO \"Tile\" (\"tileId\",\"programId\",\"tile\", \"raCenter\", \"decCenter\", \"pa\", \"finished\") VALUES (%s,%s,%s,%s,%s,%s,%s)", (tileId, programId, tile, raCenter, decCenter, pa, finished,))
            self.conn.commit()
            print('insert into %s' % (__tablename__))
        except Exception as e:
            self.conn.rollback()
            try:
                self.cur.execute("UPDATE \"Tile\" SET (\"tileId\",\"programId\",\"tile\", \"raCenter\", \"decCenter\", \"pa\", \"finished\") = (%s,%s,%s,%s,%s,%s,%s) WHERE \"tileId\" = (%s)", (tileId, programId, tile, raCenter, decCenter, pa, finished, tileId, ))
                self.conn.commit()
                print('update %s' % (__tablename__))
            except Exception as e:
                print(e)
        return None

    def insert_target(self, programId, objId, ra, dec, tract, patch, priority, targetTypeId, catId, catObjId,
                      fiberMag_g, fiberMag_r, fiberMag_i, fiberMag_z, fiberMag_y, fiberMag_j, fiducialExptime,
                      photz, mediumResolution, QATypeId, QALambdaMin, QALambdaMax, QAThreshold, QALineFlux,
                      completeness, finished):
        '''
            Description
            -----------
                Insert information into "Target"

            Parameters
            ----------
                programId : `int`
                objId : `numpy.ndarray` of `int`
                ra : `numpy.ndarray` of `float`
                dec : `numpy.ndarray` of `float`
                tract : `numpy.ndarray` of `int`
                patch : `numpy.ndarray` of `str`
                priority : `numpy.ndarray` of `int`
                targetTypeId : `numpy.ndarray` of `int`
                catId : `numpy.ndarray` of `int`
                catObjId : `numpy.ndarray` of `int`
                fiberMag_g : `numpy.ndarray` of `float`
                fiberMag_r : `numpy.ndarray` of `float`
                fiberMag_i : `numpy.ndarray` of `float`
                fiberMag_z : `numpy.ndarray` of `float`
                fiberMag_y : `numpy.ndarray` of `float`
                fiberMag_j : `numpy.ndarray` of `float`
                fiducialExptime : `numpy.ndarray` of `float`
                photz : `numpy.ndarray` of `float`
                mediumResolution : `numpy.ndarray` of `bool`
                QATypeId : `numpy.ndarray` of `int`
                QALambdaMin : `numpy.ndarray` of `float`
                QALambdaMax : `numpy.ndarray` of `float`
                QAThreshold : `numpy.ndarray` of `float`
                QALineFlux : `numpy.ndarray` of `float`
                completeness : `numpy.ndarray` of `float`
                finished : `numpy.ndarray` of `bool`

            Returns
            -------
                None

            Note
            ----
        '''
        __tablename__ = "Target"

        ''' get objIds from "Target" '''
        self.cur.execute("SELECT \"objId\" FROM \"Target\" WHERE \"programId\" = (%s);", (programId,))
        rows = self.cur.fetchall()
        dat = np.array(rows, dtype=[('objId', 'i8')])
        objIds_db = dat['objId']

        ''' start to insert'''
        insert_list = []
        for i in range(len(objId)):
            if objId not in objIds_db:    # check duplicates
                insert_list.append((int(programId), int(objId[i]), float(ra[i]), float(dec[i]), int(tract[i]), patch[i], float(priority[i]), int(targetTypeId[i]), int(catId[i]), int(catObjId[i]), float(fiberMag_g[i]), float(fiberMag_r[i]), float(fiberMag_i[i]), float(fiberMag_z[i]), float(fiberMag_y[i]), float(fiberMag_j[i]), float(fiducialExptime[i]), float(photz[i]), bool(mediumResolution[i]), int(QATypeId[i]), float(QALambdaMin[i]), float(QALambdaMax[i]), float(QAThreshold[i]), float(QALineFlux[i]), float(completeness[i]), bool(finished[i]), ))
        try:
            extras.execute_values(self.cur, "INSERT INTO \"Target\" (\"programId\", \"objId\", \"ra\", \"dec\", \"tract\", \"patch\", \"priority\", \"targetTypeId\", \"catId\", \"catObjId\", \"fiberMag_g\", \"fiberMag_r\", \"fiberMag_i\", \"fiberMag_z\", \"fiberMag_y\", \"fiberMag_j\", \"fiducialExptime\", \"photz\", \"mediumResolution\", \"QATypeId\", \"QALambdaMin\", \"QALambdaMax\", \"QAThreshold\", \"QALineFlux\", \"completeness\", \"finished\") VALUES %s", insert_list)
            self.conn.commit()
            print('insert into %s' % (__tablename__))
        except Exception as e:
            print(e)
            print('cannot insert into %s' % (__tablename__))
        return None

    def insert_pfsDesign(self, pfsDesignId, tileId, raCenter, decCenter, paConfig, numSciDesigned, numCalDesigned, numSkyDesigned, numGuideStars, exptime, minExptime, etsVersion, etsAssigner, etsExectime, obsolete):
        '''
            Description
            -----------
                Insert information into "pfsDesign"

            Parameters
            ----------
                pfsDesignId : `int`
                tileId : `int`
                raCenter : `float`
                decCenter : `float`
                paConfig : `float`
                numSciDesigned : `int`
                numCalDesigned : `int`
                numSkyDesigned : `int`
                numGuideStars : `int`
                exptime : `float`
                minExptime : `float`
                etsVersion : `str`
                etsAssigned : `str`
                etsExectime : `timestamp`
                obsolete : `bool`

            Returns
            -------
                None

            Note
            ----
        '''
        __tablename__ = "pfsDesign"
        try:
            self.cur.execute("INSERT INTO \"pfsDesign\" (\"pfsDesignId\", \"tileId\",\"raCenter\", \"decCenter\", \"paConfig\", \"numSciDesigned\", \"numCalDesigned\", \"numSkyDesigned\", \"numGuideStars\", \"exptime\", \"minExptime\", \"etsVersion\", \"etsAssigner\", \"etsExectime\", \"obsolete\") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (pfsDesignId, tileId, raCenter, decCenter, paConfig, numSciDesigned, numCalDesigned, numSkyDesigned, numGuideStars, exptime, minExptime, etsVersion, etsAssigner, etsExectime, obsolete,))
            self.conn.commit()
            print('insert into %s' % (__tablename__))
        except Exception as e:
            self.conn.rollback()
            try:
                self.cur.execute("UPDATE \"pfsDesign\" SET (\"pfsDesignId\", \"tileId\",\"raCenter\", \"decCenter\", \"paConfig\", \"numSciDesigned\", \"numCalDesigned\", \"numSkyDesigned\", \"numGuideStars\", \"exptime\", \"minExptime\", \"etsVersion\", \"etsAssigner\", \"etsExectime\", \"obsolete\") = (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) WHERE \"pfsDesignId\" = (%s)", (pfsDesignId, tileId, raCenter, decCenter, paConfig, numSciDesigned, numCalDesigned, numSkyDesigned, numGuideStars, exptime, minExptime, etsVersion, etsAssigner, etsExectime, obsolete, pfsDesignId, ))
                self.conn.commit()
                print('update %s' % (__tablename__))
            except Exception as e:
                print(e)
        return None

    def insert_pfsDesignFiber(self, pfsDesignId, fiberId, targetId, tract, patch, ra, dec, catId, objId, targetTypeId,
                              fiberMag_g, fiberMag_r, fiberMag_i, fiberMag_z, fiberMag_y, fiberMag_j,
                              etsPriority, etsCostFunction, etsCobraMovement, pfiNominal_x, pfiNominal_y,
                              onSource):
        '''
            Description
            -----------
                Insert information into "pfsDesignFiber"

            Parameters
            ----------
                pfsDesignId : `int`
                fiberId : `numpy.ndarray` of `int`
                targetId : `numpy.ndarray` of `int`
                tract : `numpy.ndarray` of `int`
                patch : `numpy.ndarray` of `str`
                ra : `numpy.ndarray` of `float`
                dec : `numpy.ndarray` of `float`
                catId : `numpy.ndarray` of `int`
                objId : `numpy.ndarray` of `int`
                targetTypeId : `numpy.ndarray` of `int`
                fiberMag_g : `numpy.ndarray` of `float`
                fiberMag_r : `numpy.ndarray` of `float`
                fiberMag_i : `numpy.ndarray` of `float`
                fiberMag_z : `numpy.ndarray` of `float`
                fiberMag_y : `numpy.ndarray` of `float`
                fiberMag_j : `numpy.ndarray` of `float`
                etsPriority : `numpy.ndarray` of `int`
                etsCostFunction : `numpy.ndarray` of `str`
                etsCobraMovement : `numpy.ndarray` of `str`
                pfiNominal_x : `numpy.ndarray` of `float`
                pfiNominal_y : `numpy.ndarray` of `float`
                onSource : `numpy.ndarray` of `bool`

            Returns
            -------
                None

            Note
            ----
        '''
        __tablename__ = 'pfsDesignFiber'
        insert_list = []
        for i in range(len(fiberId)):
            insert_list.append((int(pfsDesignId), int(fiberId[i]), int(targetId[i]), int(tract[i]), patch[i], float(ra[i]), float(dec[i]), int(catId[i]), int(objId[i]), int(targetTypeId[i]), float(fiberMag_g[i]), float(fiberMag_r[i]), float(fiberMag_i[i]), float(fiberMag_z[i]), float(fiberMag_y[i]), float(fiberMag_j[i]), int(etsPriority[i]), etsCostFunction[i], etsCobraMovement[i], float(pfiNominal_x[i]), float(pfiNominal_y[i]), bool(onSource[i])))
        try:
            extras.execute_values(self.cur, "INSERT INTO \"pfsDesignFiber\" (\"pfsDesignId\", \"fiberId\", \"targetId\", \"tract\", \"patch\", \"ra\", \"dec\", \"catId\", \"objId\", \"targetTypeId\", \"fiberMag_g\", \"fiberMag_r\", \"fiberMag_i\", \"fiberMag_z\", \"fiberMag_y\", \"fiberMag_j\", \"etsPriority\", \"etsCostFunction\", \"etsCobraMovement\", \"pfiNominal_x\", \"pfiNominal_y\", \"onSource\") VALUES %s", insert_list)
            self.conn.commit()
            print('insert into %s' % (__tablename__))
        except Exception as e:
            print(e)
            print('cannot insert into %s' % (__tablename__))
            self.conn.rollback()
        return None

    def insert_visit(self, visit, visitTypeId, description):
        '''
            Description
            -----------
                Insert information into "Visit"

            Parameters
            ----------
                visit : `int`
                visitTypeId : `int`
                description : `str`

            Returns
            -------
                None

            Note
            ----
        '''
        __tablename__ = 'Visit'
        try:
            self.cur.execute("INSERT INTO \"Visit\" (\"visit\",\"visitTypeId\",\"description\") VALUES (%s,%s,%s)", (visit, visitTypeId, description, ))
            self.conn.commit()
            print('insert into %s' % (__tablename__))
        except Exception as e:
            self.conn.rollback()
            try:
                self.cur.execute("UPDATE \"Visit\" SET (\"visit\",\"visitTypeId\",\"description\") = (%s,%s,%s) WHERE \"visit\" = (%s)", (visit, visitTypeId, description, visit, ))
                self.conn.commit()
                print('update %s' % (__tablename__))
            except Exception as e:
                print(e)
        return None

    def insert_pfsConfig(self, pfsConfigId, pfsDesignId, visit0, raCenter, decCenter, paConfig,
                         telEl, insRot, numSciAllocated, numCalAllocated, numSkyAllocated, numGuideStars,
                         exptime, minExptime, allocNumIter, allocElapsetime, allocRmsScatter, allocExectime,
                         observed):
        '''
            Description
            -----------
                Insert information into "pfsConfig"

            Parameters
            ----------
                pfsConfigId : `int`
                pfsDesignId : `int`
                visit0 : `int`
                raCenter : `float`
                decCenter : `float`
                paConfig : `float`
                telEl : `float`
                insRot : `float`
                numSciAllocated : `int`
                numCalAllocated : `int`
                numSkyAllocated : `int`
                numGuideStars : `int`
                exptime : `float`
                minExptime : `float`
                allocNumIter : `int`
                allocElapsetime : `float`
                allocRmsScatter : 'float'
                allocExectime : `timestamp`
                observed : `bool`

            Returns
            -------
                None

            Note
            ----
        '''
        __tablename__ = "pfsConfig"
        if pfsConfigId == None:
            self.cur.execute("SELECT \"pfsConfigId\" FROM \"pfsConfig\" WHERE \"pfsDesignId\" = (%s) AND \"visit0\" = (%s);", (pfsDesignId, visit0))
            rows = self.cur.fetchall()
            if len(rows) == 0:
                self.cur.execute("INSERT INTO \"pfsConfig\" (\"pfsDesignId\", \"visit0\",\"raCenter\", \"decCenter\", \"paConfig\", \"telEl\", \"insRot\", \"numSciAllocated\", \"numCalAllocated\", \"numSkyAllocated\", \"numGuideStars\", \"exptime\", \"minExptime\", \"allocNumIter\", \"allocElapsetime\", \"allocRmsScatter\", \"allocExectime\", \"observed\") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (pfsDesignId, visit0, raCenter, decCenter, paConfig, telEl, insRot, numSciAllocated, numCalAllocated, numSkyAllocated, numGuideStars, exptime, minExptime, allocNumIter, allocElapsetime, allocRmsScatter, allocExectime, observed, ))
                self.conn.commit()
                print('insert into %s' % (__tablename__))
            else:
                print('pfsConfigId exists for pfsDesignId=%d and visit0=%d !' % (pfsDesignId, visit0))
        else:
            self.cur.execute("UPDATE \"pfsConfig\" SET (\"pfsDesignId\", \"visit0\",\"raCenter\", \"decCenter\", \"paConfig\", \"telEl\", \"insRot\", \"numSciAllocated\", \"numCalAllocated\", \"numSkyAllocated\", \"numGuideStars\", \"exptime\", \"minExptime\", \"allocNumIter\", \"allocElapsetime\", \"allocRmsScatter\", \"allocExectime\", \"observed\") = (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) WHERE \"pfsConfigId\" = (%s)", (pfsDesignId, visit0, raCenter, decCenter, paConfig, telEl, insRot, numSciAllocated, numCalAllocated, numSkyAllocated, numGuideStars, exptime, minExptime, allocNumIter, allocElapsetime, allocRmsScatter, allocExectime, observed, pfsConfigId, ))
            self.conn.commit()
            print('update %s' % (__tablename__))
        return None

    def insert_pfsConfigFiber(self, pfsConfigFiberId, pfsConfigId, fiberId, targetId,
                              tract, patch, ra, dec, catId, objId, targetTypeId,
                              fiberMag_g, fiberMag_r, fiberMag_i, fiberMag_z, fiberMag_y, fiberMag_j,
                              pfiNominal_x, pfiNominal_y, pfiCenter_x, pfiCenter_y, pfiDiff_x, pfiDiff_y,
                              mcsCenter_x, mcsCenter_y, motorMapSummary, configTime,
                              onSource):
        '''
            Description
            -----------
                Insert information into "pfsConfigFiber"

            Parameters
            ----------
                pfsConfigFiberId : `numpy.ndarray` of `int`
                pfsConfigId : `int`
                fiberId : `numpy.ndarray` of `int`
                targetId : `numpy.ndarray` of `int`
                tract : `numpy.ndarray` of `int`
                patch : `numpy.ndarray` of `str`
                ra : `numpy.ndarray` of `float`
                dec : `numpy.ndarray` of `float`
                catId : `numpy.ndarray` of `int`
                objId : `numpy.ndarray` of `int`
                targetTypeId : `numpy.ndarray` of `int`
                fiberMag_g : `numpy.ndarray` of `float`
                fiberMag_r : `numpy.ndarray` of `float`
                fiberMag_i : `numpy.ndarray` of `float`
                fiberMag_z : `numpy.ndarray` of `float`
                fiberMag_y : `numpy.ndarray` of `float`
                fiberMag_j : `numpy.ndarray` of `float`
                pfiNominal_x : `numpy.ndarray` of `float`
                pfiNominal_y : `numpy.ndarray` of `float`
                pfiCenter_x : `numpy.ndarray` of `float`
                pfiCenter_y : `numpy.ndarray` of `float`
                pfiDiff_x : `numpy.ndarray` of `float`
                pfiDiff_y : `numpy.ndarray` of `float`
                mcsCenter_x : `numpy.ndarray` of `float`
                mcsCenter_y : `numpy.ndarray` of `float`
                motorMapSummary : `numpy.ndarray` of `str`
                configTime : `numpy.ndarray` of `float`
                onSource : `numpy.ndarray` of `bool`

            Returns
            -------
                None

            Note
            ----
        '''
        __tablename__ = 'pfsConfigFiber'

        ''' get pfsConfigFiberId from "pfsConfigFiber" '''
        self.cur.execute("SELECT \"pfsConfigFiberId\" FROM \"pfsConfigFiber\" WHERE \"pfsConfigId\" = (%s);", (pfsConfigId,))
        rows = self.cur.fetchall()
        dat = np.array(rows, dtype=[('pfsConfigFiberId', 'i8')])
        pfsConfigFiberIds_db = dat['pfsConfigFiberId']

        ''' start to insert '''
        keys_list = []
        insert_list = []
        for i in range(len(fiberId)):
            keys_list.append((int(pfsConfigFiberId[i])))
            insert_list.append((int(pfsConfigFiberId[i]), int(pfsConfigId), int(fiberId[i]), int(targetId[i]), int(tract[i]), patch[i], float(ra[i]), float(dec[i]), int(catId[i]), int(objId[i]), int(targetTypeId[i]), float(fiberMag_g[i]), float(fiberMag_r[i]), float(fiberMag_i[i]), float(fiberMag_z[i]), float(fiberMag_y[i]), float(fiberMag_j[i]), float(pfiNominal_x[i]), float(pfiNominal_y[i]), float(pfiCenter_x[i]), float(pfiCenter_y[i]), float(pfiDiff_x[i]), float(pfiDiff_y[i]), float(mcsCenter_x[i]), float(mcsCenter_y[i]), motorMapSummary[i], float(configTime[i]), bool(onSource[i])))
        if len(pfsConfigFiberIds_db)==0:
            try:
                extras.execute_values(self.cur, "INSERT INTO \"pfsConfigFiber\" (\"pfsConfigFiberId\", \"pfsConfigId\", \"fiberId\", \"targetId\", \"tract\", \"patch\", \"ra\", \"dec\", \"catId\", \"objId\", \"targetTypeId\", \"fiberMag_g\", \"fiberMag_r\", \"fiberMag_i\", \"fiberMag_z\", \"fiberMag_y\", \"fiberMag_j\", \"pfiNominal_x\", \"pfiNominal_y\", \"pfiCenter_x\", \"pfiCenter_y\", \"pfiDiff_x\", \"pfiDiff_y\", \"mcsCenter_x\", \"mcsCenter_y\", \"motorMapSummary\", \"configTime\", \"onSource\") VALUES %s", insert_list)
                self.conn.commit()
                print('insert into %s' % (__tablename__))
            except Exception as e:
                print(e)
                print('cannot insert into %s' % (__tablename__))
                self.conn.rollback()
        else:
            try:
                for i in range(len(fiberId)):
                    self.cur.execute("UPDATE \"pfsConfigFiber\" SET (\"pfsConfigFiberId\", \"pfsConfigId\", \"fiberId\", \"targetId\", \"tract\", \"patch\", \"ra\", \"dec\", \"catId\", \"objId\", \"targetTypeId\", \"fiberMag_g\", \"fiberMag_r\", \"fiberMag_i\", \"fiberMag_z\", \"fiberMag_y\", \"fiberMag_j\", \"pfiNominal_x\", \"pfiNominal_y\", \"pfiCenter_x\", \"pfiCenter_y\", \"pfiDiff_x\", \"pfiDiff_y\", \"mcsCenter_x\", \"mcsCenter_y\", \"motorMapSummary\", \"configTime\", \"onSource\") = %s WHERE \"pfsConfigFiberId\" = (%s);", (insert_list[i], int(pfsConfigFiberId[i])))
                    self.conn.commit()
                print('update %s' % (__tablename__))
            except Exception as e:
                print(e)
                print('cannot update %s' % (__tablename__))
                self.conn.rollback()
        return None

    def insert_mcsData(self, datatime, frameId, moveId, fiberId,
                       centroidx, centroidy, fwhmx, fwhmy, bgvalue, peakvalue):
        '''
            Description
            -----------
                Insert information into "mcsData"

            Parameters
            ----------
                datatime : `datetime`
                frameId : `int`
                moveId : `int`
                fiberId : `numpy.ndarray` of `int`
                centroidx : `numpy.ndarray` of `float`
                centroidy : `numpy.ndarray` of `float`
                fwhmx : `numpy.ndarray` of `float`
                fwhmy : `numpy.ndarray` of `float`
                bgvalue : `numpy.ndarray` of `float`
                peakvalue : `numpy.ndarray` of `float`

            Returns
            -------
                None

            Note
            ----
        '''
        __tablename__ = 'mcsData'

        ''' get `frameId` from "mcsData" '''
        self.cur.execute("SELECT \"frameId\" FROM \"mcsData\";")
        rows = self.cur.fetchall()
        dat = np.array(rows, dtype=[('frameId', 'i4')])
        frameId_db = dat['frameId']
        frameId_db_unique = np.unique(frameId_db)

        ''' start to insert '''
        if frameId not in frameId_db_unique:
            insert_list = []
            for i in range(len(fiberId)):
                insert_list.append((datatime, int(frameId), int(moveId), int(fiberId[i]), float(centroidx[i]), float(centroidy[i]), float(fwhmx[i]), float(fwhmy[i]), float(bgvalue[i]), float(peakvalue[i])))
            try:
                extras.execute_values(self.cur, "INSERT INTO \"mcsData\" (\"datatime\", \"frameId\", \"moveId\", \"fiberId\", \"centroidx\", \"centroidy\", \"fwhmx\", \"fwhmy\", \"bgvalue\", \"peakvalue\") VALUES %s", insert_list)
                self.conn.commit()
                print('insert into %s' % (__tablename__))
            except Exception as e:
                print(e)
                print('cannot insert into %s' % (__tablename__))
                self.conn.rollback()
        else:
            print('records for frameId=%d exist!' % (frameId))

        return None

    def insert_CobraConfig(self, pfsConfigFiberId, pfsConfigId, fiberId, iteration, motorNumStepTheta, motorNumStepPhi,
                           mcsId, pfiNominal_x, pfiNominal_y, pfiCenter_x, pfiCenter_y, pfiDiff_x, pfiDiff_y,
                           mcsCenter_x, mcsCenter_y, exectime):
        '''
            Description
            -----------
                Insert information into "CobraConfig"

            Parameters
            ----------
                pfsConfigFiberId : `numpy.ndarray` of `int`
                pfsConfigId : `int`
                fiberId : `numpy.ndarray` of `int`
                iteration : `int`
                motorNumStepTheta : `numpy.ndarray` of `int`
                motorNumStepPhi : `numpy.ndarray` of `int`
                mcsId : `numpy.ndarray` of `int`
                pfiNominal_x : `numpy.ndarray` of `float`
                pfiNominal_y : `numpy.ndarray` of `float`
                pfiCenter_x : `numpy.ndarray` of `float`
                pfiCenter_y : `numpy.ndarray` of `float`
                pfiDiff_x : `numpy.ndarray` of `float`
                pfiDiff_y : `numpy.ndarray` of `float`
                mcsCenter_x : `numpy.ndarray` of `float`
                mcsCenter_y : `numpy.ndarray` of `float`
                exectime : `datetime`

            Returns
            -------
                None

            Note
            ----
        '''
        __tablename__ = 'CobraConfig'
        
        ''' get `fiberId` and `iteration` from "CobraConfig" '''
        self.cur.execute("SELECT \"fiberId\",\"iteration\" FROM \"CobraConfig\" WHERE \"pfsConfigId\" = (%s);", (pfsConfigId,))
        rows = self.cur.fetchall()
        dat = np.array(rows, dtype=[('fiberId', 'i4'),('iteration','i4')])
        fiberId_db = dat['fiberId']
        iteration_db = dat['iteration']
        iteration_db_unique = np.unique(iteration_db)

        ''' start to insert'''
        if iteration not in iteration_db_unique:
            insert_list = []
            for i in range(len(fiberId)):
                insert_list.append((int(pfsConfigFiberId[i]), int(pfsConfigId), int(fiberId[i]), iteration, int(motorNumStepTheta[i]), int(motorNumStepPhi[i]), int(mcsId[i]), float(pfiNominal_x[i]), float(pfiNominal_y[i]), float(pfiCenter_x[i]), float(pfiCenter_y[i]), float(pfiDiff_x[i]), float(pfiDiff_y[i]), float(mcsCenter_x[i]), float(mcsCenter_y[i]), exectime))
            try:
                extras.execute_values(self.cur, "INSERT INTO \"CobraConfig\" (\"pfsConfigFiberId\", \"pfsConfigId\", \"fiberId\", \"iteration\", \"motorNumStepTheta\", \"motorNumStepPhi\", \"mcsId\", \"pfiNominal_x\", \"pfiNominal_y\", \"pfiCenter_x\", \"pfiCenter_y\", \"pfiDiff_x\", \"pfiDiff_y\", \"mcsCenter_x\", \"mcsCenter_y\", \"exectime\") VALUES %s", insert_list)
                self.conn.commit()
                print('insert into %s' % (__tablename__))
            except Exception as e:
                print(e)
                print('cannot insert into %s' % (__tablename__))
                self.conn.rollback()
        else:
            print('records for pfsConfigId=%d and iteration=%d exist!' % (pfsConfigId, iteration))
        return None
