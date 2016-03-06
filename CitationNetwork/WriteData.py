'''
Created on Jun 8, 2012

@author: yyb
'''

'Write the information into GraphML format files'


import os;
import ReadData;
 
 
ReadData.readSubDate();
ReadData.readLinks();
 
 
myDayDict = ReadData.dailyDict;
myMonDict = ReadData.monthlyDict;
myYrDict = ReadData.yearlyDict;
myPaperDict = ReadData.paperDict;
myCiteDict = ReadData.citeDict;
totalDay = len(ReadData.dailyList);
totalMon = len(ReadData.monthlyList);
totalYr = len(ReadData.yearlyList);
 
 
#===============================================================================
# Write information into GraphML format files with a daily unit
#===============================================================================
def writeDailyGML(size):
    i = 1;
    fPath = '../GraphML/';
    fPath = fPath + 'span(' + str(size) + 'day(s))/';  
    if os.path.exists(fPath) != 1:
        os.mkdir(fPath);
    myDateList = ReadData.dailyList[:];
    while len(myDateList) != 0:
        wd = myDateList[0:size];
        del myDateList[0:size];
        fname = fPath + str(i) + '.graphml';
        fobj = open(fname, 'w');
        fobj.write('<?xml version="1.0" encoding="UTF-8"?>\n');
        fobj.write('<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n\txsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n\t  http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n\n');
        fobj.write('   <key id="d0" for="node" attr.name="SubmissionDate" attr.type="string"/>\n');
        fobj.write('   <key id="d1" for="edge" attr.name="timestamp" attr.type="string"/>\n');
        fobj.write('   <key id="d_n" for="node" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n');
        fobj.write('   <key id="d_e" for="edge" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n\n');
        fobj.write('  <graph id="' + str(i) + '" edgedefault="directed">\n');
        for date in wd:
            li = myDayDict[date];
            # write nodes
            for paper in li:
                fobj.write('\t<node id="' + str(paper) + '">\n');
                fobj.write('\t\t<data key=\"d0\">' + date + '</data>\n');
                fobj.write('\t</node>\n');
                if paper in myCiteDict:
                    cited = myCiteDict[paper];
                    # write edges
                    for n in cited:
                        fobj.write('\t<edge source="' + str(paper) + '" target="' + str(n) + '">\n');
                        fobj.write('\t\t<data key="d1">' + date + '</data>\n');
                        fobj.write('\t</edge>\n');
        fobj.write('  </graph>\n');
        fobj.write('</graphml>');
        fobj.close();
        i += 1;
        

#===============================================================================
# Write information into GraphML format files with a monthly unit
#===============================================================================
def writeMonthlyGML(size):
    i = 1;
    fPath = '../GraphML/';
    fPath = fPath + 'span(' + str(size) + 'month(s))/';  
    if os.path.exists(fPath) != 1:
        os.mkdir(fPath);
    myMonList = ReadData.monthlyList[:];
    while len(myMonList) != 0:
        wd = myMonList[0:size];
        del myMonList[0:size];
        fname = fPath + str(i) + '.graphml';
        fobj = open(fname, 'w');
        fobj.write('<?xml version="1.0" encoding="UTF-8"?>\n');
        fobj.write('<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n\txsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n\t  http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n\n');
        fobj.write('   <key id="d0" for="node" attr.name="SubmissionDate" attr.type="string"/>\n');
        fobj.write('   <key id="d1" for="edge" attr.name="timestamp" attr.type="string"/>\n');
        fobj.write('   <key id="d_n" for="node" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n');
        fobj.write('   <key id="d_e" for="edge" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n\n');
        fobj.write('  <graph id="' + str(i) + '" edgedefault="directed">\n');
        for mon in wd:
            li = myMonDict[mon];
            # write nodes
            for paper in li:
                fobj.write('\t<node id="' + str(paper) + '">\n');
                fobj.write('\t\t<data key=\"d0\">' + myPaperDict[paper] + '</data>\n');
                fobj.write('\t</node>\n');
                if paper in myCiteDict:
                    cited = myCiteDict[paper];
                    # write edges
                    for n in cited:
                        fobj.write('\t<edge source="' + str(paper) + '" target="' + str(n) + '">\n');
                        fobj.write('\t\t<data key="d1">' + myPaperDict[paper] + '</data>\n');
                        fobj.write('\t</edge>\n');
        fobj.write('  </graph>\n');
        fobj.write('</graphml>');
        fobj.close();
        i += 1;
        

#===============================================================================
# Write information into GraphML format files with a yearly unit
#===============================================================================
def writeYearlyGML(size):
    i = 1;
    fPath = '../GraphML/';
    fPath = fPath + 'span(' + str(size) + 'year(s))/';  
    if os.path.exists(fPath) != 1:
        os.mkdir(fPath);
    myYrList = ReadData.yearlyList[:];
    while len(myYrList) != 0:
        wd = myYrList[0:size];
        del myYrList[0:size];
        fname = fPath + str(i) + '.graphml';
        fobj = open(fname, 'w');
        fobj.write('<?xml version="1.0" encoding="UTF-8"?>\n');
        fobj.write('<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n\txsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n\t  http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n\n');
        fobj.write('   <key id="d0" for="node" attr.name="SubmissionDate" attr.type="string"/>\n');
        fobj.write('   <key id="d1" for="edge" attr.name="timestamp" attr.type="string"/>\n');
        fobj.write('   <key id="d_n" for="node" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n');
        fobj.write('   <key id="d_e" for="edge" attr.name="modification" attr.type="string">\n');
        fobj.write('     <default>add</default>\n');
        fobj.write('   </key>\n\n');
        fobj.write('  <graph id="' + str(i) + '" edgedefault="directed">\n');
        for yr in wd:
            li = myYrDict[yr];
            # write nodes
            for paper in li:
                fobj.write('\t<node id="' + str(paper) + '">\n');
                fobj.write('\t\t<data key=\"d0\">' + myPaperDict[paper] + '</data>\n');
                fobj.write('\t</node>\n');
                if paper in myCiteDict:
                    cited = myCiteDict[paper];
                    # write edges
                    for n in cited:
                        fobj.write('\t<edge source="' + str(paper) + '" target="' + str(n) + '">\n');
                        fobj.write('\t\t<data key="d1">' + myPaperDict[paper] + '</data>\n');
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
        print 'Choose a basic unit to stream the HepPh dataset (enter 1, 2, 3 or 4):\n1.daily\n2.monthly\n3.yearly\n4.Quit\n',
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

