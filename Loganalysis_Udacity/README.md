## PROJECT LOGS ANALYSIS PROJECT
## by VENNAPUSA ANANTHREDDY

## INTRODUCTION TO LOGANALYSIS PROJECT

This is a python module that uses information of large database of a web server and draw business conclusions from that information. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.
 
 news database contains  three tables 

i. authors table  containsinformation about the authors of articles.

ii. articles table includes the articles themselves.

iii. log table includes one entry for each time a user has accessed the site

 This project consists for the following files are:

* LogAnalysis_Udacity.py - main file to run this Logs Analysis Reporting tool
* README.md - instructions to install this reporting tool
* newsdata.sql - database file
* viwes.sql-database file
* Output.JPG

## THE THREE QUESTIONS WE HAVE TO ANSWER IN THIS PROJECT ARE BELOW 
  
>   1.What are the most popular three articles of all time?
>   2.What are the most popular four authors articles of all time?
>   3.On which days did more than 1% of requests lead to errors?

## MAIN FUNCTIONS USED IN LOGANALYSIS_UDACITY.PY ARE: 

i.top_three_art()--it  gives the result for most popular three articles of all time
ii.top_three_aut()--it gives the result for most popular article authors of all time
iii.log_error_ana()--it gives the result for  days on which more than 1% of requests lead to errors
iv.connect()--Connects to the PostgreSQL database and returns a database connection

## VIEWS CREATED IN THIS PROJECT ARE
 
1.create or replace view webster as
select count(*) as dhat, 
status, cast(time as date) as day
from log where status like '%404%'
group by status, day
order by dhat desc limit 3;

2.create or replace view allguest as
select count(*) as tripper,
cast(time as date) as errorphase
from log
group by errorphase;

3.create or replace view runcount as
select * from webster join allguest
on webster.day = allguest.errorphase;

There are some dependancies and a few instructions on how to run the application.

 ## DEPENDENCIES

- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

    
	HOW TO INSTALL
	
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd /vagrant` as instructed in terminal

 How to Run Project

Download the project zip file to you computer and unzip the file then place inside `vagrant/Log_Analysis_Udacity`.

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. download database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

  4. Unzip this file after downloading it. The file inside is called newsdata.sql.

  5. Copy the newsdata.sql file and place inside `vagrant/Loganalysis_Udacity`.

  6. In terminal Change directory to `vagrant/` and look around with ls.

  7. Load the data in local database using the command:

  ```
    $ psql -d news -f newsdata.sql
  ```
  8. Load the Virtual Tables or Create Views in Local Data Base
  
  ```
    $ psql -d news -f views.sql
  ```
   9. Run newsdata.py using:
  ```
    $ python LogAnalysis_Udacity.py
  ```
  Note: queries will take sometime to execute 



## OUTPUT:

## OUTPUT OF LOG ANALYSIS PROJECT:

#--------------------------------------------------------------


  
  ^^What are the top three articles of all time ?

++++++++++++++++++++++++++++++++++++++++++++++++++
Candidate is jerk, alleges rival338647 views
++++++++++++++++++++++++++++++++++++++++++++++
Bears love berries, alleges bear253801 views
++++++++++++++++++++++++++++++++++++++++++++++
Bad things gone, say good people170098 views
++++++++++++++++++++++++++++++++++++++++++++++

  ^^Who are the top article authors of all time ?

+++++++++++++++++++++++++++++++++++++++++++++
Ursula La Multa"        Aut507594 views
++++++++++++++++++++++++++++++++++++++++++++++
Rudolf von Treppenwitz" Aut423457 views
++++++++++++++++++++++++++++++++++++++++++++++
Anonymous Contributor"  Aut170098 views
++++++++++++++++++++++++++++++++++++++++++++++
Markoff Chaney" Aut84557 views
++++++++++++++++++++++++++++++++++++++++++++++

  ^^^Days on which more than 1% of requests lead to errors ?
        17 Jul 2016 - 2.263%
		
		
#---------------------------------------------------------------  
  
##  OUTPUT:

  See exact output of loganalysis project here()

##  HELPFULL DOCUMENTATION LINKS:

>  Postgresql documentation to learn sql queries(https://www.tutorialspoint.com/postgresql/)
>  PEP8 tool to check Python styles (http://pep8online.com/)