"""Remove redundant unique constraints

Revision ID: 26a4e346fbf1
Revises: 06febe7976d8
Create Date: 2025-12-22 12:13:14.382321

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '26a4e346fbf1'
down_revision = '06febe7976d8'
branch_labels = None
depends_on = None

drop_constraints = [
    [
        "agc_data",  # Table
        "agc_data_agc_exposure_id_agc_camera_id_spot_id_key",  # Constraint name
        ['agc_exposure_id', 'agc_camera_id', 'spot_id'],  # Columns
        [("agc_match", "agc_match_agc_exposure_id_fkey")]  # Dependent foreign keys
    ],
    [
        "agc_match",
        "agc_match_agc_exposure_id_agc_camera_id_spot_id_key",
        ["agc_exposure_id", "agc_camera_id", "spot_id"],
        []
    ],
    [
        "cobra_match",
        "cobra_match_pfs_visit_id_iteration_cobra_id_key",
        ["pfs_visit_id", 'iteration', 'cobra_id'],
        [("cobra_move", "cobra_move_pfs_visit_id_fkey"), ]
    ],
    [
        "cobra_move",
        "cobra_move_pfs_visit_id_iteration_cobra_id_key",
        ["pfs_visit_id", "iteration", "cobra_id"],
        []
    ],
    [
        "cobra_target",
        "cobra_target_pfs_visit_id_iteration_cobra_id_key",
        ["pfs_visit_id", "iteration", "cobra_id"],
        [("cobra_match", "cobra_match_pfs_visit_id_fkey")]
    ],
    [
        "mcs_data",
        "mcs_data_mcs_frame_id_spot_id_key",
        ["mcs_frame_id", "spot_id"],
        [
            ("cobra_match", "cobra_match_mcs_frame_id_fkey"),
            ("fiducial_fiber_match", "fiducial_fiber_match_mcs_frame_id_fkey")
        ]
    ],
]


def upgrade():
    for constraint in drop_constraints:
        table_name = constraint[0]
        constraint_name = constraint[1]
        columns = constraint[2]
        foreign_keys = constraint[3]
        # Drop dependent foreign key constraints first
        for fk in foreign_keys:
            fk_table = fk[0]
            fk_constraint_name = fk[1]
            op.drop_constraint(
                fk_constraint_name,
                fk_table,
                type_='foreignkey',
            )
        # Now drop the unique constraint
        op.drop_constraint(
            constraint_name,
            table_name,
            type_='unique',
        )
        # Recreate dependent foreign key constraints
        for fk in foreign_keys:
            fk_table = fk[0]
            fk_constraint_name = fk[1]
            op.create_foreign_key(
                fk_constraint_name,
                fk_table,
                table_name,
                local_cols=columns,
                remote_cols=columns,
            )


def downgrade():
    for constraint in drop_constraints:
        table_name = constraint[0]
        constraint_name = constraint[1]
        columns = constraint[2]
        foreign_keys = constraint[3]
        # Drop dependent foreign key constraints first
        for fk in foreign_keys:
            fk_table = fk[0]
            fk_constraint_name = fk[1]
            op.drop_constraint(
                fk_constraint_name,
                fk_table,
                type_='foreignkey',
            )
        # Recreate the unique constraint
        op.create_unique_constraint(
            constraint_name,
            table_name,
            columns,
        )
        # Recreate dependent foreign key constraints
        for fk in foreign_keys:
            fk_table = fk[0]
            fk_constraint_name = fk[1]
            op.create_foreign_key(
                fk_constraint_name,
                fk_table,
                table_name,
                local_cols=columns,
                remote_cols=columns,
            )
