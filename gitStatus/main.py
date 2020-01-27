import os
import subprocess

def getSectionFiles(sectionIdentifier, command):
    """Get the files for a certain part of the git status command
    
    Arguments:
        sectionIdentifier {str} -- The string that idenfies the file list section
        command {list} -- The git status command ran
    
    Returns:
        list -- List of files if any
    """
    if sectionIdentifier not in command:
        return []
    files = []
    listFromStart = command[command.index(sectionIdentifier):]
    blankLineCount = 0
    for line in listFromStart:
        if "\t" in line:
            files.append(line.strip("\t"))
        elif blankLineCount == 1 and line == "":
            break
        elif line == "":
            blankLineCount += 1
    return files
    
def cleanFiles(removeList, files):
    """Clean files by removing certain parts of the file name
    
    Arguments:
        removeList {list} -- Things to remove from the file
        files {list} -- List of files
    
    Returns:
        list -- List of cleaned files
    """
    cleanedFiles = []
    for file in files:
        for removeable in removeList:
            file = file.replace(removeable, "")
        file = file.strip()
        cleanedFiles.append(file)
    return cleanedFiles


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

    def unstagedFiles(self):
        """Get a list of all the unstaged files for the repo
        
        Returns:
            list -- List of all the files
        """
        files = getSectionFiles("Changes not staged for commit:", self.command)
        return cleanFiles(["deleted:", "modified:"], files)
