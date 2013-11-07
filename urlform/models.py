from django.db import models

class ShortLinks(models.Model):
    visitor_ip=models.CharField(max_length=15)
    date=models.DateTimeField(auto_now_add=True)
    long_url=models.URLField(max_length=2053) #2048 or 2053?  Is "http://" included within the 2048 char limit?
    short_url=models.CharField(max_length=40, null=True)

    class Meta:
        pass

    def __unicode__(self):
        return self.visitor_ip


