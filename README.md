# Work with local database | Basic UI | OOP | DB Browser (SQLite) 



## FILES

* Vehicles_GUI_v2.0.py (here and after - the Program) allows working with the vehicles' database

* Vehicles_python.db (here and after - the DB) contains numeric & text data about vehicles

* the Program and the DB should be saved to one Python package
  
## ABOUT

The locally-stored DB interaction program with basic GUI elements 

## FUNCTIONAL

  * the DB contains information about 3 types of vehicles: cars, planes and ships; each type has specific data fields
  
  * the Program allows interacting with the Database in 3 ways:
  
    ** adding new vehicle to the DB
	
		  *** a user is asked to choose the type of the vehicle he or she wants to add

		  *** the program displays respective data fields and asks user to enter information

		  *** after he or she can save & exit or save & add more vehicles to the database
	  
    ** modifying certain DB data
	
		  *** a user is asked to choose the type of the vehicle he or she wants to edit

		  *** the program asks what parameter to update & new data

		  *** a user can save changes & continue updating or save changes & exit the Program
	  
    ** exporting & saving DB data in the .csv
	
		  *** a user is asked to choose the table he or she wants to be saved to .csv

		  *** the file is prepared & saved within the same Python package

## PRINCIPLES USED

  * interaction between Classes
  * tkinter package for basic GUI
