'''
Created on Jun 15, 2012

@author: yyb
'''

'Read information from the original data files and write into GraphML format files'


import os;


#===============================================================================
# Function: writing the given information (num, date, addNode, addEdge, delNode, delEdge) 
#           into a GraphML format file
#===============================================================================
def writeGML(num, date, addNode, addEdge, delNode, delEdge):
    fobj = open('../GraphML/' + str(num) + '.graphml', 'w');
    fobj.write('<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n\txsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n\t  http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n\n');
    fobj.write('   <key id="d1" for="node" attr.name="timestamp" attr.type="string">\n' + '     <default>' + date + '</default>\n' + '   </key>\n');
    fobj.write('   <key id="d2" for="edge" attr.name="timestamp" attr.type="string">\n' + '     <default>' + date + '</default>\n' + '   </key>\n');
    fobj.write('   <key id="d_n" for="node" attr.name="modification" attr.type="string">\n' + '     <default>add</default>\n' + '   </key>\n');
    fobj.write('   <key id="d_e" for="edge" attr.name="modification" attr.type="string">\n' + '     <default>add</default>\n' + '   </key>\n\n');
    fobj.write('  <graph id="' + str(num) + '" edgedefault="directed">\n');
    
    # write nodes
    for n in addNode:
        fobj.write('\t<node id="' + str(n) + '"/>\n');
    for n in delNode:
        fobj.write('\t<node id="' + str(n) + '">\n');
        fobj.write('\t\t<data key="d_n">delete</data>\n');
        fobj.write('\t</node>\n');
    
    # write edges
    for (n, m) in addEdge:
        fobj.write('\t<edge source="' + str(n) + '" target="' + str(m) + '"/>\n');
    for (n, m) in delEdge:
        fobj.write('\t<edge source="' + str(n) + '" target="' + str(m) + '">\n');
        fobj.write('\t\t<data key="d_e">delete</data>\n');
        fobj.write('\t</edge>\n');
    
    fobj.write('  </graph>\n');
    fobj.write('</graphml>');
    fobj.close();
    

#===============================================================================
# Read and write data
#===============================================================================
fPath = '../Raw Data/';
fileList = os.listdir(fPath);
fileList.sort();        # a list containing all the data files to be read from

edgeList1 = []; nodeList1 = [];     # lists for storing deleted edges and nodes
nodeList2 = []; edgeList2 = [];     # lists for storing added edges and nodes
i = 0;      # file index

# read the 1st original file
fname = fileList[i];
date = date = fname[2:6] + '-' + fname[6:8] + '-' + fname[8:10];        # get the date
fobj = open(fPath + fname, 'r');
fobj.readline();fobj.readline();fobj.readline();fobj.readline();
while True:
    print i;
    s = fobj.readline();
    if len(s) == 0:
        break;
    [fromNd, toNd] = s.split('\t');
    fromNd = int(fromNd); toNd = int(toNd);
    edgeList2.append((fromNd, toNd));
    nodeList2.append(fromNd); nodeList2.append(toNd);

# write the 1st GraphML file
edgeSet1 = set(edgeList1); nodeSet1 = set(nodeList1);   # converted from lists into sets 
edgeSet2 = set(edgeList2); nodeSet2 = set(nodeList2);
s1 = nodeSet2 - nodeSet1; s2 = edgeSet2 - edgeSet1;     # get the added nodes and edges, actually all nodes and edges are added
s3 = nodeSet1 - nodeSet2; s4 = edgeSet1 - edgeSet2;     # get the deleted nodes and edges, actually no nodes or edges deleted
writeGML(i, date, s1, s2, s3, s4);      # nodeSet1 is empty, edgeSet1 is empty too


edgeList1 = edgeList2[:]; nodeList1 = nodeList2[:];
edgeSet1 = set(edgeList1); nodeSet1 = set(nodeList1);


# read the next files and write them into GraphML formats
while i < len(fileList) - 1:
    i += 1;
    print i;
    del edgeList2[:]; del nodeList2[:];     # clear edgeList2 and nodeList2
    
    # read the current file (whose index is i in fileList)
    fname = fileList[i];
    date = date = fname[2:6] + '-' + fname[6:8] + '-' + fname[8:10];        # get the date
    fobj = open(fPath + fname, 'r');
    fobj.readline();fobj.readline();fobj.readline();fobj.readline();
    while True:
        s = fobj.readline();
        if len(s) == 0:
            break;
        [fromNd, toNd] = s.split('\t');
        fromNd = int(fromNd); toNd = int(toNd);
        edgeList2.append((fromNd, toNd));
        nodeList2.append(fromNd); nodeList2.append(toNd);
    fobj.close();
    
    edgeSet2 = set(edgeList2); nodeSet2 = set(nodeList2);       # converted from lists into sets 
    s1 = nodeSet2 - nodeSet1; s2 = edgeSet2 - edgeSet1;         # get the added nodes which are present in file i but not present in file i-1
    s3 = nodeSet1 - nodeSet2; s4 = edgeSet1 - edgeSet2;         # get the deleted nodes which are not present in file i but are present in file i-1

    writeGML(i, date, s1, s2, s3, s4);      # write into GraphML format

    edgeList1 = edgeList2[:]; nodeList1 = nodeList2[:];
    edgeSet1 = set(edgeList1); nodeSet1 = set(nodeList1);
    
    
print 'Finished reading and writing...';
print 'There are', len(fileList), 'daily instances in this Autonomous System (AS) dataset.';


