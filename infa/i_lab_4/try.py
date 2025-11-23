print(501832%132) #100, там нет занятий -> 108 тоже -> 116 Понедельник,суббота, есть занятия
from HCLParser import HCLParser 
from YAMLserr import *
from XMLserr import *
import pickle
import time
parser = HCLParser()
serr = YAMLserr()
time_mon_yaml_st = time.perf_counter()
for _ in range(100):
    schedule_mon = parser.parse_file("monday.hcl")
    # print(type(schedule_mon))
    sh = pickle.dumps(schedule_mon)
    ld = pickle.loads(sh)
    # print(type(ld))
    serr.save("monday.yaml", serr.serr(ld))

time_mon_yaml_fn = time.perf_counter()
print(time_mon_yaml_fn-time_mon_yaml_st)


time_sat_yaml_st = time.perf_counter()
for _ in range(100):
    schedule_sat = parser.parse_file("saturday.hcl")
    sh = pickle.dumps(schedule_sat)
    ld = pickle.loads(sh)
    serr.save("saturday.yaml", serr.serr(ld))
time_sat_yaml_fn = time.perf_counter()
print(time_sat_yaml_fn-time_sat_yaml_st)


xml_serr = XMLserr()
time_mon_xml_st = time.perf_counter()
for _ in range(100):
    schedule_mon = parser.parse_file("monday.hcl")
    sh = pickle.dumps(schedule_mon)
    ld = pickle.loads(sh)
    xml_serr.save('monday.xml', xml_serr.serr(ld))
time_mon_xml_fn = time.perf_counter()
print(time_mon_xml_fn-time_mon_xml_st)



time_sat_xml_st = time.perf_counter()
for _ in range(100):
    schedule_sat = parser.parse_file("saturday.hcl")
    sh = pickle.dumps(schedule_sat)
    ld = pickle.loads(sh)
    xml_serr.save('saturday.xml', xml_serr.serr(ld))
time_sat_xml_fn = time.perf_counter()
print(time_sat_xml_fn-time_sat_xml_st)





