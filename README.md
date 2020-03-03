# Run0ff_Calc
This is piece of code that calculates the run off generated, its application comes in the field of Agriculture, Agricultural Engineering and more.

To run this piece of code you must be running Python 3 and have the following modules installed
<ul>
  <li>Pysimplegui</li>
  <li>imatplotlib</li>
  <li>xlrd</li>
  <li>pandas</li>
  <li>numpy</li>
  <li>time</li>
  <li>json</li>
</ul>

It has an interactive interface that was created using PySimpleGUI, each interface is self explanatory.
Here is a lumped image showing majority of the intefaces.
<br>
![interfaces](imgs/Screenshot%20(165).png)

In order to use the program, fill the form as required,
![landing nterfaces](imgs/Screenshot%20(166).png)
Enter the area of the land
<br>
Then your CN2 value if you already know it, but you can always select the calculate button to calculate the CN2 value
<br>
When you select the calculate button, you get the option to select the hydrological soil types with which you want to calculate the CN2 value.
<br>
![interfaces](imgs/Screenshot%20(168).png)
<br>
when you do this, you fill the percentage composition of the various constituent of the soil types,
<br>
![interfaces](imgs/Screenshot%20(169).png)
<br>
![interfaces](imgs/Screenshot%20(170).png)
<br>
![interfaces](imgs/Screenshot%20(171).png)
the software altomatically calculates the CN2 values and places the result in the form that appears next
![interfaces](imgs/Screenshot%20(172).png)
<br>
You can then select the source file containing the data you want the software to work on. The software works on JSON, CSV AND EXCEL files. Sample files showing the file structure the software works with are available in the *samplefile* folder.
<br>
Graphs showing the results are then generated. The ia also an avenue for making comments. After the comment has been made the entire result is written to a file as well as the comments
