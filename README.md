High Level approach to Socket Wordle Project:
1. Create a socket
2. Connect socket to proj1.4700.network port 27993
3. Send hello message and recieve start and id
4. Recieve JSON formatted data from server
5. While retry message type recieved, guess word from the word list
6. If bye message is recieved print flag
7. If error is ever recieved something wrong with username :(

Guessing strategy for first attempt is just go to through the first word, see which letters are in correct spaces. Remove all other letters that cannot be in the word, and just retry again.

Issues with windows being BAD. had to switch to linux line or something, but dos2unix wasnt working, so I had to lookup a different way and sed -i 's/\r$//' client

For code development support, I guess we can include the small talk before the quiz makeup where I basically outlined what I wanted to do and asked about whether to do this in C or python