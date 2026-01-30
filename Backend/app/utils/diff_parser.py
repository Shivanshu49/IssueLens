from typing import List, Optional
from dataclasses import dataclass, field
import re


@dataclass
class DiffHunk:
    old_start: int
    old_count: int
    new_start: int
    new_count: int
    lines: List[str] = field(default_factory=list)


@dataclass
class DiffFile:
    file_path: Optional[str] = None
    old_path: Optional[str] = None
    new_path: Optional[str] = None
    hunks: List[DiffHunk] = field(default_factory=list)
    additions: int = 0
    deletions: int = 0
    is_new_file: bool = False
    is_deleted_file: bool = False
    is_renamed: bool = False


def parse_diff(diff_content: str) -> List[DiffFile]:
    files: List[DiffFile] = []
    current_file: Optional[DiffFile] = None
    current_hunk: Optional[DiffHunk] = None
    
    lines = diff_content.split("\n")
    
    for line in lines:
        if line.startswith("diff --git"):
            if current_file:
                files.append(current_file)
            current_file = DiffFile()
            current_hunk = None
            
            match = re.match(r"diff --git a/(.+) b/(.+)", line)
            if match:
                current_file.old_path = match.group(1)
                current_file.new_path = match.group(2)
                current_file.file_path = match.group(2)
        
        elif current_file:
            if line.startswith("new file"):
                current_file.is_new_file = True
            elif line.startswith("deleted file"):
                current_file.is_deleted_file = True
            elif line.startswith("rename from"):
                current_file.is_renamed = True
            
            elif line.startswith("@@"):
                match = re.match(r"@@ -(\d+),?(\d*) \+(\d+),?(\d*) @@", line)
                if match:
                    current_hunk = DiffHunk(
                        old_start=int(match.group(1)),
                        old_count=int(match.group(2)) if match.group(2) else 1,
                        new_start=int(match.group(3)),
                        new_count=int(match.group(4)) if match.group(4) else 1,
                    )
                    current_file.hunks.append(current_hunk)
            
            elif current_hunk is not None:
                current_hunk.lines.append(line)
                if line.startswith("+") and not line.startswith("+++"):
                    current_file.additions += 1
                elif line.startswith("-") and not line.startswith("---"):
                    current_file.deletions += 1
    
    if current_file:
        files.append(current_file)
    
    return files


def get_changed_functions(diff_file: DiffFile, language: str = "python") -> List[str]:
    functions = []
    
    if language == "python":
        pattern = r"^\+?\s*def\s+(\w+)"
        for hunk in diff_file.hunks:
            for line in hunk.lines:
                match = re.match(pattern, line)
                if match:
                    functions.append(match.group(1))
    
    return list(set(functions))
