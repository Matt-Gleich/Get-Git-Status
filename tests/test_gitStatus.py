import sys
import subprocess
import os
sys.path.append("../gitStatus")

from main import gitStatus

def test_untrackedFiles():
    # ONE UNTRACKED FILE
    os.chdir("../gitStatus")
    os.system("touch test.txt")
    os.chdir("..")
    oneFileResult = gitStatus(os.getcwd()).untrackedFiles()
    os.chdir("gitStatus")
    os.system("rm test.txt")
    os.chdir("..")
    assert oneFileResult == ['gitStatus/test.txt']
    # TWO UNTRACKED FILES
    os.system("touch test1.txt")
    os.chdir("gitStatus")
    os.system("touch test2.txt")
    os.chdir("..")
    twoFilesResult = gitStatus(os.getcwd()).untrackedFiles()
    os.system("rm test1.txt")
    os.chdir("gitStatus")
    os.system("rm test2.txt")
    os.chdir("..")
    assert twoFilesResult == ['gitStatus/test2.txt', 'test1.txt']
    # UNTRACKED FILES WITH TRACKED FILE CHANGES
    os.system("touch test.txt")
    os.system("rm LICENSE.md")
    changesFilesResult = gitStatus(os.getcwd()).untrackedFiles()
    os.system("rm test.txt")
    assert changesFilesResult == ["test.txt"]
