from sqlalchemy import create_engine
from sqlalchemy import Column, BigInteger, Integer, String, FLOAT, ForeignKey, DateTime, Boolean, REAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation, backref
from sqlalchemy import UniqueConstraint, ForeignKeyConstraint

Base = declarative_base()


class proposal(Base):
    ''' Defines a scientific observing proposal.
    '''
    __tablename__ = 'proposal'

    proposal_id = Column(String, primary_key=True, unique=True, autoincrement=False,
                         comment='Unique identifier for proposal')
    created_at = Column(DateTime, comment='Creation time [YYYY-MM-DDThh:mm:ss]')
    updated_at = Column(DateTime, comment='Update time [YYYY-MM-DDThh:mm:ss]')

    def __init__(self, proposal_id, created_at, updated_at):
        self.proposal_id = proposal_id
        self.created_at = created_at
        self.updated_at = updated_at


class program(Base):
    __tablename__ = 'program'

    program_id = Column(Integer, primary_key=True, unique=True, autoincrement=False,
                        comment='Unique program identifier')
    program_name = Column(String)
    program_description = Column(String)
    proposal_id = Column(String, ForeignKey('proposal.proposal_id'))
    is_filler = Column(Boolean)  # xxxx what does this mean?
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


class cobra_geometry(Base):
    __tablename__ = 'cobra_geometry'

    fiber_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    field_on_pfi = Column(Integer)     # 1-3
    cobra_in_field = Column(Integer)   # 1-798
    module_in_field = Column(Integer)  # 1-14
    cobra_in_module = Column(Integer)  # 1-57
    module_name = Column(String(3))    # e.g.,13B
    cobra_center_on_pfi_x_mm = Column(REAL)
    cobra_center_on_pfi_y_mm = Column(REAL)
    cobra_distance_from_center_mm = Column(REAL)
    spectrograph_id = Column(Integer, ForeignKey('spectrograph.spectrograph_id'))
    slit_hole_sps = Column(Integer)
    fiber_id_sps = Column(Integer)
    fiber_id_lna = Column(String(12))
    version = Column(String)

    def __init__(self, fiber_id, field_on_pfi, cobra_in_field,
                 module_in_field, cobra_in_module, module_name,
                 cobra_center_on_pfi_x_mm, cobra_center_on_pfi_y_mm,
                 cobra_distance_from_center_mm, spectrograph_id, slit_hole_sps, fiber_id_sps,
                 fiber_id_lna, version):
        self.fiber_id = fiber_id
        self.field_on_pfi = field_on_pfi
        self.cobra_in_field = cobra_in_field
        self.module_in_field = module_in_field
        self.cobra_in_module = cobra_in_module
        self.module_name = module_name
        self.cobra_center_on_pfi_x_mm = cobra_center_on_pfi_x_mm
        self.cobra_center_on_pfi_y_mm = cobra_center_on_pfi_y_mm
        self.cobra_distance_from_center_mm = cobra_distance_from_center_mm
        self.spectrograph_id = spectrograph_id
        self.slit_hole_sps = slit_hole_sps
        self.fiber_id_sps = fiber_id_sps
        self.fiber_id_lna = fiber_id_lna
        self.version = version


class fiducial_fiber_position(Base):
    __tablename__ = 'fiducial_fiber_position'
    fiducial_fiber_id = Column(Integer, primary_key=True, autoincrement=False)
    field_on_pfi = Column(Integer)   # 1-3
    ff_in_field = Column(Integer)    # 1-32
    ff_type = Column(String(5))      # spoke/edge/agfid
    ff_id_in_type = Column(Integer)  # 1-14 for spoke, 1-14 for edge, 1-4 for agfid
    ff_center_on_pfi_x_mm = Column(REAL)
    ff_center_on_pfi_y_mm = Column(REAL)
    version = Column(String)

    def __init__(self, fiducial_fiber_id, field_on_pfi, ff_in_field, ff_type, ff_id_in_type,
                 ff_center_on_pfi_x_mm, ff_center_on_pfi_y_mm, version):
        self.fiducial_fiber_id = fiducial_fiber_id
        self.field_on_pfi = field_on_pfi
        self.ff_in_field = ff_in_field
        self.ff_type = ff_type
        self.ff_id_in_type = ff_id_in_type
        self.ff_center_on_pfi_x_mm = ff_center_on_pfi_x_mm
        self.ff_center_on_pfi_y_mm = ff_center_on_pfi_y_mm
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
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    programs = relation(program, backref=backref('target'))
    target_types = relation(target_type, backref=backref('target'))
    input_catalogs = relation(input_catalog, backref=backref('target'))
    qa_types = relation(qa_type, backref=backref('target'))

    def __init__(self, program_id, obj_id, ra, dec, tract, patch, priority, target_type_id, cat_id,
                 cat_obj_id,
                 fiber_mag_g, fiber_mag_r, fiber_mag_i, fiber_mag_z, fiber_mag_y,
                 fiber_mag_j, fiducial_exptime, photz, is_medium_resolution,
                 qa_type_id, qa_lambda_min, qa_lambda_max, qa_threshold, qa_line_flux,
                 completeness, is_finished, created_at, updated_at):
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
        self.created_at = created_at
        self.updated_at = updated_at


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
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    input_catalogs = relation(input_catalog, backref=backref('guide_stars'))
    obj_types = relation(obj_type, backref=backref('guide_stars'))

    def __init__(self, guide_star_id, ra, dec, cat_id, mag_agc, flux_agc, flags,
                 created_at, updated_at):
        self.guide_star_id = guide_star_id
        self.ra = ra
        self.dec = dec
        self.cat_id = cat_id
        self.mag_agc = mag_agc
        self.flux_agc = flux_agc
        self.flags = flags
        self.created_at = created_at
        self.updated_at = updated_at


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
    exptime_tot = Column(REAL)
    exptime_min = Column(REAL)
    ets_version = Column(String)
    ets_assigner = Column(String)
    designed_at = Column(DateTime)
    to_be_observed_at = Column(DateTime)
    is_obsolete = Column(Boolean)

    tiles = relation(tile, backref=backref('pfs_design'))

    def __init__(self, pfs_design_id, tile_id, ra_center_designed, dec_center_designed, pa_designed,
                 num_sci_designed, num_cal_designed, num_sky_designed, num_guide_stars,
                 exptime_tot, exptime_min, ets_version, ets_assigner, designed_at, to_be_observed_at,
                 is_obsolete=False):
        self.pfs_design_id = pfs_design_id
        self.tile_id = tile_id
        self.ra_center_designed = ra_center_designed
        self.dec_center_designed = dec_center_designed
        self.pa_designed = pa_designed
        self.num_sci_designed = num_sci_designed
        self.num_cal_designed = num_cal_designed
        self.num_sky_designed = num_sky_designed
        self.num_guide_stars = num_guide_stars
        self.exptime_tot = exptime_tot
        self.exptime_min = exptime_min
        self.ets_version = ets_version
        self.ets_assigner = ets_assigner
        self.designed_at = designed_at
        self.to_be_observed_at = to_be_observed_at
        self.is_obsolete = is_obsolete


class pfs_design_fiber(Base):
    '''Pre-operations information for each fiber.
    '''
    __tablename__ = 'pfs_design_fiber'
    __table_args__ = (UniqueConstraint('pfs_design_id', 'fiber_id'), {})

    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'), primary_key=True,
                           autoincrement=False)
    fiber_id = Column(Integer, ForeignKey('cobra_geometry.fiber_id'), primary_key=True, autoincrement=False)
    target_id = Column(BigInteger, ForeignKey('target.target_id'))
    pfi_target_x_mm = Column(REAL, comment='Target x-position on the PFI [mm]')
    pfi_target_y_mm = Column(REAL, comment='Target y-position on the PFI [mm]')
    ets_priority = Column(Integer)
    ets_cost_function = Column(FLOAT)
    ets_cobra_motor_movement = Column(String)
    is_on_source = Column(Boolean)

    pfs_designs = relation(pfs_design, backref=backref('psf_design_fiber'))
    targets = relation(target, backref=backref('psf_design_fiber'))
    fiber_positions = relation(cobra_geometry, backref=backref('psf_design_fiber'))

    def __init__(self, pfs_design_id, fiber_id, target_id,
                 pfi_target_x_mm, pfi_target_y_mm,
                 ets_priority, ets_cost_function, ets_cobra_motor_movement,
                 is_on_source=True):
        self.pfs_design_id = pfs_design_id
        self.fiber_id = fiber_id
        self.target_id = target_id
        self.pfi_target_x_mm = pfi_target_x_mm
        self.pfi_target_y_mm = pfi_target_y_mm
        self.ets_priority = ets_priority
        self.ets_cost_function = ets_cost_function
        self.ets_cobra_motor_movement = ets_cobra_motor_movement
        self.is_on_source = is_on_source


class pfi_visit(Base):
    '''Tracks the Gen2 visit identifier.
    This is the fundamental identifier for all instrument exposures (MCS, AGC, SPS)
    '''
    __tablename__ = 'pfi_visit'

    pfi_visit_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    pfi_visit_description = Column(String)

    def __init__(self, pfi_visit_id, pfi_visit_description):
        self.pfi_visit_id = pfi_visit_id
        self.pfi_visit_description = pfi_visit_description


class mcs_boresight(Base):
    ''' The MCS boresight for a given MCS exposure.
    '''

    __tablename__ = 'mcs_boresight'

    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'), primary_key=True, unique=True,
                          autoincrement=False)
    mcs_boresight_x_pix = Column(REAL)
    mcs_boresight_y_pix = Column(REAL)
    calculated_at = Column(DateTime)

    def __init__(self, pfi_visit_id, mcs_boresight_x_pix, mcs_boresight_y_pix, calculated_at):
        self.pfi_visit_id = pfi_visit_id
        self.mcs_boresight_x_pix = mcs_boresight_x_pix
        self.mcs_boresight_y_pix = mcs_boresight_y_pix
        self.calculated_at = calculated_at


class mcs_exposure(Base):
    ''' Provides instrument and telescope information related to a single MCS exposure.
    '''

    __tablename__ = 'mcs_exposure'

    mcs_frame_id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=False,
                          comment='MCS frame identifier as generated from Gen2')
    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'))
    mcs_exptime = Column(REAL, comment='The exposure time for the frame [sec]')
    altitude = Column(REAL, comment='The telescope attitude [deg]')
    azimuth = Column(REAL, comment='The telescope azimuth [deg]')
    insrot = Column(REAL, comment='The telescope instrument rotation angle [deg]')
    taken_at = Column(DateTime, comment='The time at which the exposure was taken [YYYY-MM-DDThh-mm-sss]')

    def __init__(self, mcs_frame_id, pfi_visit_id, mcs_exptime, altitude, azimuth, insrot, taken_at):
        self.mcs_frame_id = mcs_frame_id
        self.pfi_visit_id = pfi_visit_id
        self.mcs_exptime = mcs_exptime
        self.altitude = altitude
        self.azimuth = azimuth
        self.insrot = insrot
        self.taken_at = taken_at


class mcs_data(Base):
    '''MCS centroiding information.
    Generated by the mcsActor software.
    '''

    __tablename__ = 'mcs_data'
    __table_args__ = (UniqueConstraint('mcs_frame_id', 'spot_id'), {})

    mcs_frame_id = Column(Integer, ForeignKey('mcs_exposure.mcs_frame_id'), primary_key=True, index=True,
                          autoincrement=False)
    spot_id = Column(Integer, primary_key=True, autoincrement=False, comment='The cobra spot identifier')
    mcs_center_x_pix = Column(REAL, comment='The x-center of the spot image in MCS [pix]')
    mcs_center_y_pix = Column(REAL, comment='The y-center of the spot image in MCS [pix]]')
    mcs_second_moment_x_pix = Column(REAL,
                                     comment='The second moment along the x direction '
                                     'of the image in MCS [pix]')
    mcs_second_moment_y_pix = Column(REAL,
                                     comment='The second moment along the y direction '
                                     ' of the image [pix]')
    bgvalue = Column(REAL, comment='The background level')
    peakvalue = Column(REAL, comment='The peak image value')

    def __init__(self, mcs_frame_id, spot_id, mcs_center_x_pix, mcs_center_y_pix,
                 mcs_fwhm_x_pix, mcs_fwhm_y_pix, bgvalue, peakvalue):
        self.mcs_frame_id = mcs_frame_id
        self.spot_id = spot_id
        self.mcs_center_x_pix = mcs_center_x_pix
        self.mcs_center_y_pix = mcs_center_y_pix
        self.mcs_second_moment_x_pix = mcs_fwhm_x_pix
        self.mcs_fwhm_y_pix = mcs_fwhm_y_pix
        self.bgvalue = bgvalue
        self.peakvalue = peakvalue


class pfs_config(Base):
    __tablename__ = 'pfs_config'

    pfs_config_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'))
    visit0 = Column(Integer, comment='The first visit of the set')
    ra_center_config = Column(FLOAT, comment='The right ascension of the PFI center [deg]')
    dec_center_config = Column(FLOAT, comment='The declination of the PFI center [deg]')
    pa_config = Column(REAL, comment='The position angle of the PFI [deg]')
    converg_num_iter = Column(Integer,
                              comment='Allocated total number of cobra iterations towards convergence')
    converg_elapsed_time = Column(REAL,
                                  comment='Allocated time for convergence [sec]')
    alloc_rms_scatter = Column(REAL,
                               comment='[TBW]')
    allocated_at = Column(DateTime, comment='Time at which config was allocated [YYYY-MM-DDhhmmss] (TBC)')
    was_observed = Column(Boolean, comment='True of configuration was observed (XXX relevant?)')

    pfs_designs = relation(pfs_design, backref=backref('pfs_config'))

    def __init__(self, pfs_config_id, pfs_design_id, visit0, ra_center_config, dec_center_config, pa_config,
                 num_sci_allocated, num_cal_allocated, num_sky_allocated, num_guide_stars_allocated,
                 alloc_num_cobra_iter, alloc_elapsed_time, alloc_rms_scatter,
                 allocated_at, was_observed=False):
        self.pfs_config_id = pfs_config_id
        self.pfs_design_id = pfs_design_id
        self.visit0 = visit0
        self.ra_center_config = ra_center_config
        self.dec_center_config = dec_center_config
        self.pa_config = pa_config
        self.num_sci_allocated = num_sci_allocated
        self.num_cal_allocated = num_cal_allocated
        self.num_sky_allocated = num_sky_allocated
        self.num_guide_stars_allocated = num_guide_stars_allocated
        self.converg_num_iter = alloc_num_cobra_iter
        self.converg_elapsed_time = alloc_elapsed_time
        self.alloc_rms_scatter = alloc_rms_scatter
        self.allocated_at = allocated_at
        self.was_observed = was_observed


class pfs_config_fiber(Base):
    __tablename__ = 'pfs_config_fiber'
    __table_args__ = (UniqueConstraint('pfs_config_id', 'fiber_id'),
                      {})

    pfs_config_id = Column(BigInteger, ForeignKey('pfs_config.pfs_config_id'), primary_key=True,
                           autoincrement=False)
    fiber_id = Column(Integer, ForeignKey('cobra_geometry.fiber_id'), primary_key=True, autoincrement=False)
    target_id = Column(BigInteger, ForeignKey('target.target_id'))
    pfi_center_final_x_mm = Column(REAL)
    pfi_center_final_y_mm = Column(REAL)
    motor_map_summary = Column(String)
    config_elapsed_time = Column(REAL)
    is_on_source = Column(Boolean)

    pfs_configs = relation(pfs_config, backref=backref('psf_config_fiber'))
    targets = relation(target, backref=backref('psf_config_fiber'))
    fiber_positions = relation(cobra_geometry, backref=backref('psf_config_fiber'))

    def __init__(self, pfs_config_id, fiber_id, target_id,
                 pfi_center_final_x_mm, pfi_center_final_y_mm,
                 motor_map_summary, config_elapsed_time,
                 is_on_source=True):
        self.pfs_config_id = pfs_config_id
        self.fiber_id = fiber_id
        self.target_id = target_id
        self.motor_map_summary = motor_map_summary
        self.config_elapsed_time = config_elapsed_time
        self.is_on_source = is_on_source


class cobra_motor_axis(Base):
    '''The axis or stage of a cobra motor.
    This can be one of:
    Theta (or Stage 1)
    Phi (or Stage 2)
    '''
    __tablename__ = 'cobra_motor_axis'
    cobra_motor_axis_id = Column(Integer, primary_key=True, comment='Motor axis stage number [1,2]')
    cobra_motor_axis_name = Column(String, comment='Corresponding name for axis [Theta, Phi]')

    def __init__(self, cobra_motor_axis_id, cobra_motor_axis_name):
        self.cobra_motor_axis_id = cobra_motor_axis_id
        self.cobra_motor_axis_name = cobra_motor_axis_name


class cobra_motor_model(Base):
    '''Defines the cobra motor movement profile
    '''
    __tablename__ = 'cobra_motor_model'

    cobra_motor_model_id = Column(Integer, primary_key=True, autoincrement=True)
    fiber_id = Column(Integer, comment='The cobra fiber identifier')
    cobra_motor_axis_id = Column(Integer, ForeignKey('cobra_motor_axis.cobra_motor_axis_id'))
    cobra_motor_angle = Column(REAL, comment='The angle of the motor [deg]')
    cobra_motor_on_time = Column(REAL, comment='The ontime level')
    cobra_motor_speed = Column(REAL, comment='The speed of the motor [deg/s] (TBC)')
    calibrated_at = Column(DateTime,
                           comment='Date at which the model calibration took place [YYYY-MM-DDhh:mm:ss]')

    def __init__(self, cobra_motor_model_id, fiber_id, cobra_motor_axis_id,
                 cobra_motor_angle, cobra_motor_on_time, cobra_motor_speed,
                 calibrated_at
                 ):
        self.cobra_motor_model_id = cobra_motor_model_id
        self.fiber_id = fiber_id
        self.cobra_motor_axis_id = cobra_motor_axis_id
        self.cobra_motor_angle = cobra_motor_angle
        self.cobra_motor_on_time = cobra_motor_on_time
        self.cobra_motor_speed = cobra_motor_speed
        self.calibrated_at = calibrated_at


class cobra_movement(Base):
    ''' The actual movement of the cobra motor, in terms of individual MCS frames.
    '''
    __tablename__ = 'cobra_movement'
    __table_args__ = (UniqueConstraint('mcs_frame_id', 'fiber_id'),
                      {})

    mcs_frame_id = Column(Integer, primary_key=True, index=True, autoincrement=False,
                          comment='MCS frame identifier. Provided by Gen2')
    fiber_id = Column(Integer, primary_key=True, autoincrement=False,
                      comment='Fiber identifier')
    cobra_motor_model_id_theta = Column(Integer, ForeignKey('cobra_motor_model.cobra_motor_model_id'))
    motor_num_step_theta = Column(Integer,
                                  comment='the number of steps the theta motor has undertaken')
    motor_on_time_theta = Column(REAL,
                                 comment='the theta motor ontime value')
    cobra_motor_model_id_phi = Column(Integer, ForeignKey('cobra_motor_model.cobra_motor_model_id'))
    motor_num_step_phi = Column(Integer, comment='the number of steps the phi motor has undertaken')
    motor_on_time_phi = Column(REAL, comment='the phi motor ontime value')

    def __init__(self, mcs_frame_id, fiber_id,
                 cobra_motor_model_id_theta,
                 motor_num_step_theta, motor_on_time_theta,
                 cobra_motor_model_id_phi,
                 motor_num_step_phi, motor_on_time_phi
                 ):
        self.mcs_frame_id = mcs_frame_id
        self.fiber_id = fiber_id
        self.cobra_motor_map_model_id_theta = cobra_motor_model_id_theta
        self.motor_num_step_theta = motor_num_step_theta
        self.motor_on_time_theta = motor_on_time_theta
        self.cobra_motor_map_model_id_phi = cobra_motor_model_id_phi
        self.motor_num_step_phi = motor_num_step_phi
        self.motor_on_time_phi = motor_on_time_phi


class cobra_status(Base):
    '''Defines the status of each cobra at each step during convergence.
    '''
    __tablename__ = 'cobra_config'
    __table_args__ = (UniqueConstraint('mcs_frame_id', 'fiber_id'),
                      ForeignKeyConstraint(['mcs_frame_id', 'spot_id'],
                                           ['mcs_data.mcs_frame_id', 'mcs_data.spot_id']),
                      ForeignKeyConstraint(['mcs_frame_id', 'fiber_id'],
                                           ['cobra_movement.mcs_frame_id',
                                            'cobra_movement.fiber_id']),
                      {})

    mcs_frame_id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=False)
    fiber_id = Column(Integer, primary_key=True, autoincrement=False,
                      comment='Fiber identifier')
    spot_id = Column(Integer, comment='Corresponding MCS image spot identifier ')
    pfs_config_id = Column(BigInteger, ForeignKey('pfs_config.pfs_config_id'))
    iteration = Column(Integer, comment='Iteration number for this frame')
    pfi_target_x_mm = Column(REAL,
                             comment='Target x-position on the PFI as determined from the '
                            ' pfs_design_fiber table [mm]')
    pfi_target_y_mm = Column(REAL,
                             comment='Target y-position on the PFI as determined from the '
                            ' pfs_design_fiber table [mm]')
    pfi_center_x_mm = Column(REAL,
                             comment='Actual x-position on the PFI [mm]')
    pfi_center_y_mm = Column(REAL,
                             comment='Actual y-position on the PFI [mm]')

    def __init__(self, mcs_frame_id, fiber_id,
                 pfs_config_id, spot_id, iteration,
                 pfi_nominal_x_mm, pfi_nominal_y_mm, pfi_center_x_mm, pfi_center_y_mm
                 ):
        self.mcs_frame_id = mcs_frame_id
        self.fiber_id = fiber_id
        self.spot_id = spot_id
        self.pfs_config_id = pfs_config_id
        self.iteration = iteration
        self.pfi_target_x_mm = pfi_nominal_x_mm
        self.pfi_target_y_mm = pfi_nominal_y_mm
        self.pfi_center_x_mm = pfi_center_x_mm
        self.pfi_center_y_mm = pfi_center_y_mm


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
    ra_tel = Column(REAL)
    dec_tel = Column(REAL)
    beam_switch_mode_id = Column(Integer, ForeignKey('beam_switch_mode.beam_switch_mode_id'))
    beam_switch_offset_ra = Column(REAL)
    beam_switch_offset_dec = Column(REAL)

    def __init__(self, tel_visit_id,
                 pfs_config_id, ra_tel, dec_tel,
                 beam_switch_mode_id, beam_switch_offset_ra, beam_switch_offset_dec
                 ):
        self.tel_visit_id = tel_visit_id
        self.pfs_config_id = pfs_config_id
        self.ra_tel = ra_tel
        self.dec_tel = dec_tel
        self.beam_switch_mode_id = beam_switch_mode_id
        self.beam_switch_offset_ra = beam_switch_offset_ra
        self.beam_switch_offset_dec = beam_switch_offset_dec


class tel_condition(Base):
    __tablename__ = 'tel_condition'

    tel_visit_id = Column(Integer, ForeignKey('tel_visit.tel_visit_id'), primary_key=True, unique=True,
                          autoincrement=False)
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

    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'), primary_key=True, unique=True,
                          autoincrement=False)
    spectrograph_id = Column(Integer, ForeignKey('spectrograph.spectrograph_id'))
    sps_exptime = Column(REAL, comment='Exposure time for visit [sec]')
    is_medium_resolution = Column(Boolean,
                                  comment='Flag to indicate whether visit '
                                  'includes the medium resolution filter')
    time_exp_start = Column(DateTime, comment='Start time for exposure [YYYY-MM-DDThh:mm:ss]')
    time_exp_end = Column(DateTime, comment='End time for exposure [YYYY-MM-DDThh:mm:ss]')
    mjd_exp_start = Column(REAL, comment='Start time for exposure in MJD')
    mjd_exp_end = Column(REAL, comment='End time for exposure in MJD')
    insrot_start = Column(REAL, comment='The start instrument rotation position [deg]')
    insrot_end = Column(REAL, comment='The end instrument rotation position [deg]')

    def __init__(self, pfi_visit_id, spectrograph_id,
                 sps_exptime,
                 time_exp_start, time_exp_end, mjd_exp_start, mjd_exp_end,
                 insrot_start, insrot_end,
                 is_medium_resolution=False
                 ):
        self.pfi_visit_id = pfi_visit_id
        self.spectrograph_id = spectrograph_id
        self.sps_exptime = sps_exptime
        self.is_medium_resolution = is_medium_resolution
        self.time_exp_start = time_exp_start
        self.time_exp_end = time_exp_end
        self.mjd_exp_start = mjd_exp_start
        self.mjd_exp_end = mjd_exp_end
        self.insrot_start = insrot_start
        self.insrot_end = insrot_end


class sps_condition(Base):
    __tablename__ = 'sps_condition'

    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'), primary_key=True, unique=True,
                          autoincrement=False)
    background = Column(REAL)
    throughput = Column(REAL)

    def __init__(self, pfi_visit_id,
                 background, throughput,
                 ):
        self.pfi_visit_id = pfi_visit_id
        self.background = background
        self.throughput = throughput


class calib(Base):
    __tablename__ = 'calib'

    calib_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    calib_type = Column(String)
    sps_frames_to_use = Column(String)
    pfs_config_id = Column(BigInteger, ForeignKey('pfs_config.pfs_config_id'))
    calib_date = Column(DateTime)

    def __init__(self, calib_id, calib_type, sps_frames_to_use, pfs_config_id, calib_date):
        self.calib_id = calib_id
        self.calib_type = calib_type
        self.sps_frames_to_use = sps_frames_to_use
        self.pfs_config_id = pfs_config_id
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
    __table_args__ = (UniqueConstraint('pfi_visit_id', 'fiber_id'), {})

    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'), primary_key=True, unique=True,
                          autoincrement=False)
    fiber_id = Column(Integer, ForeignKey('cobra_geometry.fiber_id'), primary_key=True,
                      autoincrement=False)
    target_id = Column(BigInteger)
    exptime = Column(REAL)
    cum_nexp = Column(Integer)
    cum_texp = Column(REAL)

    sps_exposures = relation(sps_exposure, backref=backref('obs_fiber'))
    fiber_positions = relation(cobra_geometry, backref=backref('obs_fiber'))

    def __init__(self, pfi_visit_id, fiber_id, target_id,
                 exptime, cum_nexp, cum_texp):
        self.pfi_visit_id = pfi_visit_id
        self.fiber_id = fiber_id
        self.target_id = target_id
        self.exptime = exptime
        self.cum_nexp = cum_nexp
        self.cum_texp = cum_texp


class sky_model(Base):
    __tablename__ = 'sky_model'

    sky_model_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'))
    tel_visit_id = Column(Integer)
    spectrograph_id = Column(Integer, ForeignKey('spectrograph.spectrograph_id'))

    sps_exposures = relation(sps_exposure, backref=backref('sky_model'))
    spectrographs = relation(spectrograph, backref=backref('sky_model'))

    def __init__(self, sky_model_id, pfi_visit_id, tel_visit_id, spectrograph_id):
        self.sky_model_id = sky_model_id
        self.pfi_visit_id = pfi_visit_id
        self.tel_visit_id = tel_visit_id
        self.spectrograph_id = spectrograph_id


class psf_model(Base):
    __tablename__ = 'psf_model'

    psf_model_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'))
    tel_visit_id = Column(Integer)
    spectrograph_id = Column(Integer, ForeignKey('spectrograph.spectrograph_id'))

    sps_exposures = relation(sps_exposure, backref=backref('psf_model'))
    spectrographs = relation(spectrograph, backref=backref('psf_model'))

    def __init__(self, psf_model_id, pfi_visit_id, tel_visit_id, spectrograph_id):
        self.psf_model_id = psf_model_id
        self.pfi_visit_id = pfi_visit_id
        self.tel_visit_id = tel_visit_id
        self.spectrograph_id = spectrograph_id


class pfs_arm(Base):
    __tablename__ = 'pfs_arm'

    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'), primary_key=True, unique=True,
                          autoincrement=False)
    calib_set_id = Column(Integer, ForeignKey('calib_set.calib_set_id'))
    sky_model_id = Column(Integer, ForeignKey('sky_model.sky_model_id'))
    psf_model_id = Column(Integer, ForeignKey('psf_model.psf_model_id'))
    flags = Column(Integer)
    processed_at = Column(DateTime)
    drp2d_version = Column(String)

    calib_sets = relation(calib_set, backref=backref('pfs_arm'))
    sps_exposures = relation(sps_exposure, backref=backref('pfs_arm'))
    sky_models = relation(sky_model, backref=backref('pfs_arm'))
    psf_models = relation(psf_model, backref=backref('pfs_arm'))

    def __init__(self, pfi_visit_id,
                 calib_set_id, sky_model_id, psf_model_id, flags,
                 processed_at, drp2d_version):
        self.pfi_visit_id = pfi_visit_id
        self.calib_set_id = calib_set_id
        self.sky_model_id = sky_model_id
        self.psf_model_id = psf_model_id
        self.flags = flags
        self.processed_at = processed_at
        self.drp2d_version = drp2d_version


class pfs_arm_obj(Base):
    __tablename__ = 'pfs_arm_obj'
    __table_args__ = (UniqueConstraint('pfi_visit_id', 'fiber_id'), {})

    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'),
                          primary_key=True, autoincrement=False)
    fiber_id = Column(Integer, ForeignKey('cobra_geometry.fiber_id'), primary_key=True, autoincrement=False)
    flags = Column(Integer)
    qa_type_id = Column(Integer, ForeignKey('qa_type.qa_type_id'))
    qa_value = Column(REAL)

    pfs_arms = relation(pfs_arm, backref=backref('pfs_arm_obj'))
    fiber_positions = relation(cobra_geometry, backref=backref('pfs_arm_obj'))
    qa_types = relation(qa_type, backref=backref('pfs_arm_obj'))

    def __init__(self, pfi_visit_id, fiber_id, flags, qa_type_id, qa_value):
        self.pfi_visit_id = pfi_visit_id
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
    processed_at = Column(DateTime)
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
                 cum_texp, processed_at, drp2d_version, flux_calib_id, flags, qa_type_id, qa_value):
        self.pfs_object_id = pfs_object_id
        self.target_id = target_id
        self.tract = tract
        self.patch = patch
        self.cat_id = cat_id
        self.obj_id = obj_id
        self.n_visit = n_visit
        self.pfs_visit_hash = pfs_visit_hash
        self.cum_texp = cum_texp
        self.processed_at = processed_at
        self.drp2d_version = drp2d_version
        self.flux_calib_id = flux_calib_id
        self.flags = flags
        self.qa_type_id = qa_type_id
        self.qa_value = qa_value


class visits_to_combine(Base):
    __tablename__ = 'visits_to_combine'
    __table_args__ = (UniqueConstraint('tel_visit_id', 'pfs_visit_hash'), {})

    tel_visit_id = Column(Integer, ForeignKey('tel_visit.tel_visit_id'), primary_key=True,
                          autoincrement=False)
    pfs_visit_hash = Column(BigInteger, ForeignKey('visit_hash.pfs_visit_hash'), primary_key=True,
                            autoincrement=False)

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
    __table_args__ = (UniqueConstraint('pfs_object_id', 'processed_at'), {})

    pfs_object_id = Column(BigInteger, ForeignKey('pfs_object.pfs_object_id'), primary_key=True,
                           autoincrement=False)
    z_best = Column(REAL)
    z_best_err = Column(REAL)
    z_best_reliability = Column(REAL)
    obj_type_id = Column(Integer, ForeignKey('obj_type.obj_type_id'))
    flags = Column(Integer)
    processed_at = Column(DateTime, primary_key=True, autoincrement=False)
    drp1d_version = Column(String)

    def __init__(self, pfs_object_id, z_best, z_best_err, z_best_reliability,
                 obj_type_id, flags, processed_at, drp1d_version):
        self.pfs_object_id = pfs_object_id
        self.z_best = z_best
        self.z_best_err = z_best_err
        self.z_best_reliability = z_best_reliability
        self.obj_type_id = obj_type_id
        self.flags = flags
        self.processed_at = processed_at
        self.drp1d_version = drp1d_version


class drp1d_redshift(Base):
    __tablename__ = 'drp1d_redshift'
    __table_args__ = (UniqueConstraint('pfs_object_id', 'processed_at'),
                      ForeignKeyConstraint(['pfs_object_id', 'processed_at'],
                                           ['drp1d.pfs_object_id', 'drp1d.processed_at']),
                      {})

    pfs_object_id = Column(BigInteger, primary_key=True, autoincrement=False)
    z = Column(REAL)
    z_err = Column(REAL)
    zrank = Column(REAL)
    reliability = Column(REAL)
    spec_class = Column(String)
    spec_subclass = Column(String)
    processed_at = Column(DateTime, primary_key=True, autoincrement=False)

    def __init__(self, pfs_object_id, z, z_err, zrank, reliability, spec_class, spec_subclass, processed_at):
        self.pfs_object_id = pfs_object_id
        self.z = z
        self.z_err = z_err
        self.zrank = zrank
        self.reliability = reliability
        self.spec_class = spec_class
        self.spec_subclass = spec_subclass
        self.processed_at = processed_at


class drp1d_line(Base):
    __tablename__ = 'drp1d_line'
    __table_args__ = (UniqueConstraint('pfs_object_id', 'line_id'), {})
    __table_args__ = (UniqueConstraint('pfs_object_id', 'processed_at', 'line_id'),
                      ForeignKeyConstraint(['pfs_object_id', 'processed_at'],
                                           ['drp1d.pfs_object_id', 'drp1d.processed_at']),
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
    processed_at = Column(DateTime, primary_key=True, autoincrement=False)

    def __init__(self, pfs_object_id, drp1d_id, line_id,
                 line_name, line_wave, line_z, line_z_err, line_sigma,
                 line_sigma_err, line_vel, line_vel_err, line_flux, line_flux_err, line_ew, line_ew_err,
                 line_cont_level, line_cont_level_err, processed_at):
        self.pfs_object_id = pfs_object_id
        self.drp1d_id = drp1d_id
        self.line_id = line_id
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
        self.processed_at = processed_at


class drp_ga(Base):
    __tablename__ = 'drp_ga'
    __table_args__ = (UniqueConstraint('pfs_object_id', 'processed_at'), {})

    pfs_object_id = Column(BigInteger, ForeignKey('pfs_object.pfs_object_id'), primary_key=True,
                           autoincrement=False)
    star_type_id = Column(Integer, ForeignKey('star_type.star_type_id'))
    velocity = Column(REAL)
    metallicity = Column(REAL)
    logg = Column(REAL)
    teff = Column(REAL)
    flags = Column(Integer)
    processed_at = Column(DateTime, primary_key=True, autoincrement=False)
    drp_ga_version = Column(String)

    def __init__(self, pfs_object_id, star_type_id, velocity, metallicity, logg, teff,
                 flags, processed_at, drp_ga_version):
        self.pfs_object_id = pfs_object_id
        self.star_type_id = star_type_id
        self.velocity = velocity
        self.metallicity = metallicity
        self.logg = logg
        self.teff = teff
        self.flags = flags
        self.processed_at = processed_at
        self.drp_ga_version = drp_ga_version


class visit_set(Base):
    __tablename__ = 'visit_set'
   
    visit_set_id = Column(Integer, primary_key=True, autoincrement=False, comment='visit set identifier')
    name = Column(String, comment='The unique name assigned to this set of visits')
    cmd_str = Column(String, comment='ICS command string that generates exposures for this set of visits')

    def __init__(self, visit_set_id):
        self.visit_set_id = visit_set_id


class sps_visit(Base):
    __tablename__ = 'sps_visit'

    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'), primary_key=True, unique=True,
                          autoincrement=False)
    visit_set_id = Column(Integer, ForeignKey('visit_set.visit_set_id'))
    visit_type = Column(String, comment='Type of visit: BIAS, FLAT, DFLAT etc.')

    def __init__(self, pfi_visit_id, visit_set_id, visit_type):
        self.pfi_visit_id = pfi_visit_id
        self.visit_set_id = visit_set_id
        self.visit_type = visit_type


class sps_annotation(Base):
    __tablename__ = 'sps_annotation'

    sps_annotation_id = Column(Integer, primary_key=True, autoincrement=False,
                               comment='Unique identifier for this annotation')
    visit_set_id = Column(Integer, ForeignKey('visit_set.visit_set_id'))
    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'))
    comment = Column(String)
    anomaly = Column(String)

    def __init__(self, annotation_id, visit_set_id, pfi_visit_id, comment, anomaly):
        self.sps_annotation_id = annotation_id
        self.visit_set_id = visit_set_id
        self.pfi_visit_id = pfi_visit_id
        self.comment = comment
        self.anomaly = anomaly


class sps_camera(Base):
    __tablename__ = 'sps_camera'

    sps_camera_id = Column(Integer, primary_key=True, autoincrement=False)
    visit_set_id = Column(Integer, ForeignKey('visit_set.visit_set_id'))
    sps_module = Column(Integer, comment='SPS module identifier [1-4]')
    sps_arm_id = Column(String, comment='Spectrogram arm identifier [B, R, N, M]')

    def __init__(self, camera_id, visit_set_id, sps_module, sps_arm_id):
        self.sps_camera_id = camera_id
        self.visit_set_id = visit_set_id
        self.sps_module = sps_module
        self.sps_arm_id = sps_arm_id


class processing_status(Base):
    __tablename__ = 'processing_status'

    status_id = Column(Integer, primary_key=True, autoincrement=False,
                       comment='Unique processing status identifier')
    visit_set_id = Column(Integer, ForeignKey('visit_set.visit_set_id'))
    pfi_visit_id = Column(Integer, ForeignKey('pfi_visit.pfi_visit_id'))
    data_ok = Column(Boolean)

    def __init__(self, status_id, visit_set_id, pfi_visit_id, data_ok):
        self.status_id = status_id
        self.visit_set_id = visit_set_id
        self.pfi_visit_id = pfi_visit_id
        self.data_ok = data_ok


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
    Session()


if __name__ == '__main__':
    import sys
    dbinfo = sys.argv[1]
    print(dbinfo)
    make_database(dbinfo)
