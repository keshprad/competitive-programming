# Problem: https://www.codewars.com/kata/52685f7382004e774f0001f7/


def make_readable(seconds):
    time = [str(seconds//3600), str(seconds//60%60), str(seconds%60)]
    for i in range(len(time)):
        if len(time[i]) < 2:
            time[i] = "0" + time[i]
    return "{0}:{1}:{2}".format(*time)
