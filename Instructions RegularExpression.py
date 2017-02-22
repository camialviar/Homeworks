Instructions RegularExpression.py

Before running the program:
1.  Note that the txt "Dan Jurafsky" contains strings that begin with the prefix 'mod' as well as strings without it. 
2. Note that the txt file  "JurafskyBigChanges" is empty. 
The program will select the strings that don't have the 'mod' prefix on them and write them in the "JurafskyBigChanges" file. You can look for these strings in the "JurafskyBigChanges" file after running the program.

Program description:

The program helps identify the strings on a text file (Dan Jurafsky.txt) that don't have the code "mod" on them, and writes them in a new file (JurafskyBigChanges.txt). The original txt file was extracted from elan, in which slide changes in a video of a lecture were identified. Each string corresponds to a change in the slides and records the time of the event in ms, as well as the code assigned to that event. Some of the slide changes were small modification of the previous slide and were assigned the prefix 'mod'. In order to evaluate the performance of an automated method that identifies slide changes, we want only the 
ones that correspond to full modifications of the slides (i.e., the ones without the prefix 'mod'. This program identifies those cases and produces a text file that can be imported into R.


