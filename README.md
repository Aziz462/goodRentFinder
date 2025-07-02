# goodRentFinder
a linear regression model to find flats for renting with most optimal prices 
# how to use
You need to run the parseCian.py to get relevant data from Cian.ru (you can specify the number of rooms you want to find)
That will create a .csv file. You need to copy the name of that file and put it in the model1.py file in the csvPath variable.
Then you run the model1.py and you should get the results for relevant data.

For this project I used `cianparser` from https://github.com/lenarsaitov/cianparser
**NOTE:** parseCian.py might have issues parsing Cian because of Cian's CAPTCHA, so after a while it might stop working, but it should work for sometime before being caught.


# to-do
* add a CAPTCHA-resolver
* add multiple rooms as a parameter
* add an option to find flats for buying, not renting
* add basic UI
