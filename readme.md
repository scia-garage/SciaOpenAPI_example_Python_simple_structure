# Prepare the environment:
* install Scia Engineer (32/64bit)
	* .NET FW is included in setup
	* start Scia ENgineer to test it
* install python 3.7 
	* choose correct platform (32/64bit) based on the Scia Engineer platform
	* install using setup https://www.python.org/downloads/release/python-370/ (check the "add Python to path" checkbox)
	* copy the .\res\python.exe.config and pythonw.exe.config to the directory where the python.exe and pythonw.exe are (e.g. run cmd "where python.exe")
	* setup should also install the PIP package manager for Python
	* test python by running cmd "python"
	* test pip by running cmd "pip"
	* upgrade PIP by running "python -m pip install --upgrade pip"
	* install the WHEEL package by running "pip install wheel"

* install python.net https://github.com/pythonnet/pythonnet/wiki/Installation
	* preffered way
		* via PIP from local .whl file 
			* get .whl file
				* from https://ci.appveyor.com
					* go to https://ci.appveyor.com/project/pythonnet/pythonnet 
					* select some stable revision
					* select correct PYTHON_VERSION (e.g. 3.7) and Platform (e.g. 32/64bit based on SEn) - click it
					* go to Artifacts and download respective .whl file					
				* from https://github.com/scia-garage/SciaOpenAPI_example_parabolic/tree/master/res
					* go to website and download .whl file fitting your PYTHON version and PLATFORM
			* cmd "pip install .\<path.to.whl.file>.whl"
			
	* alternatives (sometimes tricky)
		* prerequisities
			* you need mt.exe in PATH variable
				* e.g. install MS Visual Studio https://developer.microsoft.com/en-us/windows/downloads
				* e.g. install windows sdk https://developer.microsoft.com/cs-cz/windows/downloads/windows-10-sdk
				* e.g. https://github.com/eladkarako/mt
		* ways how to install
			* via PIP from distant repo
				* cmd "pip install pythonnet"
			* via building from downloaded released sources
				* download sources https://ci.appveyor.com/project/pythonnet/pythonnet
					* select some stable revision
					* select correct version of python and platform (32/64bit based on SEn)
				* extract binaries to new directory
				* cd to that directory
				* run "setup.py build"
				* run "setup.py install"
			* from pythoniron git repo
				* install git from https://git-scm.com/download/win
				* "pip install git+https://github.com/pythonnet/pythonnet.git"

# Write your code:
* reference the Scia.OpenAPI.dll
	```
	clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\Scia.OpenAPI.dll")
	```
* import SCIA.OpenAPI classes
	```
	from SCIA.OpenAPI import *;
	from SCIA.OpenAPI.StructureModelDefinition import *;
	from SCIA.OpenAPI.Results import *;
	from Results64Enums import *;
	```
# Troubleshooting:
* if you get following exception, just register esa libraries
	* run cmd AS ADMINISTRATOR
	* navigate to Scia Engineer directory
	* run "EP_regsvr32 esa.exe"
```
Unhandled Exception: System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
```
