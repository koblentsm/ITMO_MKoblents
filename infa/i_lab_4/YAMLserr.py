from ScheduleDay import *
from Subject import *

class YAMLserr:

    def serr(self, schedule):
        day = f'{schedule.name}:\n'
        if bool(schedule.other):
            for key, value in schedule.other.items():
                day+= f'  {key}: {value}\n'

        if schedule.classes:
            day += f'  classes:\n'        
            for sub in schedule.classes:
                day += sub.to_yaml_block()
        # print(day)
        return day

    def save(self, file_name, schedule):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(schedule)