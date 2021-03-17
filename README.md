# PiCalendar

<img src="https://i.imgur.com/L3OlWdY.png" width="376">
PiCalendar displays upcoming events in a simple webpage, with colors denoting whether the event is today (red), tomorrow (yellow), or after that but within 2 weeks (green).

This project was an intro to Flask and html/css

To set it up follow the instructions on the o365 python module: https://pypi.org/project/O365/#authentication to access the Microsoft Office API to read your calendar events. I had to set it up using authentication "on behalf of a user", you could get it to work "with your own identity" but my organization doesn't allow application permissions for the API, only delegated ones.

Once the API is set up, add your credentials to app/creds.py in the form of

```
CLIENT_ID = 'YOUR_CLIENT_ID'
SECRET_ID = 'YOUR_SECRET_ID'
```

and run authentication.py to create a token.

Use `export FLASK_APP=PiCalendar.py` to point flask to your app, then do `flask run` to run the calendar. Go to localhost:5000 to see your webpage!

The page auto-refreshes every hour to get rid of old events and load new events.

The webpage looks great on the official 7" raspberry pi touchscreen, other display sizes might need adjusting of the sizes of things.
