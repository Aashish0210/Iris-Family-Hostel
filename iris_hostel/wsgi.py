import os
import sys
from django.core.wsgi import get_wsgi_application
path = '/home/AashishPradhan/'
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iris_hostel.settings')
application = get_wsgi_application()

path = '/home/AashishPradhan/'
if path not in sys.path:
    sys.path.append(path)
