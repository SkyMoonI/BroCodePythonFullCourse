# epoch = a date and time from which a computer measures system time

import time

# print(time.ctime(0))  # convert a time expressed in seconds since epoch to a readable string
#                     epoch = when your computer thinks time began (reference point)

# print(time.time())  # return current seconds since epoch

# print(time.ctime(time.time()))  # current date and time

# time_object = time.localtime()
# time_object = time.gmtime()  # UTC time
#
# print(time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)
