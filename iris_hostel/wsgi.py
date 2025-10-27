import os
import sys
from django.core.wsgi import get_wsgi_application

# Add your project directory to the Python path
project_home = '/home/AashishPradhan/Iris-Family-Hostel'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iris_hostel.settings')

# Activate your virtualenv if you have one
# Uncomment and update if needed
# activate_this = '/home/AashishPradhan/.virtualenvs/yourenv/bin/activate_this.py'
# exec(open(activate_this).read(), {'__file__': activate_this})

# Get WSGI application
application = get_wsgi_application()
