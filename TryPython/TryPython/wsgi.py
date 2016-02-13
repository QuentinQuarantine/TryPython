import os

import newrelic
from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TryPython.settings")
application = get_wsgi_application()

if settings.PRODUCTION:
    newrelic.agent.initialize(
        os.path.join(settings.PROJECT_DIR, 'newrelic.ini'), 'production')
    application = newrelic.agent.wsgi_application()(application)
