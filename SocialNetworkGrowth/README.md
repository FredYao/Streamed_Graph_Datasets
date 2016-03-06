Data link:
http://socialnetworks.mpi-sws.org/


----------------------------------------------------------------------------------------------------------------------

A. Raw Data
The Social Network Growth data consists of the Facebook-Growth data which spans an interval from Sep 5, 2006 to Jan 21, 2009.


----------------------------------------------------------------------------------------------------------------------

B. Source Code

The source code (ReadData.py and WriteData.py) are used for generating the GraphML format files. I did the programming in Python2.7+Eclipse environment. But one can compile the two Python files in any Python platform.

Here are instructions for compiling and running the code (give an example for Facebook-Growth case): 
	(1) Create a folder named 'Facebook-Growth' in your local disk.
	(2) Create 3 folders named 'Raw Data', 'src', 'GraphML' under 'Facebook-Growth' folder.
	(3) Go to http://socialnetworks.mpi-sws.org/data-wosn2009.html, download 'Facebook Links' file.
	(4) Extract the downloaded file and then you will get a file facebook-links.txt.anon
	(6) Put the file facebook-links.txt.anon into 'Raw Data' folder.
	(7) Download the two Python files in Source Code link from my website, and put them into 'src' folder.
	(8) Compile the two Python files with ReadData.py being a module, then run:
		python ReadData.py
		python WriteData.py
		 (For Windows Systems, you can directly double-click WriteData.py to execute it.) Enter any integer as a tims-windows size.
	(9) You will get your generated GraphML files in 'GraphML' folder.


----------------------------------------------------------------------------------------------------------------------

C. Sample file

It's an instance from the generated GraphML files. It contains the network growth data of a certain time-span.


----------------------------------------------------------------------------------------------------------------------

D. Citation:

	(1) Alan Mislove and Hema Swetha Koppula and Krishna P. Gummadi and Peter Druschel and Bobby Bhattacharjee. Growth of the Flickr Social Network.
		Proceedings of the 1st ACM SIGCOMM Workshop on Social Networks (WOSN'08). Seattle, WA. August, 2008.
		
	(2) Alan Mislove. Online Social Networks:  Measurement, Analysis, and Applications to Distributed Information Systems.
		PhDThesis, Rice University, Department of Computer Science. May 2009.
		
	(3) Bimal Viswanath and Alan Mislove and Meeyoung Cha and Krishna P. Gummadi. On the Evolution of User Interaction in Facebook.
		Proceedings of the 2nd ACM SIGCOMM Workshop on Social Networks (WOSN'09). Barcelona, Spain. August, 2009.
		
	(4) http://socialnetworks.mpi-sws.org

