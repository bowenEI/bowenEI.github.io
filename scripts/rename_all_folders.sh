#!/bin/bash

# 批量重命名博客文件夹的shell脚本
# 将大写字母改为小写字母，下划线改为短横线

cd /home/foo/repos/bowenEI.github.io/content/blog

echo "开始重命名博客文件夹..."

# 重命名函数
rename_folder() {
    local old_name="$1"
    local new_name=$(echo "$old_name" | tr '[:upper:]' '[:lower:]' | tr '_' '-')
    
    if [ "$old_name" != "$new_name" ] && [ -d "$old_name" ]; then
        echo "重命名: $old_name -> $new_name"
        mv "$old_name" "$new_name"
    fi
}

# 获取所有文件夹并重命名
for folder in */; do
    folder_name="${folder%/}"  # 移除末尾的斜杠
    if [ -d "$folder_name" ]; then
        rename_folder "$folder_name"
    fi
done

echo "重命名完成！"