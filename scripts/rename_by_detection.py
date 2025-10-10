#!/usr/bin/env python3
import os
from pathlib import Path

blog_path = "/home/fourier/repos/bowenEI.github.io/content/blog"

def rename_by_detection():
    """Detect and rename folders automatically"""
    blog_dir = Path(blog_path)
    
    # Get actual folder names
    actual_folders = {}
    for d in blog_dir.iterdir():
        if d.is_dir():
            name = d.name
            if '不忘初心' in name:
                actual_folders[name] = 'Never_Forget_Original_Intention_Graduate_Party_Member_Exchange'
            elif '世界民主' in name:
                actual_folders[name] = 'World_Democracy_Summit_Comedy_or_Farce'
            elif '孔乙己' in name:
                actual_folders[name] = 'Behind_the_Kong_Yiji_Literature_Phenomenon'
            elif '光头强' in name:
                actual_folders[name] = 'From_Bald_Qiang_Understand_What_is_Truly_Being_Yourself'
    
    print("Detected folders to rename:")
    for old, new in actual_folders.items():
        print(f"  {repr(old)} -> {new}")
    
    # Rename them
    renamed_count = 0
    for old_name, new_name in actual_folders.items():
        old_path = blog_dir / old_name
        new_path = blog_dir / new_name
        try:
            old_path.rename(new_path)
            print(f"✓ Successfully renamed: {old_name} -> {new_name}")
            renamed_count += 1
        except Exception as e:
            print(f"✗ Error renaming {old_name}: {e}")
    
    print(f"\nRename complete! {renamed_count} folders were renamed.")
    return actual_folders

if __name__ == "__main__":
    rename_by_detection()