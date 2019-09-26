from sqlalchemy import create_engine
from sqlalchemy import Column, BigInteger, Integer, String, FLOAT, ForeignKey, DateTime, Boolean, REAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation, backref

Base = declarative_base()


class proposal(Base):
    __tablename__ = 'proposal'

    proposal_id = Column(String, primary_key=True, autoincrement=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, proposal_id, created_at, updated_at):
        self.proposal_id = proposal_id
        self.created_at = created_at
        self.updated_at = updated_at


class program(Base):
    __tablename__ = 'program'

    program_id = Column(Integer, primary_key=True, autoincrement=False)
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

    target_type_id = Column(Integer, primary_key=True, autoincrement=False)
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

    obj_type_id = Column(Integer, primary_key=True, autoincrement=False)
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

    star_type_id = Column(Integer, primary_key=True, autoincrement=False)
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

    qa_type_id = Column(Integer, primary_key=True, autoincrement=False)
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

    cat_id = Column(Integer, primary_key=True, autoincrement=False)
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

    cloud_condition_id = Column(Integer, primary_key=True, autoincrement=False)
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
    fiber_id = Column(Integer, primary_key=True, autoincrement=False)
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


class target(Base):
    __tablename__ = 'target'

    target_id = Column(BigInteger, primary_key=True, autoincrement=True)
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
    guide_star_id = Column(BigInteger, primary_key=True, autoincrement=False)
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

    tile_id = Column(Integer, primary_key=True, autoincrement=True)
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

    pfs_design_id = Column(BigInteger, primary_key=True, autoincrement=False)
    tile_id = Column(Integer, ForeignKey('tile.tile_id'))
    ra_center = Column(FLOAT)
    dec_center = Column(FLOAT)
    pa_config = Column(REAL)
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

    def __init__(self, pfs_design_id, tile_id, ra_center, dec_center, pa_config,
                 num_sci_designed, num_cal_designed, num_sky_designed, num_guide_stars,
                 exptime, min_exptime, ets_version, ets_assgner, ets_exectime, is_obsolete=False):
        self.pfs_design_id = pfs_design_id
        self.tile_id = tile_id
        self.ra_center = ra_center
        self.dec_center = dec_center
        self.pa_config = paConfig
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

    pfs_design_fiber_id = Column(BigInteger, primary_key=True, autoincrement=True)
    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'))
    fiber_id = Column(Integer, ForeignKey('fiber_position.fiber_id'))
    target_id = Column(BigInteger, ForeignKey('target.target_id'))
    tract = Column(Integer)
    patch = Column(String)
    ra = Column(FLOAT)
    dec = Column(FLOAT)
    cat_id = Column(Integer)
    obj_id = Column(BigInteger)
    target_type_id = Column(Integer)
    fiber_mag_g = Column(REAL)
    fiber_mag_r = Column(REAL)
    fiber_mag_i = Column(REAL)
    fiber_mag_z = Column(REAL)
    fiber_mag_y = Column(REAL)
    fiber_mag_j = Column(REAL)
    ets_priority = Column(Integer)
    ets_cost_function = Column(String)
    ets_cobra_movement = Column(String)
    pfi_nominal_x = Column(REAL)
    pfi_nominal_y = Column(REAL)
    is_on_source = Column(Boolean)

    pfs_designs = relation(pfs_design, backref=backref('pfs_design_fiber'))
    targets = relation(target, backref=backref('pfs_design_fiber'))
    fiber_positions = relation(fiber_position, backref=backref('pfs_design_fiber'))
    #target_type = relation(target_type, backref=backref('pfs_design_fiber'))
    #input_catalogs = relation(input_catalog, backref=backref('pfs_design_fiber'))

    def __init__(self, pfs_design_fiber_id, pfs_design_id, fiber_id,
                 target_id, tract, patch, ra, dec, cat_d, obj_id, target_type_id,
                 fiber_mag_g, fiber_mag_r, fiber_mag_i, fiber_mag_z, fiber_mag_y, fiber_mag_j,
                 ets_priority, ets_cost_function, ets_cobra_movement,
                 pfi_nominal_x, pfi_nominal_y,
                 is_on_source=True):
        self.pfs_design_fiber_id = (pfs_design_id << 12) + fiber_id
        self.pfs_design_id = pfs_design_id
        self.fiber_id = fiber_id
        self.target_id = target_id
        self.tract = tract
        self.patch = patch
        self.ra = ra
        self.dec = dec
        self.cat_id = cat_id
        self.obj_id = obj_id
        self.target_type_id = target_type_id
        self.fiber_mag_g = fiber_mag_g
        self.fiber_mag_r = fiber_mag_r
        self.fiber_mag_i = fiber_mag_i
        self.fiber_mag_z = fiber_mag_z
        self.fiber_mag_y = fiber_mag_y
        self.fiber_mag_j = fiber_mag_j
        self.ets_priority = ets_priority
        self.ets_cost_function = ets_cost_function
        self.ets_cobra_movement = ets_cobra_movement
        self.pfi_nominal_x = pfi_nominal_x
        self.pfi_nominal_y = pfi_nominal_y
        self.is_on_source = is_on_source


class calib(Base):
    __tablename__ = 'calib'

    calib_id = Column(Integer, primary_key=True, autoincrement=False)
    calib_iype = Column(String)
    calib_date = Column(DateTime)
    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'))
    spectrograph = Column(Integer)
    arm = Column(String)
    exptime = Column(REAL)
    visits_in_use = Column(String)

    pfs_designs = relation(pfs_design, backref=backref('calib'))

    def __init__(self, calib_id, calib_type, calib_date, pfs_design_id, spectrogarph, arm,
                 exptime, visits_in_use):
        self.calib_id = calib_id
        self.calib_type = calib_type
        self.calib_date = calib_date
        self.pfs_design_id = pfs_design_id
        self.spectrograph = spectrograph
        self.arm = arm
        self.exptime = exptime
        self.visits_in_use = visits_in_use


class flux_calib(Base):
    __tablename__ = 'flux_calib'

    flux_calib_id = Column(Integer, primary_key=True, autoincrement=False)
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


class visit(Base):
    __tablename__ = 'visit'

    visit_id = Column(Integer, primary_key=True, autoincrement=False)
    visit_type = Column(Integer)
    visit_description = Column(String)

    def __init__(self, visit_id, visit_type, visit_description):
        self.visit_id = visit_id
        self.visit_type = visit_type
        self.visit_description = visit_description


class mcs_boresight(Base):

    __tablename__ = 'mcs_boresight'

    mcs_boresight_id = Column(Integer, primary_key=True, autoincrement=True)
    visit_id = Column(Integer)
    datatime = Column(DateTime)
    x = Column(REAL)
    y = Column(REAL)

    def __init__(self, visit_id, datatime, x, y):
        self.visit_id = visit_id
        self.datatime = datatime
        self.x = x
        self.y = y


class mcs_exposure(Base):

    __tablename__ = 'mcs_exposure'

    mcs_exposure_id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    frame_id = Column(Integer, index=True, nullable=False)
    starttime = Column(DateTime)
    mcs_exptime = Column(REAL, nullable=False)
    altitude = Column(REAL)
    azimuth = Column(REAL)
    insrot = Column(REAL)

    def __init__(self, mcs_exposure_id, frame_id, starttime, mcs_exptime, altitude, azimuth, insrot):
        self.mcs_exposure_id = mcs_exposure_id
        self.frame_id = frame_id
        self.starttime = starttime
        self.mcs_exptime = mcs_exptime
        self.altitude = altitude
        self.azimuth = azimuth
        self.insrot = insrot


class mcs_data(Base):

    __tablename__ = 'mcs_data'

    mcs_id = Column(Integer, primary_key=True, autoincrement=True)
    datatime = Column(DateTime)
    frame_id = Column(Integer, index=True)
    move_id = Column(Integer)
    fiber_id = Column(Integer)
    #fiber_id = Column(Integer, ForeignKey('fiber_position.fiber_id'))
    centroid_x = Column(REAL)
    centroid_y = Column(REAL)
    fwhm_x = Column(REAL)
    fwhm_y = Column(REAL)
    bgvalue = Column(REAL)
    peakvalue = Column(REAL)

    #fiber_positions = relation(fiber_position, backref=backref('mcsData'))

    def __init__(self, mcs_id, datatime, frame_id, move_id, fiber_id,
                 centroid_x, centroid_y, fwhm_x, fwhm_y, bgvalue, peakvalue):
        self.mcs_id = mcs_id
        self.datatime = datatime
        self.frame_id = frame_id
        self.move_id = move_id
        self.fiber_id = fiber_id
        self.centroid_x = centroid_x
        self.centroid_y = centroid_y
        self.fwhm_x = fwhm_x
        self.fwhm_y = fwhm_y
        self.bgvalue = bgvalue
        self.peakvalue = peakvalue


class pfs_config(Base):
    __tablename__ = 'pfs_config'

    pfs_config_id = Column(Integer, primary_key=True, autoincrement=True)
    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'))
    visit0 = Column(Integer, ForeignKey('visit.visit_id'))
    ra_center = Column(FLOAT)
    dec_center = Column(FLOAT)
    pa_config = Column(REAL)
    tel_el = Column(REAL)
    insrot = Column(REAL)
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

    visits = relation(visit, backref=backref('pfs_config'))

    def __init__(self, pfs_config_id, pfs_design_id, visit0, ra_center, dec_center, pa_config, tel_el, ins_rot,
                 num_sci_allocated, num_cal_allocated, num_sky_allocated, num_guide_stars,
                 exptime, min_exptime, alloc_num_iter, alloc_elapsetime, alloc_rms_scatter, alloc_exectime,
                 is_observed=False):
        self.pfs_config_id = pfs_config_id
        self.pfs_design_id = pfs_design_id
        self.visit0 = visit0
        self.ra_center = ra_center
        self.dec_center = dec_center
        self.pa_config = pa_config
        self.tel_el = tel_el
        self.ins_rot = ins_rot
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

    pfs_config_fiber_id = Column(BigInteger, primary_key=True, autoincrement=False)
    pfs_config_id = Column(BigInteger, ForeignKey('pfs_config.pfs_config_id'))
    fiber_id = Column(Integer, ForeignKey('fiber_position.fiber_id'))
    target_id = Column(BigInteger, ForeignKey('target.target_id'))
    tract = Column(Integer)
    patch = Column(String)
    ra = Column(FLOAT)
    dec = Column(FLOAT)
    cat_id = Column(Integer)
    obj_id = Column(BigInteger)
    target_type_id = Column(Integer)
    fiber_mag_g = Column(REAL)
    fiber_mag_r = Column(REAL)
    fiber_mag_i = Column(REAL)
    fiber_mag_z = Column(REAL)
    fiber_mag_y = Column(REAL)
    fiber_mag_j = Column(REAL)
    pfi_nominal_x = Column(REAL)
    pfi_nominal_y = Column(REAL)
    pfi_center_x = Column(REAL)
    pfi_center_y = Column(REAL)
    pfi_diff_x = Column(REAL)
    pfi_diff_y = Column(REAL)
    mcs_center_x = Column(REAL)
    mcs_center_y = Column(REAL)
    motor_map_summary = Column(String)
    config_time = Column(REAL)
    is_on_source = Column(Boolean)

    pfs_configs = relation(pfs_config, backref=backref('psf_config_fiber'))
    targets = relation(target, backref=backref('psf_config_fiber'))
    fiber_positions = relation(fiber_position, backref=backref('psf_config_fiber'))
    #target_types = relation(target_type, backref=backref('pfs_config_fiber'))
    #input_catalogs = relation(input_catalog, backref=backref('pfs_config_fiber'))

    def __init__(self, pfs_config_fiber_id, pfs_config_id, fiber_id,
                 target_id, tract, patch, cat_id, obj_id, target_type_id,
                 fiber_mag_g, fiber_mag_r, fiber_mag_i, fiber_mag_z, fiber_mag_y, fiber_mag_j,
                 pfi_nominal_x, pfi_nominal_y, pfi_center_x, pfi_center_y, pfi_diff_x, pfi_diff_y,
                 mcs_center_x, mcs_center_y, motor_map_summary, config_time,
                 is_on_source=True):
        self.pfs_config_fiber_id = (pfs_config_id << 12) + fiber_id
        self.pfs_config_id = pfs_config_id
        self.fiber_id = fiber_id
        self.target_id = target_id
        self.tract = tract
        self.patch = patch
        self.ra = ra
        self.dec = dec
        self.cat_id = cat_id
        self.obj_id = obj_id
        self.target_type_id = target_type_id
        self.fiber_mag_g = fiber_mag_g
        self.fiber_mag_r = fiber_mag_r
        self.fiber_mag_i = fiber_mag_i
        self.fiber_mag_z = fiber_mag_z
        self.fiber_mag_y = fiber_mag_y
        self.fiber_mag_j = fiber_mag_j
        self.pfi_nominal_x = pfi_nominal_x
        self.pfi_nominal_y = pfi_nominal_y
        self.pfi_center_x = pfi_center_x
        self.pfi_center_y = pfi_center_y
        self.pfi_diff_x = pfi_diff_x
        self.pfi_diff_y = pfi_diff_y
        self.mcs_center_x = mcs_center_x
        self.mcs_center_y = mcs_center_y
        self.motor_map_summary = motor_map_summary
        self.config_time = config_time
        self.is_on_source = is_on_source


class cobra_config(Base):
    __tablename__ = 'cobra_config'

    cobra_config_id = Column(BigInteger, primary_key=True, autoincrement=True)
    pfs_config_fiber_id = Column(BigInteger, ForeignKey('pfs_config_fiber.pfs_config_fiber_id'))
    pfs_config_id = Column(BigInteger)
    fiber_id = Column(Integer)
    iteration = Column(Integer)
    motor_num_step_theta = Column(Integer)
    motor_num_step_phi = Column(Integer)
    mcs_id = Column(Integer, ForeignKey('mcs_data.mcs_id'))
    pfi_nominal_x = Column(REAL)
    pfi_nominal_y = Column(REAL)
    pfi_center_x = Column(REAL)
    pfi_center_y = Column(REAL)
    pfi_diff_x = Column(REAL)
    pfi_diff_y = Column(REAL)
    mcs_center_x = Column(REAL)
    mcs_center_y = Column(REAL)
    exectime = Column(DateTime)

    def __init__(self, cobra_config_id, pfs_config_fiber_id, pfs_config_id, fiber_id, iteration,
                 motor_num_step_theta, motor_num_step_phi, mcs_id,
                 pfi_nominal_x, pfi_nominal_y, pfi_center_x, pfi_center_y, pfi_diff_x, pfi_diff_y,
                 mcs_center_x, mcs_center_y, exectime):
        self.cobra_config_id = cobra_config_id
        self.pfs_config_fiber_id = pfs_config_fiber_id
        self.pfs_config_id = pfs_config_id
        self.fiber_id = fiber_id
        self.iteration = iteration
        self.motor_num_step_theta = motor_num_step_theta
        self.motor_num_step_phi = motor_num_step_phi
        self.mcs_id = mcs_id
        self.pfi_nominal_x = pfi_nominal_x
        self.pfi_nominal_y = pfi_nominal_y
        self.pfi_center_x = pfi_center_x
        self.pfi_center_y = pfi_center_y
        self.pfi_diff_x = pfi_diff_x
        self.pfi_diff_y = pfi_diff_y
        self.mcs_center_x = mcs_center_x
        self.mcs_center_y = mcs_center_y
        self.exectime = exectime


class beam_switch_mode(Base):
    __tablename__ = 'beam_switch_mode'

    beam_switch_mode_id = Column(Integer, primary_key=True, autoincrement=False)
    beam_switch_mode_name = Column(String)
    beam_switch_mode_description = Column(String)

    def __init__(self, beam_switch_mode_id, beam_switch_mode_name, beam_switch_mode_description):
        self.beam_switch_mode_id = beam_switch_mode_id
        self.beam_switch_mode_name = beam_switch_mode_name
        self.beam_switch_mode_description = beam_switch_mode_description


class exposure(Base):
    __tablename__ = 'exposure'

    frame_id = Column(String, primary_key=True, autoincrement=False)
    visit_id = Column(Integer, ForeignKey('visit.visit_id'))
    spectrograph = Column(Integer)
    arm = Column(String)
    arm_num = Column(Integer)
    pfs_config_id = Column(BigInteger, ForeignKey('pfs_config.pfs_config_id'))
    ra_tel = Column(FLOAT)
    dec_tel = Column(FLOAT)
    exptime = Column(REAL)
    time_obs_start = Column(DateTime)
    time_obs_end = Column(DateTime)
    mjd_start = Column(REAL)
    mjd_end = Column(REAL)
    airmass = Column(REAL)
    seeing = Column(REAL)
    transp = Column(REAL)
    background = Column(REAL)
    moon_phase = Column(REAL)
    moon_alt = Column(REAL)
    moon_sep = Column(REAL)
    throughput = Column(REAL)
    cloud_condition_id = Column(Integer, ForeignKey('cloud_condition.cloud_condition_id'))
    focusing_error = Column(REAL)
    insrot_start = Column(REAL)
    insrot_end = Column(REAL)
    guide_error_dx = Column(REAL)
    guide_error_dy = Column(REAL)
    beam_switch_mode_id = Column(Integer, ForeignKey('beam_switch_mode.beam_switch_mode_id'))
    beam_switch_offset_ra = Column(REAL)
    beam_switch_offset_dec = Column(REAL)
    is_medium_resolution = Column(Boolean)

    visits = relation(visit, backref=backref('exposure'))
    pfs_configs = relation(pfs_config, backref=backref('exposure'))
    cloud_conditions = relation(cloud_condition, backref=backref('exposure'))
    beam_switch_modes = relation(beam_switch_mode, backref=backref('exposure'))

    def __init__(self, frame_id, visit_id, spectrograph, arm, arm_num,
                 pfs_config_id, ra_tel, dec_tel, exptime, time_obs_start, time_obs_end,
                 mjd_start, mjd_end, airmass, seeing, transp, background, moon_phase, moon_alt, moon_sep,
                 throughput, cloud_condition_id, guide_error_dx, guide_error_dy, focusing_error,
                 insrot_start, insrot_end, beam_switch_mode_id=0, beam_switch_offset_ra=0.0, beam_switch_offset_dec=0.0,
                 is_medium_resolution=False
                 ):
        self.frame_id = frame_id
        self.visit_id = visit_id
        self.spectrograph = spectrograph
        self.arm = arm
        self.arm_num = arm_num
        self.pfs_config_id = pfs_config_id
        self.ra_tel = ra_tel
        self.dec_tel = dec_tel
        self.exptime = exptime
        self.time_obs_start = time_obs_start
        self.time_obs_end = time_obs_end
        self.mjd_start = mjd_start
        self.mjd_end = mjd_end
        self.airmass = airmass
        self.seeing = seeing
        self.transp = transp
        self.background = background
        self.moon_phase = moon_phase
        self.moon_alt = moon_alt
        self.moon_sep = moon_sep
        self.throughput = throughput
        self.cloud_condition_id = cloud_condition_id
        self.focusing_error = focusing_error
        self.insrot_start = insrot_start
        self.insrot_end = insrot_end
        self.guide_error_dx = guide_error_dx
        self.guide_error_dy = guide_error_dy
        self.beam_switch_mode_id = beam_switch_mode_id
        self.beam_switch_offset_ra = beam_switch_offset_ra
        self.beam_switch_offset_dec = beam_switch_offset_dec
        self.is_medium_resolution = is_medium_resolution


class obs_fiber(Base):
    __tablename__ = 'obs_fiber'

    obsfiber_id = Column(BigInteger, primary_key=True, autoincrement=True)
    frame_id = Column(String, ForeignKey('exposure.frame_id'))
    visit_id = Column(Integer, ForeignKey('visit.visit_id'))
    pfs_config_fiber_id = Column(BigInteger, ForeignKey('pfs_config_fiber.pfs_config_fiber_id'))
    fiber_id = Column(Integer)
    target_id = Column(BigInteger, ForeignKey('target.target_id'))
    exptime = Column(REAL)
    cum_nexp = Column(Integer)
    cum_texp = Column(REAL)
    delta_pfi_x = Column(REAL)
    delta_pfi_y = Column(REAL)

    visits = relation(visit, backref=backref('obs_fiber'))
    exposures = relation(exposure, backref=backref('obs_fiber'))
    pfs_config_fibers = relation(pfs_config_fiber, backref=backref('obs_fiber'))
    targets = relation(target, backref=backref('obs_fiber'))

    def __init__(self, frame_id, visit_id, pfs_config_fiber_id, fiber_id, target_id,
                 exptime, cum_nexp, cum_texp, delta_pfi_x, delta_pfi_y):
        self.frame_id = frame_id
        self.visit_id = visit_id
        self.pfs_config_fiber_id = pfs_config_fiber_id
        self.fiber_id = fiber_id
        self.target_id = target_id
        self.exptime = exptime
        self.cum_nexp = cum_nexp
        self.cum_texp = cum_texp
        self.delta_pfi_x = delta_pfi_x
        self.delta_pfi_y = delta_pfi_y


class sky_model(Base):
    __tablename__ = 'sky_model'

    sky_model_id = Column(Integer, primary_key=True, autoincrement=False)
    frame_id = Column(String, ForeignKey('exposure.frame_id'))
    visit = Column(Integer, ForeignKey('visit.visit_id'))
    spectrograph = Column(Integer)
    arm = Column(String)
    arm_num = Column(Integer)

    visits = relation(visit, backref=backref('sky_model'))
    exposures = relation(exposure, backref=backref('sky_model'))

    def __init__(self, sky_model_id, frame_id, visit_id, spectrograph, arm, arm_num):
        self.sky_model_id = sky_model_id
        self.frame_id = frame_id
        self.visit_id = visit_id
        self.spectrograph = spectrograph
        self.arm = arm
        self.arm_num = arm_num


class psf_model(Base):
    __tablename__ = 'psf_model'

    psf_model_id = Column(Integer, primary_key=True, autoincrement=False)
    frame_id = Column(String, ForeignKey('exposure.frame_id'))
    visit_id = Column(Integer, ForeignKey('visit.visit_id'))
    spectrograph = Column(Integer)
    arm = Column(String)
    arm_num = Column(Integer)

    visits = relation(visit, backref=backref('psf_model'))
    exposures = relation(exposure, backref=backref('psf_model'))

    def __init__(self, psf_model_id, frame_id, visit_id, spectrograph, arm, arm_num):
        self.psf_model_id = psf_model_id
        self.frame_id = frame_id
        self.visit_id = visit_id
        self.spectrograph = spectrograph
        self.arm = arm
        self.arm_num = arm_num


class pfs_arm(Base):
    __tablename__ = 'pfs_arm'

    pfs_arm_id = Column(Integer, primary_key=True, autoincrement=True)
    frame_id = Column(String, ForeignKey('exposure.frame_id'), unique=True)
    visit_id = Column(Integer, ForeignKey('visit.visit_id'))
    spectrograph = Column(Integer)
    arm = Column(String)
    arm_num = Column(Integer)
    calib_flat_id = Column(Integer, ForeignKey('calib.calib_id'))
    calib_bias_id = Column(Integer, ForeignKey('calib.calib_id'))
    calib_dark_id = Column(Integer, ForeignKey('calib.calib_id'))
    calib_arcs_id = Column(Integer, ForeignKey('calib.calib_id'))
    pfs_config_id = Column(BigInteger, ForeignKey('pfs_config.pfs_config_id'))
    sky_model_id = Column(Integer, ForeignKey('sky_model.sky_model_id'))
    psf_model_id = Column(Integer, ForeignKey('psf_model.psf_model_id'))
    flags = Column(Integer)
    process_datetime = Column(DateTime)
    drp2d_version = Column(String)

    visits = relation(visit, backref=backref('pfs_arm'))
    exposures = relation(exposure, backref=backref('pfs_arm'))
    # calibs = relation(calib, backref=backref('pfs_arm'))
    pfs_configs = relation(pfs_config, backref=backref('pfs_arm'))
    sky_models = relation(sky_model, backref=backref('pfs_arm'))
    psf_models = relation(psf_model, backref=backref('pfs_arm'))

    def __init__(self, pfs_arm_id, frame_id, visit_id, spectrograph, arm, arm_num,
                 calib_flat_id, calib_bias_id, calib_dark_id, calib_arcs_id,
                 sky_model_id, psf_model_id, flags,
                 process_datetime, drp2d_version):
        self.pfs_arm_id = pfs_arm_id
        self.frame_id = frame_id
        self.visit_id = visit_id
        self.spectrograph = spectrograph
        self.arm = arm
        self.arm_num = arm_num
        self.calib_flat_id = calib_flat_id
        self.calib_bias_id = calib_bias_id
        self.calib_dark_id = calib_dark_id
        self.calib_arcs_id = calib_arcs_id
        self.pfs_config_id = pfs_config_id
        self.sky_model_id = sky_model_id
        self.psf_model_id = psf_model_id
        self.flags = flags
        self.process_datetime = process_datetime
        self.drp2d_version = drp2d_version


class pfs_arm_obj(Base):
    __tablename__ = 'pfs_arm_obj'

    pfs_arm_obj_id = Column(BigInteger, primary_key=True, autoincrement=True)
    pfs_arm_id = Column(Integer, ForeignKey('pfs_arm.pfs_arm_id'))
    frame_id = Column(String)
    visit_id = Column(Integer, ForeignKey('visit.visit_id'))
    spectrograph = Column(Integer)
    arm = Column(String)
    arm_num = Column(Integer)
    fiber_id = Column(Integer, ForeignKey('fiber_position.fiber_id'))
    pfs_config_fiber_id = Column(BigInteger, ForeignKey('pfs_config_fiber.pfs_config_fiber_id'))
    flags = Column(Integer)
    qa_type_id = Column(Integer, ForeignKey('qa_type.qa_type_id'))
    qa_value = Column(REAL)

    visits = relation(visit, backref=backref('pfs_arm_obj'))
    pfs_arms = relation(pfs_arm, backref=backref('pfs_arm_obj'))
    pfs_config_fibers = relation(pfs_config_fiber, backref=backref('psf_arm_obj'))
    fiber_positions = relation(fiber_position, backref=backref('pfs_arm_obj'))
    qa_types = relation(qa_type, backref=backref('pfs_arm_obj'))

    def __init__(self, pfs_arm_id, visit_id, spectrograph, arm, arm_num,
                 fiber_id, pfs_config_fiber_id, flags, qa_type_id, qa_value):
        self.pfs_arm_id = pfs_arm_id
        self.visit_id = visit_id
        self.spectrograph = spectrograph
        self.arm = arm
        self.arm_num = armNum
        self.fiber_id = fiber_id
        self.pfs_config_fiber_id = pfs_config_fiber_id
        self.flags = flags
        self.qa_type_id = qa_type_id
        self.qa_value = qa_value


class visit_hash(Base):
    __tablename__ = 'visit_hash'

    pfs_visit_hash = Column(BigInteger, primary_key=True, autoincrement=False)
    n_visit = Column(Integer)

    def __init__(self, pfs_visit_hash, n_visit):
        self.pfs_visit_hash = pfs_visit_hash
        self.n_visit = n_visit


class pfs_object(Base):
    __tablename__ = 'pfs_object'

    pfs_object_id = Column(BigInteger, primary_key=True, autoincrement=True)
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

    visits_to_combine_id = Column(BigInteger, primary_key=True, autoincrement=True)
    target_id = Column(BigInteger, ForeignKey('target.target_id'))
    visit = Column(Integer, ForeignKey('visit.visit_id'))
    pfs_visit_hash = Column(BigInteger, ForeignKey('visit_hash.pfs_visit_hash'))

    targets = relation(target, backref=backref('visits_to_combine'))
    visits = relation(visit, backref=backref('visits_to_combine'))
    visit_hashs = relation(visit_hash, backref=backref('visits_to_combine'))

    def __init__(self, target_id, visit, pfs_visit_hash):
        self.target_id = target_id
        self.visit = visit
        self.pfs_visit_hash = pfs_visit_hash


class line_list(Base):
    __tablename__ = 'line_list'

    line_id = Column(Integer, primary_key=True, autoincrement=False)
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

    drp1d_id = Column(Integer, primary_key=True, autoincrement=True)
    pfs_object_id = Column(BigInteger, ForeignKey('pfs_object.pfs_object_id'))
    z_best = Column(REAL)
    z_best_err = Column(REAL)
    z_best_reliability = Column(REAL)
    obj_type_id = Column(Integer, ForeignKey('obj_type.obj_type_id'))
    flags = Column(Integer)
    process_datetime = Column(DateTime)
    drp1d_version = Column(String)

    pfs_objects = relation(pfs_object, backref=backref('drp1d'))
    obj_types = relation(obj_type, backref=backref('drp1d'))

    def __init__(self, drp1d_id, pfs_object_id, z_best, z_best_err, z_best_reliability,
                 obj_type_id, flags, process_datetime, drp1d_version):
        self.drp1d_id = drp1d_id
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

    drp1d_redshift_id = Column(BigInteger, primary_key=True, autoincrement=True)
    drp1d_id = Column(Integer, ForeignKey('drp1d.drp1d_id'))
    z = Column(REAL)
    z_err = Column(REAL)
    zrank = Column(REAL)
    reliability = Column(REAL)
    spec_class = Column(String)
    spec_subclass = Column(String)

    def __init__(self, drp1d_redshift_id, drp1d_id, z, z_err, zrank, reliability, spec_Class, spec_subclass):
        self.drp1d_redshift_id = drp1d_redshift_id
        self.drp1d_id = drp1d_id
        self.z = z
        self.z_err = z_err
        self.zrank = zrank
        self.reliability = reliability
        self.spec_class = spec_class
        self.spec_subclass = spec_subclass


class drp1d_line(Base):
    __tablename__ = 'drp1d_line'

    drp1d_line_id = Column(BigInteger, primary_key=True, autoincrement=True)
    drp1d_id = Column(Integer, ForeignKey('drp1d.drp1d_id'))
    line_id = Column(Integer, ForeignKey('line_list.line_id'))
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

    line_lists = relation(line_list, backref=backref('drp1d_line'))

    def __init__(self, drp1d_line_id, drp1d_id, line_id, line_name, line_wave, line_z, line_z_err, line_sigma, line_sigma_err, line_vel, line_vel_err, line_flux, line_flux_err, line_ew, line_ew_err, line_cont_level, line_cont_level_err):
        self.drp1d_line_id = drp1d_line_id
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


class drp_ga(Base):
    __tablename__ = 'drp_ga'

    drp_ga_id = Column(Integer, primary_key=True, autoincrement=True)
    pfs_object_id = Column(BigInteger, ForeignKey('pfs_object.pfs_object_id'), primary_key=True)
    star_type_id = Column(Integer, ForeignKey('star_type.star_type_id'))
    velocity = Column(REAL)
    metallicity = Column(REAL)
    logg = Column(REAL)
    teff = Column(REAL)
    flags = Column(Integer)
    process_datetime = Column(DateTime)
    drp_ga_version = Column(String)

    pfs_objects = relation(pfs_object, backref=backref('drp_ga'))
    star_types = relation(star_type, backref=backref('drp_ga'))

    def __init__(self, drp_ga_id, star_type_id, velocity, metallicity, logg, teff,
                 flags, process_datetime, drp_ga_version):
        self.drp_ga_id = drp_ga_id
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
