# for x in reversed(range (1, 10)):
#    print(x);
#    print("completed");
import time
set_time = int(input("Enter time in seconds:"));
for x in reversed(range (0,set_time+1)):
     second = x % 60;
     minute = int (x/60) % 60;
     hour = int (x/3600);
     print(f"{hour:02}:{minute:02}:{second:02}");
     time.sleep(1);
print("Time Up!!!");