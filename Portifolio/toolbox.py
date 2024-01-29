import json
from datetime import datetime, timedelta, date
import holidays
from easygui import msgbox
import os
date_js = datetime.now().strftime('%d_%m_20%y')

def open_json(fila_json):
    if os.path.exists(f'Cotacao_moedas_{date_js}.json'):
        with open(f'Cotacao_moedas_{date_js}.json', 'a', encoding='utf8') as archive:
            json.dump(fila_json,archive,ensure_ascii=False, indent=4)
    else:
        with open(f'Cotacao_moedas_{date_js}.json', 'a', encoding='utf8') as archive:
            json.dump(fila_json,archive,ensure_ascii=False, indent=4)


def is_holidays(day_now):
    dd = int(day_now[:2])
    mm = int(day_now[3:5])
    yy = int(day_now[6:])
    day_now_f = date(yy,mm,dd)
    holiday_br = holidays.Brazil(years=yy)
    if day_now_f in holiday_br:
        return True
    else: return False
    

#day_now = datetime.now().strftime('%d/%m/20%y')
#is_holidays('01/01/2024')

def add_days(days_add: int, _date):
    dd = int(_date[:2])
    mm = int(_date[3:5])
    yy = int(_date[6:])
    _list = []
    for i in range(1,int(days_add) + 1):
        day_now_f = date(yy,mm,dd) + timedelta(days=i)
        day_now_f = day_now_f.strftime('%d/%m/20%y')
        _list.append(day_now_f)
    return _list

def logic_find(day_now):
    dd = int(day_now[:2])
    mm = int(day_now[3:5])
    yy = int(day_now[6:])
    day_now_f = date(yy,mm,dd)
    _d = day_now_f + timedelta(days=3)
    day_week = day_now_f.weekday() #4,5,6(friday,saturday,sunday) 
    
    if day_week == 4:
        if is_holidays(_d.strftime('%d/%m/20%y')) != True:
            add = add_days(2, day_now)
        else:
            add = add_days(3, day_now)

    else: return False

    return add

def logic_holiday(day_now):
    dd = int(day_now[:2])
    mm = int(day_now[3:5])
    yy = int(day_now[6:])
    day_now_f = date(yy,mm,dd)
    _day_now_f = day_now_f + timedelta(days=1)
    
    if is_holidays(_day_now_f.strftime('%d/%m/20%y')) != False:
        add = add_days(1, day_now)
        return add
    
    else: return False

