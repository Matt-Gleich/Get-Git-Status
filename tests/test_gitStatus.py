import sys
import subprocess
import os
sys.path.append("../gitStatus")

from main import gitStatus

def resetGit():
    """Reset all the changes done locally
    """
    os.system("git checkout .")
    os.system("git clean -fd")

def test_untrackedFiles():
    """Test for the untrackedFiles func in main.py
    """
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
    os.chdir("tests")
    assert changesFilesResult == ["test.txt"]
    resetGit()

def test_unstagedFiles():
    """Test for the unstagedFiles func in main.py
    """
    # ONE DELETED FILE
    os.chdir("..")
    os.system("rm LICENSE.md")
    deletedResult = gitStatus(os.getcwd()).unstagedFiles()
    resetGit()
    assert deletedResult == ["LICENSE.md"]
    # ONE UPDATED FILE
    with open("dev-requirements.txt", "a") as file:
        file.write("HERE IS SOME TEXT ADDED")
    updatedResult = gitStatus(os.getcwd()).unstagedFiles()
    resetGit()
    assert updatedResult == ["dev-requirements.txt"]
    # MULTIPLE FILES
    os.system("rm LICENSE.md")
    with open("dev-requirements.txt", "a") as file:
        file.write("HERE IS SOME TEXT ADDED")
    multipleFilesResult = gitStatus(os.getcwd()).unstagedFiles()
    assert multipleFilesResult == ['LICENSE.md', 'dev-requirements.txt']
    resetGit()