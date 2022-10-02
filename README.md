<p align="center">
    <img src="./calculate/static/img/rpc_logo.jpg"/>
</p>

# Running Performance Calculator
**by Josh Embury**

### Overview
Running Performance Calculator is a website for predicting future running race
 performance and ranking past performances at various distances.
The website can be found at: https://running-performance.herokuapp.com/

### Motivation
As a runner it is important to evaluate fitness as training progresses. By knowing where your
fitness is at during a training cycle, one can easily determine the appropriate training intensites.
A well-accepted method of determining running fitness is by using Dr. Jack Daniels' Running Formula to
determine VDOT.
This application calculates your VDOT for running performances at standard distances and
ranks the VDOT values. This ranking helps to illustrate the athlete's stengths and weaknesses.
Understanding your VDOT profile across various distances can help to guide future training.
<br>
Sometimes it is difficult to estimate how an athlete will perform over a certain race distance
 (perhaps a distance they've never raced before), particularly if the course is not completely flat.
Another feature this application provides is an estimation of what an athlete can run for a
specified distance and average gradient, given their personal best running
times at other distances.

### Features
<ul>
    <li>Clean and user-friendly interface</li>
    <li>Supports input of personal best running times for standard distances</li>
    <li>Support for custom target race distances</li>
    <li>Rank your personal best running times based on VDOT</li>
    <li>Input average grade to see how this impacts performance</li>
</ul>

### Technologies
<ul>
    <li>Python</li>
    <li>Django</li>
    <li>Heroku</li>
    <li>Bootstrap</li>
</ul>

### Download Instructions

*Ensure that you have installed a Code Editor such as Sublime Text*

METHOD 1, Command Line:

Open terminal and run git clone https://github.com/emburyj/Running-Performance-Calculator.git

METHOD 2, GitHub Web Interface:

1) Visit https://github.com/emburyj/Running-Performance-Calculator
2) Click on the green button labeled Clone or download
3) Select Download ZIP
4) Open the ZIP file and extract its contents to the desired location on your computer
5) Open Sublime Text or the editor of your choice
6) Open a new terminal in your code editor
7) Install all dependencies by running the command "pip install -r requirements.txt"
8) Start the program by typing the command "./manage.py runserver" in your terminal
9) The program will open locally in your browser