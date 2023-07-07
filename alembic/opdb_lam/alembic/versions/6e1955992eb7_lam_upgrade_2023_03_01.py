"""LAM upgrade 2023-03-01

Revision ID: 6e1955992eb7
Revises: dc5b82266e56
Create Date: 2023-03-01 16:51:50.236288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e1955992eb7'
down_revision = 'dc5b82266e56'
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
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment='',
    #            existing_nullable=True)
    op.add_column('pfs_config_fiber', sa.Column('pfi_nominal_final_x_mm', sa.REAL(), nullable=True))
    op.add_column('pfs_config_fiber', sa.Column('pfi_nominal_final_y_mm', sa.REAL(), nullable=True))
    op.add_column('pfs_design', sa.Column('variant', sa.Integer(), nullable=False, comment='Counter of which variant of `designId0` we are. Requires `designId0`'))
    op.add_column('pfs_design', sa.Column('design_id0', sa.BigInteger(), nullable=False, comment='pfsDesignId of the pfsDesign we are a variant of. Requires `variant`'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pfs_design', 'design_id0')
    op.drop_column('pfs_design', 'variant')
    op.drop_column('pfs_config_fiber', 'pfi_nominal_final_y_mm')
    op.drop_column('pfs_config_fiber', 'pfi_nominal_final_x_mm')
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment=None,
    #            existing_comment='',
    #            existing_nullable=True)
    op.drop_table('pfs_config_sps')
    # ### end Alembic commands ###