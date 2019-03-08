print("Hello world")

import clr
clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\Scia.OpenAPI.dll")
clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\EnvESA80.dll")

from SCIA.OpenAPI import Environment
env = Environment(r"C:\SCIA\GIT\SEN\A\Bin\release32", r".\Temp")
print("Environment set")

from EnvESA80 import TEnvESAApp_ShowWindow
enum = TEnvESAApp_ShowWindow
env.RunSCIAEngineer(enum.eEPShowWindowShow)
print("SEn started")
