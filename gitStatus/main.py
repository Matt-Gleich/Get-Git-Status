import os
import subprocess

def getSectionFiles(sectionIdentifier, command):
    if sectionIdentifier not in command:
            return []
    files = []
    listFromStart = command[command.index(sectionIdentifier):]
    blankLineCount = 0
    for line in listFromStart:
        print(line)
        if "\t" in line:
            files.append(line.strip("\t"))
        elif blankLineCount == 1 and line == "":
            break
        elif line == "":
            blankLineCount += 1
    return files
    

class gitStatus():
    """Get the git status of any repo
    """

    def __init__(self, repoPath):
        """Create an object for the repo
        
        Arguments:
            repoPath {str} -- Full path to the repo
        """
        self.path = repoPath
        os.chdir(self.path)
        self.command = subprocess.run(["git", "status"], stdout=subprocess.PIPE).stdout.decode('utf-8').split("\n")

    def untrackedFiles(self):
        """Get a list of all the untrackedFiles for the repo
        
        Returns:
            list -- List of all the files
        """
        return getSectionFiles("Untracked files:", self.command)
    
        files = []
