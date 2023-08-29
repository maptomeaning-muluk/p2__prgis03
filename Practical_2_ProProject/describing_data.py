import arcpy
import os
# path to gdb

path = r"D:\SEM III\Programming_3\p2__prgis03\Practical_2_ProProject\02_Describing_Data.gdb"
# add the path
major_attraction_feature = "MajorAttractions"
freeways_feature = "Freeways"

major_attraction_feature_path = os.path.join(path, major_attraction_feature)
freeways_feature_path = os.path.join(path, freeways_feature)
print(major_attraction_feature_path);
print(freeways_feature_path);

#creating a describe object
major_attraction_desc_obj = arcpy.Describe(major_attraction_feature_path);
freeways_desc_obj = arcpy.Describe(freeways_feature_path)

#printing the type of shape
print('The type of the shape is {}'.format(major_attraction_desc_obj.shapeType));
print('The type of the shape is {}'.format(freeways_desc_obj.shapeType));