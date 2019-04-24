from sqlalchemy import create_engine
from sqlalchemy import Column, BigInteger, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation, backref

Base = declarative_base()


class Program(Base):
    __tablename__ = 'Program'

    programId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    description = Column(String)
    filler = Column(Boolean)

    def __init__(self, programId, name, description, filler):
        self.programId = programId
        self.name = name
        self.description = description
        self.filler = filler


class TargetType(Base):
    __tablename__ = 'TargetType'

    targetType = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    description = Column(String)

    def __init__(self, targetType, name, description):
        self.targetType = targetType
        self.name = name
        self.description = description


class QAType(Base):
    __tablename__ = 'QAType'

    QATypeId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    description = Column(String)

    def __init__(self, QATypeId, name, description):
        self.QATypeId = QATypeId
        self.name = name
        self.description = description


class InputCatalog(Base):
    __tablename__ = "InputCatalog"

    catId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    description = Column(String)

    def __init__(self, catId, name, description):
        self.catId = catId
        self.name = name
        self.description = description


class CloudCondition(Base):
    __tablename__ = 'CloudCondition'

    cloudConditionId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    description = Column(String)

    def __init__(self, cloudConditionId, name, description):
        self.cloudConditionId = cloudConditionId
        self.name = name
        self.description = description


class FiberPosition(Base):
    __tablename__ = 'FiberPosition'
    cobraId = Column(Integer, primary_key=True, autoincrement=False)
    spectrograph = Column(Integer)
    slitId = Column(Integer)
    CobraCenter_x = Column(Float)
    CobraCenter_y = Column(Float)

    def __init__(self, cobraId, spectrograph, slitId, CobraCenter_x, CobraCenter_y):
        self.cobraId = cobraId
        self.spectrograph = spectrograph
        self.slitId = slitId
        self.CobraCenter_x = CobraCenter_x
        self.CobraCenter_y = CobraCenter_y


class Target(Base):
    __tablename__ = 'Target'

    targetId = Column(BigInteger, primary_key=True, autoincrement=True)
    programId = Column(Integer, ForeignKey('Program.programId'))
    objId = Column(BigInteger)
    ra = Column(Float)
    dec = Column(Float)
    tract = Column(Integer)
    patch = Column(String)
    priority = Column(Float)
    targetTypeId = Column(Integer, ForeignKey('TargetType.targetType'))
    catId = Column(Integer, ForeignKey('InputCatalog.catId'))
    catObjId = Column(BigInteger, autoincrement=True)
    fiberMag_g = Column(Float)
    fiberMag_r = Column(Float)
    fiberMag_i = Column(Float)
    fiberMag_z = Column(Float)
    fiberMag_Y = Column(Float)
    fiberMag_J = Column(Float)
    fiducialExptime = Column(Float)
    photz = Column(Float)
    QATypeId = Column(Integer, ForeignKey('QAType.QATypeId'))
    QALambdaMin = Column(Float)
    QALambdaMax = Column(Float)
    QAThreshold = Column(Float)
    QALineFlux = Column(Float)
    finished = Column(Boolean)

    programs = relation(Program, backref=backref('Target'))
    targetTypes = relation(TargetType, backref=backref('Target'))
    inputCatalogs = relation(InputCatalog, backref=backref('Target'))
    qaTypes = relation(QAType, backref=backref('Target'))

    def calculateId1(self, programId, objId):
        return (programId << 60) + objId

    def calculateId2(self, catId, objId):
        return (catId << 26) + objId

    def __init__(self, programId, objId, ra, dec, tract, patch, priority, targetType, catId,
                 fiberMag_g, fiberMag_r, fiberMag_i, fiberMag_z, fiberMag_Y,
                 fiberMag_J, fiducialExptime, photz, QATypeId,
                 QALambdaMin, QALambdaMax, QAThreshold, QALineFlux, finished=False):
        self.programId = programId
        self.objId = objId
        self.ra = ra
        self.dec = dec
        self.tract = tract
        self.patch = patch
        self.priority = priority
        self.targetTypeId = targetType
        self.catId = catId
        self.fiberMag_g = fiberMag_g
        self.fiberMag_r = fiberMag_r
        self.fiberMag_i = fiberMag_i
        self.fiberMag_z = fiberMag_z
        self.fiberMag_Y = fiberMag_Y
        self.fiberMag_J = fiberMag_Y
        self.fiducialExptime = fiducialExptime
        self.photz = photz
        self.QATypeId = QATypeId
        self.QALambdaMin = QALambdaMin
        self.QALambdaMax = QALambdaMax
        self.QAThreshold = QAThreshold
        self.QALineFlux = QALineFlux
        self.finished = finished


class Tile(Base):
    __tablename__ = 'Tile'

    tileId = Column(Integer, primary_key=True, autoincrement=True)
    programId = Column(Integer, ForeignKey('Program.programId'))
    tile = Column(Integer)
    ra_center = Column(Float)
    dec_center = Column(Float)
    pa = Column(Float)
    finished = Column(Boolean)

    programs = relation(Program, backref=backref('Tile'))

    def __init__(self, programId, tile, ra_center, dec_center, pa, finished):
        self.programId = programId
        self.tile = tile
        self.ra_center = ra_center
        self.dec_center = dec_center
        self.pa = pa
        self.finished = finished


class pfsDesign(Base):
    __tablename__ = 'pfsDesign'

    pfsDesignId = Column(BigInteger, primary_key=True, autoincrement=False)
    tileId = Column(Integer, ForeignKey('Tile.tileId'))
    num_sci_target = Column(Integer)
    num_sci_allocated = Column(Integer)
    num_cal_target = Column(Integer)
    num_cal_allocated = Column(Integer)
    num_sky_allocated = Column(Integer)
    num_guide_stars = Column(Integer)
    exptime = Column(Float)
    etsVersion = Column(String)
    etsAssigner = Column(String)
    etsExectime = Column(DateTime)
    obsolete = Column(Boolean)

    tiles = relation(Tile, backref=backref('pfsDesign'))

    def __init__(self, pfsDesignId, tileId, num_sci_target, num_sci_allocated,
                 num_cal_target, num_cal_allocated, num_sky_allocated, num_guide_stars,
                 exptime, etsVersion, etsAssgner, etsExectime, obsolete=False):
        self.pfsDesignId = pfsDesignId
        self.tileId = tileId
        self.num_sci_target = num_sci_target
        self.num_sci_allocated = num_sci_allocated
        self.num_cal_target = num_cal_target
        self.num_cal_allocated = num_cal_allocated
        self.num_sky_allocated = num_sky_allocated
        self.num_guide_stars = num_guide_stars
        self.exptime = exptime
        self.etsVersion = etsVersion
        self.etsAssigner = etsAssigner
        self.etsExectime = etsExectime
        self.obsolete = obsolete


class pfsDesignFiber(Base):
    __tablename__ = 'pfsDesignFiber'

    pfsDesignFiberId = Column(BigInteger, primary_key=True, autoincrement=True)
    pfsDesignId = Column(BigInteger, ForeignKey('pfsDesign.pfsDesignId'))
    cobraId = Column(Integer, ForeignKey('FiberPosition.cobraId'))
    targetId = Column(BigInteger, ForeignKey('Target.targetId'))
    etsCostFunction = Column(String)
    etsCobraMovement = Column(String)
    pfiNominal_x = Column(Float)
    pfiNominal_y = Column(Float)
    mcsNominal_x = Column(Float)
    mcsNominal_y = Column(Float)
    onSource = Column(Boolean)

    pfsDesigns = relation(pfsDesign, backref=backref('pfsDesignFiber'))
    targets = relation(Target, backref=backref('pfsDesignFiber'))
    FiberPositions = relation(FiberPosition, backref=backref('pfsDesignFiber'))

    def __init__(self, pfsDesignFiberId, pfsDesignId, cobraId, targetId,
                 etsCostFunction, etsCobraMovement,
                 pfiNominal_x, pfiNominal_y, mcsNominal_x, mcsNominal_y,
                 onSource=True):
        #self.pfsDesignFiberId = pfsDesignFiberId
        self.pfsDesignFiberId = (pfsDesignId << 12) + cobraId
        self.pfsDesignId = pfsDesignId
        self.cobraId = cobraId
        self.targetId = targetId
        self.etsCostFunction = etsCostFunction
        self.etsCobraMovement = etsCobraMovement
        self.pfiNominal_x = pfiNominal_x
        self.pfiNominal_y = pfiNominal_y
        self.mcsNominal_x = mcsNominal_x
        self.mcsNominal_y = mcsNominal_y
        self.onSource = onSource


class Calib(Base):
    __tablename__ = 'Calib'

    calibId = Column(Integer, primary_key=True, autoincrement=False)
    calibType = Column(String)
    calibDate = Column(DateTime)
    pfsDesignId = Column(BigInteger, ForeignKey('pfsDesign.pfsDesignId'))
    spectrograph = Column(Integer)
    arm = Column(String)
    exptime = Column(Float)
    visitStart = Column(Integer)
    visitEnd = Column(Integer)

    pfsDesigns = relation(pfsDesign, backref=backref('Calib'))

    def __init__(self, calibId, calibType, calibDate, pfsDesignId, spectrogarph, arm,
                 exptime, visitStart, visitEnd):
        self.calibId = calibId
        self.calibType = calibType
        self.calibDate = calibDate
        self.pfsDesignId = pfsDesignId
        self.spectrograph = spectrograph
        self.arm = arm
        self.exptime = exptime
        self.visitStart = visitStart
        self.visitEnd = visitEnd


class FluxCalib(Base):
    __tablename__ = 'FluxCalib'

    fluxCalibId = Column(Integer, primary_key=True, autoincrement=False)
    fluxCalibType = Column(String)
    fluxCalibDate = Column(DateTime)
    fluxCalibStarTeff = Column(Float)
    fluxCalibStarLogg = Column(Float)
    fluxCalibStarZ = Column(Float)

    def __init__(self, fluxCalibId, fluxCalibType, fluxCalibDate,
                 fluxCalibStarTeff, fluxCalibStarLogg, fluxCalibStarZ):
        self.fluxCalibId = fluxCalibId
        self.fluxCalibType = fluxCalibType
        self.fluxCalibDate = fluxCalibDate
        self.fluxCalibStarTeff = fluxCalibStarTeff
        self.fluxCalibStarLogg = fluxCalibStarLogg
        self.fluxCalibStarZ = fluxCalibStarZ


class pfsConfig(Base):
    __tablename__ = 'pfsConfig'

    pfsConfigId = Column(BigInteger, primary_key=True, autoincrement=False)
    pfsDesignId = Column(BigInteger, ForeignKey('pfsDesign.pfsDesignId'))
    ra_config = Column(Float)
    dec_config = Column(Float)
    pa_config = Column(Float)
    num_sci_allocated = Column(Integer)
    num_cal_allocated = Column(Integer)
    num_sky_allocated = Column(Integer)
    num_guide_stars = Column(Integer)
    alloc_num_iter = Column(Integer)
    alloc_elapsetime = Column(Float)
    alloc_rms_scatter = Column(Float)
    alloc_exectime = Column(DateTime)
    observed = Column(Boolean)

    pfsDesigns = relation(pfsDesign, backref=backref('pfsConfig'))

    def __init__(self, pfsConfigId, pfsDesignId, calibId, ra_config, dec_config, pa_config,
                 num_sci_allocated, num_cal_target, num_cal_allocated, num_sky_allocated, num_guide_stars,
                 alloc_num_iter, alloc_elapsetime, alloc_rms_scatter, alloc_exectime,
                 observed=False):
        self.pfsConfigId = pfsConfigId
        self.pfsDesignId = pfsDesignId
        self.calibId = calibId
        self.ra_config = ra_config
        self.dec_config = dec_config
        self.pa_config = pa_config
        self.num_sci_allocated = num_sci_allocated
        self.num_cal_allocated = num_cal_allocated
        self.num_sky_allocated = num_sky_allocated
        self.num_guide_stars = num_guide_stars
        self.alloc_num_iter = alloc_num_iter
        self.alloc_elapsetime = alloc_elapsetime
        self.alloc_rms_scatter = alloc_rms_scatter
        self.alloc_exectime = alloc_exectime
        self.observed = observed


class pfsConfigFiber(Base):
    __tablename__ = 'pfsConfigFiber'

    pfsConfigFiberId = Column(BigInteger, primary_key=True, autoincrement=False)
    pfsConfigId = Column(BigInteger, ForeignKey('pfsConfig.pfsConfigId'))
    cobraId = Column(Integer, ForeignKey('FiberPosition.cobraId'))
    targetId = Column(BigInteger, ForeignKey('Target.targetId'))
    pfiCenter_x = Column(Float)
    pfiCenter_y = Column(Float)
    mcsCenter_x = Column(Float)
    mcsCenter_y = Column(Float)
    motorMap = Column(Float)
    motorNumStep = Column(Float)
    configTime = Column(Float)
    onSource = Column(Boolean)

    pfsConfigs = relation(pfsConfig, backref=backref('psfConfigFiber'))
    targets = relation(Target, backref=backref('psfConfigFiber'))
    fiberPositions = relation(FiberPosition, backref=backref('psfConfigFiber'))

    def __init__(self, pfsConfigFiberId, pfsConfigId, cobraId, targetId,
                 pfiCenter_x, pfiCenter_y, mcsCenter_x, mcsCenter_y,
                 motorMap, motorNumStep, configTime,
                 onSource=True):
        #self.pfsConfigFiberId = pfsConfigFiberId
        self.pfsConfigFiberId = (pfsConfigId << 12) + cobraId
        self.pfsConfigId = pfsConfigId
        self.cobraId = cobraId
        self.targetId = targetId
        self.pfiCenter_x = pfiCenter_x
        self.pfiCenter_y = pfiCenter_y
        self.mcsCenter_x = mcsCenter_x
        self.mcsCenter_y = mcsCenter_y
        self.motorMap = motorMap
        self.motorNumStep = motorNumStep
        self.configTime = configTime
        self.onSource = onSource


class BeamSwitchMode(Base):
    __tablename__ = 'BeamSwitchMode'

    beamSwitchModeId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    description = Column(String)

    def __init__(self, beamSwitchModeId, name, description):
        self.beamSwitchModeId = beamSwitchModeId
        self.name = name
        self.description = description


class Exposure(Base):
    __tablename__ = 'Exposure'

    frameId = Column(String, primary_key=True, autoincrement=False)
    visit = Column(Integer, unique=True)
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)
    pfsConfigId = Column(BigInteger, ForeignKey('pfsConfig.pfsConfigId'))
    ra_tel = Column(Float)
    dec_tel = Column(Float)
    exptime = Column(Float)
    timeObsStart = Column(DateTime)
    timeObsEnd = Column(DateTime)
    mjdStart = Column(Float)
    mjdEnd = Column(Float)
    airmass = Column(Float)
    seeing = Column(Float)
    transp = Column(Float)
    background = Column(Float)
    throughput = Column(Float)
    cloudConditionId = Column(Integer, ForeignKey('CloudCondition.cloudConditionId'))
    focusing_error = Column(Float)
    insRotStart = Column(Float)
    insRotEnd = Column(Float)
    guideError_x = Column(Float)
    guideError_y = Column(Float)
    beamSwitchModeId = Column(Integer, ForeignKey('BeamSwitchMode.beamSwitchModeId'))
    beamSwitchOffsetRA = Column(Float)
    beamSwitchOffsetDec = Column(Float)

    pfsConfigs = relation(pfsConfig, backref=backref('Exposure'))
    cloudConditions = relation(CloudCondition, backref=backref('Exposure'))
    beamSwitchModes = relation(BeamSwitchMode, backref=backref('Exposure'))

    def __init__(self, frameId, visit, spectrograph, arm, armNum,
                 pfsConfigId, ra_tel, dec_tel, exptime, timeObsStart, timeObsEnd,
                 mjdStart, mjdEnd, airmass, seeing, transp, background, throughput,
                 cloudConditionId, guideError_x, guideError_y, focusing_error, insRotStart, insRotEnd,
                 beamSwitchModeId=0, beamSwitchOffsetRA=0.0, beamSwitchOffsetDec=0.0
                 ):
        self.frameId = frameId
        self.visit = visit
        self.sepctrograph = spectrograph
        self.arm = arm
        self.armNum = armNum
        self.pfsConfigId = pfsConfigId
        self.ra_tel = ra_tel
        self.dec_tel = dec_tel
        self.exptime = exptime
        self.timeObsStart = timeObsStart
        self.timeObsEnd = timeObsEnd
        self.mjdStart = mjdStart
        self.mjdEnd = mjdEnd
        self.airmass = airmass
        self.seeing = seeing
        self.transp = transp
        self.background = background
        self.cloudConditionId = cloudConditionId
        self.focusing_error = focusing_error
        self.insRotStart = insRotStart
        self.insRotEnd = insRotEnd
        self.guideError_x = guideError_x
        self.guideError_y = guideError_y
        self.beamSwitchModeId = beamSwitchModeId
        self.beamSwitchOffsetRA = beamSwitchOffsetRA
        self.beamSwitchOffsetDec = beamSwitchOffsetDec


class ObsFiber(Base):
    __tablename__ = 'ObsFiber'

    obsFiberId = Column(BigInteger, primary_key=True, autoincrement=True)
    frameId = Column(String, ForeignKey('Exposure.frameId'))
    visit = Column(Integer)
    pfsConfigFiberId = Column(BigInteger, ForeignKey('pfsConfigFiber.pfsConfigFiberId'))
    cobraId = Column(Integer)
    targetId = Column(BigInteger, ForeignKey('Target.targetId'))
    exptime = Column(Float)
    cum_nexp = Column(Integer)
    cum_texp = Column(Float)
    delta_pfi_x = Column(Float)
    delta_pfi_y = Column(Float)

    exposures = relation(Exposure, backref=backref('ObsFiber'), foreign_keys=[frameId])
    pfsConfigFibers = relation(pfsConfigFiber, backref=backref('ObsFiber'))
    targets = relation(Target, backref=backref('ObsFiber'))

    def __init__(self, frameId, visit, pfsConfigFiberId, cobraId, targetId,
                 exptime, cum_nexp, cum_texp, delta_pfi_x, delta_pfi_y):
        self.frameId = frameId
        self.visit = visit
        self.pfsConfigFiberId = pfsConfigFiberId
        self.cobraId = cobraId
        self.targetId = targetId
        self.exptime = exptime
        self.cum_nexp = cum_nexp
        self.cum_texp = cum_texp
        self.delta_pfi_x = delta_pfi_x
        self.delta_pfi_y = delta_pfi_y


class SkyModel(Base):
    __tablename__ = 'SkyModel'

    skyModelId = Column(Integer, primary_key=True, autoincrement=False)
    frameId = Column(String, ForeignKey('Exposure.frameId'))
    visit = Column(Integer)
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)

    exposures = relation(Exposure, backref=backref('SkyModel'))

    def __init__(self, skyModelId, frameId, visit, spectrograph, arm, armNum):
        self.skyModelId = skyModelId
        self.frameId = frameId
        self.visit = visit
        self.sepctrograph = spectrograph
        self.arm = arm
        self.armNum = armNum


class PsfModel(Base):
    __tablename__ = 'PsfModel'

    psfModelId = Column(Integer, primary_key=True, autoincrement=False)
    frameId = Column(String, ForeignKey('Exposure.frameId'))
    visit = Column(Integer)
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)

    exposures = relation(Exposure, backref=backref('PsfModel'))

    def __init__(self, psfModelId, frameId, visit, spectrograph, arm, armNum):
        self.psfModelId = psfModelId
        self.frameId = frameId
        self.visit = visit
        self.sepctrograph = spectrograph
        self.arm = arm
        self.armNum = armNum


class pfsArm(Base):
    __tablename__ = 'pfsArm'

    pfsArmId = Column(Integer, primary_key=True, autoincrement=True)
    frameId = Column(String, ForeignKey('Exposure.frameId'), unique=True)
    visit = Column(Integer)
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)
    calibFlatId = Column(Integer, ForeignKey('Calib.calibId'))
    calibBiasId = Column(Integer, ForeignKey('Calib.calibId'))
    calibDarkId = Column(Integer, ForeignKey('Calib.calibId'))
    calibFiberTraceId = Column(Integer, ForeignKey('Calib.calibId'))
    calibDetectorMapId = Column(Integer, ForeignKey('Calib.calibId'))
    pfsConfigId = Column(BigInteger, ForeignKey('pfsConfig.pfsConfigId'))
    skyModelId = Column(Integer, ForeignKey('SkyModel.skyModelId'))
    psfModelId = Column(Integer, ForeignKey('PsfModel.psfModelId'))
    flags = Column(Integer)
    processDate = Column(DateTime)
    DRP2DVersion = Column(String)

    exposures = relation(Exposure, backref=backref('pfsArm'))
    #calibs = relation(Calib, backref=backref('pfsArm'))
    pfsConfigs = relation(pfsConfig, backref=backref('pfsArm'))
    skyModels = relation(SkyModel, backref=backref('pfsArm'))
    psfModels = relation(PsfModel, backref=backref('pfsArm'))

    def __init__(self, pfsArmId, frameId, visit, spectrograph, arm, armNum,
                 calibFlatId, calibBiasId, calibDarkId, calibFiberTraceId,
                 pfsConfigId, skyModelId, psfModelId, flags,
                 processDate, DRP2DVersion):
        self.pfsArmId = pfsArmId
        self.frameId = frameId
        self.visit = visit
        self.spectrograph = spectrograph
        self.arm = arm
        self.armNum = armNum
        self.calibFlatId = calibFlatId
        self.calibBiasId = calibBiasId
        self.calibDarkId = calibDarkId
        self.calibFiberTraceId = calibFiberTraceId
        self.pfsConfigId = pfsConfigId
        self.skyModelId = skyModelId
        self.psfModelId = psfModelId
        self.flags = flags
        self.processDate = processDate
        self.DRP2DVersion = DRP2DVersion


class pfsArmObj(Base):
    __tablename__ = 'pfsArmObj'

    pfsArmObjId = Column(BigInteger, primary_key=True, autoincrement=True)
    pfsArmId = Column(Integer, ForeignKey('pfsArm.pfsArmId'))
    frameId = Column(String)
    visit = Column(Integer)
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)
    cobraId = Column(Integer, ForeignKey('FiberPosition.cobraId'))
    pfsConfigFiberId = Column(BigInteger, ForeignKey('pfsConfigFiber.pfsConfigFiberId'))
    flags = Column(Integer)
    QATypeId = Column(Integer, ForeignKey('QAType.QATypeId'))
    QAValue = Column(Float)

    pfsArms = relation(pfsArm, backref=backref('pfsArmObj'))
    pfsConfigFibers = relation(pfsConfigFiber, backref=backref('psfArmObj'))
    fiberPositions = relation(FiberPosition, backref=backref('pfsArmObj'))
    qaTypes = relation(QAType, backref=backref('pfsArmObj'))

    def __init__(self, pfsArmId, visit, spectrograph, arm, armNum,
                 cobraId, pfsConfigFiberId, flags, QATypeId, QAValue):
        self.pfsArmId = pfsArmId
        self.visit = visit
        self.spectrograph = spectrograph
        self.arm = arm
        self.armNum = armNum
        self.cobraId = cobraId
        self.pfsConfigFiberId = pfsConfigFiberId
        self.flags = flags
        self.QATypeId = QATypeId
        self.QAValue = QAValue


class pfsObject(Base):
    __tablename__ = 'pfsObject'

    pfsObjectId = Column(String, primary_key=True, autoincrement=False)
    targetId = Column(BigInteger, ForeignKey('Target.targetId'))
    tract = Column(Integer)
    patch = Column(String)
    catId = Column(Integer)
    objId = Column(BigInteger)
    nVisit = Column(Integer)
    pfsVisitHash = Column(BigInteger, unique=True)
    cum_texp = Column(Float)
    processDate = Column(DateTime)
    pipeline2DVersion = Column(String)
    fluxCalibId = Column(Integer, ForeignKey('FluxCalib.fluxCalibId'))
    flags = Column(Integer)
    QATypeId = Column(Integer, ForeignKey('QAType.QATypeId'))
    QAValue = Column(Float)

    targets = relation(Target, backref=backref('pfsObject'))
    fluxCalibs = relation(FluxCalib, backref=backref('pfsObject'))
    qaTypes = relation(QAType, backref=backref('pfsObject'))

    def __init__(self, pfsObjectId, targetId, tract, patch, catId, objId, nVisit, pfsVisitHash,
                 cum_texp, processDate, pipeline2DVersion, fluxCalibId, flags, QATypeId, QAValue):
        self.pfsObjectId = pfsObjectId
        self.targetId = targetId
        self.tract = tract
        self.patch = patch
        self.catId = catId
        self.objId = objId
        self.nVisit = nVisit
        self.pfsVisitHash = psfVisitHash
        self.cum_texp = cum_texp
        self.processDate = processDate
        self.pipeline2DVesion = pipeline2DVesion
        self.fluxCalibId = fluxCalibId
        self.flags = flags
        self.QATypeId = QATypeId
        self.QAValue = QAValue


class VisitsToCombine(Base):
    __tablename__ = 'VisitsToCombine'

    visitsToCombineId = Column(BigInteger, primary_key=True, autoincrement=True)
    targetid = Column(BigInteger, ForeignKey('Target.targetId'))
    visit = Column(Integer, ForeignKey('Exposure.visit'))
    pfsVisitHash = Column(BigInteger, ForeignKey('pfsObject.pfsVisitHash'))

    targets = relation(Target, backref=backref('VisitsToCombine'))
    exposures = relation(Exposure, backref=backref('VisitsToCombine'))
    pfsObjects = relation(pfsObject, backref=backref('VisitsToCombine'))

    def __init__(self, targetId, visit, pfsVisitHash):
        self.targetId = targetId
        self.visit = visit
        self.pfsVisitHash = pfsVisitHash


class ObjType(Base):
    __tablename__ = 'ObjType'

    objTypeId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    description = Column(String)

    def __init__(self, objTypeId, name, description):
        self.objTypeId = objTypeId
        self.name = name
        self.description = description


class StarType(Base):
    __tablename__ = 'StarType'

    starTypeId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    description = Column(String)

    def __init__(self, starTypeId, name, description):
        self.starTypeId = starTypeId
        self.name = name
        self.description = description


class SpecParam(Base):
    __tablename__ = 'SpecParam'

    specParamId = Column(Integer, primary_key=True, autoincrement=False)
    pfsObjectId = Column(String, ForeignKey('pfsObject.pfsObjectId'))
    redshift = Column(Float)
    z_mean = Column(Float)
    z_median = Column(Float)
    z_percentileXX = Column(Float)
    objTypeId = Column(Integer, ForeignKey('ObjType.objTypeId'))
    flags = Column(Integer)
    processDate = Column(DateTime)
    DRP1DVersion = Column(String)

    pfsObjects = relation(pfsObject, backref=backref('specParam'))
    objTypes = relation(ObjType, backref=backref('specParam'))

    def __init__(self, specParamId, pfsObjectId, redshift, z_mean, z_median, z_percentileXX,
                 objTypeId, flags, processDate, DRP1DVersion):
        self.specParamId = specParamId
        self.pfsObjectId = pfsObjectId
        self.redshift = redshift
        self.z_mean = z_mean
        self.z_median = z_median
        self.z_percentileXX = z_percentileXX
        self.objTypeId = objTypeId
        self.flags = flags
        self.processDate = processDate
        self.DRP1DVersion = DRP1DVersion


class StarSpecParam(Base):
    __tablename__ = 'StarSpecParam'

    starSpecParamId = Column(Integer, primary_key=True, autoincrement=False)
    pfsObjectId = Column(String, ForeignKey('pfsObject.pfsObjectId'), primary_key=True)
    starTypeId = Column(Integer, ForeignKey('StarType.starTypeId'))
    velocity = Column(Float)
    metallicity = Column(Float)
    logg = Column(Float)
    teff = Column(Float)
    flags = Column(Integer)
    processDate = Column(DateTime)
    DRPGAVersion = Column(String)

    pfsObjects = relation(pfsObject, backref=backref('starSpecParam'))
    starTypes = relation(StarType, backref=backref('starSpecParam'))

    def __init__(self, pfsObjectId, starTypeId, velocity, metallicity, logg, teff,
                 flags, processDate, pipelneStellarVersion):
        self.pfsObjectId = pfsObjectId
        self.starTypeId = startTypeId
        self.velocity = velocity
        self.metallicity = metallicity
        self.logg = logg
        self.teff = teff
        self.flags = flags
        self.processDate = processDate
        self.DRPGAVersion = DRPGAVersion


class LineList(Base):
    __tablename__ = 'LineList'

    lineId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    wavelength = Column(Float)

    def __init__(self, lineId, name, wavelength):
        self.lineId = lineId
        self.name = name
        self.wavelength = wavelength


class SpecLine(Base):
    __tablename__ = 'SpecLine'

    specLineId = Column(Integer, primary_key=True, autoincrement=False)
    pfsObjectId = Column(String, ForeignKey('pfsObject.pfsObjectId'))
    lineId = Column(Integer, ForeignKey('LineList.lineId'))
    wavelength = Column(Float)
    z = Column(Float)
    sigma = Column(Float)
    area = Column(Float)
    ew = Column(Float)
    contlevel = Column(Float)
    chi2 = Column(Float)

    pfsObjects = relation(pfsObject, backref=backref('specLine'))
    lineLists = relation(LineList, backref=backref('specLine'))

    def __init__(self, pfsObjectId, lineId, wavelength, z, sigma, ew, contlevel, chi2):
        self.specLineId = specLineId
        self.pfsObjectId = pfsObjectId
        self.lineId = lineId
        self.wavelength = wavelength
        self.z = z
        self.sigma = sigma
        self.area = area
        self.ew = ew
        self.contlevel = contlevel
        self.chi2 = chi2


def make_database(dbinfo):
    '''
    dbinfo is something like this: postgresql://xxxxx:yyyyy@zzz.zzz.zzz.zz/dbname 
    '''
    #engine = create_engine('sqlite:///:memory:', echo=True)
    #engine = create_engine('sqlite:///pfs_proto.sqlite', echo=False)
    engine = create_engine(dbinfo)

    Base.metadata.drop_all(engine)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()


if __name__ == '__main__':
    import sys
    dbinfo = sys.argv[1]
    print(dbinfo)
    make_database(dbinfo)
