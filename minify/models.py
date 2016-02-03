from django.db import models, IntegrityError
import uuid
import string, time, math, random
from django.core.exceptions import ObjectDoesNotExist



class Domain(models.Model):
    name =  models.CharField(null=True, blank=True, max_length=200)
    
    def __unicode__(self):
        return self.name


def uniqid(prefix='', length=4):
    uniqid = ''.join(random.SystemRandom().choice(string.ascii_lowercase.replace('o','').replace('i','').replace('l','') + string.digits.replace('0','').replace('1','')) for _ in range(length))
    return prefix + uniqid

class URLMinify(models.Model):
    short_url = models.CharField(null= True, blank=True, max_length=30, verbose_name='New URL', help_text='Eg. sale50/ OR LEAVE IT BLANK if you want a random 4 digit UUID like "3cmg/"')
    long_url = models.CharField(null=True, blank=True, max_length=1000, verbose_name='Old URL',help_text='Eg. fashion/sale/')
    long_url_domain = models.ForeignKey(Domain, null=True, blank=True, on_delete=models.PROTECT, related_name='long_url_domain',verbose_name='Old URL Domain Name', help_text='Eg. https://google.com')
    short_url_domain = models.ForeignKey(Domain, null=True, blank=True, on_delete=models.PROTECT,related_name='short_url_domain', verbose_name='New URL Domain Name', help_text='Eg. https://goo.gl')
    date_added = models.DateField(auto_now=True)



    def save(self, *args, **kwargs):
        if self.short_url == None or self.short_url == '':
            new_id = uniqid()
            # counter = 0
            # while counter<=100:
            #     try:
            #         existing_obj = URLMinify.objects.get(short_url=new_id,short_url_domain=self.short_url_domain)
            #         print 'ddafda'
            #         new_id = uniqid()
            #         print new_id
            #         counter += 1
            #     except ObjectDoesNotExist:
            #         break 
            self.short_url = new_id
        if not self.short_url_domain and self.long_url_domain:
            self.short_url_domain = self.long_url_domain
        elif not self.long_url_domain and self.short_url_domain:
            self.long_url_domain= self.short_url_domain
        super(URLMinify, self).save(*args, **kwargs)

    def __unicode__(self):
    	return self.short_url

    class Meta:
        verbose_name_plural="URL Minifiers"
        unique_together = ("short_url", "short_url_domain")
