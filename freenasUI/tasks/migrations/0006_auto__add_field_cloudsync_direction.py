# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CloudSync.direction'
        db.add_column(u'tasks_cloudsync', 'direction',
                      self.gf('django.db.models.fields.CharField')(default='PUSH', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CloudSync.direction'
        db.delete_column(u'tasks_cloudsync', 'direction')


    models = {
        u'storage.disk': {
            'Meta': {'ordering': "['disk_subsystem', 'disk_number']", 'object_name': 'Disk'},
            'disk_acousticlevel': ('django.db.models.fields.CharField', [], {'default': "'Disabled'", 'max_length': '120'}),
            'disk_advpowermgmt': ('django.db.models.fields.CharField', [], {'default': "'Disabled'", 'max_length': '120'}),
            'disk_description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'disk_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'disk_enclosure_slot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'disk_hddstandby': ('django.db.models.fields.CharField', [], {'default': "'Always On'", 'max_length': '120'}),
            'disk_identifier': ('django.db.models.fields.CharField', [], {'max_length': '42', 'primary_key': 'True'}),
            'disk_multipath_member': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'disk_multipath_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'disk_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'disk_number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'disk_serial': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'disk_size': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'disk_smartoptions': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'disk_subsystem': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'disk_togglesmart': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'disk_transfermode': ('django.db.models.fields.CharField', [], {'default': "'Auto'", 'max_length': '120'})
        },
        u'system.cloudcredentials': {
            'Meta': {'object_name': 'CloudCredentials'},
            'attributes': ('freenasUI.freeadmin.models.fields.DictField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tasks.cloudsync': {
            'Meta': {'ordering': "['description']", 'object_name': 'CloudSync'},
            'attributes': ('freenasUI.freeadmin.models.fields.DictField', [], {}),
            'credential': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.CloudCredentials']"}),
            'daymonth': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'dayweek': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'direction': ('django.db.models.fields.CharField', [], {'default': "'PUSH'", 'max_length': '10'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hour': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.CharField', [], {'default': "'00'", 'max_length': '100'}),
            'month': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'path': ('freenasUI.freeadmin.models.fields.PathField', [], {'max_length': '255'})
        },
        u'tasks.cronjob': {
            'Meta': {'ordering': "['cron_description', 'cron_user']", 'object_name': 'CronJob'},
            'cron_command': ('django.db.models.fields.TextField', [], {}),
            'cron_daymonth': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'cron_dayweek': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'cron_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cron_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cron_hour': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'cron_minute': ('django.db.models.fields.CharField', [], {'default': "'00'", 'max_length': '100'}),
            'cron_month': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'cron_stderr': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cron_stdout': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cron_user': ('freenasUI.freeadmin.models.fields.UserField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tasks.initshutdown': {
            'Meta': {'object_name': 'InitShutdown'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ini_command': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'ini_script': ('freenasUI.freeadmin.models.fields.PathField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ini_type': ('django.db.models.fields.CharField', [], {'default': "'command'", 'max_length': '15'}),
            'ini_when': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'tasks.rsync': {
            'Meta': {'ordering': "['rsync_path', 'rsync_desc']", 'object_name': 'Rsync'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rsync_archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rsync_compress': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rsync_daymonth': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'rsync_dayweek': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'rsync_delayupdates': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rsync_delete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rsync_desc': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'rsync_direction': ('django.db.models.fields.CharField', [], {'default': "'push'", 'max_length': '10'}),
            'rsync_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rsync_extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rsync_hour': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'rsync_minute': ('django.db.models.fields.CharField', [], {'default': "'00'", 'max_length': '100'}),
            'rsync_mode': ('django.db.models.fields.CharField', [], {'default': "'module'", 'max_length': '20'}),
            'rsync_month': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'rsync_path': ('freenasUI.freeadmin.models.fields.PathField', [], {'max_length': '255'}),
            'rsync_preserveattr': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rsync_preserveperm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rsync_quiet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rsync_recursive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rsync_remotehost': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'rsync_remotemodule': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'rsync_remotepath': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rsync_remoteport': ('django.db.models.fields.SmallIntegerField', [], {'default': '22'}),
            'rsync_times': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rsync_user': ('freenasUI.freeadmin.models.fields.UserField', [], {'max_length': '60'})
        },
        u'tasks.smarttest': {
            'Meta': {'ordering': "['smarttest_type']", 'object_name': 'SMARTTest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'smarttest_daymonth': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'smarttest_dayweek': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'smarttest_desc': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'smarttest_disks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['storage.Disk']", 'symmetrical': 'False'}),
            'smarttest_hour': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'smarttest_month': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '100'}),
            'smarttest_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['tasks']