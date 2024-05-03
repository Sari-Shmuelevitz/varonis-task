from github import Github, GithubException

USERNAME = "Sari-Shmuelevitz"
ACCESS_TOKEN = "*******"
gitub_connection = Github(ACCESS_TOKEN)
repo_name = "varonis-task"
repo = gitub_connection.get_repo(f"{USERNAME}/{repo_name}")
branch_name = "main"
try:
   
    branch = repo.get_branch(branch_name)
    # branch.edit_protection(strict=False)
    file_path = "risk_file.txt"
    file_content = "This is a test file created by the risk demo script."
    repo.create_file(file_path, "risk commit", file_content, branch=branch_name)
    print(f"File '{file_path}' added to the repository.")
except GithubException as e:
    if e.status == 409:
        print("Error: Changes rejected. Branch protection is working as expected.")
        print("Error:", e)
    else:
        print("Error:", e)
