# ThinkBack

ThinkBack is a website that allows the user to submit his assignment through the website's file upload system. The websites categorizes assignments into two, active assignments and past assignments. The ThinkBack system will then notify if the user's submission passed or failed, giving the results of the tests made.

### Getting started

To get the website running on your local machine you need to follow these steps. </br>

You need to have the following installed: </br>
[SQLite](https://sqlite.org/index.html) </br>
[python3](https://www.python.org/) </br>
[pip](https://pip.pypa.io/en/stable/installing/) </br>
[flask](http://flask.pocoo.org/)</br>

### Installing

Once you have those programs up and running, unzip the downloaded folder to the desired location. The next step is to set up a local server with flask. To do that you need to run the following commands in a terminal at the folder's directory:</br>

`export FLASK_APP=thinkback.py`</br>
`flask run`</br>

This will launch the server and host the website on your computer.</br>

We also have a database with some example data to work with. To initialize the database run the following command in the terminal: </br>

`flask initdb` </br>

You should receive this message in the terminal: </br>

`Initializes the database.` </br>
`Initialized the database.` </br>
`Closes the database again at the end of the request` </br>

To clear all data from the database run the following command: </br>

`flask dropdb` </br>

You should receive this message in the terminal: </br>

`Dropping database.` </br>
`Dropped database.` </br>
`Closes the database again at the end of the request` </br>

### Deployment

It is not recommended to deploy the system on a live server since this program is in it's early alpha stage, and has not gone trough extensive security testing.

### Authors

Ingi Þór Sigurðsson and Tyler Elías Jones are the creators of ThinkBack

### License 


MIT