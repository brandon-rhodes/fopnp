#!/usr/bin/expect

eval spawn ssh -p 2201 brandon@localhost curl -I http://www.example.com
#use correct prompt
set prompt ":|#|\\\$"
interact -o -nobuffer -re $prompt return
send "abc123\r"
interact

