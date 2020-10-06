from numpy import random


class Time:
    
    def __init__(self,hour,minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}'


def random_time(start,end):
    '''
    returns a random string that represents time between start and end.
    [start,end)
    
    start and end are positive integers.
    
    The parameters and results are in miliatry time.
    
    This function currently only works if
    start > end
    '''
    diff = end - start
    
    hour = start + random.randint(0, diff)
    minute = random.randint(0,61) #61 because the upper limited is exclusive.
    
    result = Time(hour,minute)
    
    return str(result)


START_TIME = 1
END_TIME = 9


result = random_time(START_TIME, END_TIME)
print(result)
