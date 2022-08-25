import git
import os 

class GitController:
    
    @staticmethod
    def clone():
        git.Git("projects").clone("https://github.com/MAMUNdevBD/project-presentation-software.git")
    