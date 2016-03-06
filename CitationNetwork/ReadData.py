'''
Created on Jun 8, 2012

@author: yyb
'''

'ReadData.py -- Read data from the original data files'


dailyDict = {};     # a dictionary for storing dates (year-month-day) and their corresponding paper-ids
monthlyDict = {};   # a dictionary for storing months (year-month) and their corresponding paper-ids
yearlyDict = {};    # a dictionary for storing years and their corresponding paper-ids

dailyList = [];      # a list for storing dates
monthlyList = [];
yearlyList = [];
paperDict = {};     # a dictionary for storing paper-ids and their corresponding submission dates
citeDict = {};      # a dictionary for storing citing paper-ids and cited paper-ids


#===============================================================================
# Read paper-ids and their submission dates
#===============================================================================
def readSubDate():
    dateFile = open('../Raw Data/cit-HepPh-dates.txt', 'r');      # open the file
    dateFile.readline();
    while True:
        s = dateFile.readline();    # read a line
        if len(s) == 0:     # zero length indicates EOF
            break;
        [pid, date] = s.split();     # split a line
        paperDict[int(pid)] = date;
        mon = date[0:7];
        yr = date[0:4];
        
        if date in dailyDict:
            dailyDict[date].append(int(pid));
        else:
            dailyDict[date] = [int(pid)];
            dailyList.append(date);
            
        if mon in monthlyDict:
            monthlyDict[mon].append(int(pid));
        else:
            monthlyDict[mon] = [int(pid)];
            monthlyList.append(mon);
            
        if yr in yearlyDict:
            yearlyDict[yr].append(int(pid));
        else:
            yearlyDict[yr] = [int(pid)];
            yearlyList.append(yr);
            
    dailyList.sort(); monthlyList.sort(); yearlyList.sort();
    dateFile.close();       # close the file


#===============================================================================
# Read links between two paper-ids
#===============================================================================
def readLinks():
    citeFile = open('../Raw Data/Cit-HepPh.txt', 'r');    # open the file
    citeFile.readline();citeFile.readline();citeFile.readline();citeFile.readline();
    while True:
        s = citeFile.readline();
        if len(s) == 0:
            break;
        [fromID, toID] = s.split();
        fromID = int(fromID);       # citing paper-id
        toID = int(toID);       # cited paper-id
        if fromID in paperDict and toID in paperDict: 
            if paperDict[fromID] > paperDict[toID]:     # filter out wrong information: one cites another which is submitted latter
                if fromID in citeDict:
                    citeDict[fromID].append(toID);
                else:
                    citeDict[fromID] = [toID];
    citeFile.close();       # close the file

