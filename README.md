# UOCIS322 - Project 6 #

Project: An ACP Brevet Randonneurs control brevets calculator implemented with Flask, Ajax, MongoDB, and a RESTful API.

Author: Avi Lance

Contact: alance@uoregon.edu

# ACP Brevet Calculator Database Interaction #

This webpage allows you to make requests to the API allowing you to access data from the MongoDB database with different formatting options.

# ACP Brevet Times Users #

When you click the "submit" button it will check to see if the entered data is appropiate, if it is it will enter your data into the database. If it is not appropiate, it will not interact with the database and display an error message.

If you click the "display" button it will display the last submit's stored data assuming it was successful.

# ACP Brevet Times Calculation #

If the Control Distance is greater than 120% of the Brevet Distance, it will return the given starting date with no change in the open and close time column.

If the Control Distance is greater than the Brevet Distance's i.e. (200, 300, 400, 600, 1000) and within 120% of the Brevet Distance, it will return the same starting and closing time you would have if you had a control distance equal to that competitions Brevet Distance.

If the Control Distance is negative, it will return the given starting date with no change in the open and close time column.

If the Control Distance is equal to 0, then the opening time will remain unchanged, while the closing time will be 1 hour past the starting time.

If the Control Distance is less than 60 and greater than 0, the closing time will use 20 km/hr with an additional hour added ontop of the calculation. 

If the Control Distance is equal to the Brevet Distance, the speed will be calculated based on the lower Control's speed.
