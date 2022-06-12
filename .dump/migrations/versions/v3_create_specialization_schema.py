"""Create Specialization Schema

Create a table 'specialization' which represents doctors specializations and have a many-to-many relationship with the
doctor table.

-- SQL

CREATE TABLE specialization (
    id SERIAL,
    specialization_name TEXT NOT NULL,
    CONSTRAINT pk_specialization PRIMARY KEY (id)
);

CREATE TABLE doctor_specialization (
    id SERIAL,
    doctor_id INTEGER NOT NULL,
    specialization_id INTEGER NOT NULL,
    CONSTRAINT pk_doctor_specialization PRIMARY KEY (id)
);

"""

import sqlalchemy as sa
from alembic import op

revision = 'v3'
down_revision = 'v2'


def upgrade():
    # Create new 'specialization' table
    op.create_table(
        'specialization',  # Table Name
        sa.Column('id', sa.Integer, autoincrement=True),
        sa.Column('specialization_name', sa.Text, nullable=False),

        # Constraints Definition
        sa.PrimaryKeyConstraint('id', name='pk_doctor')  # Primary Key
    )

    # Create many-to-many relation between 'doctor' and 'specialization' table
    op.create_table(
        'doctor_specialization',  # Table Name
        sa.Column('id', sa.Integer, autoincrement=True),
        sa.Column('doctor_id', sa.Integer, nullable=False),
        sa.Column('specialization_id', sa.Integer, nullable=False),

        # Constraints Definition
        sa.PrimaryKeyConstraint('id', name='pk_doctor_specialization')  # Primary Key
    )


def downgrade():
    # Drop 'specialization' table
    op.drop_table('specialization')

    # Drop many-to-many relation between 'doctor' and 'specialization' table
    op.drop_table('doctor_specialization')
