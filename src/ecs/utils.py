import time
import datetime
start_time_0 = '2015-01-01'
end_time_0 = '2015-01-07'

start_time_1 = '2015-01-08'
end_time_1 = '2015-01-14'

start_time_2 = '2015-01-15'
end_time_2 = '2015-01-21'
end_time = '2015-02-19'
def compare_time(l_time, start_t, end_t):
    s_time = time.mktime(time.strptime(start_t, '%Y-%m-%d'))  # get the seconds for specify date

    e_time = time.mktime(time.strptime(end_t, '%Y-%m-%d'))

    log_time = time.mktime(time.strptime(l_time, '%Y-%m-%d'))

    if (float(log_time) >= float(s_time)) and (float(log_time) <= float(e_time)):
        return True

    return False
#d1 = datetime.datetime.strptime('2012-03-05', '%Y-%m-%d')
#d2 = datetime.datetime.strptime('2012-03-02', '%Y-%m-%d')
#delta = d1 - d2
#print delta.days
def divide_time(start='2015-01-01',end='2015-02-19',divide_per_num=7):
    s_time = datetime.datetime.strptime(start, '%Y-%m-%d') # get the seconds for specify date
    e_time = datetime.datetime.strptime(end, '%Y-%m-%d')
    delta = e_time - s_time
    number_day = (delta.days)/divide_per_num
    return number_day