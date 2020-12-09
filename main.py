from web import r_web
from chrome import chrome
from generate import generate
from ICS import g_ics
from info import str_to_calobj
from user_login import user_login
from tkinter import messagebox
def login():
    mydriver = user_login()
    mydriver = r_web(mydriver)
    if mydriver.current_url != "https://mylearningspace.wlu.ca/d2l/le/calendar/6605":
        messagebox.showerror('Error',"Please login to mls")
        olist=[]
    else:
        olist = chrome(mydriver)
    return olist

def gen(list,path):
    list = str_to_calobj(list)
    g_ics(list,path)
    return


