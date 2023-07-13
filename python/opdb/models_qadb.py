from sqlalchemy import create_engine
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, DateTime, Boolean, REAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import UniqueConstraint, ForeignKeyConstraint

Base = declarative_base()


class test(Base):
    __tablename__ = 'test'

    test_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    test_val1 = Column(Integer, comment='test_val1')
    test_val2 = Column(REAL, comment='test_val2')
    test_val3 = Column(String, comment='test_val3')
    test_val4 = Column(DateTime, comment='test_val4')

    def __init__(self, test_val1, test_val2, test_val3, test_val4):
        self.test_val1 = test_val1
        self.test_val2 = test_val2
        self.test_val3 = test_val3
        self.test_val4 = test_val4


class pfs_visit(Base):
    '''Tracks the Gen2 visit identifier.
    This is the fundamental identifier for all instrument exposures (MCS, AGC, SPS)
    <<<<< copied from opDB models.py >>>>>
    '''
    __tablename__ = 'pfs_visit'

    pfs_visit_id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    pfs_visit_description = Column(String)
    pfs_design_id = Column(BigInteger)
    issued_at = Column(DateTime, comment='Issued time [YYYY-MM-DDThh:mm:ss]')

    def __init__(self, pfs_visit_id, pfs_visit_description, pfs_design_id, issued_at):
        self.pfs_visit_id = pfs_visit_id
        self.pfs_visit_description = pfs_visit_description
        self.pfs_design_id = pfs_design_id
        self.issued_at = issued_at


class seeing(Base):
    '''Statistics of seeing during a single exposure
    '''
    __tablename__ = 'seeing'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False)
    seeing_mean = Column(REAL, comment='seeing FWHM mean (arcsec.)')
    seeing_median = Column(REAL, comment='seeing FWHM median (arcsec.)')
    seeing_sigma = Column(REAL, comment='seeing FWHM sigma (arcsec.)')

    def __init__(self,
                 pfs_visit_id,
                 seeing_mean,
                 seeing_median,
                 seeing_sigma,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.seeing_mean = seeing_mean
        self.seeing_median = seeing_median
        self.seeing_sigma = seeing_sigma


class transparency(Base):
    '''Statistics of transparency during a single exposure
    '''
    __tablename__ = 'transparency'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False)
    transparency_mean = Column(REAL, comment='transparency mean')
    transparency_median = Column(REAL, comment='transparency median')
    transparency_sigma = Column(REAL, comment='transparency sigma')

    def __init__(self,
                 pfs_visit_id,
                 transparency_mean,
                 transparency_median,
                 transparency_sigma,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.transparency_mean = transparency_mean
        self.transparency_median = transparency_median
        self.transparency_sigma = transparency_sigma


class throughput(Base):
    '''Instrumental throughput for the visit
    '''
    __tablename__ = 'throughput'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False)
    throughput_mean = Column(REAL, comment='the instrumental throughput (mean)')
    throughput_median = Column(REAL, comment='the instrumental throughput (median)')
    throughput_sigma = Column(REAL, comment='the instrumental throughput (sigma)')

    def __init__(self,
                 pfs_visit_id,
                 throughput_mean,
                 throughput_median,
                 throughput_sigma,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.throughput_mean = throughput_mean
        self.throughput_median = throughput_median
        self.throughput_sigma = throughput_sigma


class noise(Base):
    '''Background noise level for the visit
    '''
    __tablename__ = 'noise'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False)
    noise_mean = Column(REAL, comment='the background noise in electron/pix? (mean)')
    noise_median = Column(REAL, comment='the background noise in electron/pix? (median)')
    noise_sigma = Column(REAL, comment='the background noise in electron/pix? (sigma)')

    def __init__(self,
                 pfs_visit_id,
                 noise_mean,
                 noise_median,
                 noise_sigma,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.noise_mean = noise_mean
        self.noise_median = noise_median
        self.noise_sigma = noise_sigma


class moon(Base):
    '''Information on the moon for the visit
    '''
    __tablename__ = 'moon'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False)
    moon_phase = Column(REAL, comment='moon phase')
    moon_alt = Column(REAL, comment='moon altitude (deg.)')
    moon_sep = Column(REAL, comment='moon separation to the pointing (deg.)')

    def __init__(self,
                 pfs_visit_id,
                 moon_phase,
                 moon_alt,
                 moon_sep,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.moon_phase = moon_phase
        self.moon_alt = moon_alt
        self.moon_sep = moon_sep


class sky(Base):
    '''Information on the sky background level for the visit
    '''
    __tablename__ = 'sky'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False)
    sky_background_mean = Column(REAL,
                                 comment='the mean sky background level averaged over the FoV/fibers (counts)')
    sky_background_median = Column(REAL,
                                   comment='the median sky background level averaged over the FoV/fibers (counts)')
    sky_background_sigma = Column(REAL,
                                  comment='the sigma of the sky background level (counts)')
    wavelength_ref = Column(REAL,
                            comment='the reference wavelength to measure the sky background level (nm)')

    def __init__(self,
                 pfs_visit_id,
                 sky_background_mean,
                 sky_background_median,
                 sky_background_sigma,
                 wavelength_ref,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.sky_background_mean = sky_background_mean
        self.sky_background_median = sky_background_median
        self.sky_background_sigma = sky_background_sigma
        self.wavelength_ref = wavelength_ref


class telescope(Base):
    '''Information on the telescope status
    '''
    __tablename__ = 'telescope'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False)
    azimuth = Column(REAL, comment='the average telescope azimuth during the exposure (deg.)')
    altitude = Column(REAL, comment='the average telescope altitude during the exposure (deg.)')
    airmass = Column(REAL, comment='the average airmass during the exposure (deg.)')

    def __init__(self,
                 pfs_visit_id,
                 azimuth,
                 altitude,
                 airmass,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.azimuth = azimuth
        self.altitude = altitude
        self.airmass = airmass


class cobra_convergence(Base):
    '''Quality of the cobra convergence for the visit
    '''
    __tablename__ = 'cobra_convergence'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False)
    number_converged = Column(Integer, comment='the number of converged targets within the threshold')
    residual_mean = Column(REAL,
                           comment='the mean residual of fiber configuration (um)')
    residual_median = Column(REAL,
                             comment='the median residual of fiber configuration (um)')
    residual_sigma = Column(REAL,
                            comment='the sigma of the residual of fiber configuration (um)')

    def __init__(self,
                 pfs_visit_id,
                 number_converged,
                 residual_mean,
                 residual_median,
                 residual_sigma,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.number_converged = number_converged
        self.residual_mean = residual_mean
        self.residual_median = residual_median
        self.residual_sigma = residual_sigma


class guide_offset(Base):
    '''Statistics of the AGC guide errors during the exposure
    '''
    __tablename__ = 'guide_offset'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False)
    number_guide_stars = Column(Integer, comment='the number of guide targets used')
    offset_mean = Column(REAL,
                           comment='the mean guide offset during the exposure (arcsec)')
    offset_median = Column(REAL,
                             comment='the median guide offset during the exposure (arcsec)')
    offset_sigma = Column(REAL,
                            comment='the sigma of the guide offset during the exposure (arcsec)')

    def __init__(self,
                 pfs_visit_id,
                 number_guide_stars,
                 offset_mean,
                 offset_median,
                 offset_sigma,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.number_guide_stars = number_guide_stars
        self.offset_mean = offset_mean
        self.offset_median = offset_median
        self.offset_sigma = offset_sigma


class exposure_time(Base):
    '''Information on the exposure_time for the visit
    '''
    __tablename__ = 'exposure_time'

    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'),
                          primary_key=True, unique=True, autoincrement=False)
    nominal_exposure_time = Column(REAL, comment='the nominal exposure time (sec.)')
    effective_exposure_time = Column(REAL,
                                     comment='the effective exposure time inferred with the observed condition (sec.)')

    def __init__(self,
                 pfs_visit_id,
                 nominal_exposure_time,
                 effective_exposure_time,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.nominal_exposure_time = nominal_exposure_time
        self.effective_exposure_time = effective_exposure_time


''' DRP QA tables '''

class data_processing(Base):
    '''Information of the pipeline processing
    '''
    __tablename__ = 'data_processing'

    run_id = Column(Integer,
                    primary_key=True,
                    unique=True,
                    autoincrement=True)
    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'))
    drp_id = Column(Integer,
                    comment='DRPxD to process the data (x=1/2)')
    drp_version = Column(String,
                         comment='DRP version (e.g., w.2023.20 (DRP2D), 0.40.0 (DRP1D) )')
    process_type = Column(String,
                         comment='the type of DRP processing (e.g., reduceExposure, mergeArms, etc.)')
    process_datetime_start = Column(DateTime,
                                comment='datetime of the processing run start')
    process_datetime_end = Column(DateTime,
                              comment='datetime of the processing run end')

    def __init__(self,
                 pfs_visit_id,
                 drp_id,
                 drp_version,
                 process_type,
                 process_datetime_start,
                 process_datetime_end,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.drp_id = drp_id
        self.drp_version = drp_version
        self.process_type = process_type
        self.process_datetime_start = process_datetime_start
        self.process_datetime_end = process_datetime_end

class data_processing_results(Base):
    '''Information on the data processing results
    '''
    __tablename__ = 'data_processing_results'

    run_id = Column(Integer, ForeignKey('data_processing.run_id'),
                    primary_key=True,
                    unique=False,
                    autoincrement=False
                    )
    tbd = Column(REAL,
                 comment='TBD')

    def __init__(self,
                 run_id,
                 tbd,
                 ):
        self.run_id = run_id
        self.tbd = tbd

class data_qa(Base):
    '''Information of the pipeline processing
    '''
    __tablename__ = 'data_qa'

    run_id = Column(Integer,
                    primary_key=True,
                    unique=True,
                    autoincrement=True)
    pfs_visit_id = Column(Integer, ForeignKey('pfs_visit.pfs_visit_id'))
    qa_version = Column(String,
                         comment='QA code version (e.g., xxxxx)')
    qa_type = Column(String,
                         comment='the type of QA processing (e.g., detectorMap, fluxCalibrate, etc.)')
    process_datetime_start = Column(DateTime,
                                comment='datetime of the processing run start')
    process_datetime_end = Column(DateTime,
                              comment='datetime of the processing run end')

    def __init__(self,
                 pfs_visit_id,
                 drp_id,
                 drp_version,
                 process_type,
                 process_datetime_start,
                 process_datetime_end,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.drp_id = drp_id
        self.drp_version = drp_version
        self.process_type = process_type
        self.process_datetime_start = process_datetime_start
        self.process_datetime_end = process_datetime_end


''' 2D DRP '''

class detector_map(Base):
    '''Quality of the detectorMap for the visit
    '''
    __tablename__ = 'detector_map'
    __table_args__ = (UniqueConstraint('run_id', 'spectrograph', 'arm'), {})

    run_id = Column(Integer, ForeignKey('data_qa.run_id'),
                    primary_key=True,
                    unique=False,
                    autoincrement=False
                    )
    spectrograph = Column(Integer,
                          primary_key=True,
                          unique=False,
                          autoincrement=False
                          )
    arm = Column(String(1),
                 primary_key=True,
                 unique=False,
                 autoincrement=False
                 )
    residual_wavelength_mean = Column(REAL,
                                      comment='the mean wavelength residual averaged over fibers (nm)')
    residual_wavelength_median = Column(REAL,
                                        comment='the median wavelength residual averaged over fibers (nm)')
    residual_wavelength_sigma = Column(REAL,
                                       comment='the sigma of the wavelength residual averaged over fibers (nm)')
    residual_trace_mean = Column(REAL,
                                comment='the mean wavelength residual averaged over fibers (nm)')
    residual_trace_median = Column(REAL,
                                   comment='the median wavelength residual averaged over fibers (nm)')
    residual_trace_sigma = Column(REAL,
                                  comment='the sigma of the wavelength residual averaged over fibers (nm)')

    def __init__(self,
                 run_id,
                 arm,
                 residual_wavelength_mean,
                 residual_wavelength_median,
                 residual_wavelength_sigma,
                 residual_trace_mean,
                 residual_trace_median,
                 residual_trace_sigma,
                 ):
        self.run_id = run_id
        self.arm = arm
        self.residual_wavelength_mean = residual_wavelength_mean
        self.residual_wavelength_median = residual_wavelength_median
        self.residual_wavelength_sigma = residual_wavelength_sigma
        self.residual_trace_mean = residual_trace_mean
        self.residual_trace_median = residual_trace_median
        self.residual_trace_sigma = residual_trace_sigma


class sky_subtraction(Base):
    '''Quality of the sky subtraction for the visit
    '''
    __tablename__ = 'sky_subtraction'
    __table_args__ = (UniqueConstraint('run_id', 'spectrograph', 'arm'), {})

    run_id = Column(Integer, ForeignKey('data_qa.run_id'),
                    primary_key=True,
                    unique=False,
                    autoincrement=False
                    )
    spectrograph = Column(Integer,
                          primary_key=True,
                          unique=False,
                          autoincrement=False
                          )
    arm = Column(String(1),
                 primary_key=True,
                 unique=False,
                 autoincrement=False
                 )
    number_of_sky_fibers = Column(Integer,
                                  comment='the number of sky fibers to make the sky model')
    residual_chi_mean = Column(REAL,
                               comment='the mean sky subtraction residual in chi averaged over FoV (counts)')
    residual_chi_median = Column(REAL,
                                 comment='the median sky subtraction residual in chi averaged over FoV (counts)')
    residual_chi_sigma = Column(REAL,
                                comment='the sigma of the sky subtraction residual in chi (counts)')

    def __init__(self,
                 run_id,
                 arm,
                 number_of_sky_fibers,
                 residual_chi_mean,
                 residual_chi_median,
                 residual_chi_sigma,
                 ):
        self.run_id = run_id
        self.arm = arm
        self.number_of_sky_fibers = number_of_sky_fibers
        self.residual_chi_mean = residual_chi_mean
        self.residual_chi_median = residual_chi_median
        self.residual_chi_sigma = residual_chi_sigma
        

class flux_calibration(Base):
    '''Quality of the flux calibration for the visit
    '''
    __tablename__ = 'flux_calibration'
    __table_args__ = (UniqueConstraint('run_id', 'spectrograph', 'arm'), {})

    run_id = Column(Integer, ForeignKey('data_qa.run_id'),
                    primary_key=True,
                    unique=False,
                    autoincrement=False
                    )
    spectrograph = Column(Integer,
                          primary_key=True,
                          unique=False,
                          autoincrement=False
                          )
    arm = Column(String(1),
                 primary_key=True,
                 unique=False,
                 autoincrement=False
                 )
    number_of_flux_standards = Column(Integer,
                                      comment='the number of flux standard stars to calculate the vector')
    tbd = Column(REAL,
                 comment='TBD')

    def __init__(self,
                 run_id,
                 arm,
                 number_of_flux_standards,
                 tbd,
                 ):
        self.run_id = run_id
        self.arm = arm
        self.number_of_flux_standards = number_of_flux_standards
        self.tbd = tbd


class cosmic_rays(Base):
    '''Quality of the cosmic rays detection for the visit
    '''
    __tablename__ = 'cosmic_rays'
    __table_args__ = (UniqueConstraint('run_id', 'spectrograph', 'arm'), {})

    run_id = Column(Integer, ForeignKey('data_qa.run_id'),
                    primary_key=True,
                    unique=False,
                    autoincrement=False
                    )
    spectrograph = Column(Integer,
                          primary_key=True,
                          unique=False,
                          autoincrement=False
                          )
    arm = Column(String(1),
                 primary_key=True,
                 unique=False,
                 autoincrement=False
                 )
    tbd = Column(REAL,
                 comment='TBD')

    def __init__(self,
                 run_id,
                 arm,
                 tbd,
                 ):
        self.run_id = run_id
        self.arm = arm
        self.tbd = tbd


class mask(Base):
    '''Information on the bit masks in the reduced products
    '''
    __tablename__ = 'mask'
    __table_args__ = (UniqueConstraint('run_id', 'spectrograph', 'arm'), {})

    run_id = Column(Integer, ForeignKey('data_qa.run_id'),
                    primary_key=True,
                    unique=False,
                    autoincrement=False
                    )
    spectrograph = Column(Integer,
                          primary_key=True,
                          unique=False,
                          autoincrement=False
                          )
    arm = Column(String(1),
                 primary_key=True,
                 unique=False,
                 autoincrement=False
                 )
    number_of_pix_in_each_bit = Column(Integer,
                                       comment='TBD')

    def __init__(self,
                 run_id,
                 arm,
                 number_of_pix_in_each_bit,
                 ):
        self.run_id = run_id
        self.arm = arm
        self.number_of_pix_in_each_bit = number_of_pix_in_each_bit

class h4_persistence(Base):
    '''Quality of the H4RG persistence correction for the visit
    '''
    __tablename__ = 'h4_persistence'
    __table_args__ = (UniqueConstraint('run_id', 'spectrograph'), {})

    run_id = Column(Integer, ForeignKey('data_qa.run_id'),
                    primary_key=True,
                    unique=False,
                    autoincrement=False
                    )
    spectrograph = Column(Integer,
                          primary_key=True,
                          unique=False,
                          autoincrement=False
                          )
    tbd = Column(REAL,
                 comment='TBD')

    def __init__(self,
                 run_id,
                 spectrograph,
                 tbd,
                 ):
        self.run_id = run_id
        self.spectrograph = spectrograph
        self.tbd = tbd


class dichroic_continuity(Base):
    '''Check the dichroic continuity after merging the arms
    '''
    __tablename__ = 'dichroic_continuity'
    __table_args__ = (UniqueConstraint('run_id', 'spectrograph'), {})

    run_id = Column(Integer, ForeignKey('data_qa.run_id'),
                    primary_key=True,
                    unique=False,
                    autoincrement=False
                    )
    spectrograph = Column(Integer,
                          primary_key=True,
                          unique=False,
                          autoincrement=False
                          )
    br_continuity = Column(REAL,
                    comment='TBD')
    rn_continuity = Column(REAL,
                    comment='TBD')

    def __init__(self,
                 run_id,
                 spectrograph,
                 br_continuity,
                 rn_continuity,
                 ):
        self.run_id = run_id
        self.spectrograph = spectrograph
        self.br_continuity = br_continuity
        self.rn_continuity = rn_continuity
        

''' 1D DRP '''


class redshift_measurement(Base):
    '''Quality of 1D redshift measurements
    '''
    __tablename__ = 'redshift_measurement'

    run_id = Column(Integer, ForeignKey('data_qa.run_id'),
                    primary_key=True,
                    unique=False,
                    autoincrement=False
                    )
    number_of_galaxies = Column(Integer,
                                comment='the number of galaxies classified')
    chisq_mean = Column(REAL,
                        comment='the mean chi^2 in the fitting')
    chisq_median = Column(REAL,
                          comment='the median chi^2 in the fitting')
    chisq_sigma = Column(REAL,
                         comment='the sigma of the chi^2 in the fitting')

    def __init__(self,
                 run_id,
                 number_of_galaxies,
                 chisq_mean,
                 chisq_median,
                 chisq_sigma,
                 ):
        self.run_id = run_id
        self.number_of_galaxies = number_of_galaxies
        self.chisq_mean = chisq_mean
        self.chisq_median = chisq_median
        self.chisq_sigma = chisq_sigma


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
