'''
Created on Jun 9, 2012

@author: yyb
'''

'Write the information into GraphML format files'


import os;
import ReadData;
from copy import deepcopy;


ReadData.readUserInfo();
ReadData.readMovieInfo();
ReadData.readRatingInfo();


myRatDict = ReadData.ratDict;
myDateDict = ReadData.dateDict;
myMonDict = ReadData.monDict;
myYearDict = ReadData.yearDict;
totalDay = len(ReadData.dateList);
totalMon = len(ReadData.monList);
totalYr = len(ReadData.yearList);


#===============================================================================
# Write the information into GraphML files with a daily unit
#===============================================================================
def writeDailyGML(size):
    i = 1;
    fPath = '../GraphML/';
    fPath = fPath + 'span(' + str(size) + 'day(s))/';
    if os.path.exists(fPath) != 1:
        os.mkdir(fPath);
    myDateList = ReadData.dateList[:];
    myUsrDict = deepcopy(ReadData.usrDict);     # Get a deep copy of usrDict
    myMovDict = deepcopy(ReadData.movDict);     # Get a deep copy of movDict
    while len(myDateList) != 0:
        fName = fPath + str(i) + '.graphml';
        fobj = open(fName, 'w');
        wd = myDateList[0:size];
        del myDateList[0:size];
        fobj.write('<?xml version="1.0" encoding="UTF-8"?>\n');
        fobj.write('<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n\txsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n\t  http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n\n');
        fobj.write('   <key id="d1" for="node" attr.name="gender" attr.type="string"/>\n');
        fobj.write('   <key id="d2" for="node" attr.name="age" attr.type="int"/>\n');
        fobj.write('   <key id="d3" for="node" attr.name="occupation" attr.type="string"/>\n');
        fobj.write('   <key id="d4" for="node" attr.name="zipcode" attr.type="string"/>\n');
        fobj.write('   <key id="d5" for="node" attr.name="title" attr.type="string"/>\n');
        fobj.write('   <key id="d6" for="node" attr.name="genres" attr.type="string"/>\n');
        fobj.write('   <key id="d7" for="edge" attr.name="rating" attr.type="int"/>\n');
        fobj.write('   <key id="d8" for="edge" attr.name="time" attr.type="string"/>\n');
        fobj.write('   <key id="d_n" for="node" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n');
        fobj.write('   <key id="d_e" for="edge" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n\n');
        fobj.write('  <graph id="' + str(i) + '" edgedefault="directed">\n');
        for date in wd:
            li = myDateDict[date];
            for (uid, mid) in li:
                if myUsrDict[uid][1] == 0:
                    myUsrDict[uid][1] = 1;
                    fobj.write('\t<node id="' + uid + '">\n');
                    fobj.write('\t\t<data key=\"d1\">' + myUsrDict[uid][0][0] + '</data>\n');
                    fobj.write('\t\t<data key=\"d2\">' + myUsrDict[uid][0][1] + '</data>\n');
                    fobj.write('\t\t<data key=\"d3\">' + myUsrDict[uid][0][2] + '</data>\n');
                    fobj.write('\t\t<data key=\"d4\">' + myUsrDict[uid][0][3] + '</data>\n');
                    fobj.write('\t</node>\n');
                if myMovDict[mid][1] == 0:
                    myMovDict[mid][1] = 1;
                    fobj.write('\t<node id="' + mid + '">\n');
                    fobj.write('\t\t<data key=\"d5\">' + myMovDict[mid][0][0] + '</data>\n');
                    fobj.write('\t\t<data key=\"d6\">' + myMovDict[mid][0][1] + '</data>\n');
                    fobj.write('\t</node>\n');
                      
                fobj.write('\t<edge source="' + uid + '" target="' + mid + '">\n');
                fobj.write('\t\t<data key="d7">' + str(myRatDict[(uid, mid)][0]) + '</data>\n');
                fobj.write('\t\t<data key="d8">' + myRatDict[(uid, mid)][1] + '</data>\n');
                fobj.write('\t</edge>\n');
        fobj.write('  </graph>\n');
        fobj.write('</graphml>');
        fobj.close();
        i += 1;


#===============================================================================
# Write the information into GraphML files with a monthly unit
#===============================================================================
def writeMonthlyGML(size):
    i = 1;
    fPath = '../GraphML/';
    fPath = fPath + 'span(' + str(size) + 'month(s))/';
    if os.path.exists(fPath) != 1:
        os.mkdir(fPath);
    myMonList = ReadData.monList[:];
    myUsrDict = deepcopy(ReadData.usrDict);     # Get a deep copy of usrDict
    myMovDict = deepcopy(ReadData.movDict);     # Get a deep copy of movDict
    while len(myMonList) != 0:
        fName = fPath + str(i) + '.graphml';
        fobj = open(fName, 'w');
        wd = myMonList[0:size];
        del myMonList[0:size];
        fobj.write('<?xml version="1.0" encoding="UTF-8"?>\n');
        fobj.write('<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n\txsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n\t  http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n\n');
        fobj.write('   <key id="d1" for="node" attr.name="gender" attr.type="string"/>\n');
        fobj.write('   <key id="d2" for="node" attr.name="age" attr.type="int"/>\n');
        fobj.write('   <key id="d3" for="node" attr.name="occupation" attr.type="string"/>\n');
        fobj.write('   <key id="d4" for="node" attr.name="zipcode" attr.type="string"/>\n');
        fobj.write('   <key id="d5" for="node" attr.name="title" attr.type="string"/>\n');
        fobj.write('   <key id="d6" for="node" attr.name="genres" attr.type="string"/>\n');
        fobj.write('   <key id="d7" for="edge" attr.name="rating" attr.type="int"/>\n');
        fobj.write('   <key id="d8" for="edge" attr.name="time" attr.type="string"/>\n');
        fobj.write('   <key id="d_n" for="node" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n');
        fobj.write('   <key id="d_e" for="edge" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n\n');
        fobj.write('  <graph id="' + str(i) + '" edgedefault="directed">\n');
        for date in wd:
            li = myMonDict[date];
            for (uid, mid) in li:
                if myUsrDict[uid][1] == 0:
                    myUsrDict[uid][1] = 1;
                    fobj.write('\t<node id="' + uid + '">\n');
                    fobj.write('\t\t<data key=\"d1\">' + myUsrDict[uid][0][0] + '</data>\n');
                    fobj.write('\t\t<data key=\"d2\">' + myUsrDict[uid][0][1] + '</data>\n');
                    fobj.write('\t\t<data key=\"d3\">' + myUsrDict[uid][0][2] + '</data>\n');
                    fobj.write('\t\t<data key=\"d4\">' + myUsrDict[uid][0][3] + '</data>\n');
                    fobj.write('\t</node>\n');
                if myMovDict[mid][1] == 0:
                    myMovDict[mid][1] = 1;
                    fobj.write('\t<node id="' + mid + '">\n');
                    fobj.write('\t\t<data key=\"d5\">' + myMovDict[mid][0][0] + '</data>\n');
                    fobj.write('\t\t<data key=\"d6\">' + myMovDict[mid][0][1] + '</data>\n');
                    fobj.write('\t</node>\n');
                      
                fobj.write('\t<edge source="' + uid + '" target="' + mid + '">\n');
                fobj.write('\t\t<data key="d7">' + str(myRatDict[(uid, mid)][0]) + '</data>\n');
                fobj.write('\t\t<data key="d8">' + myRatDict[(uid, mid)][1] + '</data>\n');
                fobj.write('\t</edge>\n');
        fobj.write('  </graph>\n');
        fobj.write('</graphml>');
        fobj.close();
        i += 1;


#===============================================================================
# Write the information into GraphML files with a yearly unit
#===============================================================================
def writeYearlyGML(size):
    i = 1;
    fPath = '../GraphML/';
    fPath = fPath + 'span(' + str(size) + 'year(s))/';
    if os.path.exists(fPath) != 1:
        os.mkdir(fPath);
    myYearList = ReadData.yearList[:];
    myUsrDict = deepcopy(ReadData.usrDict);     # Get a deep copy of usrDict
    myMovDict = deepcopy(ReadData.movDict);     # Get a deep copy of movDict
    while len(myYearList) != 0:
        fName = fPath + str(i) + '.graphml';
        fobj = open(fName, 'w');
        wd = myYearList[0:size];
        del myYearList[0:size];
        fobj.write('<?xml version="1.0" encoding="UTF-8"?>\n');
        fobj.write('<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n\txsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n\t  http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n\n');
        fobj.write('   <key id="d1" for="node" attr.name="gender" attr.type="string"/>\n');
        fobj.write('   <key id="d2" for="node" attr.name="age" attr.type="int"/>\n');
        fobj.write('   <key id="d3" for="node" attr.name="occupation" attr.type="string"/>\n');
        fobj.write('   <key id="d4" for="node" attr.name="zipcode" attr.type="string"/>\n');
        fobj.write('   <key id="d5" for="node" attr.name="title" attr.type="string"/>\n');
        fobj.write('   <key id="d6" for="node" attr.name="genres" attr.type="string"/>\n');
        fobj.write('   <key id="d7" for="edge" attr.name="rating" attr.type="int"/>\n');
        fobj.write('   <key id="d8" for="edge" attr.name="time" attr.type="string"/>\n');
        fobj.write('   <key id="d_n" for="node" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n');
        fobj.write('   <key id="d_e" for="edge" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n\n');
        fobj.write('  <graph id="' + str(i) + '" edgedefault="directed">\n');
        for date in wd:
            li = myYearDict[date];
            for (uid, mid) in li:
                if myUsrDict[uid][1] == 0:
                    myUsrDict[uid][1] = 1;
                    fobj.write('\t<node id="' + uid + '">\n');
                    fobj.write('\t\t<data key=\"d1\">' + myUsrDict[uid][0][0] + '</data>\n');
                    fobj.write('\t\t<data key=\"d2\">' + myUsrDict[uid][0][1] + '</data>\n');
                    fobj.write('\t\t<data key=\"d3\">' + myUsrDict[uid][0][2] + '</data>\n');
                    fobj.write('\t\t<data key=\"d4\">' + myUsrDict[uid][0][3] + '</data>\n');
                    fobj.write('\t</node>\n');
                if myMovDict[mid][1] == 0:
                    myMovDict[mid][1] = 1;
                    fobj.write('\t<node id="' + mid + '">\n');
                    fobj.write('\t\t<data key=\"d5\">' + myMovDict[mid][0][0] + '</data>\n');
                    fobj.write('\t\t<data key=\"d6\">' + myMovDict[mid][0][1] + '</data>\n');
                    fobj.write('\t</node>\n');
                      
                fobj.write('\t<edge source="' + uid + '" target="' + mid + '">\n');
                fobj.write('\t\t<data key="d7">' + str(myRatDict[(uid, mid)][0]) + '</data>\n');
                fobj.write('\t\t<data key="d8">' + myRatDict[(uid, mid)][1] + '</data>\n');
                fobj.write('\t</edge>\n');
        fobj.write('  </graph>\n');
        fobj.write('</graphml>');
        fobj.close();
        i += 1;


#===============================================================================
# The main function
#===============================================================================
def main():
    while True:
        print 'Choose a basic unit to stream the MovieLens dataset (enter 1, 2, 3 or 4):\n1.daily\n2.monthly\n3.yearly\n4.Quit\n',
        choice = int(raw_input());
        if choice == 1:
            print 'There are ' + str(totalDay) + ' daily instances in this dataset';  
            print 'Enter an integer as a time window size (1 ~', totalDay, '):';
            windowSize = int(raw_input());
            writeDailyGML(windowSize);
        elif choice == 2:
            print 'There are ' + str(totalMon) + ' monthly instances in this dataset';  
            print 'Enter an integer as a time window size (1 ~', totalMon, '):';
            windowSize = int(raw_input());
            writeMonthlyGML(windowSize);
        elif choice == 3:
            print 'There are ' + str(totalYr) + ' yearly instances in this dataset';  
            print 'Enter an integer as a time window size (1 ~', totalYr, '):';
            windowSize = int(raw_input());
            writeYearlyGML(windowSize);
        elif choice == 4:
            break;
        else:
            print 'Bad choice';
            continue;
            
        opt = raw_input('\nTry another time window size (yes or no)?\n');
        if opt.strip()[0].lower() == 'n':
            print 'Terminating......';
            break;
        elif opt.strip()[0].lower() == 'y':
            continue;
        else:
            print 'Invalid input, terminating......';
            break;


#===============================================================================
# Execution
#===============================================================================
if __name__ == '__main__':
    main();
    
    
