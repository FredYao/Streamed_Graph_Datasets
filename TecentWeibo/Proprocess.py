'''
Created on Jun 24, 2012

@author: yyb
'''

'Process the data file and separate it into several smaller-size files'


from datetime import datetime;


#===============================================================================
# Separate the original data file into small-size daily instances
#===============================================================================
fobj = open('../Raw Data/rec_log_train.txt', 'r');      # open the original data file  
fPath = '../Raw Data/daily/';
print 'Converting into daily instances...';
day = 1; 
fname = fPath + str(day) + '.txt';       
f = open(fname, 'w');
s = fobj.readline();
tmstmp = int(s.split()[-1]);
date = datetime.utcfromtimestamp(tmstmp).isoformat(' ')[0:10];
f.write(s);
while True:
    s = fobj.readline();        # read the next line
    if len(s) == 0:
        break;
    newtmstmp = int(s.split()[-1]);
    newDate = datetime.utcfromtimestamp(newtmstmp).isoformat(' ')[0:10];
    if newDate == date:         # if the date is the same as previous line
        f.write(s);
    else:                       # else close the current file and open another new file to write
        f.close();
        print day;
        day += 1;
        fname = fPath + str(day) + '.txt';
        f = open(fname, 'w');
        f.write(s);
        tmstmp = int(s.split()[-1]);
        date = datetime.utcfromtimestamp(tmstmp).isoformat(' ')[0:10];
f.close();

fobj.close();       # close the original data file



#===============================================================================
# Separate the original data file into small-size hourly instances
#===============================================================================
fobj = open('../Raw Data/rec_log_train.txt', 'r');      # open the original data file  
fPath = '../Raw Data/hourly/';
print 'Converting into hourly instances...';
hour = 1; 
fname = fPath + str(hour) + '.txt';       
f = open(fname, 'w');
s = fobj.readline();
tmstmp = int(s.split()[-1]);
date = datetime.utcfromtimestamp(tmstmp).isoformat(' ')[0:13];
f.write(s);
while True:
    s = fobj.readline();        # read the next line
    if len(s) == 0:
        break;
    newtmstmp = int(s.split()[-1]);
    newDate = datetime.utcfromtimestamp(newtmstmp).isoformat(' ')[0:13];
    if newDate == date:         # if the date is the same as previous line
        f.write(s);
    else:                       # else close the current file and open another new file to write
        f.close();
        print hour;
        hour += 1;
        fname = fPath + str(hour) + '.txt';
        f = open(fname, 'w');
        f.write(s);
        tmstmp = int(s.split()[-1]);
        date = datetime.utcfromtimestamp(tmstmp).isoformat(' ')[0:13];
f.close();

fobj.close();       # close the original data file


