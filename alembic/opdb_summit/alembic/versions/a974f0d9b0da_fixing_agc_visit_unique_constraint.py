"""empty message

Revision ID: a974f0d9b0da
Revises: 69f7c10323f8
Create Date: 2022-12-02 18:14:21.945688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a974f0d9b0da'
down_revision = '69f7c10323f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('test')
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment='',
    #            existing_nullable=True)

    op.execute("UPDATE agc_exposure SET pfs_visit_id=0 where (pfs_visit_id=99999 or pfs_visit_id=779594)")
    op.execute("INSERT INTO pfs_visit VALUES (0, 'fake visit, just for convenience', 0, 'now')")
    op.create_foreign_key(None, 'agc_exposure', 'pfs_visit', ['pfs_visit_id'], ['pfs_visit_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_constraint(None, 'agc_exposure', type_='foreignkey')
    # op.alter_column('agc_data', 'image_moment_00_pix',
    #            existing_type=sa.REAL(),
    #            comment=None,
    #            existing_comment='',
    #            existing_nullable=True)
    # op.create_table('test',
    # sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('value', sa.REAL(), autoincrement=False, nullable=True)
    # ### end Alembic commands ###
