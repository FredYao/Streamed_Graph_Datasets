Data link:
http://www.kddcup2012.org/c/kddcup2012-track1/data


----------------------------------------------------------------------------------------------------------------------

A. Source Code

The source code (Preprocess.py, ReadData.py and WriteData.py) are used for generating the GraphML format files. I did the programming in Python2.7+Eclipse environment. But one can compile those Python files in any Python platform.

Here are instructions for compiling and running the code:
	(1) Create a folder named 'Tencent Weibo' in your local disk.
	(2) Create 3 folders named 'Raw Data', 'src', 'GraphML' under 'Tencent Weibo' folder.
	(3) Go to http://www.kddcup2012.org/c/kddcup2012-track1/data, download 'track1.7z' or 'track1.zip', either one will be OK.
	(4) Extract the downloaded compressed file and then you will get some txt files. Get the following four files: item.txt, rec_log_train.txt, user_profile.txt, user_sns.txt, and put them into 'Raw Data' folder.
	(5) In 'Raw Data' folder, create two subfolders named 'hourly' and 'daily'.
	(6) Download preprocess code (Preprocess.py) from my website and put them into 'Tencent Weibo/src' folder.
	(7) Compile and run the preprocess code:
		python Preprocess.py
		 (In Windows Systems, you can directly double-click Preprocess.py to execute it.) And you will get .txt files in 'Raw Data/hourly' and 'Raw Data/daily' folders.
	(8) Download ReadData.py and WriteData.py in Source Code link from my website, and put them into 'Tencent Weibo/src' folder.
	(9) Compile and run them with ReadData.py being compuled as a module:
		python ReadData.py
		python WriteData.py
		 (In Windows Systems, you can double-click WriteData.py to execute it.) Then enter an integer as a value for time-window size.
	(10) You will get your generated GraphML files under 'Tencent Weibo/GraphML' folder.

----------------------------------------------------------------------------------------------------------------------

B. Sample file

It contains an hourly instance of the recommendation events in Weibo system. The nodes represent users and items. And the edges represent 
items recommended to users and follow-relations between users.

----------------------------------------------------------------------------------------------------------------------

C. Citation:
	
	(1) KDD-2012: http://sigkdd.org/kdd2012/kddcup.shtml
	
	(2) KDD Cup 2012 Track1: http://www.kddcup2012.org/c/kddcup2012-track1
	
