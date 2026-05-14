High Level approach to Socket Wordle Project:
1. Create a socket
2. Connect socket to proj1.4700.network port 27993
3. Send hello message and recieve start and id
4. Recieve JSON formatted data from server
5. While retry message type recieved, guess word from the word list
6. If bye message is recieved print flag
7. If error is ever recieved something wrong with username :(

Guessing strategy for first attempt is just go to through the first word, see which letters are in correct spaces. Remove all other letters that cannot be in the word, and just retry again.

Issues with client itself. Since there was apparantly Windows CRLF endings (DONT ASK ME WHAT THAT IS), even though I was using codespaces, linux was running /bin/bash^M instead of just /bin/bash

sed -i 's/\r$//' client