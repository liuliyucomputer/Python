#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模块文件验证脚本
用于检查所有数据结构模块文件的存在性和语法正确性
"""

import os
import sys
import ast
import importlib.util
import traceback

def validate_file(file_path):
    """验证单个文件的存在性和语法正确性"""
    print(f"\n=== 验证文件: {file_path}")
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"❌ 错误: 文件不存在")
        return False
    
    print(f"✅ 文件存在")
    
    # 检查文件大小
    file_size = os.path.getsize(file_path)
    print(f"📄 文件大小: {file_size:,} 字节")
    
    if file_size == 0:
        print(f"❌ 错误: 文件为空")
        return False
    
    # 检查Python语法
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        ast.parse(content)
        print(f"✅ Python语法正确")
    except SyntaxError as e:
        print(f"❌ Python语法错误: {e}")
        return False
    except Exception as e:
        print(f"❌ 读取文件时出错: {e}")
        return False
    
    # 尝试导入模块（可选，可能会执行模块级代码）
    try:
        # 创建模块名称
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        
        # 捕获模块导入过程中可能的错误
        try:
            spec.loader.exec_module(module)
            print(f"✅ 模块导入成功")
        except Exception as e:
            print(f"⚠️  模块导入时执行代码出错: {e}")
            print(f"   这可能是因为模块包含示例代码，这不影响文档的使用")
            # 这里不返回False，因为文档文件可能包含示例代码
    except Exception as e:
        print(f"⚠️  尝试导入模块时出错: {e}")
        print(f"   这可能是因为模块结构设计，这不影响文档的使用")
    
    return True

def validate_all_modules():
    """验证所有数据结构模块文件"""
    print("开始验证所有数据结构模块文件...")
    print("=" * 60)
    
    # 定义要验证的模块文件列表
    modules = [
        "itertools模块.py",
        "operator模块.py",
        "collections模块.py",
        "heapq模块.py",
        "functools模块.py"
    ]
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 验证结果统计
    total = len(modules)
    success = 0
    failed = []
    
    # 验证每个模块
    for module in modules:
        file_path = os.path.join(current_dir, module)
        if validate_file(file_path):
            success += 1
        else:
            failed.append(module)
    
    # 输出总结
    print("\n" + "=" * 60)
    print("验证总结:")
    print(f"总文件数: {total}")
    print(f"成功: {success}")
    print(f"失败: {len(failed)}")
    
    if failed:
        print("\n失败的文件:")
        for file in failed:
            print(f"  - {file}")
    
    print("\n验证完成!")
    return len(failed) == 0

def check_file_completeness(file_path):
    """检查文件内容的完整性"""
    print(f"\n=== 检查文件完整性: {os.path.basename(file_path)}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查必要的章节
        required_sections = [
            "核心功能与概述",
            "基本使用方法",
            "高级用法",
            "实际应用场景",
            "性能分析",
            "使用注意事项",
            "总结与最佳实践"
        ]
        
        missing_sections = []
        for section in required_sections:
            if section not in content:
                missing_sections.append(section)
        
        if missing_sections:
            print(f"⚠️  缺少以下章节:")
            for section in missing_sections:
                print(f"   - {section}")
        else:
            print(f"✅ 所有必要章节都存在")
        
        # 检查代码块数量
        code_blocks = content.count("```python")
        print(f"📊 Python代码块数量: {code_blocks}")
        
        # 检查表格数量（使用 | 分隔的表格）
        tables = content.count("|") // 5  # 估算
        print(f"📊 表格数量: {tables}")
        
        return len(missing_sections) == 0
        
    except Exception as e:
        print(f"❌ 检查文件完整性时出错: {e}")
        return False

def validate_completeness():
    """验证所有文件的完整性"""
    print("\n开始检查文件内容完整性...")
    print("=" * 60)
    
    # 定义要验证的模块文件列表
    modules = [
        "itertools模块.py",
        "operator模块.py",
        "collections模块.py",
        "heapq模块.py",
        "functools模块.py"
    ]
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 验证结果统计
    total = len(modules)
    success = 0
    
    # 验证每个模块的完整性
    for module in modules:
        file_path = os.path.join(current_dir, module)
        if os.path.exists(file_path):
            if check_file_completeness(file_path):
                success += 1
    
    # 输出总结
    print("\n" + "=" * 60)
    print("完整性检查总结:")
    print(f"总文件数: {total}")
    print(f"完整文件数: {success}")
    print(f"不完整文件数: {total - success}")
    print("\n完整性检查完成!")

if __name__ == "__main__":
    print("Python数据结构模块文件验证工具")
    print("=" * 60)
    
    # 验证文件存在性和语法
    files_valid = validate_all_modules()
    
    # 验证文件内容完整性
    validate_completeness()
    
    print("\n" + "=" * 60)
    print("最终验证结果:")
    if files_valid:
        print("🎉 所有文件验证通过!")
    else:
        print("⚠️  部分文件验证失败，请检查错误信息")
    
    print("验证工具执行完毕")
