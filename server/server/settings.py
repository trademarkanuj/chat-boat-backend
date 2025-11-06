# Allow Vercel hostnames
ALLOWED_HOSTS = ["*", ".vercel.app", "localhost", "127.0.0.1"]

# Tell Django which WSGI app to use (the one we just created)
WSGI_APPLICATION = "api.wsgi.app"

# Static files (served by WhiteNoise)
STATIC_URL = "/static/"
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[1]
STATIC_ROOT = BASE_DIR / "staticfiles"

INSTALLED_APPS = [
    # ...
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # add this line
    # ...
]

# Optional: let WhiteNoise find app static too
WHITENOISE_USE_FINDERS = True
WSGI_APPLICATION = "api.wsgi.app"