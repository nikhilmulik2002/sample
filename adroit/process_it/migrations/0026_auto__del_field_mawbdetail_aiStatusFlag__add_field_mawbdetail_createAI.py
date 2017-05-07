# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MawbDetail.aiStatusFlag'
        db.delete_column('process_it_mawbdetail', 'aiStatusFlag')

        # Adding field 'MawbDetail.createAIStatus'
        db.add_column('process_it_mawbdetail', 'createAIStatus',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'MawbDetail.createAIDesc'
        db.add_column('process_it_mawbdetail', 'createAIDesc',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'MawbDetail.updateRemarkStatus'
        db.add_column('process_it_mawbdetail', 'updateRemarkStatus',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'MawbDetail.getConsoleStatus'
        db.add_column('process_it_mawbdetail', 'getConsoleStatus',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'MawbDetail.getConsoleDesc'
        db.add_column('process_it_mawbdetail', 'getConsoleDesc',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'MawbDetail.aiStatusFlag'
        db.add_column('process_it_mawbdetail', 'aiStatusFlag',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Deleting field 'MawbDetail.createAIStatus'
        db.delete_column('process_it_mawbdetail', 'createAIStatus')

        # Deleting field 'MawbDetail.createAIDesc'
        db.delete_column('process_it_mawbdetail', 'createAIDesc')

        # Deleting field 'MawbDetail.updateRemarkStatus'
        db.delete_column('process_it_mawbdetail', 'updateRemarkStatus')

        # Deleting field 'MawbDetail.getConsoleStatus'
        db.delete_column('process_it_mawbdetail', 'getConsoleStatus')

        # Deleting field 'MawbDetail.getConsoleDesc'
        db.delete_column('process_it_mawbdetail', 'getConsoleDesc')


    models = {
        'process_it.hawbdetail': {
            'Meta': {'object_name': 'HawbDetail'},
            'consignee': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hawbNum': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mawbNum': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wpComments': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wpCommentsAt': ('django.db.models.fields.DateTimeField', [], {}),
            'wpCommentsBy': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wpStatus': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'process_it.mawbdetail': {
            'Meta': {'object_name': 'MawbDetail'},
            'aiDesc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'ataDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'ataTime': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'chgWeight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '0'}),
            'cobDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'consoleNumber': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '0'}),
            'createAIDesc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'createAIStatus': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'etaDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'etaTime': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'etdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'etdTime': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'flightCode': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'flightNum': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'getConsoleDesc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'getConsoleStatus': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itInfo': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'lastUpdatedByUser': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'lastUpdatedDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'lastUpdatedTime': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'mawbNum': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'oneFStatus': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'oneFStatusComment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'paLocked': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'paLockedByUser': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'pamFlag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'papFlag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'pendingHblNum': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '0'}),
            'pmcOrLoose': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True'}),
            'ppComments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'ppCommentsAt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'ppCommentsBy': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'preAlertReceivedDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'preAlertReceivedTime': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'recoveryNum': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'recoveryOrBO': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'remarksInClass': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'shipmentStatus': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'slac': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '0'}),
            'spCommentOfCeva': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'spCommentOfCevaAt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'spCommentOfCevaBy': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'spCommentOfHcl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'spCommentOfHclAt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'spCommentOfHclBy': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'spProStatus': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'speakWith': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'station': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'totalHblNum': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '0'}),
            'trackSource': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'updateRemarkStatus': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'updateTodayFlag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'process_it.usercountdetail': {
            'Meta': {'object_name': 'UserCountDetail'},
            'avgTime': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'totalCounts': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'userName': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['process_it']