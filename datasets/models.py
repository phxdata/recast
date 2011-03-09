from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name

class Page(models.Model):
    """describes a page with data"""
    project = models.ForeignKey('Project')
    number = models.IntegerField()
    image_file = models.FileField(upload_to='page_images', null=True, blank=True)
    
    def __unicode__(self):
        return "%s %s" % (self.project.name, self.number)

class Record(models.Model):
    """record is a collection of fields on a page"""
    page = models.ManyToManyField('Page')
    
    def __unicode__(self):
        return "A record in %s %s %s" % (self.page.project.name, self.page.number)

class FieldType(models.Model):
    """describes the name of a field and its datatype"""
    project = models.ForeignKey('Project', null=True, blank=True)
    name = models.CharField(max_length=255)
    regex = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class Field(models.Model):
    """an actual piece of data"""
    record = models.ForeignKey('Record')
    page = models.ForeignKey('Page')
    field_type = models.ForeignKey('FieldType')
    image_file = models.FileField(upload_to='field_images')
    ocr = models.TextField(null=True, blank=True)
    matches_rule = models.NullBooleanField(null=True, blank=True)
    
    def __unicode__(self):
        return "%s %s" (unicode(self.record), unicode(self.field_type))

class FieldSuggestion(models.Model):
    """a users suggestion for a fields value"""
    field = models.ForeignKey('Field')
    suggestion = models.TextField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "A suggestion by %s for %s" % (unicode(self.field), unicode(self.user))