from typing import List, Dict, Any

from app.utils.diff_parser import parse_diff, DiffFile
from app.core.logging import get_logger

logger = get_logger(__name__)


class DiffService:
    def parse_diff(self, diff_content: str) -> List[DiffFile]:
        return parse_diff(diff_content)
    
    def extract_changes(self, diff_files: List[DiffFile]) -> Dict[str, Any]:
        changes = {
            "files_changed": len(diff_files),
            "additions": 0,
            "deletions": 0,
            "modified_functions": [],
            "file_types": set(),
        }
        
        for diff_file in diff_files:
            changes["additions"] += diff_file.additions
            changes["deletions"] += diff_file.deletions
            if diff_file.file_path:
                ext = diff_file.file_path.split(".")[-1] if "." in diff_file.file_path else "unknown"
                changes["file_types"].add(ext)
        
        changes["file_types"] = list(changes["file_types"])
        return changes
    
    def is_bug_fix(self, commit_message: str, diff_files: List[DiffFile]) -> bool:
        bug_keywords = ["fix", "bug", "issue", "error", "crash", "resolve", "patch"]
        message_lower = commit_message.lower()
        return any(keyword in message_lower for keyword in bug_keywords)


diff_service = DiffService()
