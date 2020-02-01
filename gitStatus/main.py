import os
import subprocess


def getSectionFiles(sectionIdentifier, command):
    """Get the files for a certain part of the git status command

    Arguments:
        sectionIdentifier {str} -- The string that identifies the file list section
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


def matchFileAndStatus(fileList):
    """Match a file with it current status

    Arguments:
        fileList {list} -- List of all files read from the git status command

    Returns:
        dict -- Matched files
    """
    matchedFiles = {}
    for file in fileList:
        status = file.split(":")[0]
        file = file.split(":")[-1].strip()
        matchedFiles[file] = status
    return matchedFiles


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
        self.command = subprocess.run(
            ["git", "status", "-u"], stdout=subprocess.PIPE).stdout.decode('utf-8').split("\n")

    def untrackedFiles(self):
        """Get a list of all the untrackedFiles for the repo

        Returns:
            list -- List of all the files
        """
        return getSectionFiles("Untracked files:", self.command)

    def unstagedFiles(self):
        """Get a list of all the unstaged files for the repo

        Returns:
            dict -- List of all the files and they're statuses
        """
        files = getSectionFiles("Changes not staged for commit:", self.command)
        return matchFileAndStatus(files)

    def stagedFiles(self):
        """Get a list of all the staged files for the repo

        Returns:
            dict -- List of all the files and they're statuses
        """
        files = getSectionFiles("Changes to be committed:", self.command)
        return matchFileAndStatus(files)
