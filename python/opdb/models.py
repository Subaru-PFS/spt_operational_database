from sqlalchemy import create_engine
from sqlalchemy import Column, BigInteger, Integer, String, FLOAT, ForeignKey, DateTime, Boolean, REAL, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql.schema import PrimaryKeyConstraint

Base = declarative_base()


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


class cobra(Base):
    '''
        Very basic information on cobra
    '''
    __tablename__ = 'cobra'

    cobra_id = Column(Integer, primary_key=True, unique=True, autoincrement=False,
                      comment='Cobra identifier (1..2394). There is one of these for each science fiber.')
    field_on_pfi = Column(Integer, comment='Field (1..3).')
    cobra_in_field = Column(Integer, comment='Cobra-in-field (1..798). cf = 57*(mf-1)+cm.')
    cobra_module_id = Column(Integer, comment='Cobra module id (1..42)')
    module_in_field = Column(
        Integer, comment='Module-in-field (1..14). The number of the module within the field, with 1 at the center of the PFI.')
    cobra_in_module = Column(
        Integer, comment='Cobra-in-module (1..57). 1 is the bottom-left cobra in a module when looked at with the wide (29-cobra) board down. Increasing as you move across the module.')
    cobra_in_board = Column(Integer, comment='Cobra-in-board (1..29). Each board has either 29 or 28 cobras.')
    cobra_board_id = Column(Integer, comment='Cobra board id (1..84). One Cobra module has two boards.')
    mtp = Column(String(
        3), comment='Cobra module id associated with MTP ferrule. There are 84 of these, numbered 1 through 42 with A and B suffixes. (e.g.,13B)')
    sps_module_id = Column(Integer, comment='Spectrograph that the cobra feeds (1..4)')
    sps_slit_hole = Column(
        Integer, comment='Fiber hole (1..651). This is the position in the spectrograph slit head.')
    science_fiber_id = Column(
        Integer, comment=' Science fiber (1..2394). This is a unique identifier for each science fiber.')
    fiber_id = Column(
        Integer, comment='The fiber identifier (1..2604). This is a unique identifier for each fiber (both science and engineering). fiberId = 651*(sp-1)+fh.')
    sunss_id = Column(
        String(4), comment='SuNSS fiber id. ID consists of fiber number and mode (i is imaging, and d is diffuse).')
    mtp_a_id = Column(
        String(), comment='Identifier of the USCONNEC connector hole at the Cable B-C interface. MTP = A)')
    mtp_c_id = Column(
        String(), comment='Identifier of the USCONNEC connector hole at the Cable B-C interface. MTP = C)')
    mtp_ba_id = Column(
        String(), comment='Identifier of the USCONNEC connector hole at the Cable B-C interface. MTP = BA)')
    mtp_bc_id = Column(
        String(), comment='Identifier of the USCONNEC connector hole at the Cable B-C interface. MTP = BC)')
    version = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, cobra_id, field_on_pfi, cobra_in_field, cobra_module_id,
                 module_in_field, cobra_in_module, cobra_in_board, cobra_board_id,
                 mtp, sps_module_id, sps_slit_hole, science_fiber_id, fiber_id,
                 sunss_id, mtp_a_id, mtp_c_id, mtp_ba_id, mtp_bc_id,
                 version, created_at, updated_at):
        self.cobra_id = cobra_id
        self.field_on_pfi = field_on_pfi
        self.cobra_in_field = cobra_in_field
        self.cobra_module_id = cobra_module_id
        self.module_in_field = module_in_field
        self.cobra_in_module = cobra_in_module
        self.cobra_in_board = cobra_in_board
        self.cobra_board_id = cobra_board_id
        self.mtp = mtp
        self.sps_module_id = sps_module_id
        self.sps_slit_hole = sps_slit_hole
        self.science_fiber_id = science_fiber_id
        self.fiber_id = fiber_id
        self.sunss_id = sunss_id
        self.mtp_a_id = mtp_a_id
        self.mtp_c_id = mtp_c_id
        self.mtp_ba_id = mtp_ba_id
        self.mtp_bc_id = mtp_bc_id
        self.version = version
        self.created_at = created_at
        self.updated_at = updated_at


class cobra_geometry(Base):
    __tablename__ = 'cobra_geometry'
    __table_args__ = (UniqueConstraint('cobra_geometry_calib_id', 'cobra_id'),
                      {})

    cobra_geometry_calib_id = Column(Integer, ForeignKey('cobra_geometry_calib.cobra_geometry_calib_id'),
                                     primary_key=True, autoincrement=False)
    cobra_id = Column(Integer, ForeignKey('cobra.cobra_id'),
                      primary_key=True, autoincrement=False)
    center_x_mm = Column(REAL)
    center_y_mm = Column(REAL)
    motor_theta_limit0 = Column(REAL)
    motor_theta_limit1 = Column(REAL)
    motor_theta_length_mm = Column(REAL)
    motor_phi_limit_in = Column(REAL)
    motor_phi_limit_out = Column(REAL)
    motor_phi_length_mm = Column(REAL)
    status = Column(Integer,
                    comment='0x0001=OK/0x0002=INVISIBLE/0x0004=BROKEN_THETA/0x0008=BROKEN_PHI')

    def __init__(self, cobra_id,
                 center_x_mm, center_y_mm,
                 motor_theta_limit0, motor_theta_limit1, motor_theta_length_mm,
                 motor_phi_limit_in, motor_phi_limit_out, motor_phi_length_mm,
                 status
                 ):
        self.cobra_id = cobra_id
        self.center_x_mm = center_x_mm
        self.center_y_mm = center_y_mm
        self.motor_theta_limit0 = motor_theta_limit0
        self.motor_theta_limit1 = motor_theta_limit1
        self.motor_theta_length_mm = motor_theta_length_mm
        self.motor_phi_limit_in = motor_phi_limit_in
        self.motor_phi_limit_out = motor_phi_limit_out
        self.motor_phi_length_mm = motor_phi_length_mm
        self.status = status


class fiducial_fiber(Base):
    __tablename__ = 'fiducial_fiber'

    fiducial_fiber_id = Column(Integer, primary_key=True, autoincrement=False)
    field_on_pfi = Column(Integer)   # 1-3
    ff_in_field = Column(Integer)    # 1-32
    ff_type = Column(String(5))      # spoke/edge/agfid
    ff_id_in_type = Column(Integer)  # 1-14 for spoke, 1-14 for edge, 1-4 for agfid
    mask = Column(Integer)           # bit mask for FF status
    version = Column(String)

    def __init__(self, fiducial_fiber_id, field_on_pfi, ff_in_field, ff_type, ff_id_in_type, mask, version):
        self.fiducial_fiber_id = fiducial_fiber_id
        self.field_on_pfi = field_on_pfi
        self.ff_in_field = ff_in_field
        self.ff_type = ff_type
        self.ff_id_in_type = ff_id_in_type
        self.mask = mask
        self.version = version


class fiducial_fiber_calib(Base):
    '''Defines the fiducial fiber calibration profile
    '''
    __tablename__ = 'fiducial_fiber_calib'

    fiducial_fiber_calib_id = Column(Integer, primary_key=True, autoincrement=True)
    calibrated_at = Column(DateTime,
                           comment='Date of the calibration [YYYY-MM-DDhh:mm:ss]')
    comments = Column(String, comment='Comments')

    def __init__(self, calibrated_at, comments):
        self.calibrated_at = calibrated_at
        self.comments = comments


class fiducial_fiber_geometry(Base):
    __tablename__ = 'fiducial_fiber_geometry'
    __table_args__ = (UniqueConstraint('fiducial_fiber_id', 'fiducial_fiber_calib_id'),
                      {})

    fiducial_fiber_id = Column(Integer, ForeignKey(
        'fiducial_fiber.fiducial_fiber_id'), primary_key=True, autoincrement=False)
    fiducial_fiber_calib_id = Column(Integer, ForeignKey(
        'fiducial_fiber_calib.fiducial_fiber_calib_id'), primary_key=True, autoincrement=False)
    ff_center_on_pfi_x_mm = Column(REAL)
    ff_center_on_pfi_y_mm = Column(REAL)
    elevation = Column(REAL, comment='Elevation')
    ambient_temp = Column(REAL, comment='Ambient temperature')

    def __init__(self, fiducial_fiber_id, fiducial_fiber_calib_id,
                 ff_center_on_pfi_x_mm, ff_center_on_pfi_y_mm,
                 elevation, ambient_temp
                 ):
        self.fiducial_fiber_id = fiducial_fiber_id
        self.fiducial_fiber_calib_id = fiducial_fiber_calib_id
        self.ff_center_on_pfi_x_mm = ff_center_on_pfi_x_mm
        self.ff_center_on_pfi_y_mm = ff_center_on_pfi_y_mm
        self.elevation = elevation
        self.ambient_temp = ambient_temp


class guide_stars(Base):
    __tablename__ = 'guide_stars'

    guide_star_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    ra = Column(FLOAT)
    decl = Column(FLOAT)
    cat_id = Column(Integer, ForeignKey('input_catalog.cat_id'))
    obj_type_id = Column(Integer)
    mag_agc = Column(REAL)
    flux_agc = Column(REAL)
    flags = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    input_catalogs = relationship(input_catalog, backref=backref('guide_stars'))

    def __init__(self, guide_star_id, ra, decl, cat_id, obj_type_id,
                 mag_agc, flux_agc, flags, created_at, updated_at):
        self.guide_star_id = guide_star_id
        self.ra = ra
        self.decl = decl
        self.cat_id = cat_id
        self.obj_type_id = obj_type_id
        self.mag_agc = mag_agc
        self.flux_agc = flux_agc
        self.flags = flags
        self.created_at = created_at
        self.updated_at = updated_at


class pfs_design(Base):
    __tablename__ = 'pfs_design'

    pfs_design_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    design_name = Column(String, comment='Human-readable name for the design (designName)')
    variant = Column(
        Integer, comment='Counter of which variant of `designId0` we are. Requires `designId0`', nullable=False)
    design_id0 = Column(
        BigInteger, comment='pfsDesignId of the pfsDesign we are a variant of. Requires `variant`', nullable=False)
    tile_id = Column(Integer)
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
    to_be_observed_at = Column(DateTime, comment='Planned observation time creating the pfsDesign')
    pfs_utils_version = Column(String, comment='pfs_utils version creating the pfsDesign')
    is_obsolete = Column(Boolean)

    pfs_design_agcs = relationship('pfs_design_agc', back_populates='pfs_design')
    pfs_design_fibers = relationship('pfs_design_fiber', back_populates='pfs_design')

    def __init__(self, pfs_design_id, design_name, variant, design_id0,
                 tile_id, ra_center_designed, dec_center_designed, pa_designed,
                 num_sci_designed, num_cal_designed, num_sky_designed, num_guide_stars,
                 exptime_tot, exptime_min, ets_version, ets_assigner, designed_at, to_be_observed_at,
                 pfs_utils_version, is_obsolete=False):
        self.pfs_design_id = pfs_design_id
        self.design_name = design_name
        self.variant = variant
        self.design_id0 = design_id0
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
        self.pfs_utils_version = pfs_utils_version
        self.is_obsolete = is_obsolete


class pfs_design_fiber(Base):
    '''Pre-operations information for each fiber.
    '''
    __tablename__ = 'pfs_design_fiber'
    __table_args__ = (UniqueConstraint('pfs_design_id', 'fiber_id'), {})

    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'), primary_key=True,
                           autoincrement=False)
    fiber_id = Column(Integer, primary_key=True, autoincrement=False)
    target_cat_id = Column(Integer, comment='catId of the target')
    target_tract = Column(Integer, comment='tract of the target')
    target_patch = Column(String, comment='patch of the target')
    target_obj_id = Column(BigInteger, comment='objId of the target')
    target_ra = Column(FLOAT, comment='R.A. of the target')
    target_dec = Column(FLOAT, comment='Dec. of the target')
    target_pm_ra = Column(REAL, comment='Proper motion of the target in R.A. [mas/yr]')
    target_pm_dec = Column(REAL, comment='Proper motion of the target in Dec. [mas/yr]')
    target_parallax = Column(REAL, comment='Parallax of the target [mas]')
    epoch = Column(String, comment='epoch')
    proposal_id = Column(String, comment='Proposal ID')
    ob_code = Column(String, comment='OB code')
    target_type = Column(Integer, comment='targetType: enumerated e.g. SCIENCE,SKY,FLUXSTD')
    fiber_status = Column(Integer, comment='fiberStatus: enumerated e.g. GOOD,BROKENFIBER,BLOCKED,BLACKSPOT')
    pfi_nominal_x_mm = Column(REAL, comment='Nominal x-position on the PFI [mm]')
    pfi_nominal_y_mm = Column(REAL, comment='Nominal y-position on the PFI [mm]')
    ets_priority = Column(Integer)
    ets_cost_function = Column(FLOAT)
    ets_cobra_motor_movement = Column(String)
    is_on_source = Column(Boolean)
    comments = Column(String, comment='comments')

    pfs_design = relationship('pfs_design', back_populates='pfs_design_fibers')

    def __init__(self, pfs_design_id, fiber_id,
                 target_cat_id, target_tract, target_patch, target_obj_id,
                 target_ra, target_dec,
                 target_pm_ra, target_pm_dec, target_parallax, epoch,
                 proposal_id, ob_code,
                 target_type, fiber_status,
                 pfi_nominal_x_mm, pfi_nominal_y_mm,
                 ets_priority, ets_cost_function, ets_cobra_motor_movement,
                 is_on_source, comments):
        self.pfs_design_id = pfs_design_id
        self.fiber_id = fiber_id
        self.target_cat_id = target_cat_id
        self.target_tract = target_tract
        self.target_patch = target_patch
        self.target_obj_id = target_obj_id
        self.target_ra = target_ra
        self.target_dec = target_dec
        self.target_pm_ra = target_pm_ra
        self.target_pm_dec = target_pm_dec
        self.target_parallax = target_parallax
        self.epoch = epoch
        self.proposal_id = proposal_id
        self.ob_code = ob_code
        self.target_type = target_type
        self.fiber_status = fiber_status
        self.pfi_nominal_x_mm = pfi_nominal_x_mm
        self.pfi_nominal_y_mm = pfi_nominal_y_mm
        self.ets_priority = ets_priority
        self.ets_cost_function = ets_cost_function
        self.ets_cobra_motor_movement = ets_cobra_motor_movement
        self.is_on_source = is_on_source
        self.comments = comments


class pfs_design_agc(Base):
    '''Pre-operations information for AGC.
    '''
    __tablename__ = 'pfs_design_agc'
    __table_args__ = (UniqueConstraint('pfs_design_id', 'guide_star_id'), {})

    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'),
                           primary_key=True, autoincrement=False
                           )
    guide_star_id = Column(BigInteger,
                           primary_key=True, autoincrement=False,
                           comment='GuideStar identifier'
                           )
    epoch = Column(String, comment='epoch')
    guide_star_ra = Column(FLOAT, comment='GuideStar R.A. [deg.]')
    guide_star_dec = Column(FLOAT, comment='GuideStar Dec. [deg.]')
    guide_star_pm_ra = Column(REAL, comment='GuideStar proper motion in R.A. [mas/yr]')
    guide_star_pm_dec = Column(REAL, comment='GuideStar proper motion in Dec. [mas/yr]')
    guide_star_parallax = Column(REAL, comment='GuideStar parallax [mas]')
    guide_star_magnitude = Column(REAL, comment='GuideStar magnitude [mag]')
    passband = Column(String, comment='passband')
    guide_star_color = Column(REAL, comment='GuideStar color [mag]')
    guide_star_flag = Column(Integer, comment='GuideStar catalog flag')
    agc_camera_id = Column(Integer, comment='AGC camera identifier')
    agc_target_x_pix = Column(REAL, comment='Target x-position on the AGC [pix]')
    agc_target_y_pix = Column(REAL, comment='Target y-position on the AGC [pix]')
    comments = Column(String, comment='comments')

    pfs_design = relationship('pfs_design', back_populates='pfs_design_agcs')

    def __init__(self, pfs_design_id, guide_star_id,
                 epoch, guide_star_ra, guide_star_dec, guide_star_pm_ra, guide_star_pm_dec,
                 guide_star_parallax, guide_star_magnitude, passband, guide_star_color, guide_star_flag,
                 agc_camera_id, agc_target_x_pix, agc_target_y_pix, comments):
        self.pfs_design_id = pfs_design_id
        self.guide_star_id = guide_star_id
        self.epoch = epoch
        self.guide_star_ra = guide_star_ra
        self.guide_star_dec = guide_star_dec
        self.guide_star_pm_ra = guide_star_pm_ra
        self.guide_star_pm_dec = guide_star_pm_dec
        self.guide_star_parallax = guide_star_parallax
        self.guide_star_magnitude = guide_star_magnitude
        self.passband = passband
        self.guide_star_color = guide_star_color
        self.guide_star_flag = guide_star_flag
        self.agc_camera_id = agc_camera_id
        self.agc_target_x_pix = agc_target_x_pix
        self.agc_target_y_pix = agc_target_y_pix
        self.comments = comments


class pfs_visit(Base):
    '''Tracks the Gen2 visit identifier.
    This is the fundamental identifier for all instrument exposures (MCS, AGC, SPS)
    '''
    __tablename__ = 'pfs_visit'

    pfs_visit_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    pfs_visit_description = Column(String)
    pfs_design_id = Column(BigInteger)
    issued_at = Column(DateTime, comment='Issued time [YYYY-MM-DDThh:mm:ss]')

    sps_visit = relationship('sps_visit', uselist=False, back_populates='pfs_visit')
    mcs_exposure = relationship('mcs_exposure', back_populates='pfs_visit')
    visit_set = relationship('visit_set', back_populates='pfs_visit', uselist=False)
    obslog_notes = relationship('obslog_visit_note')
    agc_exposure = relationship('agc_exposure', back_populates='pfs_visit')
    tel_status = relationship('tel_status', back_populates='pfs_visit')
    pfs_config_sps = relationship('pfs_config_sps', back_populates='pfs_visit', uselist=False)

    def __init__(self, pfs_visit_id, pfs_visit_description, pfs_design_id, issued_at):
        self.pfs_visit_id = pfs_visit_id
        self.pfs_visit_description = pfs_visit_description
        self.pfs_design_id = pfs_design_id
        self.issued_at = issued_at


class tel_status(Base):
    '''Tracks the telescope status.
    '''
    __tablename__ = 'tel_status'
    __table_args__ = (UniqueConstraint('pfs_visit_id', 'status_sequence_id'),
                      {})

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=False, autoincrement=False)
    status_sequence_id = Column(Integer, primary_key=True, unique=False, autoincrement=False,
                                comment='Gen2 status sequence')
    altitude = Column(REAL, comment='The telescope altitude [deg]')
    azimuth = Column(REAL, comment='The telescope azimuth [deg]')
    insrot = Column(REAL, comment='The telescope instrument rotation angle [deg]')
    inst_pa = Column(REAL, comment='The INST_PA at which the exposure started [deg]')
    adc_pa = Column(REAL, comment='ADC PA at which the exposure started [deg]')
    m2_pos3 = Column(REAL, comment='Hexapod position [mm]')
    m2_off3 = Column(REAL, comment='Hexapod focus offset [mm]')
    tel_ra = Column(REAL, comment='The telescope target R.A. [deg]')
    tel_dec = Column(REAL, comment='The telescope target Dec. [deg]')
    dither_ra = Column(REAL, comment='Offset to the R.A. coordinate [arcsec]')
    dither_dec = Column(REAL, comment='Offset to the DEC. coordinate [arcsec]')
    dither_pa = Column(REAL, comment='Offset to the INST_PA [arcsec]')
    dome_shutter_status = Column(Integer, comment='Dome slit status (open/close/unknown)')
    dome_light_status = Column(Integer, comment='Dome (room) light mask interger')
    caller = Column(String, comment='Which sub-system calls (e.g., mcs, agcc, etc.)')
    created_at = Column(DateTime, index=True,
                        comment='Issued time [YYYY-MM-DDThh:mm:ss]')

    pfs_visit = relationship('pfs_visit', back_populates='tel_status')

    def __init__(self, pfs_visit_id, status_sequence_id,
                 altitude, azimuth, insrot, inst_pa, adc_pa, m2_pos3, m2_off3,
                 tel_ra, tel_dec, dither_ra, dither_dec, dither_pa,
                 dome_shutter_status, dome_light_status, caller,
                 created_at
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.status_sequence_id = status_sequence_id
        self.altitude = altitude
        self.azimuth = azimuth
        self.insrot = insrot
        self.inst_pa = inst_pa
        self.adc_pa = adc_pa
        self.m2_pos3 = m2_pos3
        self.m2_off3 = m2_off3
        self.tel_ra = tel_ra
        self.tel_dec = tel_dec
        self.dither_ra = dither_ra
        self.dither_dec = dither_dec
        self.dither_pa = dither_pa
        self.dome_shutter_status = dome_shutter_status
        self.dome_light_status = dome_light_status
        self.caller = caller
        self.created_at = created_at


class env_condition(Base):
    '''Tracks the telescope environment condition.
    '''
    __tablename__ = 'env_condition'
    __table_args__ = (UniqueConstraint('pfs_visit_id', 'status_sequence_id'),
                      {})

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=False, autoincrement=False)
    status_sequence_id = Column(Integer, primary_key=True, unique=False, autoincrement=False,
                                comment='Gen2 status sequence')
    dome_temperature = Column(REAL, comment='Dome temperature [K]')
    dome_pressure = Column(REAL, comment='Dome pressure [hPa]')
    dome_humidity = Column(REAL, comment='Dome humidity [%]')
    outside_temperature = Column(REAL, comment='Outside temperature [K]')
    outside_pressure = Column(REAL, comment='Outside pressure [hPa]')
    outside_humidity = Column(REAL, comment='Outside humidity [%]')
    created_at = Column(DateTime, index=True,
                        comment='Issued time [YYYY-MM-DDThh:mm:ss]')

    def __init__(self, pfs_visit_id, status_sequence_id,
                 dome_temperature, dome_pressure, dome_humidity,
                 outside_temperature, outside_pressure, outside_humidity,
                 created_at
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.status_sequence_id = status_sequence_id
        self.dome_temperature = dome_temperature
        self.dome_pressure = dome_pressure
        self.dome_humidity = dome_humidity
        self.outside_temperature = outside_temperature
        self.outside_pressure = outside_pressure
        self.outside_humidity = outside_humidity
        self.created_at = created_at


class obs_condition(Base):
    '''Tracks the telescope environment condition.
    '''
    __tablename__ = 'obs_condition'
    __table_args__ = (UniqueConstraint('pfs_visit_id', 'status_sequence_id'),
                      {})

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=False, autoincrement=False)
    status_sequence_id = Column(Integer, primary_key=True, unique=False, autoincrement=False,
                                comment='Gen2 status sequence')
    airmass = Column(REAL)
    moon_phase = Column(REAL)
    moon_alt = Column(REAL)
    moon_sep = Column(REAL)
    seeing = Column(REAL)
    transparency = Column(REAL)
    cloud_condition_id = Column(Integer, ForeignKey('cloud_condition.cloud_condition_id'))
    created_at = Column(DateTime, index=True,
                        comment='Issued time [YYYY-MM-DDThh:mm:ss]')

    def __init__(self, pfs_visit_id, status_sequence_id,
                 airmass, moon_phase, moon_altitude, moon_separation, seeing, transparency,
                 cloud_condition_id,
                 created_at
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.status_sequence_id = status_sequence_id
        self.airmass = airmass
        self.moon_phase = moon_phase
        self.moon_altitude = moon_altitude
        self.moon_separation = moon_separation
        self.seeing = seeing
        self.transparency = transparency
        self.cloud_condition_id = cloud_condition_id
        self.created_at = created_at


class mcs_boresight(Base):
    ''' The MCS boresight for a given MCS exposure.
    '''

    __tablename__ = 'mcs_boresight'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'), primary_key=True, unique=True,
                          autoincrement=False)
    mcs_boresight_x_pix = Column(REAL)
    mcs_boresight_y_pix = Column(REAL)
    calculated_at = Column(DateTime)

    def __init__(self, pfs_visit_id, mcs_boresight_x_pix, mcs_boresight_y_pix, calculated_at):
        self.pfs_visit_id = pfs_visit_id
        self.mcs_boresight_x_pix = mcs_boresight_x_pix
        self.mcs_boresight_y_pix = mcs_boresight_y_pix
        self.calculated_at = calculated_at


class mcs_camera(Base):
    __tablename__ = 'mcs_camera'

    mcs_camera_id = Column(Integer, primary_key=True, autoincrement=False,
                           comment='MCS camera identifier [e.g. 0=Canon_50M, 1=RMOD_71M]')
    mcs_camera_name = Column(String,
                             comment='MCS camera name [e.g. "Canon_50M", "RMOD_71M"]')
    comments = Column(String)

    def __init__(self, mcs_camera_id, mcs_camera_name,
                 comments):
        self.mcs_camera_id = mcs_camera_id
        self.mcs_camera_name = mcs_camera_name
        self.comments = comments


class mcs_exposure(Base):
    ''' Provides instrument and telescope information related to a single MCS exposure.
    '''

    __tablename__ = 'mcs_exposure'

    mcs_frame_id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=False,
                          comment='MCS frame identifier as generated from Gen2')
    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'))
    mcs_exptime = Column(REAL, comment='The exposure time for the frame [sec]')
    altitude = Column(REAL, comment='The telescope attitude [deg]')
    azimuth = Column(REAL, comment='The telescope azimuth [deg]')
    insrot = Column(REAL, comment='The telescope instrument rotation angle [deg]')
    adc_pa = Column(REAL, comment='ADC PA at which the exposure started [deg]')
    dome_temperature = Column(REAL, comment='Dome temperature [K]')
    dome_pressure = Column(REAL, comment='Dome pressure [hPa]')
    dome_humidity = Column(REAL, comment='Dome humidity [%]')
    outside_temperature = Column(REAL, comment='Outside temperature [K]')
    outside_pressure = Column(REAL, comment='Outside pressure [hPa]')
    outside_humidity = Column(REAL, comment='Outside humidity [%]')
    mcs_cover_temperature = Column(REAL, comment='MCS cover panel temperature [degC]')
    mcs_m1_temperature = Column(REAL, comment='MCS primary mirror temperature [degC]')
    mcs_camera_id = Column(Integer, ForeignKey('mcs_camera.mcs_camera_id'))
    measurement_algorithm = Column(String, comment='Spot measurement algorithm (windowed/sep)')
    version_actor = Column(String, comment='Version of the actor')
    version_instdata = Column(String, comment='Version of the pfs_instdata')
    taken_at = Column(DateTime, comment='The time at which the exposure was taken [YYYY-MM-DDThh-mm-sss]')
    taken_in_hst_at = Column(
        DateTime, comment='The time (in HST) at which the exposure was taken [YYYY-MM-DDThh-mm-sss]')

    pfs_visit = relationship('pfs_visit', back_populates='mcs_exposure')
    obslog_notes = relationship('obslog_mcs_exposure_note')

    def __init__(self, mcs_frame_id, pfs_visit_id, mcs_exptime, altitude, azimuth, insrot, adc_pa,
                 dome_temperature, dome_pressure, dome_humidity,
                 outside_temperature, outside_pressure, outside_humidity,
                 mcs_cover_temperature, mcs_m1_temperature, mcs_camera_id,
                 measurement_algorithm, version_actor, version_instdata, taken_at, taken_in_hst_at):
        self.mcs_frame_id = mcs_frame_id
        self.pfs_visit_id = pfs_visit_id
        self.mcs_exptime = mcs_exptime
        self.altitude = altitude
        self.azimuth = azimuth
        self.insrot = insrot
        self.adc_pa = adc_pa
        self.dome_temperature = dome_temperature
        self.dome_pressure = dome_pressure
        self.dome_humidity = dome_humidity
        self.outside_temperature = outside_temperature
        self.outside_pressure = outside_pressure
        self.outside_humidity = outside_humidity
        self.mcs_cover_temperature = mcs_cover_temperature
        self.mcs_m1_temperature = mcs_m1_temperature
        self.mcs_camera_id = mcs_camera_id
        self.measurement_algorithm = measurement_algorithm
        self.version_actor = version_actor
        self.version_instdata = version_instdata
        self.taken_at = taken_at
        self.taken_in_hst_at = taken_in_hst_at


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
                                     comment='The x-component of the second moment '
                                     'of the image in MCS [pix^2]')
    mcs_second_moment_y_pix = Column(REAL,
                                     comment='The y-component of the second moment '
                                     ' of the image [pix^2]')
    mcs_second_moment_xy_pix = Column(REAL,
                                      comment='The xy-component of the second moment '
                                      ' of the image [pix^2]')
    bgvalue = Column(REAL, comment='The background level')
    peakvalue = Column(REAL, comment='The peak image value')
    flags = Column(Integer, comment='Flags about the fitted centroids parameters')
    flux = Column(REAL, comment='The measured flux')
    fluxerr = Column(REAL, comment='The measured flux error')

    def __init__(self, mcs_frame_id, spot_id, mcs_center_x_pix, mcs_center_y_pix,
                 mcs_second_moment_x_pix, mcs_second_moment_y_pix, mcs_second_moment_xy_pix,
                 bgvalue, peakvalue, flags, flux, fluxerr):
        self.mcs_frame_id = mcs_frame_id
        self.spot_id = spot_id
        self.mcs_center_x_pix = mcs_center_x_pix
        self.mcs_center_y_pix = mcs_center_y_pix
        self.mcs_second_moment_x_pix = mcs_second_moment_x_pix
        self.mcs_second_moment_y_pix = mcs_second_moment_y_pix
        self.mcs_second_moment_xy_pix = mcs_second_moment_xy_pix
        self.bgvalue = bgvalue
        self.peakvalue = peakvalue
        self.flags = flags
        self.flux = flux
        self.fluxerr = fluxerr


class mcs_pfi_transformation(Base):
    ''' The MCS-PFI coordinate transformation including coefficients
    '''
    __tablename__ = 'mcs_pfi_transformation'

    mcs_frame_id = Column(Integer, ForeignKey('mcs_exposure.mcs_frame_id'),
                          primary_key=True, unique=True, autoincrement=False,
                          comment='MCS frame identifier as generated from Gen2')
    x0 = Column(REAL,
                comment='Transformation x shift')
    y0 = Column(REAL,
                comment='Transformation y shift')
    dscale = Column(REAL,
                    comment='First transformation scale')
    scale2 = Column(REAL,
                    comment='Second transformation scale')
    theta = Column(REAL,
                   comment='Transformation rotation angle')
    alpha_rot = Column(REAL,
                       comment='coefficient for the dtheta^2 term in the penalty function')
    camera_name = Column(String,
                         comment='camera name for transformation function')

    def __init__(self, mcs_frame_id,
                 x0, y0, dscale, scale2,
                 theta, alpha_rot, camera_name
                 ):

        self.mcs_frame_id = mcs_frame_id
        self.x0 = x0
        self.y0 = y0
        self.dscale = dscale
        self.scale2 = scale2
        self.theta = theta
        self.alpha_rot = alpha_rot
        self.camera_name = camera_name


class camera_model_f3c_mcs(Base):
    ''' Distortion parameters for sanity check
    '''
    __tablename__ = 'camera_model_f3c_mcs'

    mcs_frame_id = Column(Integer, ForeignKey('mcs_exposure.mcs_frame_id'),
                          primary_key=True, unique=True, autoincrement=False,
                          comment='MCS frame identifier as generated from Gen2')
    matrix = Column(ARRAY(REAL),
                    comment='camMatrix')
    distor = Column(ARRAY(REAL),
                    comment='camDistor')
    rot_vector = Column(ARRAY(REAL),
                        comment='camRotVec')
    tran_vector = Column(ARRAY(REAL),
                         comment='camTranVec')

    def __init__(self, mcs_frame_id,
                 matrix, distor, rot_vector, tran_vector
                 ):
        self.mcs_frame_id = mcs_frame_id
        self.matrix = matrix
        self.distor = distor
        self.rot_vector = rot_vector
        self.tran_vector = tran_vector


class pfs_config(Base):
    __tablename__ = 'pfs_config'
    __table_args__ = (UniqueConstraint('pfs_design_id', 'visit0'), {})

    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'),
                           primary_key=True, autoincrement=False)
    visit0 = Column(Integer, primary_key=True, autoincrement=False, unique=True,
                    comment='The first visit of the set')
    ra_center_config = Column(FLOAT, comment='The right ascension of the PFI center [deg]')
    dec_center_config = Column(FLOAT, comment='The declination of the PFI center [deg]')
    pa_config = Column(REAL, comment='The position angle of the PFI [deg]')
    converg_num_iter = Column(Integer,
                              comment='Allocated total number of cobra iterations towards convergence')
    converg_elapsed_time = Column(REAL,
                                  comment='Allocated time for convergence [sec]')
    converg_tolerance = Column(REAL,
                               comment='Tolerance for convergence [mm]')
    alloc_rms_scatter = Column(REAL,
                               comment='[TBW]')
    allocated_at = Column(DateTime, comment='Time at which config was allocated [YYYY-MM-DDhhmmss] (TBC)')

    to_be_observed_at = Column(DateTime, comment='Planned observation time creating the pfsConfig')
    pfs_utils_version = Column(String, comment='pfs_utils version creating the pfsConfig')
    to_be_observed_at_design = Column(DateTime, comment='Planned observation time creating the pfsDesign')
    pfs_utils_version_design = Column(String, comment='pfs_utils version creating the pfsDesign')

    was_observed = Column(Boolean, comment='True of configuration was observed (XXX relevant?)')

    pfs_designs = relationship(pfs_design, backref=backref('pfs_config'))
    field_set = relationship('field_set', back_populates='pfs_config')
    pfs_config_sps = relationship('pfs_config_sps', back_populates='pfs_config')

    def __init__(self, pfs_design_id, visit0, ra_center_config, dec_center_config, pa_config,
                 num_sci_allocated, num_cal_allocated, num_sky_allocated, num_guide_stars_allocated,
                 converg_num_iter, converg_elapsed_time, converg_tolerance, alloc_rms_scatter,
                 allocated_at, to_be_observed_at, pfs_utils_version, to_be_observed_at_design,
                 pfs_utils_version_design, was_observed=False):

        self.pfs_design_id = pfs_design_id
        self.visit0 = visit0
        self.ra_center_config = ra_center_config
        self.dec_center_config = dec_center_config
        self.pa_config = pa_config
        self.num_sci_allocated = num_sci_allocated
        self.num_cal_allocated = num_cal_allocated
        self.num_sky_allocated = num_sky_allocated
        self.num_guide_stars_allocated = num_guide_stars_allocated
        self.converg_num_iter = converg_num_iter
        self.converg_elapsed_time = converg_elapsed_time
        self.converg_tolerance = converg_tolerance
        self.alloc_rms_scatter = alloc_rms_scatter
        self.allocated_at = allocated_at
        self.to_be_observed_at = to_be_observed_at
        self.pfs_utils_version = pfs_utils_version
        self.to_be_observed_at_design = to_be_observed_at_design
        self.pfs_utils_version_design = pfs_utils_version_design
        self.was_observed = was_observed


class pfs_config_fiber(Base):
    __tablename__ = 'pfs_config_fiber'
    __table_args__ = (UniqueConstraint('pfs_design_id', 'visit0', 'fiber_id'),
                      ForeignKeyConstraint(['pfs_design_id', 'visit0'],
                                           ['pfs_config.pfs_design_id', 'pfs_config.visit0']),
                      {})

    pfs_design_id = Column(BigInteger, primary_key=True, autoincrement=False)
    visit0 = Column(Integer, primary_key=True, autoincrement=False,
                    comment='The first visit of the set')
    fiber_id = Column(Integer, primary_key=True, autoincrement=False)
    target_ra = Column(FLOAT, comment='R.A. of the target')
    target_dec = Column(FLOAT, comment='Dec. of the target')
    fiber_status = Column(Integer, comment='fiberStatus: enumerated e.g. GOOD,BROKENFIBER,BLOCKED,BLACKSPOT')
    pfi_nominal_x_mm = Column(REAL, comment='Nominal x-position on the PFI')
    pfi_nominal_y_mm = Column(REAL, comment='Nominal y-position on the PFI')
    pfi_center_final_x_mm = Column(REAL, comment='Final measured x-position on the PFI')
    pfi_center_final_y_mm = Column(REAL, comment='Final measured y-position on the PFI')
    motor_map_summary = Column(String)
    config_elapsed_time = Column(REAL)
    is_on_source = Column(Boolean)
    comments = Column(String, comment='comments')

    pfs_configs = relationship(pfs_config, backref=backref('pfs_config_fiber'))

    def __init__(self, pfs_design_id, visit0, fiber_id, target_ra, target_dec, fiber_status,
                 pfi_nominal_x_mm, pfi_nominal_y_mm,
                 pfi_center_final_x_mm, pfi_center_final_y_mm,
                 motor_map_summary, config_elapsed_time,
                 is_on_source, comments):
        self.pfs_design_id = pfs_design_id
        self.visit0 = visit0
        self.fiber_id = fiber_id
        self.target_ra = target_ra
        self.target_dec = target_dec
        self.fiber_status = fiber_status
        self.pfi_nominal_x_mm = pfi_nominal_x_mm
        self.pfi_nominal_y_mm = pfi_nominal_y_mm
        self.pfi_center_final_x_mm = pfi_center_final_x_mm
        self.pfi_center_final_y_mm = pfi_center_final_y_mm
        self.motor_map_summary = motor_map_summary
        self.config_elapsed_time = config_elapsed_time
        self.is_on_source = is_on_source
        self.comments = comments


class pfs_config_agc(Base):
    __tablename__ = 'pfs_config_agc'
    __table_args__ = (UniqueConstraint('pfs_design_id', 'visit0', 'guide_star_id'),
                      ForeignKeyConstraint(['pfs_design_id', 'visit0'],
                                           ['pfs_config.pfs_design_id', 'pfs_config.visit0']),
                      {})

    pfs_design_id = Column(BigInteger, primary_key=True, autoincrement=False)
    visit0 = Column(Integer, primary_key=True, autoincrement=False,
                    comment='The first visit of the set')
    guide_star_id = Column(BigInteger,
                           primary_key=True, autoincrement=False,
                           comment='GuideStar identifier'
                           )
    agc_camera_id = Column(Integer, comment='AGC camera identifier')
    agc_final_x_pix = Column(REAL, comment='Final x-position on the AGC [pix]')
    agc_final_y_pix = Column(REAL, comment='Final y-position on the AGC [pix]')
    comments = Column(String, comment='comments')

    pfs_configs = relationship(pfs_config, backref=backref('pfs_config_agc'))

    def __init__(self, pfs_design_id, visit0, guide_star_id,
                 agc_camera_id, agc_final_x_pix, agc_final_y_pix, comments):
        self.pfs_design_id = pfs_design_id
        self.visit0 = visit0
        self.guide_star_id = guide_star_id
        self.agc_camera_id = agc_camera_id
        self.agc_final_x_pix = agc_final_x_pix
        self.agc_final_y_pix = agc_final_y_pix
        self.comments = comments


class pfs_config_sps(Base):
    __tablename__ = 'pfs_config_sps'
    __table_args__ = (UniqueConstraint('pfs_visit_id', 'visit0'),
                      ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id']),
                      ForeignKeyConstraint(['visit0'], ['pfs_config.visit0']),
                      {})
    pfs_visit_id = Column(Integer, primary_key=True, autoincrement=False)
    visit0 = Column(Integer, primary_key=True, autoincrement=False, comment='The first visit of the set')
    cam_mask = Column(Integer, comment='bitMask describing which cameras were use for this visit.')
    inst_status_flag = Column(Integer, comment='Bitmask indicating instrument-related status flags for this visit.')

    pfs_visit = relationship('pfs_visit', uselist=False, back_populates='pfs_config_sps')
    pfs_config = relationship('pfs_config', uselist=False, back_populates='pfs_config_sps')

    def __init__(self, pfs_visit_id, visit0, cam_mask, inst_status_flag):
        self.pfs_visit_id = pfs_visit_id
        self.visit0 = visit0
        self.cam_mask = cam_mask
        self.inst_status_flag = inst_status_flag

class cobra_motor_axis(Base):
    '''The axis or stage of a cobra motor.
    This can be one of:
    Theta (or Stage 1)
    Phi (or Stage 2)
    '''
    __tablename__ = 'cobra_motor_axis'

    cobra_motor_axis_id = Column(Integer, primary_key=True, autoincrement=False,
                                 comment='Motor axis stage number [1,2]')
    cobra_motor_axis_name = Column(String, comment='Corresponding name for axis [Theta, Phi]')

    def __init__(self, cobra_motor_axis_id, cobra_motor_axis_name):
        self.cobra_motor_axis_id = cobra_motor_axis_id
        self.cobra_motor_axis_name = cobra_motor_axis_name


class cobra_motor_direction(Base):
    '''The axis or stage of a cobra motor.
    This can be one of:
    Forward (0)
    Reverse (1)
    '''
    __tablename__ = 'cobra_motor_direction'

    cobra_motor_direction_id = Column(Integer, primary_key=True,
                                      autoincrement=False, comment='Motor movement direction [0,1]')
    cobra_motor_direction_name = Column(
        String, comment='Corresponding name for the movement [Forward, Reverse]')

    def __init__(self, cobra_motor_direction_id, cobra_motor_direction_name):
        self.cobra_motor_direction_id = cobra_motor_direction_id
        self.cobra_motor_direction_name = cobra_motor_direction_name


class cobra_geometry_calib(Base):
    '''Defines the cobra motor calibration profile
    '''
    __tablename__ = 'cobra_geometry_calib'

    cobra_geometry_calib_id = Column(Integer, primary_key=True, autoincrement=True)
    calibrated_at = Column(DateTime,
                           comment='Date at which the model calibration took place [YYYY-MM-DDhh:mm:ss]')
    comments = Column(String, comment='Comments')

    def __init__(self, calibrated_at, comments
                 ):
        self.calibrated_at = calibrated_at
        self.comments = comments


class cobra_motor_calib(Base):
    '''Defines the cobra motor calibration profile
    '''
    __tablename__ = 'cobra_motor_calib'

    cobra_motor_calib_id = Column(Integer, primary_key=True, autoincrement=True)
    calibrated_at = Column(DateTime,
                           comment='Date at which the model calibration took place [YYYY-MM-DDhh:mm:ss]')
    comments = Column(String, comment='Comments')

    def __init__(self, calibrated_at, comments
                 ):
        self.calibrated_at = calibrated_at
        self.comments = comments


class cobra_motor_model(Base):
    '''Defines the cobra motor model profile fr om
    '''
    __tablename__ = 'cobra_motor_model'

    cobra_motor_model_id = Column(Integer, primary_key=True, autoincrement=True)
    cobra_motor_calib_id = Column(Integer, ForeignKey('cobra_motor_calib.cobra_motor_calib_id'), index=True)
    cobra_id = Column(Integer, comment='The cobra fiber identifier', index=True)
    cobra_motor_axis_id = Column(Integer, ForeignKey('cobra_motor_axis.cobra_motor_axis_id'), index=True)
    cobra_motor_direction_id = Column(Integer, ForeignKey(
        'cobra_motor_direction.cobra_motor_direction_id'), index=True)
    cobra_motor_on_time = Column(REAL, comment='The ontime level')
    cobra_motor_step_size = Column(REAL, comment='The step size resolution')
    cobra_motor_frequency = Column(REAL, comment='The motor frequency')

    def __init__(self, cobra_motor_calib_id, cobra_id, cobra_motor_axis_id,
                 cobra_motor_angle, cobra_motor_on_time, cobra_motor_speed,
                 cobra_motor_frequency
                 ):
        self.cobra_motor_calib_id = cobra_motor_calib_id
        self.cobra_id = cobra_id
        self.cobra_motor_axis_id = cobra_motor_axis_id
        self.cobra_motor_angle = cobra_motor_angle
        self.cobra_motor_on_time = cobra_motor_on_time
        self.cobra_motor_speed = cobra_motor_speed
        self.cobra_motor_frequency = cobra_motor_frequency


class cobra_motor_map(Base):
    '''Defines the detailed cobra motor map
    '''
    __tablename__ = 'cobra_motor_map'
    __table_args__ = (UniqueConstraint('cobra_motor_model_id', 'cobra_motor_move_sequence'),
                      {})

    cobra_motor_model_id = Column(Integer, ForeignKey(
        'cobra_motor_model.cobra_motor_model_id'), primary_key=True, autoincrement=False)
    cobra_motor_move_sequence = Column(Integer, primary_key=True,
                                       autoincrement=False, comment='The motor movement sequence')
    cobra_motor_angle = Column(REAL, comment='The angle of the motor [deg]')
    cobra_motor_speed = Column(REAL, comment='The speed of the motor [deg/step] (TBC)')

    def __init__(self, cobra_motor_model_id, cobra_motor_move_sequence,
                 cobra_motor_angle, cobra_motor_speed
                 ):
        self.cobra_motor_model_id = cobra_motor_model_id
        self.cobra_motor_move_sequence = cobra_motor_move_sequence
        self.cobra_motor_angle = cobra_motor_angle
        self.cobra_motor_speed = cobra_motor_speed


class cobra_convergence_test(Base):
    ''' The results of the cobra convergence test
    '''
    __tablename__ = 'cobra_convergence_test'
    __table_args__ = (UniqueConstraint('cobra_motor_model_id', 'iteration', 'cobra_motor_angle_target_id'),
                      {})

    cobra_motor_model_id = Column(Integer, ForeignKey(
        'cobra_motor_model.cobra_motor_model_id'), primary_key=True, autoincrement=False)
    iteration = Column(Integer, primary_key=True, autoincrement=False, comment='The iteration number')
    cobra_motor_angle_target_id = Column(
        Integer, primary_key=True, autoincrement=False, comment='The ID for the target angle of the motor to test')
    cobra_motor_angle_target = Column(REAL, comment='The target angle of the motor to test')
    cobra_motor_angle_difference = Column(REAL, comment='The difference of the motor angle [deg.]')
    signal_to_noise_ratio = Column(REAL, comment='Signal-to-Noise ratio')

    def __init__(self, cobra_motor_model_id, iteration, cobra_motor_angle_target_id,
                 cobra_motor_angle_target, cobra_motor_angle_difference, signal_to_noise_ratio
                 ):
        self.cobra_motor_model_id = cobra_motor_model_id
        self.iteration = iteration
        self.cobra_motor_angle_target_id = cobra_motor_angle_target_id
        self.cobra_motor_angle_target = cobra_motor_angle_target
        self.cobra_motor_angle_difference = cobra_motor_angle_difference
        self.signal_to_noise_ratio = signal_to_noise_ratio


class cobra_target(Base):
    ''' The actual movement of the cobra motor, in terms of individual MCS frames.
    '''
    __tablename__ = 'cobra_target'
    __table_args__ = (UniqueConstraint('pfs_visit_id', 'iteration', 'cobra_id'),
                      {})

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=False, autoincrement=False,
                          comment='PFS visit identifier')
    iteration = Column(Integer,
                       primary_key=True, unique=False, autoincrement=False,
                       comment='Iteration number for this frame')
    cobra_id = Column(Integer,
                      primary_key=True, unique=False, autoincrement=False,
                      comment='Fiber identifier')
    pfs_config_id = Column(BigInteger)
    pfi_nominal_x_mm = Column(REAL,
                              comment='Nominal x-position on the PFI as determined from the '
                              ' pfs_design_fiber table [mm]')
    pfi_nominal_y_mm = Column(REAL,
                              comment='Nominal y-position on the PFI as determined from the '
                              ' pfs_design_fiber table [mm]')
    pfi_target_x_mm = Column(REAL,
                             comment='Target x-position on the PFI for each iteration')
    pfi_target_y_mm = Column(REAL,
                             comment='Target y-position on the PFI for each iteration')
    flags = Column(Integer, comment='flags for movement etc.')

    def __init__(self, pfs_visit_id, iteration, cobra_id,
                 pfs_config_id,
                 pfi_nominal_x_mm, pfi_nominal_y_mm,
                 pfi_target_x_mm, pfi_target_y_mm,
                 flags
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.iteration = iteration
        self.cobra_id = cobra_id
        self.pfs_config_id = pfs_config_id
        self.pfi_nominal_x_mm = pfi_nominal_x_mm
        self.pfi_nominal_y_mm = pfi_nominal_y_mm
        self.pfi_target_x_mm = pfi_target_x_mm
        self.pfi_target_y_mm = pfi_target_y_mm
        self.flags = flags


class cobra_move(Base):
    ''' The actual movement of the cobra motor, in terms of individual MCS frames.
    '''
    __tablename__ = 'cobra_move'
    __table_args__ = (UniqueConstraint('pfs_visit_id', 'iteration', 'cobra_id'),
                      ForeignKeyConstraint(['pfs_visit_id', 'iteration', 'cobra_id'],
                                           ['cobra_match.pfs_visit_id', 'cobra_match.iteration', 'cobra_match.cobra_id']),
                      {})

    pfs_visit_id = Column(Integer,
                          primary_key=True, unique=False, autoincrement=False,
                          comment='PFS visit identifier')
    iteration = Column(Integer,
                       primary_key=True, unique=False, autoincrement=False,
                       comment='Iteration number for this frame')
    cobra_id = Column(Integer,
                      primary_key=True, unique=False, autoincrement=False,
                      comment='Fiber identifier')
    cobra_motor_model_id_theta = Column(Integer)
    motor_target_theta = Column(REAL,
                                comment='the target angle of the theta motor'
                                )
    motor_num_step_theta = Column(Integer,
                                  comment='the number of steps the theta motor has undertaken')
    motor_on_time_theta = Column(REAL,
                                 comment='the theta motor ontime value')
    cobra_motor_model_id_phi = Column(Integer)
    motor_target_phi = Column(REAL,
                              comment='the target angle of the phi motor'
                              )
    motor_num_step_phi = Column(Integer, comment='the number of steps the phi motor has undertaken')
    motor_on_time_phi = Column(REAL, comment='the phi motor ontime value')
    flags = Column(Integer, comment='flags for movement etc.')

    def __init__(self, pfs_visit_id, iteration, cobra_id,
                 cobra_motor_calib_id,
                 motor_target_theta, motor_num_step_theta, motor_on_time_theta,
                 motor_target_phi, motor_num_step_phi, motor_on_time_phi,
                 flags
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.iteration = iteration
        self.cobra_id = cobra_id
        self.cobra_motor_map_model_id = cobra_motor_calib_id
        self.motor_target_theta = motor_target_theta
        self.motor_num_step_theta = motor_num_step_theta
        self.motor_on_time_theta = motor_on_time_theta
        self.motor_target_phi = motor_target_phi
        self.motor_num_step_phi = motor_num_step_phi
        self.motor_on_time_phi = motor_on_time_phi
        self.flags = flags


class cobra_match(Base):
    '''Defines the status of each cobra at each step during convergence.
    '''
    __tablename__ = 'cobra_match'
    __table_args__ = (UniqueConstraint('pfs_visit_id', 'iteration', 'cobra_id'),
                      ForeignKeyConstraint(['pfs_visit_id', 'iteration', 'cobra_id'],
                                           ['cobra_target.pfs_visit_id', 'cobra_target.iteration', 'cobra_target.cobra_id']),
                      ForeignKeyConstraint(['mcs_frame_id', 'spot_id'],
                                           ['mcs_data.mcs_frame_id', 'mcs_data.spot_id']),
                      {})

    pfs_visit_id = Column(Integer,
                          primary_key=True, unique=False, autoincrement=False,
                          comment='PFS visit identifier')
    iteration = Column(Integer,
                       primary_key=True, unique=False, autoincrement=False,
                       comment='Iteration number for this frame')
    cobra_id = Column(Integer,
                      primary_key=True, unique=False, autoincrement=False,
                      comment='Fiber identifier')
    mcs_frame_id = Column(Integer,
                          primary_key=False, unique=False, autoincrement=False,
                          comment='MCS frame identifier as generated from Gen2')
    spot_id = Column(Integer,
                     primary_key=False, unique=False, autoincrement=False,
                     comment='Corresponding MCS image spot identifier ')
    pfi_center_x_mm = Column(REAL,
                             comment='Actual x-position on the PFI [mm]')
    pfi_center_y_mm = Column(REAL,
                             comment='Actual y-position on the PFI [mm]')
    flags = Column(Integer, comment='flags for movement etc.')

    def __init__(self, pfs_visit_id, iteration, cobra_id,
                 mcs_frame_id, spot_id,
                 pfi_center_x_mm, pfi_center_y_mm, flags
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.iteration = iteration
        self.cobra_id = cobra_id
        self.mcs_frame_id = mcs_frame_id
        self.spot_id = spot_id
        self.pfi_center_x_mm = pfi_center_x_mm
        self.pfi_center_y_mm = pfi_center_y_mm
        self.flags = flags


class fiducial_fiber_match(Base):
    '''Defines the status of each cobra at each step during convergence.
    '''
    __tablename__ = 'fiducial_fiber_match'
    __table_args__ = (UniqueConstraint('pfs_visit_id', 'iteration', 'fiducial_fiber_id'),
                      ForeignKeyConstraint(['mcs_frame_id', 'spot_id'],
                                           ['mcs_data.mcs_frame_id', 'mcs_data.spot_id']),
                      {})

    pfs_visit_id = Column(Integer,
                          primary_key=True, unique=False, autoincrement=False,
                          comment='PFS visit identifier')
    iteration = Column(Integer,
                       primary_key=True, unique=False, autoincrement=False,
                       comment='Iteration number for this frame')
    fiducial_fiber_id = Column(Integer,
                               primary_key=True, unique=False, autoincrement=False,
                               comment='Fiducial fiber identifier')
    mcs_frame_id = Column(Integer,
                          primary_key=False, unique=False, autoincrement=False,
                          comment='MCS frame identifier as generated from Gen2')
    spot_id = Column(Integer,
                     primary_key=False, unique=False, autoincrement=False,
                     comment='Corresponding MCS image spot identifier ')
    pfi_center_x_mm = Column(REAL,
                             comment='Measured FF x-position on the PFI [mm]')
    pfi_center_y_mm = Column(REAL,
                             comment='Measured FF y-position on the PFI [mm]')
    fiducial_tweaked_x_mm = Column(REAL,
                             comment='Expected FF x-position on the PFI at the convergence [mm]')
    fiducial_tweaked_y_mm = Column(REAL,
                             comment='Expected FF y-position on the PFI at the convergence [mm]')
    flags = Column(Integer, comment='flags for movement etc.')
    match_mask = Column(Integer, comment='mask for FF match (1 for FFs used in outer ring, 2 for FFs used in first iteration of transformation, 4 for FFs used in final transformation.')

    def __init__(self, pfs_visit_id, iteration, fiducial_fiber_id,
                 mcs_frame_id, spot_id, pfi_center_x_mm, pfi_center_y_mm, fiducial_tweaked_x_mm, fiducial_tweaked_y_mm, flags,
                 match_mask,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.iteration = iteration
        self.fiducial_fiber_id = fiducial_fiber_id
        self.mcs_frame_id = mcs_frame_id
        self.spot_id = spot_id
        self.pfi_center_x_mm = pfi_center_x_mm
        self.pfi_center_y_mm = pfi_center_y_mm
        self.fiducial_tweaked_x_mm = fiducial_tweaked_x_mm
        self.fiducial_tweaked_y_mm = fiducial_tweaked_y_mm
        self.flags = flags
        self.match_mask = match_mask


class sps_visit(Base):
    __tablename__ = 'sps_visit'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False,
                          comment='PFS visit identifier')
    exp_type = Column(String,
                      comment='Type of exposure: BIAS, FLAT, DFLAT etc.')

    pfs_visit = relationship('pfs_visit', uselist=False, back_populates='sps_visit')
    sps_exposure = relationship('sps_exposure', back_populates='sps_visit')

    def __init__(self, pfs_visit_id, exp_type):
        self.pfs_visit_id = pfs_visit_id
        self.exp_type = exp_type


class sps_sequence(Base):
    __tablename__ = 'sps_sequence'

    visit_set_id = Column(Integer, primary_key=True, unique=True, autoincrement=False,
                          comment='SpS visit set identifier')
    sequence_type = Column(String,
                           comment='SpS sequence type')
    name = Column(String,
                  comment='The unique name assigned to this set of visits')
    comments = Column(String,
                      comment='Comments for the sequence')
    cmd_str = Column(String,
                     comment='ICS command string that generates exposures for this set of visits')
    status = Column(String,
                    comment='Status of the sequence')

    def __init__(self, visit_set_id, sequence_type, name, comments, cmd_str, status):
        self.visit_set_id = visit_set_id
        self.sequence_type = sequence_type
        self.name = name
        self.comments = comments
        self.cmd_str = cmd_str
        self.status = status


class iic_sequence(Base):
    __tablename__ = 'iic_sequence'

    iic_sequence_id = Column(Integer, primary_key=True, autoincrement=False,
                             comment='Sequence identifier')
    sequence_type = Column(String,
                           comment='Sequence type')
    name = Column(String,
                  comment='The unique name assigned to this set of visits')
    comments = Column(String,
                      comment='Comments for the sequence')
    cmd_str = Column(String,
                     comment='ICS command string that generates exposures for this set of visits')
    group_id = Column(Integer, ForeignKey('sequence_group.group_id'), comment='Group identifier')
    created_at = Column(DateTime,
                        comment='Creation time [YYYY-MM-DDThh:mm:ss]')

    visit_set = relationship('visit_set', uselist=False, back_populates='iic_sequence')
    iic_sequence_status = relationship('iic_sequence_status', uselist=False, back_populates='iic_sequence')
    field_set = relationship('field_set', back_populates='iic_sequence')
    obslog_notes = relationship('obslog_visit_set_note')
    sequence_group = relationship('sequence_group', back_populates='iic_sequence')

    def __init__(self, iic_sequence_id, sequence_type, name, comments, cmd_str, group_id, created_at):
        self.iic_sequence_id = iic_sequence_id
        self.sequence_type = sequence_type
        self.name = name
        self.comments = comments
        self.cmd_str = cmd_str
        self.group_id = group_id
        self.created_at = created_at


class iic_sequence_status(Base):
    __tablename__ = 'iic_sequence_status'

    iic_sequence_id = Column(Integer, ForeignKey('iic_sequence.iic_sequence_id'),
                             primary_key=True, autoincrement=False,
                             comment='Sequence identifier')
    status_flag = Column(Integer,
                         comment='Status flag of the sequence')
    cmd_output = Column(String,
                        comment='Status output')

    iic_sequence = relationship('iic_sequence', back_populates='iic_sequence_status')
    finished_at = Column(DateTime,
                         comment='End time [YYYY-MM-DDThh:mm:ss]')

    def __init__(self, iic_sequence_id, status_flag, cmd_output, finished_at):
        self.iic_sequence_id = iic_sequence_id
        self.status_flag = status_flag
        self.cmd_output = cmd_output
        self.finished_at = finished_at


class visit_set(Base):
    __tablename__ = 'visit_set'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False)
    iic_sequence_id = Column(Integer, ForeignKey('iic_sequence.iic_sequence_id'))

    pfs_visit = relationship('pfs_visit', uselist=False, back_populates='visit_set')
    iic_sequence = relationship('iic_sequence', uselist=False, back_populates='visit_set')

    def __init__(self, pfs_visit_id, iic_sequence_id):
        self.pfs_visit_id = pfs_visit_id
        self.iic_sequence_id = iic_sequence_id


class sequence_group(Base):
    __tablename__ = 'sequence_group'

    group_id = Column(Integer, primary_key=True, autoincrement=False,  comment='Group identifier')
    group_name = Column(String, comment='Group name')
    created_at = Column(DateTime,
                        comment='Creation time [YYYY-MM-DDThh:mm:ss]')

    iic_sequence = relationship('iic_sequence', uselist=False, back_populates='sequence_group')

    def __init__(self, group_id, group_name, created_at):
        self.group_id = group_id
        self.group_name = group_name
        self.created_at = created_at


class field_set(Base):
    __tablename__ = 'field_set'
    iic_sequence_id = Column(Integer, ForeignKey('iic_sequence.iic_sequence_id'), primary_key=True)
    visit0 = Column(Integer, ForeignKey('pfs_config.visit0'))

    iic_sequence = relationship('iic_sequence', uselist=False, back_populates='field_set')
    pfs_config = relationship('pfs_config', uselist=False, back_populates='field_set')

    def __init__(self, iic_sequence_id, visit0):
        self.iic_sequence_id = iic_sequence_id
        self.visit0 = visit0


class sps_exposure(Base):
    __tablename__ = 'sps_exposure'
    __table_args__ = (UniqueConstraint('pfs_visit_id', 'sps_camera_id'), {})

    pfs_visit_id = Column(Integer, ForeignKey('sps_visit.pfs_visit_id'), primary_key=True,
                          comment='PFS visit identifier')
    sps_camera_id = Column(Integer, ForeignKey('sps_camera.sps_camera_id'), primary_key=True,
                           comment='SpS camera identifier [1-16]')
    exptime = Column(REAL,
                     comment='Exposure time for visit [sec]')
    time_exp_start = Column(DateTime,
                            comment='Start time for exposure [YYYY-MM-DDThh:mm:ss]')
    time_exp_end = Column(DateTime,
                          comment='End time for exposure [YYYY-MM-DDThh:mm:ss]')
    beam_config_date = Column(FLOAT,
                              comment='MJD when the configuration changed')

    sps_visit = relationship('sps_visit', back_populates='sps_exposure')

    sps_annotation = relationship('sps_annotation', back_populates='sps_exposure')

    def __init__(self, pfs_visit_id, sps_camera_id,
                 exptime, time_exp_start, time_exp_end,
                 beam_config_date
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.sps_camera_id = sps_camera_id
        self.exptime = exptime
        self.time_exp_start = time_exp_start
        self.time_exp_end = time_exp_end
        self.beam_config_date = beam_config_date


class sps_module(Base):
    __tablename__ = 'sps_module'

    sps_module_id = Column(Integer, primary_key=True, unique=True, autoincrement=False,
                           comment='SpS module identifier [1-4]')
    description = Column(String,
                         comment='SpS module name')

    def __init__(self, sps_module_id, description):
        self.sps_module_id = sps_module_id
        self.description = description


class sps_camera(Base):
    __tablename__ = 'sps_camera'

    sps_camera_id = Column(Integer, primary_key=True, autoincrement=False,
                           comment='SpS camera identifier [1-16]')
    sps_camera_name = Column(String(2),
                             comment='SpS camera name [e.g. "b3"]')
    sps_module_id = Column(Integer, ForeignKey('sps_module.sps_module_id'),
                           comment='SpS module identifier [1-4]')
    sps_module_name = Column(String(3),
                             comment='SpS module name [e.g. "sm3"]')
    arm = Column(String(1),
                 comment='Spectrograph arm identifier [b, r, n, m]')
    arm_num = Column(Integer,
                     comment='Spectrograph arm identifier as a number [1-4]')

    def __init__(self, sps_camera_id, sps_camera_name,
                 sps_module_id, sps_module_name,
                 arm, arm_num):
        self.sps_camera_id = sps_camera_id
        self.sps_camera_name = sps_camera_name
        self.sps_module_id = sps_module_id
        self.sps_module_name = sps_module_name
        self.arm = arm
        self.arm_num = arm_num


class sps_annotation(Base):
    __tablename__ = 'sps_annotation'
    __table_args__ = (ForeignKeyConstraint(['pfs_visit_id', 'sps_camera_id'],
                                           ['sps_exposure.pfs_visit_id', 'sps_exposure.sps_camera_id']),
                      {})

    annotation_id = Column(Integer, primary_key=True, autoincrement=True,
                           comment='SpS annotation identifier (primary key)')
    pfs_visit_id = Column(Integer,
                          comment='PFS visit identifier')
    sps_camera_id = Column(Integer,
                           comment='SpS camera identifier [1-16]')
    data_flag = Column(Integer,
                       comment='Flag of obtained data')
    notes = Column(String,
                   comment='Notes of obtained data')
    created_at = Column(DateTime,
                        comment='Creation time [YYYY-MM-DDThh:mm:ss]')

    sps_exposure = relationship('sps_exposure', back_populates='sps_annotation')

    def __init__(self, annotation_id, pfs_visit_id, sps_camera_id, data_flag, notes, created_at):
        self.annotation_id = annotation_id
        self.pfs_visit_id = pfs_visit_id
        self.sps_camera_id = sps_camera_id
        self.data_flag = data_flag
        self.notes = notes
        self.created_at = created_at


class sps_condition(Base):
    __tablename__ = 'sps_condition'
    __table_args__ = (UniqueConstraint('pfs_visit_id', 'sps_camera_id'),
                      ForeignKeyConstraint(['pfs_visit_id', 'sps_camera_id'],
                                           ['sps_exposure.pfs_visit_id', 'sps_exposure.sps_camera_id']),
                      {})

    pfs_visit_id = Column(Integer, primary_key=True,
                          comment='PFS visit identifier')
    sps_camera_id = Column(Integer, primary_key=True,
                           comment='SpS camera identifier [1-16]')
    background = Column(REAL,
                        comment='Background level (TBD)')
    throughput = Column(REAL,
                        comment='System throughput (TBD)')

    def __init__(self, pfs_visit_id, sps_camera_id,
                 background, throughput,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.sps_camera_id = sps_camera_id
        self.background = background
        self.throughput = throughput


class beam_switch_mode(Base):
    __tablename__ = 'beam_switch_mode'

    beam_switch_mode_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    beam_switch_mode_name = Column(String)
    beam_switch_mode_description = Column(String)

    def __init__(self, beam_switch_mode_id, beam_switch_mode_name, beam_switch_mode_description):
        self.beam_switch_mode_id = beam_switch_mode_id
        self.beam_switch_mode_name = beam_switch_mode_name
        self.beam_switch_mode_description = beam_switch_mode_description


class calib(Base):
    __tablename__ = 'calib'

    calib_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    calib_type = Column(String)
    sps_frames_to_use = Column(String)
    pfs_design_id = Column(BigInteger, ForeignKey('pfs_design.pfs_design_id'))
    calib_date = Column(DateTime)

    def __init__(self, calib_id, calib_type, sps_frames_to_use, pfs_design_id, calib_date):
        self.calib_id = calib_id
        self.calib_type = calib_type
        self.sps_frames_to_use = sps_frames_to_use
        self.pfs_design_id = pfs_design_id
        self.calib_date = calib_date


class calib_set(Base):
    __tablename__ = 'calib_set'
    calib_set_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    calib_flat_id = Column(Integer, ForeignKey('calib.calib_id'))
    calib_bias_id = Column(Integer, ForeignKey('calib.calib_id'))
    calib_dark_id = Column(Integer, ForeignKey('calib.calib_id'))
    calib_arcs_id = Column(Integer, ForeignKey('calib.calib_id'))

    calib_flat = relationship(calib, primaryjoin="calib_set.calib_flat_id==calib.calib_id")
    calib_bias = relationship(calib, primaryjoin="calib_set.calib_bias_id==calib.calib_id")
    calib_dark = relationship(calib, primaryjoin="calib_set.calib_dark_id==calib.calib_id")
    calib_arcs = relationship(calib, primaryjoin="calib_set.calib_arcs_id==calib.calib_id")

    def __init__(self, calib_set_id,
                 calib_flat_id, calib_bias_id, calib_dark_id, calib_arcs_id
                 ):
        self.calib_set_id = calib_set_id
        self.calib_flat_id = calib_flat_id
        self.calib_bias_id = calib_bias_id
        self.calib_dark_id = calib_dark_id
        self.calib_arcs_id = calib_arcs_id


class obslog_user(Base):
    __tablename__ = 'obslog_user'

    id = Column(Integer, primary_key=True)
    account_name = Column(String, nullable=False, unique=True)

    visit_notes = relationship('obslog_visit_note')
    visit_set_notes = relationship('obslog_visit_set_note')
    mcs_exposure_notes = relationship('obslog_mcs_exposure_note')


class obslog_visit_set_note(Base):
    __tablename__ = 'obslog_visit_set_note'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('obslog_user.id'))
    iic_sequence_id = Column(Integer, ForeignKey('iic_sequence.iic_sequence_id'))
    body = Column(String, nullable=False)

    user = relationship('obslog_user', back_populates='visit_set_notes')
    iic_sequence = relationship('iic_sequence', back_populates='obslog_notes')


class obslog_visit_note(Base):
    __tablename__ = 'obslog_visit_note'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('obslog_user.id'))
    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'))
    body = Column(String, nullable=False)

    user = relationship('obslog_user', back_populates='visit_notes')
    pfs_visit = relationship('pfs_visit', back_populates='obslog_notes')


class obslog_mcs_exposure_note(Base):
    __tablename__ = 'obslog_mcs_exposure_note'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('obslog_user.id'))
    mcs_exposure_frame_id = Column(Integer, ForeignKey('mcs_exposure.mcs_frame_id'))
    body = Column(String, nullable=False)

    user = relationship('obslog_user', back_populates='mcs_exposure_notes')
    mcs_exposure = relationship('mcs_exposure', back_populates='obslog_notes')


class obslog_fits_header(Base):
    ''' Headers of FITS file belonging to a visit
    '''
    __tablename__ = 'obslog_fits_header'
    __table_args__ = (PrimaryKeyConstraint('filestem', 'hdu_index'),
                      {})

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'), index=True)

    filestem = Column(String)  # ex.) agcc_20210919_0455221 or PFSA01967911
    hdu_index = Column(Integer)  # ex.) 0 or 1
    cards_dict = Column(JSONB, nullable=False)  # ex.) {"SIMPLE": true, "BITPIX": 8, ...}
    cards_list = Column(JSONB, nullable=False)  # ex.) [["SIMPLE", true, "conform..."], ...]


class agc_exposure(Base):
    ''' Provides instrument and telescope information related to a single AGC exposure.
    '''

    __tablename__ = 'agc_exposure'

    agc_exposure_id = Column(Integer, primary_key=True, unique=True, autoincrement=False,
                             comment='AGC exposure number identifier')
    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'), comment='PFS visit identifier')
    agc_exptime = Column(REAL, comment='The exposure time for the frame [sec]')
    altitude = Column(REAL, comment='The telescope altitude [deg]')
    azimuth = Column(REAL, comment='The telescope azimuth [deg]')
    insrot = Column(REAL, comment='The telescope instrument rotation angle [deg]')
    adc_pa = Column(REAL, comment='ADC PA at which the exposure started [deg]')
    m2_pos3 = Column(REAL, comment='Hexapod position [mm]')
    outside_temperature = Column(REAL, comment='Outside temperature [K]')
    outside_pressure = Column(REAL, comment='Outside pressure [hPa]')
    outside_humidity = Column(REAL, comment='Outside humidity [%]')
    measurement_algorithm = Column(String, comment='Spot measurement algorithm (windowed/sep)')
    version_actor = Column(String, comment='Version of the actor')
    version_instdata = Column(String, comment='Version of the pfs_instdata')
    taken_at = Column(DateTime, comment='The time at which the exposure was taken [YYYY-MM-DDThh-mm-sss]')

    pfs_visit = relationship('pfs_visit', back_populates='agc_exposure')
    agc_guide_offset = relationship('agc_guide_offset', uselist=False, back_populates='agc_exposure')

    def __init__(self, agc_exposure_id, pfs_visit_id, agc_exptime, altitude, azimuth, insrot, adc_pa,
                 m2_pos3, outside_temperature, outside_pressure, outside_humidity,
                 measurement_algorithm, version_actor, version_instdata, taken_at):
        self.agc_exposure_id = agc_exposure_id
        self.pfs_visit_id = pfs_visit_id
        self.agc_exptime = agc_exptime
        self.altitude = altitude
        self.azimuth = azimuth
        self.insrot = insrot
        self.adc_pa = adc_pa
        self.m2_pos3 = m2_pos3
        self.outside_temperature = outside_temperature
        self.outside_pressure = outside_pressure
        self.outside_humidity = outside_humidity
        self.measurement_algorithm = measurement_algorithm
        self.version_actor = version_actor
        self.version_instdata = version_instdata
        self.taken_at = taken_at


class agc_data(Base):
    '''AGC centroiding information.
    Generated by the agccActor software.
    '''

    __tablename__ = 'agc_data'
    __table_args__ = (UniqueConstraint('agc_exposure_id', 'agc_camera_id', 'spot_id'),
                      {})

    agc_exposure_id = Column(Integer, ForeignKey('agc_exposure.agc_exposure_id'),
                             primary_key=True, autoincrement=False,
                             comment='AGC exposure number identifier')
    agc_camera_id = Column(Integer, primary_key=True, autoincrement=False,
                           comment='AGC camera identifier')
    spot_id = Column(Integer, primary_key=True, autoincrement=False,
                     comment='The AGC spot identifier')
    image_moment_00_pix = Column(REAL, comment='')
    centroid_x_pix = Column(REAL, comment='The x-center of the spot image in AGC [pix]')
    centroid_y_pix = Column(REAL, comment='The y-center of the spot image in AGC [pix]]')
    central_image_moment_11_pix = Column(REAL,
                                         comment='The 11-component of the second moment')
    central_image_moment_20_pix = Column(REAL,
                                         comment='The 20-component of the second moment')
    central_image_moment_02_pix = Column(REAL,
                                         comment='The 02-component of the second moment')
    peak_pixel_x_pix = Column(Integer, comment='The peak x pixel')
    peak_pixel_y_pix = Column(Integer, comment='The peak y pixel')
    peak_intensity = Column(REAL, comment='The peak intensity')
    background = Column(REAL, comment='The background value')
    estimated_magnitude = Column(REAL, comment='The estimated magnitude of the object')
    flags = Column(Integer, comment='Flags')

    def __init__(self, agc_exposure_id, spot_id, agc_camera_id,
                 image_moment_00_pix, centroid_x_pix, centroid_y_pix,
                 central_image_moment_11_pix, central_image_moment_20_pix, central_image_moment_02_pix,
                 peak_pixel_x_pix, peak_pixel_y_pix, peak_intensity,
                 background, estimated_magnitude, flags):
        self.agc_exposure_id = agc_exposure_id
        self.spot_id = spot_id
        self.agc_camera_id = agc_camera_id
        self.image_moment_00_pix = image_moment_00_pix
        self.centroid_x_pix = centroid_x_pix
        self.centroid_y_pix = centroid_y_pix
        self.central_image_moment_11_pix = central_image_moment_11_pix
        self.central_image_moment_20_pix = central_image_moment_20_pix
        self.central_image_moment_02_pix = central_image_moment_02_pix
        self.peak_pixel_x_pix = peak_pixel_x_pix
        self.peak_pixel_y_pix = peak_pixel_y_pix
        self.peak_intensity = peak_intensity
        self.background = background
        self.estimated_magnitude = estimated_magnitude
        self.flags = flags


class agc_match(Base):
    '''AGC matching information.
    '''

    __tablename__ = 'agc_match'
    __table_args__ = (UniqueConstraint('agc_exposure_id', 'agc_camera_id', 'spot_id'),
                      ForeignKeyConstraint(['agc_exposure_id', 'agc_camera_id', 'spot_id'],
                                           ['agc_data.agc_exposure_id', 'agc_data.agc_camera_id', 'agc_data.spot_id']),
                      {})

    agc_exposure_id = Column(Integer,
                             primary_key=True, unique=False, autoincrement=False,
                             comment='AGC exposure number identifier')
    agc_camera_id = Column(Integer,
                           primary_key=True, unique=False, autoincrement=False,
                           comment='AGC camera identifier')
    spot_id = Column(Integer,
                     primary_key=True, unique=False, autoincrement=False,
                     comment='The AGC spot identifier')
    pfs_design_id = Column(BigInteger,
                           comment='pfsDesignId')
    guide_star_id = Column(BigInteger,
                           comment='GuideStar identifier')
    agc_nominal_x_mm = Column(REAL,
                              comment='Nominal designed x-position on the AGC [PFI mm]')
    agc_nominal_y_mm = Column(REAL,
                              comment='Nominal designed y-position on the AGC [PFI mm]')
    agc_center_x_mm = Column(REAL,
                             comment='Center measured x-position on the AGC [PFI mm]')
    agc_center_y_mm = Column(REAL,
                             comment='Center measured y-position on the AGC [PFI mm]')
    flags = Column(Integer, comment='Flags')

    def __init__(self, agc_exposure_id, spot_id, agc_camera_id,
                 pfs_design_id, guide_star_id,
                 agc_nominal_x_mm, agc_nominal_y_mm,
                 agc_center_x_mm, agc_center_y_mm,
                 flags):
        self.agc_exposure_id = agc_exposure_id
        self.spot_id = spot_id
        self.agc_camera_id = agc_camera_id
        self.pfs_design_id = pfs_design_id
        self.guide_star_id = guide_star_id
        self.agc_nominal_x_mm = agc_nominal_x_mm
        self.agc_nominal_y_mm = agc_nominal_y_mm
        self.agc_center_x_mm = agc_center_x_mm
        self.agc_center_y_mm = agc_center_y_mm
        self.flags = flags


class agc_guide_offset(Base):
    ''' Provides the final guide offset
    '''

    __tablename__ = 'agc_guide_offset'

    agc_exposure_id = Column(Integer, ForeignKey('agc_exposure.agc_exposure_id'),
                             primary_key=True, autoincrement=False,
                             comment='AGC exposure number identifier')
    guide_ra = Column(FLOAT,
                      comment='The designed FoV R.A. center [deg.]')
    guide_dec = Column(FLOAT,
                       comment='The designed FoV Dec. center [deg.]')
    guide_pa = Column(REAL,
                      comment='The designed FoV PA [deg.]')
    guide_delta_ra = Column(REAL,
                            comment='The calculated FoV R.A. offset [arcsec.]')
    guide_delta_dec = Column(REAL,
                             comment='The calculated FoV Dec. offset [arcsec.]')
    guide_delta_insrot = Column(REAL,
                                comment='The calculated InsRot offset [arcsec.]')
    guide_delta_scale = Column(REAL,
                               comment='The calculated scale offset [arcsec.]')
    guide_delta_az = Column(REAL,
                            comment='The calculated Az offset [arcsec.] (optional)')
    guide_delta_el = Column(REAL,
                            comment='The calculated El offset [arcsec.] (optional)')
    guide_delta_z = Column(REAL,
                           comment='The calculated focus offset [mm]')
    guide_delta_z1 = Column(REAL,
                            comment='The calculated focus offset for AGC1 [mm]')
    guide_delta_z2 = Column(REAL,
                            comment='The calculated focus offset for AGC2 [mm]')
    guide_delta_z3 = Column(REAL,
                            comment='The calculated focus offset for AGC3 [mm]')
    guide_delta_z4 = Column(REAL,
                            comment='The calculated focus offset for AGC4 [mm]')
    guide_delta_z5 = Column(REAL,
                            comment='The calculated focus offset for AGC5 [mm]')
    guide_delta_z6 = Column(REAL,
                            comment='The calculated focus offset for AGC6 [mm]')
    mask = Column(Integer,
                  comment='A mask of the active elements being fit')

    agc_exposure = relationship('agc_exposure', back_populates='agc_guide_offset')

    def __init__(self, agc_exposure_id, guide_ra, guide_dec, guide_pa,
                 guide_delta_ra, guide_delta_dec, guide_delta_insrot, guide_delta_scale,
                 guide_delta_az, guide_delta_el, guide_delta_z,
                 guide_delta_z1, guide_delta_z2, guide_delta_z3, guide_delta_z4, guide_delta_z5, guide_delta_z6,
                 mask):
        self.agc_exposure_id = agc_exposure_id
        self.guide_ra = guide_ra
        self.guide_dec = guide_dec
        self.guide_pa = guide_pa
        self.guide_delta_ra = guide_delta_ra
        self.guide_delta_dec = guide_delta_dec
        self.guide_delta_insrot = guide_delta_insrot
        self.guide_delta_scale = guide_delta_scale
        self.guide_delta_az = guide_delta_az
        self.guide_delta_el = guide_delta_el
        self.guide_delta_z = guide_delta_z
        self.guide_delta_z1 = guide_delta_z1
        self.guide_delta_z2 = guide_delta_z2
        self.guide_delta_z3 = guide_delta_z3
        self.guide_delta_z4 = guide_delta_z4
        self.guide_delta_z5 = guide_delta_z5
        self.guide_delta_z6 = guide_delta_z6
        self.mask = mask


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
