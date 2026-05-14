import socket
import json
import argparse #https://www.geeksforgeeks.org/python/python-how-to-parse-command-line-options/
import ssl # python tls support

def parse_args():
    '''
    Parses arguments into the command line
    Parameters:
        None
    Returns:
        args: The parsed arguments object containing hostname, username, port and tls flag
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int)
    parser.add_argument('-s', action='store_true')
    parser.add_argument('hostname')
    parser.add_argument('username')

    return parser.parse_args()

def get_port(args):
    '''
    Determines the port to connect to based on the arguments
    Parameters:
        args: the parsed arguments object
    Returns:
        port: the port to connect to
    '''
    if args.port:
        return args.port
    elif args.s:
        return 27994
    else:
        return 27993

def connect_socket(hostname, port, use_tls):
    '''
    Creates a socket and connects to the server
    Parameters:
        hostname: Server hostname to connect to
        port: Port number on server
        use_tls: TLS flag
    Returns
        s: The socket
    '''
    # Inet streaming socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))

    # https://docs.python.org/3/library/ssl.html for TLS socket :(
    if use_tls:
        context = ssl.create_default_context()
        s = context.wrap_socket(s, server_hostname = hostname)

    return s

def send_message(s, obj):
    '''
    Sends a JSON formatted message to server
    Parameters:
        s: Socket connected to server
        obj: Dictionary to send as message
    Returns:
        Nothing
    '''
    # https://www.geeksforgeeks.org/python/python-convert-dictionary-object-into-string/ json formatted string
    s.sendall((json.dumps(obj) + '\n').encode())

def recv_message(s):
    '''
    Recieves a message from the server
    Parameters:
        s: Socket connected to server
    Returns:
        response: JSON response as a dictonary
    '''
    buf = b''
    while not buf.endswith(b'\n'):
        buf += s.recv(4096)
    return json.loads(buf.decode())

def load_words():
    '''
    Loads the word list from wordlist.txt.
    Parameters:
        None
    Returns:
        words: A list of valid guess words
    '''
    # https://www.geeksforgeeks.org/python/read-a-file-line-by-line-in-python/
    with open('wordlist.txt') as f:
        return [line.strip() for line in f]

def filter_words(words, word, marks):
    '''
    Filters the word list based on marks returned from the server.
    Parameters:
        words: The current list of candidate words
        word: The word that was guessed
        marks: The list of marks returned by the server for that guess
    Returns:
        words: The filtered list of candidate words
    '''
    for index in range(len(word)):
        char = word[index]
        mark = marks[index]
        if mark == 2:
            words = [w for w in words if w[index] == char]
        elif mark == 0:
            if char not in [word[j] for j in range(len(word)) if marks[j] in (1, 2)]:
                words = [w for w in words if char not in w]
    return words

def main():
    args = parse_args()
    port = get_port(args)
    s = connect_socket(args.hostname, port, args.s)

    send_message(s, {"type": "hello", "northeastern_username": "jea.d"})
    response = recv_message(s)
    my_id = response["id"]

    words = load_words()

    while True:
        if not words:
            print("word list empty")
            s.close()
            break
        
        guess = words[0]
        send_message(s, {"type": "guess", "id": my_id, "word": guess})
        response = recv_message(s)

        if response["type"] == "bye":
            print(response["flag"])
            break
        elif response["type"] == "retry":
            last_guess = response["guesses"][-1]
            word, marks = last_guess["word"], last_guess["marks"]
            words = filter_words(words, word, marks)

    s.close()

main()