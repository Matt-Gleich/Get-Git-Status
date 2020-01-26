import os
import subprocess

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
        self.command = subprocess.run(["git", 'status'], stdout=subprocess.PIPE).stdout.decode('utf-8').split("\n")
        print(self.command)

    def untrackedFiles(self):
        if "Untracked Files:" not in self.command:
            return []
        files = []
        listFromStart = self.command[self.command.index("Untracked Files:"):]
        blankLineCount = 0
        for line in listFromStart:
            if "\t" in line:
                files.append(line)
            elif blankLineCount == 1 and line == "":
                break
            elif line == "":
                blankLineCount += 1
        return files
        
        
