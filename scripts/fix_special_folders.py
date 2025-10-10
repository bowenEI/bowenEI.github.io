#!/usr/bin/env python3
import os
from pathlib import Path

blog_path = "/home/fourier/repos/bowenEI.github.io/content/blog"

def rename_special_folders():
    """Rename folders with special characters by listing them first"""
    blog_dir = Path(blog_path)
    
    print("Current blog folder contents:")
    all_dirs = [d for d in blog_dir.iterdir() if d.is_dir()]
    
    # Find folders that contain Chinese characters and need renaming
    need_rename = []
    for d in all_dirs:
        name = d.name
        if any(char in name for char in ['不忘初心', '世界民主', '孔乙己', '光头强']):
            need_rename.append(d)
            print(f"Found folder to rename: {repr(name)}")
    
    # Define the mapping (using the correct smart quotes)
    mapping = {
        '"不忘初心 一生一誓"——毕业生党员交流会': 'Never_Forget_Original_Intention_Graduate_Party_Member_Exchange',
        '"世界民主峰会"喜剧还是闹剧？': 'World_Democracy_Summit_Comedy_or_Farce', 
        '"孔乙己文学"现象的背后': 'Behind_the_Kong_Yiji_Literature_Phenomenon',
        '从"改变命运的"光头强体会什么才是真正的做自己': 'From_Bald_Qiang_Understand_What_is_Truly_Being_Yourself',
    }
    
    # Rename each folder
    renamed_count = 0
    for folder in need_rename:
        old_name = folder.name
        if old_name in mapping:
            new_name = mapping[old_name]
            new_path = folder.parent / new_name
            try:
                folder.rename(new_path)
                print(f"✓ Successfully renamed: {old_name} -> {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"✗ Error renaming {old_name}: {e}")
        else:
            print(f"? No mapping found for: {old_name}")
    
    print(f"\nRename complete! {renamed_count} folders were renamed.")

if __name__ == "__main__":
    rename_special_folders()