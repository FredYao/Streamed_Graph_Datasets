'''
Created on Jun 25, 2012

@author: yyb
'''

import os;
import ReadData;
from copy import deepcopy;
from datetime import datetime;


ReadData.readItemInfo();
ReadData.readUserInfo();


myUsrInfo = ReadData.usrInfo;
myItmInfo = ReadData.itmInfo;


#===============================================================================
# Defining my own comparison function for sorting filenames in filelist
#===============================================================================
def compare(s1, s2):
    a = int(s1.split('.')[0]);
    b = int(s2.split('.')[0]);
    return cmp(a, b);


#===============================================================================
# A function for writing given data into GraphML format 
#===============================================================================
def gml(index, fname, addUsrNode, addItmNode, addEdge):
    fobj = open(fname, 'w');
    fobj.write('<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n\txsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n\t  http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n\n');
    fobj.write('   <key id="d1" for="node" attr.name="birth,gender,tweet,tags" attr.type="string"/>\n');
    fobj.write('   <key id="d2" for="node" attr.name="category,keywords" attr.type="string"/>\n'); 
    fobj.write('   <key id="d3" for="node" attr.name="timestamp,result" attr.type="string"/>\n');   
    fobj.write('   <key id="d_n" for="node" attr.name="modification" attr.type="string">\n' + '     <default>add</default>\n' + '   </key>\n');
    fobj.write('   <key id="d_e" for="edge" attr.name="modification" attr.type="string">\n' + '     <default>add</default>\n' + '   </key>\n\n');
    fobj.write('  <graph id="' + str(index) + '" edgedefault="directed">\n');   
    
    # write user nodes
    for node in addUsrNode:
        tup = myUsrInfo[node];
        fobj.write('\t<node id="' + str(node) + '">\n');
        fobj.write('\t\t<data key="d1">' + tup[0] + ',' + tup[1] + ',' + tup[2] + ',' + tup[3] + '</data>\n');
        fobj.write('\t</node>\n');
    # write item nodes
    for node in addItmNode:
        tup = myItmInfo[node];
        fobj.write('\t<node id="' + str(node) + '">\n');
        fobj.write('\t\t<data key="d2">' + tup[0] + ',' + tup[1] + '</data>\n');
        fobj.write('\t</node>\n');
    
    # write edges
    for (usrNode, itmNode, result, tmstmp) in addEdge:
        fobj.write('\t<edge source="' + str(usrNode) + '" target="' + str(itmNode) + '">\n');
        fobj.write('\t\t<data key="d3">' + str(result) + ',' + datetime.utcfromtimestamp(tmstmp).isoformat(' ') + '</data>\n');
        fobj.write('\t</edge>\n');
        
    fobj.write('  </graph>\n');
    fobj.write('</graphml>');
    fobj.close();


#===============================================================================
# Write information into GraphML format files with a hourly unit
#===============================================================================
def writeHourlyGML(size):
    filelist = os.listdir('../Raw Data/hourly/');
    filelist.sort(compare);     # sort the filenames in an ascending order
        
    fPath = '../GraphML/span(' + str(size) + 'hour(s))/';
    if os.path.exists(fPath) != 1:      # create a path to store all the generated GraphML files
        os.mkdir(fPath);
    
    myItmDict = deepcopy(ReadData.itmDict);
    myUsrDict = deepcopy(ReadData.usrDict);
    addEdgeList = [];       # a list for storing added edges   
    addUsrNode = [];        # a list for storing added user nodes
    addItmNode = [];        # a list for storing added item nodes
    i = 1;
    
    while len(filelist) != 0:
        print 'Writing file ', i;
        wd = filelist[0:size];
        del filelist[0:size];
        del addEdgeList[:];
        del addUsrNode[:];
        del addItmNode[:];
        for filename in wd:
            fobj = open('../Raw Data/hourly/' + filename, 'r');
            while True:
                s = fobj.readline();
                if len(s) == 0:
                    break;
                li = s.split();
                uID = int(li[0]); iID = int(li[1]); rslt = int(li[2]); tmstmp = int(li[3]);
                addEdgeList.append((uID, iID, rslt, tmstmp));
                if myItmDict[iID] == 0:
                    myItmDict[iID] = 1;
                    addItmNode.append(iID);
                if myUsrDict[uID] == 0:
                    myUsrDict[uID] = 1;
                    addUsrNode.append(uID);
            fobj.close();
        
        # write GraphML files
        gml(i, fPath + str(i) + '.graphml', addUsrNode, addItmNode, addEdgeList);
        i += 1;


#===============================================================================
# Write information into GraphML format files with a daily unit
#===============================================================================
def writeDailyGML(size):
    filelist = os.listdir('../Raw Data/daily/');
    filelist.sort(compare);     # sort the filenames in an ascending order
        
    fPath = '../GraphML/span(' + str(size) + 'day(s))/';
    if os.path.exists(fPath) != 1:      # create a path to store all the generated GraphML files
        os.mkdir(fPath);
    
    myItmDict = deepcopy(ReadData.itmDict);
    myUsrDict = deepcopy(ReadData.usrDict);
    addEdgeList = [];       # a list for storing added edges   
    addUsrNode = [];        # a list for storing added user nodes
    addItmNode = [];        # a list for storing added item nodes
    i = 1;
    
    while len(filelist) != 0:
        print 'Writing file ', i;
        wd = filelist[0:size];
        del filelist[0:size];
        del addEdgeList[:];
        del addUsrNode[:];
        del addItmNode[:];
        for filename in wd:
            fobj = open('../Raw Data/daily/' + filename, 'r');
            while True:
                s = fobj.readline();
                if len(s) == 0:
                    break;
                li = s.split();
                uID = int(li[0]); iID = int(li[1]); rslt = int(li[2]); tmstmp = int(li[3]);
                addEdgeList.append((uID, iID, rslt, tmstmp));
                if myItmDict[iID] == 0:
                    myItmDict[iID] = 1;
                    addItmNode.append(iID);
                if myUsrDict[uID] == 0:
                    myUsrDict[uID] = 1;
                    addUsrNode.append(uID);
            fobj.close();
        
        # write GraphML files
        gml(i, fPath + str(i) + '.graphml', addUsrNode, addItmNode, addEdgeList);
        i += 1;       
    
    
#===============================================================================
# The main function
#===============================================================================
def main():
    flist1 = os.listdir('../Raw Data/hourly/');
    flist2 = os.listdir('../Raw Data/daily/');
    len1 = len(flist1);
    len2 = len(flist2);
    
    while True:
        print 'Choose a basic unit to stream the Tencent dataset (enter 1, 2 or 3):\n1.hourly\n2.daily\n3.quit\n',
        choice = int(raw_input());
        if choice == 1:
            print 'There are ' + str(len1) + ' hourly instances in this dataset.';  
            print 'Enter an integer as a time window size (1 ~', len1, '):';
            windowSize = int(raw_input());
            writeHourlyGML(windowSize);
        elif choice == 2:
            print 'There are ' + str(len2) + ' daily instances in this dataset';  
            print 'Enter an integer as a time window size (1 ~', len2, '):';
            windowSize = int(raw_input());
            writeDailyGML(windowSize);
        elif choice == 3:
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
    
    
    

