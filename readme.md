#Dice roller!
This is a super basic webapp that I wrote because I wanted a way to roll
any particular dice combination, whether it's a d20 or some variant of the fudge
die. I also wanted to be able to see all of my characters while doing that.
I  realize that if I tried to learn roll20 I could probably get everything I wanted
from that site, but this is also a good opportunity to learn Flask.

This is still in a development "stage." Setting it up for actual deployment can be
done with [Flask's deployment tutorial][1]. Alternatively, it can be run as is,
by installing Flask. Currently, the project has no dependencies beyond standard
Flask, javascript, and a browser that can run html5 (I use data attributes).

[1]:http://flask.pocoo.org/docs/0.12/deploying/
## Current features:
* When a dice formula is entered in the form of "ndx + [first three letters of attribute]"
the program generates the dice throws and displays it by "result".

## Future features:
* The ability to add characters
* The ability to define the attributes for characters
* Saving this data to a file within the flask directory. (This, and templates, is why I'm using flask)
* The ability to show a table for test difficulties.
* Make this pretty
