"""empty message

Revision ID: a1c17effff1d
Revises: 1c6f7e989021
Create Date: 2017-04-19 05:17:26.020254

"""

# revision identifiers, used by Alembic.
revision = 'a1c17effff1d'
down_revision = '1c6f7e989021'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql


def upgrade():
    # commands auto generated by Alembic - please adjust! #
    op.rename_table('activity', 'activities')
    op.rename_table('custom_placeholder', 'custom_placeholders')
    op.rename_table('custom_sys_role', 'custom_sys_roles')
    op.rename_table('email_notification', 'email_notifications')
    op.rename_table('event_copyright', 'event_copyrights')
    op.rename_table('microlocation', 'microlocations')
    op.rename_table('role_invite', 'role_invites')
    op.rename_table('role', 'roles')
    op.rename_table('service','services')
    op.rename_table('session_type', 'session_types')
    op.rename_table('session', 'sessions')
    op.rename_table('session_version', 'sessions_version')
    op.rename_table('ticket', 'tickets')
    op.rename_table('eventsusers', 'event_user')
    op.rename_table('social_link', 'social_links')

    op.alter_column('message_settings', 'notif_status', new_column_name='notification_status')
    op.alter_column('notification', 'has_read', new_column_name='is_read')
    op.alter_column('tax', 'send_invoice', new_column_name='is_invoice_sent')
    op.alter_column('tax', 'tax_include_in_price', new_column_name='is_tax_included_in_price')
    op.alter_column('ticket_holders', 'checked_in', new_column_name='is_checked_in')
    op.alter_column('user', 'created_date', new_column_name='created_at')
    op.alter_column('tickets', 'absorb_fees', new_column_name='is_fee_absorbed')
    op.alter_column('role_invites', 'create_time', new_column_name='created_at')
    op.alter_column('role_invites', 'declined', new_column_name='is_declined')
    op.alter_column('sessions', 'state_email_sent', new_column_name='is_mail_sent')
    op.alter_column('sessions_version', 'state_email_sent', new_column_name='is_mail_sent')

    op.drop_constraint(u'association_ticket_id_fkey', 'association', type_='foreignkey')
    op.create_foreign_key(u'association_ticket_id_fkey', 'association', 'tickets', ['ticket_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(u'booked_ticket_ticket_id_fkey', 'booked_ticket', type_='foreignkey')
    op.create_foreign_key(u'booked_ticket_ticket_id_fkey', 'booked_ticket', 'tickets', ['ticket_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(u'invites_session_id_fkey', 'invites', type_='foreignkey')
    op.create_foreign_key(u'invites_session_id_fkey', 'invites', 'sessions', ['session_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(u'orders_tickets_ticket_id_fkey', 'orders_tickets', type_='foreignkey')
    op.create_foreign_key(u'orders_tickets_ticket_id_fkey', 'orders_tickets', 'tickets', ['ticket_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(u'panel_permissions_role_id_fkey', 'panel_permissions', type_='foreignkey')
    op.create_foreign_key(u'panel_permissions_role_id_fkey', 'panel_permissions', 'custom_sys_roles', ['role_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(u'permissions_role_id_fkey', 'permissions', type_='foreignkey')
    op.drop_constraint(u'permissions_service_id_fkey', 'permissions', type_='foreignkey')
    op.create_foreign_key(u'permissions_service_id_fkey', 'permissions', 'services', ['service_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(u'permissions_role_id_fkey', 'permissions', 'roles', ['role_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(u'speakers_sessions_session_id_fkey', 'speakers_sessions', type_='foreignkey')
    op.create_foreign_key(u'speakers_sessions_session_id_fkey', 'speakers_sessions', 'sessions', ['session_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(u'ticket_holders_ticket_id_fkey', 'ticket_holders', type_='foreignkey')
    op.create_foreign_key(u'ticket_holders_ticket_id_fkey', 'ticket_holders', 'tickets', ['ticket_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(u'user_system_role_role_id_fkey', 'user_system_role', type_='foreignkey')
    op.create_foreign_key(u'user_system_role_role_id_fkey', 'user_system_role', 'custom_sys_roles', ['role_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(u'users_events_roles_role_id_fkey', 'users_events_roles', type_='foreignkey')
    op.create_foreign_key(u'users_events_roles_role_id_fkey', 'users_events_roles', 'roles', ['role_id'], ['id'], ondelete='CASCADE')
    ### end Alembic commands ###


def downgrade():
    # commands auto generated by Alembic - please adjust! #
    op.rename_table('activities', 'activity')
    op.rename_table('custom_placeholders', 'custom_placeholder')
    op.rename_table('custom_sys_roles', 'custom_sys_role')
    op.rename_table('email_notifications', 'email_notification')
    op.rename_table('event_copyrights', 'event_copyright')
    op.rename_table('microlocations', 'microlocation')
    op.rename_table('role_invites', 'role_invite')
    op.rename_table('roles', 'role')
    op.rename_table('services', 'service')
    op.rename_table('session_types', 'session_type')
    op.rename_table('sessions', 'session')
    op.rename_table('sessions_version', 'session_version')
    op.rename_table('tickets', 'ticket')
    op.rename_table('event_user', 'eventsusers')
    op.rename_table('social_links', 'social_link')

    op.alter_column('message_settings', 'notification_status', new_column_name='notif_status')
    op.alter_column('notification', 'is_read', new_column_name='has_read')
    op.alter_column('tax', 'is_invoice_sent', new_column_name='send_invoice')
    op.alter_column('tax', 'is_tax_included_in_price', new_column_name='tax_include_in_price')
    op.alter_column('ticket_holders', 'is_checked_in', new_column_name='checked_in')
    op.alter_column('user', 'created_at', new_column_name='created_date')
    op.alter_column('ticket', 'is_fee_absorbed', new_column_name='absorb_fees')
    op.alter_column('role_invite', 'created_at', new_column_name='create_time')
    op.alter_column('role_invite', 'is_declined', new_column_name='declined')
    op.alter_column('session', 'is_mail_sent', new_column_name='state_email_sent')
    op.alter_column('session_version', 'is_mail_sent', new_column_name='state_email_sent')

    op.drop_constraint(u'user_system_role_role_id_fkey', 'user_system_role', type_='foreignkey')
    op.drop_constraint(u'users_events_roles_role_id_fkey', 'users_events_roles', type_='foreignkey')
    op.create_foreign_key(u'users_events_roles_role_id_fkey', 'users_events_roles', 'role', ['role_id'], ['id'], ondelete=u'CASCADE')
    op.create_foreign_key(u'user_system_role_role_id_fkey', 'user_system_role', 'custom_sys_role', ['role_id'], ['id'], ondelete=u'CASCADE')
    op.drop_constraint(u'ticket_holders_ticket_id_fkey', 'ticket_holders', type_='foreignkey')
    op.create_foreign_key(u'ticket_holders_ticket_id_fkey', 'ticket_holders', 'ticket', ['ticket_id'], ['id'], ondelete=u'CASCADE')
    op.drop_constraint(u'speakers_sessions_session_id_fkey', 'speakers_sessions', type_='foreignkey')
    op.create_foreign_key(u'speakers_sessions_session_id_fkey', 'speakers_sessions', 'session', ['session_id'], ['id'], ondelete=u'CASCADE')
    op.drop_constraint(u'permissions_service_id_fkey', 'permissions', type_='foreignkey')
    op.drop_constraint(u'permissions_role_id_fkey', 'permissions', type_='foreignkey')
    op.create_foreign_key(u'permissions_service_id_fkey', 'permissions', 'service', ['service_id'], ['id'], ondelete=u'CASCADE')
    op.create_foreign_key(u'permissions_role_id_fkey', 'permissions', 'role', ['role_id'], ['id'], ondelete=u'CASCADE')
    op.drop_constraint(u'panel_permissions_role_id_fkey', 'panel_permissions', type_='foreignkey')
    op.create_foreign_key(u'panel_permissions_role_id_fkey', 'panel_permissions', 'custom_sys_role', ['role_id'], ['id'], ondelete=u'CASCADE')
    op.drop_constraint(u'orders_tickets_ticket_id_fkey', 'orders_tickets', type_='foreignkey')
    op.create_foreign_key(u'orders_tickets_ticket_id_fkey', 'orders_tickets', 'ticket', ['ticket_id'], ['id'], ondelete=u'CASCADE')
    op.drop_constraint(u'invites_session_id_fkey', 'invites', type_='foreignkey')
    op.create_foreign_key(u'invites_session_id_fkey', 'invites', 'session', ['session_id'], ['id'], ondelete=u'CASCADE')
    op.drop_constraint(u'booked_ticket_ticket_id_fkey', 'booked_ticket', type_='foreignkey')
    op.create_foreign_key(u'booked_ticket_ticket_id_fkey', 'booked_ticket', 'ticket', ['ticket_id'], ['id'], ondelete=u'CASCADE')
    op.drop_constraint(u'association_ticket_id_fkey', 'association', type_='foreignkey')
    op.create_foreign_key(u'association_ticket_id_fkey', 'association', 'ticket', ['ticket_id'], ['id'], ondelete=u'CASCADE')
    ### end Alembic commands ###
