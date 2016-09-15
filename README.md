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
    
