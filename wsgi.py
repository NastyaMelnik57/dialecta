#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

## GETTING-STARTED: make sure the next line points to your settings.py:
os.environ['DJANGO_SETTINGS_MODULE'] = 'trimco.settings'
## GETTING-STARTED: make sure the next line points to your django project dir:
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'trimco'))
from distutils.sysconfig import get_python_lib
os.environ['PYTHON_EGG_CACHE'] = get_python_lib()

import django.core.wsgi
application = django.core.wsgi.get_wsgi_application()