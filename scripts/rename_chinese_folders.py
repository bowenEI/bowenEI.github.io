#!/usr/bin/env python3
"""
Script to rename Chinese blog folder names to English equivalents
with underscores instead of spaces and punctuation.
"""

import os
import re
import shutil
from pathlib import Path

# Function words that should remain lowercase (except when they're the first word)
FUNCTION_WORDS = {
    'a', 'an', 'the',  # articles
    'and', 'or', 'but', 'nor',  # conjunctions
    'for', 'on', 'at', 'to', 'in', 'of', 'by', 'with', 'from', 'up', 'about', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'between', 'among', 'against',  # prepositions
    'is', 'was', 'are', 'were', 'be', 'been', 'being',  # auxiliary verbs
}

def to_title_case(text):
    """Convert text to title case, keeping function words lowercase except when first"""
    words = text.split('_')
    title_words = []
    
    for i, word in enumerate(words):
        if i == 0 or word.lower() not in FUNCTION_WORDS:
            title_words.append(word.capitalize())
        else:
            title_words.append(word.lower())
    
    return '_'.join(title_words)

# Mapping of Chinese folder names to English equivalents (will be converted to title case)
folder_mapping_raw = {
    '"不忘初心 一生一誓"——毕业生党员交流会': 'never_forget_original_intention_graduate_party_member_exchange',
    '"世界民主峰会"喜剧还是闹剧？': 'world_democracy_summit_comedy_or_farce',
    '"孔乙己文学"现象的背后': 'behind_the_kong_yiji_literature_phenomenon',
    '【跨年演讲】温铁军：为什么我对中国2022年的经济前景保持乐观？': 'new_year_speech_wen_tiejun_why_optimistic_about_china_2022_economy',
    '东方之美：谈谈中国人的审美自信': 'eastern_beauty_chinese_aesthetic_confidence',
    '中国社会各阶级分析': 'analysis_of_social_classes_in_china',
    '为什么会有人说辩证法是错误的？': 'why_do_people_say_dialectics_is_wrong',
    '从"改变命运的"光头强体会什么才是真正的做自己': 'from_bald_qiang_understand_what_is_truly_being_yourself',
    '从公司到国家：美国制度困局的历史解释': 'from_company_to_nation_historical_explanation_of_american_institutional_dilemma',
    '从圆锥曲线到二次型': 'from_conic_sections_to_quadratic_forms',
    '从精神上站立起来': 'stand_up_spiritually',
    '八次危机：中国的真实经验': 'eight_crises_china_real_experience',
    '分块矩阵的乘法': 'block_matrix_multiplication',
    '加速行业智能化 共赢智能化未来': 'accelerate_industry_intelligence_win_win_intelligent_future',
    '图解 Flash Attention': 'illustrated_flash_attention',
    '在服务器上部署 Overleaf': 'deploying_overleaf_on_server',
    '大模型的参数量及其计算访存开销的理论分析': 'theoretical_analysis_of_large_model_parameters_and_computational_memory_overhead',
    '并行计算集合通信初步': 'introduction_to_parallel_computing_collective_communication',
    '思想殖民——美国认知战的手段、根源及国际危害': 'ideological_colonization_means_roots_and_international_harm_of_american_cognitive_warfare',
    '我的马克思主义爱情观': 'my_marxist_view_of_love',
    '挑战 2021 年高考数学全国乙卷压轴大题': 'challenge_2021_gaokao_math_national_paper_b_final_problem',
    '挑战 2022 年高考全国乙卷数学压轴大题': 'challenge_2022_gaokao_national_paper_b_math_final_problem',
    '挑战 2023 年高考全国乙卷数学压轴大题': 'challenge_2023_gaokao_national_paper_b_math_final_problem',
    '挑战 2024 年考研数学（一）': 'challenge_2024_graduate_entrance_exam_math_one',
    '挑战 2024 年高考数学新课标 I 卷压轴大题': 'challenge_2024_gaokao_math_new_curriculum_standard_i_final_problem',
    '挑战 2025 年高考数学新课标 I 卷压轴大题': 'challenge_2025_gaokao_math_new_curriculum_standard_i_final_problem',
    '沉痛悼念杂交水稻之父袁隆平院士': 'mourning_yuan_longping_father_of_hybrid_rice',
    '深度学习中的矩阵求导基础': 'matrix_calculus_fundamentals_in_deep_learning',
    '相关性和因果性': 'correlation_and_causality',
    '破解 Synthesia': 'cracking_synthesia',
    '社会学的邀请': 'invitation_to_sociology',
    '系统爆破西方话语体系': 'systematically_dismantling_western_discourse_system',
    '美式反恐 越反越恐': 'american_counter_terrorism_more_terror_with_more_counter',
    '美西方民主的政治责任缺位': 'absence_of_political_responsibility_in_western_democracy',
    '论男女两性的解放': 'on_the_liberation_of_both_sexes',
    '调和级数的前 n 项和': 'sum_of_first_n_terms_of_harmonic_series',
    '郑强与杨澜对话中国教育': 'zheng_qiang_and_yang_lan_dialogue_on_chinese_education',
    'Dirichlet 积分': 'dirichlet_integral'
}

# Convert to title case
folder_mapping = {key: to_title_case(value) for key, value in folder_mapping_raw.items()}

def rename_folders(blog_path):
    """Rename folders according to the mapping"""
    blog_dir = Path(blog_path)
    renamed_folders = {}
    
    print("Starting folder renaming process...")
    
    for old_name, new_name in folder_mapping.items():
        old_path = blog_dir / old_name
        new_path = blog_dir / new_name
        
        if old_path.exists() and old_path.is_dir():
            print(f"Renaming: {old_name} -> {new_name}")
            try:
                old_path.rename(new_path)
                renamed_folders[old_name] = new_name
                print(f"✓ Successfully renamed: {old_name}")
            except Exception as e:
                print(f"✗ Error renaming {old_name}: {e}")
        else:
            print(f"? Folder not found: {old_name}")
    
    return renamed_folders

def find_and_update_links(content_path, renamed_folders):
    """Find and update any links that reference the renamed folders"""
    print("\nSearching for links to update...")
    
    content_dir = Path(content_path)
    updated_files = []
    
    # Search for markdown files that might contain links
    for md_file in content_dir.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Update links for each renamed folder
            for old_name, new_name in renamed_folders.items():
                # Escape special characters in old_name for regex
                escaped_old_name = re.escape(old_name)
                
                # Update various link formats using string replacement instead of regex
                patterns_and_replacements = [
                    (f'](/blog/{old_name})', f'](/blog/{new_name})'),
                    (f'](../blog/{old_name})', f'](../blog/{new_name})'),
                    (f'](../../blog/{old_name})', f'](../../blog/{new_name})'),
                    (f'](/blog/{old_name}/', f'](/blog/{new_name}/'),
                    (f'](../blog/{old_name}/', f'](../blog/{new_name}/'),
                    (f'](../../blog/{old_name}/', f'](../../blog/{new_name}/'),
                ]
                
                for pattern, replacement in patterns_and_replacements:
                    content = content.replace(pattern, replacement)
            
            # Save if content changed
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated_files.append(str(md_file))
                print(f"✓ Updated links in: {md_file}")
        
        except Exception as e:
            print(f"✗ Error processing {md_file}: {e}")
    
    return updated_files

def main():
    blog_path = "/home/fourier/repos/bowenEI.github.io/content/blog"
    content_path = "/home/fourier/repos/bowenEI.github.io/content"
    
    print("=" * 60)
    print("Blog Folder Renaming Script")
    print("=" * 60)
    
    # Step 1: Rename folders
    renamed_folders = rename_folders(blog_path)
    
    if not renamed_folders:
        print("No folders were renamed.")
        return
    
    print(f"\nSuccessfully renamed {len(renamed_folders)} folders:")
    for old, new in renamed_folders.items():
        print(f"  {old} -> {new}")
    
    # Step 2: Update links
    updated_files = find_and_update_links(content_path, renamed_folders)
    
    if updated_files:
        print(f"\nUpdated links in {len(updated_files)} files:")
        for file in updated_files:
            print(f"  {file}")
    else:
        print("\nNo link updates were needed.")
    
    print("\n" + "=" * 60)
    print("Renaming process completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()