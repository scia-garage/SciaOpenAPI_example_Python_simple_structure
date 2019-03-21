Prepare the environment:
- install python 3.7
	- setup https://www.python.org/downloads/release/python-370/
	- if not done automatically, add the python.exe location into Path system variable (e.g. C:\Users\...\AppData\Local\Programs\Python\Python37-32\python.exe)
	- place the .\res\python.exe.config to the directory where the python.exe is (e.g. run cmd "where python.exe")
- install python.net 
	- download https://ci.appveyor.com/project/pythonnet/pythonnet/branch/master/job/aqi7eyx1j0gcxcs0/artifacts
	- setup.py build
	- setup.py install

Write your code:
	- reference the Scia.OpenAPI.dll
			clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\Scia.OpenAPI.dll")
			clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\EnvESA80.dll")
