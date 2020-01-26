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