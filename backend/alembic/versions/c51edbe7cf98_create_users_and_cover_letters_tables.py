"""create users and cover_letters tables

Revision ID: c51edbe7cf98
Revises: 
Create Date: 2025-06-05 13:19:27.360682

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid


# revision identifiers, used by Alembic.
revision = 'c51edbe7cf98'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', UUID(as_uuid=True),
                  primary_key=True, default=uuid.uuid4),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('lastname', sa.String(100), nullable=False),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('enabled', sa.Boolean(), nullable=False, default=True),
    )

    op.create_table(
        'cover_letters',
        sa.Column('id', UUID(as_uuid=True),
                  primary_key=True, default=uuid.uuid4),
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey(
            'users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('letter', sa.Text(), nullable=False),
    )

    # Insert test user (password here is in plain text for testing)
    op.execute(
        f"""
        INSERT INTO users (id, name, lastname, email, password, enabled)
        VALUES ('{uuid.uuid4()}', 'Test', 'User', 'test@example.com', 'testpassword', true)
        """
    )


def downgrade():
    op.drop_table('cover_letters')
    op.drop_table('users')
