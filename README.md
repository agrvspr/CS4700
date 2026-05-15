High Level approach to Socket Wordle Project:
1. Create a socket
2. Connect socket to proj1.4700.network port 27993
3. Send hello message and recieve start and id
4. Recieve JSON formatted data from server
5. While retry message type recieved, guess word from the word list
6. If bye message is recieved print flag

Guessing strategy for first attempt is just go to through the first word, see which letters are in correct spaces. Filter all remaining words based on those results

Issues with windows being BAD. had to switch to linux line or something, but dos2unix wasnt working, so I had to lookup a different way and sed -i 's/\r$//' client

For code development support, I guess we can include the small talk before the quiz makeup where I basically outlined what I wanted to do and asked about whether to do this in C or python

Thank you whoever made those gradescope comments for helping me figure out issues :D

For testing my code, I did not make another test file for tests and stuff. I used print statements within my code at points where either I thought things might go wrong, or at places where gradescope was telling me, "Hey you uh, you missed this"


https://www.geeksforgeeks.org/python/read-a-file-line-by-line-in-python/
https://www.geeksforgeeks.org/python/python-convert-dictionary-object-into-string/ json formatted string
https://docs.python.org/3/library/ssl.html
https://www.geeksforgeeks.org/python/python-how-to-parse-command-line-options/

These 2 were super helpful websites... of course the python documents were helpful. Google was nice enough so that when I typed a How To question, it led me to usually these 2 websites.