# FileForge
Automate setting up information gathering directories and sub-directories including files to be copied for pentest engagements.

A command-line tool to create new directories, copy files, and open in code editors.

## Changes Made
- January 16, 2023:
    - Initial version of the program created
- January 17, 2023: 
    - Added support for copying multiple files using the `shutil.copy()` method in a for loop
    - Added support for specifying the file path using the `--file_path` or `-f` option
    - Added support for specifying the code editor using the `--editor` or `-e` option
    - Added error handling for invalid hostname and incorrect file path
- January 18, 2023:
    - Added option to copy multiple files, updated -h summary and README.
- January 22, 2023:
    - Added error case handling via invalid chars
- January 23, 2023: 
    - Rewrote program to be well-structured and easy to understand
    - Debugged editor option: added if/else functionality to have -e EDITOR open files_to_copy
    - Redirect the -e EDITOR output to /dev/null, detaching it from the terminal and continue running in the background after the script exits

## To-Do List
- [x] Add how to add multiple files to script
- [x] Adjust FileForge to only open 1 window (notekeeping template) when multiple files are copied
- [x] Update summary
- [x] Explain how to use the tool via bash aliases
- [x] Remove error case that states hostname can not contain "" (underscore)
- [x] Debug editor option, alternative editors not able to open hostname directory. Perhaps have it open files_to_copy only
- [ ] Debugging the above now created the issue that default EDITOR (Visual Studio Code) is no longer opening directory either
- [ ] Issue is the os.chdir(hostname) function changes the current working directory of the script, but it does not change the working directory of the terminal.

There are a few different types of hostnames that could be considered "invalid" and handled as error cases in your program. Here are a few examples:

An empty hostname: If the user does not provide any input for the hostname when prompted, this would be considered an invalid hostname and should be handled as an error case.

A hostname that contains invalid characters: If the user provides a hostname that contains characters that are not allowed in a hostname, such as special characters or spaces, this would be considered an invalid hostname and should be handled as an error case.

=============================================
What hostnames will be handled as error cases
=============================================

A hostname that is too long: If the user provides a hostname that is longer than the maximum allowed length for a hostname, this would be considered an invalid hostname and should be handled as an error case.

A hostname that is already taken: If the user provides a hostname that already exist in the current directory and the program is trying to create a directory with the same name, this would be considered an invalid hostname and should be handled as an error case.

A hostname that begins with a number or a symbol: Hostname can not begin with a number or a symbol

#Removed: A hostname that contains "" (underscore) : Hostname can not contain "" (underscore)

It is important to consider these edge cases, and also to consider other possible cases that may not be listed here, when developing your program to ensure that it can handle all possible inputs and provide an appropriate error message to the user when an invalid hostname is provided.


=================================
longer explanation for on github:
=================================

To add this tool to your bash aliases, you'll need to edit your bash profile file (usually located at ~/.bash_profile or ~/.bashrc) and add a new alias.

For example, if you want to call the tool by the name "fileforge" you can add the following line to your bash profile file:

```
alias fileforge='python3 /path/to/fileforge.py'
```
Make sure to replace "/path/to/fileforge.py" with the actual path of your fileforge script.

Once you've added the alias, you'll need to reload your bash profile file for the changes to take effect. You can do this by running the following command:

```
source ~/.bash_profile
```

```
source ~/.bashrc
```
After that, you should be able to use the "fileforge" command directly from the terminal.

You will still be able to use the -h and -e options as well as providing the hostname when using the tool through a bash alias. The alias simply creates a shortcut for the command, it does not change the functionality of the tool itself. So you can use the command alias fileforge='python3 /path/to/fileforge.py' and then use fileforge -h or fileforge -e or fileforge hostname as usual.
