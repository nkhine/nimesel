# -*- coding: utf-8 -*-
#
# Update the settings as needed
#

from tools.common import is_testenv

TEMPLATE_DIR = "templates/"

# MailChimp settings to subscribe users after signup
MAILCHIMP_API_KEY = ""

# Find it on mailchimp.com via "settings" -> "list settings and unique id"
MAILCHIMP_LIST_ID = ""

# Use this switch to turn the MailChimp API calls on and off. Set to True only
# for testing and production. Set to False during development.
MAILCHIMP_ENABLED = False

if is_testenv():
    CDN_PREFIX = ""
else:
    CDN_PREFIX = ""
    #CDN_PREFIX = "http://s3-ap-southeast-1.amazonaws.com/bucket"
    #CDN_PREFIX = "http://d2m9d0no7kkld2.cloudfront.net"
