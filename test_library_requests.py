# ModuleNotFoundError: No module named 'requests'

# First, execute this script in command line (CLI)
# % python3 test_library_requests.py

import requests
print(requests.__version__)

# Case I : the library is not install, correct in CLI
# % pip install --upgrade pip
# % pip install requests  

# Case II : no error in CLI but error in IDE
# this is an software configuration issue
# Brackets : menu Edit | Edit Builder >  "name": "Python",
import sys
print(sys.executable)
# returns something like /Library/Frameworks ... /python3
# adjust cmd value accordingly 
# restart