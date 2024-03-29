"""add sequence_group table

Revision ID: 102a149a18d6
Revises: 9a6d3c101e2c
Create Date: 2022-10-18 19:57:51.270347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '102a149a18d6'
down_revision = '9a6d3c101e2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sequence_group',
    sa.Column('group_id', sa.Integer(), autoincrement=False, nullable=False, comment='Group identifier'),
    sa.Column('group_name', sa.String(), nullable=True, comment='Group name'),
    sa.Column('created_at', sa.DateTime(), nullable=True, comment='Creation time [YYYY-MM-DDThh:mm:ss]'),
    sa.PrimaryKeyConstraint('group_id')
    )
    # op.drop_table('test')
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment='',
    #            existing_nullable=True)
    # op.create_foreign_key(None, 'agc_exposure', 'pfs_visit', ['pfs_visit_id'], ['pfs_visit_id'])
    op.alter_column('iic_sequence', 'group_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_comment='Group identifier')

    op.execute("UPDATE iic_sequence SET group_id = NULL")

    op.create_foreign_key(None, 'iic_sequence', 'sequence_group', ['group_id'], ['group_id'])
    # op.alter_column('pfs_config', 'pfs_design_id',
    #            existing_type=sa.BIGINT(),
    #            nullable=False,
    #            autoincrement=False)
    # op.alter_column('pfs_config', 'visit0',
    #            existing_type=sa.INTEGER(),
    #            nullable=False,
    #            existing_comment='The first visit of the set',
    #            autoincrement=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.alter_column('pfs_config', 'visit0',
    #            existing_type=sa.INTEGER(),
    #            nullable=True,
    #            existing_comment='The first visit of the set',
    #            autoincrement=False)
    # op.alter_column('pfs_config', 'pfs_design_id',
    #            existing_type=sa.BIGINT(),
    #            nullable=True,
    #            autoincrement=False)
    op.drop_constraint(None, 'iic_sequence', type_='foreignkey')
    op.alter_column('iic_sequence', 'group_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_comment='Group identifier')
    # op.drop_constraint(None, 'agc_exposure', type_='foreignkey')
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment=None,
    #            existing_comment='',
    #            existing_nullable=True)
    # op.create_table('test',
    # sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('value', sa.REAL(), autoincrement=False, nullable=True)
    # )
    op.drop_table('sequence_group')
    # ### end Alembic commands ###
