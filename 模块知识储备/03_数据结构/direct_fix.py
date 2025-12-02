#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接修复Python模块文件的脚本
使用简单的方法修复语法问题
"""

import os
import re

def fix_file(file_path):
    """直接修复文件"""
    print(f"处理文件: {file_path}")
    
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 简单修复方法：将所有代码块标记为注释
        modified_lines = []
        in_code_block = False
        code_block_lines = []
        
        for i, line in enumerate(lines):
            if '```python' in line:
                in_code_block = True
                modified_lines.append(line)
                code_block_lines = []
            elif '```' in line and in_code_block:
                in_code_block = False
                # 检查代码块是否有语法问题（简单检查）
                code_content = ''.join(code_block_lines)
                triple_single_count = code_content.count("'''")
                triple_double_count = code_content.count('"""')
                
                # 确保三引号闭合
                if triple_single_count % 2 != 0:
                    modified_lines.append("'''  # 闭合未闭合的三引号\n")
                    print(f"  行 {i}: 添加闭合的单三引号")
                if triple_double_count % 2 != 0:
                    modified_lines.append('"""  # 闭合未闭合的双三引号\n')
                    print(f"  行 {i}: 添加闭合的双三引号")
                
                # 添加原始代码块的行
                modified_lines.extend(code_block_lines)
                modified_lines.append(line)
            elif in_code_block:
                # 替换特殊字符
                line = line.replace('∞', 'float("inf")')
                line = line.replace('≤', '<=')
                line = line.replace('≥', '>=')
                code_block_lines.append(line)
            else:
                # 非代码块部分
                # 替换反引号为双引号
                line = line.replace('`', '"')
                modified_lines.append(line)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)
        
        print(f"✅ 文件修复完成")
        return True
        
    except Exception as e:
        print(f"❌ 处理文件时出错: {e}")
        return False

def test_syntax(file_path):
    """测试文件是否可以成功导入"""
    try:
        # 创建一个临时测试脚本来尝试导入
        test_script = f"""
import sys
import io
import traceback

sys.stdout = io.StringIO()
sys.stderr = io.StringIO()

try:
    with open(r'{file_path}', 'r', encoding='utf-8') as f:
        code = f.read()
    # 尝试编译代码
    compile(code, '{file_path}', 'exec')
    print("语法检查通过")
except SyntaxError as e:
    print(f"语法错误: {e}")
    print(f"错误位置: 行 {e.lineno}, 列 {e.offset}")
    print(f"错误信息: {e.text}")
except Exception as e:
    print(f"其他错误: {e}")
"""
        
        test_script_path = file_path + '.test.py'
        with open(test_script_path, 'w', encoding='utf-8') as f:
            f.write(test_script)
        
        # 运行测试脚本
        import subprocess
        result = subprocess.run(
            ['python', test_script_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # 删除临时文件
        os.remove(test_script_path)
        
        if result.returncode == 0:
            output = result.stdout.strip()
            print(f"测试结果: {output}")
            return "语法检查通过" in output
        else:
            print(f"测试失败: {result.stderr.strip()}")
            return False
            
    except Exception as e:
        print(f"测试脚本执行错误: {e}")
        return False

def main():
    """主函数"""
    print("Python模块文件直接修复工具")
    print("=" * 50)
    
    # 定义要处理的模块文件列表
    modules = [
        "itertools模块.py",
        "operator模块.py",
        "collections模块.py",
        "heapq模块.py",
        "functools模块.py"
    ]
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 处理每个文件
    for module in modules:
        file_path = os.path.join(current_dir, module)
        if os.path.exists(file_path):
            print(f"\n=== 处理 {module} ===")
            fix_file(file_path)
            print("测试语法...")
            test_syntax(file_path)
        else:
            print(f"❌ 文件不存在: {file_path}")
    
    print("\n" + "=" * 50)
    print("所有文件处理完成!")

if __name__ == "__main__":
    main()
