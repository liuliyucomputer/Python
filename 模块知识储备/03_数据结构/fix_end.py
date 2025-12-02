import os

def fix_file_end(file_path):
    print(f"修复文件末尾: {file_path}")
    
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 在文件末尾添加闭合标记
        # 添加各种可能需要的闭合标记
        fixers = [
            '```\n',  # 代码块闭合
            '"""\n', # 三引号闭合
            "'''\n",   # 单引号三引号闭合
            '"\n',    # 双引号闭合
            "'\n"     # 单引号闭合
        ]
        
        for fixer in fixers:
            # 先检查是否已经有这些标记
            if not content.endswith(fixer):
                content += fixer
        
        # 保存文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} 修复完成")
        return True
    except Exception as e:
        print(f"❌ 修复失败: {e}")
        return False

def fix_all_files():
    modules = [
        "itertools模块.py",
        "operator模块.py",
        "collections模块.py",
        "heapq模块.py",
        "functools模块.py"
    ]
    
    success_count = 0
    for module in modules:
        file_path = os.path.join(os.getcwd(), module)
        if os.path.exists(file_path):
            if fix_file_end(file_path):
                success_count += 1
        else:
            print(f"❌ 文件不存在: {file_path}")
    
    print(f"\n修复完成！成功修复: {success_count}/{len(modules)}")

if __name__ == "__main__":
    fix_all_files()