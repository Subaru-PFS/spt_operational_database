"""record the frames each boresight measurement used

mcs_boresight_frame_set
    The MCS frames a boresight was measured from, one row per frame, ids handed out by
    mcs_boresight_frame_set_id_seq.
mcs_boresight_meas.mcs_boresight_frame_set_id
    The frame set of the measurement; NULL on rows written before.
mcs_boresight_meas.calculated_at
    Timezone aware; the rows written before hold UTC.

Revision ID: a4d2f8c61b37
Revises: f3b8d1c6a9e2
Create Date: 2026-11-09 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'a4d2f8c61b37'
down_revision = 'f3b8d1c6a9e2'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(sa.schema.CreateSequence(sa.Sequence('mcs_boresight_frame_set_id_seq')))
    op.create_table('mcs_boresight_frame_set',
                    sa.Column('mcs_boresight_frame_set_id', sa.Integer(), autoincrement=False,
                              nullable=False,
                              comment='Frame set identifier, from mcs_boresight_frame_set_id_seq'),
                    sa.Column('mcs_frame_id', sa.Integer(), autoincrement=False, nullable=False,
                              comment='MCS frame identifier'),
                    sa.ForeignKeyConstraint(['mcs_frame_id'], ['mcs_exposure.mcs_frame_id']),
                    sa.PrimaryKeyConstraint('mcs_boresight_frame_set_id', 'mcs_frame_id'))
    op.add_column('mcs_boresight_meas',
                  sa.Column('mcs_boresight_frame_set_id', sa.Integer(), nullable=True,
                            comment='The frames measured, in mcs_boresight_frame_set; '
                                    'NULL if not recorded'))
    op.alter_column('mcs_boresight_meas', 'calculated_at',
                    existing_type=sa.DateTime(),
                    type_=sa.DateTime(timezone=True),
                    comment='When the measurement was made',
                    existing_comment='When the measurement was made (HST)',
                    existing_nullable=False,
                    postgresql_using="calculated_at AT TIME ZONE 'UTC'")


def downgrade():
    op.alter_column('mcs_boresight_meas', 'calculated_at',
                    existing_type=sa.DateTime(timezone=True),
                    type_=sa.DateTime(),
                    comment='When the measurement was made (HST)',
                    existing_comment='When the measurement was made',
                    existing_nullable=False,
                    postgresql_using="calculated_at AT TIME ZONE 'UTC'")
    op.drop_column('mcs_boresight_meas', 'mcs_boresight_frame_set_id')
    op.drop_table('mcs_boresight_frame_set')
    op.execute(sa.schema.DropSequence(sa.Sequence('mcs_boresight_frame_set_id_seq')))
