import json
from print_result_5 import print_result
from unique_3 import Unique
from field_1 import field
from gen_random_2 import gen_random
from cm_timer_6 import cm_timer_1

#path = '/C:/Users/MSI/PycharmProjects/Lab-3/data_light.json'
path = "../data/data_light.json"

#with open(path) as f:
#    data = json.load(f)

with open(path, encoding='utf-8') as f:
   data = json.load(f)

@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name')))


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    gen_salary = list(gen_random(len(arg), 100000, 200000))
    work_and_salary = list(zip(arg, gen_salary))
    return list(map(lambda x: x[0] + ', зарплата ' + str(x[1]) + ' руб', work_and_salary))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
