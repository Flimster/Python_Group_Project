# ThinkBack

ThinkBack is a website that allows the user to submit his assignment through the website's file upload system. The websites categorizes assignments into two, active assignments and past assignments. The ThinkBack system will then notify if the user's submission passed or failed, giving the results of the tests.</br>
We prioritized on having a functional bug-free program as opposed to a semi-functioning feature rich problem. Each feature that we added was done with a lot of testing
and refactoring.

### Getting started

To get the website running on your local machine you need to follow these steps. </br>

You need to have the following installed: </br>
[SQLite 3.26.0](https://sqlite.org/index.html) </br>
[python3 3.7.1](https://www.python.org/) </br>
[pip 18.1](https://pip.pypa.io/en/stable/installing/) </br>
[flask 1.0.2](http://flask.pocoo.org/) </br>

## Installing

Once you have those installed, unzip the downloaded folder to the desired location. The next step is to set up a local server with flask. To do that you need to run the following commands in a terminal at the folder's directory:</br>

`pip3 install -r requirement.txt`</br>
`export FLASK_APP=thinkback/thinkback.py`</br>
`flask run`</br>

This will launch the server and host the website on your computer.</br>

#### Setting up the database with example data

We also have a database with some example data to work with. To **initialize** the database run the following command in the terminal: </br>

`flask initdb` </br>

You should receive this message in the terminal: </br>

`Initializes the database.` </br>
`Initialized the database.` </br>
`Closes the database again at the end of the request` </br>

#### Deleting the database

To **clear** all data from the database run the following command: </br>

`flask dropdb` </br>

You should receive this message in the terminal: </br>

`Dropping database.` </br>
`Dropped database.` </br>
`Closes the database again at the end of the request` </br>

If, for some reason, you don't feel like making the solutions yourself for the example Assignments and their problems in the database with the example data
we have mode them for you. They can be found in the 'solutions' folder and if you want to test to see how the system reacts to wrong answers or function names,
just break the code.

### Deployment

It is not recommended to deploy the system on a live server since this program is in it's early alpha stage, and has not gone through extensive security testing.

### Authors

Ingi Þór Sigurðsson and Tyler Elías Jones are the creators of ThinkBack

### License 

MIT
