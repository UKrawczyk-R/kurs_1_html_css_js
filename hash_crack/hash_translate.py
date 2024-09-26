#!/usr/bin/python3
import hashlib

target_hash = "2d58b0ac72f929ca9ad3238ade9eab69" # paste your hash


wordlist = open("./word_list.txt")
passwords = wordlist.readlines()

for password in passwords:
    if password[0] == "#":
        continue
    password = password.strip() # remove new line character /n
    hash = hashlib.md5(password.encode("UTF-8")).hexdigest() #convert to bytes create hash obiect and hash the hash obiect
    if hash == target_hash:
        print("found passowrd: " + password)
