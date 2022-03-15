import git

message = input("Please enter the commit message:\n")
print(message)
local_folder = './'
print("Repo already cloned, local folder: ", local_folder)
# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = git.Repo(local_folder)

#origin = repo.remote("origin")
#assert origin.exists()
#origin.fetch()
repo.git.status()
repo.git.add(all=True)
repo.git.status()
repo.git.commit('-m', message)
print("commit ")
repo.git.status()
repo.git.push()
print("push ")
