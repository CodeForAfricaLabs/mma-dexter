"""initial sync with alembic

Revision ID: 437e0ac0a455
Revises: None
Create Date: 2015-03-24 16:42:05.596131

"""

# revision identifiers, used by Alembic.
revision = '437e0ac0a455'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_affiliations_code', 'affiliations', ['code'], unique=False)
    op.create_index('ix_affiliations_country_id', 'affiliations', ['country_id'], unique=False)
    op.create_index('ix_affiliations_name', 'affiliations', ['name'], unique=False)
    op.drop_index('ix_individuals_name', table_name='affiliations')
    op.alter_column('document_entities', 'doc_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.create_index('ix_document_fairness_bias_favour_affiliation_id', 'document_fairness', ['bias_favour_affiliation_id'], unique=False)
    op.create_index('ix_document_fairness_bias_oppose_affiliation_id', 'document_fairness', ['bias_oppose_affiliation_id'], unique=False)
    op.drop_index('ix_document_fairness_bias_favour_individual_id', table_name='document_fairness')
    op.drop_index('ix_document_fairness_bias_oppose_individual_id', table_name='document_fairness')
    op.create_index('ix_document_places_relevant', 'document_places', ['relevant'], unique=False)
    op.create_index('ix_document_sources_affiliation_id', 'document_sources', ['affiliation_id'], unique=False)
    op.create_index('ix_document_sources_person_id', 'document_sources', ['person_id'], unique=False)
    op.drop_constraint(u'document_sources_ibfk_2', 'document_sources', type_='foreignkey')
    op.drop_constraint(u'documents_ibfk_6', 'documents', type_='foreignkey')
    op.drop_index('ix_document_sources_entity_id', table_name='document_sources')
    op.drop_column('document_sources', 'entity_id')
    op.alter_column('documents', 'origin_location_Id', new_column_name='origin_location_id',
               existing_type=mysql.INTEGER(display_width=11))
    op.drop_index('origin_location_Id', table_name='documents')
    op.create_index('ix_documents_analysis_nature_id', 'documents', ['analysis_nature_id'], unique=False)
    op.create_index('ix_documents_author_id', 'documents', ['author_id'], unique=False)
    op.create_index('ix_documents_checked_by_user_id', 'documents', ['checked_by_user_id'], unique=False)
    op.create_index('ix_documents_country_id', 'documents', ['country_id'], unique=False)
    op.create_index('ix_documents_created_by_user_id', 'documents', ['created_by_user_id'], unique=False)
    op.create_index('ix_documents_document_type_id', 'documents', ['document_type_id'], unique=False)
    op.create_index('ix_documents_flagged', 'documents', ['flagged'], unique=False)
    op.create_index('ix_documents_medium_id', 'documents', ['medium_id'], unique=False)
    op.create_index('ix_documents_origin_location_id', 'documents', ['origin_location_id'], unique=False)
    op.create_index('ix_documents_section', 'documents', ['section'], unique=False)
    op.create_index('ix_documents_topic_id', 'documents', ['topic_id'], unique=False)
    op.create_foreign_key(None, 'documents', 'locations', ['origin_location_id'], ['id'])
    op.create_foreign_key(None, 'issues', 'analysis_natures', ['analysis_nature_id'], ['id'])
    op.create_index('ix_locations_country_id', 'locations', ['country_id'], unique=False)
    op.create_index('ix_mediums_country_id', 'mediums', ['country_id'], unique=False)
    op.create_index('ix_mediums_domain', 'mediums', ['domain'], unique=False)
    op.create_index('ix_topics_analysis_nature_id', 'topics', ['analysis_nature_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    pass
