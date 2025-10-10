#!/usr/bin/env python3
"""
Search for and update links to renamed blog folders
"""

import os
import re
from pathlib import Path

# All the renames that happened
all_renames = {
    # Chinese to English renames
    '【跨年演讲】温铁军：为什么我对中国2022年的经济前景保持乐观？': 'New_Year_Speech_Wen_Tiejun_Why_Optimistic_about_China_2022_Economy',
    '东方之美：谈谈中国人的审美自信': 'Eastern_Beauty_Chinese_Aesthetic_Confidence',
    '中国社会各阶级分析': 'Analysis_of_Social_Classes_in_China',
    '为什么会有人说辩证法是错误的？': 'Why_Do_People_Say_Dialectics_is_Wrong',
    '从公司到国家：美国制度困局的历史解释': 'From_Company_to_Nation_Historical_Explanation_of_American_Institutional_Dilemma',
    '从圆锥曲线到二次型': 'From_Conic_Sections_to_Quadratic_Forms',
    '从精神上站立起来': 'Stand_up_Spiritually',
    '八次危机：中国的真实经验': 'Eight_Crises_China_Real_Experience',
    '分块矩阵的乘法': 'Block_Matrix_Multiplication',
    '加速行业智能化 共赢智能化未来': 'Accelerate_Industry_Intelligence_Win_Win_Intelligent_Future',
    '图解 Flash Attention': 'Illustrated_Flash_Attention',
    '在服务器上部署 Overleaf': 'Deploying_Overleaf_on_Server',
    '大模型的参数量及其计算访存开销的理论分析': 'Theoretical_Analysis_of_Large_Model_Parameters_and_Computational_Memory_Overhead',
    '并行计算集合通信初步': 'Introduction_to_Parallel_Computing_Collective_Communication',
    '思想殖民——美国认知战的手段、根源及国际危害': 'Ideological_Colonization_Means_Roots_and_International_Harm_of_American_Cognitive_Warfare',
    '我的马克思主义爱情观': 'My_Marxist_View_of_Love',
    '挑战 2021 年高考数学全国乙卷压轴大题': 'Challenge_2021_Gaokao_Math_National_Paper_B_Final_Problem',
    '挑战 2022 年高考全国乙卷数学压轴大题': 'Challenge_2022_Gaokao_National_Paper_B_Math_Final_Problem',
    '挑战 2023 年高考全国乙卷数学压轴大题': 'Challenge_2023_Gaokao_National_Paper_B_Math_Final_Problem',
    '挑战 2024 年考研数学（一）': 'Challenge_2024_Graduate_Entrance_Exam_Math_One',
    '挑战 2024 年高考数学新课标 I 卷压轴大题': 'Challenge_2024_Gaokao_Math_New_Curriculum_Standard_I_Final_Problem',
    '挑战 2025 年高考数学新课标 I 卷压轴大题': 'Challenge_2025_Gaokao_Math_New_Curriculum_Standard_I_Final_Problem',
    '沉痛悼念杂交水稻之父袁隆平院士': 'Mourning_Yuan_Longping_Father_of_Hybrid_Rice',
    '深度学习中的矩阵求导基础': 'Matrix_Calculus_Fundamentals_in_Deep_Learning',
    '相关性和因果性': 'Correlation_and_Causality',
    '破解 Synthesia': 'Cracking_Synthesia',
    '社会学的邀请': 'Invitation_to_Sociology',
    '系统爆破西方话语体系': 'Systematically_Dismantling_Western_Discourse_System',
    '美式反恐 越反越恐': 'American_Counter_Terrorism_More_Terror_with_More_Counter',
    '美西方民主的政治责任缺位': 'Absence_of_Political_Responsibility_in_Western_Democracy',
    '论男女两性的解放': 'On_the_Liberation_of_Both_Sexes',
    '调和级数的前 n 项和': 'Sum_of_First_N_Terms_of_Harmonic_Series',
    '郑强与杨澜对话中国教育': 'Zheng_Qiang_and_Yang_Lan_Dialogue_on_Chinese_Education',
    'Dirichlet 积分': 'Dirichlet_Integral',
    
    # Special character folder renames
    '"不忘初心 一生一誓"——毕业生党员交流会': 'Never_Forget_Original_Intention_Graduate_Party_Member_Exchange',
    '"世界民主峰会"喜剧还是闹剧？': 'World_Democracy_Summit_Comedy_or_Farce',
    '"孔乙己文学"现象的背后': 'Behind_the_Kong_Yiji_Literature_Phenomenon',
    '从"改变命运的"光头强体会什么才是真正的做自己': 'From_Bald_Qiang_Understand_What_is_Truly_Being_Yourself',
    
    # English folder renames
    'A Survey of Recent Advances in Edge-Computing-Powered Artificial Intelligence of Things': 'A_Survey_of_Recent_Advances_in_Edge_Computing_Powered_Artificial_Intelligence_of_Things',
    'An Image is Worth 16x16 Words_ Transformers for Image Recognition at Scale': 'An_Image_is_Worth_16x16_Words_Transformers_for_Image_Recognition_at_Scale',
    'Attention Is All You Need': 'Attention_Is_All_You_Need',
    'Classification of Computation Offloading': 'Classification_of_Computation_Offloading',
    'Cloud Computing Architecture': 'Cloud_Computing_Architecture',
    'Edge Intelligence_ Architectures_ Challenges_ and Applications': 'Edge_Intelligence_Architectures_Challenges_and_Applications',
    'How to Read a Paper': 'How_to_Read_a_Paper',
    'Nonviolent Communication': 'Nonviolent_Communication',
    'Towards Efficient Generative Large Language Model Serving_ A Survey From Algorithms to Systems': 'Towards_Efficient_Generative_Large_Language_Model_Serving_A_Survey_From_Algorithms_to_Systems',
    'Types of Transition Words and Phrases in Academic Writing': 'Types_of_Transition_Words_and_Phrases_in_Academic_Writing',
}

def search_and_update_links():
    """Search for links in all markdown files and update them"""
    content_dir = Path("/home/fourier/repos/bowenEI.github.io/content")
    updated_files = []
    
    print("Searching for files with links to update...")
    
    # Search all markdown files
    for md_file in content_dir.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            changes_made = []
            
            # Update links for each renamed folder
            for old_name, new_name in all_renames.items():
                # URL encode old_name for potential URL usage
                old_name_url = old_name.replace(' ', '%20')
                
                # Different possible link patterns
                patterns_and_replacements = [
                    # Standard relative links
                    (f'](/blog/{old_name})', f'](/blog/{new_name})'),
                    (f'](../blog/{old_name})', f'](../blog/{new_name})'),
                    (f'](../../blog/{old_name})', f'](../../blog/{new_name})'),
                    (f'](/blog/{old_name}/', f'](/blog/{new_name}/'),
                    (f'](../blog/{old_name}/', f'](../blog/{new_name}/'),
                    (f'](../../blog/{old_name}/', f'](../../blog/{new_name}/'),
                    
                    # URL encoded versions
                    (f'](/blog/{old_name_url})', f'](/blog/{new_name})'),
                    (f'](../blog/{old_name_url})', f'](../blog/{new_name})'),
                    (f'](../../blog/{old_name_url})', f'](../../blog/{new_name})'),
                    (f'](/blog/{old_name_url}/', f'](/blog/{new_name}/'),
                    (f'](../blog/{old_name_url}/', f'](../blog/{new_name}/'),
                    (f'](../../blog/{old_name_url}/', f'](../../blog/{new_name}/'),
                    
                    # Direct text references that might be folder names
                    (f'blog/{old_name}', f'blog/{new_name}'),
                    (f'blog/{old_name}/', f'blog/{new_name}/'),
                ]
                
                for pattern, replacement in patterns_and_replacements:
                    if pattern in content:
                        content = content.replace(pattern, replacement)
                        changes_made.append(f"  {pattern} -> {replacement}")
            
            # Save if content changed
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated_files.append(str(md_file))
                print(f"✓ Updated links in: {md_file}")
                for change in changes_made:
                    print(change)
                print()
        
        except Exception as e:
            print(f"✗ Error processing {md_file}: {e}")
    
    return updated_files

def main():
    print("=" * 60)
    print("Link Update Script")
    print("=" * 60)
    
    updated_files = search_and_update_links()
    
    if updated_files:
        print(f"\nUpdated links in {len(updated_files)} files:")
        for file in updated_files:
            print(f"  {file}")
    else:
        print("\nNo link updates were needed.")
    
    print("\n" + "=" * 60)
    print("Link update process completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()