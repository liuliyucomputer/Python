#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全角字符修复脚本
用于将Python文件中的全角字符替换为半角字符
"""

import os
import re

def fix_fullwidth_chars(file_path):
    """修复文件中的全角字符"""
    print(f"处理文件: {file_path}")
    
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 定义全角字符到半角字符的映射
        full_to_half = {
            '（': '(', '）': ')',  # 括号
            '，': ',', '。': '.',  # 标点
            '；': ';', '：': ':',  # 冒号分号
            '！': '!', '？': '?',  # 感叹号问号
            '”': '"', '“': '"',  # 引号
            '’': "'", '‘': "'",  # 单引号
            '【': '[', '】': ']',  # 方括号
            '《': '<', '》': '>',  # 书名号
            '、': ',',  # 顿号
            '～': '~',  # 波浪号
            '—': '-',  # 破折号
            '…': '...',  # 省略号
            '　': ' ',  # 全角空格
        }
        
        # 替换全角字符
        modified = content
        changes = 0
        
        for full, half in full_to_half.items():
            count = modified.count(full)
            if count > 0:
                modified = modified.replace(full, half)
                changes += count
                print(f"  替换 '{full}' -> '{half}': {count} 处")
        
        # 检查是否有变化
        if changes > 0:
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified)
            print(f"✅ 文件修复完成，替换了 {changes} 处全角字符")
        else:
            print(f"✅ 文件无需修复，未发现全角字符")
        
        return changes
        
    except Exception as e:
        print(f"❌ 处理文件时出错: {e}")
        return -1

def main():
    """主函数"""
    print("Python文件全角字符修复工具")
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
    total_changes = 0
    for module in modules:
        file_path = os.path.join(current_dir, module)
        if os.path.exists(file_path):
            changes = fix_fullwidth_chars(file_path)
            if changes >= 0:
                total_changes += changes
        else:
            print(f"❌ 文件不存在: {file_path}")
    
    # 输出总结
    print("\n" + "=" * 50)
    print(f"修复总结: 总共替换了 {total_changes} 处全角字符")
    print("修复完成!")

if __name__ == "__main__":
    main()
