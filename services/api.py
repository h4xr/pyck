#services/api.py
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from services.models import ServiceData


class ServiceDataResource(ModelResource):
    '''
    Resources for the REST API built upon tastypie
    '''

    class Meta:
        queryset = ServiceData.objects.all()
        resource_name = 'servicedata'
        allowed_methods = ['get']
        filtering = {
            'pincode': ['exact'],
            'money_limit': ALL,
        }
        ordering = ['priority']
