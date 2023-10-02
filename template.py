import os, sys
from pathlib import Path 
import logging

while True:
    project_name = input("Enter your Project Name: ")
    if project_name !="":
        break 

#src/__init__.py
#src/compontes/__init__.py 
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components__init__.py",
    f"{project_name}/config__init__.py",
    f"{project_name}/constants__init__.py",
    f"{project_name}/entity__init__.py",
    f"{project_name}/exception__init__.py",
    f"{project_name}/logger__init__.py",
    f"{project_name}/pipeline__init__.py",
    f"{project_name}/utils__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]


for filepth in list_of_files:
    filepth = Path(filepth)
    filedir, filename = os.path.split(filepth)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepth)) or (os.path. getsize(filepth) == 0 ):
        with open(filepth, "w") as f:
            pass

    else:
        logging.info("file is already present at : {filepath}")


