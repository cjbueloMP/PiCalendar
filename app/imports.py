from O365 import Account, MSGraphProtocol, FileSystemTokenBackend
import os
path = '/home/pi/calendarapp/app/'

from .creds import *
token_backend = FileSystemTokenBackend(token_path=path+'/token_dir', token_filename='my_token.txt')

credentials = (CLIENT_ID, SECRET_ID)
