SECRET_KEY = "giant-people"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "giant-people",
    }
}

INSTALLED_APPS = [
    "cms",
    "treebeard",
    "menus",
    "sekizai",
    "easy_thumbnails",
    "filer",
    "mptt",
    "adminsortable2",
    "djangocms_admin_style",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "people",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["people/templates"],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

SITE_ID = 1

LANGUAGE_CODE = "en-gb"

LANGUAGES = [
    ("en-gb", "English"),
]

ROOT_URLCONF = "people.tests.urls"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]