"""add data_processing

Revision ID: 24b802710f00
Revises: 1fccd2414131
Create Date: 2022-08-22 13:31:16.042470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24b802710f00'
down_revision = '1fccd2414131'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reduced_visits',
                    sa.Column('pfs_visit_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('is_ingested', sa.Boolean(), nullable=True, comment='ingested?'),
                    sa.Column('is_isred', sa.Boolean(), nullable=True, comment='ISRed?'),
                    sa.Column('is_reduced', sa.Boolean(), nullable=True, comment='reduceExposure.py done?'),
                    sa.Column('is_merged', sa.Boolean(), nullable=True, comment='pfsArm merged?'),
                    sa.Column('is_calibrated', sa.Boolean(), nullable=True, comment='flux calibrated?'),
                    sa.Column('is_coadded', sa.Boolean(), nullable=True, comment='coadded?'),
                    sa.Column('updated_at', sa.DateTime(), nullable=True, comment='datetime of the table update'),
                    sa.PrimaryKeyConstraint('pfs_visit_id'),
                    sa.UniqueConstraint('pfs_visit_id')
                    )
    op.create_table('data_processing',
                    sa.Column('run_id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('pfs_visit_id', sa.Integer(), nullable=True, comment='PFS visit identifier'),
                    sa.Column('run_description', sa.String(), nullable=True, comment='description of the processing run'),
                    sa.Column('run_status', sa.String(), nullable=True, comment='status of the processing run'),
                    sa.Column('run_datetime_start', sa.DateTime(), nullable=True, comment='datetime of the processing run start'),
                    sa.Column('run_datetime_end', sa.DateTime(), nullable=True, comment='datetime of the processing run end'),
                    sa.ForeignKeyConstraint(['pfs_visit_id'], ['reduced_visits.pfs_visit_id'], ),
                    sa.PrimaryKeyConstraint('run_id'),
                    sa.UniqueConstraint('run_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_processing')
    op.drop_table('reduced_visits')
    # ### end Alembic commands ###
