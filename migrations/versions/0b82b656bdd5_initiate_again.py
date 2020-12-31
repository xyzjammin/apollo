"""initiate again

Revision ID: 0b82b656bdd5
Revises: 
Create Date: 2020-11-10 11:05:15.202407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b82b656bdd5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('freefilestackupload',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(length=250), nullable=False),
    sa.Column('file_type', sa.String(length=100), nullable=False),
    sa.Column('file_upload_id', sa.String(length=70), nullable=False),
    sa.Column('file_url', sa.String(length=250), nullable=False),
    sa.Column('file_size', sa.Integer(), nullable=False),
    sa.Column('time_received', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('file_url')
    )
    op.create_index(op.f('ix_freefilestackupload_file_upload_id'), 'freefilestackupload', ['file_upload_id'], unique=False)
    op.create_index(op.f('ix_freefilestackupload_time_received'), 'freefilestackupload', ['time_received'], unique=False)
    op.create_table('freeuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('organization', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=12), nullable=True),
    sa.Column('premium_conversion', sa.Boolean(), nullable=False),
    sa.Column('last_file_share', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_freeuser_email'), 'freeuser', ['email'], unique=True)
    op.create_index(op.f('ix_freeuser_last_file_share'), 'freeuser', ['last_file_share'], unique=False)
    op.create_table('freefileshare',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.String(length=120), nullable=True),
    sa.Column('file_type', sa.String(length=100), nullable=False),
    sa.Column('file_name', sa.String(length=250), nullable=False),
    sa.Column('dashboard_url', sa.String(length=250), nullable=False),
    sa.Column('file_url', sa.String(length=250), nullable=False),
    sa.Column('file_size', sa.Integer(), nullable=True),
    sa.Column('file_upload_id', sa.String(length=70), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('ip_address', sa.String(length=45), nullable=True),
    sa.Column('status', sa.String(length=12), nullable=False),
    sa.Column('stage', sa.String(length=24), nullable=True),
    sa.Column('shares', sa.Integer(), nullable=False),
    sa.Column('downloads', sa.Integer(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=False),
    sa.Column('last_accessed', sa.DateTime(), nullable=True),
    sa.Column('watermarked', sa.Boolean(), nullable=False),
    sa.Column('paid', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['freeuser.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('file_url')
    )
    op.create_index(op.f('ix_freefileshare_created'), 'freefileshare', ['created'], unique=False)
    op.create_index(op.f('ix_freefileshare_dashboard_url'), 'freefileshare', ['dashboard_url'], unique=True)
    op.create_index(op.f('ix_freefileshare_file_upload_id'), 'freefileshare', ['file_upload_id'], unique=False)
    op.create_index(op.f('ix_freefileshare_ip_address'), 'freefileshare', ['ip_address'], unique=False)
    op.create_index(op.f('ix_freefileshare_status'), 'freefileshare', ['status'], unique=False)
    op.create_table('freerecipient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_share_id', sa.Integer(), nullable=False),
    sa.Column('watermarked_file_url', sa.String(length=250), nullable=True),
    sa.Column('file_type', sa.String(length=10), nullable=True),
    sa.Column('invitation_url', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('organization', sa.String(length=100), nullable=True),
    sa.Column('ip_address', sa.String(length=45), nullable=True),
    sa.Column('nda_required', sa.Boolean(), nullable=False),
    sa.Column('nda_signed', sa.Boolean(), nullable=False),
    sa.Column('clicks', sa.Integer(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=False),
    sa.Column('downloads', sa.Integer(), nullable=False),
    sa.Column('last_accessed', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['file_share_id'], ['freefileshare.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('watermarked_file_url')
    )
    op.create_index(op.f('ix_freerecipient_email'), 'freerecipient', ['email'], unique=False)
    op.create_index(op.f('ix_freerecipient_invitation_url'), 'freerecipient', ['invitation_url'], unique=True)
    op.create_index(op.f('ix_freerecipient_ip_address'), 'freerecipient', ['ip_address'], unique=False)
    op.create_table('freenda',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_share_id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('signature', sa.Text(), nullable=False),
    sa.Column('file_url', sa.String(length=250), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['file_share_id'], ['freefileshare.id'], ),
    sa.ForeignKeyConstraint(['recipient_id'], ['freerecipient.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('file_url'),
    sa.UniqueConstraint('signature')
    )
    op.create_table('freeuselog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_share_id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=30), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['file_share_id'], ['freefileshare.id'], ),
    sa.ForeignKeyConstraint(['recipient_id'], ['freerecipient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('freeuselog')
    op.drop_table('freenda')
    op.drop_index(op.f('ix_freerecipient_ip_address'), table_name='freerecipient')
    op.drop_index(op.f('ix_freerecipient_invitation_url'), table_name='freerecipient')
    op.drop_index(op.f('ix_freerecipient_email'), table_name='freerecipient')
    op.drop_table('freerecipient')
    op.drop_index(op.f('ix_freefileshare_status'), table_name='freefileshare')
    op.drop_index(op.f('ix_freefileshare_ip_address'), table_name='freefileshare')
    op.drop_index(op.f('ix_freefileshare_file_upload_id'), table_name='freefileshare')
    op.drop_index(op.f('ix_freefileshare_dashboard_url'), table_name='freefileshare')
    op.drop_index(op.f('ix_freefileshare_created'), table_name='freefileshare')
    op.drop_table('freefileshare')
    op.drop_index(op.f('ix_freeuser_last_file_share'), table_name='freeuser')
    op.drop_index(op.f('ix_freeuser_email'), table_name='freeuser')
    op.drop_table('freeuser')
    op.drop_index(op.f('ix_freefilestackupload_time_received'), table_name='freefilestackupload')
    op.drop_index(op.f('ix_freefilestackupload_file_upload_id'), table_name='freefilestackupload')
    op.drop_table('freefilestackupload')
    # ### end Alembic commands ###
