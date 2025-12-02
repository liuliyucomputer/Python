import os
import shutil
import datetime

def package_all_files():
    print("开始打包所有文件...")
    
    # 创建打包目录
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    package_dir = f"Python数据结构模块文档_{timestamp}"
    
    if not os.path.exists(package_dir):
        os.makedirs(package_dir)
    
    # 复制核心模块文件
    core_files = [
        "itertools模块.py",
        "operator模块.py",
        "collections模块.py",
        "heapq模块.py",
        "functools模块.py",
        "README.md",
        "使用指南.md"
    ]
    
    copied_count = 0
    for file in core_files:
        if os.path.exists(file):
            try:
                shutil.copy2(file, os.path.join(package_dir, file))
                copied_count += 1
                print(f"✅ 复制: {file}")
            except Exception as e:
                print(f"❌ 复制失败: {file}, 错误: {e}")
    
    # 复制Markdown版本
    md_files = [
        "itertools模块.md",
        "operator模块.md",
        "collections模块.md",
        "heapq模块.md",
        "functools模块.md"
    ]
    
    for file in md_files:
        if os.path.exists(file):
            try:
                shutil.copy2(file, os.path.join(package_dir, file))
                copied_count += 1
                print(f"✅ 复制: {file}")
            except Exception as e:
                print(f"❌ 复制失败: {file}, 错误: {e}")
    
    # 复制示例代码目录
    examples_dir = "examples"
    if os.path.exists(examples_dir) and os.path.isdir(examples_dir):
        try:
            shutil.copytree(examples_dir, os.path.join(package_dir, examples_dir))
            print(f"✅ 复制示例代码目录: {examples_dir}")
        except Exception as e:
            print(f"❌ 复制示例代码目录失败: {e}")
    
    print(f"\n打包完成！")
    print(f"生成的打包目录: {package_dir}")
    print(f"成功复制 {copied_count} 个文件")
    print("\n📋 打包内容包含:")
    print("  - 5个核心模块的Python源代码文件")
    print("  - 5个核心模块的Markdown文档")
    print("  - README.md 和 使用指南.md")
    print("  - 示例代码目录")
    
    print("\n🎉 Python数据结构模块文档包已准备就绪！")

if __name__ == "__main__":
    package_all_files()