#permeate minute keeping
##usage
create a new (LaTeX) file for each new meeting. The process automatically adds a table of contents to each file, so create sections and subsection.

invoke the program with python3 with the argument of the file you want to compile. It will---if there aren't any errors---spit out a pdf for this meeting.

eg.
python3 filler.py date.tex

##what are these files?
###template.tex
this is the LaTeX template that the minutes use.
###filler.py
this is the python script that's used to populate the templates.

##TODO:
###create a way to compile yaml to LaTeX
