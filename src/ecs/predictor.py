from utils import compare_time,divide_time
from utils import (start_time_0,start_time_1,start_time_2,
                   end_time_0,end_time_1,end_time_2,end_time)

import datetime
'''
flave1:[0,1,1,0,1,,,,,]
flave2:[1,2,4,5,,,,,,]

'''
def process_flave_count(data_source):
    '''
    sum of count of flavor
    :param data_source:
    :return:
    '''
    flave_dict_count = flave_dict()
    flave_number_day = []
    for index in data_source:
        flave_time = '%s_%s'%(index[1],index[3])
        flave_number_day.append(flave_time)
        for flave in flave_dict_count.iterkeys():
            if index[1] == flave:
                flave_dict_count[flave]+=1
    return flave_dict_count,flave_number_day
def flave_dict():
    '''
    sum flave number dict
    :return:
    '''
    dict = {}
    for flave_number in range(1,16,1):
        flave_count_dict = 'flavor%s'%str(flave_number)
        dict[flave_count_dict] = 0
    return dict

def filter_flavor_day_count(x, flavorstring='flavor%s'):
    '''
    filter each [] of flavor
    :param x:
    :return:
    #for i in range(1,16,1):
        #for i,array in enumerate(x):
     #   temp = filter(lambda x:x.split('_')[0] == flavorstring%str(i),array)
        #print(temp)
    '''
    flavor_count_day_sum = []
    for i in range(1, 16, 1):
        flavor_count = []
        for flavor_day in x:
            if flavor_day.split('_')[0] == flavorstring % str(i):
                flavor_count.append(flavor_day)
        flavor_count_day_sum.append(flavor_count)
    return flavor_count_day_sum

def time_divide(flavor_count_day_sum,time_start,time_end):
    '''
    count from time_start to time_end
    :param flavor_count_day_sum:
    :param time_start:
    :param time_end:
    :return:
    '''
    flavor_day_dict = {}
    for i,flavor_sum in enumerate(flavor_count_day_sum):
        for element in flavor_sum:
            if compare_time(element.split('_')[1], time_start, time_end):
                flavor = 'flavor%s' % str(i)
                flavor_day_dict.setdefault(flavor, 0)
                flavor_day_dict[flavor] += 1

    return flavor_day_dict

def process_time(flavor_count_day_sum,divide_per_num=7):

    '''
    time_divide_window
    :param flavor_count_day_sum:
    :return:
     #flavor_day_dict = time_divide(flavor_count_day_sum, start_time_0, end_time_0)
   # return flavor_day_dict
    '''
    temp = []
    x = divide_time(start_time_0, end_time, divide_per_num)
    for i in range(divide_time(start_time_0,end_time,divide_per_num)):
        flavor_day_dict = time_divide(flavor_count_day_sum,(datetime.datetime.strptime(start_time_0,'%Y-%m-%d')+datetime.timedelta(days=i*divide_per_num)).strftime('%Y-%m-%d'),(datetime.datetime.strptime(start_time_0,'%Y-%m-%d')+datetime.timedelta(days=((i+1)*divide_per_num))).strftime('%Y-%m-%d'))
        temp.append(flavor_day_dict)
    return temp
###logistic
####
def model(input_features):
    '''
    model TODO:train a model
    '''
    pass






def predict_vm(ecs_lines, input_lines):
    # Do your work from here#
    result = []
    if ecs_lines is None:
        print 'ecs information is none'
        return result
    if input_lines is None:
        print 'input file information is none'
        return result
    data_source = []
    for item in ecs_lines:
        values = item.split("\t")
        uuid = values[0]
        flavorName = values[1]
        createTime = values[2]
        temp_create_time = createTime.split(" ")
        day_create_time = temp_create_time[0]
        day_hour_create_time = temp_create_time[1]
        temp_data_source = [uuid, flavorName, createTime, day_create_time, day_hour_create_time]
        data_source.append(temp_data_source)
    flavor_count, flave_number_day = process_flave_count(data_source)
    flavor_count_day_sum = filter_flavor_day_count(flave_number_day)
    flavor_day_dict_0 = process_time(flavor_count_day_sum, divide_per_num=7)
    flavor_day_dict_1 = process_time(flavor_count_day_sum, divide_per_num=5)
    flavor_day_dict_2 = process_time(flavor_count_day_sum, divide_per_num=3)
    flavor_day_dict_3 = process_time(flavor_count_day_sum, divide_per_num=1)
    for item in input_lines:
        print "index of input data"
    return result














