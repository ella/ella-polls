# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Poll'
        db.create_table('polls_poll', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text_announcement', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('text_results', self.gf('django.db.models.fields.TextField')()),
            ('active_from', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('active_till', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ella_polls.Question'], unique=True)),
        ))
        db.send_create_signal('ella_polls', ['Poll'])

        # Adding model 'Contest'
        db.create_table('polls_contest', (
            ('publishable_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Publishable'], unique=True, primary_key=True)),
            ('text_announcement', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('text_results', self.gf('django.db.models.fields.TextField')()),
            ('active_from', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('active_till', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('ella_polls', ['Contest'])

        # Adding model 'Quiz'
        db.create_table('polls_quiz', (
            ('publishable_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Publishable'], unique=True, primary_key=True)),
            ('text_announcement', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('text_results', self.gf('django.db.models.fields.TextField')()),
            ('active_from', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('active_till', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('has_correct_answers', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('ella_polls', ['Quiz'])

        # Adding model 'Question'
        db.create_table('polls_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('allow_multiple', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_no_choice', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ella_polls.Quiz'], null=True, blank=True)),
            ('contest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ella_polls.Contest'], null=True, blank=True)),
        ))
        db.send_create_signal('ella_polls', ['Question'])

        # Adding model 'Choice'
        db.create_table('polls_choice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ella_polls.Question'])),
            ('choice', self.gf('django.db.models.fields.TextField')()),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, blank=True)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('ella_polls', ['Choice'])

        # Adding model 'Survey'
        db.create_table('polls_survey', (
            ('question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ella_polls.Question'], unique=True, primary_key=True)),
            ('active_from', self.gf('django.db.models.fields.DateTimeField')()),
            ('active_till', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('ella_polls', ['Survey'])

        # Adding model 'SurveyVote'
        db.create_table('polls_surveyvote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ella_polls.Survey'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True)),
        ))
        db.send_create_signal('ella_polls', ['SurveyVote'])

        # Adding model 'Vote'
        db.create_table('polls_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ella_polls.Poll'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True)),
        ))
        db.send_create_signal('ella_polls', ['Vote'])

        # Adding model 'Contestant'
        db.create_table('polls_contestant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ella_polls.Contest'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phonenumber', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('choices', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('count_guess', self.gf('django.db.models.fields.IntegerField')()),
            ('winner', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('ella_polls', ['Contestant'])

        # Adding unique constraint on 'Contestant', fields ['contest', 'email']
        db.create_unique('polls_contestant', ['contest_id', 'email'])

        # Adding model 'Result'
        db.create_table('polls_result', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ella_polls.Quiz'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('points_from', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('points_to', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('ella_polls', ['Result'])


    def backwards(self, orm):

        # Removing unique constraint on 'Contestant', fields ['contest', 'email']
        db.delete_unique('polls_contestant', ['contest_id', 'email'])

        # Deleting model 'Poll'
        db.delete_table('polls_poll')

        # Deleting model 'Contest'
        db.delete_table('polls_contest')

        # Deleting model 'Quiz'
        db.delete_table('polls_quiz')

        # Deleting model 'Question'
        db.delete_table('polls_question')

        # Deleting model 'Choice'
        db.delete_table('polls_choice')

        # Deleting model 'Survey'
        db.delete_table('polls_survey')

        # Deleting model 'SurveyVote'
        db.delete_table('polls_surveyvote')

        # Deleting model 'Vote'
        db.delete_table('polls_vote')

        # Deleting model 'Contestant'
        db.delete_table('polls_contestant')

        # Deleting model 'Result'
        db.delete_table('polls_result')


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
        'core.author': {
            'Meta': {'object_name': 'Author'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'core.category': {
            'Meta': {'unique_together': "(('site', 'tree_path'),)", 'object_name': 'Category'},
            'app_data': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tree_parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Category']", 'null': 'True', 'blank': 'True'}),
            'tree_path': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.publishable': {
            'Meta': {'object_name': 'Publishable'},
            'app_data': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Author']", 'symmetrical': 'False'}),
            'category': ('ella.core.cache.fields.CachedForeignKey', [], {'to': "orm['core.Category']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('ella.core.cache.fields.CachedForeignKey', [], {'to': "orm['photos.Photo']", 'null': 'True', 'blank': 'True'}),
            'publish_from': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(3000, 1, 1, 0, 0, 0, 2)', 'db_index': 'True'}),
            'publish_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Source']", 'null': 'True', 'blank': 'True'}),
            'static': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.source': {
            'Meta': {'object_name': 'Source'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'ella_polls.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ella_polls.Question']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'ella_polls.contest': {
            'Meta': {'ordering': "('-active_from',)", 'object_name': 'Contest', '_ormbases': ['core.Publishable']},
            'active_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'active_till': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'publishable_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Publishable']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_announcement': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'text_results': ('django.db.models.fields.TextField', [], {})
        },
        'ella_polls.contestant': {
            'Meta': {'ordering': "('-datetime',)", 'unique_together': "(('contest', 'email'),)", 'object_name': 'Contestant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'choices': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ella_polls.Contest']"}),
            'count_guess': ('django.db.models.fields.IntegerField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phonenumber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'winner': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'ella_polls.poll': {
            'Meta': {'ordering': "('-active_from',)", 'object_name': 'Poll'},
            'active_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'active_till': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ella_polls.Question']", 'unique': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_announcement': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'text_results': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ella_polls.question': {
            'Meta': {'object_name': 'Question'},
            'allow_multiple': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_no_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ella_polls.Contest']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ella_polls.Quiz']", 'null': 'True', 'blank': 'True'})
        },
        'ella_polls.quiz': {
            'Meta': {'ordering': "('-active_from',)", 'object_name': 'Quiz', '_ormbases': ['core.Publishable']},
            'active_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'active_till': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'has_correct_answers': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publishable_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Publishable']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_announcement': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'text_results': ('django.db.models.fields.TextField', [], {})
        },
        'ella_polls.result': {
            'Meta': {'object_name': 'Result'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points_from': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'points_to': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ella_polls.Quiz']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'ella_polls.survey': {
            'Meta': {'ordering': "('-active_from',)", 'object_name': 'Survey', '_ormbases': ['ella_polls.Question']},
            'active_from': ('django.db.models.fields.DateTimeField', [], {}),
            'active_till': ('django.db.models.fields.DateTimeField', [], {}),
            'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['ella_polls.Question']", 'unique': 'True', 'primary_key': 'True'})
        },
        'ella_polls.surveyvote': {
            'Meta': {'ordering': "('-time',)", 'object_name': 'SurveyVote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ella_polls.Survey']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'ella_polls.vote': {
            'Meta': {'ordering': "('-time',)", 'object_name': 'Vote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ella_polls.Poll']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'app_data': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'photo_set'", 'symmetrical': 'False', 'to': "orm['core.Author']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'important_bottom': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'important_left': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'important_right': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'important_top': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Source']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['ella_polls']
