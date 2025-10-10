#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

# Remaining folders that need to be renamed
remaining_folders = {
    '"不忘初心 一生一誓"——毕业生党员交流会': 'Never_Forget_Original_Intention_Graduate_Party_Member_Exchange',
    '"世界民主峰会"喜剧还是闹剧？': 'World_Democracy_Summit_Comedy_or_Farce',
    '"孔乙己文学"现象的背后': 'Behind_the_Kong_Yiji_Literature_Phenomenon',
    '从"改变命运的"光头强体会什么才是真正的做自己': 'From_Bald_Qiang_Understand_What_is_Truly_Being_Yourself',
}

blog_path = "/home/fourier/repos/bowenEI.github.io/content/blog"

def rename_remaining_folders():
    """Rename the remaining folders with special characters"""
    blog_dir = Path(blog_path)
    renamed_count = 0
    
    print("Renaming remaining folders with special characters...")
    
    for old_name, new_name in remaining_folders.items():
        old_path = blog_dir / old_name
        new_path = blog_dir / new_name
        
        if old_path.exists() and old_path.is_dir():
            try:
                old_path.rename(new_path)
                print(f"✓ Successfully renamed: {old_name} -> {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"✗ Error renaming {old_name}: {e}")
        else:
            print(f"? Folder not found: {old_name}")
    
    print(f"\nRename complete! {renamed_count} folders were renamed.")
    return renamed_count > 0

if __name__ == "__main__":
    rename_remaining_folders()