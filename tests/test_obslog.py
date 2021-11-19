import datetime
from pathlib import Path
from typing import Any, Callable, List, Tuple

import astropy.io.fits as pyfits
import numpy
import pytest
from opdb import models
from opdb.obslog import fits_headers_from_file, guess_pfs_visit_id
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

HERE = Path(__file__).parent
db_url_file = HERE / 'secrets' / 'testdb.sample.url'

FitsFromCardsType = Callable[[List[List[Tuple[str, Any, str]]], str], Path]


@pytest.mark.skipif(not db_url_file.exists(), reason='db credentails not provided')
def test_add_fits_headers_from_file(db: Session, pfs_visit_id: int, fits_from_cards: FitsFromCardsType):
    sample_fits = fits_from_cards([[
        ('I_VALUE', 42, 'answer'),
        ('F_VALUE', 3.14, 'pi'),
        ('B_VALUE', True, 'true'),
        ('S_VALUE', 'string', 'string'),
    ]], 'PFSA01967811.fits')
    db.add_all(fits_headers_from_file(sample_fits, pfs_visit_id))

    record = db.query(models.obslog_fits_header).filter(
        models.obslog_fits_header.pfs_visit_id == pfs_visit_id,
    ).one()

    assert record.filestem == 'PFSA01967811'
    assert isinstance(record.cards_dict, dict)
    assert isinstance(record.cards_list, list)
    assert record.cards_dict['I_VALUE'] == 42
    assert record.cards_dict['F_VALUE'] == pytest.approx(3.14)
    assert record.cards_dict['B_VALUE'] is True
    assert record.cards_dict['S_VALUE'] == 'string'


@pytest.mark.parametrize('hdu_index', range(3))
@pytest.mark.parametrize('name_value_cast', [
    ('I_VALUE', 42, lambda c: c.as_integer()),
    ('F_VALUE', 3.14, lambda c: c.as_float()),
    ('S_VALUE', 'hello', lambda c: c.astext),
    ('B_VALUE', True, lambda c: c.as_boolean()),
    ('B_VALUE', False, lambda c: c.as_boolean()),
])
@pytest.mark.skipif(not db_url_file.exists(), reason='db credentails not provided')
def test_query(
    hdu_index: int,
    name_value_cast: Tuple[str, Any, Any],
    db: Session, fits_from_cards: FitsFromCardsType, pfs_visit_id: int,
):
    name, value, cast = name_value_cast
    cards_list = [[] for _ in range(3)]
    cards_list[hdu_index] = [(name, value)]

    sample_fits = fits_from_cards(
        cards_list,
        'PFSA01967811.fits',
    )
    db.add_all(fits_headers_from_file(sample_fits, pfs_visit_id))

    record = db.query(models.obslog_fits_header).filter(
        cast(models.obslog_fits_header.cards_dict[name]) == value,
    ).one()

    assert record.filestem == 'PFSA01967811'
    assert record.hdu_index == hdu_index
    assert isinstance(record.cards_dict, dict)
    assert record.cards_dict[name] == value


def test_guess_pfs_visit_id():
    assert guess_pfs_visit_id(Path('/data/raw/2021-09-12/sps/PFSA06645311.fits')) == 66453
    assert guess_pfs_visit_id(Path('/data/raw/2021-07-18/mcs/PFSC06484800.fits')) == 64848
    with pytest.raises(RuntimeError):
        guess_pfs_visit_id(Path('/error/PFSA123456890000.fits'))


@pytest.fixture
def db():
    engine = create_engine(db_url_file.read_text().strip(), echo=False)
    SessionClass = sessionmaker(engine)
    db = SessionClass()
    try:
        db.query(models.obslog_fits_header).filter(models.obslog_fits_header.pfs_visit_id < 0).delete()
        db.query(models.pfs_visit).filter(models.pfs_visit.pfs_visit_id < 0).delete()
        db.flush()
        yield db
    finally:
        db.rollback()


@pytest.fixture
def pfs_visit_id(db: Session):
    db.add(models.pfs_visit(pfs_visit_id=-1, pfs_visit_description='', pfs_design_id=-1, issued_at=datetime.datetime.now()))
    db.flush()


@pytest.fixture
def fits_from_cards(tmp_path: Path):
    def f(cards_list: List[List[Tuple[str, Any, str]]], filename: str = 'PFSA01967811.fits'):
        fitsfile_path = tmp_path / filename
        pyfits.HDUList([
            pyfits.PrimaryHDU(header=pyfits.Header(cards_list[0])),
            *(pyfits.ImageHDU(numpy.zeros((1, 1)), header=pyfits.Header(cards)) for cards in cards_list[1:]),
        ]).writeto(fitsfile_path)
        return fitsfile_path
    yield f
