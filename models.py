from sqlalchemy import create_engine
from sqlalchemy import Column, BigInteger, Integer, String, FLOAT, ForeignKey, DateTime, Boolean, REAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation, backref
from sqlalchemy import UniqueConstraint, ForeignKeyConstraint

Base = declarative_base()


class proposal(Base):
    __tablename__ = 'proposal'

    proposal_id = Column(String, primary_key=True, unique=True, autoincrement=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, proposal_id, created_at, updated_at):
        self.proposal_id = proposal_id
        self.created_at = created_at
        self.updated_at = updated_at


class program(Base):
    __tablename__ = 'program'

    program_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    program_name = Column(String)
    program_description = Column(String)
    proposal_id = Column(String, ForeignKey('proposal.proposal_id'))
    is_filler = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    proposals = relation(proposal, backref=backref('program'))

    def __init__(self, program_id, program_name, program_description, proposal_id,
                 is_filler, created_at, updated_at):
        self.program_id = program_id
        self.program_name = program_name
        self.program_description = program_description
        self.proposal_id = proposal_id
        self.is_filler = is_filler
        self.created_at = created_at
        self.updated_at = updated_at


class target_type(Base):
    __tablename__ = 'target_type'

    target_type_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    target_type_name = Column(String)
    target_type_description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, target_type_id, target_type_name, target_type_description, created_at, updated_at):
        self.target_type_id = target_type_id
        self.target_type_name = target_type_name
        self.target_type_description = target_type_description
        self.created_at = created_at
        self.updated_at = updated_at


class obj_type(Base):
    __tablename__ = 'obj_type'

    obj_type_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    obj_type_name = Column(String)
    obj_type_description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, obj_type_id, obj_type_name, obj_type_description, created_at, updated_at):
        self.obj_type_Id = obj_type_id
        self.obj_type_name = obj_type_name
        self.obj_type_description = obj_type_description
        self.created_at = created_at
        self.updated_at = updated_at


class star_type(Base):
    __tablename__ = 'star_type'

    star_type_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    star_type_name = Column(String)
    star_type_description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, star_type_id, star_type_name, star_type_description, created_at, updated_at):
        self.star_type_id = star_type_id
        self.star_type_name = star_type_name
        self.star_type_description = star_type_description
        self.created_at = created_at
        self.updated_at = updated_at


class qa_type(Base):
    __tablename__ = 'qa_type'

    qa_type_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    qa_type_name = Column(String)
    qa_type_description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, qa_type_id, qa_type_name, qa_type_description, created_at, updated_at):
        self.qa_type_id = qa_type_id
        self.qa_type_name = qa_type_name
        self.qa_type_description = qa_type_description
        self.created_at = created_at
        self.updated_at = updated_at


class input_catalog(Base):
    __tablename__ = "input_catalog"

    cat_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    input_catalog_name = Column(String)
    input_catalog_description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, cat_id, input_catalog_name, input_catalog_description,
                 created_at, updated_at):
        self.cat_id = cat_id
        self.input_catalog_name = input_catalog_name
        self.input_catalog_description = input_catalog_description
        self.created_at = created_at
        self.updated_at = updated_at


class cloud_condition(Base):
    __tablename__ = 'cloud_condition'

    cloud_condition_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    cloud_condition_name = Column(String)
    cloud_condition_description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, cloud_condition_id, cloud_condition_name, cloud_condition_description,
                 created_at, updated_at):
        self.cloud_condition_id = cloud_condition_id
        self.cloud_condition_name = cloud_condition_name
        self.cloud_condition_description = cloud_condition_description
        self.created_at = created_at
        self.updated_at = updated_at


class fiber_position(Base):
    __tablename__ = 'fiber_position'
    fiber_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    ftype = Column(String)
    x = Column(REAL)
    y = Column(REAL)

    def __init__(self, fiber_id, ftype, x, y):
        self.fiber_id = fiber_id
        self.ftype = ftype
        self.x = x
        self.y = y


class cobra_position(Base):
    __tablename__ = 'cobra_position'
    cobra_id = Column(Integer, primary_key=True, autoincrement=False)
    fiber_id = Column(Integer, ForeignKey('fiber_position.fiber_id'))
    fld = Column(Integer)
    cf = Column(Integer)
    mf = Column(Integer)
    cm = Column(Integer)
    mod = Column(String)
    x = Column(REAL)
    y = Column(REAL)
    r = Column(REAL)
    sp = Column(Integer)
    fh = Column(Integer)
    sfib = Column(Integer)
    fiber_id_lna = Column(String)
    version = Column(String, primary_key=True, autoincrement=False)

    fiber_positions = relation(fiber_position, backref=backref('cobra_position'))

    def __init__(self, cobra_id, fiber_id, fld, cf, mf, cm, mod, x, y, r, sp, fh, sfib, fiber_id_lna, version):
        self.cobra_id = cobra_id
        self.fiber_id = fiber_id
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
        self.fiber_id_lna = fiber_id_lna
        self.version = version


class fiducial_fiber_position(Base):
    __tablename__ = 'fiducial_fiber_position'
    ff_id = Column(Integer, primary_key=True, autoincrement=False)
    fiber_id = Column(Integer, ForeignKey('fiber_position.fiber_id'))
    ff = Column(Integer)
    fff = Column(Integer)
    fftype = Column(String)
    fft = Column(Integer)
    x = Column(REAL)
    y = Column(REAL)
    version = Column(String, primary_key=True, autoincrement=False)

    fiber_positions = relation(fiber_position, backref=backref('fiducial_fiber_position'))

    def __init__(self, ff_id, fiber_id, ff, fff, fftype, fft, x, y, version):
        self.ff_id = ff_id
        self.fiber_id = fiber_id
        self.ff = ff
        self.fff = fff
        self.fftype = fftype
        self.fft = fft
        self.x = x
        self.y = y
        self.version = version


class spectrograph(Base):
    __tablename__ = 'spectrograph'

    spectrograph_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    spectrograph_module = Column(Integer)
    arm = Column(String(1))
    arm_num = Column(Integer)

    def __init__(self, spectrograph_id, spectrograph_module, arm, arm_num):
        self.spectrograph_id = spectrograph_id
        self.spectrograph_module = spectrograph_module
        self.arm = arm
        self.arm_num = arm_num


class target(Base):
    __tablename__ = 'target'

    target_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    program_id = Column(Integer, ForeignKey('program.program_id'))
    obj_id = Column(BigInteger)
    ra = Column(FLOAT)
    dec = Column(FLOAT)
    tract = Column(Integer)
    patch = Column(String)
    priority = Column(REAL)
    target_type_id = Column(Integer, ForeignKey('target_type.target_type_id'))
    cat_id = Column(Integer, ForeignKey('input_catalog.cat_id'))
    cat_obj_id = Column(BigInteger)
    fiber_mag_g = Column(REAL)
    fiber_mag_r = Column(REAL)
    fiber_mag_i = Column(REAL)
    fiber_mag_z = Column(REAL)
    fiber_mag_y = Column(REAL)
    fiber_mag_j = Column(REAL)
    fiducial_exptime = Column(REAL)
    photz = Column(REAL)
    is_medium_resolution = Column(Boolean)
    qa_type_id = Column(Integer, ForeignKey('qa_type.qa_type_id'))
    qa_lambda_min = Column(REAL)
    qa_lambda_max = Column(REAL)
    qa_threshold = Column(REAL)
    qa_line_flux = Column(REAL)
    completeness = Column(REAL)
    is_finished = Column(Boolean)

    programs = relation(program, backref=backref('target'))
    target_types = relation(target_type, backref=backref('target'))
    input_catalogs = relation(input_catalog, backref=backref('target'))
    qa_types = relation(qa_type, backref=backref('target'))

    def __init__(self, program_id, obj_id, ra, dec, tract, patch, priority, target_type_id, cat_id, cat_obj_id,
                 fiber_mag_g, fiber_mag_r, fiber_mag_i, fiber_mag_z, fiber_mag_y,
                 fiber_mag_j, fiducial_exptime, photz, is_medium_resolution,
                 qa_type_id, qa_lambda_min, qa_lambda_max, qa_threshold, qa_line_flux,
                 completeness=0.0, is_finished=False):
        self.program_id = program_id
        self.obj_id = obj_id
        self.ra = ra
        self.dec = dec
        self.tract = tract
        self.patch = patch
        self.priority = priority
        self.target_type_id = target_type_id
        self.cat_id = cat_id
        self.cat_obj_id = cat_obj_id
        self.fiber_mag_g = fiber_mag_g
        self.fiber_mag_r = fiber_mag_r
        self.fiber_mag_i = fiber_mag_i
        self.fiber_mag_z = fiber_mag_z
        self.fiber_mag_y = fiber_mag_y
        self.fiber_mag_j = fiber_mag_j
        self.fiducial_exptime = fiducial_exptime
        self.photz = photz
        self.is_medium_resolution = is_medium_resolution
        self.qa_type_id = qa_type_id
        self.qa_lambda_min = qa_lambda_min
        self.qa_lambda_max = qa_lambda_max
        self.qa_threshold = qa_threshold
        self.qa_line_flux = qa_line_flux
        self.completeness = completeness
        self.is_finished = is_finished


class guide_stars(Base):
    __tablename__ = 'guide_stars'
    guide_star_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    ra = Column(FLOAT)
    dec = Column(FLOAT)
    cat_id = Column(Integer, ForeignKey('input_catalog.cat_id'))
    obj_type_id = Column(Integer, ForeignKey('obj_type.obj_type_id'))
    mag_agc = Column(REAL)
    flux_agc = Column(REAL)
    flags = Column(Integer)

    input_catalogs = relation(input_catalog, backref=backref('guide_stars'))
    obj_types = relation(obj_type, backref=backref('guide_stars'))

    def __init__(self, guide_star_id, ra, dec, cat_id, mag_agc, flux_agc, flags):
        self.guide_star_id = guide_star_id
        self.ra = ra
        self.dec = dec
        self.cat_id = cat_id
        self.mag_agc = mag_agc
        self.flux_agc = flux_agc
        self.flags = flags


class tile(Base):
    __tablename__ = 'tile'

    tile_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    program_id = Column(Integer, ForeignKey('program.program_id'))
    tile = Column(Integer)
    ra_center = Column(FLOAT)
    dec_center = Column(FLOAT)
    pa = Column(REAL)
    is_finished = Column(Boolean)

    programs = relation(program, backref=backref('tile'))

    def __init__(self, program_id, tile, ra_center, dec_center, pa, is_finished):
        self.program_id = program_id
        self.tile = tile
        self.ra_center = ra_center
        self.dec_center = dec_center
        self.pa = pa
        self.is_finished = is_finished


class pfs_design(Base):
    __tablename__ = 'pfs_design'

    pfs_design_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    tile_id = Column(Integer, ForeignKey('tile.tile_id'))
    ra_center_designed = Column(FLOAT)
    dec_center_designed = Column(FLOAT)
    pa_designed = Column(REAL)
    num_sci_designed = Column(Integer)
    num_cal_designed = Column(Integer)
    num_sky_designed = Column(Integer)
    num_guide_stars = Column(Integer)
    exptime = Column(REAL)
    min_exptime = Column(REAL)
    ets_version = Column(String)
    ets_assigner = Column(String)
    ets_exectime = Column(DateTime)
    is_obsolete = Column(Boolean)

    tiles = relation(tile, backref=backref('pfs_design'))

    def __init__(self, pfs_design_id, tile_id, ra_center_designed, dec_center_designed, pa_designed,
                 num_sci_designed, num_cal_designed, num_sky_designed, num_guide_stars,
                 exptime, min_exptime, ets_version, ets_assgner, ets_exectime, is_obsolete=False):
        self.pfs_design_id = pfs_design_id
        self.tile_id = tile_id
        self.ra_center_designed = ra_center_designed
        self.dec_center_designed = dec_center_designed
        self.pa_designed = pa_designed
        self.num_sci_designed = num_sci_designed
        self.num_cal_designed = num_cal_designed
        self.num_sky_designed = num_sky_designed
        self.num_guide_stars = num_guide_stars
        self.exptime = exptime
        self.min_exptime = min_exptime
        self.ets_version = ets_version
        self.ets_assigner = ets_assigner
        self.ets_exectime = ets_exectime
        self.is_obsolete = is_obsolete


class pfs_design_fiber(Base):
    __tablename__ = 'pfs_design_fiber'
    __table_args__ = (UniqueConstraint('pfs_design_id', 'fiber_id'), {})

    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'), primary_key=True, autoincrement=False)
    fiber_id = Column(Integer, ForeignKey('fiber_position.fiber_id'), primary_key=True, autoincrement=False)
    target_id = Column(BigInteger, ForeignKey('target.target_id'))
    ets_priority = Column(Integer)
    ets_cost_function = Column(String)
    ets_cobra_movement = Column(String)
    pfi_nominal_x_mm = Column(REAL)
    pfi_nominal_y_mm = Column(REAL)
    is_on_source = Column(Boolean)

    pfs_designs = relation(pfs_design, backref=backref('psf_design_fiber'))
    targets = relation(target, backref=backref('psf_design_fiber'))
    fiber_positions = relation(fiber_position, backref=backref('psf_design_fiber'))

    def __init__(self, pfs_design_id, fiber_id, target_id,
                 ets_priority, ets_cost_function, ets_cobra_movement,
                 pfi_nominal_x_mm, pfi_nominal_y_mm,
                 is_on_source=True):
        self.pfs_design_id = pfs_design_id
        self.fiber_id = fiber_id
        self.target_id = target_id
        self.ets_priority = ets_priority
        self.ets_cost_function = ets_cost_function
        self.ets_cobra_movement = ets_cobra_movement
        self.pfi_nominal_x_mm = pfi_nominal_x_mm
        self.pfi_nominal_y_mm = pfi_nominal_y_mm
        self.is_on_source = is_on_source


class pfi_visit(Base):
    __tablename__ = 'pfi_visit'

    pfi_visit_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    pfi_visit_type = Column(Integer)
    pfi_visit_description = Column(String)

    def __init__(self, pfi_visit_id, pfi_visit_type, pfi_visit_description):
        self.pfi_visit_id = pfi_visit_id
        self.pfi_visit_type = pfi_visit_type
        self.pfi_visit_description = pfi_visit_description


class mcs_boresight(Base):

    __tablename__ = 'mcs_boresight'

    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'), primary_key=True, unique=True, autoincrement=False)
    datatime = Column(DateTime)
    mcs_boresight_x_pix = Column(REAL)
    mcs_boresight_y_pix = Column(REAL)

    def __init__(self, pfi_visit_id, datatime, mcs_boresight_x_pix, mcs_boresight_y_pix):
        self.pfi_visit_id = pfi_visit_id
        self.datatime = datatime
        self.mcs_boresight_x_pix = mcs_boresight_x_pix
        self.mcs_boresight_y_pix = mcs_boresight_y_pix


class mcs_exposure(Base):

    __tablename__ = 'mcs_exposure'

    frame_id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=False)
    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'))
    starttime = Column(DateTime)
    mcs_exptime = Column(REAL)
    altitude = Column(REAL)
    azimuth = Column(REAL)
    insrot = Column(REAL)

    def __init__(self, frame_id, pfi_visit_id, starttime, mcs_exptime, altitude, azimuth, insrot):
        self.frame_id = frame_id
        self.pfi_visit_id = pfi_visit_id
        self.starttime = starttime
        self.mcs_exptime = mcs_exptime
        self.altitude = altitude
        self.azimuth = azimuth
        self.insrot = insrot


class mcs_data(Base):

    __tablename__ = 'mcs_data'
    __table_args__ = (UniqueConstraint('frame_id', 'fiber_id'), {})

    frame_id = Column(Integer, ForeignKey('mcs_exposure.frame_id'), primary_key=True, index=True, autoincrement=False)
    fiber_id = Column(Integer, ForeignKey('fiber_position.fiber_id'), primary_key=True, autoincrement=False)
    move_id = Column(Integer)
    mcs_center_x_pix = Column(REAL)
    mcs_center_y_pix = Column(REAL)
    mcs_fwhm_x_pix = Column(REAL)
    mcs_fwhm_y_pix = Column(REAL)
    bgvalue = Column(REAL)
    peakvalue = Column(REAL)
    datatime = Column(DateTime)

    def __init__(self, frame_id, fiber_id, move_id, mcs_center_x_pix, mcs_center_y_pix,
                 mcs_fwhm_x_pix, fmcs_whm_y_pix, bgvalue, peakvalue, datatime):
        self.frame_id = frame_id
        self.fiber_id = fiber_id
        self.move_id = move_id
        self.mcs_center_x_pix = mcs_center_x_pix
        self.mcs_center_y_pix = mcs_center_y_pix
        self.mcs_fwhm_x_pix = mcs_fwhm_x_pix
        self.mcs_fwhm_y_pix = mcs_fwhm_y_pix
        self.bgvalue = bgvalue
        self.peakvalue = peakvalue
        self.datatime = datatime


class pfs_config(Base):
    __tablename__ = 'pfs_config'

    pfs_config_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'))
    visit0 = Column(Integer)
    ra_center_config = Column(FLOAT)
    dec_center_config = Column(FLOAT)
    pa_config = Column(REAL)
    num_sci_allocated = Column(Integer)
    num_cal_allocated = Column(Integer)
    num_sky_allocated = Column(Integer)
    num_guide_stars = Column(Integer)
    exptime = Column(REAL)
    min_exptime = Column(REAL)
    alloc_num_ter = Column(Integer)
    alloc_elapsetime = Column(REAL)
    alloc_rms_scatter = Column(REAL)
    alloc_exectime = Column(DateTime)
    is_observed = Column(Boolean)

    pfs_designs = relation(pfs_design, backref=backref('pfs_config'))

    def __init__(self, pfs_config_id, pfs_design_id, visit0, ra_center_config, dec_center_config, pa_config,
                 num_sci_allocated, num_cal_allocated, num_sky_allocated, num_guide_stars,
                 exptime, min_exptime, alloc_num_iter, alloc_elapsetime, alloc_rms_scatter, alloc_exectime,
                 is_observed=False):
        self.pfs_config_id = pfs_config_id
        self.pfs_design_id = pfs_design_id
        self.visit0 = visit0
        self.ra_center_config = ra_center_config
        self.dec_center_config = dec_center_config
        self.pa_config = pa_config
        self.num_sci_allocated = num_sci_allocated
        self.num_cal_allocated = num_cal_allocated
        self.num_sky_allocated = num_sky_allocated
        self.num_guide_stars = num_guide_stars
        self.exptime = exptime
        self.min_exptime = min_exptime
        self.alloc_num_iter = alloc_num_iter
        self.alloc_elapsetime = alloc_elapsetime
        self.alloc_rms_scatter = alloc_rms_scatter
        self.alloc_exectime = alloc_exectime
        self.is_observed = is_observed


class pfs_config_fiber(Base):
    __tablename__ = 'pfs_config_fiber'
    __table_args__ = (UniqueConstraint('pfs_config_id', 'fiber_id'),
                      {})

    pfs_config_id = Column(BigInteger, ForeignKey('pfs_config.pfs_config_id'), primary_key=True, autoincrement=False)
    fiber_id = Column(Integer, ForeignKey('fiber_position.fiber_id'), primary_key=True, autoincrement=False)
    target_id = Column(BigInteger, ForeignKey('target.target_id'))
    motor_map_summary = Column(String)
    config_time = Column(REAL)
    is_on_source = Column(Boolean)

    pfs_configs = relation(pfs_config, backref=backref('psf_config_fiber'))
    targets = relation(target, backref=backref('psf_config_fiber'))
    fiber_positions = relation(fiber_position, backref=backref('psf_config_fiber'))

    def __init__(self, pfs_config_id, fiber_id, target_id,
                 motor_map_summary, config_time,
                 is_on_source=True):
        self.pfs_config_id = pfs_config_id
        self.fiber_id = fiber_id
        self.target_id = target_id
        self.motor_map_summary = motor_map_summary
        self.config_time = config_time
        self.is_on_source = is_on_source


class cobra_motor_map(Base):
    __tablename__ = 'cobra_motor_map'

    cobra_motor_map_id = Column(Integer, primary_key=True, autoincrement=True)
    fiber_id = Column(Integer)
    calib_date = Column(DateTime)
    info1 = Column(REAL)
    info2 = Column(REAL)

    def __init__(self, cobra_motor_map_id,
                 fiber_id, calib_date, info1, info2
                 ):
        self.cobra_motor_map_id = cobra_motor_map_id
        self.fiber_id = fiber_id
        self.calib_date = calib_date
        self.info1 = info1
        self.info2 = info2


class cobra_movement(Base):
    __tablename__ = 'cobra_movement'
    __table_args__ = (UniqueConstraint('frame_id', 'fiber_id'),
                      ForeignKeyConstraint(['frame_id', 'fiber_id'],
                                           ['cobra_config.frame_id', 'cobra_config.fiber_id']),
                      {})

    frame_id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=False)
    fiber_id = Column(Integer, primary_key=True, autoincrement=False)
    motor_num_step_theta = Column(Integer)
    motor_on_time_theta = Column(REAL)
    motor_num_step_phi = Column(Integer)
    motor_on_time_phi = Column(REAL)
    cobra_motor_map_id = Column(Integer, ForeignKey('cobra_motor_map.cobra_motor_map_id'))

    def __init__(self, frame_id, fiber_id,
                 motor_num_step_theta, motor_on_time_theta, motor_num_step_phi, motor_on_time_phi,
                 cobra_motor_map_id
                 ):
        self.frame_id = frame_id
        self.fiber_id = fiber_id
        self.motor_num_step_theta = motor_num_step_theta
        self.motor_on_time_theta = motor_on_time_theta
        self.motor_num_step_phi = motor_num_step_phi
        self.motor_on_time_phi = motor_on_time_phi
        self.cobra_motor_map_id = cobra_motor_map_id


class cobra_config(Base):
    __tablename__ = 'cobra_config'
    __table_args__ = (UniqueConstraint('frame_id', 'fiber_id'),
                      ForeignKeyConstraint(['frame_id', 'fiber_id'],
                                           ['mcs_data.frame_id', 'mcs_data.fiber_id']),
                      {})

    frame_id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=False)
    fiber_id = Column(Integer, primary_key=True, autoincrement=False)
    pfs_config_id = Column(BigInteger, ForeignKey('pfs_config.pfs_config_id'))
    iteration = Column(Integer)
    pfi_nominal_x_mm = Column(REAL)
    pfi_nominal_y_mm = Column(REAL)
    pfi_center_x_mm = Column(REAL)
    pfi_center_y_mm = Column(REAL)
    exectime = Column(DateTime)

    def __init__(self, pfs_config_id, frame_id, fiber_id,
                 iteration, motor_num_step_theta, motor_num_step_phi,
                 pfi_nominal_x_mm, pfi_nominal_y_mm, pfi_center_x_mm, pfi_center_y_mm,
                 exectime):
        self.pfs_config_id = pfs_config_id
        self.frame_id = frame_id
        self.fiber_id = fiber_id
        self.iteration = iteration
        self.pfi_nominal_x_mm = pfi_nominal_x_mm
        self.pfi_nominal_y_mm = pfi_nominal_y_mm
        self.pfi_center_x_mm = pfi_center_x_mm
        self.pfi_center_y_mm = pfi_center_y_mm
        self.exectime = exectime


class beam_switch_mode(Base):
    __tablename__ = 'beam_switch_mode'

    beam_switch_mode_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    beam_switch_mode_name = Column(String)
    beam_switch_mode_description = Column(String)

    def __init__(self, beam_switch_mode_id, beam_switch_mode_name, beam_switch_mode_description):
        self.beam_switch_mode_id = beam_switch_mode_id
        self.beam_switch_mode_name = beam_switch_mode_name
        self.beam_switch_mode_description = beam_switch_mode_description


class tel_visit(Base):
    __tablename__ = 'tel_visit'

    tel_visit_id = Column(Integer, primary_key=True, autoincrement=False)
    pfs_config_id = Column(BigInteger, ForeignKey('pfs_config.pfs_config_id'))
    ra_tel = Column(FLOAT)
    dec_tel = Column(FLOAT)
    beam_switch_mode_id = Column(Integer, ForeignKey('beam_switch_mode.beam_switch_mode_id'))
    beam_switch_offset_ra = Column(REAL)
    beam_switch_offset_dec = Column(REAL)
    time_exp_start = Column(DateTime)
    time_exp_end = Column(DateTime)
    mjd_exp_start = Column(REAL)
    mjd_exp_end = Column(REAL)
    insrot_start = Column(REAL)
    insrot_end = Column(REAL)

    def __init__(self, tel_visit_id,
                 pfs_config_id, ra_tel, dec_tel,
                 beam_switch_mode_id, beam_switch_offset_ra, beam_switch_offset_dec,
                 time_exp_start, time_exp_end, mjd_exp_start, mjd_exp_end,
                 insrot_start, insrot_end
                 ):
        self.tel_visit_id = tel_visit_id
        self.pfs_config_id = pfs_config_id
        self.ra_tel = ra_tel
        self.dec_tel = dec_tel
        self.beam_switch_mode_id = beam_switch_mode_id
        self.beam_switch_offset_ra = beam_switch_offset_ra
        self.beam_switch_offset_dec = beam_switch_offset_dec
        self.time_exp_start = time_exp_start
        self.time_exp_end = time_exp_end
        self.mjd_start = mjd_start
        self.mjd_end = mjd_end
        self.insrot_start = insrot_start
        self.insrot_end = insrot_end


class tel_condition(Base):
    __tablename__ = 'tel_condition'

    tel_visit_id = Column(Integer, ForeignKey('tel_visit.tel_visit_id'), primary_key=True, unique=True, autoincrement=False)
    focusing_error = Column(REAL)
    guide_error_sigma_arcsec = Column(REAL)
    airmass = Column(REAL)
    moon_phase = Column(REAL)
    moon_alt = Column(REAL)
    moon_sep = Column(REAL)
    seeing = Column(REAL)
    transp = Column(REAL)
    cloud_condition_id = Column(Integer, ForeignKey('cloud_condition.cloud_condition_id'))

    def __init__(self, tel_visit_id,
                 focusing_error, guide_error_sigma_arcsec,
                 airmass, moon_phase, moon_alt, moon_sep, seeing, transp,
                 cloud_condition_id,
                 ):
        self.tel_visit_id = tel_visit_id
        self.focusing_error = focusing_error
        self.guide_error_sigma_arcsec = guide_error_sigma_arcsec
        self.airmass = airmass
        self.moon_phase = moon_phase
        self.moon_alt = moon_alt
        self.moon_sep = moon_sep
        self.seeing = seeing
        self.transp = transp
        self.cloud_condition_id = cloud_condition_id


class sps_exposure(Base):
    __tablename__ = 'sps_exposure'

    frame_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    tel_visit_id = Column(Integer, ForeignKey('tel_visit.tel_visit_id'))
    spectrograph_id = Column(Integer, ForeignKey('spectrograph.spectrograph_id'))
    sps_exptime = Column(REAL)
    is_medium_resolution = Column(Boolean)

    tel_visits = relation(tel_visit, backref=backref('sps_exposure'))
    spectrographs = relation(spectrograph, backref=backref('sps_exposure'))
    pfs_configs = relation(pfs_config, backref=backref('sps_exposure'))
    cloud_conditions = relation(cloud_condition, backref=backref('sps_exposure'))
    beam_switch_modes = relation(beam_switch_mode, backref=backref('sps_exposure'))

    def __init__(self, frame_id, tel_visit_id, spectrograph_id,
                 sps_exptime, is_medium_resolution=False
                 ):
        self.frame_id = frame_id
        self.tel_visit_id = tel_visit_id
        self.spectrograph_id = spectrograph_id
        self.sps_exptime = sps_exptime
        self.is_medium_resolution = is_medium_resolution


class sps_condition(Base):
    __tablename__ = 'sps_condition'

    frame_id = Column(Integer, ForeignKey('sps_exposure.frame_id'), primary_key=True, autoincrement=False)
    background = Column(REAL)
    throughput = Column(REAL)

    def __init__(self, frame_id,
                 background, throughput,
                 ):
        self.frame_id = frame_id
        self.background = background
        self.throughput = throughput


class calib(Base):
    __tablename__ = 'calib'

    calib_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    calib_type = Column(String)
    frame_id_start = Column(Integer, ForeignKey('sps_exposure.frame_id'))
    frame_id_end = Column(Integer, ForeignKey('sps_exposure.frame_id'))
    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'))
    calib_date = Column(DateTime)

    sps_exposures = relation(sps_exposure, backref=backref('calib'))
    pfs_designs = relation(pfs_design, backref=backref('calib'))

    def __init__(self, calib_id, calib_type, frame_id_start, frame_id_end,
                 pfs_design_id, calib_date):
        self.calib_id = calib_id
        self.calib_type = calib_type
        self.frame_id_start = frame_id_start
        self.frame_id_end = frame_id_end
        self.pfs_design_id = pfs_design_id
        self.calib_date = calib_date


class calib_set(Base):
    __tablename__ = 'calib_set'
    calib_set_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    calib_flat_id = Column(Integer, ForeignKey('calib.calib_id'))
    calib_bias_id = Column(Integer, ForeignKey('calib.calib_id'))
    calib_dark_id = Column(Integer, ForeignKey('calib.calib_id'))
    calib_arcs_id = Column(Integer, ForeignKey('calib.calib_id'))

    calibs = relation(calib, backref=backref('calib_set'))

    def __init__(self, calib_set_id,
                 calib_flat_id, calib_bias_id, calib_dark_id, calib_arcs_id
                 ):
        self.calib_set_id = calib_set_id
        self.calib_flat_id = calib_flat_id
        self.calib_bias_id = calib_bias_id
        self.calib_dark_id = calib_dark_id
        self.calib_arcs_id = calib_arcs_id


class flux_calib(Base):
    __tablename__ = 'flux_calib'

    flux_calib_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    flux_calib_type = Column(String)
    flux_calib_date = Column(DateTime)
    flux_calib_star_teff = Column(REAL)
    flux_calib_star_logg = Column(REAL)
    flux_calib_star_z = Column(REAL)

    def __init__(self, flux_calib_id, flux_calib_type, flux_calib_date,
                 flux_calib_star_teff, flux_calib_star_logg, flux_calib_star_z):
        self.flux_calib_id = flux_calib_id
        self.flux_calib_type = flux_calib_type
        self.flux_calib_date = flux_calib_date
        self.flux_calib_star_teff = flux_calib_star_teff
        self.flux_calib_star_logg = flux_calib_star_logg
        self.flux_calib_star_z = flux_calib_star_z


class obs_fiber(Base):
    __tablename__ = 'obs_fiber'
    __table_args__ = (UniqueConstraint('frame_id', 'fiber_id'), {})

    frame_id = Column(Integer, ForeignKey('sps_exposure.frame_id'), primary_key=True, autoincrement=False)
    fiber_id = Column(Integer, ForeignKey('fiber_position.fiber_id'), primary_key=True, autoincrement=False)
    target_id = Column(BigInteger)
    exptime = Column(REAL)
    cum_nexp = Column(Integer)
    cum_texp = Column(REAL)

    sps_exposures = relation(sps_exposure, backref=backref('obs_fiber'))
    fiber_positions = relation(fiber_position, backref=backref('obs_fiber'))

    def __init__(self, frame_id, fiber_id, target_id,
                 exptime, cum_nexp, cum_texp):
        self.frame_id = frame_id
        self.fiber_id = fiber_id
        self.target_id = target_id
        self.exptime = exptime
        self.cum_nexp = cum_nexp
        self.cum_texp = cum_texp


class sky_model(Base):
    __tablename__ = 'sky_model'

    sky_model_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    frame_id = Column(Integer, ForeignKey('sps_exposure.frame_id'))
    tel_visit_id = Column(Integer)
    spectrograph_id = Column(Integer, ForeignKey('spectrograph.spectrograph_id'))

    sps_exposures = relation(sps_exposure, backref=backref('sky_model'))
    spectrographs = relation(spectrograph, backref=backref('sky_model'))

    def __init__(self, sky_model_id, frame_id, tel_visit_id, spectrograph_id):
        self.sky_model_id = sky_model_id
        self.frame_id = frame_id
        self.tel_visit_id = tel_visit_id
        self.spectrograph_id = spectrograph_id


class psf_model(Base):
    __tablename__ = 'psf_model'

    psf_model_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    frame_id = Column(Integer, ForeignKey('sps_exposure.frame_id'))
    tel_visit_id = Column(Integer)
    spectrograph_id = Column(Integer, ForeignKey('spectrograph.spectrograph_id'))

    sps_exposures = relation(sps_exposure, backref=backref('psf_model'))
    spectrographs = relation(spectrograph, backref=backref('psf_model'))

    def __init__(self, psf_model_id, frame_id, tel_visit_id, spectrograph_id):
        self.psf_model_id = psf_model_id
        self.frame_id = frame_id
        self.tel_visit_id = tel_visit_id
        self.spectrograph_id = spectrograph_id


class pfs_arm(Base):
    __tablename__ = 'pfs_arm'

    frame_id = Column(Integer, ForeignKey('sps_exposure.frame_id'), primary_key=True, unique=True, autoincrement=False)
    calib_set_id = Column(Integer, ForeignKey('calib_set.calib_set_id'))
    sky_model_id = Column(Integer, ForeignKey('sky_model.sky_model_id'))
    psf_model_id = Column(Integer, ForeignKey('psf_model.psf_model_id'))
    flags = Column(Integer)
    process_datetime = Column(DateTime)
    drp2d_version = Column(String)

    calib_sets = relation(calib_set, backref=backref('pfs_arm'))
    sps_exposures = relation(sps_exposure, backref=backref('pfs_arm'))
    sky_models = relation(sky_model, backref=backref('pfs_arm'))
    psf_models = relation(psf_model, backref=backref('pfs_arm'))

    def __init__(self, frame_id,
                 calib_set_id, sky_model_id, psf_model_id, flags,
                 process_datetime, drp2d_version):
        self.frame_id = frame_id
        self.calib_set_id = calib_set_id
        self.sky_model_id = sky_model_id
        self.psf_model_id = psf_model_id
        self.flags = flags
        self.process_datetime = process_datetime
        self.drp2d_version = drp2d_version


class pfs_arm_obj(Base):
    __tablename__ = 'pfs_arm_obj'
    __table_args__ = (UniqueConstraint('frame_id', 'fiber_id'), {})

    frame_id = Column(Integer, ForeignKey('pfs_arm.frame_id'), primary_key=True, autoincrement=False)
    fiber_id = Column(Integer, ForeignKey('fiber_position.fiber_id'), primary_key=True, autoincrement=False)
    flags = Column(Integer)
    qa_type_id = Column(Integer, ForeignKey('qa_type.qa_type_id'))
    qa_value = Column(REAL)

    pfs_arms = relation(pfs_arm, backref=backref('pfs_arm_obj'))
    fiber_positions = relation(fiber_position, backref=backref('pfs_arm_obj'))
    qa_types = relation(qa_type, backref=backref('pfs_arm_obj'))

    def __init__(self, frame_id, fiber_id, flags, qa_type_id, qa_value):
        self.frame_id = frame_id
        self.fiber_id = fiber_id
        self.flags = flags
        self.qa_type_id = qa_type_id
        self.qa_value = qa_value


class visit_hash(Base):
    __tablename__ = 'visit_hash'

    pfs_visit_hash = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    n_visit = Column(Integer)

    def __init__(self, pfs_visit_hash, n_visit):
        self.pfs_visit_hash = pfs_visit_hash
        self.n_visit = n_visit


class pfs_object(Base):
    __tablename__ = 'pfs_object'

    pfs_object_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    target_id = Column(BigInteger, ForeignKey('target.target_id'))
    tract = Column(Integer)
    patch = Column(String)
    cat_id = Column(Integer)
    obj_id = Column(BigInteger)
    n_visit = Column(Integer)
    pfs_visit_hash = Column(BigInteger, ForeignKey('visit_hash.pfs_visit_hash'))
    cum_texp = Column(REAL)
    process_datetime = Column(DateTime)
    drp2d_version = Column(String)
    flux_calib_id = Column(Integer, ForeignKey('flux_calib.flux_calib_id'))
    flags = Column(Integer)
    qa_type_id = Column(Integer, ForeignKey('qa_type.qa_type_id'))
    qa_value = Column(REAL)

    targets = relation(target, backref=backref('pfs_object'))
    flux_calibs = relation(flux_calib, backref=backref('pfs_object'))
    qa_types = relation(qa_type, backref=backref('pfs_object'))
    visit_hashs = relation(visit_hash, backref=backref('pfs_object'))

    def __init__(self, pfs_object_id, target_id, tract, patch, cat_id, obj_id, n_visit, pfs_visit_hash,
                 cum_texp, process_datetime, drp2d_version, flux_calib_id, flags, qa_type_id, qa_value):
        self.pfs_object_id = pfs_object_id
        self.target_id = target_id
        self.tract = tract
        self.patch = patch
        self.cat_id = cat_id
        self.obj_id = obj_id
        self.n_visit = n_visit
        self.pfs_visit_hash = pfs_visit_hash
        self.cum_texp = cum_texp
        self.process_datetime = process_datetime
        self.drp2d_version = drp2d_version
        self.flux_calib_id = flux_calib_id
        self.flags = flags
        self.qa_type_id = qa_type_id
        self.qa_value = qa_value


class visits_to_combine(Base):
    __tablename__ = 'visits_to_combine'
    __table_args__ = (UniqueConstraint('tel_visit_id', 'pfs_visit_hash'), {})

    tel_visit_id = Column(Integer, ForeignKey('tel_visit.tel_visit_id'), primary_key=True, autoincrement=False)
    pfs_visit_hash = Column(BigInteger, ForeignKey('visit_hash.pfs_visit_hash'), primary_key=True, autoincrement=False)

    sps_exposures = relation(sps_exposure, backref=backref('visits_to_combine'))
    visit_hashs = relation(visit_hash, backref=backref('visits_to_combine'))

    def __init__(self, tel_visit_id, pfs_visit_hash):
        self.tel_visit_id = tel_visit_id
        self.pfs_visit_hash = pfs_visit_hash


class line_list(Base):
    __tablename__ = 'line_list'

    line_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    line_name = Column(String)
    line_wavelength = Column(REAL)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, line_id, line_name, line_wavelength, created_at, updated_at):
        self.line_id = line_id
        self.line_name = line_name
        self.line_wavelength = line_wavelength
        self.created_at = created_at
        self.updated_at = updated_at


class drp1d(Base):
    __tablename__ = 'drp1d'
    __table_args__ = (UniqueConstraint('pfs_object_id', 'process_datetime'), {})

    pfs_object_id = Column(BigInteger, ForeignKey('pfs_object.pfs_object_id'), primary_key=True, autoincrement=False)
    z_best = Column(REAL)
    z_best_err = Column(REAL)
    z_best_reliability = Column(REAL)
    obj_type_id = Column(Integer, ForeignKey('obj_type.obj_type_id'))
    flags = Column(Integer)
    process_datetime = Column(DateTime, primary_key=True, autoincrement=False)
    drp1d_version = Column(String)

    def __init__(self, pfs_object_id, z_best, z_best_err, z_best_reliability,
                 obj_type_id, flags, process_datetime, drp1d_version):
        self.pfs_object_id = pfs_object_id
        self.z_best = z_best
        self.z_best_err = z_best_err
        self.z_best_reliability = z_best_reliability
        self.obj_type_id = obj_type_id
        self.flags = flags
        self.process_datetime = process_datetime
        self.drp1d_version = drp1d_version


class drp1d_redshift(Base):
    __tablename__ = 'drp1d_redshift'
    __table_args__ = (UniqueConstraint('pfs_object_id', 'process_datetime'),
                      ForeignKeyConstraint(['pfs_object_id', 'process_datetime'],
                                           ['drp1d.pfs_object_id', 'drp1d.process_datetime']),
                      {})

    pfs_object_id = Column(BigInteger, primary_key=True, autoincrement=False)
    z = Column(REAL)
    z_err = Column(REAL)
    zrank = Column(REAL)
    reliability = Column(REAL)
    spec_class = Column(String)
    spec_subclass = Column(String)
    process_datetime = Column(DateTime, primary_key=True, autoincrement=False)

    def __init__(self, pfs_object_id, z, z_err, zrank, reliability, spec_Class, spec_subclass, process_datetime):
        self.pfs_object_id = pfs_object_id
        self.z = z
        self.z_err = z_err
        self.zrank = zrank
        self.reliability = reliability
        self.spec_class = spec_class
        self.spec_subclass = spec_subclass
        self.process_datetime = process_datetime


class drp1d_line(Base):
    __tablename__ = 'drp1d_line'
    __table_args__ = (UniqueConstraint('pfs_object_id', 'line_id'), {})
    __table_args__ = (UniqueConstraint('pfs_object_id', 'process_datetime', 'line_id'),
                      ForeignKeyConstraint(['pfs_object_id', 'process_datetime'],
                                           ['drp1d.pfs_object_id', 'drp1d.process_datetime']),
                      {})

    pfs_object_id = Column(BigInteger, primary_key=True, autoincrement=False)
    line_id = Column(Integer, ForeignKey('line_list.line_id'), primary_key=True, autoincrement=False)
    line_name = Column(String)
    line_wave = Column(REAL)
    line_z = Column(REAL)
    line_z_err = Column(REAL)
    line_sigma = Column(REAL)
    line_sigma_err = Column(REAL)
    line_vel = Column(REAL)
    line_vel_err = Column(REAL)
    line_flux = Column(REAL)
    line_flux_err = Column(REAL)
    line_ew = Column(REAL)
    line_ew_err = Column(REAL)
    line_cont_level = Column(REAL)
    line_cont_level_err = Column(REAL)
    process_datetime = Column(DateTime, primary_key=True, autoincrement=False)

    def __init__(self, pfs_object_id, line_id, line_name, line_wave, line_z, line_z_err, line_sigma, line_sigma_err, line_vel, line_vel_err, line_flux, line_flux_err, line_ew, line_ew_err, line_cont_level, line_cont_level_err, process_datetime):
        self.pfs_object_id = pfs_object_id
        self.drp1d_id = drp1d_id
        self.line_id = lineId
        self.line_name = line_name
        self.line_wave = line_wave
        self.line_z = line_z
        self.line_z_err = line_z_err
        self.line_sigma = line_sigma
        self.line_sigma_err = line_sigma_err
        self.line_vel = line_vel
        self.line_vel_err = line_vel_err
        self.line_flux = line_flux
        self.line_flux_err = line_flux_err
        self.line_ew = line_ew
        self.line_ew_err = line_ew_err
        self.line_cont_level = line_cont_level
        self.line_cont_level_err = line_cont_level_err
        self.process_datetime = process_datetime


class drp_ga(Base):
    __tablename__ = 'drp_ga'
    __table_args__ = (UniqueConstraint('pfs_object_id', 'process_datetime'), {})

    pfs_object_id = Column(BigInteger, ForeignKey('pfs_object.pfs_object_id'), primary_key=True, autoincrement=False)
    star_type_id = Column(Integer, ForeignKey('star_type.star_type_id'))
    velocity = Column(REAL)
    metallicity = Column(REAL)
    logg = Column(REAL)
    teff = Column(REAL)
    flags = Column(Integer)
    process_datetime = Column(DateTime, primary_key=True, autoincrement=False)
    drp_ga_version = Column(String)

    def __init__(self, pfs_object_id, star_type_id, velocity, metallicity, logg, teff,
                 flags, process_datetime, drp_ga_version):
        self.pfs_object_id = pfs_object_id
        self.star_type_id = start_type_id
        self.velocity = velocity
        self.metallicity = metallicity
        self.logg = logg
        self.teff = teff
        self.flags = flags
        self.process_datetime = process_datetime
        self.drp_ga_version = drp_ga_version


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
