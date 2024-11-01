"""
WSGI config for employeemanagement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employeemanagement.settings')

# application = get_wsgi_application()

import sys
import os
path = '/home/yourusername/Employee-Management-API-using-DRF'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'employeemanagement.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# Import Django's WSGI handler

