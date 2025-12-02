# collections.namedtuple模块 - Python标准库中的命名元组

"""
collections.namedtuple是Python标准库中的一个工厂函数，用于创建具有命名字段的元组子类。

namedtuple结合了元组的不可变性和字典的可读性，允许通过名称而不仅仅是位置索引来访问元素。

它在需要轻量级类来存储数据而不需要完整类的方法定义的场景中特别有用。
"""

# 1. 核心功能介绍

print("=== 1. 核心功能介绍 ===")
print("\ncollections.namedtuple模块提供了以下主要功能:")
print("1. 创建具有命名字段的元组子类")
print("2. 支持通过名称和索引访问元素")
print("3. 保持元组的不可变性")
print("4. 支持所有元组操作（解包、迭代等）")
print("5. 比普通类更节省内存")
print("6. 提供良好的字符串表示形式")
print("7. 支持转换为字典和其他数据结构")

# 2. 基本操作

print("\n=== 2. 基本操作 ===")

# 导入namedtuple
from collections import namedtuple

print("\n2.1 创建namedtuple类")
print("可以通过多种方式创建namedtuple类:")

# 基本方式创建namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])
print(f"创建的namedtuple类: {Person.__name__}")
print(f"字段名称: {Person._fields}")

# 使用字符串指定字段名（空格或逗号分隔）
Point = namedtuple('Point', 'x y z')
print(f"使用空格分隔字段: {Point._fields}")

Contact = namedtuple('Contact', 'name, email, phone')
print(f"使用逗号分隔字段: {Contact._fields}")

# 使用rename=True参数处理非法字段名
# 非法字段名将被自动重命名为'_索引'
InvalidFields = namedtuple('InvalidFields', ['class', 'def', '123'], rename=True)
print(f"重命名后的字段: {InvalidFields._fields}")

print("\n2.2 创建实例")
print("创建namedtuple实例的方法:")

# 基本方式创建实例
person1 = Person(name='Alice', age=30, city='New York')
print(f"使用关键字参数: {person1}")

# 使用位置参数创建实例
person2 = Person('Bob', 25, 'Boston')
print(f"使用位置参数: {person2}")

# 从列表或元组解包创建
person_data = ['Charlie', 35, 'Chicago']
person3 = Person(*person_data)
print(f"从列表解包: {person3}")

# 从字典创建（使用**解包）
person_dict = {'name': 'David', 'age': 40, 'city': 'Dallas'}
person4 = Person(**person_dict)
print(f"从字典解包: {person4}")

print("\n2.3 访问元素")
print("可以通过字段名或索引访问namedtuple元素:")

point = Point(10, 20, 30)

# 通过字段名访问
print(f"x坐标: {point.x}")
print(f"y坐标: {point.y}")
print(f"z坐标: {point.z}")

# 通过索引访问（与普通元组相同）
print(f"x坐标(索引0): {point[0]}")
print(f"y坐标(索引1): {point[1]}")
print(f"z坐标(索引2): {point[2]}")

# 迭代访问
print(f"迭代访问: {list(point)}")

# 解包（与普通元组相同）
x, y, z = point
print(f"解包后的坐标: x={x}, y={y}, z={z}")

print("\n2.4 基本方法")
print("namedtuple提供了一些有用的内置方法:")

person = Person('Eve', 28, 'Los Angeles')

# _asdict() - 转换为OrderedDict
person_dict = person._asdict()
print(f"转换为字典: {person_dict}")
print(f"类型: {type(person_dict)}")

# _replace() - 创建修改后的新实例（不修改原实例）
new_person = person._replace(age=29, city='San Francisco')
print(f"原实例: {person}")
print(f"修改后的新实例: {new_person}")

# _make() - 从可迭代对象创建实例
new_person2 = Person._make(['Frank', 33, 'Seattle'])
print(f"从可迭代对象创建: {new_person2}")

# _fields - 获取字段名
print(f"字段名: {person._fields}")

# _field_defaults - 获取字段默认值（Python 3.6+）
# 先定义带有默认值的namedtuple
Employee = namedtuple('Employee', ['name', 'id', 'department', 'salary'], defaults=['IT', 50000])
print(f"字段默认值: {Employee._field_defaults}")

# 使用默认值创建实例
emp1 = Employee('Grace', 1001)
print(f"使用部分默认值: {emp1}")

print("\n2.5 不可变性")
print("与普通元组一样，namedtuple实例也是不可变的:")

point = Point(10, 20, 30)
print(f"原始point: {point}")

try:
    # 尝试修改字段值（会引发AttributeError）
    point.x = 100
except AttributeError as e:
    print(f"修改失败: {e}")

try:
    # 尝试通过索引修改（会引发TypeError）
    point[0] = 100
except TypeError as e:
    print(f"通过索引修改失败: {e}")

# 正确的修改方式：创建新实例
new_point = point._replace(x=100)
print(f"修改后的新point: {new_point}")

# 3. 高级用法

print("\n=== 3. 高级用法 ===")

print("\n3.1 带默认值的namedtuple")
print("Python 3.6+版本中，namedtuple支持为字段指定默认值:")

# 定义带默认值的namedtuple
Product = namedtuple('Product', ['name', 'price', 'category', 'in_stock'], defaults=['General', True])
print(f"Product字段默认值: {Product._field_defaults}")

# 使用默认值创建实例
product1 = Product('Laptop', 999.99)
product2 = Product('Mouse', 19.99, 'Accessories')
product3 = Product('Keyboard', 49.99, in_stock=False)

print(f"product1: {product1}")
print(f"product2: {product2}")
print(f"product3: {product3}")

print("\n3.2 继承namedtuple")
print("可以创建namedtuple的子类来添加自定义方法:")

class ExtendedPoint(Point):
    """Point的扩展类，添加了一些实用方法"""
    
    def distance_to_origin(self):
        """计算到原点的距离"""
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    def distance_to(self, other):
        """计算到另一个点的距离"""
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5
    
    def __str__(self):
        """自定义字符串表示"""
        return f"Point3D({self.x}, {self.y}, {self.z})"

# 创建扩展点实例
p1 = ExtendedPoint(3, 4, 0)
p2 = ExtendedPoint(0, 0, 0)

print(f"p1: {p1}")
print(f"p1到原点的距离: {p1.distance_to_origin()}")
print(f"p1到p2的距离: {p1.distance_to(p2)}")

print("\n3.3 嵌套namedtuple")
print("namedtuple可以嵌套使用，创建复杂的数据结构:")

# 定义地址namedtuple
Address = namedtuple('Address', ['street', 'city', 'state', 'zip_code'])

# 定义联系人namedtuple，包含Address
ContactInfo = namedtuple('ContactInfo', ['name', 'email', 'phone', 'address'])

# 创建嵌套实例
address = Address('123 Main St', 'Anytown', 'CA', '12345')
contact = ContactInfo('John Doe', 'john@example.com', '555-1234', address)

print(f"联系人信息: {contact}")
print(f"联系人城市: {contact.address.city}")
print(f"联系人邮编: {contact.address.zip_code}")

print("\n3.4 使用类型注解")
print("可以为namedtuple添加类型注解，提高代码的可读性和类型检查:")

# 使用typing模块添加类型注解
from typing import NamedTuple, Optional

class PersonWithType(NamedTuple):
    """带类型注解的Person类"""
    name: str
    age: int
    city: str
    email: Optional[str] = None

# 创建带类型注解的实例
person_with_type = PersonWithType('Jane Smith', 32, 'Portland', 'jane@example.com')
print(f"带类型注解的person: {person_with_type}")

# 注意：使用NamedTuple时，字段默认值需要在类体中定义
class Config(NamedTuple):
    """配置类"""
    host: str = 'localhost'
    port: int = 8000
    debug: bool = False

config = Config(port=9000)
print(f"配置: {config}")

print("\n3.5 转换和序列化")
print("namedtuple可以方便地与其他数据结构进行转换:")

# 创建namedtuple实例
student = namedtuple('Student', ['id', 'name', 'grades'])(1, 'Alice', [95, 87, 92])

# 转换为字典
student_dict = student._asdict()
print(f"转换为字典: {student_dict}")

# 转换为元组
student_tuple = tuple(student)
print(f"转换为元组: {student_tuple}")

# 转换为列表
student_list = list(student)
print(f"转换为列表: {student_list}")

# JSON序列化
import json

# 注意：需要先转换为字典
student_json = json.dumps(student_dict)
print(f"JSON序列化: {student_json}")

# JSON反序列化
restored_dict = json.loads(student_json)
restored_student = namedtuple('Student', restored_dict.keys())(**restored_dict)
print(f"JSON反序列化: {restored_student}")

print("\n3.6 命名元组作为字典键")
print("由于namedtuple是不可变的，可以作为字典的键:")

# 创建点的namedtuple
Point2D = namedtuple('Point2D', ['x', 'y'])

# 使用namedtuple作为字典键
points_data = {
    Point2D(0, 0): '原点',
    Point2D(1, 0): 'x轴',
    Point2D(0, 1): 'y轴',
    Point2D(1, 1): '对角点'
}

print(f"点字典: {points_data}")
print(f"Point(0,0)的值: {points_data[Point2D(0, 0)]}")
print(f"Point(1,1)的值: {points_data[Point2D(1, 1)]}")

# 4. 实际应用场景

print("\n=== 4. 实际应用场景 ===")

print("\n4.1 数据记录")
print("namedtuple非常适合表示数据库记录、CSV行数据等结构化数据:")

print("\n示例: 处理CSV数据")

# 模拟CSV数据
csv_data = [
    'id,name,age,city',
    '1,Alice,30,New York',
    '2,Bob,25,Boston',
    '3,Charlie,35,Chicago'
]

def process_csv_data(csv_lines):
    """处理CSV数据并转换为namedtuple列表"""
    # 解析表头
    headers = csv_lines[0].split(',')
    
    # 创建namedtuple类
    Record = namedtuple('Record', headers)
    
    # 解析数据行
    records = []
    for line in csv_lines[1:]:
        values = line.split(',')
        # 类型转换
        values[0] = int(values[0])  # id转整数
        values[2] = int(values[2])  # age转整数
        records.append(Record(*values))
    
    return records

# 处理CSV数据
records = process_csv_data(csv_data)
print(f"处理后的记录:")
for record in records:
    print(f"  {record.name} (ID: {record.id}, Age: {record.age}) 住在 {record.city}")

print("\n4.2 配置管理")
print("namedtuple可以用于表示配置信息，提供类型安全和良好的可读性:")

print("\n示例: 应用配置")

AppConfig = namedtuple('AppConfig', ['host', 'port', 'debug', 'log_level', 'max_connections'], 
                     defaults=['localhost', 8000, False, 'INFO', 100])

# 创建配置实例
config = AppConfig(debug=True, log_level='DEBUG')
print(f"应用配置:")
print(f"  主机: {config.host}")
print(f"  端口: {config.port}")
print(f"  调试模式: {config.debug}")
print(f"  日志级别: {config.log_level}")
print(f"  最大连接数: {config.max_connections}")

print("\n4.3 枚举替代方案")
print("namedtuple可以用作更强大的枚举替代方案，提供额外的字段和功能:")

print("\n示例: HTTP状态码")

HTTPStatus = namedtuple('HTTPStatus', ['code', 'message', 'description'])

# 定义HTTP状态码
HTTP_STATUS = {
    'OK': HTTPStatus(200, 'OK', '请求成功'),
    'BAD_REQUEST': HTTPStatus(400, 'Bad Request', '请求无效'),
    'UNAUTHORIZED': HTTPStatus(401, 'Unauthorized', '需要身份验证'),
    'FORBIDDEN': HTTPStatus(403, 'Forbidden', '服务器拒绝访问'),
    'NOT_FOUND': HTTPStatus(404, 'Not Found', '请求的资源不存在'),
    'INTERNAL_ERROR': HTTPStatus(500, 'Internal Server Error', '服务器内部错误')
}

# 使用HTTP状态码
status = HTTP_STATUS['NOT_FOUND']
print(f"状态码: {status.code}")
print(f"状态消息: {status.message}")
print(f"状态描述: {status.description}")
print(f"完整表示: {status}")

print("\n4.4 函数返回多个值")
print("当函数需要返回多个相关值时，namedtuple提供了比普通元组更好的可读性:")

print("\n示例: 计算统计信息")

def calculate_stats(numbers):
    """计算数值列表的统计信息"""
    if not numbers:
        return None
    
    # 导入必要的模块
    import statistics
    
    # 创建统计结果namedtuple
    Stats = namedtuple('Stats', ['count', 'mean', 'median', 'std_dev', 'min', 'max'])
    
    # 计算统计信息
    return Stats(
        count=len(numbers),
        mean=statistics.mean(numbers),
        median=statistics.median(numbers),
        std_dev=statistics.stdev(numbers) if len(numbers) > 1 else 0,
        min=min(numbers),
        max=max(numbers)
    )

# 测试函数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats = calculate_stats(numbers)

print(f"统计信息:")
print(f"  数量: {stats.count}")
print(f"  平均值: {stats.mean}")
print(f"  中位数: {stats.median}")
print(f"  标准差: {stats.std_dev}")
print(f"  最小值: {stats.min}")
print(f"  最大值: {stats.max}")

print("\n4.5 数据传输对象")
print("在应用程序的不同部分之间传递数据时，namedtuple可以作为轻量级的数据传输对象:")

print("\n示例: 数据传输对象")

# 定义数据传输对象
UserDTO = namedtuple('UserDTO', ['user_id', 'username', 'email', 'roles'])

# 模拟从数据库获取用户
class UserRepository:
    @staticmethod
    def get_user_by_id(user_id):
        # 模拟数据库查询
        return {
            'id': user_id,
            'username': f'user{user_id}',
            'email': f'user{user_id}@example.com',
            'password_hash': 'hashed_password',  # 敏感信息
            'roles': ['user']
        }

# 模拟服务层
class UserService:
    @staticmethod
    def get_user_dto(user_id):
        # 从数据库获取用户
        db_user = UserRepository.get_user_by_id(user_id)
        
        # 转换为DTO（不包含敏感信息）
        return UserDTO(
            user_id=db_user['id'],
            username=db_user['username'],
            email=db_user['email'],
            roles=db_user['roles']
        )

# 使用服务获取DTO
user_dto = UserService.get_user_dto(1)
print(f"用户DTO: {user_dto}")
print(f"用户名: {user_dto.username}")
print(f"角色: {user_dto.roles}")

print("\n4.6 与标准库配合使用")
print("namedtuple可以与Python的其他标准库很好地配合使用:")

print("\n示例: 与csv模块配合")

try:
    import csv
    from io import StringIO
    
    # 模拟CSV数据
    csv_content = '''name,age,city
Alice,30,New York
Bob,25,Boston
Charlie,35,Chicago'''
    
    # 创建CSV reader
    reader = csv.reader(StringIO(csv_content))
    
    # 获取表头
    headers = next(reader)
    
    # 创建namedtuple类
    Person = namedtuple('Person', headers)
    
    # 解析数据
    people = [Person(*row) for row in reader]
    
    print(f"解析后的CSV数据:")
    for person in people:
        print(f"  {person.name}, {person.age}岁, 来自{person.city}")
        
except ImportError:
    print("CSV模块不可用")

print("\n4.7 单元测试中的数据表示")
print("在单元测试中，namedtuple可以用于表示测试数据和期望结果:")

print("\n示例: 单元测试数据")

# 定义测试用例namedtuple
TestCase = namedtuple('TestCase', ['input_data', 'expected_output', 'description'])

# 创建测试用例
math_test_cases = [
    TestCase(input_data=(2, 3), expected_output=5, description="正数相加"),
    TestCase(input_data=(-2, 3), expected_output=1, description="负数与正数相加"),
    TestCase(input_data=(-2, -3), expected_output=-5, description="负数相加"),
    TestCase(input_data=(0, 0), expected_output=0, description="零相加")
]

# 模拟测试函数
def test_addition(test_cases):
    print("执行加法测试:")
    for i, case in enumerate(test_cases):
        a, b = case.input_data
        result = a + b
        status = "通过" if result == case.expected_output else "失败"
        print(f"  测试{i+1}: {case.description} - {status}")
        print(f"    输入: {case.input_data}, 期望: {case.expected_output}, 实际: {result}")

# 执行测试
test_addition(math_test_cases)

# 5. 性能分析

print("\n=== 5. 性能分析 ===")

print("\n5.1 内存效率")
print("namedtuple比普通类更节省内存，因为它不存储实例字典:")

class RegularClass:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# 创建namedtuple类
PersonTuple = namedtuple('PersonTuple', ['name', 'age', 'city'])

# 创建实例
regular_obj = RegularClass('Alice', 30, 'New York')
tuple_obj = PersonTuple('Alice', 30, 'New York')

print(f"普通类实例的__dict__: {regular_obj.__dict__}")
print(f"namedtuple实例占用的内存更少，因为它没有__dict__属性")

print("\n5.2 访问速度")
print("namedtuple的字段访问速度通常比普通类稍快，与元组相当:")
print("  - namedtuple通过属性名访问接近元组通过索引访问的速度")
print("  - 比普通类通过属性访问略快，因为不需要查找__dict__")
print("  - 比字典通过键访问快得多")

print("\n5.3 与其他数据结构的比较")
print("namedtuple与其他数据结构的比较:")
print("  - 与普通元组相比: namedtuple可读性更好，可以通过名称访问，但功能略有增加")
print("  - 与普通类相比: namedtuple更节省内存，字段访问更快，但不可变")
print("  - 与字典相比: namedtuple占用内存更少，字段访问更快，但不可变且需要预先定义字段")
print("  - 与dataclass相比: dataclass提供更多功能但内存占用更大，而namedtuple更轻量")

print("\n5.4 性能优化建议")
print("使用namedtuple时的性能优化建议:")
print("  - 对于大量实例，namedtuple比普通类更高效")
print("  - 对于频繁访问字段的场景，namedtuple性能更好")
print("  - 对于需要序列化/反序列化的场景，namedtuple提供了便捷的方法")
print("  - 如果需要字段的可变性，考虑使用dataclass或普通类")
print("  - 使用_fields和_field_defaults等属性可以在运行时检查namedtuple的结构")

# 6. 使用注意事项

print("\n=== 6. 使用注意事项 ===")

print("\n6.1 不可变性限制")
print("namedtuple实例是不可变的，一旦创建就不能修改其字段值:")

Person = namedtuple('Person', ['name', 'age'])
p = Person('Alice', 30)

print(f"原始实例: {p}")
try:
    p.age = 31
except AttributeError as e:
    print(f"修改失败: {e}")

# 正确的修改方式：创建新实例
new_p = p._replace(age=31)
print(f"新实例: {new_p}")

print("\n6.2 字段名限制")
print("namedtuple的字段名需要遵循Python标识符规则:")
print("  - 不能是Python关键字（如class、def、if等）")
print("  - 不能以数字开头")
print("  - 不能包含空格或特殊字符（下划线除外）")
print("  - 可以使用rename=True参数自动重命名非法字段名")

# 示例：非法字段名
BadFieldTuple = namedtuple('BadFieldTuple', ['class', '123abc'], rename=True)
print(f"重命名后的字段名: {BadFieldTuple._fields}")

print("\n6.3 嵌套结构的不可变性")
print("namedtuple的不可变性只适用于顶层字段，如果字段包含可变对象（如列表、字典），这些对象仍然可以修改:")

# 创建包含可变对象的namedtuple
Data = namedtuple('Data', ['id', 'values'])
data = Data(1, [1, 2, 3])

print(f"原始数据: {data}")
# 修改列表内容（这是允许的）
data.values.append(4)
print(f"修改后的列表: {data}")

# 如何防止这种情况：使用不可变对象
from copy import deepcopy
DataImmutable = namedtuple('DataImmutable', ['id', 'values'])
data_immutable = DataImmutable(1, tuple([1, 2, 3]))  # 使用元组代替列表
print(f"使用不可变对象: {data_immutable}")

print("\n6.4 默认值的限制")
print("在Python 3.6之前，namedtuple不支持默认值:")
print("  - 如果需要在旧版本中使用默认值，可以创建一个自定义工厂函数")
print("  - 默认值必须从右往左定义（不能只为中间的字段设置默认值）")

print("\n示例: 为旧版本Python提供默认值")

def create_person_with_defaults(name, age=30, city='Unknown'):
    """创建Person实例的工厂函数，提供默认值"""
    Person = namedtuple('Person', ['name', 'age', 'city'])
    return Person(name, age, city)

# 使用工厂函数
person1 = create_person_with_defaults('Alice')
person2 = create_person_with_defaults('Bob', 25)
person3 = create_person_with_defaults('Charlie', 35, 'Chicago')

print(f"使用默认值创建: {person1}")
print(f"部分覆盖默认值: {person2}")
print(f"全部指定值: {person3}")

print("\n6.5 继承和扩展")
print("当继承namedtuple时，需要注意一些限制:")
print("  - 子类如果有__init__方法，需要调用父类的__init__")
print("  - 由于namedtuple的不可变性，不能在子类中添加可变的实例属性")
print("  - 如果需要添加方法，应该使用常规的方法定义")

# 示例：正确继承namedtuple
class ExtendedPerson(Person):
    """Person的扩展类"""
    
    def is_adult(self):
        """检查是否成年"""
        return self.age >= 18
    
    def greet(self):
        """返回问候语"""
        return f"Hello, my name is {self.name}!"

# 使用扩展类
ext_person = ExtendedPerson('David', 28)
print(f"扩展类实例: {ext_person}")
print(f"是否成年: {ext_person.is_adult()}")
print(f"问候: {ext_person.greet()}")

print("\n6.6 序列化注意事项")
print("在序列化namedtuple时，需要注意以下几点:")
print("  - 直接序列化namedtuple可能会丢失字段名信息")
print("  - 推荐先使用_asdict()方法转换为字典再序列化")
print("  - 反序列化时，需要知道namedtuple的结构才能正确恢复")

print("\n示例: 正确序列化和反序列化")

import json

# 定义namedtuple
Book = namedtuple('Book', ['title', 'author', 'year'])
book = Book('Python Programming', 'John Smith', 2023)

# 正确序列化
book_dict = book._asdict()
book_json = json.dumps(book_dict)
print(f"序列化结果: {book_json}")

# 正确反序列化
restored_dict = json.loads(book_json)
restored_book = Book(**restored_dict)
print(f"反序列化结果: {restored_book}")

# 7. 综合示例：简单的ORM映射系统

print("\n=== 7. 综合示例：简单的ORM映射系统 ===")

print("\n实现一个使用namedtuple的简单ORM映射系统，用于将数据库记录映射到Python对象:")

from collections import namedtuple
from typing import Dict, List, Any, Optional, Type

class ModelMeta(type):
    """
    模型元类，用于自动创建namedtuple类
    """
    def __new__(mcs, name, bases, attrs):
        # 跳过基类
        if name == 'Model':
            return super().__new__(mcs, name, bases, attrs)
        
        # 获取字段信息
        fields = attrs.get('__fields__', [])
        field_defaults = attrs.get('__field_defaults__', {})
        
        # 创建namedtuple类
        tuple_class = namedtuple(f"{name}Tuple", fields, defaults=list(field_defaults.values()) if field_defaults else None)
        
        # 保存tuple_class到属性中
        attrs['_tuple_class'] = tuple_class
        attrs['_field_defaults'] = field_defaults
        
        return super().__new__(mcs, name, bases, attrs)

class Model(metaclass=ModelMeta):
    """
    基础模型类
    """
    __fields__ = []
    __field_defaults__ = {}
    __table__ = ""
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Model':
        """
        从字典创建模型实例
        
        Args:
            data: 包含字段值的字典
        
        Returns:
            模型实例
        """
        # 过滤出有效的字段
        filtered_data = {k: v for k, v in data.items() if k in cls.__fields__}
        
        # 创建namedtuple实例
        tuple_instance = cls._tuple_class(**filtered_data)
        
        # 创建模型实例并设置tuple属性
        instance = cls()
        instance._data = tuple_instance
        
        return instance
    
    @classmethod
    def from_row(cls, row: tuple) -> 'Model':
        """
        从数据库行创建模型实例
        
        Args:
            row: 数据库行元组
        
        Returns:
            模型实例
        """
        # 创建namedtuple实例
        tuple_instance = cls._tuple_class(*row)
        
        # 创建模型实例并设置tuple属性
        instance = cls()
        instance._data = tuple_instance
        
        return instance
    
    def to_dict(self) -> Dict[str, Any]:
        """
        将模型实例转换为字典
        
        Returns:
            包含字段值的字典
        """
        return self._data._asdict()
    
    def __getattr__(self, name: str) -> Any:
        """
        代理属性访问到namedtuple
        """
        if name in self.__fields__:
            return getattr(self._data, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    
    def __setattr__(self, name: str, value: Any) -> None:
        """
        防止修改实例属性
        """
        if name == '_data':
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object attribute '{name}' is read-only")
    
    def __str__(self) -> str:
        """
        字符串表示
        """
        return f"{self.__class__.__name__}({', '.join(f'{k}={v}' for k, v in self._data._asdict().items())})"
    
    def __repr__(self) -> str:
        """
        正式表示
        """
        return self.__str__()

# 定义具体的模型类
class User(Model):
    """
    用户模型
    """
    __table__ = "users"
    __fields__ = ['id', 'username', 'email', 'first_name', 'last_name', 'created_at', 'is_active']
    __field_defaults__ = {'is_active': True}
    
    def full_name(self) -> str:
        """
        获取用户全名
        """
        return f"{self.first_name} {self.last_name}"
    
    def to_dict_public(self) -> Dict[str, Any]:
        """
        返回不包含敏感信息的字典
        """
        data = self.to_dict()
        # 移除可能的敏感字段
        return {k: v for k, v in data.items() if k not in ['id', 'email']}

class Product(Model):
    """
    产品模型
    """
    __table__ = "products"
    __fields__ = ['id', 'name', 'description', 'price', 'stock', 'category', 'created_at', 'updated_at']
    __field_defaults__ = {'stock': 0}
    
    def is_in_stock(self) -> bool:
        """
        检查产品是否有库存
        """
        return self.stock > 0
    
    def get_discounted_price(self, discount: float = 0.1) -> float:
        """
        获取折扣价格
        
        Args:
            discount: 折扣比例（0-1之间）
        
        Returns:
            折扣后的价格
        """
        return self.price * (1 - discount)

class Order(Model):
    """
    订单模型
    """
    __table__ = "orders"
    __fields__ = ['id', 'user_id', 'total_amount', 'status', 'created_at', 'shipping_address']
    __field_defaults__ = {'status': 'pending'}
    
    def is_completed(self) -> bool:
        """
        检查订单是否已完成
        """
        return self.status == 'completed'
    
    def get_shipping_city(self) -> Optional[str]:
        """
        从配送地址中提取城市
        """
        # 假设shipping_address是一个包含城市信息的字典
        if isinstance(self.shipping_address, dict):
            return self.shipping_address.get('city')
        return None

# 模拟数据库
class Database:
    """
    简单的模拟数据库类
    """
    
    def __init__(self):
        """
        初始化数据库
        """
        self.users = [
            (1, 'alice', 'alice@example.com', 'Alice', 'Smith', '2023-01-01', True),
            (2, 'bob', 'bob@example.com', 'Bob', 'Johnson', '2023-02-01', True),
            (3, 'charlie', 'charlie@example.com', 'Charlie', 'Brown', '2023-03-01', False)
        ]
        
        self.products = [
            (1, 'Laptop', 'Powerful gaming laptop', 1299.99, 10, 'electronics', '2023-01-10', '2023-01-10'),
            (2, 'Smartphone', 'Latest model smartphone', 799.99, 25, 'electronics', '2023-01-15', '2023-01-15'),
            (3, 'Desk Chair', 'Comfortable office chair', 299.99, 5, 'furniture', '2023-02-01', '2023-02-01'),
            (4, 'Coffee Mug', 'Custom printed coffee mug', 19.99, 0, 'home goods', '2023-02-10', '2023-02-10')
        ]
        
        self.orders = [
            (1, 1, 1299.99, 'completed', '2023-03-01', {'street': '123 Main St', 'city': 'New York', 'zip': '10001'}),
            (2, 1, 19.99, 'shipped', '2023-03-05', {'street': '123 Main St', 'city': 'New York', 'zip': '10001'}),
            (3, 2, 799.99, 'pending', '2023-03-10', {'street': '456 Elm St', 'city': 'Boston', 'zip': '02101'})
        ]
    
    def query(self, model_class: Type[Model]) -> List[Model]:
        """
        查询指定模型的所有记录
        
        Args:
            model_class: 模型类
        
        Returns:
            模型实例列表
        """
        table_name = model_class.__table__
        
        if table_name == 'users':
            return [model_class.from_row(row) for row in self.users]
        elif table_name == 'products':
            return [model_class.from_row(row) for row in self.products]
        elif table_name == 'orders':
            return [model_class.from_row(row) for row in self.orders]
        else:
            return []
    
    def get_by_id(self, model_class: Type[Model], id: int) -> Optional[Model]:
        """
        根据ID获取记录
        
        Args:
            model_class: 模型类
            id: 记录ID
        
        Returns:
            模型实例或None
        """
        all_records = self.query(model_class)
        for record in all_records:
            if record.id == id:
                return record
        return None

# 演示ORM系统
print("\n演示简单的ORM映射系统:")

# 创建数据库实例
db = Database()

print("\n1. 查询所有用户:")
users = db.query(User)
for user in users:
    print(f"  {user} - 全名: {user.full_name()}")
    print(f"  公开信息: {user.to_dict_public()}")

print("\n2. 查询所有产品:")
products = db.query(Product)
for product in products:
    print(f"  {product}")
    print(f"  有库存: {product.is_in_stock()}")
    print(f"  9折价格: ${product.get_discounted_price(0.1):.2f}")

print("\n3. 查询所有订单:")
orders = db.query(Order)
for order in orders:
    print(f"  {order}")
    print(f"  已完成: {order.is_completed()}")
    print(f"  配送城市: {order.get_shipping_city()}")

print("\n4. 根据ID获取记录:")
user1 = db.get_by_id(User, 1)
product3 = db.get_by_id(Product, 3)
order2 = db.get_by_id(Order, 2)

print(f"  用户ID=1: {user1}")
print(f"  产品ID=3: {product3}")
print(f"  订单ID=2: {order2}")

print("\n5. 数据转换:")
# 转换为字典
user_dict = user1.to_dict()
print(f"  用户字典: {user_dict}")

# 从字典创建
new_user = User.from_dict({
    'id': 4,
    'username': 'david',
    'email': 'david@example.com',
    'first_name': 'David',
    'last_name': 'Wilson',
    'created_at': '2023-04-01'
})
print(f"  从字典创建的新用户: {new_user}")
print(f"  使用默认值: is_active={new_user.is_active}")

print("\n6. 不可变性测试:")
try:
    user1.username = 'new_username'
except AttributeError as e:
    print(f"  修改失败: {e}")

# 8. 总结

print("\n=== 8. 总结 ===")

print("\ncollections.namedtuple是Python标准库中提供的一个强大工具，它创建具有命名字段的元组子类。")

print("\n主要功能:")
print("1. 创建带有命名属性的元组子类")
print("2. 支持通过名称和索引访问元素")
print("3. 保持元组的不可变性")
print("4. 提供良好的字符串表示")
print("5. 内置方法支持字典转换、替换字段等操作")
print("6. 内存占用小于普通类")
print("7. 支持类型注解（通过typing.NamedTuple）")

print("\n优势:")
print("1. 比普通元组更具可读性，通过名称访问字段")
print("2. 比普通类更节省内存，没有__dict__属性")
print("3. 提供良好的默认字符串表示")
print("4. 可以用作字典键和集合元素")
print("5. 支持所有元组操作（解包、迭代等）")
print("6. 易于与其他数据结构转换")

print("\n限制:")
print("1. 实例是不可变的，不能修改字段值")
print("2. 字段名必须是合法的Python标识符")
print("3. 嵌套的可变对象仍然可以被修改")
print("4. 在Python 3.6之前不支持默认值")

print("\n应用场景:")
print("1. 表示数据库记录、CSV行数据等结构化数据")
print("2. 作为函数返回多个相关值的容器")
print("3. 配置管理和枚举替代")
print("4. 轻量级的数据传输对象")
print("5. 单元测试中的测试数据表示")
print("6. 简单的ORM映射系统")
print("7. 与标准库中的csv等模块配合使用")

print("\n使用建议:")
print("1. 对于需要不可变数据结构且希望通过名称访问字段的场景，namedtuple是理想选择")
print("2. 当需要大量实例时，namedtuple比普通类更高效")
print("3. 对于需要序列化/反序列化的数据，namedtuple提供了便捷方法")
print("4. 如果需要字段的可变性，考虑使用dataclass或普通类")
print("5. 利用_replace()方法可以在不修改原始实例的情况下创建新实例")

print("\ncollections.namedtuple是Python中处理轻量级数据结构的强大工具，它结合了元组的不可变性和字典的可读性，")
print("在许多场景下提供了比普通类和字典更高效、更清晰的解决方案。")
