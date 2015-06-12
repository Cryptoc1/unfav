# unfav
### What?
Removes all of favorites by the authenticated user.

### Why?
So that josh will think I'm cool

### How?
Run **install.sh**

    $ ./install.sh
  
It will install all dependencies, then read instructions.md. Finally:

    $ ./unfav.py <consumer_key> <consumer_secret>
    
Please note, *This willl most likely cause a rate limit for your client*.

### Dependencies
* python-twitter
* oauth
