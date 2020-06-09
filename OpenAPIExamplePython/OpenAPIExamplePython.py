import uuid
import sys
import clr
import os
from pathlib import Path

sys.path.append(r"C:\Program Files\SCIA\Engineer19.1\OpenAPI_dll")


clr.AddReference(r"C:\Program Files\SCIA\Engineer19.1\OpenAPI_dll\SCIA.OpenAPI.dll")

from SCIA.OpenAPI import *
from SCIA.OpenAPI.StructureModelDefinition import *
from SCIA.OpenAPI.Results import *
from Results64Enums import *
from SCIA.OpenAPI.OpenAPIEnums import *
from SCIA.OpenAPI.Utils import *
from System import Guid

env = Environment(r"C:\Program Files\SCIA\Engineer19.1", r"c:\Temp\OpenAPITemp","1.0.0.0")


EnumGuiMode = Environment.GuiMode.ShowWindowShow
env.RunSCIAEngineer(Environment.GuiMode.ShowWindowShow)

fileGetter = SciaFileGetter()
EsaFile = fileGetter.PrepareBasicEmptyFile(r"C:/TEMP/") #path where the template file "template.esa" is created
#if (!File.Exists(EsaFile))
#                throw new InvalidOperationException($"File from manifest resource is not created ! Temp: {env.AppTempPath}")
# }

#proj = env.OpenProject(r"C:\WORK\SourceCodes\SciaOpenAPI_example_Python_simple_structure\res\OpenAPIEmptyProject.esa")# empty SCIA Engineer project
proj = env.OpenProject(EsaFile)# empty SCIA Engineer project



steelmatid = ApiGuid.NewGuid()
steelmatGrade = "S 235"
steelmat = Material(steelmatid, r"steel S235", 1,steelmatGrade)
proj.Model.CreateMaterial(steelmat)
comatid = ApiGuid.NewGuid()
conmatGrade = "C20/25"
conmat = Material(comatid, "conc", 0,conmatGrade)
proj.Model.CreateMaterial(conmat)

css_steel = ApiGuid.NewGuid()
steelCss = "HEA260"
cssHEA260 = CrossSectionManufactured(css_steel, "steel.HEA", steelmatid,steelCss, 1, 0)
proj.Model.CreateCrossSection(cssHEA260)

a = 5.0
b = 6.0
c = 3.0
n1 = ApiGuid.NewGuid()
n2 = ApiGuid.NewGuid()
n3 = ApiGuid.NewGuid()
n4 = ApiGuid.NewGuid()
n5 = ApiGuid.NewGuid()
n6 = ApiGuid.NewGuid()
n7 = ApiGuid.NewGuid()
n8 = ApiGuid.NewGuid()
proj.Model.CreateNode(StructNode(n1, "n1", 0.0, 0.0, 0.0))
proj.Model.CreateNode(StructNode(n2, "n2", float(a), 0.0, 0.0))
proj.Model.CreateNode(StructNode(n3, "n3", float(a), float(b), 0.0))
proj.Model.CreateNode(StructNode(n4, "n4", 0.0, float(b), 0.0))
proj.Model.CreateNode(StructNode(n5, "n5", 0.0, 0.0, float(c)))
proj.Model.CreateNode(StructNode(n6, "n6", float(a), 0.0, float(c)))
proj.Model.CreateNode(StructNode(n7, "n7", float(a), float(b), float(c)))
proj.Model.CreateNode(StructNode(n8, "n8", 0.0, float(b), float(c)))

b1 = ApiGuid.NewGuid()
b2 = ApiGuid.NewGuid()
b3 = ApiGuid.NewGuid()
b4 = ApiGuid.NewGuid()
proj.Model.CreateBeam(Beam(b1, "b1", css_steel, ApiGuidArr([n1, n5])))
proj.Model.CreateBeam(Beam(b2, "b2", css_steel, ApiGuidArr([n2, n6])))
proj.Model.CreateBeam(Beam(b3, "b3", css_steel, ApiGuidArr([n3, n7])))
proj.Model.CreateBeam(Beam(b4, "b4", css_steel, ApiGuidArr([n4, n8])))

Su1 = PointSupport(ApiGuid.NewGuid(), "Su1", n1)
Su1.ConstraintRx = eConstraintType.Free
Su1.ConstraintRy = eConstraintType.Free
Su1.ConstraintRz = eConstraintType.Free
proj.Model.CreatePointSupport(Su1)
proj.Model.CreatePointSupport(PointSupport(ApiGuid.NewGuid(), "Su2", n2))
proj.Model.CreatePointSupport(PointSupport(ApiGuid.NewGuid(), "Su3", n3))
proj.Model.CreatePointSupport(PointSupport(ApiGuid.NewGuid(), "Su4", n4))


s1 = ApiGuid.NewGuid()
nodes = ApiGuidArr([n5, n6, n7, n8])
thickness = 0.30
proj.Model.CreateSlab(Slab(s1, "s1", 0, comatid, float(thickness), nodes))


lg1 = ApiGuid.NewGuid()
proj.Model.CreateLoadGroup(LoadGroup(lg1, "lg1", 0))

lc1 = ApiGuid.NewGuid()
proj.Model.CreateLoadCase(LoadCase(lc1, "lc1", 0, lg1, 1))
CI1 = CombinationItem(lc1, 1.5)
combinationItems = []
combinationItems.append(CI1)
C1 = Combination(ApiGuid.NewGuid(), "C1", combinationItems)
C1.Category = eLoadCaseCombinationCategory.AccordingNationalStandard
C1.NationalStandard = eLoadCaseCombinationStandard.EnUlsSetC
proj.Model.CreateCombination(C1)

sf1 = ApiGuid.NewGuid()
loadvalue = -12500
proj.Model.CreateSurfaceLoad(SurfaceLoad(sf1, "sf1",float(loadvalue), lc1, s1, 2))


lineSupport = LineSupport(ApiGuid.NewGuid(), "lineSupport", b1)
lineSupport.Member = b1
lineSupport.ConstraintRx = eConstraintType.Free
lineSupport.ConstraintRy = eConstraintType.Free
lineSupport.ConstraintRz = eConstraintType.Free
proj.Model.CreateLineSupport(lineSupport)

lineLoad = LineLoadOnBeam(ApiGuid.NewGuid(), "lineLoad")
lineLoad.Member = b1
lineLoad.LoadCase = lc1
lineLoad.Value1 = -12500
lineLoad.Value2 = -12500
lineLoad.Direction = eDirection.X
proj.Model.CreateLineLoad(lineLoad)

proj.Model.RefreshModel_ToSCIAEngineer()

print("My model sent to SEn")


proj.RunCalculation()
print("My model calculate")


rapi = proj.Model.InitializeResultsAPI()
if rapi !=  None :
    
    IntFor1Db1 = Result()
    keyIntFor1Db1 = ResultKey()

    keyIntFor1Db1.CaseType = eDsElementType.eDsElementType_LoadCase
    keyIntFor1Db1.CaseId = lc1
    keyIntFor1Db1.EntityType = eDsElementType.eDsElementType_Beam
    keyIntFor1Db1.EntityName = "b1"
    keyIntFor1Db1.Dimension = eDimension.eDim_1D
    keyIntFor1Db1.ResultType = eResultType.eFemBeamInnerForces
    keyIntFor1Db1.CoordSystem = eCoordSystem.eCoordSys_Local
    IntFor1Db1 = rapi.LoadResult(keyIntFor1Db1)

    print(IntFor1Db1.GetTextOutput())
    #combination
    #Create container for 1D results
    IntFor1Db1Combi = Result()
    #Results key for internal forces on beam 1
    keyIntFor1Db1Combi = ResultKey()
    keyIntFor1Db1Combi.EntityType = eDsElementType.eDsElementType_Beam
    keyIntFor1Db1Combi.EntityName = "b1"
    keyIntFor1Db1Combi.CaseType = eDsElementType.eDsElementType_Combination
    keyIntFor1Db1Combi.CaseId = C1.Id
    keyIntFor1Db1Combi.Dimension = eDimension.eDim_1D
    keyIntFor1Db1Combi.ResultType = eResultType.eFemBeamInnerForces
    keyIntFor1Db1Combi.CoordSystem = eCoordSystem.eCoordSys_Local
    #Load 1D results based on results key
    IntFor1Db1Combi = rapi.LoadResult(keyIntFor1Db1Combi)

    Def2Ds1 = Result()
    keyDef2Ds1 = ResultKey()
    keyDef2Ds1.CaseType = eDsElementType.eDsElementType_LoadCase
    keyDef2Ds1.CaseId = lc1
    keyDef2Ds1.EntityType = eDsElementType.eDsElementType_Slab
    keyDef2Ds1.EntityName = "s1"
    keyDef2Ds1.Dimension = eDimension.eDim_2D
    keyDef2Ds1.ResultType = eResultType.eFemDeformations
    keyDef2Ds1.CoordSystem = eCoordSystem.eCoordSys_Local

    Def2Ds1 = rapi.LoadResult(keyDef2Ds1)
    print(Def2Ds1.GetTextOutput())

    maxvalue = 0.0
    pivot = maxvalue
    elemcount = Def2Ds1.GetMeshElementCount()
    for i in range(0, elemcount):
        pivot = Def2Ds1.GetValue(2, i)
        if (abs(pivot) > abs(maxvalue)):
            maxvalue = pivot

print("Maximum deformation on slab:")
print(maxvalue)
print("Press any key to continue:")
sys.stdin.readline()
#rapi.Dispose()
proj.CloseProject(SaveMode.SaveChangesNo)

env.Dispose()

