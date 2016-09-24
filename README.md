# Python-Text-Editor
A simple console text editor made in Python

#How to run
Run the program just as you would any other python script.


  .\text-editor.py filename.fileextention

You may need to create a file named file.txt within the programs folder inorder for it to run.

#Commands
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
    
#Plugin support
The newest update allows for plugin support. All plugins have a text file, called their list file, named the same as the python file for the plugin, which lists all of the functions in the python file.

For example, if you had two functions in the python file, the list file will list the function's names like so,

  node.txt
  
    node_function
    
    second_node_function
    
When a plugin function is called, the text editor creates a temporary file and outputs the currently opened file into it. This is used so the plugins can manipulate the text file. When the function exits, the text editor opens and then deletes the temp file. 

    -load, [plugin]
    
  Loads the specified plugin (plugin). If the plugin's list file is named node.txt, the plugin argument would be just node.
  
    -[plugin function] [arg1] [arg2] [arg3] ...
    
  Runs specified plugin function (plugin function), as listed in plugin list file, with as many arguments (arg1, arg2, arg3, ...) as the function calls for.
  
Theoretically plugins allow the skilled python programmer could use this to do really cool things with data and stuff. Amen.
