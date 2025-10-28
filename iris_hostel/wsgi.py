import os
import sys
from django.core.wsgi import get_wsgi_application

# Add your project directory
project_home = '/home/AashishPradhan/Iris-Family-Hostel'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iris_hostel.settings')

application = get_wsgi_application()
