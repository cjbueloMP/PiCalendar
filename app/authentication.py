from imports import *
from O365 import Connection
import readline
protocol = MSGraphProtocol() 
#protocol = MSGraphProtocol(defualt_resource='<sharedcalendar@domain.com>') 
account = Account(credentials,token_backend=token_backend)
#account = Account(credentials,protocol=protocol)

if account.authenticate(scopes=['Calendars.Read','Calendars.Read.Shared','basic']):
   print('Authenticated!')

Connection.refresh_token
