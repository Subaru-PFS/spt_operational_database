"""add cobra_command

What fps did with each cobra, as opposed to what it thought of the target.  Two
questions with two answers: target_validation_mask is a verdict on a target and so is
only set where there was one, while whether fps commanded a cobra is true or false
whatever the cobra carried.

pfs_config_fiber.cobra_command
    CobraCommand: NOT_COMMANDED (0), CONVERGE, HOME, BLACK_DOT, NOT_SET.  Exclusive and
    exhaustive over the cobras, so a non-zero value means fps drove the cobra and says
    where to.  Zero includes the broken cobras, which are never commanded, and the
    fibers with no cobra at all.

Without it, "which cobras did fps actually move this visit" is not answerable: a broken
cobra parked where it stood and a cobra driven onto its dot both read as a science
target that did not converge.

Revision ID: d7f3a5b21c04
Revises: b4e7c92a1d38
Create Date: 2026-08-06 09:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'd7f3a5b21c04'
down_revision = 'b4e7c92a1d38'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('pfs_config_fiber',
                  sa.Column('cobra_command', sa.Integer(), nullable=True,
                            comment='CobraCommand: what fps did with this cobra. '
                                    '0=NOT_COMMANDED, 1=CONVERGE, 2=HOME, 3=BLACK_DOT, 4=NOT_SET'))

    # Point a reader at the column that says what was done, since this one does not.
    op.alter_column('pfs_config_fiber', 'target_validation_mask',
                    comment='TargetValidation bits: why fps refused this target, 0 if it did not. '
                            'Set only for science target types; see cobra_command for what fps did')


def downgrade():
    op.drop_column('pfs_config_fiber', 'cobra_command')
    op.alter_column('pfs_config_fiber', 'target_validation_mask',
                    comment='TargetValidation bits: why fps refused this target, 0 if it did not')
