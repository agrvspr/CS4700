import socket
import json
import argparse #https://www.geeksforgeeks.org/python/python-how-to-parse-command-line-options/

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int)
parser.add_argument('-s', action='store_true')
parser.add_argument('hostname')
parser.add_argument('username')
args = parser.parse_args()

if args.port:
    port = args.port
elif args.s:
    port = 27994
else:
    port = 27993

# Inet streaming socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to proj1.4700.network
s.connect((args.hostname, port))

# send the server the hello message
hello = {"type": "hello", "northeastern_username": "jea.d"}
 
# https://www.geeksforgeeks.org/python/python-convert-dictionary-object-into-string/ json formatted string
formatted = json.dumps(hello)

s.sendall(formatted.encode() + b'\n')

#save the response
buf = b'' # empty bytes prefixing taught by dad :D
while not buf.endswith(b'\n'):
    buf += s.recv(4096)
response = json.loads(buf.decode())

my_id = response["id"]

# read the wordlist line by line
# https://www.geeksforgeeks.org/python/read-a-file-line-by-line-in-python/
with open('words.txt') as f:
    words = [line.strip() for line in f]

while True:
    guess = words[0] # hopefully becomes new word every iteration based on the filter
    s.sendall((json.dumps({"type":"guess", "id": my_id, "word": guess}) + '\n').encode())

    buf = b''
    while not buf.endswith(b'\n'):
        buf += s.recv(4096)
    response = json.loads(buf.decode())

    if response["type"] == "bye":
        print(response["flag"])
        break
    elif response["type"] == "retry":
        last_guess = response["guesses"][-1] #take the last guess
        word, marks = last_guess["word"], last_guess["marks"]
        for index in range(len(word)):
            char = word[index]
            mark = marks[index]
            if mark == 2:
                words = [w for w in words if w[index] == char] #filter wordlist by correct character
            elif mark == 0:
                words = [w for w in words if char not in w] # get rid of this letter