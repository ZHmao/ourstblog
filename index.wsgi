import os
import sys

root = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(root, 'site-packages'))


import sae

from ourst import wsgi

print sys.path

application = sae.create_wsgi_app(wsgi.application)
