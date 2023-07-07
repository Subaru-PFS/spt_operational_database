"""Added pfs_config.converg_tolerance column

Revision ID: 1cbebc1b27ea
Revises: ecf87508e91f
Create Date: 2023-05-31 15:37:50.263686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cbebc1b27ea'
down_revision = 'ecf87508e91f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('test')
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment='',
    #            existing_nullable=True)
    op.add_column('pfs_config', sa.Column('converg_tolerance', sa.REAL(), nullable=True, comment='Tolerance for convergence [mm]'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pfs_config', 'converg_tolerance')
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment=None,
    #            existing_comment='',
    #            existing_nullable=True)
    # op.create_table('test',
    # sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('value', sa.REAL(), autoincrement=False, nullable=True)
    # )
    # ### end Alembic commands ###