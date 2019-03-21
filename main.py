print("Hello world")

import uuid
import sys
import clr
clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\Scia.OpenAPI.dll")
clr.AddReference(r"C:\SCIA\GIT\SEN\A\Bin\release32\EnvESA80.dll")



from SCIA.OpenAPI import *
from SCIA.OpenAPI.StructureModelDefinition import *
from EnvESA80 import *
from System import Guid

env = Environment(r"C:\SCIA\GIT\SEN\A\Bin\release32", r".\Temp")
print("Environment set")


EnumGuiMode = TEnvESAApp_ShowWindow
env.RunSCIAEngineer(EnumGuiMode.eEPShowWindowShow)
print("SEn started")



proj = env.OpenProject(r"c:\SCIA\GIThub\SciaOpenAPI_example_parabolic\res\template.esa")
print("project opened")

steelmatid = Guid.NewGuid()
mat = Material(steelmatid, r"steel S235", 1, r"S 235")
proj.Model.CreateMaterial(mat)

proj.Model.RefreshModel_ToSCIAEngineer()

print("Press any key to continue:")
sys.stdin.readline()

env.CloseAllProjects(TEnvESAApp_SaveChanges.eEPSaveChangesNo)

