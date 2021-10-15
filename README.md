# CTF Completion Marker
A script that automates renaming directories after obtaining the corresponding flag.

# Summary
I created this script to automate the repetitive process of renaming directories after completing HackTheBox machines, as checking and renaming directories by hand was boring and taking precious time.

# Features
1. **Renaming directories**: the script appends a string (default '_completed') to a directory name if a flag file (default 'root.txt') is found inside.

# Requirements
**python3**

# Examples of use
```
./mark_completed.py explorer
./mark_completed.py admirer -f flag.txt
```

If you want to be able to use it from anywhere on the system, link it to */usr/local/bin* using:
```
sudo ln -s $(pwd)/mark_completed.py /usr/local/bin/
```
