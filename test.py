import git
import tempfile
import os
import uuid
from shutil import copyfile
from pathlib import Path, PureWindowsPath

uid = str(uuid.uuid4())
#PATH_OF_GIT_REPO = os.path.join(tempfile.gettempdir(), uid)
folder = os.path.join(os.path.dirname(__file__))
PATH_OF_GIT_REPO = os.path.join(folder, uid)
COMMIT_MESSAGE = '[AUTO] Add acl'
REMOTE_URL = "https://github.com/MRagulin/Stepik.git"


BRANCH = 'master'
USER = ""
PASS = ""

REMOTE_URL = f"https://{USER}:{PASS}@github.com/MRagulin/Stepik.git"

class Git:
    def __init__(self):
        print("Git init")
        self.repo = git.Repo.init()  # uid, bare=True
       # self.repo.config_writer().set_value("name", "email", USER).release()
        #self.repo.config_writer().set_value("name", "email", "myemail").release()
        # project_dir = os.path.dirname(os.path.abspath(__file__))
        # os.environ['GIT_ASKPASS'] = os.path.join(project_dir, 'acl.md')
        # os.environ['GIT_USERNAME'] = USER
        # os.environ['GIT_PASSWORD'] = PASS


        if not os.path.exists(PATH_OF_GIT_REPO):
         os.makedirs(PATH_OF_GIT_REPO)
         print("Create folder: {}".format(PATH_OF_GIT_REPO))

    def clone(self):
        self.repo = self.repo.clone_from(REMOTE_URL, PATH_OF_GIT_REPO)
        if len(self.repo.index.entries) == 0:
           print("Ничего не скачалось :-(")
           return 0
        print("Download: {} files".format(len(self.repo.index.entries)))

    def activity(self):
        sfile = os.path.join(Path(folder).resolve().parent.parent, 'acl_276dfeef-ddb3-4bd5-af52-04424352b8c8.md')
        dfile = os.path.join(PATH_OF_GIT_REPO, 'acl.md')
        copyfile(sfile, dfile)
        print("File has been copied: {}".format(dfile))
        return str(PureWindowsPath(dfile)).replace('/', '//')


    def addindex(self, filename):
        index = self.repo.index
        index.add([filename])
        #assert len(list(index.iter_blobs())) == len([o for o in self.repo.head.commit.tree.traverse() if o.type == 'blob'])
        index.commit(COMMIT_MESSAGE)
        print("Commit changes")


    def push(self):
        #remote = self.repo.create_remote('origin', self.repo.remotes.origin.url)
        self.repo.remotes.origin.push(refspec='master:master')



if __name__ == "__main__":

    g = Git()
    g.clone()
    f = g.activity()
    g.addindex(f)
    g.push()
    print("Finish.")



    # if not os.path.exists(PATH_OF_GIT_REPO):
    #     os.makedirs(PATH_OF_GIT_REPO)
    #     print("Create folder: {}".format(PATH_OF_GIT_REPO))
    #
    # repo = git.Repo.init() #uid, bare=True
    # repo.config_reader()
    # o = repo.clone_from(REMOTE_URL, PATH_OF_GIT_REPO)
    # if len(o.index.entries) == 0:
    #     print("Ничего не скачалось :-(")
    #     return 0
    # if repo.active_branch != BRANCH:
    #     BRANCH = repo.active_branch




