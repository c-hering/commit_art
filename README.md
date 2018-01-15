# commit_art
**Description:**
Simple Python script that automates commits to a repo so as to create pixel art in your commit history.

**Setting what to draw:**
Inside the script there is a 2D array which is has x rows per week, and 7 columns per day. 

Ex. 10 Weeks, 7 days:
 ```
     S M T W T F S
 W0: 0 0 0 0 0 0 0
 W1: 0 0 0 0 0 0 0
 W2: 0 0 0 0 0 0 0
 W3: 0 0 0 0 0 0 0
 W4: 0 0 0 0 0 0 0
 W5: 0 0 0 0 0 0 0
 W6: 0 0 0 0 0 0 0
 W7: 0 0 0 0 0 0 0
 W8: 0 0 0 0 0 0 0
 W9: 0 0 0 0 0 0 0
 
 ```
 
 To tell the program you want to commit on a certain day, you set it's position to a 1.
 Keep in mind that whatever you draw or type will have to be backwards.
 
 Ex. Setting the Thursday of the 3rd week would look like this:
 ```
     S M T W T F S
 W0: 0 0 0 0 0 0 0
 W1: 0 0 0 0 0 0 0
 W2: 0 0 0 0 1 0 0
 W3: 0 0 0 0 0 0 0
 W4: 0 0 0 0 0 0 0
 W5: 0 0 0 0 0 0 0
 W6: 0 0 0 0 0 0 0
 W7: 0 0 0 0 0 0 0
 W8: 0 0 0 0 0 0 0
 W9: 0 0 0 0 0 0 0
 
