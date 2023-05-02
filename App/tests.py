
import datetime as dt

date = '2022/09/21 15:14:00'
datee = "2012/12/12"+ " " +"10:24:00"

date1 = dt.datetime.strptime(date, '%Y/%m/%d %H:%M:%S')
date2 = dt.datetime.strptime(datee, '%Y/%m/%d %H:%M:%S')

print(date1 < date2)

