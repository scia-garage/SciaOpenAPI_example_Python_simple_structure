Prepare the environment:
* install Scia Engineer
	* .NET FW is included in setup
	* start Scia ENgineer to test it
* install python 3.7 
	* install using setup https://www.python.org/downloads/release/python-370/ (check the "add Python to path" checkbox)
	* copy the .\res\python.exe.config and pythonw.exe.config to the directory where the python.exe and pythonw.exe are (e.g. run cmd "where python.exe")
	* setup should also install the PIP package manager for Python
	* test python by running cmd python
	* test pip by running cmd pip
	* upgrade PIP by running "python -m pip install --upgrade pip"
	* install the WHEEL package by running "pip install wheel"

* install python.net https://github.com/pythonnet/pythonnet/wiki/Installation
	* preffered way
		* via PIP from local .whl file 
			* get .whl file
				* from https://ci.appveyor.com
					* go to https://ci.appveyor.com/project/pythonnet/pythonnet 
					* select some stable revision
					* select correct PYTHON_VERSION (e.g. 3.7) and Platform (e.g. x64) - click it
					* go to Artifacts and download respective .whl file					
				* from https://github.com/scia-garage/SciaOpenAPI_example_parabolic/tree/master/res
					* go to website and download .whl file fitting your PYTHON version and PLATFORM
			* cmd pip install .\<path.to.whl.file>.whl
			
	* alternatives
		* prerequisities
			* you need mt.exe in PATH variable
				* e.g. install MS Visual Studio https://developer.microsoft.com/en-us/windows/downloads
				* e.g. install windows sdk https://developer.microsoft.com/cs-cz/windows/downloads/windows-10-sdk
				* e.g. https://github.com/eladkarako/mt
		* ways how to install
			* via PIP from distant repo
				* cmd pip install pythonnet
			* via building released sources
				* download sources https://ci.appveyor.com/project/pythonnet/pythonnet
					* select some stable revision
					* select correct version of python and platform
				* extract binaries to new directory in PTYHON home directory (cmd where python)
				* cd to that directory
				* run python setup.py build
				* run python setup.py install
			* from pythoniron git repo
				* install git https://git-scm.com/download/win
				* pip install git+https://github.com/pythonnet/pythonnet.git

Write your code:
* reference the Scia.OpenAPI.dll
	```
	clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\Scia.OpenAPI.dll")
	clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\EnvESA80.dll")
	```
* import SCIA.OpenAPI classes
	```
	from SCIA.OpenAPI import *
	from SCIA.OpenAPI.StructureModelDefinition import *
	from EnvESA80 import *
	```
