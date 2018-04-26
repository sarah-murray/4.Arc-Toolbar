import arcpy

arcpy.env.workspace = "M:/All_GIS_work/Programming2/Prac4"

if arcpy.Exists("crime.shp"):
    arcpy.Delete_management ("crime.shp")
	
if arcpy.Exists("temp_crime.shp"):
    arcpy.Delete_management ("temp_crime.shp")

Burglaries = arcpy.GetParameterAsText(0)
Distance = arcpy.GetParameterAsText(1)
Buildings = arcpy.GetParameterAsText(2)
Out1 = "temp_crime.shp"
Out2 = "crime.shp"

arcpy.ImportToolbox("M:/All_GIS_work/Programming2/Prac1/Models.tbx", "models")
arcpy.TraffordModel_models(Burglaries, Distance, Out1, Buildings, Out2)

if arcpy.Exists("crime_sorted.shp"):
    arcpy.Delete_management ("crime_sorted.shp")
arcpy.Sort_management(Out1, "crime_sorted", [["Join_Count", "DESCENDING"]])

mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame 
newlayer = arcpy.mapping.Layer("crime_sorted.shp")
layerFile = arcpy.mapping.Layer("albertsquare/buildings.lyr")
arcpy.mapping.UpdateLayer(df, newlayer, layerFile, True)
newlayer.symbology.valueField = "Join_Count"
newlayer.symbology.addAllValues() 
arcpy.mapping.AddLayer(df, newlayer,"TOP")