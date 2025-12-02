# Python内置函数总览

'''
Python内置函数是Python解释器自带的函数，不需要导入任何模块就可以直接使用。
本文件详细介绍所有Python内置函数的功能、语法、参数、返回值和使用示例。
'''

# 1. 核心功能介绍
print("=== Python内置函数总览 ===")
print("Python 3.x版本共有69个内置函数，按功能可以分为以下几类：")
print("- 类型转换函数")
print("- 数学函数")
print("- 集合操作函数")
print("- 迭代器和迭代工具函数")
print("- 内存管理函数")
print("- 输入输出函数")
print("- 变量和对象操作函数")
print("- 类型和属性操作函数")
print("- 其他实用函数")

# 2. 类型转换函数
def type_conversion_functions():
    """类型转换相关内置函数"""
    print("\n=== 类型转换函数 ===")
    
    # int() - 转换为整数
    print("\n1. int() - 将对象转换为整数")
    print(f"   int('123') = {int('123')}")
    print(f"   int(3.9) = {int(3.9)}")
    print(f"   int('1010', 2) = {int('1010', 2)}  # 二进制转十进制")
    
    # float() - 转换为浮点数
    print("\n2. float() - 将对象转换为浮点数")
    print(f"   float('3.14') = {float('3.14')}")
    print(f"   float(42) = {float(42)}")
    
    # complex() - 创建复数
    print("\n3. complex() - 创建复数")
    print(f"   complex(3, 4) = {complex(3, 4)}")
    print(f"   complex('3+4j') = {complex('3+4j')}")
    
    # str() - 转换为字符串
    print("\n4. str() - 将对象转换为字符串")
    print(f"   str(123) = {str(123)}")
    print(f"   str([1, 2, 3]) = {str([1, 2, 3])}")
    
    # bytes() - 创建字节对象
    print("\n5. bytes() - 创建字节对象")
    print(f"   bytes('hello', 'utf-8') = {bytes('hello', 'utf-8')}")
    print(f"   bytes([72, 101, 108, 108, 111]) = {bytes([72, 101, 108, 108, 111])}")
    
    # bytearray() - 创建可变字节数组
    print("\n6. bytearray() - 创建可变字节数组")
    ba = bytearray('hello', 'utf-8')
    ba[0] = 72  # 修改第一个字节
    print(f"   bytearray('hello', 'utf-8') 并修改首字母 = {ba}")
    
    # bool() - 转换为布尔值
    print("\n7. bool() - 将对象转换为布尔值")
    print(f"   bool(0) = {bool(0)}")
    print(f"   bool(1) = {bool(1)}")
    print(f"   bool('') = {bool('')}")
    print(f"   bool([]) = {bool([])}")
    print(f"   bool([1]) = {bool([1])}")
    
    # list() - 创建列表
    print("\n8. list() - 创建列表")
    print(f"   list('hello') = {list('hello')}")
    print(f"   list((1, 2, 3)) = {list((1, 2, 3))}")
    
    # tuple() - 创建元组
    print("\n9. tuple() - 创建元组")
    print(f"   tuple([1, 2, 3]) = {tuple([1, 2, 3])}")
    print(f"   tuple('hello') = {tuple('hello')}")
    
    # set() - 创建集合
    print("\n10. set() - 创建集合")
    print(f"   set([1, 2, 2, 3]) = {set([1, 2, 2, 3])}")
    print(f"   set('hello') = {set('hello')}")
    
    # frozenset() - 创建不可变集合
    print("\n11. frozenset() - 创建不可变集合")
    print(f"   frozenset([1, 2, 3]) = {frozenset([1, 2, 3])}")
    
    # dict() - 创建字典
    print("\n12. dict() - 创建字典")
    print(f"   dict(a=1, b=2) = {dict(a=1, b=2)}")
    print(f"   dict([('a', 1), ('b', 2)]) = {dict([('a', 1), ('b', 2)])}")
    
    # chr() - 整数转字符
    print("\n13. chr() - 将整数转换为Unicode字符")
    print(f"   chr(65) = {chr(65)}")
    print(f"   chr(8364) = {chr(8364)}")  # 欧元符号
    
    # ord() - 字符转整数
    print("\n14. ord() - 返回字符的Unicode码点")
    print(f"   ord('A') = {ord('A')}")
    print(f"   ord('€') = {ord('€')}")

# 3. 数学函数
def math_functions():
    """数学相关内置函数"""
    print("\n=== 数学函数 ===")
    
    # abs() - 绝对值
    print("\n1. abs() - 返回数字的绝对值")
    print(f"   abs(-10) = {abs(-10)}")
    print(f"   abs(-3.14) = {abs(-3.14)}")
    print(f"   abs(complex(3, 4)) = {abs(complex(3, 4))}")  # 复数的模
    
    # divmod() - 商和余数
    print("\n2. divmod() - 返回商和余数的元组")
    print(f"   divmod(10, 3) = {divmod(10, 3)}")
    print(f"   divmod(7.5, 2.5) = {divmod(7.5, 2.5)}")
    
    # max() - 最大值
    print("\n3. max() - 返回最大值")
    print(f"   max(1, 3, 5, 2) = {max(1, 3, 5, 2)}")
    print(f"   max([1, 3, 5, 2]) = {max([1, 3, 5, 2])}")
    print(f"   max('hello') = {max('hello')}")
    # 使用key参数
    print(f"   max(['a', 'abc', 'ab'], key=len) = {max(['a', 'abc', 'ab'], key=len)}")
    
    # min() - 最小值
    print("\n4. min() - 返回最小值")
    print(f"   min(1, 3, 5, 2) = {min(1, 3, 5, 2)}")
    print(f"   min([1, 3, 5, 2]) = {min([1, 3, 5, 2])}")
    print(f"   min('hello') = {min('hello')}")
    
    # pow() - 幂运算
    print("\n5. pow() - 幂运算")
    print(f"   pow(2, 3) = {pow(2, 3)}")
    print(f"   pow(2, 3, 5) = {pow(2, 3, 5)}  # (2^3) % 5")
    
    # round() - 四舍五入
    print("\n6. round() - 四舍五入")
    print(f"   round(3.14159) = {round(3.14159)}")
    print(f"   round(3.14159, 2) = {round(3.14159, 2)}")
    print(f"   round(2.5) = {round(2.5)}  # 注意：Python的四舍五入是银行家舍入法")
    print(f"   round(3.5) = {round(3.5)}")

# 4. 集合操作函数
def collection_functions():
    """集合操作相关内置函数"""
    print("\n=== 集合操作函数 ===")
    
    # all() - 全部为真
    print("\n1. all() - 所有元素为真时返回True")
    print(f"   all([1, 2, 3]) = {all([1, 2, 3])}")
    print(f"   all([1, 0, 3]) = {all([1, 0, 3])}")
    print(f"   all([]) = {all([])}  # 空迭代器返回True")
    
    # any() - 任一为真
    print("\n2. any() - 任一元素为真时返回True")
    print(f"   any([0, 1, 0]) = {any([0, 1, 0])}")
    print(f"   any([0, 0, 0]) = {any([0, 0, 0])}")
    print(f"   any([]) = {any([])}  # 空迭代器返回False")
    
    # len() - 长度
    print("\n3. len() - 返回对象长度")
    print(f"   len([1, 2, 3]) = {len([1, 2, 3])}")
    print(f"   len('hello') = {len('hello')}")
    print(f"   len({'a': 1, 'b': 2}) = {len({'a': 1, 'b': 2})}")
    
    # sum() - 求和
    print("\n4. sum() - 求和")
    print(f"   sum([1, 2, 3, 4]) = {sum([1, 2, 3, 4])}")
    print(f"   sum((1, 2, 3), 10) = {sum((1, 2, 3), 10)}  # 初始值为10")
    print(f"   sum([], 5) = {sum([], 5)}  # 空序列加初始值")
    
    # sorted() - 排序
    print("\n5. sorted() - 返回排序后的新列表")
    print(f"   sorted([3, 1, 4, 2]) = {sorted([3, 1, 4, 2])}")
    print(f"   sorted('hello') = {sorted('hello')}")
    print(f"   sorted([3, 1, 4, 2], reverse=True) = {sorted([3, 1, 4, 2], reverse=True)}")
    # 使用key参数
    print(f"   sorted(['abc', 'a', 'ab'], key=len) = {sorted(['abc', 'a', 'ab'], key=len)}")

# 5. 迭代器和迭代工具函数
def iterator_functions():
    """迭代器和迭代工具相关内置函数"""
    print("\n=== 迭代器和迭代工具函数 ===")
    
    # iter() - 创建迭代器
    print("\n1. iter() - 创建迭代器")
    it = iter([1, 2, 3])
    print(f"   iter([1, 2, 3]) -> next(it) = {next(it)}, next(it) = {next(it)}, next(it) = {next(it)}")
    
    # next() - 获取下一个元素
    print("\n2. next() - 获取迭代器的下一个元素")
    it = iter([1, 2, 3])
    print(f"   next(it) = {next(it)}")
    print(f"   next(it) = {next(it)}")
    print(f"   next(it, '默认值') = {next(it)}")
    print(f"   next(it, '默认值') = {next(it, '默认值')}  # 迭代结束时返回默认值")
    
    # enumerate() - 枚举
    print("\n3. enumerate() - 枚举迭代器")
    for i, value in enumerate(['a', 'b', 'c']):
        print(f"   索引: {i}, 值: {value}")
    # 指定起始索引
    for i, value in enumerate(['a', 'b', 'c'], 10):
        print(f"   索引(起始=10): {i}, 值: {value}")
    
    # range() - 范围
    print("\n4. range() - 创建整数范围")
    print(f"   list(range(5)) = {list(range(5))}")
    print(f"   list(range(2, 8)) = {list(range(2, 8))}")
    print(f"   list(range(0, 10, 2)) = {list(range(0, 10, 2))}")
    print(f"   list(range(-5, 5)) = {list(range(-5, 5))}")
    print(f"   list(range(5, 0, -1)) = {list(range(5, 0, -1))}")
    
    # map() - 映射
    print("\n5. map() - 对序列元素应用函数")
    print(f"   list(map(lambda x: x*2, [1, 2, 3])) = {list(map(lambda x: x*2, [1, 2, 3]))}")
    print(f"   list(map(lambda x, y: x+y, [1, 2, 3], [4, 5, 6])) = {list(map(lambda x, y: x+y, [1, 2, 3], [4, 5, 6]))}")
    
    # filter() - 过滤
    print("\n6. filter() - 过滤序列元素")
    print(f"   list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) = {list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))}")
    
    # zip() - 压缩
    print("\n7. zip() - 聚合多个迭代器的元素")
    print(f"   list(zip([1, 2, 3], ['a', 'b', 'c'])) = {list(zip([1, 2, 3], ['a', 'b', 'c']))}")
    # 长度不同时以最短为准
    print(f"   list(zip([1, 2, 3], ['a', 'b'])) = {list(zip([1, 2, 3], ['a', 'b']))}")
    # 使用*解压缩
    pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
    numbers, letters = zip(*pairs)
    print(f"   zip(*[(1, 'a'), (2, 'b'), (3, 'c')]) -> 数字: {numbers}, 字母: {letters}")

# 6. 内存管理函数
def memory_functions():
    """内存管理相关内置函数"""
    print("\n=== 内存管理函数 ===")
    
    # id() - 对象标识符
    print("\n1. id() - 返回对象的唯一标识符")
    x = 10
    y = 10
    print(f"   id(10) = {id(10)}")
    print(f"   id(x) = {id(x)}")
    print(f"   id(y) = {id(y)}")
    print(f"   x is y = {x is y}")
    
    # isinstance() - 类型检查
    print("\n2. isinstance() - 检查对象是否为指定类型的实例")
    print(f"   isinstance(5, int) = {isinstance(5, int)}")
    print(f"   isinstance(5.5, (int, float)) = {isinstance(5.5, (int, float))}")
    print(f"   isinstance([], list) = {isinstance([], list)}")
    print(f"   isinstance([], (list, tuple)) = {isinstance([], (list, tuple))}")
    
    # issubclass() - 子类检查
    print("\n3. issubclass() - 检查类是否为另一个类的子类")
    class A:
        pass
    class B(A):
        pass
    class C:
        pass
    print(f"   issubclass(B, A) = {issubclass(B, A)}")
    print(f"   issubclass(A, B) = {issubclass(A, B)}")
    print(f"   issubclass(B, (A, C)) = {issubclass(B, (A, C))}")
    
    # type() - 获取类型
    print("\n4. type() - 返回对象的类型")
    print(f"   type(5) = {type(5)}")
    print(f"   type([1, 2, 3]) = {type([1, 2, 3])}")
    print(f"   type('hello') = {type('hello')}")
    print(f"   type(type(5)) = {type(type(5))}")
    # 创建新类型
    NewClass = type('NewClass', (), {'x': 10})
    print(f"   动态创建的类: {NewClass}，x属性: {NewClass.x}")

# 7. 输入输出函数
def io_functions():
    """输入输出相关内置函数"""
    print("\n=== 输入输出函数 ===")
    
    # print() - 打印输出
    print("\n1. print() - 打印输出")
    print("   print函数示例:", "Hello", "World")
    # 重定向到字符串
    from io import StringIO
    import sys
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    print("Hello World")
    sys.stdout = old_stdout
    print(f"   捕获的输出: '{mystdout.getvalue().strip()}'")
    
    # input() - 获取输入
    print("\n2. input() - 获取用户输入")
    print("   使用方法: user_input = input('提示信息: ')")
    
    # open() - 打开文件
    print("\n3. open() - 打开文件")
    print("   基本用法: with open('filename.txt', 'r') as f:")
    print("   模式:")
    print("   - 'r': 只读（默认）")
    print("   - 'w': 写入（会截断文件）")
    print("   - 'x': 独占创建，如果文件已存在则失败")
    print("   - 'a': 追加写入")
    print("   - 'b': 二进制模式")
    print("   - 't': 文本模式（默认）")
    print("   - '+': 读写模式")

# 8. 变量和对象操作函数
def variable_functions():
    """变量和对象操作相关内置函数"""
    print("\n=== 变量和对象操作函数 ===")
    
    # globals() - 全局变量字典
    print("\n1. globals() - 返回当前全局符号表的字典")
    print(f"   globals() 包含的键数量: {len(globals())}")
    print(f"   是否包含'print'函数: {'print' in globals()}")
    
    # locals() - 局部变量字典
    print("\n2. locals() - 返回当前局部符号表的字典")
    x = 10
    y = 20
    print(f"   局部变量示例: x={x}, y={y}")
    print(f"   locals() 包含的键数量: {len(locals())}")
    
    # vars() - 对象的__dict__属性
    print("\n3. vars() - 返回对象的__dict__属性")
    class MyClass:
        def __init__(self):
            self.a = 1
            self.b = 2
    obj = MyClass()
    print(f"   对象的属性字典: {vars(obj)}")
    print(f"   vars() 无参数时等同于 locals(): {vars() is locals()}")

# 9. 类型和属性操作函数
def attribute_functions():
    """类型和属性操作相关内置函数"""
    print("\n=== 类型和属性操作函数 ===")
    
    # hasattr() - 检查属性是否存在
    print("\n1. hasattr() - 检查对象是否具有指定属性")
    class MyClass:
        x = 10
        def method(self):
            pass
    obj = MyClass()
    print(f"   hasattr(obj, 'x') = {hasattr(obj, 'x')}")
    print(f"   hasattr(obj, 'method') = {hasattr(obj, 'method')}")
    print(f"   hasattr(obj, 'y') = {hasattr(obj, 'y')}")
    
    # getattr() - 获取属性值
    print("\n2. getattr() - 获取对象的属性值")
    print(f"   getattr(obj, 'x') = {getattr(obj, 'x')}")
    print(f"   getattr(obj, 'y', '默认值') = {getattr(obj, 'y', '默认值')}")
    
    # setattr() - 设置属性值
    print("\n3. setattr() - 设置对象的属性值")
    setattr(obj, 'y', 20)
    print(f"   设置y属性后: obj.y = {obj.y}")
    
    # delattr() - 删除属性
    print("\n4. delattr() - 删除对象的属性")
    delattr(obj, 'y')
    print(f"   删除y属性后: hasattr(obj, 'y') = {hasattr(obj, 'y')}")
    
    # callable() - 可调用性检查
    print("\n5. callable() - 检查对象是否可调用")
    print(f"   callable(obj.method) = {callable(obj.method)}")
    print(f"   callable(obj.x) = {callable(obj.x)}")
    print(f"   callable(print) = {callable(print)}")
    print(f"   callable([1, 2, 3]) = {callable([1, 2, 3])}")

# 10. 其他实用函数
def other_functions():
    """其他实用内置函数"""
    print("\n=== 其他实用函数 ===")
    
    # __import__() - 动态导入模块
    print("\n1. __import__() - 动态导入模块")
    math_module = __import__('math')
    print(f"   动态导入math模块: math_module.pi = {math_module.pi}")
    
    # ascii() - 返回对象的ASCII表示
    print("\n2. ascii() - 返回对象的可打印ASCII表示")
    print(f"   ascii('hello') = {ascii('hello')}")
    print(f"   ascii('你好') = {ascii('你好')}")
    
    # bin() - 转换为二进制
    print("\n3. bin() - 将整数转换为二进制字符串")
    print(f"   bin(10) = {bin(10)}")
    print(f"   bin(0) = {bin(0)}")
    print(f"   bin(-10) = {bin(-10)}")
    
    # oct() - 转换为八进制
    print("\n4. oct() - 将整数转换为八进制字符串")
    print(f"   oct(10) = {oct(10)}")
    
    # hex() - 转换为十六进制
    print("\n5. hex() - 将整数转换为十六进制字符串")
    print(f"   hex(10) = {hex(10)}")
    print(f"   hex(255) = {hex(255)}")
    
    # compile() - 编译代码
    print("\n6. compile() - 将源码编译为代码对象")
    code = compile('print("Hello, World!")', '<string>', 'exec')
    print("   编译代码对象后执行:")
    exec(code)
    
    # eval() - 评估表达式
    print("\n7. eval() - 评估表达式并返回结果")
    print(f"   eval('1 + 2 * 3') = {eval('1 + 2 * 3')}")
    x = 10
    print(f"   eval('x + 5') = {eval('x + 5')}")
    
    # exec() - 执行代码
    print("\n8. exec() - 执行动态Python代码")
    print("   执行多行代码:")
    exec('''
x = 5
y = 10
print(f"x + y = {x + y}")
''')
    
    # format() - 格式化字符串
    print("\n9. format() - 格式化值")
    print(f"   format(42, '08d') = {format(42, '08d')}")
    print(f"   format(3.14159, '.2f') = {format(3.14159, '.2f')}")
    print(f"   format(10, 'x') = {format(10, 'x')}")
    
    # help() - 获取帮助
    print("\n10. help() - 获取帮助信息")
    print("   help() 不带参数进入交互式帮助系统")
    print(f"   help(print) 返回print函数的帮助信息")
    
    # hash() - 哈希值
    print("\n11. hash() - 返回对象的哈希值")
    print(f"   hash('hello') = {hash('hello')}")
    print(f"   hash(123) = {hash(123)}")
    print(f"   hash((1, 2, 3)) = {hash((1, 2, 3))}")
    # 不可哈希的对象会抛出异常
    try:
        hash([1, 2, 3])
    except TypeError as e:
        print(f"   hash([1, 2, 3]) 引发异常: {e}")
    
    # repr() - 字符串表示
    print("\n12. repr() - 返回对象的可打印表示")
    print(f"   repr('hello') = {repr('hello')}")
    print(f"   repr([1, 2, 3]) = {repr([1, 2, 3])}")
    
    # slice() - 创建切片对象
    print("\n13. slice() - 创建切片对象")
    s = slice(1, 10, 2)
    print(f"   slice(1, 10, 2) 应用于range(20): {list(range(20)[s])}")
    
    # super() - 调用父类方法
    print("\n14. super() - 调用父类的方法")
    class Parent:
        def method(self):
            return "Parent method"
    class Child(Parent):
        def method(self):
            parent_result = super().method()
            return f"{parent_result} + Child method"
    child = Child()
    print(f"   super()调用结果: {child.method()}")
    
    # breakpoint() - 调试断点（Python 3.7+）
    print("\n15. breakpoint() - 调试断点")
    print("   调用Python调试器")

# 11. 内置函数综合使用示例
def comprehensive_example():
    """内置函数综合使用示例"""
    print("\n=== 内置函数综合使用示例 ===")
    
    # 示例1: 数据处理管道
    print("\n示例1: 数据处理管道")
    data = [1.2, 3.5, -2.1, 0, 4.7, -0.8]
    print(f"原始数据: {data}")
    
    # 使用内置函数链进行数据处理
    result = list(map(
        round,
        filter(
            lambda x: x > 0,
            sorted(data)
        ),
        [2] * len(data)  # 每个元素都保留2位小数
    ))
    print(f"处理后的数据（排序、过滤正数、保留2位小数）: {result}")
    print(f"数据总和: {sum(result)}")
    print(f"最大值: {max(result)}")
    print(f"最小值: {min(result)}")
    
    # 示例2: 文本分析
    print("\n示例2: 文本分析")
    text = "Python is a powerful programming language. Python is easy to learn."
    
    # 分析文本
    words = text.lower().replace('.', '').split()
    word_freq = {}
    
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    print(f"单词总数: {len(words)}")
    print(f"不同单词数: {len(word_freq)}")
    print(f"单词频率: {word_freq}")
    print(f"出现次数最多的单词: {max(word_freq.items(), key=lambda x: x[1])}")
    
    # 示例3: 类与对象操作
    print("\n示例3: 类与对象操作")
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def greet(self):
            return f"Hello, my name is {self.name}"
    
    # 动态创建和操作对象
    people = []
    for name, age in [('Alice', 30), ('Bob', 25), ('Charlie', 35)]:
        person = Person(name, age)
        people.append(person)
    
    # 使用内置函数操作对象
    print(f"人员列表: {[getattr(p, 'name') for p in people]}")
    print(f"平均年龄: {sum(getattr(p, 'age') for p in people) / len(people)}")
    
    # 过滤成年人员
    adults = list(filter(lambda p: getattr(p, 'age') >= 30, people))
    print(f"成年人数量: {len(adults)}, 名字: {[getattr(p, 'name') for p in adults]}")
    
    # 调用对象方法
    for person in people:
        if hasattr(person, 'greet') and callable(getattr(person, 'greet')):
            print(getattr(person, 'greet')())

# 12. 内置函数使用注意事项
def usage_notes():
    print("\n=== 内置函数使用注意事项 ===")
    print("1. eval()和exec()函数执行任意代码，存在安全风险，避免用于不可信输入")
    print("2. isinstance()比type()更适合类型检查，因为它考虑了继承关系")
    print("3. sorted()返回新列表，而list.sort()直接修改原列表")
    print("4. 对于大型数据集，filter()和map()返回迭代器，比列表推导式更节省内存")
    print("5. round()使用银行家舍入法（四舍六入五成偶），可能与预期不同")
    print("6. 使用open()函数时，始终使用with语句来确保文件正确关闭")
    print("7. locals()返回的字典在函数内是只读的，修改不会影响实际局部变量")
    print("8. all()和any()对于空迭代器分别返回True和False")
    print("9. zip()在Python 3中返回迭代器，不再是列表")
    print("10. 在Python中，小整数（通常是-5到256）会被缓存，所以它们的id相同")

# 执行所有示例
if __name__ == "__main__":
    type_conversion_functions()
    math_functions()
    collection_functions()
    iterator_functions()
    memory_functions()
    io_functions()
    variable_functions()
    attribute_functions()
    other_functions()
    comprehensive_example()
    usage_notes()
