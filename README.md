# Python-Text-Editor
A simple console text editor made in Python

# How to run
Run the program just as you would any other python script.


  .\text-editor.py filename.fileextention

You may need to create a file named file.txt within the programs folder inorder for it to run.

# Commands
Commands and their argumennts are separated by commas

  -open, [file path]
  
    Open a specific file
    
    The file path argument is optional, running the command without it will just reload the current file
    
  -print, [line num]
  
    Print a specific line (line num)
  
    The line num argument is optional, running the command without it will print the entire current file
  
  -change, [line num], [new line]
  
    Change a specific line (line num) to a new line (new line)
  
  -save, [file path]
  
    Save file to a file path
  
    The file path argument is optional, running the command without it will overwrite the current file
  
  -nl, [line num], [new line]
  
  -\n, [line num], [new line]
  
  -new line, [line num], [new line]
  
    Create new line (new line) at specified line number (line num)
  
  -find, [query], [after line num]
  
    Output cases of a query (query) after a specified line (line num)
  
    After line num argument is optional, running command without it will search the whole file
    
  -remove, [string], [replace-with-string]
  
    Removes any cases of a string in file (string), and replaces this with a new string [replace-with-string]
    
    Replace with string argument is optional, running command with out it just removes the requested string
    
# Plugin support
The newest update allows for plugin support. 

A plugin is a python script which loads the temporay .temp file which the text editor creates for the time the plugin is being run, containing the currently loaded file in the text editor, and makes changes to the temp file, which will be loaded when the plugin is done being executed. Alternativly, the plugin does not nessicarily need to make changes to the temp file at all, it may just load the temp file and maybe do analytics on it. In theory, the plugin doesn't need to do anything with the temp file at all, it just needs to be a python script.  

    -load, [plugin]
    
Checks if the specified plugin (plugin) exists as a python file, and adds to list of existing plugins. For example if you have a plugin whose filename is "plugin.py", you would use the command "load, plugin". This needs to be run before the plugin can be used.

Note that the plugin must be in the same folder as the text editor. 
  
    -[plugin] [arg1] [arg2] [arg3] ...
    
Runs specified plugin (plugin), with as many arguments (arg1, arg2, arg3, ...) as the plugin calls for.

An example of a functioning plugin is the graphing.py plugin.
