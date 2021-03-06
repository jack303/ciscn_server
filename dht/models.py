from django.db import models

# Create your models here.
# the models of dht include:
# resource: the origin resource collected by web crawler
# file_list: the files contained by the resource
# request: the amount of times that the corresponding resource is requested
# type: the type of the resource that has the same info_hash
# resource_shield: the record of shield resource
# node_shield: the record of shield node
# resource_text:
# keyword:
# resource_media
TYPE_CHOICES = (('1','normal'),('2','porn'))
LEVEL_CHOICES = (('1','serious'),('2','not bad'))

# class Resource(models.Model):
#     info_hash = models.CharField(max_length=40, null=False)
#     category = models.CharField(max_length=20, null=False)
#     data_hash = models.CharField(max_length=32, null=False)
#     name = models.CharField(max_length=255, null=False)
#     extension = models.CharField(max_length=20, null=False)
#     classified = models.CharField(max_length=255, null=False)
#     source_ip = models.CharField(max_length=20, null=True)
#     tagged = models.CharField(max_length=255, null=False)
#     length = models.CharField(max_length=255, null=False)
#     # change the type to date ???
#     create_time = models.CharField(max_length=255, null=False)
#     last_seen = models.CharField(max_length=255, null=False)
#     #
#     requests = models.IntegerField(null=False, default=0)
#     comment = models.CharField(max_length=255, null=True)
#     creator = models.CharField(max_length=20, null=True)
#     pass
class SearchHash(models.Model):
    info_hash = models.CharField(unique=True, max_length=40)
    category = models.CharField(max_length=20)
    data_hash = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    extension = models.CharField(max_length=20)
    classified = models.IntegerField()
    source_ip = models.CharField(max_length=20, blank=True, null=True)
    tagged = models.IntegerField()
    length = models.BigIntegerField()
    create_time = models.DateTimeField()
    last_seen = models.DateTimeField()
    requests = models.IntegerField()
    comment = models.CharField(max_length=255, blank=True, null=True)
    creator = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    level = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'search_hash'

# class File_list(models.Model):
#     info_hash = models.CharField(max_length=40, primary_key=True)
#     file_list = models.CharField(max_length=255)
class SearchFilelist(models.Model):
    info_hash = models.CharField(primary_key=True, max_length=40)
    file_list = models.TextField()

    class Meta:
        managed = False
        db_table = 'search_filelist'

class Node(models.Model):
    ip = models.CharField(max_length=20,primary_key=True)#节点唯一标识
    heading = models.CharField(max_length=20)#节点在页面上的显示
    img_src = models.CharField(max_length=255)
    resource_num = models.IntegerField(auto_created=0)
    anti_num = models.IntegerField(auto_created=0)
    porn_num = models.IntegerField(auto_created=0)
    vio_num = models.IntegerField(auto_created=0)
    capture_time = models.DateTimeField(auto_now_add=True)
    belonging = models.CharField(max_length=255)
    feature = models.CharField(max_length=255)


class Request(models.Model):
    #maybe we need to record the request time to make DHT visible
    info_hash = models.CharField(max_length=40)
    request_ip = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

# class Type(models.Model):
#     info_hash = models.CharField(max_length=40, primary_key=True)
#     type = models.CharField(choices=TYPE_CHOICES,default='1',max_length=20)
#     level = models.CharField(choices=LEVEL_CHOICES,default='1',max_length=20)

class Resource_shield(models.Model):
    info_hash = models.CharField(max_length=40, primary_key=True)
    time = models.DateTimeField(auto_now_add=True)

class Node_shield(models.Model):
    node_ip = models.CharField(max_length=20, null=True)
    time = models.DateTimeField(auto_now_add=True)

class Resource_text(models.Model):
    info_hash = models.CharField(max_length=40)
    key_word = models.ForeignKey('Keyword',related_name='labeled_resource',on_delete=models.CASCADE)


class Keyword(models.Model):
    key_word_id = models.IntegerField(primary_key=True,auto_created=True)
    word = models.CharField(max_length=20)
    word_type = models.CharField(choices=TYPE_CHOICES,max_length=20,default='1')

class Resource_media(models.Model):
    info_hash = models.CharField(max_length=40)
    # api do not provide file upload
    frame_address = models.CharField(max_length=255)
    frame_type = models.CharField(choices=TYPE_CHOICES, max_length=20, default='1')

