from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class CorpusCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'corpus_category'


class CorpusConversation(models.Model):
    statement = models.CharField(max_length=200)
    response = models.CharField(max_length=300)
    category = models.ForeignKey(CorpusCategory, models.DO_NOTHING)

    class Meta:
        db_table = 'corpus_conversation'



class DjangoChatterbotStatement(models.Model):
    created_at = models.DateTimeField()
    conversation = models.CharField(max_length=32)
    in_response_to = models.CharField(max_length=255, blank=True, null=True)
    persona = models.CharField(max_length=50)
    search_text = models.CharField(max_length=255)
    search_in_response_to = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    class Meta:
        db_table = 'django_chatterbot_statement'


class DjangoChatterbotStatementTags(models.Model):
    statement = models.ForeignKey(DjangoChatterbotStatement, models.DO_NOTHING)
    tag = models.ForeignKey('DjangoChatterbotTag', models.DO_NOTHING)

    class Meta:
        db_table = 'django_chatterbot_statement_tags'
        unique_together = (('statement', 'tag'),)


class DjangoChatterbotTag(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'django_chatterbot_tag'

