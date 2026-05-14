import socket
import json
import argparse #https://www.geeksforgeeks.org/python/python-how-to-parse-command-line-options/

parser = argparse.ArgumentParser
parser.add_argument('-p', '--port', type=int)

if args.port:
    port = args.port
elif args.s:
    port = 27994
else:
    port = 27993

# Inet streaming socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to proj1.4700.network
s.connect((args.hostname, 27993))
