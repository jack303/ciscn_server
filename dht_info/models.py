from django.db import models

# Create your models here.
class DhtResource(models.Model):

    info_hash = models.CharField(max_length=40,null=False)
    category = models.CharField(max_length=20,null=False)
    data_hash = models.CharField(max_length=32,null=False)
    name = models.CharField(max_length=255,null=False)
    extension = models.CharField(max_length=20,null=False)
    classified = models.CharField(max_length=255,null=False)
    source_ip = models.CharField(max_length=20)
    tagged = models.CharField(max_length=255,null=False)
    length = models.CharField(max_length=255,null=False)
    # change the type to date ???
    create_time = models.CharField(max_length=255,null=False)
    last_see = models.CharField(max_length=255,null=False)
    #
    requests = models.IntegerField(null=False,default=0)
    comment = models.CharField(max_length=255,blank=True)
    creator = models.CharField(max_length=20,blank=True)
    pass





# django rest api example
class Subject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    pass