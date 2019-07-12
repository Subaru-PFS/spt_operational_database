from sqlalchemy import create_engine
from sqlalchemy import Column, BigInteger, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation, backref

Base = declarative_base()


class Proposal(Base):
    __tablename__ = 'Proposal'

    proposalId = Column(String, primary_key=True, autoincrement=False)

    def __init__(self, proposalId):
        self.proposalId = proposalId


class Program(Base):
    __tablename__ = 'Program'

    programId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    description = Column(String)
    proposalId = Column(String, ForeignKey('Proposal.proposalId'))
    filler = Column(Boolean)

    proposals = relation(Proposal, backref=backref('Program'))

    def __init__(self, programId, name, description, proposalId, filler):
        self.programId = programId
        self.name = name
        self.description = description
        self.proposalId = proposalId
        self.filler = filler


class TargetType(Base):
    __tablename__ = 'TargetType'

    targetTypeId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    description = Column(String)

    def __init__(self, targetTypeId, name, description):
        self.targetTypeId = targetTypeId
        self.name = name
        self.description = description


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
    fiberId = Column(Integer, primary_key=True, autoincrement=False)
    ftype = Column(String)
    x = Column(Float(precision=24))
    y = Column(Float(precision=24))

    def __init__(self, fiberId, ftype, x, y):
        self.fiberId = fiberId
        self.ftype = ftype
        self.x = x
        self.y = y


class CobraPosition(Base):
    __tablename__ = 'CobraPosition'
    cobraId = Column(Integer, primary_key=True, autoincrement=False)
    fiberId = Column(Integer, ForeignKey('FiberPosition.fiberId'))
    fld = Column(Integer)
    cf = Column(Integer)
    mf = Column(Integer)
    cm = Column(Integer)
    mod = Column(String)
    x = Column(Float(precision=24))
    y = Column(Float(precision=24))
    r = Column(Float(precision=24))
    sp = Column(Integer)
    fh = Column(Integer)
    sfib = Column(Integer)
    fiberIdLNA = Column(String)

    fiberPositions = relation(FiberPosition, backref=backref('CobraPosition'))

    def __init__(self, cobraId, fiberId, fld, cf, mf, cm, mod, x, y, r, sp, fh, sfib, fiberIdLNA):
        self.cobraId = cobraId
        self.fiberId = fiberId
        self.fld = fld
        self.cf = cf
        self.mf = mf
        self.cm = cm
        self.mod = mod
        self.x = x
        self.y = y
        self.r = r
        self.sp = sp
        self.fh = fh
        self.sfib = sfib
        self.fiberIdLNA = fiberIdLNA


class FiducialFiberPosition(Base):
    __tablename__ = 'FiducialFiberPosition'
    ffId = Column(Integer, primary_key=True, autoincrement=False)
    fiberId = Column(Integer, ForeignKey('FiberPosition.fiberId'))
    ff = Column(Integer)
    fff = Column(Integer)
    fftype = Column(String)
    fft = Column(Integer)
    x = Column(Float(precision=24))
    y = Column(Float(precision=24))

    fiberPositions = relation(FiberPosition, backref=backref('FiducialFiberPosition'))

    def __init__(self, ffId, fiberId, ff, fff, fftype, fft, x, y):
        self.ffId = ffId
        self.fiberId = fiberId
        self.ff = ff
        self.fff = fff
        self.fftype = fftype
        self.fft = fft
        self.x = x
        self.y = y


class Target(Base):
    __tablename__ = 'Target'

    targetId = Column(BigInteger, primary_key=True, autoincrement=True)
    programId = Column(Integer, ForeignKey('Program.programId'))
    objId = Column(BigInteger)
    ra = Column(Float(precision=24))
    dec = Column(Float(precision=24))
    tract = Column(Integer)
    patch = Column(String)
    priority = Column(Float(precision=24))
    targetTypeId = Column(Integer, ForeignKey('TargetType.targetTypeId'))
    catId = Column(Integer, ForeignKey('InputCatalog.catId'))
    catObjId = Column(BigInteger)
    fiberMag_g = Column(Float(precision=24))
    fiberMag_r = Column(Float(precision=24))
    fiberMag_i = Column(Float(precision=24))
    fiberMag_z = Column(Float(precision=24))
    fiberMag_y = Column(Float(precision=24))
    fiberMag_j = Column(Float(precision=24))
    fiducialExptime = Column(Float(precision=24))
    photz = Column(Float(precision=24))
    mediumResolution = Column(Boolean)
    QATypeId = Column(Integer, ForeignKey('QAType.QATypeId'))
    QALambdaMin = Column(Float(precision=24))
    QALambdaMax = Column(Float(precision=24))
    QAThreshold = Column(Float(precision=24))
    QALineFlux = Column(Float(precision=24))
    completeness = Column(Float(precision=24))
    finished = Column(Boolean)

    programs = relation(Program, backref=backref('Target'))
    targetTypes = relation(TargetType, backref=backref('Target'))
    inputCatalogs = relation(InputCatalog, backref=backref('Target'))
    qaTypes = relation(QAType, backref=backref('Target'))

    def __init__(self, programId, objId, ra, dec, tract, patch, priority, targetTypeId, catId, catObjId,
                 fiberMag_g, fiberMag_r, fiberMag_i, fiberMag_z, fiberMag_y,
                 fiberMag_j, fiducialExptime, photz, mediumResolution,
                 QATypeId, QALambdaMin, QALambdaMax, QAThreshold, QALineFlux,
                 completeness=0.0, finished=False):
        self.programId = programId
        self.objId = objId
        self.ra = ra
        self.dec = dec
        self.tract = tract
        self.patch = patch
        self.priority = priority
        self.targetTypeId = targetTypeId
        self.catId = catId
        self.catObjId = catObjId
        self.fiberMag_g = fiberMag_g
        self.fiberMag_r = fiberMag_r
        self.fiberMag_i = fiberMag_i
        self.fiberMag_z = fiberMag_z
        self.fiberMag_y = fiberMag_y
        self.fiberMag_j = fiberMag_j
        self.fiducialExptime = fiducialExptime
        self.photz = photz
        self.mediumResolution = mediumResolution
        self.QATypeId = QATypeId
        self.QALambdaMin = QALambdaMin
        self.QALambdaMax = QALambdaMax
        self.QAThreshold = QAThreshold
        self.QALineFlux = QALineFlux
        self.completeness = completeness
        self.finished = finished


class GuideStars(Base):
    __tablename__ = 'GuideStars'
    guideStarId = Column(BigInteger, primary_key=True, autoincrement=False)
    ra = Column(Float(precision=24))
    dec = Column(Float(precision=24))
    catId = Column(Integer, ForeignKey('InputCatalog.catId'))
    objTypeId = Column(Integer, ForeignKey('ObjType.objTypeId'))
    mag_agc = Column(Float(precision=24))
    flux_agc = Column(Float(precision=24))
    flags = Column(Integer)

    inputCatalogs = relation(InputCatalog, backref=backref('GuideStars'))
    objTypes = relation(ObjType, backref=backref('GuideStars'))

    def __init__(self, guideStarId, ra, dec, catId, mag_agc, flux_agc, flags):
        self.guideStarId = guideStarId
        self.ra = ra
        self.dec = dec
        self.catId = catId
        self.mag_agc = mag_agc
        self.flux_agc = flux_agc
        self.flags = flags


class Tile(Base):
    __tablename__ = 'Tile'

    tileId = Column(Integer, primary_key=True, autoincrement=True)
    programId = Column(Integer, ForeignKey('Program.programId'))
    tile = Column(Integer)
    raCenter = Column(Float(precision=24))
    decCenter = Column(Float(precision=24))
    pa = Column(Float(precision=24))
    finished = Column(Boolean)

    programs = relation(Program, backref=backref('Tile'))

    def __init__(self, programId, tile, raCenter, decCenter, pa, finished):
        self.programId = programId
        self.tile = tile
        self.raCenter = raCenter
        self.decCenter = decCenter
        self.pa = pa
        self.finished = finished


class pfsDesign(Base):
    __tablename__ = 'pfsDesign'

    pfsDesignId = Column(BigInteger, primary_key=True, autoincrement=False)
    tileId = Column(Integer, ForeignKey('Tile.tileId'))
    raCenter = Column(Float(precision=24))
    decCenter = Column(Float(precision=24))
    paConfig = Column(Float(precision=24))
    numSciDesigned = Column(Integer)
    numCalDesigned = Column(Integer)
    numSkyDesigned = Column(Integer)
    numGuideStars = Column(Integer)
    exptime = Column(Float(precision=24))
    minExptime = Column(Float(precision=24))
    etsVersion = Column(String)
    etsAssigner = Column(String)
    etsExectime = Column(DateTime)
    obsolete = Column(Boolean)

    tiles = relation(Tile, backref=backref('pfsDesign'))

    def __init__(self, pfsDesignId, tileId, raCenter, decCenter, paConfig,
                 numSciDesigned, numCalDesigned, numSkyDesigned, numGuideStars,
                 exptime, minExptime, etsVersion, etsAssgner, etsExectime, obsolete=False):
        self.pfsDesignId = pfsDesignId
        self.tileId = tileId
        self.raCenter = raCenter
        self.decCenter = decCenter
        self.paConfig = paConfig
        self.numSciDesigned = numSciDesigned
        self.numCalDesigned = numCalDesigned
        self.numSkyDesigned = numSkyDesigned
        self.numGuideStars = numGuideStars
        self.exptime = exptime
        self.minExptime = minExptime
        self.etsVersion = etsVersion
        self.etsAssigner = etsAssigner
        self.etsExectime = etsExectime
        self.obsolete = obsolete


class pfsDesignFiber(Base):
    __tablename__ = 'pfsDesignFiber'

    pfsDesignFiberId = Column(BigInteger, primary_key=True, autoincrement=True)
    pfsDesignId = Column(BigInteger, ForeignKey('pfsDesign.pfsDesignId'))
    fiberId = Column(Integer, ForeignKey('FiberPosition.fiberId'))
    targetId = Column(BigInteger, ForeignKey('Target.targetId'))
    tract = Column(Integer)
    patch = Column(String)
    ra = Column(Float(precision=24))
    dec = Column(Float(precision=24))
    catId = Column(Integer, ForeignKey('InputCatalog.catId'))
    objId = Column(BigInteger)
    targetTypeId = Column(Integer, ForeignKey('TargetType.targetTypeId'))
    fiberMag_g = Column(Float(precision=24))
    fiberMag_r = Column(Float(precision=24))
    fiberMag_i = Column(Float(precision=24))
    fiberMag_z = Column(Float(precision=24))
    fiberMag_y = Column(Float(precision=24))
    fiberMag_j = Column(Float(precision=24))
    etsPriority = Column(Integer)
    etsCostFunction = Column(String)
    etsCobraMovement = Column(String)
    pfiNominal_x = Column(Float(precision=24))
    pfiNominal_y = Column(Float(precision=24))
    onSource = Column(Boolean)

    pfsDesigns = relation(pfsDesign, backref=backref('pfsDesignFiber'))
    targets = relation(Target, backref=backref('pfsDesignFiber'))
    fiberPositions = relation(FiberPosition, backref=backref('pfsDesignFiber'))
    #targetTypes = relation(TargetType, backref=backref('pfsDesignFiber'))
    #inputCatalogs = relation(InputCatalog, backref=backref('pfsDesignFiber'))

    def __init__(self, pfsDesignFiberId, pfsDesignId, fiberId,
                 targetId, tract, patch, ra, dec, catId, objId, targetTypeId,
                 fiberMag_g, fiberMag_r, fiberMag_i, fiberMag_z, fiberMag_y, fiberMag_j,
                 etsPriority, etsCostFunction, etsCobraMovement,
                 pfiNominal_x, pfiNominal_y,
                 onSource=True):
        self.pfsDesignFiberId = (pfsDesignId << 12) + fiberId
        self.pfsDesignId = pfsDesignId
        self.fiberId = fiberId
        self.targetId = targetId
        self.tract = tract
        self.patch = patch
        self.ra = ra
        self.dec = dec
        self.catId = catId
        self.objId = objId
        self.targetTypeId = targetTypeId
        self.fiberMag_g = fiberMag_g
        self.fiberMag_r = fiberMag_r
        self.fiberMag_i = fiberMag_i
        self.fiberMag_z = fiberMag_z
        self.fiberMag_y = fiberMag_y
        self.fiberMag_j = fiberMag_j
        self.etsPriority = etsPriority
        self.etsCostFunction = etsCostFunction
        self.etsCobraMovement = etsCobraMovement
        self.pfiNominal_x = pfiNominal_x
        self.pfiNominal_y = pfiNominal_y
        self.onSource = onSource


class Calib(Base):
    __tablename__ = 'Calib'

    calibId = Column(Integer, primary_key=True, autoincrement=False)
    calibType = Column(String)
    calibDate = Column(DateTime)
    pfsDesignId = Column(BigInteger, ForeignKey('pfsDesign.pfsDesignId'))
    spectrograph = Column(Integer)
    arm = Column(String)
    exptime = Column(Float(precision=24))
    visitsInUse = Column(String)

    pfsDesigns = relation(pfsDesign, backref=backref('Calib'))

    def __init__(self, calibId, calibType, calibDate, pfsDesignId, spectrogarph, arm,
                 exptime, visitsInUse):
        self.calibId = calibId
        self.calibType = calibType
        self.calibDate = calibDate
        self.pfsDesignId = pfsDesignId
        self.spectrograph = spectrograph
        self.arm = arm
        self.exptime = exptime
        self.visitsInUse = visitsInUse


class FluxCalib(Base):
    __tablename__ = 'FluxCalib'

    fluxCalibId = Column(Integer, primary_key=True, autoincrement=False)
    fluxCalibType = Column(String)
    fluxCalibDate = Column(DateTime)
    fluxCalibStarTeff = Column(Float(precision=24))
    fluxCalibStarLogg = Column(Float(precision=24))
    fluxCalibStarZ = Column(Float(precision=24))

    def __init__(self, fluxCalibId, fluxCalibType, fluxCalibDate,
                 fluxCalibStarTeff, fluxCalibStarLogg, fluxCalibStarZ):
        self.fluxCalibId = fluxCalibId
        self.fluxCalibType = fluxCalibType
        self.fluxCalibDate = fluxCalibDate
        self.fluxCalibStarTeff = fluxCalibStarTeff
        self.fluxCalibStarLogg = fluxCalibStarLogg
        self.fluxCalibStarZ = fluxCalibStarZ


class Visit(Base):
    __tablename__ = 'Visit'

    visit = Column(Integer, primary_key=True, autoincrement=False)
    visitTypeId = Column(Integer)
    description = Column(String)

    def __init__(self, visit, visitTypeId, description):
        self.visit = visit
        self.visitTypeId = visitTypeId
        self.description = description


class mcsData(Base):

    __tablename__ = 'mcsData'

    mcsId = Column(Integer, primary_key=True, autoincrement=True)
    datatime = Column(DateTime)
    frameId = Column(Integer, index=True)
    moveId = Column(Integer)
    fiberId = Column(Integer)
    centroidx = Column(Float(precision=24))
    centroidy = Column(Float(precision=24))
    fwhmx = Column(Float(precision=24))
    fwhmy = Column(Float(precision=24))
    bgvalue = Column(Float(precision=24))
    peakvalue = Column(Float(precision=24))

    def __init__(self, mcsId, datatime, frameId, moveId, fiberId,
                 centroidx, centroidy, fwhmx, fwhmy, bgvalue, peakvalue):
        self.mcsId = mcsId
        self.datatime = datatime
        self.frameId = frameId
        self.moveId = moveId
        self.fiberId = fiberId
        self.centroidx = centroidx
        self.centroidy = centroidy
        self.fwhmx = fwhmx
        self.fwhmy = fwhmy
        self.bgvalue = bgvalue
        self.peakvalue = peakvalue


class pfsConfig(Base):
    __tablename__ = 'pfsConfig'

    pfsConfigId = Column(BigInteger, primary_key=True, autoincrement=False)
    pfsDesignId = Column(BigInteger, ForeignKey('pfsDesign.pfsDesignId'))
    visit0 = Column(Integer, ForeignKey('Visit.visit'))
    raCenter = Column(Float(precision=24))
    decCenter = Column(Float(precision=24))
    paConfig = Column(Float(precision=24))
    telEl = Column(Float(precision=24))
    insRot = Column(Float(precision=24))
    numSciAllocated = Column(Integer)
    numCalAllocated = Column(Integer)
    numSkyAllocated = Column(Integer)
    numGuideStars = Column(Integer)
    exptime = Column(Float(precision=24))
    minExptime = Column(Float(precision=24))
    allocNumIter = Column(Integer)
    allocElapsetime = Column(Float(precision=24))
    allocRmsScatter = Column(Float(precision=24))
    allocExectime = Column(DateTime)
    observed = Column(Boolean)

    pfsDesigns = relation(pfsDesign, backref=backref('pfsConfig'))

    visits = relation(Visit, backref=backref('pfsConfig'))

    def __init__(self, pfsConfigId, pfsDesignId, visit0, raCenter, decCenter, paConfig, telEl, insRot,
                 numSciAllocated, numCalAllocated, numSkyAllocated, numGuideStars,
                 exptime, minExptime, allocNumIter, allocElapsetime, allocRmsScatter, allocExectime,
                 observed=False):
        self.pfsConfigId = pfsConfigId
        self.pfsDesignId = pfsDesignId
        self.visit0 = visit0
        self.raCenter = raCenter
        self.decCenter = decCenter
        self.paConfig = paConfig
        self.telEl = telEl
        self.insRot = insRot
        self.numSciAllocated = numSciAllocated
        self.numCalAllocated = numCalAllocated
        self.numSkyAllocated = numSkyAllocated
        self.numGuideStars = numGuideStars
        self.exptime = exptime
        self.minExptime = minExptime
        self.allocNumIter = allocNumIter
        self.allocElapsetime = allocElapsetime
        self.allocRmsScatter = allocRmsScatter
        self.allocExectime = allocExectime
        self.observed = observed


class pfsConfigFiber(Base):
    __tablename__ = 'pfsConfigFiber'

    pfsConfigFiberId = Column(BigInteger, primary_key=True, autoincrement=True)
    pfsConfigId = Column(BigInteger, ForeignKey('pfsConfig.pfsConfigId'))
    fiberId = Column(Integer, ForeignKey('FiberPosition.fiberId'))
    targetId = Column(BigInteger, ForeignKey('Target.targetId'))
    tract = Column(Integer)
    patch = Column(String)
    ra = Column(Float(precision=24))
    dec = Column(Float(precision=24))
    catId = Column(Integer, ForeignKey('InputCatalog.catId'))
    objId = Column(BigInteger)
    targetTypeId = Column(Integer, ForeignKey('TargetType.targetTypeId'))
    fiberMag_g = Column(Float(precision=24))
    fiberMag_r = Column(Float(precision=24))
    fiberMag_i = Column(Float(precision=24))
    fiberMag_z = Column(Float(precision=24))
    fiberMag_y = Column(Float(precision=24))
    fiberMag_j = Column(Float(precision=24))
    pfiNominal_x = Column(Float(precision=24))
    pfiNominal_y = Column(Float(precision=24))
    pfiCenter_x = Column(Float(precision=24))
    pfiCenter_y = Column(Float(precision=24))
    pfiDiff_x = Column(Float(precision=24))
    pfiDiff_y = Column(Float(precision=24))
    mcsCenter_x = Column(Float(precision=24))
    mcsCenter_y = Column(Float(precision=24))
    motorMapSummary = Column(String)
    configTime = Column(Float(precision=24))
    onSource = Column(Boolean)

    pfsConfigs = relation(pfsConfig, backref=backref('psfConfigFiber'))
    targets = relation(Target, backref=backref('psfConfigFiber'))
    fiberPositions = relation(FiberPosition, backref=backref('psfConfigFiber'))
    #targetTypes = relation(TargetType, backref=backref('pfsConfigFiber'))
    #inputCatalogs = relation(InputCatalog, backref=backref('pfsDesignFiber'))

    def __init__(self, pfsConfigFiberId, pfsConfigId, fiberId,
                 targetId, tract, patch, catId, objId, targetTypeId,
                 pfiNominal_x, pfiNominal_y, pfiCenter_x, pfiCenter_y, pfiDiff_x, pfiDiff_y,
                 mcsCenter_x, mcsCenter_y, motorMapSummary, configTime,
                 onSource=True):
        #self.pfsConfigFiberId = pfsConfigFiberId
        self.pfsConfigFiberId = (pfsConfigId << 12) + fiberId
        self.pfsConfigId = pfsConfigId
        self.fiberId = fiberId
        self.targetId = targetId
        self.tract = tract
        self.patch = patch
        self.ra = ra
        self.dec = dec
        self.catId = catId
        self.objId = objId
        self.targetTypeId = targetTypeId
        self.fiberMag_g = fiberMag_g
        self.fiberMag_r = fiberMag_r
        self.fiberMag_i = fiberMag_i
        self.fiberMag_z = fiberMag_z
        self.fiberMag_y = fiberMag_y
        self.fiberMag_j = fiberMag_j
        self.pfiNominal_x = pfiNominal_x
        self.pfiNominal_y = pfiNominal_y
        self.pfiCenter_x = pfiCenter_x
        self.pfiCenter_y = pfiCenter_y
        self.pfiDiff_x = pfiDiff_x
        self.pfiDiff_y = pfiDiff_y
        self.mcsCenter_x = mcsCenter_x
        self.mcsCenter_y = mcsCenter_y
        self.motorMapSummary = motorMapSummary
        self.configTime = configTime
        self.onSource = onSource


class CobraConfig(Base):
    __tablename__ = 'CobraConfig'

    cobraConfigId = Column(BigInteger, primary_key=True, autoincrement=True)
    pfsConfigFiberId = Column(BigInteger, ForeignKey('pfsConfigFiber.pfsConfigFiberId'))
    iteration = Column(Integer)
    motorNumStepTheta = Column(Integer)
    motorNumStepPhi = Column(Integer)
    mcsId = Column(Integer, ForeignKey('mcsData.mcsId'))
    pfiNominal_x = Column(Float(precision=24))
    pfiNominal_y = Column(Float(precision=24))
    pfiCenter_x = Column(Float(precision=24))
    pfiCenter_y = Column(Float(precision=24))
    pfiDiff_x = Column(Float(precision=24))
    pfiDiff_y = Column(Float(precision=24))
    mcsCenter_x = Column(Float(precision=24))
    mcsCenter_y = Column(Float(precision=24))
    exectime = Column(DateTime)

    def __init__(self, cobraConfigId, pfsConfigFiberId, iteration, motorNumStepTheta, motorNumStepPhi, mcsId,
                 pfiNominal_x, pfiNominal_y, pfiCenter_x, pfiCenter_y, pfiDiff_x, pfiDiff_y,
                 mcsCenter_x, mcsCenter_y, exectime):
        self.cobraConfigId = cobraConfigId
        self.pfsConfigFiberId = pfsConfigFiberId
        self.iteration = iteration
        self.motorNumStepTheta = motorNumStepTheta
        self.motorNumStepPhi = motorNumStepPhi
        self.mcsId = mcsId
        self.pfiNominal_x = pfiNominal_x
        self.pfiNominal_y = pfiNominal_y
        self.pfiCenter_x = pfiCenter_x
        self.pfiCenter_y = pfiCenter_y
        self.pfiDiff_x = pfiDiff_x
        self.pfiDiff_y = pfiDiff_y
        self.mcsCenter_x = mcsCenter_x
        self.mcsCenter_y = mcsCenter_y
        self.exectime = exectime


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
    visit = Column(Integer, ForeignKey('Visit.visit'))
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)
    pfsConfigId = Column(BigInteger, ForeignKey('pfsConfig.pfsConfigId'))
    ra_tel = Column(Float(precision=24))
    dec_tel = Column(Float(precision=24))
    exptime = Column(Float(precision=24))
    timeObsStart = Column(DateTime)
    timeObsEnd = Column(DateTime)
    mjdStart = Column(Float(precision=24))
    mjdEnd = Column(Float(precision=24))
    airmass = Column(Float(precision=24))
    seeing = Column(Float(precision=24))
    transp = Column(Float(precision=24))
    background = Column(Float(precision=24))
    moonPhase = Column(Float(precision=24))
    moonAlt = Column(Float(precision=24))
    moonSep = Column(Float(precision=24))
    throughput = Column(Float(precision=24))
    cloudConditionId = Column(Integer, ForeignKey('CloudCondition.cloudConditionId'))
    focusing_error = Column(Float(precision=24))
    insRotStart = Column(Float(precision=24))
    insRotEnd = Column(Float(precision=24))
    guideError_dx = Column(Float(precision=24))
    guideError_dy = Column(Float(precision=24))
    beamSwitchModeId = Column(Integer, ForeignKey('BeamSwitchMode.beamSwitchModeId'))
    beamSwitchOffsetRA = Column(Float(precision=24))
    beamSwitchOffsetDec = Column(Float(precision=24))
    mediumResolution = Column(Boolean)

    visits = relation(Visit, backref=backref('Exposure'))
    pfsConfigs = relation(pfsConfig, backref=backref('Exposure'))
    cloudConditions = relation(CloudCondition, backref=backref('Exposure'))
    beamSwitchModes = relation(BeamSwitchMode, backref=backref('Exposure'))

    def __init__(self, frameId, visit, spectrograph, arm, armNum,
                 pfsConfigId, ra_tel, dec_tel, exptime, timeObsStart, timeObsEnd,
                 mjdStart, mjdEnd, airmass, seeing, transp, background, moonPhase, moonAlt, moonSep,
                 throughput, cloudConditionId, guideError_dx, guideError_dy, focusing_error,
                 insRotStart, insRotEnd, beamSwitchModeId=0, beamSwitchOffsetRA=0.0, beamSwitchOffsetDec=0.0,
                 mediumResolution=False
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
        self.moonPhase = moonPhase
        self.moonAlt = moonAlt
        self.moonSep = moonSep
        self.throughput = throughput
        self.cloudConditionId = cloudConditionId
        self.focusing_error = focusing_error
        self.insRotStart = insRotStart
        self.insRotEnd = insRotEnd
        self.guideError_dx = guideError_dx
        self.guideError_dy = guideError_dy
        self.beamSwitchModeId = beamSwitchModeId
        self.beamSwitchOffsetRA = beamSwitchOffsetRA
        self.beamSwitchOffsetDec = beamSwitchOffsetDec
        self.mediumResolution = mediumResolution


class ObsFiber(Base):
    __tablename__ = 'ObsFiber'

    obsFiberId = Column(BigInteger, primary_key=True, autoincrement=True)
    frameId = Column(String, ForeignKey('Exposure.frameId'))
    visit = Column(Integer, ForeignKey('Visit.visit'))
    pfsConfigFiberId = Column(BigInteger, ForeignKey('pfsConfigFiber.pfsConfigFiberId'))
    fiberId = Column(Integer)
    targetId = Column(BigInteger, ForeignKey('Target.targetId'))
    exptime = Column(Float(precision=24))
    cum_nexp = Column(Integer)
    cum_texp = Column(Float(precision=24))
    delta_pfi_x = Column(Float(precision=24))
    delta_pfi_y = Column(Float(precision=24))

    visits = relation(Visit, backref=backref('ObsFiber'))
    exposures = relation(Exposure, backref=backref('ObsFiber'))
    pfsConfigFibers = relation(pfsConfigFiber, backref=backref('ObsFiber'))
    targets = relation(Target, backref=backref('ObsFiber'))

    def __init__(self, frameId, visit, pfsConfigFiberId, fiberId, targetId,
                 exptime, cum_nexp, cum_texp, delta_pfi_x, delta_pfi_y):
        self.frameId = frameId
        self.visit = visit
        self.pfsConfigFiberId = pfsConfigFiberId
        self.fiberId = fiberId
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
    visit = Column(Integer, ForeignKey('Visit.visit'))
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)

    visits = relation(Visit, backref=backref('SkyModel'))
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
    visit = Column(Integer, ForeignKey('Visit.visit'))
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)

    visits = relation(Visit, backref=backref('PsfModel'))
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
    visit = Column(Integer, ForeignKey('Visit.visit'))
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)
    calibFlatId = Column(Integer, ForeignKey('Calib.calibId'))
    calibBiasId = Column(Integer, ForeignKey('Calib.calibId'))
    calibDarkId = Column(Integer, ForeignKey('Calib.calibId'))
    calibArcsId = Column(Integer, ForeignKey('Calib.calibId'))
    pfsConfigId = Column(BigInteger, ForeignKey('pfsConfig.pfsConfigId'))
    skyModelId = Column(Integer, ForeignKey('SkyModel.skyModelId'))
    psfModelId = Column(Integer, ForeignKey('PsfModel.psfModelId'))
    flags = Column(Integer)
    processDate = Column(DateTime)
    DRP2DVersion = Column(String)

    visits = relation(Visit, backref=backref('pfsArm'))
    exposures = relation(Exposure, backref=backref('pfsArm'))
    # calibs = relation(Calib, backref=backref('pfsArm'))
    pfsConfigs = relation(pfsConfig, backref=backref('pfsArm'))
    skyModels = relation(SkyModel, backref=backref('pfsArm'))
    psfModels = relation(PsfModel, backref=backref('pfsArm'))

    def __init__(self, pfsArmId, frameId, visit, spectrograph, arm, armNum,
                 calibFlatId, calibBiasId, calibDarkId, calibArcsId,
                 skyModelId, psfModelId, flags,
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
        self.calibArcsId = calibArcsId
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
    visit = Column(Integer, ForeignKey('Visit.visit'))
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)
    fiberId = Column(Integer, ForeignKey('FiberPosition.fiberId'))
    pfsConfigFiberId = Column(BigInteger, ForeignKey('pfsConfigFiber.pfsConfigFiberId'))
    flags = Column(Integer)
    QATypeId = Column(Integer, ForeignKey('QAType.QATypeId'))
    QAValue = Column(Float(precision=24))

    visits = relation(Visit, backref=backref('pfsArmObj'))
    pfsArms = relation(pfsArm, backref=backref('pfsArmObj'))
    pfsConfigFibers = relation(pfsConfigFiber, backref=backref('psfArmObj'))
    fiberPositions = relation(FiberPosition, backref=backref('pfsArmObj'))
    qaTypes = relation(QAType, backref=backref('pfsArmObj'))

    def __init__(self, pfsArmId, visit, spectrograph, arm, armNum,
                 fiberId, pfsConfigFiberId, flags, QATypeId, QAValue):
        self.pfsArmId = pfsArmId
        self.visit = visit
        self.spectrograph = spectrograph
        self.arm = arm
        self.armNum = armNum
        self.fiberId = fiberId
        self.pfsConfigFiberId = pfsConfigFiberId
        self.flags = flags
        self.QATypeId = QATypeId
        self.QAValue = QAValue


class VisitHash(Base):
    __tablename__ = 'VisitHash'

    pfsVisitHash = Column(BigInteger, primary_key=True, autoincrement=False)
    nVisit = Column(Integer)
#    visit = Column(Integer, ForeignKey('Visit.visit'))
#    visits = relation(Visit, backref=backref('VisitHash'))

    def __init__(self, pfsVisitHash, nVisit):
        self.pfsVisitHash = pfsVisitHash
        self.nVisit = nVisit


class pfsObject(Base):
    __tablename__ = 'pfsObject'

    pfsObjectId = Column(BigInteger, primary_key=True, autoincrement=True)
    targetId = Column(BigInteger, ForeignKey('Target.targetId'))
    tract = Column(Integer)
    patch = Column(String)
    catId = Column(Integer)
    objId = Column(BigInteger)
    nVisit = Column(Integer)
    pfsVisitHash = Column(BigInteger, ForeignKey('VisitHash.pfsVisitHash'))
    cum_texp = Column(Float(precision=24))
    processDate = Column(DateTime)
    DRP2DVersion = Column(String)
    fluxCalibId = Column(Integer, ForeignKey('FluxCalib.fluxCalibId'))
    flags = Column(Integer)
    QATypeId = Column(Integer, ForeignKey('QAType.QATypeId'))
    QAValue = Column(Float(precision=24))

    targets = relation(Target, backref=backref('pfsObject'))
    fluxCalibs = relation(FluxCalib, backref=backref('pfsObject'))
    qaTypes = relation(QAType, backref=backref('pfsObject'))
    visitHashs = relation(VisitHash, backref=backref('pfsObject'))

    def __init__(self, pfsObjectId, targetId, tract, patch, catId, objId, nVisit, pfsVisitHash,
                 cum_texp, processDate, DRP2DVersion, fluxCalibId, flags, QATypeId, QAValue):
        self.pfsObjectId = pfsObjectId
        self.targetId = targetId
        self.tract = tract
        self.patch = patch
        self.catId = catId
        self.objId = objId
        self.nVisit = nVisit
        self.pfsVisitHash = pfsVisitHash
        self.cum_texp = cum_texp
        self.processDate = processDate
        self.DRP2DVesion = DRP2DVesion
        self.fluxCalibId = fluxCalibId
        self.flags = flags
        self.QATypeId = QATypeId
        self.QAValue = QAValue


class VisitsToCombine(Base):
    __tablename__ = 'VisitsToCombine'

    visitsToCombineId = Column(BigInteger, primary_key=True, autoincrement=True)
    targetid = Column(BigInteger, ForeignKey('Target.targetId'))
    visit = Column(Integer, ForeignKey('Visit.visit'))
    pfsVisitHash = Column(BigInteger, ForeignKey('VisitHash.pfsVisitHash'))

    targets = relation(Target, backref=backref('VisitsToCombine'))
    visits = relation(Visit, backref=backref('VisitsToCombine'))
    visitHashs = relation(VisitHash, backref=backref('VisitsToCombine'))

    def __init__(self, targetId, visit, pfsVisitHash):
        self.targetId = targetId
        self.visit = visit
        self.pfsVisitHash = pfsVisitHash


class LineList(Base):
    __tablename__ = 'LineList'

    lineId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    wavelength = Column(Float(precision=24))

    def __init__(self, lineId, name, wavelength):
        self.lineId = lineId
        self.name = name
        self.wavelength = wavelength


class Drp1D(Base):
    __tablename__ = 'Drp1D'

    drp1DId = Column(Integer, primary_key=True, autoincrement=True)
    pfsObjectId = Column(BigInteger, ForeignKey('pfsObject.pfsObjectId'))
    z_best = Column(Float(precision=24))
    z_best_err = Column(Float(precision=24))
    z_best_reliability = Column(Float(precision=24))
    objTypeId = Column(Integer, ForeignKey('ObjType.objTypeId'))
    flags = Column(Integer)
    processDate = Column(DateTime)
    DRP1DVersion = Column(String)

    pfsObjects = relation(pfsObject, backref=backref('Drp1D'))
    objTypes = relation(ObjType, backref=backref('Drp1D'))

    def __init__(self, drp1DId, pfsObjectId, z_best, z_best_err, z_best_reliability,
                 objTypeId, flags, processDate, DRP1DVersion):
        self.drp1DId = drp1DId
        self.pfsObjectId = pfsObjectId
        self.z_best = z_best
        self.z_best_err = z_best_err
        self.z_best_reliability = z_best_reliability
        self.objTypeId = objTypeId
        self.flags = flags
        self.processDate = processDate
        self.DRP1DVersion = DRP1DVersion


class Drp1DRedshift(Base):
    __tablename__ = 'Drp1DRedshift'

    drp1DRedshiftId = Column(BigInteger, primary_key=True, autoincrement=True)
    drp1DId = Column(Integer, ForeignKey('Drp1D.drp1DId'))
    z = Column(Float(precision=24))
    z_err = Column(Float(precision=24))
    zrank = Column(Float(precision=24))
    reliability = Column(Float(precision=24))
    specClass = Column(String)
    specSubclass = Column(String)

    def __init__(self, drp1DRedshiftId, drp1DId, z, z_err, zrank, reliability, specClass, specSubclass):
        self.drp1DRedshiftId = drp1DRedshiftId
        self.drp1DId = drp1DId
        self.z = z
        self.z_err = z_err
        self.zrank = zrank
        self.reliability = reliability
        self.specClass = specClass
        self.specSubclass = specSubclass


class Drp1DLine(Base):
    __tablename__ = 'Drp1DLine'

    drp1DLineId = Column(BigInteger, primary_key=True, autoincrement=True)
    drp1DId = Column(Integer, ForeignKey('Drp1D.drp1DId'))
    lineId = Column(Integer, ForeignKey('LineList.lineId'))
    lineName = Column(String)
    lineWave = Column(Float(precision=24))
    lineZ = Column(Float(precision=24))
    lineZ_err = Column(Float(precision=24))
    lineSigma = Column(Float(precision=24))
    lineSigma_err = Column(Float(precision=24))
    lineVel = Column(Float(precision=24))
    lineVel_err = Column(Float(precision=24))
    lineFlux = Column(Float(precision=24))
    lineFlux_err = Column(Float(precision=24))
    lineEW = Column(Float(precision=24))
    lineEW_err = Column(Float(precision=24))
    lineContLevel = Column(Float(precision=24))
    lineContLevel_err = Column(Float(precision=24))

    lineLists = relation(LineList, backref=backref('specLine'))

    def __init__(self, drp1DLineId, drp1DId, lineId, lineName, lineWave, lineZ, lineZ_err, lineSigma, lineSigma_err, lineVel, lineVel_err, lineFlux, lineFlux_err, lineEW, lineEW_err, lineContLevel, lineContLevel_err):
        self.drp1DLineId = drp1DLineId
        self.drp1DId = drp1DId
        self.lineId = lineId
        self.lineName = lineName
        self.lineWave = lineWave
        self.lineZ = lineZ
        self.lineZ_err = lineZ_err
        self.lineSigma = lineSigma
        self.lineSigma_err = lineSigma_err
        self.lineVel = lineVel
        self.lineVel_err = lineVel_err
        self.lineFlux = lineFlux
        self.lineFlux_err = lineFlux_err
        self.lineEW = lineEW
        self.lineEW_err = lineEW_err
        self.lineContLevel = lineContLevel
        self.lineContLevel_err = lineContLevel_err


class DrpGA(Base):
    __tablename__ = 'DrpGA'

    drpGAId = Column(Integer, primary_key=True, autoincrement=True)
    pfsObjectId = Column(BigInteger, ForeignKey('pfsObject.pfsObjectId'), primary_key=True)
    starTypeId = Column(Integer, ForeignKey('StarType.starTypeId'))
    velocity = Column(Float(precision=24))
    metallicity = Column(Float(precision=24))
    logg = Column(Float(precision=24))
    teff = Column(Float(precision=24))
    flags = Column(Integer)
    processDate = Column(DateTime)
    DRPGAVersion = Column(String)

    pfsObjects = relation(pfsObject, backref=backref('DrpGA'))
    starTypes = relation(StarType, backref=backref('DrpGA'))

    def __init__(self, drpGAId, starTypeId, velocity, metallicity, logg, teff,
                 flags, processDate, pipelneStellarVersion):
        self.drpGAId = drpGAId
        self.starTypeId = startTypeId
        self.velocity = velocity
        self.metallicity = metallicity
        self.logg = logg
        self.teff = teff
        self.flags = flags
        self.processDate = processDate
        self.DRPGAVersion = DRPGAVersion


def make_database(dbinfo):
    '''
    dbinfo is something like this: postgresql://xxxxx:yyyyy@zzz.zzz.zzz.zz/dbname
    '''
    # engine = create_engine('sqlite:///:memory:', echo=True)
    # engine = create_engine('sqlite:///pfs_proto.sqlite', echo=False)
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
