#!/usr/bin/env python3
"""
更新博客文章中的链接引用脚本
根据重命名映射更新所有相对链接
"""

import os
import re
import json
from pathlib import Path


def load_rename_mapping(mapping_file):
    """加载重命名映射表"""
    with open(mapping_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def update_links_in_file(file_path, mapping, dry_run=True):
    """更新单个文件中的链接"""
    changes = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 查找相对链接模式：../文件夹名/
        for old_name, new_name in mapping.items():
            # 匹配 ../老文件夹名/ 的模式
            pattern = r'\.\./' + re.escape(old_name) + r'/'
            replacement = '../' + new_name + '/'
            
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                changes.append(f"  {old_name} -> {new_name}")
        
        if changes and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return changes
    
    except Exception as e:
        return [f"错误: {str(e)}"]


def find_markdown_files(root_dir):
    """查找所有markdown文件"""
    markdown_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files


def update_all_links(blog_dir, mapping, dry_run=True):
    """更新所有文件中的链接"""
    markdown_files = find_markdown_files(blog_dir)
    results = []
    
    for file_path in markdown_files:
        rel_path = os.path.relpath(file_path, blog_dir)
        changes = update_links_in_file(file_path, mapping, dry_run)
        
        if changes:
            status = "[预览]" if dry_run else "✓"
            results.append(f"{status} {rel_path}:")
            results.extend(changes)
            results.append("")
    
    return results


def main():
    # 博客目录路径
    blog_dir = "/home/foo/repos/bowenEI.github.io/content/blog"
    
    # 映射文件路径
    mapping_file = "/home/foo/repos/bowenEI.github.io/scripts/blog_rename_mapping.json"
    
    print("正在加载重命名映射...")
    
    # 加载映射表
    if not os.path.exists(mapping_file):
        print(f"错误: 映射文件不存在: {mapping_file}")
        return
    
    mapping = load_rename_mapping(mapping_file)
    print(f"已加载 {len(mapping)} 个重命名映射")
    
    # 预览链接更新
    print("\n=== 链接更新预览 ===")
    preview_results = update_all_links(blog_dir, mapping, dry_run=True)
    
    if not preview_results:
        print("没有找到需要更新的链接")
    else:
        for result in preview_results[:20]:  # 只显示前20行
            print(result)
        if len(preview_results) > 20:
            print(f"... 还有 {len(preview_results) - 20} 行")
    
    print(f"\n脚本生成完成，发现 {len([r for r in preview_results if r.startswith('[预览]')])} 个文件需要更新链接")
    
    return len(preview_results)


if __name__ == "__main__":
    main()