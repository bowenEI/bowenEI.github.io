import sys
import hashlib
import os


def rename_file_with_md5(file_path):
    # 打开文件并计算MD5值
    with open(file_path, "rb") as file:
        data = file.read()
        md5_hash = hashlib.md5(data).hexdigest()

    # 获取文件的扩展名
    folder_path, file_name = os.path.split(file_path)

    # 构建新的文件名
    new_file_name = md5_hash + "." + file_name.split(".")[-1]
    new_file_path = os.path.join(folder_path, new_file_name)

    # 重命名文件
    os.rename(file_path, new_file_path)


# 获取命令行参数，忽略脚本文件名
args = sys.argv[1:]

# 遍历所有传入的文件路径
for file_path in args:
    # 重命名文件
    rename_file_with_md5(file_path)
