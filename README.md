# PFS Operational Database (opDB)

## Introduction

## Requirements
* Python 3
* SQLAlchemy
* alembic (optional)

## Contents

* python/opdb
    * models.py: database model
    * utils.py: various functions to talk to database
    * manage.py: various functions to construct database
* diagrams
    * PFS-DAT-IPM003002-01_pfs_schema.pdf: database schema diagram (full version)
    * PFS-DAT-IPM003003-01_pfs_schema_light.pdf: database schema diagram (simplified version)
* alembic/*database_name*
    * alembic.ini
    * alembic/env.py
    * alembic/versions
    * alembic/trash

## opDB API

TBW

## Schema diagram
`diagrams` directory has the schema diagram (ER diagram), both full version and simplified version. The diagrams are generated by using <a href="https://www.schemacrawler.com/" target="_blank">SchemaCrawler</a>. The command to generate the full version is as follows:

```sh
$ schemacrawler.sh --server=postgresql --host=hostname --port=portname --database=dbname --schemas=public --user=username --password=password --info-level=standard --command=schema --log-level=CONFIG  --portable-names  --title='PFS Operational Database'  --output-format=ps2 --output-file=schema.ps --no-remarks
$ ps2pdf schema.ps
```

## Schema management using *alembic* (FOR ONLY DEVELOPERS)

### Preparation

* make a dedicated directory for the database (e.g., `alembic/opdb`) 

__Note that contact opDB manager if you make a new directory__

* copy all files on `alembic/test`

* make sure that both `trash` and `versions` are empty

* make `db.cfg` in the directory where `alembic.ini` exists. This file contains the following string:
```sh
postgres://username:password@hostname:port/dbname
```

__Note that DO NOT commit `db.cfg` on the repository__

* follow the procedure below

### Procedure (for opDB at summit)

* create a JIRA ticket for the update

* make announcement (_Slack_ or _ML_) for the update (currently setting downtime is desirable)

* change SpS AIT log for the plan

* create tag for the repository

* stop the cron job for the regular exposure

* make a backup before you apply the change

* take the following procedure to update opDB with the target schema using `alembic`:

```sh
$ git checkout master
$ python setup.py install
$ cd alembic/database_name
$ alembic revision --autogenerate -m "comments (including e.g. tag, JIRA ticket number)"
# edit the corresponding python script in alembic/versions
$ alembic upgrade head
```

* make sure `alembic_version.version_num` in the database is consistent with your upgrade target

* make announcement / change SpS AIT log status / and close JIRA ticket

## Tests

To test the consistency of relations of models, run the following commands.

```
python -m venv .venv
./.venv/bin/pip install --editable .
./.venv/bin/pip install --editable '.[dev]'
./.venv/bin/pytest
./.venv/bin/pylint --errors-only opdb.models
```

## OBSLOG

### Registration of FITS headers of existing files

```bash
find /data/raw/ -name PFS*.fits | xargs -r ./.venv/bin/python -m opdb.obslog -d postgresql://dbuser@dbhost/dbname --no-echo register --commit-each
```
