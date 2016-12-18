"""
Script to fillup our django models from the csv file
"""
import sys, os
django_project_path = '/home/saurabh/development/pyck/pyck'
sys.path.append(django_project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from services.models import ServiceData
from csv import reader
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application

data = reader(open('output.csv'))
header = data.next()

for row in data:
    service_data = ServiceData()
    service_data.pincode = row[0]
    service_data.company_name = row[1]
    service_data.money_limit = row[2]
    service_data.priority = row[3]
    service_data.save()
