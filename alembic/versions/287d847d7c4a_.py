"""empty message

Revision ID: d06da34eade6
Revises:
Create Date: 2021-08-27 21:28:20.546282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd06da34eade6'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "Users",
        sa.Column("id", sa.String(100), primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("password", sa.String(100))
    )

def downgrade():
    op.drop_table("Users")