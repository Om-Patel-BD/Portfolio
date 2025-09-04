# api/index.py
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio.settings")
app = get_asgi_application()  # Vercel looks for "app"
