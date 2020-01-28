import sys
import subprocess
import os
sys.path.append("../gitStatus")
from main import gitStatus

def resetGit():
    """Reset local git changes
    """
    os.system("git reset")
    os.system("git checkout .")


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
    assert deletedResult == {"LICENSE.md": "deleted"}
    # ONE UPDATED FILE
    with open("dev-requirements.txt", "a") as file:
        file.write("HERE IS SOME TEXT ADDED")
    updatedResult = gitStatus(os.getcwd()).unstagedFiles()
    resetGit()
    assert updatedResult == {"dev-requirements.txt": "modified"}
    # MULTIPLE FILES
    os.system("rm LICENSE.md")
    with open("dev-requirements.txt", "a") as file:
        file.write("HERE IS SOME TEXT ADDED")
    multipleFilesResult = gitStatus(os.getcwd()).unstagedFiles()
    assert multipleFilesResult == {
        "LICENSE.md": "deleted", "dev-requirements.txt": "modified"}
    os.chdir("tests")
    resetGit()


def test_stagedFiles():
    """Test for the stagedFiles func in main.py
    """
    # ONE DELETED FILE
    os.chdir("..")
    os.system("rm LICENSE.md")
    os.system("git add .")
    deletedResult = gitStatus(os.getcwd()).stagedFiles()
    resetGit()
    assert deletedResult == {"LICENSE.md": "deleted"}
    # ONE UPDATED FILE
    with open("dev-requirements.txt", "a") as file:
        file.write("HERE IS SOME TEXT ADDED")
    os.system("git add .")
    updatedResult = gitStatus(os.getcwd()).unstagedFiles()
    resetGit()
    assert updatedResult == {"dev-requirements.txt": "modified"}
    # MULTIPLE FILES
    os.system("rm LICENSE.md")
    with open("dev-requirements.txt", "a") as file:
        file.write("HERE IS SOME TEXT ADDED")
    os.system("git add .")
    multipleFilesResult = gitStatus(os.getcwd()).unstagedFiles()
    assert multipleFilesResult == {
        "LICENSE.md": "deleted", "dev-requirements.txt": "modified"}
    os.chdir("tests")
    resetGit()
