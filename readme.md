#Appointments WebApp

## Synopsis
This is a simple WebApp that takes in inputs from the user  to record the date, time and description of an appointment.

## Technologies Used
PERL</br>
JSON</br>
SQL (can be any type of SQL)</br>
JQUERY</br>
HTML</br>

##Deployed Here
[http://52.23.229.225/appoint.html](http://52.23.229.225/appoint.html)

#Front End Look
When appointments are absent
```
=============================================
	=  +---+
	=  |NEW|
	=  +---+
	=  
	=  +-------------------+  +------+
	=  |                   |  |SEARCH|
	=  +-------------------+  +------+
	=
	=  <appointments table will be here>
=============================================
```
When appointments exist
```
==============================================
	=  
	=  +---+
	=  |NEW|
	=  +---+
	=  
	=  +-------------------+  +------+
	=  |                   |  |SEARCH|
	=  +-------------------+  +------+
	=  
	=  +-------+---------+----------------+
	=  | DATE  | TIME    | DESCRIPTION    |
	=  +-------+---------+----------------+
	=  | May 2 | 11:00am | Something      |
	=  | May 2 | 12:00pm | Something else |
	=  | May 4 |  8:00am | Meet foo       |
	=  +-------+---------+----------------+
	=  
==============================================
```
When search is implemented
```
==============================================
	=  
	=  +---+
	=  |NEW|
	=  +---+
	=  
	=  +-------------------+  +------+
	=  | Something         |  |SEARCH|
	=  +-------------------+  +------+
	=  
	=  +-------+---------+----------------+
	=  | DATE  | TIME    | DESCRIPTION    |
	=  +-------+---------+----------------+
	=  | May 2 | 11:00am | Something      |
	=  | May 2 | 12:00pm | Something else |
	=  +-------+---------+----------------+
	=  <notice only the rows containing "Something" appear>
==============================================
```
When you "ADD" something
```
==============================================
	=  
	=  +---+ +------+
	=  |ADD| |CANCEL|
	=  +---+ +------+
	=  
	=       +--------------------+
	=  DATE |                    |
	=       +--------------------+
	=       +--------------------+
	=  TIME |                    |
	=       +--------------------+
	=       +--------------------+
	=  DESC |                    |
	=       +--------------------+ 
	=  
	=  +-------------------+  +------+
	=  |                   |  |SEARCH|
	=  +-------------------+  +------+
	=  
	=  +-------+---------+----------------+
	=  | DATE  | TIME    | DESCRIPTION    |
	=  +-------+---------+----------------+
	=  | May 2 | 11:00am | Something      |
	=  | May 2 | 12:00pm | Something else |
	=  | May 4 |  8:00am | Meet foo       |
	=  +-------+---------+----------------+
	=  
==============================================
```

##Install the dependencies
```
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install sqlite3 libsqlite3-dev
sudo apt-get install build-essential
```

##Create cgi-bin folder and grant it permissions
`sudo mkdir /home/www/cgi-bin/`</br>
`sudo chmod 777 /home/www/cgi-bin/` </br>

##Put your html files in  
`/var/www/html/` 

##Edit apache2.conf
I've given you the file, if you just want to go ahead and replace it.

```
ScriptAlias /cgi-bin/ /home/www/cgi-bin/
AddHandler cgi-script .pl
TypesConfig /etc/mime.types 
<Directory /home/www/cgi-bin/>
Options +ExecCGI

#AddHandler cgi-script cgi pl
Require all granted
#Options Indexes FollowSymLinks
</Directory> 

```

##Install perl dependencies
```
sudo apt-get install libconfig-yaml-perl
cpan DBD::SQLite
cpan DBI
```

##One very important point : To enable CGI scripts to run Apache2
`sudo a2enmod cgi`

Also , remember to `sudo chmod 777 <your_script_file>` your `.cgi` files. 

## API Reference
![JQUERY API](https://api.jquery.com/)</br>
![AJAX](http://api.jquery.com/jquery.ajax/)</br>
![SQLite3](https://www.sqlite.org/docs.html)</br>
![JSON Docs](http://www.json.org/)</br>
![Apache Docs](http://httpd.apache.org/docs/current/howto/cgi.html)</br>
![Perl Docs](http://perldoc.perl.org/)</br>
![SQLite3 for Perl](http://search.cpan.org/~msergeant/DBD-SQLite-0.31/lib/DBD/SQLite.pm)</br>

## Contributors
If you want to contribute or add to it or make it better, more readable, go for it. Tweet me issues if you can  : [@shreyaslumos](https://www.twitter.com/shreyaslumos) 

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Appointments WebApp</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Shreyas Gune</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.


 
