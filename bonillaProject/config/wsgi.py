"""
WSGI config for bonillaProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
sys.path.append('/var/www/bonillaproject.com/bonillaProject')
sys.path.append('/var/www/bonillaproject.com/bonillaProject/bonillaProject')

application = get_wsgi_application()
