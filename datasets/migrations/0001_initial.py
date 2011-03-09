# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Project'
        db.create_table('datasets_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('datasets', ['Project'])

        # Adding model 'Page'
        db.create_table('datasets_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasets.Project'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('image_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('datasets', ['Page'])

        # Adding model 'Record'
        db.create_table('datasets_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('datasets', ['Record'])

        # Adding M2M table for field page on 'Record'
        db.create_table('datasets_record_page', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('record', models.ForeignKey(orm['datasets.record'], null=False)),
            ('page', models.ForeignKey(orm['datasets.page'], null=False))
        ))
        db.create_unique('datasets_record_page', ['record_id', 'page_id'])

        # Adding model 'FieldType'
        db.create_table('datasets_fieldtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasets.Project'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('regex', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('datasets', ['FieldType'])

        # Adding model 'Field'
        db.create_table('datasets_field', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasets.Record'])),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasets.Page'])),
            ('field_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasets.FieldType'])),
            ('image_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('ocr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('matches_rule', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('datasets', ['Field'])

        # Adding model 'FieldSuggestion'
        db.create_table('datasets_fieldsuggestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasets.Field'])),
            ('suggestion', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('datasets', ['FieldSuggestion'])


    def backwards(self, orm):
        
        # Deleting model 'Project'
        db.delete_table('datasets_project')

        # Deleting model 'Page'
        db.delete_table('datasets_page')

        # Deleting model 'Record'
        db.delete_table('datasets_record')

        # Removing M2M table for field page on 'Record'
        db.delete_table('datasets_record_page')

        # Deleting model 'FieldType'
        db.delete_table('datasets_fieldtype')

        # Deleting model 'Field'
        db.delete_table('datasets_field')

        # Deleting model 'FieldSuggestion'
        db.delete_table('datasets_fieldsuggestion')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'datasets.field': {
            'Meta': {'object_name': 'Field'},
            'field_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datasets.FieldType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'matches_rule': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'ocr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datasets.Page']"}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datasets.Record']"})
        },
        'datasets.fieldsuggestion': {
            'Meta': {'object_name': 'FieldSuggestion'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datasets.Field']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'suggestion': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'datasets.fieldtype': {
            'Meta': {'object_name': 'FieldType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datasets.Project']", 'null': 'True', 'blank': 'True'}),
            'regex': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'datasets.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datasets.Project']"})
        },
        'datasets.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'datasets.record': {
            'Meta': {'object_name': 'Record'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['datasets.Page']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['datasets']
