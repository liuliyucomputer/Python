import os
import ast

def fix_syntax(file_path):
    print(f"尝试修复: {file_path}")
    
    # 读取文件内容
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"读取失败: {e}")
        return False
    
    # 尝试解析语法，如果失败，添加足够的引号来闭合可能的字符串
    try:
        ast.parse(content)
        print(f"  语法已经正确")
        return True
    except SyntaxError as e:
        print(f"  发现语法错误: {e}")
        
        # 简单修复：统计单引号和双引号数量
        single_quotes = content.count("'")
        double_quotes = content.count('"')
        
        # 如果数量为奇数，添加一个闭合引号
        fixed = False
        if single_quotes % 2 != 0:
            content += "'"
            fixed = True
            print(f"  添加了单引号闭合")
        if double_quotes % 2 != 0:
            content += '"'
            fixed = True
            print(f"  添加了双引号闭合")
        
        # 再次尝试解析
        if fixed:
            try:
                ast.parse(content)
                print(f"  语法修复成功")
                # 保存修复后的文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
            except:
                print(f"  简单修复失败")
        
        # 如果简单修复失败，尝试添加多个闭合引号
        for i in range(1, 10):
            try:
                test_content = content + '"' * i + "'" * i
                ast.parse(test_content)
                print(f"  添加{i}个双引号和{i}个单引号后修复成功")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(test_content)
                return True
            except:
                pass
    
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
            if fix_syntax(file_path):
                success_count += 1
        else:
            print(f"文件不存在: {file_path}")
    
    print(f"\n修复完成！成功修复: {success_count}/{len(modules)}")

if __name__ == "__main__":
    fix_all_files()