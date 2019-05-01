import datetime
import calendar

now = datetime.datetime.now()
print("The Time is: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


cal = calendar.month(2019, 1)
print ("Here is the calendar:")
print (cal)