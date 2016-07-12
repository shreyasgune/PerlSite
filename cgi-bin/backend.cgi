#!/usr/bin/perl -w #gives warnings enabled 
#telling the OS (that understands the shebang) to find the first "perl" executable in the list of $PATH, and exec that program by appending the current file name after the shebang. 

use warnings; 
use CGI qw(:standard); 
use DBI;
use CGI::Carp qw(fatalsToBrowser);
use strict; # Perl will check for potential mistakes, thereby helping you to avoid common Perl pitfalls
use HTML::Parser;

my $cgi = new CGI;
print $cgi->header; #pushes out the header for the browser to make sense of the script output
print $cgi->start_html(-title=>'Appointed Output');

#get stuff from the web page
my $dateset = param('dateset');
my $timeset = param('timeset');
my $descset = param('descset'); 

print "Date: $dateset | Time: $timeset | Description: $descset has been added to the database";
#the above prints an interim message to show that the data that you entered is being put into the database


#connect to the DB
my $driver = "SQLite";
my $database = "/home/www/cgi-bin/mydata.db"; #this is already packaged in the /cgi-bin/ , but you could host the Database someplace else and pass the URL here.
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, {RaiseError=> 1}) or die $DBI::errstr;
my $stmt = q/INSERT INTO appointed (dateval,timeval,descval) VALUES (?,?,?)/; #the '?,?,?' is a neat way to pass values when you execute the SQL statement.
my $sth = $dbh->prepare($stmt); #SQL prepped
$sth->execute($dateset, $timeset, $descset);

#Reroute to the same page
print '<meta http-equiv="refresh" content="1;url=http://localhost/appoint.html">';

#to disconnect uncomment the code below
$dbh->disconnect(); 

