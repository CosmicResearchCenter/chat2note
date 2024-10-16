"""修改apikeys表

Revision ID: a04983012f27
Revises: fd530dceeb0b
Create Date: 2024-10-17 00:21:16.807647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a04983012f27'
down_revision: Union[str, None] = 'fd530dceeb0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apikeys',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('provider', sa.String(length=255), nullable=True),
    sa.Column('api_key', sa.String(length=255), nullable=True),
    sa.Column('config', sa.JSON(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('apikeys')
    # ### end Alembic commands ###
