import os
from github import Github
import google.generativeai as genai

# 1. Grab the API keys from GitHub Secrets (Environment Variables)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the AI Brain
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def main():
    # 2. Connect to GitHub
    g = Github(GITHUB_TOKEN)
    
    # Get the repository and PR number from GitHub Actions
    repo_name = os.getenv("GITHUB_REPOSITORY")
    pr_number = int(os.environ.get("PR_NUMBER", 0))
    
    if pr_number == 0:
        print("No PR number found. Exiting.")
        return

    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)

    # 3. Fetch the exact code changes (the + and - lines)
    diff_text = ""
    for file in pr.get_files():
        diff_text += f"File: {file.filename}\n"
        diff_text += f"Changes:\n{file.patch}\n\n"

    if not diff_text.strip():
        print("No code changes found to review.")
        return

    # 4. Give the AI its instructions and the code
    prompt = f"""
    You are a strict but helpful Senior Python Developer. 
    Review the following GitHub Pull Request diff.
    Look for bugs, security flaws, and bad time complexity. 
    Keep your feedback concise and helpful.
    
    Code Diff:
    {diff_text}
    """
    
    print("Sending code to AI for review...")
    response = model.generate_content(prompt)

    # 5. Post the AI's response as a comment on the PR
    pr.create_issue_comment(f"🤖 **PR Reviewer**\n\n{response.text}")
    print("Review posted successfully!")

if __name__ == "__main__":
    main()