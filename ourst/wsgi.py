import os
import sys

root = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(root, '..', 'site-packages'))
"""
WSGI config for ourst project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ourst.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
