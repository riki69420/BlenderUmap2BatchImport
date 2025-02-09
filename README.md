# Blender UMAP Batch Import Script

This script is designed to automate the import of `.umap` files into Blender using the BlenderUmap2 addon. It can either load `.umap` files from a specified directory or manually input them, and it organizes imported objects into a "MAIN" collection.

## Features

- Automatically loads `.umap` files from a specified directory and its subdirectories.
- Option to manually input `.umap` files.
- Configurable game path and export path.
- Allows you to configure additional options like specular, diffuse, and normal maps.
- Imports objects into a "MAIN" collection in Blender.
- Pauses for 5 seconds after each import to allow memory usage to calm down.
- Handles log processing and skips maps if timeouts occur.

## Requirements

- Blender (tested with Blender 4.3 and the BlenderUmap2 addon).
- FModel (for exporting `.umap` files from Unreal Engine).

## Installation

1. Clone or download the repository to your computer.
2. Make sure you have the [BlenderUmap2 addon](https://github.com/yourusername/BlenderUmap2) installed and working in Blender.
3. Place the script in a folder of your choice.

## Usage

1. Set `manual_input` to `False` if you want to automatically load `.umap` files from a specified directory, or `True` for manual input.
2. If using automatic loading, specify the path to the directory containing `.umap` files in `umap_directory`.
3. Set other configuration paths like `exportPath`, `Game_Path`, and `mappings_path` to suit your project.
4. Run the script inside Blender's scripting environment.

### Example Configuration:

```python
manual_input = False  # Set to True for manual input, False for automatic loading
umap_directory = r"H:\ToolsForGameRipping\ToolsForGameRipping\unreal engine tools\FModel\Output\Exports"  # Directory to load .umap files from
