"""updated users_messages table

Revision ID: 927aa67ad171
Revises: 0ef4818a8de9
Create Date: 2024-09-20 00:23:45.016585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '927aa67ad171'
down_revision: Union[str, None] = '0ef4818a8de9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_messages', sa.Column('room_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users_messages', 'rooms', ['room_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users_messages', type_='foreignkey')
    op.drop_column('users_messages', 'room_id')
    # ### end Alembic commands ###
