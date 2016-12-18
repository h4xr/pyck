from __future__ import unicode_literals

from django.db import models

class ServiceData(models.Model):
    '''
    ServiceData model for storing the service information about different
    delivery companies, organized according to their pincode.
    '''

    class Meta:
        app_label = 'services'

    pincode = models.PositiveIntegerField()
    company_name = models.CharField(max_length=50)
    money_limit = models.PositiveIntegerField(default=0)
    priority = models.IntegerField(default=0)

    def __unicode__(self):
        ''' Return a UNICODE valid name '''

        return "ServiceData Model"

    def save(self, *args, **kwargs):
        ''' Convert the required inputs to Integers before saving '''

        self.pincode = int(self.pincode)
        if self.money_limit:
            self.money_limit = int(self.money_limit)
        if self.priority:
            self.priority = int(self.priority)

        return super(ServiceData, self).save(*args, **kwargs)
