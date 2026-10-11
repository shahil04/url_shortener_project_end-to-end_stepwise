### 1 Local run setups
a. install python and requirements.txt
---

- option 1 -->  use your mysql local server form your system 

then run --
b. python app.py

###  option 2. run without sqlsetups 
- use sqllite
- run 
- python appsqllite.py

---------------------
### host in EC2 
1. config the RDS or SQLLITE 
one of then run
- rds config the app.py and then run --> db_create.py
- for sqllite run the(without rds) --> python appsqllite.py
- or for EC2 Config the port inbound ,3306 and 5000 in ec2 

2. then open  the local host 127.0.0.0:5000 


3. Manually do all steps  in EC2 CMD 
1.os--> ubuntu update 
sudo apt update
sudo apt upgrade

2.--> git latest-code push main 
git clone https://github.com/shahil04/url_shortener_project_end-to-end_stepwise.git
cd url_shortener_project_end-to-end_stepwise

--> install python 
sudo apt install python3 python3-pip python3-venv

--> also create venv
# Create the environment
python3 -m venv venv

# Activate it (your prompt will show '(venv)')
source venv/bin/activate

3. --> depenecies install --> python
pip3 install -r requirements.txt --break-system-packages

ec2--> inboud rule 3306 activate also add port tcp 5000

--> run python file
python app.py

public ip --> http://98.85.251.65:5000/

-------------------------------------------------------------------------------------
### Add Github ACtion for CI(continous Integrations)
```
name: Demo CI Pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
   demo-build-and-test:
    runs-on: ubuntu-latest

    steps:
    # Step 1: Pull down the source code from your repository
    - name: Checkout Code
      uses: actions/checkout@v4

    # Step 2: Initialize a clean Python environment
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'
        cache: 'pip' # Automatically caches dependencies to speed up future runs

    # Step 3: Install all packages listed in your requirements text
    - name: Install Project Dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

    # Step 4: Perform a test compile check to catch syntax errors immediately
    - name: Compile and Verify Code
      run: |
        python -m py_compile appsqllite.py app.py

```
