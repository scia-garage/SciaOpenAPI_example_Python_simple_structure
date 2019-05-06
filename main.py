print("Hello world");

import clr;
import sys;

clr.AddReference(r"c:\SCIA\VER\Full_R_19.0_patch_1_bugfix_19_05_03_10_37_19.0100.1053.32\Scia.OpenAPI.dll");

from SCIA.OpenAPI import *;
from SCIA.OpenAPI.StructureModelDefinition import *;
from SCIA.OpenAPI.Results import *;
from Results64Enums import *;
from System import Guid

env = Environment(r"c:\SCIA\VER\Full_R_19.0_patch_1_bugfix_19_05_03_10_37_19.0100.1053.32", r".\Temp", "1.0.0.0");
print("Environment set");

EnumGuiMode = Environment.GuiMode
env.RunSCIAEngineer(EnumGuiMode.ShowWindowShow)
print("SEn started")


proj = env.OpenProject(r"c:\SCIA\GIThub\SciaOpenAPI_example_parabolic\res\template.esa");

print("project opened");



steelmatid = ApiGuid.NewGuid();

steelmat = Material(steelmatid, r"steel S235", 1, r"S 235");
proj.Model.CreateMaterial(steelmat);
comatid = ApiGuid.NewGuid();
conmat = Material(comatid, "conc", 0, "C30/37");
proj.Model.CreateMaterial(conmat);
css_steel = ApiGuid.NewGuid();
cssHEA260 = CrossSectionManufactured(css_steel, "steel.HEA", steelmatid, "HEA260", 1, 0);
proj.Model.CreateCrossSection(cssHEA260);

zero = 0.0; # you can't use the "0" because it is INT and wrong constructor would be used by python.net...you must use the "0.0" DOUBLE value
a = 6.0;
b = 8.0;
c = 3.0;
n1 = ApiGuid.NewGuid();
n2 = ApiGuid.NewGuid();
n3 = ApiGuid.NewGuid();
n4 = ApiGuid.NewGuid();
n5 = ApiGuid.NewGuid();
n6 = ApiGuid.NewGuid();
n7 = ApiGuid.NewGuid();
n8 = ApiGuid.NewGuid();
proj.Model.CreateNode(StructNode(n1, "n1", zero, zero, zero));
proj.Model.CreateNode(StructNode(n2, "n2", a, zero, zero));
proj.Model.CreateNode(StructNode(n3, "n3", a, b, zero));
proj.Model.CreateNode(StructNode(n4, "n4", zero, b, zero));
proj.Model.CreateNode(StructNode(n5, "n5", zero, zero, c));
proj.Model.CreateNode(StructNode(n6, "n6", a, zero, c));
proj.Model.CreateNode(StructNode(n7, "n7", a, b, c));
proj.Model.CreateNode(StructNode(n8, "n8", zero, b, c));

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

proj.Model.CreateSlab(Slab(s1, "s1", 0, comatid, 0.15, ApiGuidArr( [ n5, n6, n7, n8 ])));

lg1 = ApiGuid.NewGuid();
proj.Model.CreateLoadGroup(LoadGroup(lg1, "lg1", 0));

lc1 = ApiGuid.NewGuid();
proj.Model.CreateLoadCase(LoadCase(lc1, "lc1", 0, lg1, 1));

sf1 = ApiGuid.NewGuid();
proj.Model.CreateSurfaceLoad(SurfaceLoad(sf1, "sf1", -12500.0, lc1, s1, 2));



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

#IntFor1Db1 =  rapi.CreateNewResult(keyIntFor1Db1);
IntFor1Db1 = rapi.LoadResult(keyIntFor1Db1);


print(IntFor1Db1.GetTextOutput());
#var N = IntFor1Db1.GetMagnitudeName(0);
#var Nvalue = IntFor1Db1.GetValue(0, 0);
#print(N);
#print(Nvalue);


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
pivot = 0.0;
i = 0;
while i < Def2Ds1.GetMeshElementCount():
	pivot = Def2Ds1.GetValue(2, i);
	if abs(pivot) > abs(maxvalue):
		maxvalue = pivot;
	i += 1

print("Calculated max deformation of slab is ", maxvalue, " m.")


proj.CloseProject(SaveMode.SaveChangesNo)
