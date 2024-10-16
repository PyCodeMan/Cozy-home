import sys
import os


HOST = '127.0.0.1'
PORT = 5432
USER = 'unit2147'
DATABASE = 'cozy_home'
PASSWORD = os.getenv('DATABASE_PASSWORD')

if not PASSWORD:
    print('Password are not defined')
    sys.exit(0)