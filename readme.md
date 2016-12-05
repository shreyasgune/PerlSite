#Appointments WebApp

## Synopsis
This is a simple WebApp that takes in inputs from the user  to record the date, time and description of an appointment.

## Technologies Used
PERL</br>
JSON</br>
SQL (can be any type of SQL)</br>
JQUERY</br>
HTML</br>

# Front End Look
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

## Install the dependencies
```
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install sqlite3 libsqlite3-dev
sudo apt-get install build-essential
```

## Create cgi-bin folder and grant it permissions
`sudo mkdir /home/www/cgi-bin/`</br>
`sudo chmod 777 /home/www/cgi-bin/` </br>

## Put your html files in  
`/var/www/html/` 

## Edit apache2.conf
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

## Install perl dependencies
```
sudo apt-get install libconfig-yaml-perl
cpan DBD::SQLite
cpan DBI
```

## One very important point : To enable CGI scripts to run Apache2
`sudo a2enmod cgi`

Also , remember to `sudo chmod 777 <your_script_file>` your `.cgi` files. 

# A Short and Sweet : Perl Essentials
### ------------------------{PERL GUIDE BEGINS}---------------
So, I have had a bit of an experience with Perl. So here is my : get it done fast listing.</br> 

A Perl script is a text file with the extension `.pl`.</br>

## Hello World
Here's the full text of `helloworld.pl`:
```
use strict;
use warnings;

print "Hello world";
Perl scripts are interpreted by the Perl interpreter, perl or perl.exe:
```
</br>
To run it :: `perl helloworld.pl [arg0 [arg1 [arg2 ...]]]`
</br>
## Variables
Perl is made up of only three kind of variables : Scalars, Arrays and Hashes</br>
Scalar can be : undef(null), number, string, reference to another variable. PERL HAS NO BOOLEAN.</br> False is (undef, 0, string "", string "0")

## Arrays 
They are declared with `@variableName` syntax.</br>
```
my @array = (
	"print",
	"these",
	"strings",
	"out",
	"for",
	"me", # trailing comma is okay
);

```

The access to the array elements is the usual array[num] or backwards : array[-num]. Yeah, it's circular that way.</br>
There is no collision between a scalar `$var` and an array `@var` containing a scalar entry `$var[0]`</br>
This is also allowed : `print "@array"` and you'll get the enitre array printed.</br>


### Array Functions
`<func> @arrayName`</br>
`pop @array` returns the final element of the array.</br>
`push @array, "val1", "val2";` appends stuff to the array.</br>
`shift @array` extracts and returns the first element of the array.</br>
`unshift @array, "val1"` inserts a new element at the start of the array.</br>
`join(", ", @arrayElements` concatenates many strings into one.</br>

Map,grep and sort</br>
`my @capitals = ("Baton Rouge", "Indianapolis", "Columbus", "Montgomery", "Helena", "Denver", "Boise");`

MAP</br>
The `map` function takes an array as input and applies an operation to every scalar $_ in this array. It then constructs a new array out of the results</br>
```
print join ", ", map { uc $_ } @capitals;
# "BATON ROUGE, INDIANAPOLIS, COLUMBUS, MONTGOMERY, HELENA, DENVER, BOISE"
```

GREP</br>
The grep function takes an array as input and returns a filtered array as output. The syntax is similar to map. This time, the second argument is evaluated for each scalar $_ in the input array. If a boolean true value is returned, the scalar is put into the output array, otherwise not.</br>
```
print join ", ", grep { length $_ == 6 } @capitals;
# "Helena, Denver"

print scalar grep { $_ eq "Columbus" } @capitals; # "1"
```

SORT</br>
```
my @elevations = (19, 1, 2, 100, 3, 98, 100, 1056);

print join ", ", sort @elevations;
# "1, 100, 100, 1056, 19, 2, 3, 98"
```

## Hash
Hashes take the form of your normal key-value pair.</br>
`my %varname = ( "key" => "value" ); ` 

example</br> 
```
my %scientists = (
	"Newton"   => "Isaac",
	"Einstein" => "Albert",
	"Darwin"   => "Charles",
);
```
If you want to access a particular key's value : `print $scientists{"Newton"};` and the output will be `Isaac`.</br>

## References
The same `\` works for hashes and arrays as well as far as references is concerned.</br>
```
my $variable = "somevalue";
my $variableRef = \$variable;
```

## A roundup
```
my $data = "orange";
my @data = ("purple");
my %data = ( "0" => "blue");

print $data;      # "orange"
print $data[0];   # "purple"
print $data["0"]; # "purple"
print $data{0};   # "blue"
print $data{"0"}; # "blue"

```

## Conditionals
Pretty straight forward. Just, `else if` changes to `elif`. There is this `unless ... else` thing but it's confusing so I'm going to skip it.</br>

## Ternary Operator
```
my $gain = 48;
print "You gained ", $gain, " ", ($gain == 1 ? "experience point" : "experience points"), "!";
```

## Loops
### While
```
my $i = 0;
while($i < scalar @array) {
	print $i, ": ", $array[$i];
	$i++;
}
```

### until
```
my $i = 0;
until($i >= scalar @array) {
	print $i, ": ", $array[$i];
	$i++;
}
```

### For and For-each
```
#for loop
for(my $i = 0; $i < scalar @array; $i++) {
	print $i, ": ", $array[$i];
}

#foreach
foreach my $key (keys %scientists) {
	print $key, ": ", $scientists{$key};
}
```


## Subroutines
Subroutines are declared using the `sub` keyword. In contrast with built-in functions, user-defined subroutines always accept the same input: a list of scalars.</br>That list may of course have a single element, or be empty.</br> A single scalar is taken as a list with a single element. A hash with N elements is taken as a list with 2N elements.</br>

```
sub somename()
{
	my($arg1,$arg2,$arg3) = (@_); #this is where all our arguments from our function call land up
	
	#here is a simple test that will show how we return a hash
	if(!$arg1 || !$arg2 || !$arg3) 
	{
		#This is a hash that is returned.
		return {Message => "No argument found"};
	}
	
	return { KEY => arg1 };
}

somename() # nothing is passed in so it's going to fail and return { Message => "No argument found" }
somename("argument 1","argument 2","argument 3"); # this will return :: { KEY=> "argument 1"}

```

## Module
A module is a `.pm` file that you can include in another Perl file (script or module). A module is a text file with exactly the same syntax as a `.pl` Perl script.</br> An example module might be located at `C:\foo\bar\baz\Demo\StringUtils.pm` or `/foo/bar/baz/Demo/StringUtils.pm`, and read as follows:</br>

```
use strict;
use warnings;

sub zombify {
	my $word = shift @_;
	$word =~ s/[aeiou]/r/g;
	return $word;
}

return 1;
```
</br>
Because a module is executed from top to bottom when it is loaded, you need to return a true value at the end to show that it was loaded successfully.</br>

Once the Perl module is created and perl knows where to look for it, you can use the `require` built-in function to search for and execute it during a Perl script.</br>

```
use strict;
use warnings;

require Demo::StringUtils;

print zombify("i want brains"); # "r wrnt brrrns"
```

## Packages
A package is a namespace in which subroutines can be declared. Any subroutine you declare is implicitly declared within the current package. At the beginning of execution, you are in the main package, but you can switch package using the package built-in function:</br>

```
use strict;
use warnings;

sub subroutine {
	print "universe";
}

package Food::Potatoes;

# no collision:
sub subroutine {
	print "kingedward";
}
```
### ATTENTION :
A Perl script (.pl file) must always contain exactly zero package declarations.</br>
A Perl module (.pm file) must always contain exactly one package declaration, corresponding exactly to its name and location. E.g.</br> module `Demo/StringUtils.pm` must begin with package `Demo::StringUtils`.

### -----------------------------{PERL GUIDE ENDS}-------------------

## API Reference
[JQUERY API](https://api.jquery.com/)</br>
[AJAX](http://api.jquery.com/jquery.ajax/)</br>
[SQLite3](https://www.sqlite.org/docs.html)</br>
[JSON Docs](http://www.json.org/)</br>
[Apache Docs](http://httpd.apache.org/docs/current/howto/cgi.html)</br>
[Perl Docs](http://perldoc.perl.org/)</br>
[SQLite3 for Perl](http://search.cpan.org/~msergeant/DBD-SQLite-0.31/lib/DBD/SQLite.pm)</br>

## Contributors
If you want to contribute or add to it or make it better, more readable, go for it. Tweet me issues if you can  : [@shreyaslumos](https://www.twitter.com/shreyaslumos) 

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Appointments WebApp</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Shreyas Gune</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.


 
