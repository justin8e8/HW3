HW3: This is our submission for our HW3 Assignment, which will have functionality specified by the assignment

Justin Si
Jon Jones

## Quick Start
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```

The Assignment has the functionality as follows
```
127.0.0.1:5000 will show the entries in basket_a in the dvdrental database
127.0.0.1:5000/api/update_basket_a will update add a 5th entry cherry, if not there already, returns an error otherwise.
127.0.0.1:5000/api/unique will show unique entries of basket A & basket B with no common fruits, will return an error if something goes wrong
```
