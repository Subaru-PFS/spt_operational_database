import re
from pathlib import Path
from typing import Any, Dict, List

import astropy.io.fits as pyfits
from astropy.io.fits.hdu.hdulist import HDUList
from sqlalchemy.orm import Session

from .. import models


def add_fits_headers_from_file(db: Session, filepath: Path):
    db.add_all(fits_headers_from_file(filepath, pfs_visit_id=guess_pfs_visit_id(filepath)))


def fits_headers_from_file(filepath: Path, pfs_visit_id: int):
    with pyfits.open(filepath) as hdul:
        return fits_headers_from_hdulist(hdul, pfs_visit_id, filepath.stem)


def fits_headers_from_hdulist(hdul: HDUList, pfs_visit_id: int, filestem: str):
    records: List[models.obslog_fits_header] = []
    for hdu_index, hdu in enumerate(hdul):
        cards: Dict[str, Any] = {}
        for name, value, _ in hdu.header.cards:
            cards.setdefault(name, []).append(value)
        record = models.obslog_fits_header(
            pfs_visit_id=pfs_visit_id,
            filestem=filestem,
            hdu_index=hdu_index,
            cards_dict={name: value[0] for name, value in cards.items()
                        if len(value) == 1 and
                        not isinstance(value[0], pyfits.Undefined)},
            cards_list=[list(card) for card in hdu.header.cards if not isinstance(card[1], pyfits.Undefined)],
        )
        records.append(record)
    return records


def guess_pfs_visit_id(filepath: Path):
    filestem = filepath.stem  # PFSA01967811 or PFSC06879100.fits
    m = re.match(r'PFS[A-D](\d{6})\d{2}$', filestem)
    if m is None:
        raise RuntimeError(f'Unexpected filename format: {filepath}')
    return int(m.group(1))
