import re
from typing import List, Optional


def extract_issue_numbers(text: str) -> List[int]:
    """Extract issue numbers from commit messages or PR descriptions.
    
    Matches patterns like: #123, fixes #456, closes #789
    """
    pattern = r"#(\d+)"
    matches = re.findall(pattern, text)
    return [int(m) for m in matches]


def parse_repo_url(url: str) -> Optional[dict]:
    """Parse a GitHub repository URL.
    
    Returns dict with owner and repo name, or None if invalid.
    """
    patterns = [
        r"github\.com[:/]([^/]+)/([^/\.]+)",  # Handles both HTTPS and SSH
        r"^([^/]+)/([^/]+)$",  # Simple owner/repo format
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return {
                "owner": match.group(1),
                "repo": match.group(2).replace(".git", ""),
            }
    
    return None


def truncate_text(text: str, max_length: int = 500, suffix: str = "...") -> str:
    """Truncate text to a maximum length."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def sanitize_filename(filename: str) -> str:
    """Sanitize a filename for safe storage."""
    return re.sub(r'[<>:"/\\|?*]', "_", filename)


def is_code_file(filename: str) -> bool:
    """Check if a file is likely a code file based on extension."""
    code_extensions = {
        ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".c", ".cpp", ".h",
        ".go", ".rs", ".rb", ".php", ".cs", ".swift", ".kt", ".scala",
        ".vue", ".svelte", ".html", ".css", ".scss", ".sql"
    }
    
    for ext in code_extensions:
        if filename.endswith(ext):
            return True
    return False
