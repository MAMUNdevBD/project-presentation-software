import git
import os 

class GitController:
    
    @staticmethod
    def clone(url):
        git.Git("projects").clone(url)
    
GitController.clone("https://github.com/Wa316082/uvproject")