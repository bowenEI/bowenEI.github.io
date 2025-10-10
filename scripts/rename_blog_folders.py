#!/usr/bin/env python3
"""
批量重命名博客文件夹的脚本
将大写字母改为小写字母，下划线改为短横线
"""

import os
import re
import json
from pathlib import Path


def convert_folder_name(name):
    """
    将文件夹名称从大写+下划线格式转换为小写+短横线格式
    例如：LLM_Parallelism_Communication_Analysis -> llm-parallelism-communication-analysis
    """
    # 将下划线替换为短横线，然后转换为小写
    return name.replace('_', '-').lower()


def get_blog_folders(blog_dir):
    """获取所有博客文件夹（排除_index.md文件）"""
    folders = []
    for item in os.listdir(blog_dir):
        item_path = os.path.join(blog_dir, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
            folders.append(item)
    return sorted(folders)


def create_rename_mapping(folders):
    """创建重命名映射表"""
    mapping = {}
    for folder in folders:
        new_name = convert_folder_name(folder)
        if folder != new_name:  # 只有当名称确实需要改变时才加入映射
            mapping[folder] = new_name
    return mapping


def rename_folders(blog_dir, mapping, dry_run=True):
    """重命名文件夹"""
    results = []
    
    for old_name, new_name in mapping.items():
        old_path = os.path.join(blog_dir, old_name)
        new_path = os.path.join(blog_dir, new_name)
        
        if not os.path.exists(old_path):
            results.append(f"警告: 源文件夹不存在: {old_path}")
            continue
            
        if os.path.exists(new_path):
            results.append(f"警告: 目标文件夹已存在: {new_path}")
            continue
        
        if dry_run:
            results.append(f"[预览] {old_name} -> {new_name}")
        else:
            try:
                os.rename(old_path, new_path)
                results.append(f"✓ 成功重命名: {old_name} -> {new_name}")
            except Exception as e:
                results.append(f"✗ 重命名失败: {old_name} -> {new_name}, 错误: {str(e)}")
    
    return results


def main():
    # 博客目录路径
    blog_dir = "/home/foo/repos/bowenEI.github.io/content/blog"
    
    # 输出文件路径
    mapping_file = "/home/foo/repos/bowenEI.github.io/scripts/blog_rename_mapping.json"
    
    print("正在分析博客文件夹...")
    
    # 获取所有博客文件夹
    folders = get_blog_folders(blog_dir)
    print(f"找到 {len(folders)} 个文件夹")
    
    # 创建重命名映射
    mapping = create_rename_mapping(folders)
    print(f"需要重命名 {len(mapping)} 个文件夹")
    
    if not mapping:
        print("没有需要重命名的文件夹")
        return
    
    # 保存映射到文件
    with open(mapping_file, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
    print(f"映射表已保存到: {mapping_file}")
    
    # 预览重命名操作
    print("\n=== 重命名预览 ===")
    preview_results = rename_folders(blog_dir, mapping, dry_run=True)
    for result in preview_results:
        print(result)
    
    # 询问是否执行重命名
    print(f"\n即将重命名 {len(mapping)} 个文件夹，是否继续？(y/N): ", end="")
    # 为了脚本自动化，这里直接返回映射，不执行重命名
    print("脚本生成完成，请手动确认后执行重命名操作")
    
    return mapping


if __name__ == "__main__":
    mapping = main()