import arcpy
import os

gdb_path = r"D:\SEM_III\Programming_3\p2__prgis03\Practical_2_ProProject\02_Describing_Data.gdb"
fc_name_list = ["MajorAttractions","Freeways"]

for fc in fc_name_list:
    fc_path = os.path.join(gdb_path,fc)
    desc_obj = arcpy.Describe(fc_path)

    shape_type = desc_obj.shapeType
    print("The geometry of feature class {} is {}".format(fc,shape_type))

    # user assigned name
    fc_name =desc_obj.name
    print(fc_name)

    #The type of dataset Some possible values : FeatureDataset, FeatureClass, Raster, TAble
    dataset_type =desc_obj.datasetType
    print(dataset_type)

    sr_obj = desc_obj.spatialReference
    print(sr_obj.name)
    print(sr_obj.type)

    field_list = desc_obj.fields
    for field in field_list:
        field_name = field.name
        field_type = field.type

        '''print(field_name)
        print(field_type)'''

        print("In {} have field name: {} which field type is {}".format(fc,field_name,field_type))

print("process completed")

