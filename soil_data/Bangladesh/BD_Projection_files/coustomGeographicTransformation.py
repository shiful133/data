# Name: CreateCustomGeographicTransformation.py
# Description: Creates a custom geographic transformation in the default directory.


# import system modules
import arcpy

# set the variables
try:
    geoTransfmName = "cgt_geocentric_WGS84_EVERST"
    inGCS="GEOGCS['GCS_WGS_1984', DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
    outGCS="GEOGCS['GCS_Everest_Bangladesh',DATUM['D_Everest_Bangladesh',SPHEROID['Everest_Adjustment_1937',6377276.345,300.8017]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
    customGeoTransfm = "GEOGTRAN[METHOD['Geocentric_Translation'],PARAMETER['X_Axis_Translation',''],PARAMETER['Y_Axis_Translation',''],PARAMETER['Z_Axis_Translation','']]"
    arcpy.CreateCustomGeoTransformation_management(geoTransfmName, inGCS, outGCS, customGeoTransfm)

except:
    print "transformation failed."
    print arcpy.GetMessages()
