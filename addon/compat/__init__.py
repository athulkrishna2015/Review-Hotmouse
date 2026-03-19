from typing import TYPE_CHECKING
from .v1 import v1_compat

def compat(prev_version_str: str) -> None:
    """Executes code for compatability from older versions."""
    if prev_version_str == "-1.-1":
        return
    
    # Simple version comparison for v1
    try:
        parts = prev_version_str.split(".")
        major = int(parts[0])
        if major < 2:
            print("Review Hotmouse: Running v1_compat()")
            v1_compat()
    except (ValueError, IndexError):
        pass
