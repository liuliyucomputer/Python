# Python内置函数练习题

'''
本文件包含Python所有内置函数的练习题，每个练习题都有详细的解答和说明。
通过这些练习，你可以更好地理解和掌握Python内置函数的使用。
'''

import sys
import io

print("=== Python内置函数练习题集 ===")
print("以下是按类别组织的Python内置函数练习题\n")

# ===========================
# 第一部分：类型转换函数练习
# ===========================
print("第一部分：类型转换函数练习")
print("-" * 50)

# 练习1：int()函数
def exercise_int():
    print("\n练习1：int()函数 - 将各种类型转换为整数")
    print("题目：将以下值转换为整数")
    print("a) '42'")
    print("b) '1010'（二进制）")
    print("c) 'FF'（十六进制）")
    print("d) 3.9")
    print("e) True")
    
    # 参考答案
    print("\n参考答案：")
    print(f"a) int('42') = {int('42')}")
    print(f"b) int('1010', 2) = {int('1010', 2)}")
    print(f"c) int('FF', 16) = {int('FF', 16)}")
    print(f"d) int(3.9) = {int(3.9)}  # 注意：直接截断小数部分，不是四舍五入")
    print(f"e) int(True) = {int(True)}")

# 练习2：float()和complex()函数
def exercise_float_complex():
    print("\n练习2：float()和complex()函数")
    print("题目：")
    print("a) 将字符串'3.14159'转换为浮点数")
    print("b) 创建一个实部为2，虚部为3的复数")
    print("c) 将字符串'1+2j'转换为复数")
    print("d) 计算复数2+3j的模")
    
    # 参考答案
    print("\n参考答案：")
    print(f"a) float('3.14159') = {float('3.14159')}")
    print(f"b) complex(2, 3) = {complex(2, 3)}")
    print(f"c) complex('1+2j') = {complex('1+2j')}")
    c = complex(2, 3)
    print(f"d) abs(complex(2, 3)) = {abs(c)}")

# 练习3：字符串和字节转换
def exercise_str_bytes():
    print("\n练习3：字符串和字节转换")
    print("题目：")
    print("a) 将字符串'Hello, 世界'转换为UTF-8编码的字节")
    print("b) 将字节转换回字符串")
    print("c) 创建一个可变字节数组并修改其内容")
    
    # 参考答案
    print("\n参考答案：")
    s = 'Hello, 世界'
    b = s.encode('utf-8')
    print(f"a) '{s}'.encode('utf-8') = {b}")
    print(f"b) {b}.decode('utf-8') = {b.decode('utf-8')}")
    
    # 创建并修改字节数组
    ba = bytearray('hello', 'utf-8')
    original = bytes(ba)
    ba[0] = 72  # 将'h'改为'H'
    print(f"c) 原字节数组: {original}, 修改后: {ba}, 转换为字符串: {ba.decode('utf-8')}")

# 练习4：容器类型转换
def exercise_container_conversion():
    print("\n练习4：容器类型转换")
    print("题目：")
    print("a) 将字符串'python'转换为列表")
    print("b) 将列表[1, 2, 2, 3]转换为集合（去重）")
    print("c) 将字典{'a': 1, 'b': 2}的键值对转换为元组列表")
    print("d) 创建一个包含列表、元组、集合、字典的综合转换示例")
    
    # 参考答案
    print("\n参考答案：")
    print(f"a) list('python') = {list('python')}")
    print(f"b) set([1, 2, 2, 3]) = {set([1, 2, 2, 3])}")
    print(f"c) list({'a': 1, 'b': 2}.items()) = {list({'a': 1, 'b': 2}.items())}")
    
    # 综合转换
    data = '1,2,3,4,5'
    print(f"d) 综合转换示例:")
    print(f"   原始字符串: '{data}'")
    lst = data.split(',')
    print(f"   分割为列表: {lst}")
    lst_int = list(map(int, lst))
    print(f"   转换为整数列表: {lst_int}")
    tpl = tuple(lst_int)
    print(f"   转换为元组: {tpl}")
    unique_set = set(lst_int)
    print(f"   转换为集合: {unique_set}")

# ===========================
# 第二部分：数学函数练习
# ===========================
print("\n\n第二部分：数学函数练习")
print("-" * 50)

# 练习5：基本数学函数
def exercise_basic_math():
    print("\n练习5：基本数学函数")
    print("题目：计算以下表达式的值")
    print("a) abs(-15.7)")
    print("b) divmod(25, 4)")
    print("c) pow(2, 10)")
    print("d) pow(2, 10, 3)")
    print("e) round(3.14159, 2)")
    print("f) round(2.5) 和 round(3.5) 结果为什么不同？")
    
    # 参考答案
    print("\n参考答案：")
    print(f"a) abs(-15.7) = {abs(-15.7)}")
    print(f"b) divmod(25, 4) = {divmod(25, 4)}  # (商, 余数)")
    print(f"c) pow(2, 10) = {pow(2, 10)}")
    print(f"d) pow(2, 10, 3) = {pow(2, 10, 3)}  # (2^10) % 3")
    print(f"e) round(3.14159, 2) = {round(3.14159, 2)}")
    print(f"f) round(2.5) = {round(2.5)}, round(3.5) = {round(3.5)}")
    print("   解释：Python使用银行家舍入法（四舍六入五成偶），当小数部分为0.5时，")
    print("         舍入到最近的偶数。所以2.5舍入为2，3.5舍入为4。")

# 练习6：max()和min()函数
def exercise_max_min():
    print("\n练习6：max()和min()函数")
    print("题目：")
    print("a) 找出列表[34, 12, 89, 5, 67]中的最大值和最小值")
    print("b) 找出字典{'a': 10, 'b': 5, 'c': 15}中值最大的键值对")
    print("c) 找出字符串列表['apple', 'banana', 'cherry', 'date']中按长度最长的字符串")
    
    # 参考答案
    print("\n参考答案：")
    lst = [34, 12, 89, 5, 67]
    print(f"a) 列表{lst}中的最大值: {max(lst)}, 最小值: {min(lst)}")
    
    d = {'a': 10, 'b': 5, 'c': 15}
    max_item = max(d.items(), key=lambda x: x[1])
    print(f"b) 字典{d}中值最大的键值对: {max_item}")
    
    fruits = ['apple', 'banana', 'cherry', 'date']
    longest = max(fruits, key=len)
    print(f"c) 列表{fruits}中按长度最长的字符串: '{longest}'")

# ===========================
# 第三部分：集合操作函数练习
# ===========================
print("\n\n第三部分：集合操作函数练习")
print("-" * 50)

# 练习7：all()和any()函数
def exercise_all_any():
    print("\n练习7：all()和any()函数")
    print("题目：判断以下表达式的结果")
    print("a) all([True, True, False])")
    print("b) any([True, False, False])")
    print("c) all([])")
    print("d) any([])")
    print("e) 检查列表中的所有数字是否都为正数")
    print("f) 检查列表中是否包含至少一个偶数")
    
    # 参考答案
    print("\n参考答案：")
    print(f"a) all([True, True, False]) = {all([True, True, False])}")
    print(f"b) any([True, False, False]) = {any([True, False, False])}")
    print(f"c) all([]) = {all([])}  # 空迭代器返回True")
    print(f"d) any([]) = {any([])}  # 空迭代器返回False")
    
    numbers = [1, 3, 5, 7, 9]
    print(f"e) 列表{numbers}中的所有数字是否都为正数: {all(x > 0 for x in numbers)}")
    
    numbers2 = [1, 3, 5, 8, 9]
    print(f"f) 列表{numbers2}中是否包含至少一个偶数: {any(x % 2 == 0 for x in numbers2)}")

# 练习8：sum()和len()函数
def exercise_sum_len():
    print("\n练习8：sum()和len()函数")
    print("题目：")
    print("a) 计算列表[1, 2, 3, 4, 5]的总和和平均值")
    print("b) 计算嵌套列表[[1, 2], [3, 4], [5]]中所有元素的总和")
    print("c) 计算字典中所有值的总和")
    
    # 参考答案
    print("\n参考答案：")
    lst = [1, 2, 3, 4, 5]
    total = sum(lst)
    average = total / len(lst)
    print(f"a) 列表{lst}的总和: {total}, 平均值: {average}")
    
    nested_lst = [[1, 2], [3, 4], [5]]
    flat_sum = sum(sum(sublist) for sublist in nested_lst)
    print(f"b) 嵌套列表{nested_lst}中所有元素的总和: {flat_sum}")
    
    d = {'a': 10, 'b': 20, 'c': 30}
    values_sum = sum(d.values())
    print(f"c) 字典{d}中所有值的总和: {values_sum}")

# 练习9：sorted()函数
def exercise_sorted():
    print("\n练习9：sorted()函数")
    print("题目：")
    print("a) 对列表[5, 2, 9, 1, 5, 6]进行升序排序")
    print("b) 对列表[5, 2, 9, 1, 5, 6]进行降序排序")
    print("c) 对字符串列表按照字符串长度排序")
    print("d) 对字典列表按照某个键的值排序")
    
    # 参考答案
    print("\n参考答案：")
    lst = [5, 2, 9, 1, 5, 6]
    print(f"a) 列表{lst}升序排序: {sorted(lst)}")
    print(f"b) 列表{lst}降序排序: {sorted(lst, reverse=True)}")
    
    words = ['apple', 'banana', 'kiwi', 'watermelon']
    print(f"c) 列表{words}按长度排序: {sorted(words, key=len)}")
    
    people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_by_age = sorted(people, key=lambda x: x['age'])
    print(f"d) 按年龄排序的人员列表: {sorted_by_age}")

# ===========================
# 第四部分：迭代器和迭代工具练习
# ===========================
print("\n\n第四部分：迭代器和迭代工具练习")
print("-" * 50)

# 练习10：iter()和next()函数
def exercise_iter_next():
    print("\n练习10：iter()和next()函数")
    print("题目：")
    print("a) 创建一个列表迭代器并使用next()获取所有元素")
    print("b) 使用迭代器和try-except处理StopIteration异常")
    print("c) 使用next()函数的默认值参数")
    
    # 参考答案
    print("\n参考答案：")
    print("a) 创建迭代器并获取元素:")
    my_list = [10, 20, 30]
    my_iter = iter(my_list)
    print(f"   next(my_iter) = {next(my_iter)}")
    print(f"   next(my_iter) = {next(my_iter)}")
    print(f"   next(my_iter) = {next(my_iter)}")
    
    print("\nb) 处理StopIteration异常:")
    my_iter = iter(my_list)
    while True:
        try:
            item = next(my_iter)
            print(f"   迭代元素: {item}")
        except StopIteration:
            print("   迭代结束")
            break
    
    print("\nc) 使用next()的默认值参数:")
    my_iter = iter([1, 2])
    print(f"   next(my_iter, '默认值') = {next(my_iter, '默认值')}")
    print(f"   next(my_iter, '默认值') = {next(my_iter, '默认值')}")
    print(f"   next(my_iter, '默认值') = {next(my_iter, '默认值')}  # 迭代结束时返回默认值")

# 练习11：enumerate()函数
def exercise_enumerate():
    print("\n练习11：enumerate()函数")
    print("题目：")
    print("a) 使用enumerate遍历列表并打印索引和值")
    print("b) 使用enumerate从索引10开始遍历列表")
    print("c) 使用enumerate和列表推导式创建索引-值对字典")
    
    # 参考答案
    print("\n参考答案：")
    fruits = ['apple', 'banana', 'cherry']
    print("a) enumerate遍历示例:")
    for i, fruit in enumerate(fruits):
        print(f"   索引{i}: {fruit}")
    
    print("\nb) 从索引10开始遍历:")
    for i, fruit in enumerate(fruits, 10):
        print(f"   索引{i}: {fruit}")
    
    fruit_dict = {i: fruit for i, fruit in enumerate(fruits)}
    print(f"c) 索引-值对字典: {fruit_dict}")

# 练习12：range()函数
def exercise_range():
    print("\n练习12：range()函数")
    print("题目：生成以下序列")
    print("a) 0到9的整数")
    print("b) 5到15的整数（包括5和15）")
    print("c) 0到20的偶数")
    print("d) 10到1的递减序列")
    
    # 参考答案
    print("\n参考答案：")
    print(f"a) 0到9: {list(range(10))}")
    print(f"b) 5到15: {list(range(5, 16))}")
    print(f"c) 0到20的偶数: {list(range(0, 21, 2))}")
    print(f"d) 10到1递减: {list(range(10, 0, -1))}")

# 练习13：map()、filter()和zip()函数
def exercise_map_filter_zip():
    print("\n练习13：map()、filter()和zip()函数")
    print("题目：")
    print("a) 使用map()将列表中的所有数字乘以2")
    print("b) 使用filter()过滤出列表中的所有偶数")
    print("c) 使用zip()将两个列表配对成元组列表")
    print("d) 组合使用map()、filter()和sorted()处理数据")
    
    # 参考答案
    print("\n参考答案：")
    numbers = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, numbers))
    print(f"a) 数字列表{numbers}乘以2: {doubled}")
    
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"b) 列表{numbers}中的偶数: {evens}")
    
    names = ['Alice', 'Bob', 'Charlie']
    ages = [30, 25, 35]
    paired = list(zip(names, ages))
    print(f"c) 配对结果: {paired}")
    
    # 组合使用
    data = [5, 12, 8, 3, 15, 22]
    result = sorted(map(lambda x: x * 2, filter(lambda x: x > 5, data)))
    print(f"d) 组合处理: 过滤{data}中大于5的数，乘以2，然后排序: {result}")

# ===========================
# 第五部分：内存管理和对象操作练习
# ===========================
print("\n\n第五部分：内存管理和对象操作练习")
print("-" * 50)

# 练习14：id()、type()和isinstance()函数
def exercise_id_type_isinstance():
    print("\n练习14：id()、type()和isinstance()函数")
    print("题目：")
    print("a) 检查两个变量是否指向同一个对象")
    print("b) 使用type()检查对象的类型")
    print("c) 使用isinstance()检查对象是否为指定类型的实例")
    print("d) 理解小整数缓存机制")
    
    # 参考答案
    print("\n参考答案：")
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print(f"a) a和b是否指向同一对象: {a is b}")
    print(f"   a和c是否指向同一对象: {a is c}")
    print(f"   a的id: {id(a)}, b的id: {id(b)}, c的id: {id(c)}")
    
    print(f"b) 123的类型: {type(123)}")
    print(f"   'abc'的类型: {type('abc')}")
    print(f"   [1, 2]的类型: {type([1, 2])}")
    
    print(f"c) 123是否为int类型: {isinstance(123, int)}")
    print(f"   'abc'是否为(str, list)类型之一: {isinstance('abc', (str, list))}")
    print(f"   [1, 2]是否为(list, tuple)类型之一: {isinstance([1, 2], (list, tuple))}")
    
    print("d) 小整数缓存机制:")
    x = 200
    y = 200
    print(f"   x = 200, y = 200, x is y: {x is y}")
    # 在Python中，通常-5到256之间的整数会被缓存

# 练习15：hasattr()、getattr()、setattr()和delattr()函数
def exercise_attr_functions():
    print("\n练习15：属性操作函数")
    print("题目：")
    print("a) 创建一个类并使用属性操作函数动态管理其属性")
    print("b) 使用默认值获取可能不存在的属性")
    print("c) 检查并调用对象的方法")
    
    # 参考答案
    print("\n参考答案：")
    class Person:
        def __init__(self, name):
            self.name = name
        
        def greet(self):
            return f"Hello, I'm {self.name}"
    
    person = Person("Alice")
    print(f"a) 初始属性: name = {person.name}")
    
    # 动态添加属性
    setattr(person, "age", 30)
    print(f"   添加age属性后: age = {person.age}")
    
    # 检查属性是否存在
    print(f"   是否有gender属性: {hasattr(person, 'gender')}")
    print(f"   是否有name属性: {hasattr(person, 'name')}")
    
    print(f"b) 获取存在的属性: {getattr(person, 'name')}")
    print(f"   获取不存在的属性（带默认值）: {getattr(person, 'gender', 'Unknown')}")
    
    print(f"c) 检查并调用方法:")
    if hasattr(person, 'greet') and callable(getattr(person, 'greet')):
        print(f"   调用greet()方法: {getattr(person, 'greet')()}")
    
    # 删除属性
    delattr(person, 'age')
    print(f"   删除age属性后，是否还有age属性: {hasattr(person, 'age')}")

# ===========================
# 第六部分：输入输出函数练习
# ===========================
print("\n\n第六部分：输入输出函数练习")
print("-" * 50)

# 练习16：print()函数
def exercise_print():
    print("\n练习16：print()函数")
    print("题目：")
    print("a) 使用不同的分隔符打印多个值")
    print("b) 使用end参数自定义行尾字符")
    print("c) 将输出重定向到字符串")
    
    # 参考答案
    print("\n参考答案：")
    print(f"a) 使用逗号分隔: ", end="")
    print(1, 2, 3, 4)
    print(f"   使用'-'分隔: ", end="")
    print(1, 2, 3, 4, sep='-')
    print(f"   使用'\t'分隔: ", end="")
    print(1, 2, 3, 4, sep='\t')
    
    print(f"b) 自定义行尾字符: ", end="")
    print("Hello", end="!")
    print(" World", end="\\n")
    
    print("c) 输出重定向到字符串:")
    # 保存原始stdout
    old_stdout = sys.stdout
    # 创建一个StringIO对象
    mystdout = io.StringIO()
    # 重定向stdout
    sys.stdout = mystdout
    # 打印内容
    print("Hello, World!")
    print("This is a test.")
    # 恢复stdout
    sys.stdout = old_stdout
    # 获取输出内容
    output = mystdout.getvalue()
    print(f"   捕获的输出:\n{output}")

# 练习17：open()函数和文件操作
def exercise_open():
    print("\n练习17：open()函数和文件操作")
    print("题目：")
    print("a) 写入文本到文件")
    print("b) 读取文件内容")
    print("c) 使用with语句安全地处理文件")
    print("d) 追加内容到文件")
    
    # 参考答案
    print("\n参考答案：")
    filename = "test_file.txt"
    
    # 写入文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Hello, World!\n")
        f.write("This is a test file.\n")
    print(f"a) 已写入文件: {filename}")
    
    # 读取文件
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"b) 文件内容:\n{content}")
    
    # 追加内容
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("Appended line.\n")
    
    # 再次读取
    with open(filename, 'r', encoding='utf-8') as f:
        updated_content = f.read()
    print(f"d) 追加后的内容:\n{updated_content}")
    
    print("注意：实际操作中会在当前目录创建test_file.txt文件")

# ===========================
# 第七部分：其他实用函数练习
# ===========================
print("\n\n第七部分：其他实用函数练习")
print("-" * 50)

# 练习18：eval()和exec()函数
def exercise_eval_exec():
    print("\n练习18：eval()和exec()函数")
    print("题目：")
    print("a) 使用eval()计算数学表达式")
    print("b) 使用exec()执行多行Python代码")
    print("c) 理解eval()和exec()的区别")
    
    # 参考答案
    print("\n参考答案：")
    expression = "2 + 3 * 4"
    result = eval(expression)
    print(f"a) eval('{expression}') = {result}")
    
    # 在局部作用域中使用eval
    x = 10
    y = 5
    result2 = eval('x + y')
    print(f"   eval('x + y') 其中x={x}, y={y} = {result2}")
    
    print("b) 使用exec()执行多行代码:")
    code = '''
x = 10
y = 20
z = x + y
print(f"x + y = {z}")
'''
    print("   执行代码:")
    exec(code)
    
    print("c) eval()和exec()的区别:")
    print("   - eval()只能执行表达式并返回结果")
    print("   - exec()可以执行语句但不返回值")
    print("   - 两者都有安全风险，避免处理不可信输入")

# 练习19：format()函数
def exercise_format():
    print("\n练习19：format()函数")
    print("题目：使用format()函数格式化以下内容")
    print("a) 整数格式化（宽度为8，左对齐）")
    print("b) 浮点数格式化（保留2位小数）")
    print(c) 百分比格式化
    print("d) 日期格式化")
    
    # 参考答案
    print("\n参考答案：")
    num = 42
    print(f"a) 整数格式化: '{format(num, '<8d')}'")
    print(f"   零填充: '{format(num, '08d')}'")
    
    pi = 3.14159
    print(f"b) 浮点数格式化（2位小数）: {format(pi, '.2f')}")
    print(f"   科学计数法: {format(pi, '.2e')}")
    
    ratio = 0.75
    print(f"c) 百分比格式化: {format(ratio, '.1%')}")
    
    # 日期格式化（需要导入datetime）
    from datetime import datetime
    now = datetime.now()
    print(f"d) 日期格式化: {format(now, '%Y-%m-%d %H:%M:%S')}")

# 练习20：综合练习
def exercise_comprehensive():
    print("\n练习20：综合练习")
    print("题目：使用多个内置函数解决实际问题")
    print("场景：统计文本中单词频率并找出最常见的10个单词")
    
    # 示例文本
    text = "Python is a powerful programming language. Python is easy to learn and fun to use. "
    text += "Python has a large standard library. Python is used for web development, data analysis, "
    text += "artificial intelligence, and more. Python is loved by programmers around the world."
    
    print("\n参考答案：")
    print("1. 文本预处理:")
    # 转换为小写并移除标点符号
    text_lower = text.lower()
    for char in ",.!?;:":
        text_lower = text_lower.replace(char, "")
    
    # 分割成单词
    words = text_lower.split()
    print(f"   预处理后文本长度: {len(text_lower)}")
    print(f"   单词总数: {len(words)}")
    
    print("\n2. 计算单词频率:")
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    print(f"   不同单词数: {len(word_freq)}")
    
    print("\n3. 找出最常见的10个单词:")
    # 排序并获取前10个
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_words[:10]
    
    for i, (word, freq) in enumerate(top_10, 1):
        print(f"   {i}. '{word}': {freq}次")
    
    print("\n4. 计算单词频率的统计信息:")
    frequencies = list(word_freq.values())
    print(f"   最高频率: {max(frequencies)}")
    print(f"   最低频率: {min(frequencies)}")
    print(f"   平均频率: {sum(frequencies) / len(frequencies):.2f}")
    
    # 计算唯一出现的单词数
    unique_words = list(filter(lambda x: x == 1, frequencies))
    print(f"   只出现一次的单词数: {len(unique_words)}")

# 执行所有练习
if __name__ == "__main__":
    # 执行各部分练习
    try:
        exercise_int()
        exercise_float_complex()
        exercise_str_bytes()
        exercise_container_conversion()
        
        exercise_basic_math()
        exercise_max_min()
        
        exercise_all_any()
        exercise_sum_len()
        exercise_sorted()
        
        exercise_iter_next()
        exercise_enumerate()
        exercise_range()
        exercise_map_filter_zip()
        
        exercise_id_type_isinstance()
        exercise_attr_functions()
        
        exercise_print()
        exercise_open()
        
        exercise_eval_exec()
        exercise_format()
        exercise_comprehensive()
        
        print("\n\n=== 所有练习完成！===")
        print("通过这些练习，你应该已经掌握了Python所有内置函数的基本用法。")
        print("继续练习和实践是掌握编程技能的关键。")
        
    except Exception as e:
        print(f"执行过程中遇到错误: {e}")
