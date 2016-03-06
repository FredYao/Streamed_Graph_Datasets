Data link:
http://snap.stanford.edu/data/cit-HepPh.html


----------------------------------------------------------------------------------------------------------------------

A. Source Code

The source code (ReadData.py and WriteData.py) are used for generating the GraphML format files. I did the programming in Python2.7+Eclipse environment. But one can compile these two files in any Python platform.

Here are some instructions for compiling and running the code:
	(1) Create a folder named 'HepPh' in your local disk.
	(2) Create 3 folders named 'Raw Data', 'src', 'GraphML' in 'HepPh' folder.
	(3) Go to http://snap.stanford.edu/data/cit-HepPh.html, download 'cit-HepPh.txt.gz' and 'cit-HepPh-dates.txt.gz', extract them and put all the extracted txt documents into your 'Raw Data' folder.
	(4) Download ReadData.py and WriteData.py from my website and put them into 'src' folder, and you can compile and run them with ReadData.py being a module:
		python ReadData.py
		python WriteData.py
		(In Windows Systems, you can double-click WriteData.py to execute them.) 
	(5) Enter an integer as a value for time-window size, then you will get your generated GraphML files in 'GraphML' folder.

----------------------------------------------------------------------------------------------------------------------

B. Sample file

The original data files have been converted into 3487 daily instances. And the sample file is one of the those instances.
The nodes represent papers submitted in the corresponding month. And the directed edges represent citations from the new papers to the old papers.

----------------------------------------------------------------------------------------------------------------------

C. Citations:

(1)J. Leskovec, J. Kleinberg and C. Faloutsos. Graphs over Time: Densification Laws, Shrinking Diameters and Possible Explanations. 
	ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), 2005.
	
(2)J. Gehrke, P. Ginsparg, J. M. Kleinberg. Overview of the 2003 KDD Cup. SIGKDD Explorations 5(2): 149-151, 2003.
