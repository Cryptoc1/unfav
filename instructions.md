# Installation Instructions for Hiroshima 

### Where to Start
The first thing that should be done is to run *install.py*. This script moves and setup some stuff for easier authentication.

### What next?

Twitter: Setting up Twitter client is similar to Instgrams process.

1. Go to [Twitter App Manager](https://apps.twitter.com/)

2. Click on __*Create New App*__

3. Name it *\<your screen-name\>*-unfav

4. Under description, enter whatever.

5. Under the __*Callback URL*__ enter *http://127.0.0.1/unfav/auth/* (using localhost will NOT work here)

6. Once created, go to the settings page and enter the *Keys and Access Tokens* tab

7. Ensure that the __*Acces Level*__ is set to *Read and Write*

8. The client tokens (*Consumer Key* and *Consumer Secret*) can be used as arguments (**./unfav.py <consumer_key> <consumer_secret>**), or you can replace the variable values in the code.

9. You should be set.
