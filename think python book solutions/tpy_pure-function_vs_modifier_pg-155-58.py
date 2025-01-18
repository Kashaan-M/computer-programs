import copy

class Time:
    """Represents the time of the day.

    attributes: hour,minute,second.
    """


def add_time(t1, t2):
    """ pure function.Adds time of two provided time objects"""
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    
    if sum.minute >=60:
        sum.minute -= 60
        sum.hour += 1

    return sum


def increment(time, seconds):
    """ A modifier

    this function modifies the time object by adding the seconds to it
    """

    rem = seconds % 60
    if rem != 0:
        # need this check to avoid infiinte recursion
        # in case we get perfect division with zero remainder
        seconds_left = seconds - rem
        time.second += rem
    else:
        # in case of perfect division we subtract one from seconds_left
        # and add one to rem. This is to keep perfect division from occuring on next iterations
        seconds_left = seconds - rem - 1
        time.second += rem + 1

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    # recursive call to increment() with seconds_left in place of seconds
    if seconds_left > 0:
        increment(time,seconds_left)


def pure_increment(time, seconds):
    """A pure function

    This is a version of increment() which doesn't modify the provided time object
    but creates and returns a new_time object
    """

    # place an atribute of exists on new_time object in order to distinct it from time object

    if not hasattr(time,'exists'):
        print('yes')
        new_time = copy.copy(time)
        new_time.exists = True

    rem = seconds % 60

    if rem != 0:
        # need this check to avoid infiinte recursion
        # in case, we get perfect division with zero remainder
        seconds_left = seconds - rem
        new_time.second += rem
    else:
        # in case of perfect division we subtract one from seconds_left
        #and add one to rem.This is to keep perfect division from occuring on next iterations
        seconds_left = seconds - rem - 1
        new_time.second += rem + 1

    if new_time.second >= 60:
        new_time.second -= 60
        new_time.minute += 1

    if new_time.minute >= 60:
        new_time.minute -= 60
        new_time.hour += 1

    # recursive call to increment() with seconds_left in place of seconds
    if seconds_left > 0:
        increment(new_time,seconds_left)
    # if rem becomes zero then new_time object
    else:
        return new_time

        
    


