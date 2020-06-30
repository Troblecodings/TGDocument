# Deployment View

The following chapter describes the different build environments and the artifacts that each produce. This also covers how and for what they are used.

**To build your own versions you need to download all dependencies using the setup.py script in the engine repository (or submodule). Otherwise it will not compile.** For more information see [https://troblecodings.com/](https://troblecodings.com/)

## TGEngine and ShaderTool

This part is about the [TGEngine](https://github.com/Troblecodings/TGEngine) repository. This repository should not be used by the engine users. For user who want to make a game with the engine you should use the Template repository or use this repository as submodule.

Like Google, we want to enable the compiler to optimise our code hence we use static linkage.

There is no auto deployment for anything but the ShaderTool. The Artifacts produced by the compile pipeline can be accessed through the Artifacts tab on the given build. This produces a runnable dotnet core application. This should be able to run through the dotnet command on Linux and Mac. On windows you just need to execute the given executable (.exe) file. The ShaderTool manages your projects and resources. The engine itself produces a static library which can be used to link your project against. The engine itself currently only works on windows systems with the according Vulkan 1.0 compatible Graphics device. For more information on wether your system is Vulkan capable or not please visit [the gpuinfo database](https://vulkan.gpuinfo.org/). *Note: There is a working Linux compile chain however there is currently no demo as the window creation is still missing*

## Template

This part is about the [Template](https://github.com/Troblecodings/Template) repository. This repository should normally be used to create a new game project. However as there is currently a github bug that prevents the submodule template to work correctly. Hence we recommend to manually install the submodule and still use the project but reset the contents. A getting started page is currently being worked on. For a example on how that could look see TGTest. This system should produce a runnable with the same restrictions as the engine itself.

## TGTest

This part is about the [TGTest](https://github.com/Troblecodings/TGTest) repository. This (what a coincidence) is a test repository to show of current features and general usage of the engine. This again produces a runnable file with the same restrictions as the engine itself. This already contains a version of the Engine as submodule.

## TGEditor

The [TGEditor](https://github.com/Troblecodings/TGEditor) repository holds the editor source code and it's resources. The editor is build upon the engine and is used as GUI for the ShaderTool. Therefore it produces a runnable file as well as a TGEngine Resource File (.tgr) file containing the baked resources from our resource system. On top of the restrictions applied by the engine the editor needs a working shader tool artifact which is included in the repository under the TGEditor folder.

## TGDocument

That is the repository this documentation is saved in. HTML Version available [TGDocument](https://troblecodings.github.io/TGDocument/)