# apidemonstration
This application was created for full throtle labs assingment for django application.

This application is a sample demonstration of creating custom management commands in django and use of django rest framework.

-----
DEPENDENCIES

The List of modules required are:
asgiref==3.2.7
Babel==2.8.0
Delorean==1.0.0
Django==3.0.6
djangorestframework==3.11.0
Faker==0.9.1
humanize==2.4.0
mixer==6.1.3
names==0.3.0
python-dateutil==2.8.1
pytz==2020.1
six==1.15.0
sqlparse==0.3.1
text-unidecode==1.2
tzlocal==2.1



The dependencies are listed in requirements.txt file in the root directory. You can run command in the terminal

pip install -r requirements.txt to add all the modules to your enviroment.


------
CUSTOM MANAGEMENT COMMAND

This app has a custom management command called "insertdummydata", which creates 10 random rows in the database. Each time this command is executed it 
comand is executed, it adds 10 sample values to database.

----
DJANGO REST API

This root address(http://themayurjha.pythonanywhere.com/) of this application is A GET request which returns a JSON Response of the sample values in the database. This is implemented using django rest api.

NOTE: There is no post request implemented in this application and it doesn't have any other pages except http://themayurjha.pythonanywhere.com/


---
CONTRIBUTORS:
Mayur Jha <kumarmayur541@gmail.com>
