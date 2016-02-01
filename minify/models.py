from django.db import models

class Domain(models.Model):
	name =  models.CharField(null=True, blank=True, max_length=200)

class URLMinify(models.Model):
    short_url = models.CharField(null= True, blank=True, max_length=200, verbose_name='New URL', help_text='Eg. /sale/')
    long_url = models.CharField(null=True, blank=True, max_length=1000, verbose_name='Old URL',help_text='Eg. /fashion/sale/')
    long_url_domain = models.ForeignKey(Domain, null=True, blank=True, on_delete=models.PROTECT, related_name='long_url_domain',verbose_name='Old URL Domain Name')
    short_url_domain = models.ForeignKey(Domain, null=True, blank=True, on_delete=models.PROTECT,related_name='short_url_domain', verbose_name='New URL Domain Name')
    date_added = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
    	if not self.short_url_domain and self.long_url_domain:
    		self.short_url_domain = self.long_url_domain
    	elif not self.long_url_domain and self.short_url_domain:
    		self.long_url_domain= self.short_url_domain
    	super(URLMinify, self).save(*args, **kwargs)

    def __unicode__(self):
    	return short_url

    class Meta:
        verbose_name_plural="URL Minifiers"