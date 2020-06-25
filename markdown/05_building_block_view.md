# Building Block View

## ShaderTool

The primary purpose of the ShaderTool was to compile shader into the Engine. The tool started to grow because of it's console interface which makes it ideal for tooling.

![Whitebox](images/whitebox1.png)

| Subsystem         | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| Console Interface | Allowes for Console input and forwards the arguments to the give subsystem   |
| Shader Interface  | This system compiles shader and embeds them into the Engine                  |
| Pipe Interface    | Analyzes the compiled shaders and creates the according pipeline information |
| Ressource System  | This system administrates all game ressources.                               |

## TGEngine

The decomposition has historical resons

![Whitebox](images/whitebox2.png)

| Subsystem       | Description                                                                                                                        |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| IO              | For general in and output managment                                                                                                |
| UI              | Contains all user interface components                                                                                             |
| Gamecontent     | Everything that can be put into the game (Actors, Lights  ...)                                                                     |
| Pipeline        | This is the heart of the engine and contains everything needed to create a Vulkan Application with the according featureset needed |
| General IO      | Platform independency layer for file handling                                                                                      |
| Properties      | A small XML reader with a given schema                                                                                             |
| Ressourcesystem | the counterpart to the ShaderTools Ressource System, except this one only reads the ressources                                     |
| Memory Layer    | The own Memory managmet for the GPU as well as the system memory                                                                   |
| Pipeline Stages | Consists of all passes and commands recorded to the GPU                                                                            |
| Buffer          | All the static memory buffering on the GPU                                                                                         |