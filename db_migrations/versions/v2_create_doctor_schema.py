"""Create Doctor Schema

Create a new schema object named 'doctor' which represents all the doctors in the entire application.

-- SQL

CREATE TABLE doctor (
    id SERIAL,
    root_id INTEGER NOT NULL,
    professional_statement TEXT NOT NULL,
    practicing_from TIMESTAMP NOT NULL,
    CONSTRAINT pk_doctor PRIMARY KEY (id),
    CONSTRAINT uc_doctor_root_id UNIQUE (root_id)
);

"""

import sqlalchemy as sa
from alembic import op

revision = 'v2'
down_revision = 'v1'


def upgrade():
    # Create new 'doctor' table
    op.create_table(
        'doctor',  # Table Name
        sa.Column('id', sa.Integer, autoincrement=True),
        sa.Column('root_id', sa.Integer, nullable=False),
        sa.Column('professional_statement', sa.Text, nullable=False),
        sa.Column('practicing_from', sa.DateTime, nullable=False),

        # Constraints Definition
        sa.PrimaryKeyConstraint('id', name='pk_doctor'),  # Primary Key
        sa.UniqueConstraint('root_id', name='uc_doctor_root_id'),
    )


def downgrade():
    # Drop 'doctor' table
    op.drop_table('doctor')
