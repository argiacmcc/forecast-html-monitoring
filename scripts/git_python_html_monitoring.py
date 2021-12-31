import git
#from git import Repo

message = input("Please enter the commit message:\n")

local_folder = '/Users/argia/cmcc/repos/forecast-html-monitoring'
print("Repo already cloned, local folder: ", local_folder)
# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = git.Repo(local_folder)
#repo = Repo(self.rorepo.local_folder)
#assert not repo.bare

origin = repo.remote("origin")
assert origin.exists()
origin.fetch()
#repo.git.add('--all')
repo.git.status()
repo.git.add(all=True)
repo.git.status()
repo.git.commit(message)
print("commit ")
repo.git.status()
repo.git.push()
print("push ")
