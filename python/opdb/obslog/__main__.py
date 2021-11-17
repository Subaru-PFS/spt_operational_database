import logging
from pathlib import Path
from typing import List

import sqlalchemy
from astropy.io.fits.util import ignore_sigint
from opdb import models
from opdb.obslog import add_fits_headers_from_file
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session

logger = logging.getLogger(__name__)


def main():
    import argparse

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    parser = argparse.ArgumentParser()
    parser.add_argument('--db-url', '-d', required=True)
    parser.add_argument('--no-echo', dest='echo', default=True, action='store_false')
    parser.set_defaults(action=lambda: parser.print_help())

    subparsers = parser.add_subparsers()

    register_parser = subparsers.add_parser('register')
    register_parser.add_argument('file', nargs='+', type=Path)
    register_parser.add_argument('--commit-each', action='store_true')
    register_parser.set_defaults(action=lambda: register_files(db, args.file, args.commit_each))

    schema_parser = subparsers.add_parser('create-table')
    schema_parser.set_defaults(action=lambda: create_table(engine))

    args = parser.parse_args()

    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO)

    engine = create_engine(args.db_url, echo=args.echo)
    SessionClass = sessionmaker(engine)
    db = SessionClass()

    args.action()


def register_files(db: Session, files: List[Path], commit_each: bool):
    for file in files:
        logger.info(f'registering {file}...')
        add_fits_headers_from_file(db, file)
        if commit_each:
            try:
                db.commit()
            except sqlalchemy.exc.IntegrityError:
                db.rollback()
        db.commit()


def create_table(engine: Engine):
    tables = [models.obslog_fits_header]
    for table in tables:
        models.Base.metadata.create_all(engine, tables=[table.__table__])


if __name__ == '__main__':
    main()
