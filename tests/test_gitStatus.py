import sys
import os
sys.path.append("../gitStatus")
os.chdir("../gitStatus")

from main import gitStatus

def test_untrackedFiles():
    os.system("touch test.txt")
    print(gitStatus(os.getcwd()).untrackedFiles())
    assert gitStatus(os.getcwd()).untrackedFiles() == True