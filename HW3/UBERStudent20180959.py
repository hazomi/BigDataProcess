import sys
import datetime

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
args = sys.argv[1]
args2 = sys.argv[2]
sys.stdout = open(args2, 'w')

f = open(args, "rt")
for line in f:
    result = line.split(",")
    new_result = [l.strip() for l in result]
    week = new_result[1].split("/")
    wk = [int(i) for i in week]
    d = days[datetime.date(wk[2], wk[0], wk[1]).weekday()]
    print(new_result[0], d, sep = ",", end=" ")
    print(new_result[2], new_result[3], sep = ",")
f.close()
sys.stdout.close()
