#!/usr/bin/env python3
import os
import re
import shutil
import unicodedata
import string

# 获取脚本所在目录
cur_path = os.path.dirname(os.path.abspath(__file__))

# 定义blog文件夹路径
blog_folder = os.path.join(cur_path, '../content/blog')

# 定义正则表达式模式匹配title字段
pattern = re.compile(r'title:\s*"(.*?)"')

# 定义有效的文件名字符
valid_chars = set(string.ascii_letters + string.digits + ' ._-' + ''.join(chr(c) for c in range(0x4e00, 0x9fff)))

# 用于规范化文件夹名的函数
def sanitize_folder_name(name):
    # 移除首尾空格
    name = name.strip()
    # 替换无效字符为下划线
    sanitized = ''.join(c if c in valid_chars else '_' for c in name)
    # 移除多余的下划线
    sanitized = re.sub(r'_+', '_', sanitized)
    # 确保文件夹名不为空
    if not sanitized:
        sanitized = 'unnamed'
    return sanitized

# 用于处理重名的函数
def get_unique_folder_name(base_name, parent_folder):
    counter = 1
    unique_name = base_name
    while os.path.exists(os.path.join(parent_folder, unique_name)):
        unique_name = f"{base_name}_{counter}"
        counter += 1
    return unique_name

# 遍历blog文件夹下的所有子文件夹
def rename_blog_folders():
    # 获取blog文件夹下的所有子文件夹
    subfolders = [f for f in os.listdir(blog_folder) if os.path.isdir(os.path.join(blog_folder, f)) and f != '_index.md']
    
    # 遍历每个子文件夹
    for folder in subfolders:
        folder_path = os.path.join(blog_folder, folder)
        index_file = os.path.join(folder_path, 'index.md')
        
        # 检查index.md文件是否存在
        if os.path.exists(index_file):
            try:
                # 读取index.md文件内容
                with open(index_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 匹配title字段
                match = pattern.search(content)
                if match:
                    title = match.group(1)
                    # 规范化文件夹名
                    new_folder_name = sanitize_folder_name(title)
                    
                    # 如果文件夹名已经是基于title的，则跳过
                    if folder == new_folder_name:
                        print(f"文件夹 {folder} 已经是正确的名称，无需重命名")
                        continue
                    
                    # 获取唯一的文件夹名
                    unique_folder_name = get_unique_folder_name(new_folder_name, blog_folder)
                    
                    # 构建新的文件夹路径
                    new_folder_path = os.path.join(blog_folder, unique_folder_name)
                    
                    # 重命名文件夹
                    shutil.move(folder_path, new_folder_path)
                    print(f"已将文件夹 {folder} 重命名为 {unique_folder_name}")
                else:
                    print(f"在文件夹 {folder} 的index.md文件中未找到title字段")
            except Exception as e:
                print(f"处理文件夹 {folder} 时出错: {e}")
        else:
            print(f"文件夹 {folder} 中未找到index.md文件")

if __name__ == "__main__":
    print("开始重命名blog文件夹...")
    rename_blog_folders()
    print("重命名完成！")