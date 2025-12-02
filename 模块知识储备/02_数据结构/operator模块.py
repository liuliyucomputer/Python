# Python operator模块详解

# 1. operator模块概述
print("=== 1. operator模块概述 ===")
print("operator模块提供了Python内置操作符的函数式接口，使得可以在函数式编程中使用这些操作符。")
print("该模块对于高阶函数、map/reduce等操作特别有用，可以避免编写匿名lambda函数。")
print("operator模块的核心功能包括：比较操作、算术操作、逻辑操作、序列操作、属性和元素访问操作等。")
print("使用operator模块可以使代码更简洁、更易读，并且在某些情况下提高性能。")
print()

# 2. operator模块核心函数
print("=== 2. operator模块核心函数 ===")

def operator_core_functions():
    """展示operator模块中的核心函数"""
    import operator
    
    print("1. 算术运算符:")
    print("   operator.add(a, b): 等价于 a + b")
    print("   operator.sub(a, b): 等价于 a - b")
    print("   operator.mul(a, b): 等价于 a * b")
    print("   operator.truediv(a, b): 等价于 a / b (Python 3中的真除法)")
    print("   operator.floordiv(a, b): 等价于 a // b (整除)")
    print("   operator.mod(a, b): 等价于 a % b (取模)")
    print("   operator.pow(a, b): 等价于 a ** b (幂运算)")
    print("   operator.neg(a): 等价于 -a (取负)")
    print("   operator.pos(a): 等价于 +a (取正)")
    print("   operator.abs(a): 等价于 abs(a) (绝对值)")
    
    # 算术运算符示例
    print("   \n算术运算符示例:")
    a, b = 10, 3
    print(f"   a = {a}, b = {b}")
    print(f"   operator.add(a, b) = {operator.add(a, b)}")
    print(f"   operator.sub(a, b) = {operator.sub(a, b)}")
    print(f"   operator.mul(a, b) = {operator.mul(a, b)}")
    print(f"   operator.truediv(a, b) = {operator.truediv(a, b)}")
    print(f"   operator.floordiv(a, b) = {operator.floordiv(a, b)}")
    print(f"   operator.mod(a, b) = {operator.mod(a, b)}")
    print(f"   operator.pow(a, b) = {operator.pow(a, b)}")
    print(f"   operator.neg(a) = {operator.neg(a)}")
    print(f"   operator.pos(a) = {operator.pos(a)}")
    print(f"   operator.abs(-a) = {operator.abs(-a)}")
    
    print("\n2. 比较运算符:")
    print("   operator.lt(a, b): 等价于 a < b")
    print("   operator.le(a, b): 等价于 a <= b")
    print("   operator.eq(a, b): 等价于 a == b")
    print("   operator.ne(a, b): 等价于 a != b")
    print("   operator.gt(a, b): 等价于 a > b")
    print("   operator.ge(a, b): 等价于 a >= b")
    
    # 比较运算符示例
    print("   \n比较运算符示例:")
    x, y = 5, 10
    print(f"   x = {x}, y = {y}")
    print(f"   operator.lt(x, y) = {operator.lt(x, y)}")
    print(f"   operator.le(x, y) = {operator.le(x, y)}")
    print(f"   operator.eq(x, y) = {operator.eq(x, y)}")
    print(f"   operator.ne(x, y) = {operator.ne(x, y)}")
    print(f"   operator.gt(x, y) = {operator.gt(x, y)}")
    print(f"   operator.ge(x, y) = {operator.ge(x, y)}")
    
    print("\n3. 逻辑运算符:")
    print("   operator.not_(a): 等价于 not a")
    print("   operator.and_(a, b): 等价于 a & b (按位与)")
    print("   operator.or_(a, b): 等价于 a | b (按位或)")
    print("   operator.xor(a, b): 等价于 a ^ b (按位异或)")
    print("   operator.invert(a): 等价于 ~a (按位取反)")
    
    # 逻辑运算符示例
    print("   \n逻辑运算符示例:")
    p, q = True, False
    print(f"   p = {p}, q = {q}")
    print(f"   operator.not_(p) = {operator.not_(p)}")
    
    # 按位操作
    m, n = 0b1010, 0b1100  # 十进制的10和12
    print(f"   m = {m} (二进制: 0b{m:04b}), n = {n} (二进制: 0b{n:04b})")
    print(f"   operator.and_(m, n) = {operator.and_(m, n)} (二进制: 0b{operator.and_(m, n):04b})")
    print(f"   operator.or_(m, n) = {operator.or_(m, n)} (二进制: 0b{operator.or_(m, n):04b})")
    print(f"   operator.xor(m, n) = {operator.xor(m, n)} (二进制: 0b{operator.xor(m, n):04b})")
    print(f"   operator.invert(m) = {operator.invert(m)} (二进制: {bin(operator.invert(m))})")
    
    print("\n4. 序列操作:")
    print("   operator.concat(a, b): 等价于 a + b (序列连接)")
    print("   operator.contains(a, b): 等价于 b in a")
    print("   operator.countOf(a, b): 计算b在a中出现的次数")
    print("   operator.indexOf(a, b): 查找b在a中第一次出现的索引")
    
    # 序列操作示例
    print("   \n序列操作示例:")
    list1, list2 = [1, 2, 3], [4, 5, 6]
    print(f"   list1 = {list1}, list2 = {list2}")
    print(f"   operator.concat(list1, list2) = {operator.concat(list1, list2)}")
    
    sequence = [1, 2, 3, 2, 1, 2, 3]
    element = 2
    print(f"   sequence = {sequence}, element = {element}")
    print(f"   operator.contains(sequence, element) = {operator.contains(sequence, element)}")
    print(f"   operator.countOf(sequence, element) = {operator.countOf(sequence, element)}")
    print(f"   operator.indexOf(sequence, element) = {operator.indexOf(sequence, element)}")
    
    # 字符串操作
    string = "hello world"
    substr = "world"
    print(f"   string = '{string}', substr = '{substr}'")
    print(f"   operator.contains(string, substr) = {operator.contains(string, substr)}")
    print(f"   operator.indexOf(string, 'o') = {operator.indexOf(string, 'o')}")
    
    print("\n5. 元素访问操作:")
    print("   operator.getitem(a, b): 等价于 a[b] (获取索引/键对应的值)")
    print("   operator.setitem(a, b, c): 等价于 a[b] = c (设置索引/键对应的值)")
    print("   operator.delitem(a, b): 等价于 del a[b] (删除索引/键对应的值)")
    print("   operator.itemgetter(*items): 返回一个函数，该函数从对象中获取指定的项")
    
    # 元素访问操作示例
    print("   \n元素访问操作示例:")
    # 列表索引访问
    my_list = ['a', 'b', 'c', 'd']
    print(f"   my_list = {my_list}")
    print(f"   operator.getitem(my_list, 2) = {operator.getitem(my_list, 2)}")
    
    # 修改列表
    operator.setitem(my_list, 1, 'x')
    print(f"   执行operator.setitem(my_list, 1, 'x')后: {my_list}")
    
    # 删除列表元素
    operator.delitem(my_list, 3)
    print(f"   执行operator.delitem(my_list, 3)后: {my_list}")
    
    # 字典键访问
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(f"   my_dict = {my_dict}")
    print(f"   operator.getitem(my_dict, 'b') = {operator.getitem(my_dict, 'b')}")
    
    # itemgetter示例
    print("   \nitemgetter示例:")
    # 创建一个获取索引1和2的函数
    get_second_third = operator.itemgetter(1, 2)
    print(f"   get_second_third = operator.itemgetter(1, 2)")
    print(f"   get_second_third([10, 20, 30, 40]) = {get_second_third([10, 20, 30, 40])}")
    
    # 使用itemgetter获取字典值
    get_name_age = operator.itemgetter('name', 'age')
    person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    print(f"   person = {person}")
    print(f"   get_name_age(person) = {get_name_age(person)}")
    
    print("\n6. 属性访问操作:")
    print("   operator.attrgetter(*attrs): 返回一个函数，该函数获取对象的指定属性")
    print("   operator.attrgetter可以链式获取属性，例如attrgetter('a.b.c')")
    
    # 属性访问操作示例
    print("   \n属性访问操作示例:")
    # 定义一个简单的类
    class Person:
        def __init__(self, name, age, address):
            self.name = name
            self.age = age
            self.address = address
    
    class Address:
        def __init__(self, city, country):
            self.city = city
            self.country = country
    
    # 创建对象
    address = Address('Beijing', 'China')
    person = Person('Bob', 25, address)
    
    # 使用attrgetter
    get_name = operator.attrgetter('name')
    get_age = operator.attrgetter('age')
    get_city = operator.attrgetter('address.city')
    get_name_age = operator.attrgetter('name', 'age')
    
    print(f"   person = Person(name='Bob', age=25, address=Address('Beijing', 'China'))")
    print(f"   get_name(person) = '{get_name(person)}'")
    print(f"   get_age(person) = {get_age(person)}")
    print(f"   get_city(person) = '{get_city(person)}'")
    print(f"   get_name_age(person) = {get_name_age(person)}")
    
    print("\n7. 函数调用操作:")
    print("   operator.call(a, *args, **kwargs): 等价于 a(*args, **kwargs) (调用对象)")
    
    # 函数调用操作示例
    print("   \n函数调用操作示例:")
    # 定义一个函数
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    # 使用call调用函数
    result1 = operator.call(greet, "Alice")
    result2 = operator.call(greet, "Bob", greeting="Hi")
    
    print(f"   def greet(name, greeting='Hello'): return f'{greeting}, {name}!'")
    print(f"   operator.call(greet, 'Alice') = '{result1}'")
    print(f"   operator.call(greet, 'Bob', greeting='Hi') = '{result2}'")
    
    # 使用call调用对象的方法
    print(f"   operator.call(person.__init__, person, 'Charlie', 35, address) = {operator.call(person.__init__, person, 'Charlie', 35, address)}")
    print(f"   修改后的person.name = '{person.name}'")

operator_core_functions()
print()

# 3. operator模块在函数式编程中的应用
print("=== 3. operator模块在函数式编程中的应用 ===")

def operator_functional_programming():
    """operator模块在函数式编程中的应用示例"""
    import operator
    import functools
    
    print("1. 与map()配合使用:")
    print("   使用operator函数替代lambda函数与map配合，代码更简洁高效")
    
    # 使用operator.add代替lambda x, y: x + y
    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = [10, 20, 30, 40, 50]
    
    # 使用lambda
    result_lambda = list(map(lambda x, y: x + y, numbers1, numbers2))
    
    # 使用operator.add
    result_operator = list(map(operator.add, numbers1, numbers2))
    
    print(f"   numbers1 = {numbers1}")
    print(f"   numbers2 = {numbers2}")
    print(f"   使用lambda: {result_lambda}")
    print(f"   使用operator.add: {result_operator}")
    
    # 计算平方
    squares_lambda = list(map(lambda x: x ** 2, numbers1))
    squares_operator = list(map(operator.pow, numbers1, [2]*len(numbers1)))
    
    print(f"   \n计算平方:")
    print(f"   使用lambda: {squares_lambda}")
    print(f"   使用operator.pow: {squares_operator}")
    
    print("\n2. 与filter()配合使用:")
    print("   使用operator函数替代lambda函数与filter配合")
    
    # 过滤偶数
    even_lambda = list(filter(lambda x: x % 2 == 0, numbers1))
    
    # 使用operator.mod和operator.eq的组合（需要额外的函数包装）
    def is_even(x):
        return operator.eq(operator.mod(x, 2), 0)
    
    even_operator = list(filter(is_even, numbers1))
    
    print(f"   numbers1 = {numbers1}")
    print(f"   使用lambda过滤偶数: {even_lambda}")
    print(f"   使用operator过滤偶数: {even_operator}")
    
    # 检查元素是否在集合中
    allowed_values = {2, 4, 6, 8}
    
    # 使用lambda
    filtered_lambda = list(filter(lambda x: x in allowed_values, numbers1))
    
    # 使用operator.contains
    filtered_operator = list(filter(lambda x: operator.contains(allowed_values, x), numbers1))
    
    print(f"   \nallowed_values = {allowed_values}")
    print(f"   使用lambda过滤允许的值: {filtered_lambda}")
    print(f"   使用operator.contains过滤允许的值: {filtered_operator}")
    
    print("\n3. 与functools.reduce()配合使用:")
    print("   operator函数特别适合与reduce配合，避免编写匿名lambda函数")
    
    # 计算列表元素的总和
    numbers = [1, 2, 3, 4, 5]
    
    # 使用lambda
    sum_lambda = functools.reduce(lambda x, y: x + y, numbers)
    
    # 使用operator.add
    sum_operator = functools.reduce(operator.add, numbers)
    
    print(f"   numbers = {numbers}")
    print(f"   使用lambda计算总和: {sum_lambda}")
    print(f"   使用operator.add计算总和: {sum_operator}")
    
    # 计算列表元素的乘积
    product_lambda = functools.reduce(lambda x, y: x * y, numbers)
    product_operator = functools.reduce(operator.mul, numbers)
    
    print(f"   \n使用lambda计算乘积: {product_lambda}")
    print(f"   使用operator.mul计算乘积: {product_operator}")
    
    # 查找列表中的最大值
    max_lambda = functools.reduce(lambda x, y: x if x > y else y, numbers)
    max_operator = functools.reduce(operator.gt, numbers, float('-inf'))  # 注意：这里需要调整
    
    # 更正最大值计算方式
    def max_op(x, y):
        return x if operator.gt(x, y) else y
    max_operator_correct = functools.reduce(max_op, numbers)
    
    print(f"   \n使用lambda查找最大值: {max_lambda}")
    print(f"   使用operator.gt查找最大值: {max_operator_correct}")
    
    print("\n4. 使用itemgetter进行排序:")
    print("   itemgetter在排序操作中特别有用，可以根据对象的特定字段进行排序")
    
    # 定义一个人员列表
    people = [
        {'name': 'Alice', 'age': 30, 'score': 85},
        {'name': 'Bob', 'age': 25, 'score': 90},
        {'name': 'Charlie', 'age': 35, 'score': 80},
        {'name': 'David', 'age': 25, 'score': 95}
    ]
    
    # 使用lambda根据年龄排序
    sorted_by_age_lambda = sorted(people, key=lambda x: x['age'])
    
    # 使用itemgetter根据年龄排序
    sorted_by_age_operator = sorted(people, key=operator.itemgetter('age'))
    
    print(f"   人员列表: {people}")
    print("   \n根据年龄排序:")
    print(f"   使用lambda: {[p['name'] + '-' + str(p['age']) for p in sorted_by_age_lambda]}")
    print(f"   使用itemgetter: {[p['name'] + '-' + str(p['age']) for p in sorted_by_age_operator]}")
    
    # 多级排序：先按年龄，再按分数
    sorted_by_age_score_lambda = sorted(people, key=lambda x: (x['age'], x['score']))
    sorted_by_age_score_operator = sorted(people, key=operator.itemgetter('age', 'score'))
    
    print("   \n多级排序（先年龄，再分数）:")
    print(f"   使用lambda: {[p['name'] + '-' + str(p['age']) + '-' + str(p['score']) for p in sorted_by_age_score_lambda]}")
    print(f"   使用itemgetter: {[p['name'] + '-' + str(p['age']) + '-' + str(p['score']) for p in sorted_by_age_score_operator]}")
    
    # 降序排序
    sorted_by_score_desc_lambda = sorted(people, key=lambda x: x['score'], reverse=True)
    sorted_by_score_desc_operator = sorted(people, key=operator.itemgetter('score'), reverse=True)
    
    print("   \n根据分数降序排序:")
    print(f"   使用lambda: {[p['name'] + '-' + str(p['score']) for p in sorted_by_score_desc_lambda]}")
    print(f"   使用itemgetter: {[p['name'] + '-' + str(p['score']) for p in sorted_by_score_desc_operator]}")
    
    print("\n5. 使用attrgetter进行对象排序:")
    print("   当排序对象是自定义类的实例时，attrgetter特别有用")
    
    # 定义一个简单的类
    class Student:
        def __init__(self, name, age, grade):
            self.name = name
            self.age = age
            self.grade = grade
        
        def __repr__(self):
            return f"Student(name='{self.name}', age={self.age}, grade={self.grade})"
    
    # 创建学生对象列表
    students = [
        Student('Alice', 20, 'A'),
        Student('Bob', 19, 'B'),
        Student('Charlie', 21, 'A'),
        Student('David', 19, 'A')
    ]
    
    # 使用lambda根据成绩排序
    sorted_by_grade_lambda = sorted(students, key=lambda x: x.grade)
    
    # 使用attrgetter根据成绩排序
    sorted_by_grade_operator = sorted(students, key=operator.attrgetter('grade'))
    
    print(f"   学生列表: {students}")
    print("   \n根据成绩排序:")
    print(f"   使用lambda: {sorted_by_grade_lambda}")
    print(f"   使用attrgetter: {sorted_by_grade_operator}")
    
    # 多级排序：先按成绩，再按年龄
    sorted_by_grade_age_lambda = sorted(students, key=lambda x: (x.grade, x.age))
    sorted_by_grade_age_operator = sorted(students, key=operator.attrgetter('grade', 'age'))
    
    print("   \n多级排序（先成绩，再年龄）:")
    print(f"   使用lambda: {sorted_by_grade_age_lambda}")
    print(f"   使用attrgetter: {sorted_by_grade_age_operator}")
    
    print("\n6. 在高阶函数中的应用:")
    print("   operator函数可以作为高阶函数的参数，提供更简洁的代码")
    
    # 定义一个应用操作符的函数
    def apply_operation(op, a, b):
        return op(a, b)
    
    # 使用不同的操作符
    add_result = apply_operation(operator.add, 5, 3)
    sub_result = apply_operation(operator.sub, 5, 3)
    mul_result = apply_operation(operator.mul, 5, 3)
    
    print(f"   定义函数: def apply_operation(op, a, b): return op(a, b)")
    print(f"   apply_operation(operator.add, 5, 3) = {add_result}")
    print(f"   apply_operation(operator.sub, 5, 3) = {sub_result}")
    print(f"   apply_operation(operator.mul, 5, 3) = {mul_result}")
    
    # 创建一个操作符映射字典
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    
    # 使用映射执行不同的操作
    def calculate(operation, a, b):
        if operation in operations:
            return operations[operation](a, b)
        else:
            raise ValueError(f"不支持的操作: {operation}")
    
    print(f"   \n操作符映射: {operations}")
    print(f"   calculate('+', 10, 5) = {calculate('+', 10, 5)}")
    print(f"   calculate('-', 10, 5) = {calculate('-', 10, 5)}")
    print(f"   calculate('*', 10, 5) = {calculate('*', 10, 5)}")
    print(f"   calculate('/', 10, 5) = {calculate('/', 10, 5)}")

operator_functional_programming()
print()

# 4. 高级应用示例
print("=== 4. 高级应用示例 ===")

def operator_advanced_examples():
    """operator模块的高级应用示例"""
    import operator
    import functools
    import itertools
    
    print("示例1: 创建自定义排序键")
    print("   使用itemgetter和自定义函数组合创建复杂的排序键")
    
    # 定义一个包含嵌套结构的数据列表
    data = [
        {'name': 'Alice', 'scores': {'math': 85, 'english': 92}},
        {'name': 'Bob', 'scores': {'math': 95, 'english': 88}},
        {'name': 'Charlie', 'scores': {'math': 85, 'english': 90}},
        {'name': 'David', 'scores': {'math': 92, 'english': 95}}
    ]
    
    # 创建一个获取数学成绩的函数
    get_math_score = operator.itemgetter('scores', 'math')
    
    # 根据数学成绩排序
    sorted_by_math = sorted(data, key=lambda x: get_math_score(x), reverse=True)
    
    print(f"   数据列表: {data}")
    print("   \n根据数学成绩降序排序:")
    for item in sorted_by_math:
        print(f"     {item['name']}: 数学成绩 = {item['scores']['math']}")
    
    # 多级排序：先按数学成绩，再按英语成绩
    def get_scores(item):
        return (item['scores']['math'], item['scores']['english'])
    
    sorted_by_both_scores = sorted(data, key=get_scores, reverse=True)
    
    print("   \n多级排序（先数学成绩，再英语成绩）:")
    for item in sorted_by_both_scores:
        print(f"     {item['name']}: 数学 = {item['scores']['math']}, 英语 = {item['scores']['english']}")
    
    print("\n示例2: 创建属性访问链")
    print("   使用attrgetter处理复杂的对象关系")
    
    # 定义嵌套类
    class Department:
        def __init__(self, name, location):
            self.name = name
            self.location = location
    
    class Employee:
        def __init__(self, name, department):
            self.name = name
            self.department = department
    
    # 创建对象
    dept1 = Department("Engineering", "Building A")
    dept2 = Department("Marketing", "Building B")
    
    employees = [
        Employee("Alice", dept1),
        Employee("Bob", dept2),
        Employee("Charlie", dept1),
        Employee("David", dept2)
    ]
    
    # 使用attrgetter获取部门位置
    get_dept_location = operator.attrgetter('department.location')
    
    # 根据部门位置排序
    sorted_by_location = sorted(employees, key=get_dept_location)
    
    print("   员工和部门信息:")
    for emp in sorted_by_location:
        print(f"     {emp.name} - {emp.department.name} - {get_dept_location(emp)}")
    
    # 按部门名称和员工名称排序
    sorted_by_dept_and_name = sorted(employees, key=lambda x: (x.department.name, x.name))
    
    print("   \n按部门名称和员工名称排序:")
    for emp in sorted_by_dept_and_name:
        print(f"     {emp.name} - {emp.department.name}")
    
    print("\n示例3: 在数据处理管道中的应用")
    print("   结合operator模块和函数式编程工具创建数据处理管道")
    
    # 定义销售数据
    sales_data = [
        {'product': 'A', 'price': 10, 'quantity': 5},
        {'product': 'B', 'price': 20, 'quantity': 3},
        {'product': 'C', 'price': 15, 'quantity': 4},
        {'product': 'D', 'price': 25, 'quantity': 2}
    ]
    
    # 1. 计算每个产品的总销售额
    def calculate_total(item):
        # 使用operator.mul计算总价
        item['total'] = operator.mul(item['price'], item['quantity'])
        return item
    
    # 2. 过滤销售额大于50的产品
    def filter_high_sales(item):
        # 使用operator.gt进行比较
        return operator.gt(item['total'], 50)
    
    # 3. 按产品名称排序
    get_product_name = operator.itemgetter('product')
    
    # 创建数据处理管道
    processed_data = (
        calculate_total(item) for item in sales_data  # 生成器表达式
    )
    filtered_data = filter(filter_high_sales, processed_data)
    sorted_data = sorted(filtered_data, key=get_product_name)
    
    print("   销售数据处理管道:")
    print("   1. 计算每个产品的总销售额")
    print("   2. 过滤销售额大于50的产品")
    print("   3. 按产品名称排序")
    print("   \n处理结果:")
    for item in sorted_data:
        print(f"     产品 {item['product']}: {item['total']}元 (单价:{item['price']}, 数量:{item['quantity']})")
    
    # 计算总销售额
    total_sales = functools.reduce(
        operator.add, 
        (item['total'] for item in sales_data)
    )
    
    print(f"   \n总销售额: {total_sales}元")
    
    print("\n示例4: 动态属性访问和修改")
    print("   使用operator模块动态地访问和修改对象的属性")
    
    # 定义一个配置类
    class Config:
        def __init__(self):
            self.debug = False
            self.log_level = "INFO"
            self.timeout = 30
    
    # 创建配置对象
    config = Config()
    
    # 动态获取属性
    print("   初始配置:")
    config_attrs = ['debug', 'log_level', 'timeout']
    for attr in config_attrs:
        # 使用getattr函数获取属性值
        value = getattr(config, attr)
        print(f"     {attr}: {value}")
    
    # 动态设置属性
    config_updates = {
        'debug': True,
        'log_level': 'DEBUG',
        'timeout': 60
    }
    
    print("   \n应用配置更新:")
    for attr, value in config_updates.items():
        # 使用setattr函数设置属性值
        setattr(config, attr, value)
        print(f"     {attr} -> {value}")
    
    # 使用attrgetter批量获取属性
    get_config_values = operator.attrgetter(*config_attrs)
    values = get_config_values(config)
    
    print("   \n更新后的配置:")
    for attr, value in zip(config_attrs, values):
        print(f"     {attr}: {value}")
    
    print("\n示例5: 创建通用的比较器")
    print("   使用operator模块创建通用的对象比较器")
    
    # 定义一个通用的比较器类
    class Comparator:
        def __init__(self, key_func=None, reverse=False):
            self.key_func = key_func if key_func is not None else lambda x: x
            self.reverse = reverse
            
        def compare(self, a, b):
            # 获取比较键
            key_a = self.key_func(a)
            key_b = self.key_func(b)
            
            # 使用operator模块进行比较
            if operator.lt(key_a, key_b):
                return -1 if not self.reverse else 1
            elif operator.gt(key_a, key_b):
                return 1 if not self.reverse else -1
            else:
                return 0
    
    # 测试数据
    products = [
        {'name': 'Laptop', 'price': 1000, 'rating': 4.5},
        {'name': 'Phone', 'price': 500, 'rating': 4.7},
        {'name': 'Tablet', 'price': 300, 'rating': 4.3},
        {'name': 'Monitor', 'price': 200, 'rating': 4.6}
    ]
    
    # 创建按价格排序的比较器
    price_comparator = Comparator(key_func=operator.itemgetter('price'))
    
    # 创建按评分降序排序的比较器
    rating_comparator_desc = Comparator(
        key_func=operator.itemgetter('rating'), 
        reverse=True
    )
    
    # 使用比较器排序
    sorted_by_price = sorted(products, key=functools.cmp_to_key(price_comparator.compare))
    sorted_by_rating = sorted(products, key=functools.cmp_to_key(rating_comparator_desc.compare))
    
    print("   产品列表: {products}")
    print("   \n按价格排序:")
    for product in sorted_by_price:
        print(f"     {product['name']}: {product['price']}元")
    
    print("   \n按评分降序排序:")
    for product in sorted_by_rating:
        print(f"     {product['name']}: {product['rating']}分")
    
    # 自定义多字段比较器
    def get_sort_key(product):
        return (-product['rating'], product['price'])  # 先按评分降序，再按价格升序
    
    multi_field_comparator = Comparator(key_func=get_sort_key)
    sorted_by_multi = sorted(products, key=functools.cmp_to_key(multi_field_comparator.compare))
    
    print("   \n按评分降序和价格升序排序:")
    for product in sorted_by_multi:
        print(f"     {product['name']}: {product['rating']}分, {product['price']}元")

operator_advanced_examples()
print()

# 5. 性能考虑
print("=== 5. 性能考虑 ===")

def operator_performance_considerations():
    """operator模块的性能考虑"""
    import operator
    import functools
    import time
    import random
    
    print("1. operator函数 vs lambda函数")
    print("   operator函数通常比等效的lambda函数更高效，因为operator使用C实现")
    
    # 测试数据
    size = 1000000
    numbers1 = [random.randint(1, 100) for _ in range(size)]
    numbers2 = [random.randint(1, 100) for _ in range(size)]
    
    # 测试operator.add vs lambda
    start_time = time.time()
    sum_lambda = sum(map(lambda x, y: x + y, numbers1, numbers2))
    lambda_time = time.time() - start_time
    
    start_time = time.time()
    sum_operator = sum(map(operator.add, numbers1, numbers2))
    operator_time = time.time() - start_time
    
    print(f"   数据规模: {size}对数字")
    print(f"   lambda函数耗时: {lambda_time:.6f}秒")
    print(f"   operator.add耗时: {operator_time:.6f}秒")
    print(f"   operator比lambda快: {lambda_time/operator_time:.2f}倍")
    
    print("\n2. itemgetter vs lambda函数")
    print("   itemgetter在获取元素时通常比lambda更高效")
    
    # 准备测试数据
    size = 500000
    data = [{'id': i, 'value': random.randint(1, 1000)} for i in range(size)]
    
    # 测试lambda排序
    start_time = time.time()
    sorted_lambda = sorted(data, key=lambda x: x['value'])
    lambda_time = time.time() - start_time
    
    # 测试itemgetter排序
    start_time = time.time()
    sorted_itemgetter = sorted(data, key=operator.itemgetter('value'))
    itemgetter_time = time.time() - start_time
    
    print(f"   数据规模: {size}个字典元素")
    print(f"   lambda排序耗时: {lambda_time:.6f}秒")
    print(f"   itemgetter排序耗时: {itemgetter_time:.6f}秒")
    print(f"   itemgetter比lambda快: {lambda_time/itemgetter_time:.2f}倍")
    
    print("\n3. attrgetter vs lambda函数")
    print("   attrgetter在访问对象属性时通常比lambda更高效")
    
    # 定义一个简单的类
    class Item:
        def __init__(self, id, value):
            self.id = id
            self.value = value
    
    # 准备测试数据
    size = 500000
    items = [Item(i, random.randint(1, 1000)) for i in range(size)]
    
    # 测试lambda排序
    start_time = time.time()
    sorted_lambda = sorted(items, key=lambda x: x.value)
    lambda_time = time.time() - start_time
    
    # 测试attrgetter排序
    start_time = time.time()
    sorted_attrgetter = sorted(items, key=operator.attrgetter('value'))
    attrgetter_time = time.time() - start_time
    
    print(f"   数据规模: {size}个对象")
    print(f"   lambda排序耗时: {lambda_time:.6f}秒")
    print(f"   attrgetter排序耗时: {attrgetter_time:.6f}秒")
    print(f"   attrgetter比lambda快: {lambda_time/attrgetter_time:.2f}倍")
    
    print("\n4. 多级排序性能")
    print("   对于多级排序，itemgetter和attrgetter的优势更加明显")
    
    # 准备更复杂的测试数据
    size = 300000
    complex_data = [
        {'category': random.choice(['A', 'B', 'C']), 
         'subcategory': random.randint(1, 5), 
         'value': random.randint(1, 1000)}
        for _ in range(size)
    ]
    
    # 测试lambda多级排序
    start_time = time.time()
    sorted_lambda = sorted(complex_data, key=lambda x: (x['category'], x['subcategory'], x['value']))
    lambda_time = time.time() - start_time
    
    # 测试itemgetter多级排序
    start_time = time.time()
    sorted_itemgetter = sorted(complex_data, key=operator.itemgetter('category', 'subcategory', 'value'))
    itemgetter_time = time.time() - start_time
    
    print(f"   数据规模: {size}个复杂字典元素")
    print(f"   lambda多级排序耗时: {lambda_time:.6f}秒")
    print(f"   itemgetter多级排序耗时: {itemgetter_time:.6f}秒")
    print(f"   itemgetter比lambda快: {lambda_time/itemgetter_time:.2f}倍")
    
    print("\n5. 使用场景建议")
    print("   1. 对于性能敏感的应用，特别是处理大规模数据时，优先使用operator模块")
    print("   2. 在函数式编程中，使用operator模块可以获得更好的性能和可读性")
    print("   3. 在需要进行大量排序操作的场景中，itemgetter和attrgetter是更好的选择")
    print("   4. 对于简单的、非性能关键的操作，lambda函数仍然是方便的选择")
    
    # 测试functools.reduce与operator的性能
    print("\n6. functools.reduce与operator组合的性能")
    
    # 准备测试数据
    size = 2000000
    large_numbers = [random.randint(1, 10) for _ in range(size)]
    
    # 测试lambda与reduce
    start_time = time.time()
    sum_lambda_reduce = functools.reduce(lambda x, y: x + y, large_numbers)
    lambda_reduce_time = time.time() - start_time
    
    # 测试operator与reduce
    start_time = time.time()
    sum_operator_reduce = functools.reduce(operator.add, large_numbers)
    operator_reduce_time = time.time() - start_time
    
    print(f"   数据规模: {size}个数字")
    print(f"   lambda+reduce耗时: {lambda_reduce_time:.6f}秒")
    print(f"   operator.add+reduce耗时: {operator_reduce_time:.6f}秒")
    print(f"   operator+reduce比lambda+reduce快: {lambda_reduce_time/operator_reduce_time:.2f}倍")

# 注意：由于性能测试可能会耗费一定时间，这里注释掉实际执行，只保留示例代码
print("注意：完整的性能测试代码已提供，但在文档模式下不会实际执行以避免耗时")
print("在实际使用时，您可以取消下面的注释来运行性能测试")
# operator_performance_considerations()
print()

# 6. 注意事项和常见问题
print("=== 6. 注意事项和常见问题 ===")

def operator_caveats():
    """operator模块的注意事项和常见问题"""
    import operator
    import functools
    
    print("1. 操作符函数的参数顺序")
    print("   注意操作符函数的参数顺序，特别是减法、除法等非交换操作符")
    
    a, b = 10, 5
    print(f"   a = {a}, b = {b}")
    print(f"   operator.sub(a, b) = {operator.sub(a, b)}  # 相当于 a - b")
    print(f"   operator.sub(b, a) = {operator.sub(b, a)}  # 相当于 b - a")
    print(f"   operator.truediv(a, b) = {operator.truediv(a, b)}  # 相当于 a / b")
    print(f"   operator.truediv(b, a) = {operator.truediv(b, a)}  # 相当于 b / a")
    
    print("\n2. 按位操作与逻辑操作的区别")
    print("   operator模块中的and_、or_等是按位操作，不是逻辑操作")
    
    x, y = True, False
    print(f"   x = {x}, y = {y}")
    print(f"   x and y = {x and y}  # 逻辑与")
    print(f"   operator.and_(1, 0) = {operator.and_(1, 0)}  # 按位与 (True=1, False=0)")
    print()
    print(f"   x or y = {x or y}  # 逻辑或")
    print(f"   operator.or_(1, 0) = {operator.or_(1, 0)}  # 按位或")
    
    print("\n3. itemgetter和attrgetter的局限性")
    print("   这些函数只能进行简单的属性或元素访问，不能执行复杂的计算")
    
    # 定义一个类
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
        
        @property
        def area(self):
            return self.width * self.height
    
    rect = Rectangle(5, 10)
    
    # 可以访问简单属性
    get_dimensions = operator.attrgetter('width', 'height')
    print(f"   rect = Rectangle(5, 10)")
    print(f"   get_dimensions(rect) = {get_dimensions(rect)}")
    
    # 也可以访问属性方法
    get_area = operator.attrgetter('area')
    print(f"   get_area(rect) = {get_area(rect)}")
    
    print("   \n但是对于需要计算的情况，如width*2，则需要使用lambda")
    # 这将不起作用：get_double_width = operator.attrgetter('width*2')
    # 应该使用lambda: get_double_width = lambda x: x.width * 2
    
    print("\n4. 链式属性访问的限制")
    print("   attrgetter支持链式属性访问，但只能访问直接的属性链，不支持方法调用")
    
    # 定义嵌套类
    class Address:
        def __init__(self, city):
            self.city = city
    
    class Person:
        def __init__(self, name, address):
            self.name = name
            self.address = address
        
        def get_name_upper(self):
            return self.name.upper()
    
    address = Address("Beijing")
    person = Person("Alice", address)
    
    # 支持链式属性访问
    get_city = operator.attrgetter('address.city')
    print(f"   person = Person('Alice', Address('Beijing'))")
    print(f"   get_city(person) = '{get_city(person)}'")
    
    print("   \n但不支持方法调用")
    # 这将不起作用：get_upper_name = operator.attrgetter('get_name_upper()')
    # 应该使用lambda: get_upper_name = lambda x: x.get_name_upper()
    
    print("\n5. 版本兼容性问题")
    print("   大多数operator函数在Python 2和Python 3中都可用，但有一些差异需要注意")
    print("   - Python 3中的truediv对应Python 2中的div")
    print("   - Python 3中移除了部分不常用的函数")
    
    print("\n6. 常见问题与解决方案")
    print("\n问题1: itemgetter不能处理动态计算的键")
    print("解决方案: 结合itemgetter和lambda函数")
    
    # 示例：根据动态计算的键排序
    data = [
        {'a': 1, 'b': 2},
        {'a': 3, 'b': 1},
        {'a': 2, 'b': 3}
    ]
    
    # 根据a和b的和排序
    sorted_data = sorted(data, key=lambda x: (x['a'] + x['b']))
    print(f"   data = {data}")
    print(f"   根据a+b排序: {sorted_data}")
    
    print("\n问题2: 如何在多级排序中混合升序和降序")
    print("解决方案: 使用lambda函数调整排序键")
    
    # 示例：先按a升序，再按b降序
    mixed_sorted = sorted(data, key=lambda x: (x['a'], -x['b']))
    print(f"   先按a升序，再按b降序: {mixed_sorted}")
    
    print("\n问题3: 如何在操作符函数中处理自定义对象")
    print("解决方案: 确保自定义对象实现了相应的特殊方法")
    
    # 定义一个自定义类，实现__add__方法
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)
        
        def __repr__(self):
            return f"Vector({self.x}, {self.y})"
    
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    
    # 可以使用operator.add
    v3 = operator.add(v1, v2)
    print(f"   v1 = {v1}, v2 = {v2}")
    print(f"   operator.add(v1, v2) = {v3}")
    
    print("\n问题4: 如何在map函数中使用多参数操作符")
    print("解决方案: 使用zip或itertools.starmap")
    
    import itertools
    
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]
    
    # 使用map和zip
    result1 = list(map(operator.add, numbers1, numbers2))
    
    # 使用itertools.starmap
    pairs = list(zip(numbers1, numbers2))
    result2 = list(itertools.starmap(operator.add, pairs))
    
    print(f"   numbers1 = {numbers1}, numbers2 = {numbers2}")
    print(f"   使用map: {result1}")
    print(f"   使用starmap: {result2}")
    
    print("\n问题5: 如何创建一个自定义的操作符映射表")
    print("解决方案: 使用字典将操作符名称映射到对应的operator函数")
    
    # 创建操作符映射
    ops_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '>': operator.gt,
        '<': operator.lt,
        '==': operator.eq
    }
    
    # 使用映射执行操作
    def apply_op(op_str, a, b):
        if op_str in ops_map:
            return ops_map[op_str](a, b)
        else:
            raise ValueError(f"不支持的操作: {op_str}")
    
    print(f"   操作符映射: {list(ops_map.keys())}")
    print(f"   apply_op('+', 5, 3) = {apply_op('+', 5, 3)}")
    print(f"   apply_op('*', 5, 3) = {apply_op('*', 5, 3)}")
    print(f"   apply_op('>', 5, 3) = {apply_op('>', 5, 3)}")

operator_caveats()
print()

# 7. 总结和最佳实践
print("=== 7. 总结和最佳实践 ===")

def operator_summary():
    """operator模块总结和最佳实践"""
    
    print("1. operator模块的核心优势")
    print("   • 提供了Python操作符的函数式接口，便于在函数式编程中使用")
    print("   • 大多数操作符函数是用C实现的，执行效率高于等效的lambda函数")
    print("   • 代码更简洁、更易读，特别是在复杂的数据处理场景中")
    print("   • itemgetter和attrgetter对于排序和数据提取操作特别有用")
    
    print("\n2. 最佳实践")
    print("   • 在性能敏感的应用中，优先使用operator模块替代lambda函数")
    print("   • 对于简单的属性或元素访问，使用itemgetter和attrgetter")
    print("   • 在需要多级排序时，itemgetter和attrgetter比lambda更高效")
    print("   • 与functools.reduce配合使用时，operator函数可以显著提高性能")
    print("   • 在创建通用算法或框架时，使用operator模块可以增加代码的灵活性")
    
    print("\n3. 使用建议")
    print("   • 对于简单的、一次性的操作，lambda函数仍然是方便的选择")
    print("   • 对于复杂的计算，组合使用operator函数和自定义函数")
    print("   • 在团队协作中，确保所有成员都理解operator模块的用法")
    print("   • 对于频繁访问的属性或元素，考虑使用itemgetter或attrgetter缓存结果")
    
    print("\n4. 核心应用场景")
    print("   • 函数式编程：与map、filter、reduce等函数配合使用")
    print("   • 数据排序：特别是多级排序和复杂对象排序")
    print("   • 数据转换：创建通用的数据处理管道")
    print("   • 动态操作：基于运行时输入选择不同的操作符")
    print("   • 元编程：在运行时动态生成操作")
    
    print("\n5. 输入输出示例")
    print("   示例1: 基本算术操作")
    print("   输入:")
    print("     import operator")
    print("     x, y = 10, 5")
    print("     print(f'Add: {operator.add(x, y)}')")
    print("     print(f'Subtract: {operator.sub(x, y)}')")
    print("     print(f'Multiply: {operator.mul(x, y)}')")
    print("     print(f'Divide: {operator.truediv(x, y)}')")
    print("   输出:")
    print("     Add: 15")
    print("     Subtract: 5")
    print("     Multiply: 50")
    print("     Divide: 2.0")
    
    print("\n   示例2: 使用itemgetter排序")
    print("   输入:")
    print("     import operator")
    print("     people = [")
    print("         {'name': 'Alice', 'age': 30, 'score': 85},")
    print("         {'name': 'Bob', 'age': 25, 'score': 90},")
    print("         {'name': 'Charlie', 'age': 35, 'score': 80}")
    print("     ]")
    print("     sorted_by_age = sorted(people, key=operator.itemgetter('age'))")
    print("     print(sorted_by_age)")
    print("   输出:")
    print("     [{'name': 'Bob', 'age': 25, 'score': 90}, ")
    print("      {'name': 'Alice', 'age': 30, 'score': 85}, ")
    print("      {'name': 'Charlie', 'age': 35, 'score': 80}]")
    
    print("\n   示例3: 与functools.reduce配合")
    print("   输入:")
    print("     import operator")
    print("     import functools")
    print("     numbers = [1, 2, 3, 4, 5]")
    print("     total = functools.reduce(operator.add, numbers)")
    print("     product = functools.reduce(operator.mul, numbers)")
    print("     print(f'Total: {total}')")
    print("     print(f'Product: {product}')")
    print("   输出:")
    print("     Total: 15")
    print("     Product: 120")
    
    print("\n6. 完整导入指南")
    print("   基本导入:")
    print("     import operator")
    print("   ")
    print("   导入特定函数:")
    print("     from operator import add, sub, mul, truediv")
    print("     from operator import itemgetter, attrgetter")
    print("   ")
    print("   常用导入组合:")
    print("     # 用于数据处理和排序")
    print("     from operator import itemgetter, attrgetter")
    print("     ")
    print("     # 用于函数式编程")
    print("     from operator import add, mul")
    print("     from functools import reduce")
    print("   ")
    print("   版本兼容性:")
    print("     • 所有核心函数在Python 2.7+和Python 3.x中均可使用")
    print("     • 在Python 3中，'div'被重命名为'truediv'")
    print("     • Python 3.8+添加了一些新的操作符函数")
    
    print("\n总结: operator模块是Python函数式编程的重要工具，通过提供操作符的函数式接口，")
    print("可以使代码更简洁、更高效。在需要大量使用操作符的场景中，尤其是排序和数据处理，")
    print("operator模块可以显著提高代码质量和性能。")

operator_summary()
print()

# 运行模块中的演示函数
if __name__ == "__main__":
    print("开始运行operator模块演示...")
    print("===================================")
    
    # 我们已经在模块主体中展示了大部分功能，这里再做一个简单的演示
    import operator
    
    print("快速演示:")
    print("1. 基本操作:")
    print(f"   5 + 3 = {operator.add(5, 3)}")
    print(f"   5 - 3 = {operator.sub(5, 3)}")
    print(f"   5 * 3 = {operator.mul(5, 3)}")
    print(f"   5 / 3 = {operator.truediv(5, 3)}")
    
    print("\n2. 排序演示:")
    data = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 90},
        {'name': 'Charlie', 'score': 80}
    ]
    sorted_data = sorted(data, key=operator.itemgetter('score'), reverse=True)
    print(f"   按分数降序: {[(d['name'], d['score']) for d in sorted_data]}")
    
    print("\noperator模块演示完成。")
    print("===================================")
