#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
argparse模块 - 命令行参数解析

argparse模块是Python标准库中用于解析命令行参数的强大工具。

主要功能包括：
- 自动生成帮助信息
- 支持位置参数和可选参数
- 支持参数类型检查和转换
- 支持参数默认值
- 支持子命令
- 支持互斥参数
- 支持参数分组

使用场景：
- 命令行工具开发
- 复杂脚本参数解析
- 交互式命令行界面
- 命令行应用程序

官方文档：https://docs.python.org/3/library/argparse.html
"""

import argparse
import sys

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. argparse模块基本介绍")
print("=" * 50)
print("argparse模块用于解析命令行参数")
print("提供了强大的参数解析功能")
print("支持自动生成帮助信息")
print("适合复杂的命令行参数解析需求")

# ===========================
# 2. 基本用法
# ===========================
print("\n" + "=" * 50)
print("2. 基本用法")
print("=" * 50)

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(
    description='argparse模块基本用法示例',
    epilog='这是示例的结尾信息'
)

# 添加位置参数
parser.add_argument('filename', help='输入文件名')

# 添加可选参数
parser.add_argument('-o', '--output', help='输出文件名', default='output.txt')

# 添加布尔参数
parser.add_argument('-v', '--verbose', action='store_true', help='启用详细模式')

# 解析命令行参数
# 注意：实际使用时，应该使用sys.argv[1:]
args = parser.parse_args(['input.txt', '--output', 'result.txt', '--verbose'])

print("解析后的参数:")
print(f"  输入文件名: {args.filename}")
print(f"  输出文件名: {args.output}")
print(f"  详细模式: {args.verbose}")

# 查看帮助信息
print("\n帮助信息:")
parser.print_help()

# ===========================
# 3. 参数类型
# ===========================
print("\n" + "=" * 50)
print("3. 参数类型")
print("=" * 50)

parser = argparse.ArgumentParser(description='参数类型示例')

# 整数类型
parser.add_argument('-n', '--number', type=int, help='整数参数')

# 浮点数类型
parser.add_argument('-f', '--float', type=float, help='浮点数参数')

# 布尔类型（通过store_true/store_false）
parser.add_argument('-b', '--boolean', action='store_true', help='布尔参数')

# 文件类型
parser.add_argument('-i', '--input-file', type=argparse.FileType('r'), help='输入文件')

# 自定义类型
parser.add_argument('-c', '--color', type=str.lower, choices=['red', 'green', 'blue'], help='颜色选择')

# 测试参数类型
print("测试参数类型:")
args = parser.parse_args(['-n', '10', '-f', '3.14', '-b', '-c', 'RED'])

print(f"  整数参数: {args.number} (类型: {type(args.number).__name__})")
print(f"  浮点数参数: {args.float} (类型: {type(args.float).__name__})")
print(f"  布尔参数: {args.boolean} (类型: {type(args.boolean).__name__})")
print(f"  颜色参数: {args.color} (类型: {type(args.color).__name__})")

# ===========================
# 4. 参数默认值
# ===========================
print("\n" + "=" * 50)
print("4. 参数默认值")
print("=" * 50)

parser = argparse.ArgumentParser(description='参数默认值示例')

# 设置默认值
parser.add_argument('-d', '--default', default='默认值', help='带有默认值的参数')
parser.add_argument('-n', '--number', type=int, default=42, help='整数参数默认值')
parser.add_argument('-b', '--boolean', action='store_false', default=True, help='布尔参数默认值')

# 测试默认值
print("测试默认值:")
args = parser.parse_args([])

print(f"  默认值参数: {args.default}")
print(f"  整数默认值: {args.number}")
print(f"  布尔默认值: {args.boolean}")

# 测试覆盖默认值
print("\n测试覆盖默认值:")
args = parser.parse_args(['-d', '新值', '-n', '100', '-b'])

print(f"  默认值参数: {args.default}")
print(f"  整数默认值: {args.number}")
print(f"  布尔默认值: {args.boolean}")

# ===========================
# 5. 互斥参数
# ===========================
print("\n" + "=" * 50)
print("5. 互斥参数")
print("=" * 50)

parser = argparse.ArgumentParser(description='互斥参数示例')

# 创建互斥组
mutex_group = parser.add_mutually_exclusive_group()

# 添加互斥参数
mutex_group.add_argument('-v', '--verbose', action='store_true', help='详细模式')
mutex_group.add_argument('-q', '--quiet', action='store_true', help='安静模式')

# 测试互斥参数
print("测试互斥参数:")
args = parser.parse_args(['-v'])
print(f"  详细模式: {args.verbose}, 安静模式: {args.quiet}")

args = parser.parse_args(['-q'])
print(f"  详细模式: {args.verbose}, 安静模式: {args.quiet}")

# 测试同时使用互斥参数（会报错）
print("\n测试同时使用互斥参数:")
try:
    args = parser.parse_args(['-v', '-q'])
except SystemExit:
    print("  同时使用互斥参数导致错误")

# ===========================
# 6. 参数分组
# ===========================
print("\n" + "=" * 50)
print("6. 参数分组")
print("=" * 50)

parser = argparse.ArgumentParser(description='参数分组示例')

# 添加常规参数
parser.add_argument('filename', help='文件名')

# 创建输入参数组
input_group = parser.add_argument_group('输入参数', '与输入相关的参数')
input_group.add_argument('-i', '--input', help='输入文件路径')
input_group.add_argument('--encoding', help='输入文件编码', default='utf-8')

# 创建输出参数组
output_group = parser.add_argument_group('输出参数', '与输出相关的参数')
output_group.add_argument('-o', '--output', help='输出文件路径')
output_group.add_argument('-f', '--format', choices=['txt', 'csv', 'json'], default='txt', help='输出格式')

# 打印帮助信息，查看参数分组效果
print("帮助信息（含参数分组）:")
parser.print_help()

# ===========================
# 7. 子命令
# ===========================
print("\n" + "=" * 50)
print("7. 子命令")
print("=" * 50)

parser = argparse.ArgumentParser(description='子命令示例')

# 创建子命令解析器
subparsers = parser.add_subparsers(dest='command', help='可用子命令')

# 创建list子命令
list_parser = subparsers.add_parser('list', help='列出文件')
list_parser.add_argument('-l', '--long', action='store_true', help='长格式列表')
list_parser.add_argument('path', nargs='?', default='.', help='目录路径')

# 创建create子命令
create_parser = subparsers.add_parser('create', help='创建文件')
create_parser.add_argument('filename', help='文件名')
create_parser.add_argument('-t', '--type', choices=['file', 'dir'], default='file', help='创建类型')

# 创建delete子命令
delete_parser = subparsers.add_parser('delete', help='删除文件')
delete_parser.add_argument('filename', help='文件名')
delete_parser.add_argument('-f', '--force', action='store_true', help='强制删除')

# 测试子命令
print("测试子命令:")

# 测试list子命令
args = parser.parse_args(['list', '-l', '/tmp'])
print(f"  子命令: {args.command}")
print(f"  长格式: {args.long}")
print(f"  路径: {args.path}")

# 测试create子命令
args = parser.parse_args(['create', 'new_file.txt', '-t', 'file'])
print(f"  子命令: {args.command}")
print(f"  文件名: {args.filename}")
print(f"  类型: {args.type}")

# 打印帮助信息，查看子命令效果
print("\n帮助信息（含子命令）:")
parser.print_help()

# ===========================
# 8. 高级功能
# ===========================
print("\n" + "=" * 50)
print("8. 高级功能")
print("=" * 50)

# 多个值的参数
parser = argparse.ArgumentParser(description='高级功能示例')

# nargs参数控制接收值的数量
parser.add_argument('-m', '--multi', nargs='+', help='接收多个值')
parser.add_argument('-o', '--optional', nargs='?', const='常量值', default='默认值', help='可选参数值')
parser.add_argument('-a', '--all', nargs='*', help='接收所有剩余参数')

# 测试多个值的参数
print("测试多个值的参数:")
args = parser.parse_args(['-m', 'value1', 'value2', 'value3', '-o', 'option_value', '-a', 'arg1', 'arg2'])

print(f"  多个值: {args.multi}")
print(f"  可选值: {args.optional}")
print(f"  所有参数: {args.all}")

# ===========================
# 9. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("9. 实际应用示例")
print("=" * 50)

# 示例1: 文件处理工具
def file_processor():
    """文件处理工具示例"""
    parser = argparse.ArgumentParser(
        description='文件处理工具',
        epilog='使用示例: file_tool.py -i input.txt -o output.txt -v'
    )
    
    # 输入输出参数
    parser.add_argument('-i', '--input', required=True, help='输入文件路径')
    parser.add_argument('-o', '--output', default='output.txt', help='输出文件路径')
    
    # 处理选项
    parser.add_argument('-v', '--verbose', action='store_true', help='启用详细模式')
    parser.add_argument('--encoding', default='utf-8', help='文件编码')
    parser.add_argument('--format', choices=['txt', 'csv', 'json'], default='txt', help='输出格式')
    
    # 处理参数
    parser.add_argument('-n', '--number', type=int, default=10, help='处理行数')
    parser.add_argument('--skip', type=int, default=0, help='跳过行数')
    
    # 解析参数
    # 注意：实际使用时，应该使用sys.argv[1:]
    args = parser.parse_args(['-i', 'data.txt', '-o', 'result.json', '--format', 'json', '-v', '-n', '50'])
    
    # 执行处理逻辑
    if args.verbose:
        print("文件处理工具配置:")
        print(f"  输入文件: {args.input}")
        print(f"  输出文件: {args.output}")
        print(f"  文件编码: {args.encoding}")
        print(f"  输出格式: {args.format}")
        print(f"  处理行数: {args.number}")
        print(f"  跳过行数: {args.skip}")
    
    print("执行文件处理...")
    print(f"文件处理完成: {args.input} -> {args.output}")

# 测试文件处理工具
print("示例1: 文件处理工具")
file_processor()

# 示例2: 网络请求工具
def network_request():
    """网络请求工具示例"""
    parser = argparse.ArgumentParser(
        description='网络请求工具',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # URL参数
    parser.add_argument('url', help='请求URL')
    
    # 请求方法
    parser.add_argument('-X', '--method', choices=['GET', 'POST', 'PUT', 'DELETE'], default='GET', help='请求方法')
    
    # 请求头
    parser.add_argument('-H', '--header', action='append', help='请求头 (格式: Key:Value)')
    
    # 请求数据
    parser.add_argument('-d', '--data', help='请求数据')
    parser.add_argument('-f', '--file', help='上传文件路径')
    
    # 认证信息
    parser.add_argument('-u', '--user', help='用户名:密码')
    
    # 代理设置
    parser.add_argument('--proxy', help='代理服务器 (http://proxy:port)')
    
    # 输出选项
    parser.add_argument('-v', '--verbose', action='count', default=0, help='详细模式 (-v, -vv)')
    parser.add_argument('-o', '--output', help='输出文件路径')
    
    # 解析参数
    args = parser.parse_args(['http://example.com/api', '-X', 'POST', '-H', 'Content-Type:application/json', '-d', '{"key":"value"}', '-v'])
    
    # 执行请求逻辑
    print("网络请求工具配置:")
    print(f"  URL: {args.url}")
    print(f"  方法: {args.method}")
    print(f"  请求头: {args.header}")
    print(f"  请求数据: {args.data}")
    print(f"  上传文件: {args.file}")
    print(f"  认证信息: {args.user}")
    print(f"  代理服务器: {args.proxy}")
    print(f"  详细模式级别: {args.verbose}")
    print(f"  输出文件: {args.output}")
    
    print("发送网络请求...")
    print("请求完成")

# 测试网络请求工具
print("\n示例2: 网络请求工具")
network_request()

# 示例3: 数据库管理工具
def database_manager():
    """数据库管理工具示例"""
    parser = argparse.ArgumentParser(description='数据库管理工具')
    
    # 创建子命令解析器
    subparsers = parser.add_subparsers(dest='command', required=True, help='可用命令')
    
    # 创建连接子命令
    connect_parser = subparsers.add_parser('connect', help='连接数据库')
    connect_parser.add_argument('-h', '--host', default='localhost', help='数据库主机')
    connect_parser.add_argument('-P', '--port', type=int, default=3306, help='数据库端口')
    connect_parser.add_argument('-u', '--user', required=True, help='用户名')
    connect_parser.add_argument('-p', '--password', required=True, help='密码')
    connect_parser.add_argument('-d', '--database', help='数据库名')
    
    # 创建查询子命令
    query_parser = subparsers.add_parser('query', help='执行查询')
    query_parser.add_argument('sql', help='SQL查询语句')
    query_parser.add_argument('-f', '--format', choices=['table', 'json', 'csv'], default='table', help='输出格式')
    query_parser.add_argument('-o', '--output', help='输出文件')
    
    # 创建导入子命令
    import_parser = subparsers.add_parser('import', help='导入数据')
    import_parser.add_argument('-f', '--file', required=True, help='数据文件')
    import_parser.add_argument('-t', '--table', required=True, help='目标表')
    import_parser.add_argument('--format', choices=['csv', 'json'], required=True, help='文件格式')
    import_parser.add_argument('--delimiter', default=',', help='分隔符 (仅CSV格式)')
    
    # 创建导出子命令
    export_parser = subparsers.add_parser('export', help='导出数据')
    export_parser.add_argument('-t', '--table', required=True, help='源表')
    export_parser.add_argument('-o', '--output', required=True, help='输出文件')
    export_parser.add_argument('--format', choices=['csv', 'json'], required=True, help='文件格式')
    export_parser.add_argument('--where', help='条件语句')
    
    # 解析参数
    args = parser.parse_args(['query', 'SELECT * FROM users WHERE id < 100', '--format', 'json', '-o', 'users.json'])
    
    # 执行数据库操作
    print("数据库管理工具操作:")
    print(f"  命令: {args.command}")
    print(f"  SQL语句: {args.sql}")
    print(f"  输出格式: {args.format}")
    print(f"  输出文件: {args.output}")
    
    print("执行数据库查询...")
    print("查询完成")

# 测试数据库管理工具
print("\n示例3: 数据库管理工具")
database_manager()

# ===========================
# 10. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("10. 最佳实践和注意事项")
print("=" * 50)

print("1. 帮助信息")
print("   - 提供清晰的description和epilog")
print("   - 为每个参数添加详细的help文本")
print("   - 使用合适的formatter_class格式化帮助信息")

print("\n2. 参数设计")
print("   - 使用有意义的参数名称")
print("   - 区分位置参数和可选参数")
print("   - 合理设置默认值")
print("   - 使用类型检查确保参数有效性")

print("\n3. 错误处理")
print("   - 使用required=True标记必要参数")
print("   - 使用choices限制参数值范围")
print("   - 提供有意义的错误消息")

print("\n4. 子命令")
print("   - 对于复杂工具，使用子命令组织功能")
print("   - 为每个子命令提供独立的帮助信息")
print("   - 使用dest参数捕获子命令名称")

print("\n5. 参数分组")
print("   - 使用add_argument_group分组相关参数")
print("   - 为参数组提供描述信息")

print("\n6. 类型转换")
print("   - 使用type参数进行类型转换")
print("   - 可以使用自定义函数进行复杂类型转换")
print("   - 使用argparse.FileType处理文件参数")

print("\n7. 互斥参数")
print("   - 使用add_mutually_exclusive_group创建互斥参数")
print("   - 互斥参数组可以嵌套")

print("\n8. 性能考虑")
print("   - argparse的性能开销很小")
print("   - 对于简单参数解析，可以考虑使用sys.argv直接处理")

# ===========================
# 11. 总结
# ===========================
print("\n" + "=" * 50)
print("11. 总结")
print("=" * 50)
print("argparse模块是Python中功能强大的命令行参数解析工具")
print("提供了丰富的参数解析功能和灵活的配置选项")

print("\n主要功能:")
print("- 自动生成帮助信息")
print("- 支持位置参数和可选参数")
print("- 参数类型检查和转换")
print("- 参数默认值设置")
print("- 子命令支持")
print("- 互斥参数和参数分组")

print("\n应用场景:")
print("- 命令行工具开发")
print("- 复杂脚本参数解析")
print("- 交互式命令行界面")
print("- 命令行应用程序")

print("\n使用argparse模块可以快速开发功能完善的命令行工具")
print("提高命令行工具的可用性和用户体验")
