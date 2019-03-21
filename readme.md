Prepare the environment:
- install python 3.7
	- setup https://www.python.org/downloads/release/python-370/
	- if not done automatically, add the python.exe location into Path system variable (e.g. C:\Users\...\AppData\Local\Programs\Python\Python37-32\python.exe)
	- place the .\res\python.exe.config and pythonw.exe.config to the directory where the python.exe and pythonw.exe are (e.g. run cmd "where python.exe")
- install python.net 
	- direct install:
		- download https://ci.appveyor.com/project/pythonnet/pythonnet/branch/master/job/aqi7eyx1j0gcxcs0/artifacts
		- setup.py build
		- setup.py install
	- or via PIP:
		- install pip (https://pip.pypa.io/en/stable/installing/)
			- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
			- python get-pip.py
		- test pip in python directory:
			- cmd "cd C:\Users\...\AppData\Local\Programs\Python\Python37-32\Scripts (or where the Python is located)"
			- cmd "pip freeze"
		- install python.net via PIP:
			- cmd "cd C:\Users\...\AppData\Local\Programs\Python\Python37-32\Scripts (or where the Python is located)"
			- cmd "pip install pythonnet""

Write your code:
	- reference the Scia.OpenAPI.dll
			clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\Scia.OpenAPI.dll")
			clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\EnvESA80.dll")
	- import SCIA.OpenAPI classes
			from SCIA.OpenAPI import *
			from SCIA.OpenAPI.StructureModelDefinition import *
			from EnvESA80 import *
