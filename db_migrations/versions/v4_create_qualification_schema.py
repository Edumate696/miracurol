"""Create Qualification Schema

Create a table 'qualification' which represents doctors qualifications and have a many-to-one relationship with the
doctor table.

-- SQL

CREATE TABLE qualification (
    id SERIAL,
    doctor_id INTEGER NOT NULL,
    qualification_name TEXT NOT NULL,
    institute_name TEXT,
    procurement_year TIMESTAMP NOT NULL,
    CONSTRAINT pk_qualification PRIMARY KEY (id)
);

"""

import sqlalchemy as sa
from alembic import op

revision = 'v4'
down_revision = 'v3'


def upgrade():
    # Create new 'qualification' table
    op.create_table(
        'qualification',  # Table Name
        sa.Column('id', sa.Integer, autoincrement=True),
        sa.Column('doctor_id', sa.Integer, nullable=False),
        sa.Column('qualification_name', sa.Text, nullable=False),
        sa.Column('institute_name', sa.Text),
        sa.Column('procurement_year', sa.DateTime, nullable=False),

        # Constraints Definition
        sa.PrimaryKeyConstraint('id', name='pk_qualification'),  # Primary Key
    )


def downgrade():
    # Drop 'qualification' table
    op.drop_table('qualification')
