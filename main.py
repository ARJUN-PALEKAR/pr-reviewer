import os
from github import Github
from google import genai  # The brand new SDK

# 1. Grab the API keys from the environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Initialize the new AI Client
client = genai.Client(api_key=GEMINI_API_KEY)

def main():
    # 3. Connect to GitHub
    g = Github(GITHUB_TOKEN)
    
    # Get the repository and PR number
    repo_name = os.getenv("GITHUB_REPOSITORY")
    pr_number = int(os.environ.get("PR_NUMBER", 0))
    
    if pr_number == 0:
        print("No PR number found. Exiting.")
        return

    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)

    # 4. Fetch the code changes
    diff_text = ""
    for file in pr.get_files():
        diff_text += f"File: {file.filename}\n"
        diff_text += f"Changes:\n{file.patch}\n\n"

    if not diff_text.strip():
        print("No code changes found to review.")
        return

    # 5. Instructions for the AI
    prompt = f"""
    You are a strict but helpful Senior Python Developer. 
    Review the following GitHub Pull Request diff.
    Look for bugs, security flaws, and bad time complexity. 
    Keep your feedback concise and helpful. Do not write a massive essay.
    
    Code Diff:
    {diff_text}
    """
    
    print("Sending code to AI for review...")
    
    # 6. Generate the response using the new SDK syntax
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )

    # 7. Post the comment
    pr.create_issue_comment(f"🤖 *Automated PR Review*\n\n{response.text}")
    print("Review posted successfully!")

if __name__ == "__main__":
    main()