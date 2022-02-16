"""Create User Schema

Create a new schema object named 'user' which represents all the users of the entire application. This should include
the login information as well.

-- SQL

CREATE TABLE user (
    id SERIAL,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    address TEXT,
    password TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    last_known_loc TEXT,
    CONSTRAINT pk_user PRIMARY KEY (id),
    CONSTRAINT uc_user_email UNIQUE (email),
    CONSTRAINT uc_user_phone UNIQUE (phone)
);

"""

import sqlalchemy as sa
from alembic import op

revision = 'v1_create_user_schema'
down_revision = None


def upgrade():
    # Create new 'user' table
    op.create_table(
        'user',  # Table Name
        sa.Column('id', sa.Integer, autoincrement=True),
        sa.Column('name', sa.Text, nullable=False),
        sa.Column('email', sa.Text),
        sa.Column('phone', sa.Text),
        sa.Column('address', sa.Text),
        sa.Column('password', sa.Text, nullable=False),
        sa.Column('is_admin', sa.Boolean, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('last_known_loc', sa.Text),

        # Constraints Definition
        sa.PrimaryKeyConstraint('id', name='pk_user'),  # Primary Key
        sa.UniqueConstraint('email', name='uc_user_email'),
        sa.UniqueConstraint('phone', name='uc_user_phone'),
    )


def downgrade():
    # Drop 'user' table
    op.drop_table('user')
