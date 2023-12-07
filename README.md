#datatransformation

This README provides information about the data transformation process implemented in this project. Data transformation involves converting raw data into a format that is suitable for analysis, reporting, or other downstream processes. This document aims to guide users and collaborators on how to understand, use, and contribute to the data transformation process.

prerequisite:
*). install anaconda and set a virtual environment. mahi_venv (installed at below path C:\Users\mahib\anaconda3\envs\mahi_venv\)
*). set the interpreter in Pycharm as andaconda virtual environment 
*). install ubuntu 
------------------------------------------------
if you want to install any unix command then please run below command
sudo apt-get update
sudo apt-get install dos2unix

------------------------------------------------
how to run the shell script from pycharm edit configuration 
In File-->Settings-->Tools-->Terminal, change the shell path from cmd.exe to bash.exe.

*). open ubuntu terminal 
cd /mnt/d/ to go to windows d drive 

run shell script:->

clear; bash runTransformation.sh -e dev -n mortgage
Note: if you're running from shell script then you don't need to set PYTHONPATH in edit configuration. however you can directly set at .sh file
export PYTHONPATH=$PATH:/d/gitrepository/datatransformation/
python '/d/gitrepository/datatransformation/scripts/runTransformation.py' --modelname ${modelname} --businessdate ${date} --mode ${env}

-------------------------------

*). directly run from wrapper python script runTransformation.py as below. in that case you need to define the PYTHONPATH in edit configuration. 
Edit configuration 
set this environment variable in Edit Configuration
PYTHONUNBUFFERED=1;PYTHONPATH=D:\gitrepository\datatransformation
