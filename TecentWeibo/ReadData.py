'''
Created on Jun 22, 2012

@author: yyb
'''

'Read data from these original data files'


usrInfo = {};       # a dictionary for storing user information (key = userID, value = (birth year, gender, num of tweets, tagIDs))
itmInfo = {};       # a dictionary for storing item information (key = itemID, value = (category, keyword))
kwdDict = {};       # a dictionary for storing users' keywords

usrDict = {};
itmDict = {};


#===============================================================================
# Read user information
#===============================================================================
def readUserInfo():
    fobj = open('../Raw Data/user_profile.txt', 'r');
    print 'Reading user data ... ';
    while True:
        s = fobj.readline();
        if len(s) == 0:
            break;
        li = s.split();
        uID = int(li[0]); birth = li[1]; gender = li[2]; tweet = li[3]; tagIDs = li[4];
        usrInfo[uID] = (birth, gender, tweet, tagIDs);
        usrDict[uID] = 0;
    fobj.close();
    print 'Finish!';


#===============================================================================
# Read item information
#===============================================================================
def readItemInfo():
    fobj = open('../Raw Data/item.txt', 'r');
    print 'Reading item data ... ';
    while True:
        s = fobj.readline();
        if len(s) == 0:
            break;
        li = s.split();
        itmID = int(li[0]); cat = li[1]; kword = li[2];
        itmInfo[itmID] = (cat, kword);
        itmDict[itmID] = 0;
    fobj.close(); 
    print 'Finish!';   


#===============================================================================
# Read users' keywords
#===============================================================================
def readUsrKwd():
    fobj = open('../Raw Data/user_key_word.txt', 'r');
    print 'Reading user keywords ... ';
    while True:
        s = fobj.readline();
        if len(s) == 0:
            break;
        li = s.split();
        uid = int(li[0]);
        kwdDict[uid] = li[1];
    fobj.close();
    print 'Finish!';

    
    
