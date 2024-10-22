import json
from datetime import datetime, timedelta, date
import holidays
import os
date_js = datetime.now().strftime('%d_%m_20%y')


class ToolBox:
    def create_archive_json(self,fila_json:dict)->str:
        self.fila_json = fila_json
        if os.path.exists(f'quotation_prices_{date_js}.json'):
            with open(f'quotation_prices_{date_js}.json', 'a', encoding='utf8') as archive:
                json.dump(self.fila_json,archive,ensure_ascii=False, indent=4)
        else:
            with open(f'quotation_prices_{date_js}.json', 'a', encoding='utf8') as archive:
                json.dump(self.fila_json,archive,ensure_ascii=False, indent=4)
        return "Archive create with sucess"


    def is_holidays(self,day_now:str)->bool:
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

    def add_days(self,days_add: int, _date:str)->list:
        dd = int(_date[:2])
        mm = int(_date[3:5])
        yy = int(_date[6:])
        _list = []
        for i in range(1,int(days_add) + 1):
            day_now_f = date(yy,mm,dd) + timedelta(days=i)
            day_now_f = day_now_f.strftime('%d/%m/20%y')
            _list.append(day_now_f)
        return _list

    def logic_find(self,day_now:str)->list:
        dd = int(day_now[:2])
        mm = int(day_now[3:5])
        yy = int(day_now[6:])
        day_now_f = date(yy,mm,dd)
        _d = day_now_f + timedelta(days=3)
        day_week = day_now_f.weekday() #4,5,6(friday,saturday,sunday) 
        
        if day_week == 4:
            if self.is_holidays(_d.strftime('%d/%m/20%y')) != True:
                add = self.add_days(2, day_now)
            else:
                add = self.add_days(3, day_now)

        else: return False

        return add

    def logic_holiday(self,day_now:str)->list:
        dd = int(day_now[:2])
        mm = int(day_now[3:5])
        yy = int(day_now[6:])
        day_now_f = date(yy,mm,dd)
        _day_now_f = day_now_f + timedelta(days=1)
        
        if self.is_holidays(_day_now_f.strftime('%d/%m/20%y')) != False:
            add = self.add_days(1, day_now)
            return add
        
        else: return False

