import os
import json

MY_DATABASE = None

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def ReadFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)

def CheckFile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            data[0].update(ReadFile())
    else: 
        if(len(param)):
            NewFile(data[0])

def AddData(origin): 
    with open(MY_DATABASE,"w") as rwf:
        json.dump(origin,rwf,indent=4)