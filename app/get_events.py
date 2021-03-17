from .imports import *
import datetime as dt

from O365 import Connection

def parse_event_string(event):
    event_string = str(event)
    subject_start = 9
    subject_index = event_string.find('(on:')-1

    start_index = event_string.find('from:') + 6
    end_index = event_string.find('to:') - 1 
    start_meeting_time = event_string[start_index:end_index]

    start_index = event_string.find('on:') + 4
    end_index = event_string.find('from:') - 1
    date = event_string[start_index:end_index]

    start_obj = dt.datetime.strptime(start_meeting_time, '%H:%M:%S').time()
    date_obj = dt.datetime.strptime(date, '%Y-%m-%d')
    fulltime = dt.datetime.combine(date_obj,start_obj)
    hourminute = fulltime.strftime("%-I:%M %p")
    hourminute = '{:>8}'.format(hourminute)
    subject = event_string[subject_start:subject_index]
    color = set_color(fulltime)
    return {'subject':subject, 'start_time':fulltime, 'hourminute':hourminute,'color':color}

def set_color(fulltime):
    if fulltime.date() == dt.date.today():
        return "red"
    if fulltime.date() == dt.date.today() + dt.timedelta(days=1):
        return "yellow"
    else:
        return "green"

def get_events():

    account = Account(credentials, token_backend=token_backend)
    Connection.refresh_token
    
    
    schedule = account.schedule()
    calendar = schedule.get_default_calendar()
    q = calendar.new_query('start').greater_equal(dt.datetime.now())
    q.chain('and').on_attribute('end').less_equal(dt.datetime.now()+dt.timedelta(days=14))
    #events = calendar.get_events(include_recurring=False) 
    events = calendar.get_events(query=q, include_recurring=True) 
    
    eventlist = []
    numevents = 11
    i=0
    for event in events:
        i+=1
        if i==numevents:
            break
        event = parse_event_string(event)
        eventlist.append(event)
    
    
    eventlist = sorted(eventlist, key=lambda start: start['start_time'])
    return eventlist


