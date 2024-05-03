from github import Github, GithubException

USERNAME = "Sari-Shmuelevitz"
ACCESS_TOKEN = "*******"
gitub_connection = Github(ACCESS_TOKEN)
repo_name = "varonis-task"
repo = gitub_connection.get_repo(f"{USERNAME}/{repo_name}")


# Configuration 1: Enable Dependabot alerts
try:
    config_vulnerability_alert = repo.get_vulnerability_alert()
    print("Configuration 1 (Dependabot alerts):")
    print(f"Status: {'Enabled' if config_vulnerability_alert else 'Disabled'}")
    
    # If Dependabot alerts are disabled, enable them
    if not config_vulnerability_alert:
        repo.enable_vulnerability_alert()
        print("Dependabot alerts have been enabled.")
except GithubException as e:
    print(f"Error: {e}")

# Configuration 2: Enable branch protection rules
try:
    branch_name = "main"
    branch = repo.get_branch(branch_name)
    protection = branch.protected
    print("\nConfiguration 2 (Branch protection rules):")
    print(f"Status: {'Enabled' if protection else 'Disabled'}")

    # If branch protection rules are disabled, enable them
    if not protection:
            branch.edit_protection(
                enforce_admins=True,
                require_code_owner_reviews=True,# Require code owner reviews
                required_approving_review_count=1,# Require at least 1 approving review
                dismiss_stale_reviews=True # Dismiss approval reviews automatically when new commits are pushed
            )
            print("Branch protection rules have been enabled.")
except GithubException as e:
    print(f"Error: {e}")

# Configuration 3: Enable Require Signed Commits setting
try:
    require_signed_commits = repo.allow_squash_merge and repo.allow_merge_commit and repo.allow_rebase_merge
    print("\nConfiguration 3 (Require Signed Commits setting):")
    print(f"Status: {'Enabled' if require_signed_commits else 'Disabled'}")

    # If setting is not enabled, configure it
    if not require_signed_commits:
        repo.edit(allow_squash_merge=True, allow_merge_commit=True, allow_rebase_merge=True)
        print("Require Signed Commits setting has been enabled.")

except GithubException as e:
    print(f"Error: {e}")

# Configuration 4: Enable Private repository visibility
try:
    repo_visibility = repo.private
    print("\nConfiguration 4 (Private repository visibility):")
    print(f"Status: {'Private' if repo_visibility else 'Public'}")

    if not repo_visibility:
        repo.edit(private=True)
        print("Private repository visibility has been enabled.")
except GithubException as e:
    print(f"Error: {e}")
