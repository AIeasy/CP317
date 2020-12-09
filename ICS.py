'''
use information go generate ics file
'''
from icalendar import Calendar,Event,LocalTimezone
import pytz

from datetime import datetime
import tempfile,os

def g_ics(sort_info,path):
    c= Calendar()
    
    lt = LocalTimezone()
    
    for x in range(len(sort_info)):
        e=Event()
        title = sort_info[x].title
        start = sort_info[x].start
        end = sort_info[x].end
        year=start[0:4]
        mon = start[5:7]
        day = start[8:10]
        hour = start[11:13]
        min = start[14:16]
        e.add('summary',title)
        e.add('dtstart',datetime(int(year),int(mon),int(day),int(hour),int(min),0,tzinfo=lt))
        year=end[0:4]
        mon = end[5:7]
        day = end[8:10]
        hour = end[11:13]
        min = end[14:16]
        e.add('dtend',datetime(int(year),int(mon),int(day),int(hour),int(min),0,tzinfo=lt))
        c.add_component(e)


        f = open(os.path.join(path, 'example.ics'), 'wb')
        f.write(c.to_ical())
        f.close()