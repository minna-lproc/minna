import os

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'storage')
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
# UPLOAD_EXTENSIONS
GOOGLEMAPS_KEY = "AIzaSyDNc_aHa9fNKbTS1amE0gSO2ouOj9trU8U"

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = "587"
MAIL_USE_TLS = "True"
MAIL_USE_SSL = "False"
MAIL_USERNAME = "joe.clio001@gmail.com"
MAIL_PASSWORD = "Wysiwyg15!"
MAIL_RECEIVER = "alemaniacamilleite111@gmail.com"



# nmvwntgtnucnlcgx
# sampleemail123
# cfflzfrsehwdixfs
# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
