import uuid;
import sys;
import clr;
import os;
from pathlib import Path;


clr.AddReference(r"c:\Program Files (x86)\SCIA\Engineer19.0\Scia.OpenAPI.dll");

from SCIA.OpenAPI import *;
from SCIA.OpenAPI.StructureModelDefinition import *;
from SCIA.OpenAPI.Results import *;
from Results64Enums import *;
from System import Guid

env = Environment(r"c:\Program Files (x86)\SCIA\Engineer19.0", r".\Temp","1.0.0.0");
print("Environment set");

EnumGuiMode = Environment.GuiMode
env.RunSCIAEngineer(EnumGuiMode.ShowWindowShow)
print("SEn started")

scriptDir = os.getcwd();
templatePath = Path(scriptDir) / Path(r"..\res\OpenAPIEmptyProject.esa")

if not templatePath.exists():

    print("Oops, file doesn't exist!")

proj = env.OpenProject(str(templatePath));

print("project opened");



steelmatid = ApiGuid.NewGuid();
steelmatGrade = input('Steel grade: ');
steelmat = Material(steelmatid, r"steel S235", 1,steelmatGrade);
proj.Model.CreateMaterial(steelmat);
comatid = ApiGuid.NewGuid();
conmatGrade = input('Concrete grade: ');
conmat = Material(comatid, "conc", 0,conmatGrade);
proj.Model.CreateMaterial(conmat);
css_steel = ApiGuid.NewGuid();
steelCss = input('Steel Css: ')
cssHEA260 = CrossSectionManufactured(css_steel, "steel.HEA", steelmatid,steelCss, 1, 0);
proj.Model.CreateCrossSection(cssHEA260);
a = input('Input a: ');
b = input('Input b: ');
c = input('Input c: ');
n1 = ApiGuid.NewGuid();
n2 = ApiGuid.NewGuid();
n3 = ApiGuid.NewGuid();
n4 = ApiGuid.NewGuid();
n5 = ApiGuid.NewGuid();
n6 = ApiGuid.NewGuid();
n7 = ApiGuid.NewGuid();
n8 = ApiGuid.NewGuid();
proj.Model.CreateNode(StructNode(n1, "n1", 0.0, 0.0, 0.0));
proj.Model.CreateNode(StructNode(n2, "n2", float(a), 0.0, 0.0));
proj.Model.CreateNode(StructNode(n3, "n3", float(a), float(b), 0.0));
proj.Model.CreateNode(StructNode(n4, "n4", 0.0, float(b), 0.0));
proj.Model.CreateNode(StructNode(n5, "n5", 0.0, 0.0, float(c)));
proj.Model.CreateNode(StructNode(n6, "n6", float(a), 0.0, float(c)));
proj.Model.CreateNode(StructNode(n7, "n7", float(a), float(b), float(c)));
proj.Model.CreateNode(StructNode(n8, "n8", 0.0, float(b), float(c)));

b1 = ApiGuid.NewGuid();
b2 = ApiGuid.NewGuid();
b3 = ApiGuid.NewGuid();
b4 = ApiGuid.NewGuid();
proj.Model.CreateBeam(Beam(b1, "b1", css_steel, ApiGuidArr( [ n1, n5 ])));
proj.Model.CreateBeam(Beam(b2, "b2", css_steel, ApiGuidArr( [ n2, n6 ])));
proj.Model.CreateBeam(Beam(b3, "b3", css_steel, ApiGuidArr( [ n3, n7 ])));
proj.Model.CreateBeam(Beam(b4, "b4", css_steel, ApiGuidArr( [ n4, n8 ])));

proj.Model.CreatePointSupport(PointSupport(ApiGuid.NewGuid(), "Su1", n1));
proj.Model.CreatePointSupport(PointSupport(ApiGuid.NewGuid(), "Su2", n2));
proj.Model.CreatePointSupport(PointSupport(ApiGuid.NewGuid(), "Su3", n3));
proj.Model.CreatePointSupport(PointSupport(ApiGuid.NewGuid(), "Su4", n4));


s1 = ApiGuid.NewGuid();
nodes = ApiGuidArr( [ n5, n6, n7, n8 ]);
thickness = input('Slab thickness: ');
proj.Model.CreateSlab(Slab(s1, "s1", 0, comatid, float(thickness), nodes));

lg1 = ApiGuid.NewGuid();
proj.Model.CreateLoadGroup(LoadGroup(lg1, "lg1", 0));

lc1 = ApiGuid.NewGuid();
proj.Model.CreateLoadCase(LoadCase(lc1, "lc1", 0, lg1, 1));

sf1 = ApiGuid.NewGuid();
loadvalue = input('Value of surface load: ');
proj.Model.CreateSurfaceLoad(SurfaceLoad(sf1, "sf1",float(loadvalue), lc1, s1, 2));



proj.Model.RefreshModel_ToSCIAEngineer()

print("My model sent to SEn");


proj.RunCalculation();
print("My model calculate");


#ee = CXEP_SimpleResultsAPI();
#rapi = ResultsAPI(ee,proj.Model);
#proj.Model.InitializeResultsAPI(rapi);

rapi = proj.Model.InitializeResultsAPI();

IntFor1Db1 = Result();
keyIntFor1Db1 = ResultKey();

keyIntFor1Db1.CaseType = eDsElementType.eDsElementType_LoadCase;
keyIntFor1Db1.CaseId = lc1;
keyIntFor1Db1.EntityType = eDsElementType.eDsElementType_Beam;
keyIntFor1Db1.EntityName = "b1";
keyIntFor1Db1.Dimension = eDimension.eDim_1D;
keyIntFor1Db1.ResultType = eResultType.eFemBeamInnerForces;
keyIntFor1Db1.CoordSystem = eCoordSystem.eCoordSys_Local;

print(IntFor1Db1.GetTextOutput());






Def2Ds1 = Result();
keyDef2Ds1 = ResultKey();
keyDef2Ds1.CaseType = eDsElementType.eDsElementType_LoadCase;
keyDef2Ds1.CaseId = lc1;
keyDef2Ds1.EntityType = eDsElementType.eDsElementType_Slab;
keyDef2Ds1.EntityName = "s1";
keyDef2Ds1.Dimension = eDimension.eDim_2D;
keyDef2Ds1.ResultType = eResultType.eFemDeformations;
keyDef2Ds1.CoordSystem = eCoordSystem.eCoordSys_Local;

Def2Ds1 = rapi.LoadResult(keyDef2Ds1);
print(Def2Ds1.GetTextOutput());

maxvalue = 0.0;
pivot = maxvalue;
elemcount = Def2Ds1.GetMeshElementCount()
for i in range (0, elemcount):
    pivot = Def2Ds1.GetValue(2, i);
    if (abs(pivot) > abs(maxvalue)):
        maxvalue = pivot;

print("Maximum deformation on slab:");
print(maxvalue);
#print("Press any key to continue:")
#sys.stdin.readline()



env.Dispose()

