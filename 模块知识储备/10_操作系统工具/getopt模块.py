#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
getopt模块 - 命令行参数解析

getopt模块提供了C语言风格的命令行参数解析功能。

主要功能包括：
- 解析短选项（如-a, -b）
- 解析长选项（如--help, --version）
- 处理选项参数
- 支持选项和非选项参数混合

使用场景：
- 命令行工具开发
- 脚本参数解析
- 简单的命令行界面

官方文档：https://docs.python.org/3/library/getopt.html
"""

import getopt
import sys

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. getopt模块基本介绍")
print("=" * 50)
print("getopt模块用于解析命令行参数")
print("提供了C语言风格的参数解析功能")
print("支持短选项和长选项")
print("适合简单的命令行参数解析")

# ===========================
# 2. 基本用法
# ===========================
print("\n" + "=" * 50)
print("2. 基本用法")
print("=" * 50)

# 示例：解析命令行参数
def parse_args_example():
    """解析命令行参数示例"""
    print("原始命令行参数:", sys.argv)
    
    # 定义短选项字符串（:表示需要参数）
    short_options = "hu:f:"
    
    # 定义长选项列表（=表示需要参数）
    long_options = ["help", "url=", "file=", "verbose"]
    
    try:
        # 解析命令行参数
        opts, args = getopt.getopt(sys.argv[1:], short_options, long_options)
        
        print(f"解析后的选项: {opts}")
        print(f"非选项参数: {args}")
        
        # 处理选项
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("显示帮助信息")
            elif opt in ("-u", "--url"):
                print(f"URL选项值: {arg}")
            elif opt in ("-f", "--file"):
                print(f"文件选项值: {arg}")
            elif opt in ("--verbose",):
                print("启用详细模式")
        
        # 处理非选项参数
        for arg in args:
            print(f"非选项参数: {arg}")
            
    except getopt.GetoptError as e:
        print(f"参数解析错误: {e}")
        sys.exit(1)

# 测试参数解析示例
print("参数解析示例:")
# 临时修改sys.argv进行测试
sys.argv = ["script.py", "-h", "-u", "http://example.com", "--file", "data.txt", "--verbose", "input.txt"]
parse_args_example()

# ===========================
# 3. 短选项解析
# ===========================
print("\n" + "=" * 50)
print("3. 短选项解析")
print("=" * 50)

# 短选项示例
def short_options_example():
    """短选项解析示例"""
    # 短选项字符串格式：
    # - 每个字符代表一个选项
    # - 如果选项需要参数，后面跟冒号(:)
    short_opts = "ab:c:"
    
    print("短选项示例:")
    print(f"选项格式: {short_opts}")
    print("-a: 无参数选项")
    print("-b: 需要参数的选项")
    print("-c: 需要参数的选项")
    
    # 测试用例1: 正常使用
    print("\n测试用例1: 正常使用")
    try:
        opts, args = getopt.getopt(["-a", "-b", "value_b", "-cvalue_c"], short_opts)
        print(f"  解析结果: {opts}")
        print(f"  非选项参数: {args}")
    except getopt.GetoptError as e:
        print(f"  解析错误: {e}")
    
    # 测试用例2: 缺少参数
    print("\n测试用例2: 缺少参数")
    try:
        opts, args = getopt.getopt(["-a", "-b"], short_opts)
        print(f"  解析结果: {opts}")
    except getopt.GetoptError as e:
        print(f"  解析错误: {e}")
    
    # 测试用例3: 选项组合
    print("\n测试用例3: 选项组合")
    try:
        opts, args = getopt.getopt(["-ab", "value_b"], short_opts)
        print(f"  解析结果: {opts}")
    except getopt.GetoptError as e:
        print(f"  解析错误: {e}")

# 执行短选项示例
short_options_example()

# ===========================
# 4. 长选项解析
# ===========================
print("\n" + "=" * 50)
print("4. 长选项解析")
print("=" * 50)

# 长选项示例
def long_options_example():
    """长选项解析示例"""
    # 长选项列表格式：
    # - 每个元素是一个长选项名称
    # - 如果需要参数，后面跟等号(=)
    long_opts = ["help", "output=", "verbose"]
    
    print("长选项示例:")
    print(f"选项列表: {long_opts}")
    print("--help: 无参数选项")
    print("--output: 需要参数的选项")
    print("--verbose: 无参数选项")
    
    # 测试用例1: 正常使用
    print("\n测试用例1: 正常使用")
    try:
        opts, args = getopt.getopt(["--help", "--output", "result.txt", "--verbose"], "", long_opts)
        print(f"  解析结果: {opts}")
    except getopt.GetoptError as e:
        print(f"  解析错误: {e}")
    
    # 测试用例2: 使用等号指定参数
    print("\n测试用例2: 使用等号指定参数")
    try:
        opts, args = getopt.getopt(["--output=result.txt"], "", long_opts)
        print(f"  解析结果: {opts}")
    except getopt.GetoptError as e:
        print(f"  解析错误: {e}")
    
    # 测试用例3: 缺少参数
    print("\n测试用例3: 缺少参数")
    try:
        opts, args = getopt.getopt(["--output"], "", long_opts)
        print(f"  解析结果: {opts}")
    except getopt.GetoptError as e:
        print(f"  解析错误: {e}")

# 执行长选项示例
long_options_example()

# ===========================
# 5. 混合选项解析
# ===========================
print("\n" + "=" * 50)
print("5. 混合选项解析")
print("=" * 50)

# 混合选项示例
def mixed_options_example():
    """混合选项解析示例"""
    short_opts = "hu:v"
    long_opts = ["help", "url=", "verbose"]
    
    print("混合选项解析示例:")
    print(f"短选项: {short_opts}")
    print(f"长选项: {long_opts}")
    
    # 测试用例: 混合使用短选项和长选项
    try:
        opts, args = getopt.getopt(
            ["-h", "--url", "http://example.com", "-v", "input.txt"], 
            short_opts, 
            long_opts
        )
        
        print(f"  解析结果: {opts}")
        print(f"  非选项参数: {args}")
        
        # 处理选项
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("  处理--help选项")
            elif opt in ("-u", "--url"):
                print(f"  处理--url选项，值: {arg}")
            elif opt in ("-v", "--verbose"):
                print("  处理--verbose选项")
        
        # 处理非选项参数
        for arg in args:
            print(f"  处理非选项参数: {arg}")
            
    except getopt.GetoptError as e:
        print(f"参数解析错误: {e}")

# 执行混合选项示例
mixed_options_example()

# ===========================
# 6. 错误处理
# ===========================
print("\n" + "=" * 50)
print("6. 错误处理")
print("=" * 50)

# 错误处理示例
def error_handling_example():
    """错误处理示例"""
    short_opts = "a:b:"
    long_opts = ["alpha=", "beta="]
    
    # 测试用例1: 未知选项
    print("测试用例1: 未知选项")
    try:
        opts, args = getopt.getopt(["-a", "10", "-c", "20"], short_opts, long_opts)
        print(f"  解析结果: {opts}")
    except getopt.GetoptError as e:
        print(f"  解析错误: {e}")
    
    # 测试用例2: 缺少参数
    print("\n测试用例2: 缺少参数")
    try:
        opts, args = getopt.getopt(["-a", "-b", "20"], short_opts, long_opts)
        print(f"  解析结果: {opts}")
    except getopt.GetoptError as e:
        print(f"  解析错误: {e}")
    
    # 测试用例3: 无效的长选项
    print("\n测试用例3: 无效的长选项")
    try:
        opts, args = getopt.getopt(["--alpha", "10", "--gamma", "20"], short_opts, long_opts)
        print(f"  解析结果: {opts}")
    except getopt.GetoptError as e:
        print(f"  解析错误: {e}")

# 执行错误处理示例
error_handling_example()

# ===========================
# 7. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("7. 实际应用示例")
print("=" * 50)

# 示例1: 文件处理脚本
def file_processing_script():
    """文件处理脚本示例"""
    short_opts = "hi:o:v"
    long_opts = ["help", "input=", "output=", "verbose"]
    
    # 默认参数
    input_file = "input.txt"
    output_file = "output.txt"
    verbose = False
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
        
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("使用方法:")
                print("  script.py [-h] [-i INPUT] [-o OUTPUT] [-v]")
                print("选项:")
                print("  -h, --help: 显示帮助信息")
                print("  -i, --input: 输入文件路径")
                print("  -o, --output: 输出文件路径")
                print("  -v, --verbose: 启用详细模式")
                sys.exit(0)
            elif opt in ("-i", "--input"):
                input_file = arg
            elif opt in ("-o", "--output"):
                output_file = arg
            elif opt in ("-v", "--verbose"):
                verbose = True
        
        # 执行文件处理逻辑
        if verbose:
            print(f"输入文件: {input_file}")
            print(f"输出文件: {output_file}")
            print("执行文件处理...")
        
        print(f"文件处理完成: {input_file} -> {output_file}")
        
    except getopt.GetoptError as e:
        print(f"参数错误: {e}")
        print("使用 -h 或 --help 查看帮助信息")
        sys.exit(1)
    except Exception as e:
        print(f"处理错误: {e}")
        sys.exit(1)

# 测试文件处理脚本
print("示例1: 文件处理脚本")
sys.argv = ["file_script.py", "-i", "data.txt", "-o", "result.txt", "-v"]
file_processing_script()

# 示例2: URL下载工具
def url_downloader():
    """URL下载工具示例"""
    short_opts = "hu:o:p:"
    long_opts = ["help", "url=", "output=", "proxy="]
    
    # 默认参数
    url = None
    output = "downloaded_file"
    proxy = None
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
        
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("URL下载工具")
                print("使用方法:")
                print("  downloader.py -u URL [-o OUTPUT] [-p PROXY]")
                print("选项:")
                print("  -h, --help: 显示帮助信息")
                print("  -u, --url: 下载URL")
                print("  -o, --output: 输出文件名")
                print("  -p, --proxy: 代理服务器")
                sys.exit(0)
            elif opt in ("-u", "--url"):
                url = arg
            elif opt in ("-o", "--output"):
                output = arg
            elif opt in ("-p", "--proxy"):
                proxy = arg
        
        # 验证必要参数
        if not url:
            print("错误: 必须指定URL")
            print("使用 -h 或 --help 查看帮助信息")
            sys.exit(1)
        
        # 执行下载逻辑
        print(f"下载URL: {url}")
        if proxy:
            print(f"使用代理: {proxy}")
        print(f"保存到: {output}")
        print("开始下载...")
        
    except getopt.GetoptError as e:
        print(f"参数错误: {e}")
        print("使用 -h 或 --help 查看帮助信息")
        sys.exit(1)
    except Exception as e:
        print(f"下载错误: {e}")
        sys.exit(1)

# 测试URL下载工具
print("\n示例2: URL下载工具")
sys.argv = ["downloader.py", "-u", "http://example.com", "-o", "example.html", "-p", "http://proxy.example.com:8080"]
url_downloader()

# 示例3: 数据处理工具
def data_processor():
    """数据处理工具示例"""
    short_opts = "hi:o:f:t:"
    long_opts = ["help", "input=", "output=", "format=", "type="]
    
    # 默认参数
    input_file = None
    output_file = None
    format = "csv"
    data_type = "text"
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
        
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("数据处理工具")
                print("使用方法:")
                print("  processor.py -i INPUT -o OUTPUT [-f FORMAT] [-t TYPE]")
                print("选项:")
                print("  -h, --help: 显示帮助信息")
                print("  -i, --input: 输入文件")
                print("  -o, --output: 输出文件")
                print("  -f, --format: 输出格式 (csv, json, xml)")
                print("  -t, --type: 数据类型 (text, binary)")
                sys.exit(0)
            elif opt in ("-i", "--input"):
                input_file = arg
            elif opt in ("-o", "--output"):
                output_file = arg
            elif opt in ("-f", "--format"):
                format = arg
            elif opt in ("-t", "--type"):
                data_type = arg
        
        # 验证必要参数
        if not input_file or not output_file:
            print("错误: 必须指定输入和输出文件")
            print("使用 -h 或 --help 查看帮助信息")
            sys.exit(1)
        
        # 验证格式参数
        valid_formats = ["csv", "json", "xml"]
        if format not in valid_formats:
            print(f"错误: 无效的格式 '{format}'. 有效值: {', '.join(valid_formats)}")
            sys.exit(1)
        
        # 执行数据处理
        print(f"数据处理配置:")
        print(f"  输入文件: {input_file}")
        print(f"  输出文件: {output_file}")
        print(f"  输出格式: {format}")
        print(f"  数据类型: {data_type}")
        print("执行数据处理...")
        
    except getopt.GetoptError as e:
        print(f"参数错误: {e}")
        print("使用 -h 或 --help 查看帮助信息")
        sys.exit(1)

# 测试数据处理工具
print("\n示例3: 数据处理工具")
sys.argv = ["processor.py", "-i", "raw_data.txt", "-o", "processed.json", "-f", "json", "-t", "text"]
data_processor()

# ===========================
# 8. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("8. 最佳实践和注意事项")
print("=" * 50)

print("1. 选项定义")
print("   - 使用短选项字符串定义短选项")
print("   - 使用列表定义长选项")
print("   - 使用:和=标记需要参数的选项")

print("\n2. 错误处理")
print("   - 总是捕获getopt.GetoptError异常")
print("   - 提供清晰的错误消息")
print("   - 在错误消息中包含帮助信息")

print("\n3. 帮助信息")
print("   - 实现-h/--help选项")
print("   - 提供清晰的使用说明")
print("   - 列出所有可用选项")

print("\n4. 参数验证")
print("   - 验证必要参数是否存在")
print("   - 验证参数值是否有效")
print("   - 提供默认参数值")

print("\n5. 长选项与短选项")
print("   - 同时支持短选项和长选项")
print("   - 保持短选项和长选项的功能一致")

print("\n6. 局限性")
print("   - getopt适合简单的参数解析")
print("   - 不支持位置参数")
print("   - 不支持自动生成帮助信息")
print("   - 复杂的参数需求建议使用argparse模块")

# ===========================
# 9. 总结
# ===========================
print("\n" + "=" * 50)
print("9. 总结")
print("=" * 50)
print("getopt模块提供了C语言风格的命令行参数解析功能")
print("支持短选项和长选项的解析")
print("适合简单的命令行工具开发")

print("\n主要功能:")
print("- 解析短选项（如-a, -b）")
print("- 解析长选项（如--help, --version）")
print("- 处理选项参数")
print("- 支持选项和非选项参数混合")

print("\n应用场景:")
print("- 简单的命令行工具")
print("- 脚本参数解析")
print("- 快速开发的命令行界面")

print("\n使用getopt模块时，需要注意错误处理")
print("和提供清晰的帮助信息")
print("对于复杂的参数需求，建议使用argparse模块")
