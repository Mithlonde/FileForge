#!/usr/bin/env python3
#
# Author: Mithlonde
#
# FileForge v1.0.4 - Last updated: April 19, 2024
# https://github.com/Mithlonde/FileForge 


import os, shutil, subprocess, argparse


# -------------- Arguments -------------- #
parser = argparse.ArgumentParser(prog='FileForge',
    description='Automate setting up information gathering directories and subdirectories including files to be copied for pentest engagements.',
    epilog='Quick summary: FileForge can be used to automate setting up your information gathering archives. A task often repeated manually prior to any pentest engagement. It will quickly create a new directory with the provided hostname, create sub-directories for images and scan results, and copy files specified by the user (like your preferred note keeping template). Your FileForge will be opened in Visual Studio Code, ready set to go start your engagement!'
    )
                                     
parser.add_argument('hostname', type=str, help='Preferred hostname of directory')
parser.add_argument('files_to_copy', nargs='*', help='Files to be copied ["path/to/file1", "path/to/file2"]')
parser.add_argument('-e', '--editor', type=str, default='code', help='code editor to open the directory (default: code)')

args = parser.parse_args()

# -------------- Functions -------------- #
def main(hostname, files_to_copy, editor):

    try:

        invalid_chars = '\/:*?"<>|'

        if not hostname or any(char in hostname for char in invalid_chars):
            raise Exception("Invalid hostname")
        
        os.mkdir(hostname)
        os.mkdir(f"{hostname}/scans")
        os.mkdir(f"{hostname}/images")
        os.mkdir(f"{hostname}/vulns")
        os.mkdir(f"{hostname}/files")
        # Additional subdirectories can be added here
        # os.mkdir(f"{hostname}/NameYourFolder")
        os.chdir(hostname)

        if files_to_copy:
            for file in files_to_copy:
                try:
                    shutil.copy(file, ".")
                except Exception as e:
                    print(f"Error copying file {file}: {e}")

        else:
            print("No files to copy")
    
    	# Create empty files
        open("hashes", "w").close()
        open("passwords", "w").close()
        open("users", "w").close()
        
        subprocess.Popen([editor, "."])
        print("FileForge created successfully, GL!")

    except Exception as e:
        print(e)

# ----------- Copy Files ----------- #
files_to_copy = ["path/to/notes.md", "path/to/file2"]
# Additional files to be copied can be added here
# ["path/to/file1", "path/to/file2"]


if __name__ == '__main__':
	main(args.hostname, files_to_copy, args.editor)
