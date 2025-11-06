import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parents[1]  # points to project root containing server/

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = ["*"]  # or restrict later: ["your-project.vercel.app"]

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
# WhiteNoise
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ... rest
]

# Serve compressed static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Databases
DATABASES = {
    "default": dj_database_url.parse(
        os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3"), conn_max_age=600
    )
}

# Important for proxies (Vercel)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
