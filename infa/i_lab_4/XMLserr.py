from ScheduleDay import *
from Subject import *

class XMLserr:

    def serr(self, schedule):
        day = '<?xml version="1.0" encoding="UTF-8"?>'
        day += f'<Schedule>\n  <Day name="{schedule.name}">\n'
        if bool(schedule.other):
            for key, value in schedule.other.items():
                day+= f'    <{key}>{value}</{key}>\n'

        if schedule.classes:
            day += f'    <Classes>\n'  
            for sub in schedule.classes:
                day += sub.to_xml_block()
            day +=f'    </Classes>\n'
        # print(day)
        day += '</Schedule>'
        return day
    
    def save(self, file_name, schedule):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(schedule)