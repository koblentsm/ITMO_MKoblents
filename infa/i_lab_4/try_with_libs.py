# hcl_to_yaml_with_libs.py
import hcl
import yaml
import time
import pickle

def convert_hcl_to_yaml(hcl_filename: str, yaml_filename: str):
    # t_st = time.perf_counter()
    with open(hcl_filename, "r", encoding="utf-8") as f:
        data = hcl.load(f)
    sh = pickle.dumps(data)
    ld = pickle.loads(sh)
    with open(yaml_filename, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, indent=2)
    # t_fn = time.perf_counter()
    # print((t_fn-t_st))
t_mon_st = time.perf_counter()
for _ in range(100):
    convert_hcl_to_yaml("monday.hcl", "monday_libs.yaml")
t_mon_fn = time.perf_counter()
print(t_mon_fn-t_mon_st)


t_sat_st = time.perf_counter()
for _ in range(100):
    convert_hcl_to_yaml("saturday.hcl", "saturday_libs.yaml")
t_sat_fn = time.perf_counter()
print(t_sat_fn-t_sat_st)