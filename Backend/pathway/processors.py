from typing import Dict, Any, List


def process_commit(commit_data: Dict[str, Any]) -> Dict[str, Any]:
    message = commit_data.get("message", "")
    
    return {
        "sha": commit_data.get("id", commit_data.get("sha", "")),
        "message": message,
        "is_bug_fix": is_bug_fix_commit(message),
        "files_changed": len(commit_data.get("modified", [])),
        "author": commit_data.get("author", {}).get("name", "unknown"),
    }


def process_issue(issue_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "number": issue_data.get("number"),
        "title": issue_data.get("title", ""),
        "state": issue_data.get("state", "open"),
        "is_bug": is_bug_issue(issue_data),
    }


def is_bug_fix_commit(message: str) -> bool:
    bug_keywords = [
        "fix", "bug", "issue", "error", "crash", "resolve",
        "patch", "repair", "correct", "hotfix"
    ]
    message_lower = message.lower()
    return any(keyword in message_lower for keyword in bug_keywords)


def is_bug_issue(issue_data: Dict[str, Any]) -> bool:
    labels = issue_data.get("labels", [])
    label_names = [l.get("name", "").lower() for l in labels]
    
    bug_labels = ["bug", "defect", "error", "issue"]
    return any(bl in label_names for bl in bug_labels)


def extract_related_issues(message: str) -> List[int]:
    import re
    
    patterns = [
        r"#(\d+)",
        r"(?:fix|fixes|fixed|close|closes|closed|resolve|resolves|resolved)\s*#(\d+)",
    ]
    
    issues = set()
    for pattern in patterns:
        matches = re.findall(pattern, message, re.IGNORECASE)
        issues.update(int(m) if isinstance(m, str) else int(m[-1]) for m in matches)
    
    return list(issues)
