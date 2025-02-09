import bpy
import time
import os

log_file = "F:\\hogleg\\processed.json"
manual_input = False  # Set this to True for manual input, False for automatic loading

umap_directory = r"H:\ToolsForGameRipping\ToolsForGameRipping\unreal engine tools\FModel\Output\Exports"  # Directory to load .umap files from
umap_files = []

if not manual_input:
    current_directory = umap_directory 
    
    for root, dirs, files in os.walk(current_directory):
        for file in files:
            if file.endswith(".umap"):
                relative_path = os.path.relpath(os.path.join(root, file), current_directory)
                umap_files.append(relative_path.replace(os.sep, "/")) 
    print(f"Loaded {len(umap_files)} .umap files automatically.")
else:
    umap_files = [
        "Phoenix/Content/Environment/Hogwarts/SUB_AstronomyTower/SUB_AstronomyTower_EXT.umap", # .umap manual list
    ]
    print(f"Loaded {len(umap_files)} .umap files manually.")

bpy.context.scene.exportPath = "F:\\hogleg\\"
bpy.context.scene.Game_Path = "F:\\Hogwarts Legacy\\"
bpy.context.scene.mappings_path = "C:\\Dumper-7\\4.27.2-1117238+++stream+Main_TeamCity_Code-Phoenix\\Mappings\\4.27.2-1117238+++stream+Main_TeamCity_Code-Phoenix.usmap"

bpy.context.scene.bUseCustomEngineVer = True
bpy.context.scene.customEngineVer = "GAME_HogwartsLegacy"

bpy.context.scene.bExportFoliage = False
bpy.context.scene.bExportLights = False
bpy.context.scene.ParallelThreads = 1
bpy.context.scene.ObjectCacheSize = 0

bpy.context.scene.specular_1 = "PM_SpecularMasks"
bpy.context.scene.diffuse_1 = "PM_Diffuse"
bpy.context.scene.normal_1 = "PM_Normals"

collection_name = "MAIN"
if collection_name not in bpy.data.collections:
    bpy.data.collections.new(collection_name)
    bpy.context.scene.collection.children.link(bpy.data.collections[collection_name])

def wait_for_import():
    print("Waiting for import to finish...")
    start_time = time.time()
    while not os.path.exists(log_file):
        if time.time() - start_time > 30:
            print("Timeout reached. Skipping this map.")
            return False
        time.sleep(1)
    time.sleep(2)
    return True

total_umaps = len(umap_files)
for index, umap in enumerate(umap_files):
    print(f"Importing: {umap} ({index + 1}/{total_umaps})")

    if os.path.exists(log_file):
        os.remove(log_file)

    existing_objects = set(bpy.data.objects)

    bpy.context.scene.package = umap
    bpy.ops.umap.importmap()

    if not wait_for_import():
        continue

    imported_objects = [obj for obj in bpy.data.objects if obj not in existing_objects]

    main_collection = bpy.data.collections[collection_name]
    for obj in imported_objects:
        if obj.users_collection:
            for col in obj.users_collection:
                col.objects.unlink(obj)
        main_collection.objects.link(obj)

    print(f"Moved imported objects to '{collection_name}' collection.")

    print(f"Pausing for 5 seconds. {total_umaps - (index + 1)} UMAP(s) left.")
    time.sleep(5)

print("All imports completed!")
