- install python 3.7
- install pip (https://pip.pypa.io/en/stable/installing/)
		curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
		python get-pip.py
- test pip in python directory:
	cd C:\Users\adamp\AppData\Local\Programs\Python\Python37-32\Scripts
	pip freeze
- install python.net 
	- download https://ci.appveyor.com/project/pythonnet/pythonnet/branch/master/job/aqi7eyx1j0gcxcs0/artifacts
	- setup.py build
	- setup.py install
- write code
	- reference the Scia.OpenAPI.dll
			clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\Scia.OpenAPI.dll")