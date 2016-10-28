from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation, backref

Base = declarative_base()

class Program(Base):
    __tablename__ = 'Program'

    programId = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __init__(self, programId, name, description):
        self.programId = programId
        self.name = name
        self.description = description
        
class TargetType(Base):
    __tablename__ = 'TargetType'

    targetType = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __init__(self, targetType, name, description):
        self.targetType = targetType
        self.name = name
        self.description = description
        
class QAType(Base):
    __tablename__ = 'QAType'

    QAType = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    
    def __init__(self, QAType, name, description):
        self.QAType = QAType
        self.name = name
        self.description = description
        
class InputCatalog(Base):
    __tablename__ = "InputCatalog"

    catId = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __init__(self, catId, name, description):
        self.catId = catId
        self.name = name
        self.description = description
        
class Target(Base):
    __tablename__ = 'Target'

    targetId = Column(Integer, primary_key=True)
    programId = Column(Integer, ForeignKey('Program.programId'))
    objId = Column(Integer)
    ra = Column(Float)
    dec = Column(Float)
    tract = Column(Integer)
    patch = Column(String)
    priority = Column(Float)
    targetTypeId = Column(Integer, ForeignKey('TargetType.targetType'))
    catId = Column(Integer, ForeignKey('InputCatalog.catId'))
    catObjId = Column(Integer)
    fiberMag_g = Column(Float)
    fiberMag_r = Column(Float)
    fiberMag_i = Column(Float)
    fiberMag_z = Column(Float)
    fiberMag_Y = Column(Float)
    fiberMag_J = Column(Float)
    fiducialExptime = Column(Float)
    QATypeId = Column(Integer, ForeignKey('QAType.QAType'))
    QALambdaMin = Column(Float)
    QALambdaMax = Column(Float)
    QAThreshold = Column(Float)
    QALineFlux  = Column(Float)
    finished = Column(Boolean)

    program = relation(Program, backref=backref('targets'))
    targetType = relation(TargetType, backref=backref('targets'))
    inputCatalog = relation(InputCatalog, backref=backref('targets'))
    qaType = relation(QAType, backref=backref('targets'))

    def calculateId(self, programId, objId):
        return (programId << 20) + objId
    
    def __init__(self, programId, objId,
                 ra, dec, tract, patch, priority, targetType, catId, catObjId,
                 fiberMag_g, fiberMag_r, fiberMag_i, fiberMag_z, fiberMag_Y,
                 fiberMag_J, fiducialExptime,
                 QAType, QALambdaMin, QALambdaMax, QAThreshold, QALineFlux,
                 finished = False):
        self.targetId = self.calculateId(programId, objId)
        self.programId = programId
        self.objId = objId
        self.ra = ra
        self.dec = dec
        self.tract = tract
        self.patch = patch
        self.priority = priority
        self.targetTypeId = targetType
        self.catId = catId
        self.catObjId = catObjId
        self.fiberMag_g = fiberMag_g
        self.fiberMag_r = fiberMag_r
        self.fiberMag_i = fiberMag_i
        self.fiberMag_z = fiberMag_z
        self.fiberMag_Y = fiberMag_Y
        self.fiberMag_J = fiberMag_Y
        self.fiducialExptime = fiducialExptime
        self.QATypeId = QAType
        self.QALambdaMin = QALambdaMin
        self.QALambdaMax = QALambdaMax
        self.QAThreshold = QAThreshold
        self.QALineFlux = QALineFlux
        self.finished = finished
        
class Tile(Base):
    __tablename__ = 'Tile'

    tileId = Column(Integer, primary_key=True)
    programId = Column(Integer, ForeignKey('Program.programId'))
    tile = Column(Integer)
    ra_center = Column(Float)
    dec_center = Column(Float)
    pa = Column(Float)

    program = relation(Program, backref=backref('tiles'))

    def calculateId(self, programId, tile):
        return (programId << 10) + tile
    
    def __init__(self, programId, tile, ra_center, dec_center, pa):
        self.tileId = self.calculateId(programId, tile)
        self.programId = programId
        self.tile = tile
        self.ra_center = ra_center
        self.dec_center = dec_center
        self.pa = pa
        
class pfsConfig(Base):
    __tablename__ = 'pfsConfig'

    pfsConfigId = Column(Integer, primary_key=True)
    tileId = Column(Integer, ForeignKey('Tile.tileId'))
    num_target = Column(Integer)
    num_allocated = Column(Integer)
    exptime = Column(Float)
    nVisit = Column(Integer)
    obsolete = Column(Boolean)
    observed = Column(Boolean)
        
    tile = relation(Tile, backref=backref('pfsConfigs'))

    def __init__(self, pfsConfigId, tileId, num_target, num_allocated, exptime,
                 nVisit, obsolete=False, observed=False):
        self.pfsConfigId = pfsConfigId
        self.tileId = tileId
        self.num_target = num_target
        self.num_allocated = num_allocated
        self.exptime = exptime
        self.nVisit = nVisit
        self.obsolete = obsolete
        self.observed = observed

class pfsConfigFiber(Base):
    __tablename__ = 'pfsConfigFiber'
    
    pfsConfigFiberId = Column(Integer, primary_key=True)
    pfsConfigId = Column(Integer, ForeignKey('pfsConfig.pfsConfigId'))
    fiberId = Column(Integer)
    targetId = Column(Integer, ForeignKey('Target.targetId'))
    MCS_Centroid_x_Plan = Column(Float)
    MCS_Centroid_y_Plan = Column(Float)
    onSource = Column(Boolean)

    pfsConfig = relation(pfsConfig, backref=backref('psfConfigFibers'))
    target = relation(Target, backref=backref('psfConfigFibers'))
    
    def __init__(self, pfsConfigFiberId, pfsConfigId, fiberId, targetId,
                 MCS_Centroid_x_Plan, MCS_Centroid_y_Plan, onSource=True):
        self.pfsConfigFiberId = pfsConfigFiberId
        self.pfsConfigId = pfsConfigId
        self.fiberId = fiberId
        self.targetId = targetId
        self.MCS_Centroid_x_Plan = MCS_Centroid_x_Plan
        self.MCS_Centroid_y_Plan = MCS_Centroid_y_Plan
        self.onSource = onSource
        
class Calib(Base):
    __tablename__ = 'Calib'

    calib_id = Column(Integer, primary_key=True)
    type = Column(String)
    calibDate = Column(DateTime)
    spectrograph = Column(Integer)
    arm = Column(String)
    exptime = Column(Float)
    visitStart = Column(Integer)
    visitEnd = Column(Integer)

    def __init__(self, calib_id, type, calibDate, spectrogarph, arm,
                 exptime, visitStart, visitEnd):
        self.calib_id = calib_id
        self.type = type
        self.calibDate = calibDate
        self.spectrograph = spectrograph
        self.arm = arm
        self.exptime = exptime
        self.visitStart = visitStart
        self.visitEnd = visitEnd

class BeamSwitchMode(Base):
    __tablename__ = 'BeamSwitchMode'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        
class Exposure(Base):
    __tablename__ = 'Exposure'

    frameId = Column(String, primary_key=True)
    visit = Column(Integer)
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)
    pfsConfigId = Column(Integer, ForeignKey('pfsConfig.pfsConfigId'))
    ra_tel = Column(Float)
    dec_tel = Column(Float)
    timeObs = Column(DateTime)
    mjd = Column(Float)
    exptime = Column(Float)
    seeing = Column(Float)
    transp = Column(Float)
    alloc_num_iter = Column(Integer)
    alloc_elapsetime = Column(Float)
    alloc_rms_scatter = Column(Float)
    alloc_exectime = Column(DateTime)
    beamSwitchMode = Column(Integer, ForeignKey('BeamSwitchMode.id'))
    beamSwitchOffsetRA = Column(Float)
    beamSwitchOffsetDec = Column(Float)

    pfsConfig = relation(pfsConfig, backref=backref('exposure'))
    bsMode = relation(BeamSwitchMode, backref=backref('exposures'))

    def __init__(self, frameId, visit, spectrograph, arm, armNum,
                 pfsConfigId, ra_tel, dec_tel, timeObs, mjd, exptime,
                 seeing, transp,
                 alloc_num_iter, alloc_elapsetime,
                 alloc_rms_scatter, alloc_exectime,
                 beamSwitchMode=0, beamSwitchOffsetRA=0.0, beamSwitchOffsetDec=0.0):
        self.frameId = frameId
        self.visit = visit
        self.sepctrograph = spectrograph
        self.arm = arm
        self.armNum = armNum
        self.pfsConfigId = pfsConfigId,
        self.ra_tel = ra_tel
        self.dec_tel = dec_tel
        self.timeObs = timeObs
        self.mjd = mjd
        self.exptime = exptime
        self.seeing = seeing
        self.transp = transp
        self.alloc_num_iter = alloc_num_iter
        self.alloc_elapsetime = alloc_elapsetime
        self.alloc_rms_scatter = alloc_rms_scatter
        self.alloc_exectime = alloc_exectime
        self.beamSwitchMode = beamSwithMode
        self.beamSwitchOffsetRA = beamSwitchOffsetRA
        self.beamSwitchOffsetDec = beamSwitchOffsetDec
                 
class ObsFiber(Base):
    __tablename__ = 'ObsFiber'
    
    obsFiberId = Column(Integer, primary_key=True)
    frameId = Column(String, ForeignKey('Exposure.frameId'))
    fiberId = Column(Integer)
    pfsConfigFiberId = Column(Integer, ForeignKey('pfsConfigFiber.pfsConfigFiberId'))
    MCS_Centroid_x_Real = Column(Float)
    MCS_Centroid_y_Real = Column(Float)

    exposure = relation(Exposure, backref=backref('obsFibers'))
    pfsConfigFiber = relation(pfsConfigFiber, backref=backref('obsFiber'))

    def __init__(self, obsFiberId, frameId, fiberId, pfsConfigFiberId,
                 MCS_Centroid_x_Real, MCS_Centroid_y_Real):
        self.obsFiberId = obsFiberId
        self.frameId = frameId
        self.fiberId = fiberId
        self.pfsConfigFiberId = pfsConfigFiberId
        self.MCS_Centroid_x_Real = MCS_Centroid_x_Real
        self.MCS_Centroid_y_Real = MCS_Centroid_y_Real
        
class FiberPosition(Base):
    __tablename__ = 'FiberPosition'

    spectrograph = Column(Integer, primary_key=True)
    arm = Column(String, primary_key=True)
    armNum = Column(Integer, primary_key=True)
    fiberId = Column(Integer, primary_key=True)
    xCenter = Column(Float)
    yCenter = Column(Float)

    def __init__(self, spectrograph, arm, armNum, fiberId, xCenter, yCenter):
        self.spectrograph = spectrograph
        self.arm = arm
        self.armNum = armNum
        self.fiberId = fiberId
        self.xCenter = xCenter
        self.yCenter = yCenter
        
class pfsArm(Base):
    __tablename__ = 'pfsArm'

    frameId = Column(String, ForeignKey('Exposure.frameId'), primary_key=True)
    visit = Column(Integer)
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)
    skyModel = Column(String)
    psfModel = Column(String)
    flags = Column(Integer)
    processDate = Column(DateTime)
    pipeline2DVersion = Column(String)

    exposure = relation(Exposure, backref=backref('pfsArm'))

    def __init__(self, frameId, visit, spectrograph, arm, armNum,
                 skyModel, psfModel, flags, processDate, pipeline2DVersion):
        self.frameId = frameId
        self.visit = visit
        self.spectrograph = spectrograph
        self.arm = arm
        self.armNum = armNum
        self.skyModel = skyModel
        self.psfModel = psfModel
        self.flags = flags
        self.processDate = processDate
        self.pipeline2DVersion = pipeline2DVersion
        
class pfsArmObj(Base):
    __tablename__ = 'pfsArmObj'

    frameId = Column(String, ForeignKey('pfsArm.frameId'), primary_key=True)
    visit = Column(Integer)
    spectrograph = Column(Integer)
    arm = Column(String)
    armNum = Column(Integer)
    pfsConfigFiberId = Column(Integer, ForeignKey('pfsConfigFiber.pfsConfigFiberId'))
    flags = Column(Integer)
    QAValue = Column(Float)

    pfsArm = relation(pfsArm, backref=backref('pfsArmObjs'))
    pfsConfigFiber = relation(pfsConfigFiber, backref=backref('psfArmObj'))

class pfsObject(Base):
    __tablename__ = 'pfsObject'

    pfsObjectId = Column(Integer, primary_key=True)
    targetId = Column(Integer, ForeignKey('Target.targetId'))
    nVisit = Column(Integer)
    pfsVisitHash = Column(Integer)
    processDate = Column(DateTime)
    pipeline2DVersion = Column(String)
    flags = Column(Integer)
    QAValue = Column(Float)

    target = relation(Target, backref=backref('pfsObjects'))

    def __init__(self, pfsObjectId, targetId, nVisit, pfsVisitHash,
                 processDate, pipeline2DVersion, flags, QAValue):
        self.pfsObjectId = pfsObjectId
        self.targetId = targetId
        self.nVisit = nVisit
        self.pfsVisitHash = psfVisitHash
        self.processDate = processDate
        self.pipeline2DVesion = pipeline2DVesion
        self.flags = flags
        self.QAValue = QAValue
        
class VisitsToCombine(Base):
    __tablename__ = 'VisitsToCombine'

    id = Column(Integer, primary_key=True)
    #targetId = Column(Integer, ForeignKey('Target.targetId'))
    #frameId = Column(String, ForeignKey('pfsArmObj.frameId'))
    targetId = Column(Integer)
    frameId = Column(String)
    visit = Column(Integer)
    #pfsVisitHash = Column(Integer, ForeignKey('pfsObject.pfsVisitHash'))
    pfsVisitHash = Column(Integer)

    #target = relation(Target, backref=backref('visitsToCombine'))
    #pfsArmObj = relation(pfsArmObj, backref=backref('visitsToCombine'))
    #pfsObject = relation(pfsObject, backref=backref('visitsToCombine'))

    def __init__(self, targetId, frameId, visit, pfsVisitHash):
        self.targetId = targetId
        self.frameId = frameId
        self.visit = visit
        self.pfsVisitHash = pfsVisitHash
        
class ObjType(Base):
    __tablename__ = 'ObjType'

    objTypeId = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __init__(self, objTypeId, name, description):
        self.objTypeId = objTypeId
        self.name = name
        self.description = description
        
class StarType(Base):
    __tablename__ = 'StarType'

    starTypeId = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    
    def __init__(self, starTypeId, name, description):
        self.starTypeId = starTypeId
        self.name = name
        self.description = description
        
class SpecParam(Base):
    __tablename__ = 'SpecParam'

    pfsObjectId = Column(Integer, ForeignKey('pfsObject.pfsObjectId'), primary_key=True)
    redshift = Column(Float)
    z_mean = Column(Float)
    z_median = Column(Float)
    z_percentileXX = Column(Float)
    objTypeId = Column(Integer, ForeignKey('ObjType.objTypeId'))
    flags = Column(Integer)
    processDate = Column(DateTime)
    pipeline1DVersion = Column(String)

    pfsObject = relation(pfsObject, backref=backref('specParam'))
    objType = relation(ObjType, backref=backref('specParams'))

    def __init__(self, pfsObjectId, redshift, z_mean, z_median, z_percentileXX,
                 objTypeId, flags, processDate, pipeline1DVersion):
        self.pfsObjectId = pfsObjectId
        self.redshift = redshift
        self.z_mean = z_mean
        self.z_median = z_median
        self.z_percentileXX = z_percentileXX
        self.objTypeId = objTypeId
        self.flags = flags
        self.processDate = processDate
        self.pipeline1DVersion = pipeline1DVersion
        
class StarSpecParam(Base):
    __tablename__ = 'StarSpecParam'

    pfsObejctId = Column(Integer, ForeignKey('pfsObject.pfsObjectId'), primary_key=True)
    starTypeId = Column(Integer, ForeignKey('StarType.starTypeId'))
    velocity = Column(Float)
    metallicity = Column(Float)
    logg = Column(Float)
    teff = Column(Float)
    flags = Column(Integer)
    processDate = Column(DateTime)
    pipelineStellarVersion = Column(String)

    pfsObject = relation(pfsObject, backref=backref('starSpecParam'))
    starType = relation(StarType, backref=backref('starSpecParams'))

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
        self.pipelineStellarVersion = pipelineStellarVersion
        
class LineList(Base):
    __tablename__ = 'LineList'

    lineId = Column(Integer, primary_key=True)
    name = Column(String)
    wavelength = Column(Float)

    def __init__(self, lineId, name, wavelength):
        self.lineId = lineId
        self.name = name
        self.wavelength = wavelength
        
class SpecLine(Base):
    __tablename__ = 'SpecLine'

    id = Column(Integer, primary_key=True)
    pfsObjectId = Column(Integer, ForeignKey('pfsObject.pfsObjectId'))
    lineId = Column(Integer, ForeignKey('LineList.lineId'))
    wavelength = Column(Float)
    z = Column(Float)
    sigma = Column(Float)
    area = Column(Float)
    ew = Column(Float)
    contlevel = Column(Float)
    chi2 = Column(Float)

    pfsObject = relation(pfsObject, backref=backref('specLines'))
    lineList = relation(LineList, backref=backref('specLine'))

    def __init__(self, pfsObjectId, lineId, wavelength, z, sigma, ew, contlevel, chi2):
        self.pfsObjectId = pfsObjectId
        self.lineId = lineId
        self.wavelength = wavelength
        self.z = z
        self.sigma = sigma
        self.ew = ew
        self.contlevel = contlevel
        self.chi2 = chi2
        
if __name__ == '__main__':

    #engine = create_engine('sqlite:///:memory:', echo=True)
    #engine = create_engine('sqlite:///pfs_proto.sqlite', echo=False)
    engine = create_engine('postgresql://pfsdbadmin:xxxxx@192.168.156.76/pfsdbsim')
    
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
