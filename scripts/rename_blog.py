import os
import re
import hashlib
import shutil

cur_path = os.path.dirname(os.path.abspath(__file__))

# 定义 blog 文件夹路径
blog_folder = os.path.join(cur_path, '../content/blog')

# 定义正则表达式模式
pattern = re.compile(r'title:\s*"(.*?)"')

# 遍历 blog 文件夹下的所有子文件夹
for root, dirs, files in os.walk(blog_folder):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            try:
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 使用正则表达式匹配 title 内容
                match = pattern.search(content)
                if match:
                    title = match.group(1)
                    # 计算 title 的 MD5 值
                    md5_hash = hashlib.md5(title.encode('utf-8')).hexdigest()
                    
                    # 获取当前文件夹路径
                    current_folder = os.path.dirname(file_path)
                    parent_folder = os.path.dirname(current_folder)
                    new_folder_name = os.path.join(parent_folder, md5_hash)

                    if current_folder != new_folder_name:
                        # 重命名文件夹
                        shutil.move(current_folder, new_folder_name)
                        print(f"已将文件夹 {current_folder} 重命名为 {new_folder_name}")
                    else:
                        print(f"{current_folder} 无需重命名")
            except Exception as e:
                print(f"处理文件 {file_path} 时出错: {e}")
