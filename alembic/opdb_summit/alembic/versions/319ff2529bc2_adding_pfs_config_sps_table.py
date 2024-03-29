"""adding pfs_config_sps table

Revision ID: 319ff2529bc2
Revises: a974f0d9b0da
Create Date: 2022-12-12 16:46:17.848475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '319ff2529bc2'
down_revision = 'a974f0d9b0da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pfs_config_sps',
    sa.Column('pfs_visit_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('visit0', sa.Integer(), autoincrement=False, nullable=False, comment='The first visit of the set'),
    sa.ForeignKeyConstraint(['pfs_visit_id'], ['pfs_visit.pfs_visit_id'], ),
    sa.ForeignKeyConstraint(['visit0'], ['pfs_config.visit0'], ),
    sa.PrimaryKeyConstraint('pfs_visit_id', 'visit0'),
    sa.UniqueConstraint('pfs_visit_id', 'visit0')
    )
    # op.drop_table('test')
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment='',
    #            existing_nullable=True)
    op.alter_column('pfs_config', 'pfs_design_id',
               existing_type=sa.BIGINT(),
               nullable=False,
               autoincrement=False)
    op.alter_column('pfs_config', 'visit0',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_comment='The first visit of the set',
               autoincrement=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pfs_config', 'visit0',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_comment='The first visit of the set',
               autoincrement=False)
    op.alter_column('pfs_config', 'pfs_design_id',
               existing_type=sa.BIGINT(),
               nullable=True,
               autoincrement=False)
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment=None,
    #            existing_comment='',
    #            existing_nullable=True)
    # op.create_table('test',
    # sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('value', sa.REAL(), autoincrement=False, nullable=True)
    # )
    op.drop_table('pfs_config_sps')
    # ### end Alembic commands ###
