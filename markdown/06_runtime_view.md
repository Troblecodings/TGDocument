# Runtime View

## Adding a texture

If the user wants to add a texture he can:

1. press the add-button in the editor
2. then a file chooser opens
3. there the user can select his textures
4. if the user accepts his selection the editor starts the shader tool with the according parameters (see [the ShaderTool docs](https://troblecodings.com/docs/shadertool.html))
5. the shader tool now copies the selected textures to the resource folder

## Building a map

If the user wants to build a map with its according resources he can:

1. he needs to execute the shader tool with the map make command
2. the shader tool then gathers all according resources
3. the according resources will then be build into a map file (see [the map file docs](https://troblecodings.com/fileformat.html))

## Loading a resource file

If the developer wants to load a resource file he has to:

1. invoke the loadResourceFile function
2. the function then reads through the file
3. for each resource the function allocates memory in the GPU or CPU
4. the resources are then being copied into the according buffer
