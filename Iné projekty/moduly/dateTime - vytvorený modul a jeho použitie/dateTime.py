
#datetime = modul, kt. vie pracovať s časom a dátumom

import datetime

def time():
    x = datetime.datetime.now()
    print("Time:",x.strftime("%H")+":"+x.strftime("%M"))

def date():
    x = datetime.datetime.now()
    print("Year:",x.strftime("%Y"),"\nMonth:",x.strftime("%B"),"\nDay:",x.strftime("%A"))

