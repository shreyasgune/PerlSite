#!/usr/bin/perl -T --

use warnings;
use CGI qw(:standard);
use DBI;
use CGI::Carp qw(fatalsToBrowser); #redirects the errors from the errorlogs to the browser, so you know exactly where things went wrong.
use strict;
use JSON; #to be able to use the JSON parsing 
binmode STDOUT, ":utf8"; #to define the proper encoding scheme
use utf8;


my @output;

#connect to the DB
my $driver = "SQLite";
my $database = "/home/www/cgi-bin/mydata.db";
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, {RaiseError=> 1}) or die $DBI::errstr;

# print DBIx::JSON->new($dsn, $userid, $password)->do_select("select * from table;")->get_json;  <--- this is an alternative method. I just left it here, but you're going to have to "cpan DBIx:JSON" to use this.

my $sth = $dbh->prepare('select * from appointed'); #our table is named appointed.
$sth -> execute;

while(my $row = $sth->fetchrow_hashref) #basically $sth is getting stuff from the database as a hashref datatype and putting all of that in a output array.
{
	push @output, $row;

}


my $cgi = CGI->new;
print $cgi->header('text/html');
print to_json({data=> \@output}); #this just returns a JSON formatted data of the stuff we pulled from our database

#make a JSON file as well. You never know, when you can use this shit.
my $fh;
open  $fh, ">", "data_out.json";
print $fh to_json({data=> \@output});
close $fh; 
