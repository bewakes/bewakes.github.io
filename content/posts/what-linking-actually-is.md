---
title: What linking actually is
date: July 27, 2017
tags:
    - computer-science
location: Patan Dhoka
---

*program.. C program.. compiler.. gcc.. library.. object file.. linker.. linking.. linkinpark.. In the end.. it doesn't even matter.. and now, I've become so numb..(cries)*

It's very easy to get carried away and frustrated while 'thinking' about 'linking'.
<br/>
NOTE: I am a great fan of LinkinPark.

If you have once been a beginner C programmer or are one now, then you must have once been confused by the concept of 'linking' and 'compiling'. 'Compiling' does not bug as much as 'linking' does(at least for me) because, simply speaking, it is a process of converting the code that we have written in high level languages into the code(binary) that the computer understands.

### Libraries
It often happens that, for many programs that we write, some of the functionalities are common(like mathematical functions used during computational programs, graphics functionalities used during making games or user interfaces, etc). These common functionalities are also implemented as code, but we call them libraries which can be used by different people without having to rewrite themselves.

### Object files
So, for libraries we just include and use them; rest is handled by compiler and linker. A library is available as an object file. An object file is a compiled file that contain the definition of library functions that we use in our programs.

### Linking
Now, when we compile our code, it is compiled by compiler to object file. The object file in our case has references to the library functions that we have used(of course, we have not written definitions for the library functions so there's no way the definitions are available in our object file). Thus, our program's object file contains void space(not literally, but you got the point..) to be filled by the definitions of library functions. The linker then fills in the void i.e. combines our object file and the object files of the library and finally an executable is created which is complete and can be run. Note that, linker is also a program like a compiler.

That's all that is happening between the time we write our code and finally run it.

### Some more..
#### Static and dynamic linking

I won't dwell into details about static and dynamic linking. In static linking, the library object file is merged with our object file into a single executable. The executable is fast and it does not require the presence of the library on the system where it is run. But the executable size is large. And also, if there are different programs using the library, same copy of library object is merged into all of the programs, which is quite redundant. The .a files in linux/unix and .lib files in windows are static libraries.

In dynamic linking, library object file is not merged with our object file. Instead, it is directly loaded into memory together with our object file and library function definition is referenced within the memory. This allows multiple programs to share the library and also keeps our executable file size smaller and upgrading of code easier. However, the library needs to be present wherever our executable file is moved. Dynamic linking is slower than static linking. Also, it can cause compatibility issues if versions do not match. The .so files in linux/unix and .dll in windows are dynamic libraries. 
