class Time(object):
 def __init__(self, hour, minute, second):
     self.hour = hour
     self.minute = minute
     self.second = second

 def __str__(self):
     return str(self.hour) + ":" + str(self.minute)+ ":" + str(self.second)
 def __add__(self, other):
     return Time( self.hour + other.hour,self.minute + other.hour, self.second + other.second)



time1 = Time(5, 32, 0)
time2 = Time(23, 11, 11)
time3 = Time (9,8,7)

print time1
print time2

print time1 +time2 +time3
