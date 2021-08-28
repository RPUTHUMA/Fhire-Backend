# -*- coding: utf-8 -*-
"""empty message

Revision ID: 2bdd4dca6987
Revises: d06da34eade6
Create Date: 2021-08-28 00:12:07.945934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bdd4dca6987'
down_revision = 'd06da34eade6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "fhire_job_description",
        sa.Column("id", sa.String(100), primary_key=True),
        sa.Column("designation", sa.String(200)),
        sa.Column("experience", sa.String(100)),
        sa.Column("skill", sa.String(100)),
        sa.Column("role", sa.Text),
        sa.Column("jd", sa.Text),
        sa.Column("skill", sa.String(100)),
        sa.Column("skill", sa.String(100)),
        sa.Column("created_by", sa.String(100)),
        sa.Column("created_on", sa.DateTime),
        sa.Column("last_modified_by", sa.String(100)),
        sa.Column("last_modified_on", sa.DateTime),
        sa.Column("status", sa.String(50), nullable=False),
    )

def downgrade():
    op.drop_table("fhire_job_description")
