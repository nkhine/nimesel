# -*- coding: utf-8 -*-
import os
from google.appengine.dist import use_library
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
use_library('django', '1.2')

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

# Load request handlers
import handlers
from tools.common import is_testenv

# Map url's to handlers
urls = [
    (r'/', handlers.Main),
    (r'/login', handlers.LogIn),
    (r'/_ah/login_required', handlers.LogIn),
    (r'/logout', handlers.LogOut),
    (r'/account', handlers.Account),
    (r'/account/setup', handlers.AccountSetup),    
    (r'.*', handlers.Error404)
]

application = webapp.WSGIApplication(urls, debug=is_testenv())


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
