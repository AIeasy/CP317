'''
info class
sort the information passed by generate class
return a calendar object that contain a title, a start date and a end date.
'''
MONTH = {'JAN':'1','FEB':'2','MAR':'3','APR':'4','MAY':'5','JUN':'6','JUL':'7','AUG':'8','SEP':'9','OCT':'10','NOV':'11','DEC':'12'}
START_DAY = "2020-09-01 00:00:00"
class calobj:
    def __init__(self,title,begin,end):
        
        self.start = begin
        self.end = end
        self.title= title

        return

def str_to_calobj(lis):
    calobj_list = []
    for i in range(0,len(lis),2):
        start,end = str_to_date(lis[i+1])
        #start = correct(start)
        #end = correct_end(end)
        calobj_list.append(calobj(lis[i],start,end))
    return calobj_list
def str_to_date(s):
    index = s.index(',')
    day = s[4:index]
    if(int(day)<10):
        day = "0" + day
    mon = MONTH[s[0:3].upper()]
    if (int(mon)<10):
        mon = "0" + mon
    ti = index+6
    year = s[index+2:ti]
    end_time = s[index+7:]
    #print(end_time)
    start= START_DAY
    end=''
    if (len(end_time)>9):
        ind = end_time.index('-')
        time1 = end_time[0:ind-4]
        aop = end_time[ind-3:ind-1]
        if (aop.upper() == "PM"):
            h = time1.index(":")
            hour = time1[0:h]
            time1 = str(int(hour)+12) + time1[h:]
        else:
            h = time1.index(":")
            hour = time1[0:h]
            hour = "0"+hour
            time1 = hour + time1[h:]
           
        start = year + '-' + mon + '-' + day + ' ' + time1 + ':00'
        
        time2 = end_time[ind+2:-3]
        aop2 = end_time[-2:]
        if (aop2.upper() == "PM"):
            h = time2.index(":")
            hour = time2[0:h]
            time2 = str(int(hour)+12) + time2[h:]
        else:
            h = time2.index(":")
            hour = time2[0:h]
            hour = "0"+hour
            time2 = hour + time2[h:]
        end = year + '-' + mon + '-' + day + ' ' + time2 + ':00'
        
    else:
        aop = end_time[-2:]
        h = end_time.index(":")
        hour = end_time[0:h]
        if (aop.upper() == "PM"):
            end_time = str(int(hour)+12) + end_time[h:-3]
        else:
            if (int(hour)<10):
                hour = "0"+hour
            end_time = hour + end_time[h:-3]
            
        end = year + '-' + mon + '-' + day + ' ' + end_time + ':00'
        
    return start,end