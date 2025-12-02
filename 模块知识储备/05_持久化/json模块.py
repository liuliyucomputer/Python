"""
# json模块详解：Python中的JSON数据处理

json模块是Python标准库中用于处理JSON（JavaScript Object Notation）数据的工具。JSON是一种轻量级的数据交换格式，易于人阅读和编写，同时也易于机器解析和生成。json模块提供了将Python对象转换为JSON格式（序列化）和将JSON格式转换为Python对象（反序列化）的功能。

## 1. 核心功能概览

json模块的主要功能包括：

1. **序列化**：将Python对象转换为JSON字符串或写入文件
2. **反序列化**：将JSON字符串或文件内容转换为Python对象
3. **格式化输出**：美化JSON输出，提高可读性
4. **自定义编码器/解码器**：处理复杂Python对象的序列化和反序列化
5. **支持Unicode**：完全支持Unicode字符集

## 2. 基本使用

### 2.1 序列化（Python对象转JSON）

```python
import json

def basic_serialization():
    print("=== 基本序列化示例 ===")
    
    # 准备不同类型的数据
    data = {
        "string": "Hello, JSON!",
        "integer": 42,
        "float": 3.14159,
        "boolean": True,
        "none_value": None,
        "list": [1, 2, 3, 4, 5],
        "nested_dict": {
            "name": "张三",
            "age": 30,
            "skills": ["Python", "JavaScript", "Data Analysis"]
        },
        "tuple": (1, 2, 3)  # 注意：元组在JSON中会被转换为列表
    }
    
    print("原始Python数据:")
    print(data)
    print(f"tuple类型: {type(data['tuple'])}")
    
    # 使用dumps()将Python对象转换为JSON字符串
    print("\n1. 使用dumps()转换为JSON字符串:")
    json_str = json.dumps(data)
    print(f"JSON字符串: {json_str}")
    print(f"类型: {type(json_str)}")
    
    # 使用indent参数进行格式化输出
    print("\n2. 使用indent参数格式化输出:")
    json_formatted = json.dumps(data, indent=2, ensure_ascii=False)
    print("格式化后的JSON:")
    print(json_formatted)
    
    # 使用separators参数自定义分隔符
    print("\n3. 使用separators参数自定义分隔符:")
    # (item_separator, key_separator)
    compact_json = json.dumps(data, separators=(',', ':'))
    print(f"紧凑JSON: {compact_json}")
    
    # 使用sort_keys参数按键排序
    print("\n4. 使用sort_keys参数按键排序:")
    sorted_json = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)
    print("按键排序后的JSON:")
    print(sorted_json)
    
    # 写入文件示例
    print("\n5. 使用dump()写入文件:")
    with open("example.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("JSON已写入example.json文件")

# 运行示例
basic_serialization()
```

### 2.2 反序列化（JSON转Python对象）

```python
import json

def basic_deserialization():
    print("=== 基本反序列化示例 ===")
    
    # JSON字符串
    json_str = '''
    {
      "string": "Hello, JSON!",
      "integer": 42,
      "float": 3.14159,
      "boolean": true,
      "none_value": null,
      "list": [1, 2, 3, 4, 5],
      "nested_dict": {
        "name": "张三",
        "age": 30,
        "skills": ["Python", "JavaScript", "Data Analysis"]
      }
    }
    '''
    
    print("原始JSON字符串:")
    print(json_str)
    
    # 使用loads()将JSON字符串转换为Python对象
    print("\n1. 使用loads()转换为Python对象:")
    python_obj = json.loads(json_str)
    print("转换后的Python对象:")
    print(python_obj)
    print(f"类型: {type(python_obj)}")
    print(f"nested_dict类型: {type(python_obj['nested_dict'])}")
    print(f"list类型: {type(python_obj['list'])}")
    
    # 访问数据
    print("\n2. 访问转换后的数据:")
    print(f"字符串值: {python_obj['string']}")
    print(f"整数值: {python_obj['integer']}")
    print(f"嵌套字典中的名字: {python_obj['nested_dict']['name']}")
    print(f"技能列表的第一个元素: {python_obj['nested_dict']['skills'][0]}")
    
    # 从文件读取
    print("\n3. 使用load()从文件读取:")
    try:
        with open("example.json", "r", encoding="utf-8") as f:
            file_data = json.load(f)
        print("从文件读取的Python对象:")
        print(file_data)
        print(f"文件中name的值: {file_data.get('nested_dict', {}).get('name')}")
    except FileNotFoundError:
        print("example.json文件不存在，请先运行序列化示例")
    
    # 处理格式错误的JSON
    print("\n4. 处理格式错误的JSON:")
    invalid_json = '{"name": "John", "age": }'  # 缺少age的值
    try:
        json.loads(invalid_json)
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        print(f"错误位置: {e.pos}")
        print(f"错误消息: {e.msg}")
        print(f"错误文档片段: {e.doc[e.pos-10:e.pos+10] if 10 < e.pos < len(e.doc) - 10 else e.doc}")

# 运行示例
basic_deserialization()
```

## 3. 数据类型转换规则

在Python和JSON之间进行转换时，数据类型会按照以下规则进行映射：

| Python | JSON |
|--------|------|
| dict | object |
| list, tuple | array |
| str | string |
| int, float | number |
| True | true |
| False | false |
| None | null |

注意事项：
- JSON不支持元组，Python元组会被转换为JSON数组
- JSON不支持集合(set)，需要自定义编码器处理
- JSON中的键必须是字符串，而Python字典的键可以是任何不可变类型
- JSON中的数字没有整数和浮点数的区分，但Python会根据值进行适当转换

让我们验证这些转换规则：

```python
import json

def data_type_conversion():
    print("=== 数据类型转换规则验证 ===")
    
    # 创建包含各种Python类型的数据
    test_data = {
        "dict": {1: "one", "two": 2, 3.0: True},
        "list": [1, "two", 3.0, True, None],
        "tuple": (1, "two", 3.0),
        "string": "Hello, JSON!",
        "integer": 42,
        "float": 3.14159,
        "boolean_true": True,
        "boolean_false": False,
        "none": None,
        # 注意：集合不能直接序列化
        # "set": {1, 2, 3}  # 这会引发TypeError
    }
    
    print("原始Python数据类型:")
    for key, value in test_data.items():
        print(f"{key}: {type(value).__name__} = {value}")
    
    # 序列化
    print("\n序列化后:")
    try:
        json_str = json.dumps(test_data, indent=2, ensure_ascii=False)
        print(json_str)
    except TypeError as e:
        print(f"序列化错误: {e}")
    
    # 反序列化回Python对象
    print("\n反序列化回Python对象后的数据类型:")
    try:
        json_str = json.dumps(test_data)
        python_obj = json.loads(json_str)
        
        for key, value in python_obj.items():
            # 特别注意元组和字典键的变化
            if key == "tuple":
                print(f"{key}: {type(value).__name__} (原来是tuple，现在是{type(value).__name__}) = {value}")
            elif key == "dict":
                print(f"{key}: {type(value).__name__}")
                print(f"   键类型变化: 原来有int和float键，现在全部是{type(list(value.keys())[0]).__name__}")
            else:
                print(f"{key}: {type(value).__name__} = {value}")
    except Exception as e:
        print(f"反序列化错误: {e}")
    
    print("\n数据类型转换总结:")
    print("1. Python dict -> JSON object: 字典键会被转换为字符串")
    print("2. Python list/tuple -> JSON array: 元组会变成列表")
    print("3. Python str -> JSON string: 保持一致")
    print("4. Python int/float -> JSON number: 保持数值")
    print("5. Python True/False -> JSON true/false: 大小写不同")
    print("6. Python None -> JSON null: 表示方式不同")
    print("7. Python set: 不支持，需要自定义序列化")

# 运行示例
data_type_conversion()
```

## 4. 自定义编码器和解码器

当我们需要序列化不支持的类型（如自定义类、集合等）时，可以创建自定义的JSONEncoder类。同样，在反序列化时，可以使用object_hook参数自定义对象的创建过程。

### 4.1 自定义JSONEncoder

```python
import json
from datetime import datetime
from decimal import Decimal
from pathlib import Path

def custom_encoder_example():
    print("=== 自定义JSONEncoder示例 ===")
    
    # 定义一些不支持直接序列化的类型
    class Person:
        def __init__(self, name, age, birthday):
            self.name = name
            self.age = age
            self.birthday = birthday
            self.skills = {"Python", "JavaScript", "Data Analysis"}  # 集合
            self.created_at = datetime.now()  # datetime对象
            self.salary = Decimal("12345.67")  # Decimal对象
            self.home_path = Path.home()  # Path对象
        
        def __repr__(self):
            return f"Person(name={self.name}, age={self.age})")
    
    # 创建自定义JSONEncoder
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            # 处理datetime对象
            if isinstance(obj, datetime):
                return {
                    "__type__": "datetime",
                    "value": obj.isoformat()
                }
            
            # 处理Decimal对象
            elif isinstance(obj, Decimal):
                return {
                    "__type__": "decimal",
                    "value": str(obj)
                }
            
            # 处理set对象
            elif isinstance(obj, set):
                return {
                    "__type__": "set",
                    "value": list(obj)
                }
            
            # 处理Path对象
            elif isinstance(obj, Path):
                return {
                    "__type__": "path",
                    "value": str(obj)
                }
            
            # 处理自定义Person对象
            elif isinstance(obj, Person):
                return {
                    "__type__": "Person",
                    "name": obj.name,
                    "age": obj.age,
                    "birthday": obj.birthday,
                    "skills": list(obj.skills),  # 转换为列表
                    "created_at": obj.created_at.isoformat(),
                    "salary": str(obj.salary),
                    "home_path": str(obj.home_path)
                }
            
            # 默认行为：调用基类default方法，这会引发TypeError
            return super().default(obj)
    
    # 创建测试数据
    birthday = datetime(1990, 1, 1).date()  # Python的date对象
    person = Person("张三", 30, birthday)
    
    # 准备包含各种类型的数据
    test_data = {
        "person": person,
        "current_time": datetime.now(),
        "price": Decimal("99.99"),
        "tags": {"important", "new", "sale"},
        "project_path": Path("/home/user/projects/python-json"),
        "regular_data": [1, "two", True, None]
    }
    
    print("原始Python数据包含不支持序列化的类型:")
    print(f"person: {person}")
    print(f"current_time: {test_data['current_time']} (类型: {type(test_data['current_time']).__name__})")
    print(f"price: {test_data['price']} (类型: {type(test_data['price']).__name__})")
    print(f"tags: {test_data['tags']} (类型: {type(test_data['tags']).__name__})")
    print(f"project_path: {test_data['project_path']} (类型: {type(test_data['project_path']).__name__})")
    
    # 使用自定义编码器序列化
    print("\n使用自定义编码器序列化:")
    try:
        json_str = json.dumps(test_data, cls=CustomJSONEncoder, indent=2, ensure_ascii=False)
        print("序列化成功:")
        print(json_str)
    except TypeError as e:
        print(f"序列化错误: {e}")
    
    # 尝试不使用自定义编码器（应该会失败）
    print("\n尝试不使用自定义编码器:")
    try:
        json.dumps(test_data)
    except TypeError as e:
        print(f"序列化失败，因为包含不支持的类型: {e}")
    
    print("\n自定义编码器的优势:")
    print("1. 可以序列化Python内置JSON模块不支持的类型")
    print("2. 可以控制序列化的格式和内容")
    print("3. 可以添加类型标识，便于后续反序列化")
    print("4. 可以过滤敏感信息或转换数据格式")

# 运行示例
custom_encoder_example()
```

### 4.2 自定义解码器

```python
import json
from datetime import datetime
from decimal import Decimal
from pathlib import Path

def custom_decoder_example():
    print("=== 自定义解码器示例 ===")
    
    # 定义与前面示例相同的Person类
    class Person:
        def __init__(self, name, age, birthday):
            self.name = name
            self.age = age
            self.birthday = birthday
        
        def __repr__(self):
            return f"Person(name={self.name}, age={self.age})")
    
    # 创建一个包含特殊类型标记的JSON字符串
    json_str = '''
    {
      "person": {
        "__type__": "Person",
        "name": "张三",
        "age": 30,
        "birthday": "1990-01-01",
        "skills": ["Python", "JavaScript", "Data Analysis"],
        "created_at": "2023-01-01T12:00:00",
        "salary": "12345.67",
        "home_path": "/home/user"
      },
      "current_time": {
        "__type__": "datetime",
        "value": "2023-01-01T15:30:45"
      },
      "price": {
        "__type__": "decimal",
        "value": "99.99"
      },
      "tags": {
        "__type__": "set",
        "value": ["important", "new", "sale"]
      },
      "project_path": {
        "__type__": "path",
        "value": "/home/user/projects/python-json"
      },
      "regular_data": [1, "two", true, null]
    }
    '''
    
    # 创建自定义解码器函数
    def custom_decoder(dct):
        # 检查是否有__type__字段
        if "__type__" in dct:
            # 根据类型进行特殊处理
            if dct["__type__"] == "datetime":
                return datetime.fromisoformat(dct["value"])
            elif dct["__type__"] == "decimal":
                return Decimal(dct["value"])
            elif dct["__type__"] == "set":
                return set(dct["value"])
            elif dct["__type__"] == "path":
                return Path(dct["value"])
            elif dct["__type__"] == "Person":
                # 创建Person对象
                person = Person(dct["name"], dct["age"], dct["birthday"])
                # 添加其他属性
                person.skills = set(dct["skills"])
                person.created_at = datetime.fromisoformat(dct["created_at"])
                person.salary = Decimal(dct["salary"])
                person.home_path = Path(dct["home_path"])
                return person
        # 默认情况：原样返回字典
        return dct
    
    # 使用自定义解码器反序列化
    print("使用自定义解码器反序列化:")
    try:
        python_obj = json.loads(json_str, object_hook=custom_decoder)
        print("反序列化成功，重建了特殊类型对象:")
        print(f"person类型: {type(python_obj['person']).__name__} = {python_obj['person']}")
        print(f"current_time类型: {type(python_obj['current_time']).__name__} = {python_obj['current_time']}")
        print(f"price类型: {type(python_obj['price']).__name__} = {python_obj['price']}")
        print(f"tags类型: {type(python_obj['tags']).__name__} = {python_obj['tags']}")
        print(f"project_path类型: {type(python_obj['project_path']).__name__} = {python_obj['project_path']}")
    except Exception as e:
        print(f"反序列化错误: {e}")
    
    # 不使用自定义解码器的情况
    print("\n不使用自定义解码器的情况:")
    regular_obj = json.loads(json_str)
    print(f"person类型: {type(regular_obj['person']).__name__}")
    print(f"current_time类型: {type(regular_obj['current_time']).__name__}")
    print(f"price类型: {type(regular_obj['price']).__name__}")
    
    print("\n自定义解码器的优势:")
    print("1. 可以将JSON反序列化为特定类型的Python对象")
    print("2. 可以重建复杂的对象结构")
    print("3. 可以执行数据验证和转换")
    print("4. 与自定义编码器配合，实现完整的对象序列化/反序列化")

# 运行示例
custom_decoder_example()
```

## 5. 高级应用示例

### 5.1 配置管理系统

```python
import json
import os
from pathlib import Path
from datetime import datetime

def json_config_manager():
    """基于JSON的配置管理系统"""
    
    class ConfigManager:
        def __init__(self, config_file="config.json"):
            """初始化配置管理器"""
            self.config_file = Path(config_file)
            self.config = {}
            # 尝试加载配置文件
            self.load()
        
        def load(self):
            """从文件加载配置"""
            if self.config_file.exists():
                try:
                    with open(self.config_file, "r", encoding="utf-8") as f:
                        self.config = json.load(f)
                    print(f"配置已从 {self.config_file} 加载")
                except json.JSONDecodeError as e:
                    print(f"配置文件解析错误: {e}")
                    self.config = {}
            else:
                print(f"配置文件 {self.config_file} 不存在，将使用默认配置")
        
        def save(self):
            """保存配置到文件"""
            # 确保目录存在
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 添加元数据
            self.config["__metadata__"] = {
                "last_updated": datetime.now().isoformat(),
                "version": "1.0"
            }
            
            # 保存到文件
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            print(f"配置已保存到 {self.config_file}")
        
        def get(self, key, default=None):
            """获取配置值"""
            # 支持点表示法访问嵌套配置
            keys = key.split(".")
            value = self.config
            
            try:
                for k in keys:
                    if k in value:
                        value = value[k]
                    else:
                        return default
                return value
            except (TypeError, KeyError):
                return default
        
        def set(self, key, value):
            """设置配置值"""
            # 支持点表示法设置嵌套配置
            keys = key.split(".")
            config = self.config
            
            # 遍历除最后一个键以外的所有键
            for k in keys[:-1]:
                if k not in config or not isinstance(config[k], dict):
                    config[k] = {}
                config = config[k]
            
            # 设置最后一个键的值
            config[keys[-1]] = value
            print(f"设置配置: {key} = {value}")
        
        def delete(self, key):
            """删除配置项"""
            keys = key.split(".")
            config = self.config
            
            try:
                # 遍历到倒数第二个键
                for k in keys[:-1]:
                    config = config[k]
                
                # 删除最后一个键
                if keys[-1] in config:
                    del config[keys[-1]]
                    print(f"删除配置: {key}")
                    return True
                return False
            except (TypeError, KeyError):
                return False
        
        def has(self, key):
            """检查配置项是否存在"""
            return self.get(key) is not None
        
        def clear(self):
            """清空所有配置"""
            self.config = {}
            print("所有配置已清空")
        
        def get_all(self):
            """获取所有配置（不包括元数据）"""
            config_copy = self.config.copy()
            if "__metadata__" in config_copy:
                del config_copy["__metadata__"]
            return config_copy
        
        def validate_schema(self, schema):
            """验证配置是否符合指定的模式"""
            def validate_section(config_section, schema_section):
                """验证配置的一部分"""
                # 检查必需的键
                for key, expected_type in schema_section.items():
                    if key not in config_section:
                        return False, f"缺少必需的配置项: {key}"
                    
                    # 检查类型
                    actual_type = type(config_section[key]).__name__
                    expected_type_name = expected_type.__name__
                    
                    # 特殊处理：允许int和float之间的转换
                    if expected_type_name == "int" and actual_type == "float":
                        config_section[key] = int(config_section[key])
                    elif expected_type_name == "float" and actual_type == "int":
                        config_section[key] = float(config_section[key])
                    elif not isinstance(config_section[key], expected_type):
                        return False, f"配置项 {key} 应为 {expected_type_name} 类型，实际为 {actual_type} 类型"
                
                return True, ""
            
            # 验证配置
            is_valid, message = validate_section(self.get_all(), schema)
            if not is_valid:
                print(f"配置验证失败: {message}")
                return False
            
            print("配置验证成功")
            return True
    
    # 测试配置管理器
    print("=== JSON配置管理系统测试 ===")
    
    # 创建配置管理器
    config = ConfigManager("app_config.json")
    
    # 设置配置
    print("\n1. 设置基本配置:")
    config.set("app.name", "MyApp")
    config.set("app.version", "1.0.0")
    config.set("app.debug", True)
    
    # 设置嵌套配置
    print("\n2. 设置嵌套配置:")
    config.set("database.host", "localhost")
    config.set("database.port", 5432)
    config.set("database.username", "admin")
    config.set("database.password", "secure_password")
    
    # 设置UI配置
    config.set("ui.theme", "dark")
    config.set("ui.font_size", 14)
    config.set("ui.notifications", True)
    
    # 获取配置
    print("\n3. 获取配置:")
    app_name = config.get("app.name")
    db_host = config.get("database.host")
    db_password = config.get("database.password")
    unknown_setting = config.get("unknown.setting", "默认值")
    
    print(f"   应用名称: {app_name}")
    print(f"   数据库主机: {db_host}")
    print(f"   数据库密码: {'*' * len(db_password)}")  # 安全显示
    print(f"   未知配置项: {unknown_setting}")
    
    # 检查配置是否存在
    print("\n4. 检查配置项是否存在:")
    print(f"   app.name 存在: {config.has('app.name')}")
    print(f"   unknown.setting 存在: {config.has('unknown.setting')}")
    
    # 获取所有配置
    print("\n5. 获取所有配置:")
    all_config = config.get_all()
    print(json.dumps(all_config, indent=2, ensure_ascii=False))
    
    # 验证配置模式
    print("\n6. 验证配置模式:")
    schema = {
        "app": dict,
        "database": dict,
        "ui": dict
    }
    config.validate_schema(schema)
    
    # 保存配置
    print("\n7. 保存配置:")
    config.save()
    
    # 删除配置
    print("\n8. 删除配置项:")
    config.delete("database.password")
    print(f"   删除后数据库密码: {config.get('database.password', '已删除')}")
    
    # 加载配置
    print("\n9. 重新加载配置:")
    config.load()
    print(f"   重新加载后应用名称: {config.get('app.name')}")
    
    # 清理测试文件
    print("\n10. 清理测试文件:")
    if Path("app_config.json").exists():
        os.remove("app_config.json")
        print("   已删除测试配置文件")

# 运行示例
json_config_manager()
```

### 5.2 REST API数据处理

```python
import json
import sys
from io import StringIO

def json_api_processing():
    """JSON API数据处理示例"""
    
    # 模拟API响应数据
    api_response = '''
    {
      "status": "success",
      "data": {
        "users": [
          {
            "id": 1,
            "name": "张三",
            "email": "zhangsan@example.com",
            "age": 30,
            "roles": ["admin", "user"],
            "active": true,
            "created_at": "2023-01-01T12:00:00Z"
          },
          {
            "id": 2,
            "name": "李四",
            "email": "lisi@example.com",
            "age": 25,
            "roles": ["user"],
            "active": true,
            "created_at": "2023-01-02T10:30:00Z"
          },
          {
            "id": 3,
            "name": "王五",
            "email": "wangwu@example.com",
            "age": 35,
            "roles": ["manager", "user"],
            "active": false,
            "created_at": "2023-01-03T09:15:00Z"
          }
        ],
        "pagination": {
          "total": 100,
          "page": 1,
          "per_page": 3,
          "total_pages": 34
        }
      },
      "meta": {
        "api_version": "1.0",
        "timestamp": "2023-01-10T15:20:30Z"
      },
      "errors": null
    }
    '''
    
    print("=== JSON API数据处理示例 ===")
    print("处理模拟的API响应数据")
    
    # 解析API响应
    print("\n1. 解析API响应:")
    try:
        response_data = json.loads(api_response)
        print(f"   状态: {response_data.get('status')}")
        print(f"   API版本: {response_data.get('meta', {}).get('api_version')}")
    except json.JSONDecodeError as e:
        print(f"   JSON解析错误: {e}")
        return
    
    # 提取和处理数据
    print("\n2. 提取和处理用户数据:")
    users = response_data.get('data', {}).get('users', [])
    print(f"   找到 {len(users)} 个用户")
    
    # 筛选活跃用户
    active_users = [user for user in users if user.get('active')]
    print(f"   活跃用户数量: {len(active_users)}")
    
    # 筛选管理员
    admin_users = [user for user in users if 'admin' in user.get('roles', [])]
    print(f"   管理员数量: {len(admin_users)}")
    
    # 计算平均年龄
    if users:
        avg_age = sum(user.get('age', 0) for user in users) / len(users)
        print(f"   用户平均年龄: {avg_age:.1f}")
    
    # 格式化用户信息
    print("\n3. 格式化用户信息:")
    for user in users:
        status = "活跃" if user.get('active') else "非活跃"
        roles = ", ".join(user.get('roles', []))
        print(f"   ID: {user.get('id')}, 姓名: {user.get('name')}, 状态: {status}, 角色: {roles}")
    
    # 创建响应数据
    print("\n4. 创建新的API请求数据:")
    new_user = {
        "name": "赵六",
        "email": "zhaoliu@example.com",
        "age": 28,
        "roles": ["user"],
        "department": "技术部"
    }
    
    # 转换为JSON字符串，用于API请求
    request_json = json.dumps(new_user, indent=2, ensure_ascii=False)
    print("   API请求数据:")
    print(request_json)
    
    # 处理分页信息
    print("\n5. 处理分页信息:")
    pagination = response_data.get('data', {}).get('pagination', {})
    print(f"   当前页: {pagination.get('page')}/{pagination.get('total_pages')}")
    print(f"   每页显示: {pagination.get('per_page')} 条")
    print(f"   总共: {pagination.get('total')} 条记录")
    
    # 错误处理示例
    print("\n6. 错误响应处理示例:")
    error_response = '''
    {
      "status": "error",
      "data": null,
      "errors": [
        {
          "code": "VALIDATION_ERROR",
          "message": "邮箱格式无效",
          "field": "email"
        },
        {
          "code": "REQUIRED_FIELD",
          "message": "姓名不能为空",
          "field": "name"
        }
      ],
      "meta": {
        "api_version": "1.0",
        "timestamp": "2023-01-10T15:25:10Z"
      }
    }
    '''
    
    error_data = json.loads(error_response)
    if error_data.get('status') == 'error':
        print(f"   错误数量: {len(error_data.get('errors', []))}")
        for error in error_data.get('errors', []):
            print(f"   - 字段 '{error.get('field')}': {error.get('message')} (错误代码: {error.get('code')})")
    
    print("\n7. JSON流式处理大型数据:")
    # 模拟大型JSON数组
    large_json_array = "[" + ",".join([f"{{\"id\":{i},\"name\":\"用户{i}\"}}" for i in range(1, 1001)]) + "]"
    
    # 使用生成器进行流式处理，避免一次性加载全部数据
    def process_large_json(json_str, chunk_size=100):
        data = json.loads(json_str)
        for i in range(0, len(data), chunk_size):
            yield data[i:i+chunk_size]
    
    # 处理大型JSON数组
    chunk_count = 0
    for chunk in process_large_json(large_json_array):
        chunk_count += 1
        print(f"   处理批次 {chunk_count}: {len(chunk)} 条记录")
        # 在实际应用中，这里会对每个批次进行处理
        if chunk_count >= 3:  # 只处理前3个批次以节省空间
            break
    
    print("\nJSON API数据处理最佳实践:")
    print("1. 始终验证API响应状态")
    print("2. 使用try-except捕获JSON解析错误")
    print("3. 对嵌套数据使用get()方法安全访问")
    print("4. 大型数据集考虑流式处理")
    print("5. 注意处理Unicode字符和特殊符号")
    print("6. 在API请求中使用ensure_ascii=False确保正确编码非ASCII字符")

# 运行示例
json_api_processing()
```

### 5.3 JSON数据验证和模式匹配

```python
import json
import re

def json_validation_example():
    """JSON数据验证和模式匹配示例"""
    
    # 示例JSON数据
    user_data = '''
    {
      "users": [
        {
          "id": 1,
          "name": "张三",
          "email": "zhangsan@example.com",
          "age": 30,
          "address": {
            "city": "北京",
            "street": "朝阳区建国路",
            "zip_code": "100022"
          },
          "phone": "13800138000",
          "registered": true,
          "last_login": "2023-01-10T15:20:30Z"
        },
        {
          "id": 2,
          "name": "李四",
          "email": "invalid-email",  # 无效邮箱
          "age": -5,  # 无效年龄
          "address": {
            "city": "上海",
            "zip_code": "200000"
          },
          "phone": "123456",  # 无效电话号码
          "registered": true,
          "last_login": "2023-01-09"
        },
        {
          "id": "3",  # 应该是整数
          "name": "",  # 空名称
          "email": "wangwu@example.com",
          "registered": false
          # 缺少age字段
        }
      ]
    }
    '''
    
    print("=== JSON数据验证和模式匹配示例 ===")
    
    # 解析JSON数据
    try:
        data = json.loads(user_data)
        users = data.get('users', [])
        print(f"解析到 {len(users)} 个用户记录")
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return
    
    # 定义验证规则
    class ValidationError(Exception):
        """验证错误异常"""
        pass
    
    def validate_user(user):
        """验证单个用户数据"""
        errors = []
        
        # 验证id字段
        if 'id' not in user:
            errors.append("缺少必填字段: id")
        elif not isinstance(user['id'], int):
            errors.append("id必须是整数类型")
        
        # 验证name字段
        if 'name' not in user:
            errors.append("缺少必填字段: name")
        elif not isinstance(user['name'], str) or not user['name'].strip():
            errors.append("name必须是非空字符串")
        elif len(user['name']) > 50:
            errors.append("name长度不能超过50个字符")
        
        # 验证email字段
        if 'email' not in user:
            errors.append("缺少必填字段: email")
        elif not isinstance(user['email'], str):
            errors.append("email必须是字符串类型")
        else:
            # 使用正则表达式验证邮箱格式
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, user['email']):
                errors.append(f"无效的邮箱格式: {user['email']}")
        
        # 验证age字段（如果存在）
        if 'age' in user:
            if not isinstance(user['age'], int):
                errors.append("age必须是整数类型")
            elif user['age'] < 0 or user['age'] > 150:
                errors.append(f"age必须在0到150之间，当前值: {user['age']}")
        
        # 验证phone字段（如果存在）
        if 'phone' in user:
            if not isinstance(user['phone'], str):
                errors.append("phone必须是字符串类型")
            else:
                # 验证中国手机号码格式
                phone_pattern = r'^1[3-9]\d{9}$'
                if not re.match(phone_pattern, user['phone']):
                    errors.append(f"无效的手机号码格式: {user['phone']}")
        
        # 验证registered字段
        if 'registered' not in user:
            errors.append("缺少必填字段: registered")
        elif not isinstance(user['registered'], bool):
            errors.append("registered必须是布尔类型")
        
        # 验证address字段（如果存在）
        if 'address' in user:
            if not isinstance(user['address'], dict):
                errors.append("address必须是对象类型")
            else:
                # 验证地址的必需字段
                address = user['address']
                if 'city' not in address:
                    errors.append("address缺少必填字段: city")
                if 'zip_code' in address:
                    # 验证邮政编码
                    zip_pattern = r'^\d{6}$'
                    if not re.match(zip_pattern, address['zip_code']):
                        errors.append(f"无效的邮政编码格式: {address['zip_code']}")
        
        return errors
    
    # 验证所有用户数据
    print("\n执行数据验证:")
    valid_users = []
    invalid_users = []
    
    for user in users:
        errors = validate_user(user)
        if errors:
            invalid_users.append((user, errors))
        else:
            valid_users.append(user)
    
    # 显示验证结果
    print(f"\n验证结果:")
    print(f"有效用户: {len(valid_users)}")
    print(f"无效用户: {len(invalid_users)}")
    
    # 显示无效用户的详细错误信息
    if invalid_users:
        print("\n无效用户详情:")
        for i, (user, errors) in enumerate(invalid_users, 1):
            user_id = user.get('id', 'N/A')
            user_name = user.get('name', 'N/A')
            print(f"\n用户 {i} (ID: {user_id}, 姓名: '{user_name}'):")
            for error in errors:
                print(f"  - {error}")
    
    # 数据清洗示例
    print("\n执行数据清洗:")
    cleaned_users = []
    
    for user in users:
        cleaned_user = user.copy()
        
        # 尝试修复一些简单的问题
        # 修复id类型
        if 'id' in cleaned_user and isinstance(cleaned_user['id'], str):
            try:
                cleaned_user['id'] = int(cleaned_user['id'])
                print(f"修复用户ID类型: {user['id']} -> {cleaned_user['id']}")
            except ValueError:
                print(f"无法修复无效的用户ID: {user['id']}")
        
        # 修复空名称
        if 'name' in cleaned_user and not cleaned_user['name'].strip():
            cleaned_user['name'] = f"用户_{cleaned_user.get('id', 'unknown')}"
            print(f"修复空名称: 设置为 '{cleaned_user['name']}'")
        
        # 添加默认年龄
        if 'age' not in cleaned_user:
            cleaned_user['age'] = 0
            print(f"添加默认年龄: 0")
        
        # 清理地址
        if 'address' in cleaned_user and isinstance(cleaned_user['address'], dict):
            # 移除无效的地址字段
            if 'street' not in cleaned_user['address']:
                cleaned_user['address']['street'] = '未知街道'
                print(f"添加默认街道信息")
        
        cleaned_users.append(cleaned_user)
    
    # 显示清洗后的数据
    print("\n数据清洗后的用户数据:")
    for user in cleaned_users:
        user_info = {
            'id': user.get('id'),
            'name': user.get('name'),
            'email': user.get('email'),
            'age': user.get('age')
        }
        print(f"{user_info}")
    
    # 生成JSON Schema（用于说明）
    print("\n对应的JSON Schema示例:")
    schema = {
        "type": "object",
        "properties": {
            "users": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["id", "name", "email", "registered"],
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string", "minLength": 1, "maxLength": 50},
                        "email": {"type": "string", "format": "email"},
                        "age": {"type": "integer", "minimum": 0, "maximum": 150},
                        "address": {
                            "type": "object",
                            "properties": {
                                "city": {"type": "string"},
                                "street": {"type": "string"},
                                "zip_code": {"type": "string", "pattern": "^\\d{6}$"}
                            },
                            "required": ["city"]
                        },
                        "phone": {"type": "string", "pattern": "^1[3-9]\\d{9}$"},
                        "registered": {"type": "boolean"},
                        "last_login": {"type": "string", "format": "date-time"}
                    }
                }
            }
        }
    }
    
    print(json.dumps(schema, indent=2))
    
    print("\nJSON数据验证最佳实践:")
    print("1. 定义明确的数据模式和验证规则")
    print("2. 验证所有必需字段是否存在")
    print("3. 检查数据类型是否符合预期")
    print("4. 对字符串格式（如邮箱、电话、日期等）使用正则表达式验证")
    print("5. 对数值范围进行限制")
    print("6. 实现数据清洗逻辑，尽可能修复可恢复的错误")
    print("7. 使用专门的验证库（如jsonschema）处理复杂验证")
    print("8. 记录详细的验证错误信息，便于调试和修复")

# 运行示例
json_validation_example()
```

## 6. 性能优化

在处理大型JSON数据时，性能优化是一个重要考虑因素。以下是一些优化技巧和实践：

### 6.1 流式处理大型JSON

```python
import json
import sys
from io import StringIO

def json_streaming_example():
    """大型JSON数据的流式处理示例"""
    
    print("=== 大型JSON数据的流式处理示例 ===")
    
    # 生成一个大型JSON数组用于演示
    print("生成大型JSON数据...")
    large_data = [
        {"id": i, "name": f"Item {i}", "value": i * 100, "tags": [f"tag{i%10}" for i in range(i%5)]}
        for i in range(10000)
    ]
    
    # 转换为JSON字符串
    json_str = json.dumps(large_data)
    print(f"生成的JSON数据大小: 约 {len(json_str) / 1024:.2f} KB")
    
    # 传统方法（一次性加载）
    print("\n方法1: 传统方法（一次性加载整个JSON）")
    import time
    start_time = time.time()
    
    try:
        data = json.loads(json_str)
        print(f"加载了 {len(data)} 个项目")
        # 处理数据（示例：计算值的总和）
        total_value = sum(item.get('value', 0) for item in data)
        print(f"值的总和: {total_value}")
        # 查找特定项目
        filtered_items = [item for item in data if item.get('value', 0) > 500000]
        print(f"值大于500000的项目数量: {len(filtered_items)}")
    except Exception as e:
        print(f"处理错误: {e}")
    
    traditional_time = time.time() - start_time
    print(f"传统方法耗时: {traditional_time:.4f} 秒")
    
    # 流式处理方法 - 自定义解析器
    print("\n方法2: 自定义流式处理（适用于简单JSON数组）")
    start_time = time.time()
    
    class SimpleJSONStreamParser:
        """简单的JSON数组流式解析器"""
        def __init__(self, json_str):
            self.json_str = json_str
            self.pos = 0
            self.total_items = 0
            self.total_value = 0
            self.filtered_count = 0
        
        def parse(self):
            """开始解析"""
            # 找到数组开始位置
            if self.json_str.startswith('['):
                self.pos = 1
            else:
                raise ValueError("输入不是有效的JSON数组")
            
            # 逐个解析项目
            while self.pos < len(self.json_str):
                # 跳过空白字符
                while self.pos < len(self.json_str) and self.json_str[self.pos].isspace():
                    self.pos += 1
                
                # 检查是否到达数组末尾
                if self.json_str[self.pos] == ']':
                    self.pos += 1
                    break
                
                # 找到当前项目的结束位置（假设没有嵌套对象）
                item_start = self.pos
                brace_count = 0
                in_string = False
                escape = False
                
                while self.pos < len(self.json_str):
                    char = self.json_str[self.pos]
                    
                    # 处理字符串
                    if char == '"' and not escape:
                        in_string = not in_string
                    elif char == '\\' and in_string:
                        escape = not escape
                    else:
                        escape = False
                    
                    # 跟踪花括号嵌套级别
                    if char == '{' and not in_string:
                        brace_count += 1
                    elif char == '}' and not in_string:
                        brace_count -= 1
                        if brace_count == 0:
                            self.pos += 1  # 包括右花括号
                            break
                    
                    self.pos += 1
                
                # 提取当前项目的JSON
                item_json = self.json_str[item_start:self.pos]
                
                # 处理可能的逗号
                while self.pos < len(self.json_str) and self.json_str[self.pos].isspace():
                    self.pos += 1
                
                if self.pos < len(self.json_str) and self.json_str[self.pos] == ',':
                    self.pos += 1
                
                # 解析单个项目
                try:
                    item = json.loads(item_json)
                    self._process_item(item)
                except json.JSONDecodeError:
                    # 跳过无效项
                    pass
            
            return {
                'total_items': self.total_items,
                'total_value': self.total_value,
                'filtered_count': self.filtered_count
            }
        
        def _process_item(self, item):
            """处理单个项目"""
            self.total_items += 1
            self.total_value += item.get('value', 0)
            if item.get('value', 0) > 500000:
                self.filtered_count += 1
    
    try:
        parser = SimpleJSONStreamParser(json_str)
        results = parser.parse()
        print(f"处理了 {results['total_items']} 个项目")
        print(f"值的总和: {results['total_value']}")
        print(f"值大于500000的项目数量: {results['filtered_count']}")
    except Exception as e:
        print(f"处理错误: {e}")
    
    streaming_time = time.time() - start_time
    print(f"自定义流式处理耗时: {streaming_time:.4f} 秒")
    
    # 使用内置json模块的分块处理
    print("\n方法3: 内置json模块的分块处理")
    start_time = time.time()
    
    try:
        # 一次性加载后分块处理
        data = json.loads(json_str)
        total_items = len(data)
        total_value = 0
        filtered_count = 0
        
        # 分块处理
        chunk_size = 1000
        for i in range(0, total_items, chunk_size):
            chunk = data[i:i+chunk_size]
            for item in chunk:
                total_value += item.get('value', 0)
                if item.get('value', 0) > 500000:
                    filtered_count += 1
        
        print(f"处理了 {total_items} 个项目")
        print(f"值的总和: {total_value}")
        print(f"值大于500000的项目数量: {filtered_count}")
    except Exception as e:
        print(f"处理错误: {e}")
    
    chunked_time = time.time() - start_time
    print(f"分块处理耗时: {chunked_time:.4f} 秒")
    
    print("\n性能比较:")
    print(f"传统方法: {traditional_time:.4f} 秒")
    print(f"自定义流式处理: {streaming_time:.4f} 秒")
    print(f"分块处理: {chunked_time:.4f} 秒")
    
    print("\n处理大型JSON的最佳实践:")
    print("1. 使用json.load()和json.dump()直接处理文件，避免一次性加载整个文件到内存")
    print("2. 对于特别大的JSON文件，考虑使用流式解析器")
    print("3. 处理数据时采用分块策略，减少内存占用")
    print("4. 只解析和处理需要的数据，忽略不需要的字段")
    print("5. 使用更高效的JSON库（如ujson、orjson）可以显著提高性能")
    print("6. 考虑使用压缩减少JSON数据的大小")
    print("7. 对于非常大的数据集，考虑使用数据库而不是JSON文件")

# 运行示例
json_streaming_example()
```

### 6.2 优化提示

1. **直接文件操作**：当处理大型JSON文件时，直接使用`json.load()`和`json.dump()`处理文件，而不是先读取文件内容再使用`json.loads()`和`json.dumps()`。

2. **选择更高效的库**：考虑使用第三方库如`ujson`、`orjson`或`simplejson`，它们通常比标准库的`json`模块快很多。

3. **减少数据转换**：尽量避免不必要的数据类型转换，特别是在处理大量数据时。

4. **使用生成器**：当处理大型数据集时，使用生成器逐个处理数据项，而不是一次性将所有数据加载到内存中。

5. **压缩数据**：对于需要传输或存储的大型JSON数据，可以使用gzip或其他压缩方法减小数据大小。

6. **数据结构优化**：设计更紧凑的JSON结构，避免不必要的嵌套和重复数据。

## 7. 安全性考虑

在处理JSON数据时，需要注意以下安全问题：

### 7.1 常见安全风险

1. **注入攻击**：如果JSON数据来自不可信来源，可能包含恶意代码。

2. **拒绝服务攻击**：恶意构造的JSON数据（如深层嵌套或超大数组）可能导致解析器崩溃或消耗大量资源。

3. **敏感信息泄露**：JSON数据可能包含敏感信息，如果不适当处理可能导致信息泄露。

4. **类型混淆**：JSON数据中的类型信息有限，可能导致类型混淆问题。

### 7.2 安全最佳实践

```python
import json
import re
import sys

def json_security_best_practices():
    """JSON处理的安全最佳实践示例"""
    
    print("=== JSON处理的安全最佳实践 ===")
    
    # 1. 限制JSON大小
    def safe_json_loads(json_str, max_size=1024 * 1024):  # 默认限制为1MB
        """安全地加载JSON字符串，限制大小"""
        if len(json_str) > max_size:
            raise ValueError(f"JSON数据过大，超过限制: {max_size} 字节")
        return json.loads(json_str)
    
    # 2. 限制递归深度
    original_recursion_limit = sys.getrecursionlimit()
    try:
        def safe_json_loads_with_depth_limit(json_str, max_depth=100):
            """安全地加载JSON字符串，限制递归深度"""
            # 临时设置递归限制
            old_limit = sys.getrecursionlimit()
            sys.setrecursionlimit(max_depth + 10)  # 增加一点缓冲区
            try:
                # 检查JSON字符串中的嵌套深度
                brace_count = 0
                bracket_count = 0
                max_nesting = 0
                in_string = False
                escape = False
                
                for char in json_str:
                    if char == '"' and not escape:
                        in_string = not in_string
                    elif char == '\\' and in_string:
                        escape = not escape
                    else:
                        escape = False
                    
                    if not in_string:
                        if char == '{':
                            brace_count += 1
                            max_nesting = max(max_nesting, brace_count + bracket_count)
                        elif char == '}':
                            brace_count -= 1
                        elif char == '[':
                            bracket_count += 1
                            max_nesting = max(max_nesting, brace_count + bracket_count)
                        elif char == ']':
                            bracket_count -= 1
                
                if max_nesting > max_depth:
                    raise ValueError(f"JSON嵌套深度过大，超过限制: {max_depth}")
                
                return json.loads(json_str)
            finally:
                # 恢复原始递归限制
                sys.setrecursionlimit(old_limit)
    finally:
        sys.setrecursionlimit(original_recursion_limit)
    
    # 3. 验证和清理数据
    def sanitize_string(s):
        """清理字符串，移除潜在的危险字符"""
        if not isinstance(s, str):
            return s
        
        # 移除控制字符（除了\t, \n, \r）
        s = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f]', '', s)
        
        # 限制字符串长度
        max_length = 10000
        if len(s) > max_length:
            s = s[:max_length] + "..."  # 截断过长字符串
        
        return s
    
    def sanitize_json_data(data):
        """递归清理JSON数据中的所有字符串"""
        if isinstance(data, dict):
            return {key: sanitize_json_data(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [sanitize_json_data(item) for item in data]
        elif isinstance(data, str):
            return sanitize_string(data)
        else:
            return data
    
    # 4. 白名单验证
    def validate_json_structure(data, allowed_keys=None, allowed_types=None):
        """验证JSON数据结构是否符合白名单要求"""
        if allowed_keys is None:
            allowed_keys = set()
        
        if allowed_types is None:
            allowed_types = {dict, list, str, int, float, bool, type(None)}
        
        if isinstance(data, dict):
            # 检查字典的键是否在白名单中
            for key in data.keys():
                if key not in allowed_keys:
                    return False, f"不允许的键: {key}"
            
            # 递归检查字典的值
            for value in data.values():
                valid, error = validate_json_structure(value, allowed_keys, allowed_types)
                if not valid:
                    return False, error
        
        elif isinstance(data, list):
            # 递归检查列表的每个元素
            for item in data:
                valid, error = validate_json_structure(item, allowed_keys, allowed_types)
                if not valid:
                    return False, error
        
        # 检查数据类型是否在白名单中
        if type(data) not in allowed_types:
            return False, f"不允许的数据类型: {type(data).__name__}"
        
        return True, ""
    
    # 测试安全实践
    print("\n测试安全最佳实践:")
    
    # 测试1: 大小限制
    print("\n1. 测试大小限制:")
    try:
        large_json = '{"data":"' + 'x' * (1024 * 1024 + 1) + '"}'
        safe_json_loads(large_json)
    except ValueError as e:
        print(f"成功捕获过大的JSON: {e}")
    
    # 测试2: 深度限制
    print("\n2. 测试深度限制:")
    # 创建一个深度嵌套的JSON
    nested_data = {"level": 1}
    current = nested_data
    for i in range(2, 150):  # 创建150层嵌套
        current["next"] = {"level": i}
        current = current["next"]
    
    nested_json = json.dumps(nested_data)
    
    try:
        safe_json_loads_with_depth_limit(nested_json, max_depth=100)
    except ValueError as e:
        print(f"成功捕获过深的JSON嵌套: {e}")
    
    # 测试3: 数据清理
    print("\n3. 测试数据清理:")
    # 创建包含潜在危险字符的JSON
    dangerous_data = {
        "username": "admin\x00user",  # 包含null字符
        "description": "Normal text\x07with\x00control\x1bchars",
        "very_long_string": "x" * 15000  # 过长字符串
    }
    
    cleaned_data = sanitize_json_data(dangerous_data)
    print(f"清理前的username: {repr(dangerous_data['username'])}")
    print(f"清理后的username: {repr(cleaned_data['username'])}")
    print(f"清理前的description: {repr(dangerous_data['description'])}")
    print(f"清理后的description: {repr(cleaned_data['description'])}")
    print(f"清理前的字符串长度: {len(dangerous_data['very_long_string'])}")
    print(f"清理后的字符串长度: {len(cleaned_data['very_long_string'])}")
    
    # 测试4: 白名单验证
    print("\n4. 测试白名单验证:")
    # 定义允许的键和类型
    allowed_keys = {"name", "age", "email", "active"}
    allowed_types = {dict, str, int, bool}
    
    # 有效的JSON
    valid_json = {"name": "张三", "age": 30, "email": "zhangsan@example.com", "active": True}
    valid, error = validate_json_structure(valid_json, allowed_keys, allowed_types)
    print(f"有效JSON验证结果: {valid}, 错误: {error}")
    
    # 无效的JSON（包含不允许的键）
    invalid_json1 = {"name": "李四", "age": 25, "password": "secret123"}  # password是不允许的键
    valid, error = validate_json_structure(invalid_json1, allowed_keys, allowed_types)
    print(f"无效JSON(不允许的键)验证结果: {valid}, 错误: {error}")
    
    # 无效的JSON（包含不允许的类型）
    invalid_json2 = {"name": "王五", "age": 35, "scores": [95, 87, 92]}  # scores是数组类型，不在允许列表中
    valid, error = validate_json_structure(invalid_json2, allowed_keys, allowed_types)
    print(f"无效JSON(不允许的类型)验证结果: {valid}, 错误: {error}")
    
    print("\nJSON处理的安全最佳实践总结:")
    print("1. 限制JSON数据大小，防止过大的输入消耗过多资源")
    print("2. 限制JSON嵌套深度，防止递归炸弹攻击")
    print("3. 验证数据结构和类型，使用白名单方法只允许预期的数据格式")
    print("4. 清理和净化输入数据，移除控制字符和潜在危险内容")
    print("5. 避免在JSON中存储敏感信息，如密码或私钥")
    print("6. 对来自不可信来源的JSON数据进行全面验证")
    print("7. 使用专门的安全库处理敏感JSON数据")
    print("8. 实现适当的错误处理，避免泄露系统信息")

# 运行示例
json_security_best_practices()
```

## 8. 与其他序列化方法的比较

Python中还有其他几种数据序列化方法，每种方法都有其优缺点和适用场景：

### 8.1 各种序列化方法对比

| 方法 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| **JSON** | 跨语言兼容、人类可读、轻量级 | 仅支持基本数据类型、性能一般 | Web API、配置文件、数据交换 |
| **Pickle** | 支持几乎所有Python对象、使用简单 | 不安全、仅Python可用、二进制格式 | Python内部对象存储、缓存 |
| **MessagePack** | 高性能、紧凑、跨语言 | 不是人类可读的、需要额外库 | 高性能数据交换、网络协议 |
| **Protocol Buffers** | 高性能、强类型、跨语言 | 设置复杂、需要预定义模式 | 大规模数据交换、RPC系统 |
| **YAML** | 人类可读、支持注释、功能丰富 | 解析速度较慢、需要额外库 | 配置文件、文档、数据序列化 |
| **XML** | 成熟、广泛支持、自描述 | 冗长、解析复杂、效率较低 | 遗留系统、某些Web服务 |

### 8.2 JSON与Pickle的比较

```python
import json
import pickle
import time
import os

def json_vs_pickle_comparison():
    """JSON与Pickle序列化方法的比较"""
    
    print("=== JSON与Pickle序列化方法的比较 ===")
    
    # 准备测试数据
    print("准备测试数据...")
    test_data = {
        "string": "Hello, 世界!",
        "integer": 42,
        "float": 3.14159,
        "boolean": True,
        "none_value": None,
        "list": [1, 2, 3, 4, 5, "text", True],
        "dict": {"key1": "value1", "key2": [1, 2, 3]},
        "nested": {
            "level1": {
                "level2": {
                    "level3": "deeply nested"
                }
            }
        }
    }
    
    # 1. 基本序列化和反序列化比较
    print("\n1. 基本序列化和反序列化:")
    
    # JSON序列化
    json_start = time.time()
    json_data = json.dumps(test_data)
    json_dump_time = time.time() - json_start
    
    # Pickle序列化
    pickle_start = time.time()
    pickle_data = pickle.dumps(test_data)
    pickle_dump_time = time.time() - pickle_start
    
    print(f"JSON序列化大小: {len(json_data)} 字节")
    print(f"Pickle序列化大小: {len(pickle_data)} 字节")
    print(f"JSON序列化时间: {json_dump_time*1000:.3f} 毫秒")
    print(f"Pickle序列化时间: {pickle_dump_time*1000:.3f} 毫秒")
    
    # JSON反序列化
    json_start = time.time()
    json_loaded = json.loads(json_data)
    json_load_time = time.time() - json_start
    
    # Pickle反序列化
    pickle_start = time.time()
    pickle_loaded = pickle.loads(pickle_data)
    pickle_load_time = time.time() - pickle_start
    
    print(f"JSON反序列化时间: {json_load_time*1000:.3f} 毫秒")
    print(f"Pickle反序列化时间: {pickle_load_time*1000:.3f} 毫秒")
    
    # 2. 复杂对象序列化比较
    print("\n2. 复杂对象序列化:")
    
    # 定义一个自定义类
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def greet(self):
            return f"Hello, my name is {self.name}!"
    
    # 创建一个自定义对象
    person = Person("张三", 30)
    
    # 尝试用JSON序列化（应该会失败）
    print("尝试用JSON序列化自定义对象:")
    try:
        json.dumps(person)
        print("成功")
    except TypeError as e:
        print(f"失败: {e}")
    
    # 尝试用Pickle序列化（应该会成功）
    print("尝试用Pickle序列化自定义对象:")
    try:
        pickled_person = pickle.dumps(person)
        print(f"成功，序列化大小: {len(pickled_person)} 字节")
        
        # 反序列化并验证
        unpickled_person = pickle.loads(pickled_person)
        print(f"反序列化后类型: {type(unpickled_person).__name__}")
        print(f"方法调用结果: {unpickled_person.greet()}")
    except Exception as e:
        print(f"失败: {e}")
    
    # 3. 文件操作比较
    print("\n3. 文件操作比较:")
    
    # JSON文件操作
    json_file = "test_data.json"
    pickle_file = "test_data.pickle"
    
    # 写入文件
    json_start = time.time()
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(test_data, f)
    json_write_time = time.time() - json_start
    
    pickle_start = time.time()
    with open(pickle_file, "wb") as f:
        pickle.dump(test_data, f)
    pickle_write_time = time.time() - pickle_start
    
    # 获取文件大小
    json_file_size = os.path.getsize(json_file)
    pickle_file_size = os.path.getsize(pickle_file)
    
    print(f"JSON文件大小: {json_file_size} 字节")
    print(f"Pickle文件大小: {pickle_file_size} 字节")
    print(f"JSON写入时间: {json_write_time*1000:.3f} 毫秒")
    print(f"Pickle写入时间: {pickle_write_time*1000:.3f} 毫秒")
    
    # 从文件读取
    json_start = time.time()
    with open(json_file, "r", encoding="utf-8") as f:
        json_read_data = json.load(f)
    json_read_time = time.time() - json_start
    
    pickle_start = time.time()
    with open(pickle_file, "rb") as f:
        pickle_read_data = pickle.load(f)
    pickle_read_time = time.time() - pickle_start
    
    print(f"JSON读取时间: {json_read_time*1000:.3f} 毫秒")
    print(f"Pickle读取时间: {pickle_read_time*1000:.3f} 毫秒")
    
    # 清理测试文件
    for file in [json_file, pickle_file]:
        if os.path.exists(file):
            os.remove(file)
    
    print("\n4. 可读性比较:")
    print("JSON示例:")
    print(json.dumps(test_data, indent=2))
    print("\nPickle示例(二进制数据，显示前100个字节):")
    print(repr(pickle_data[:100]))
    
    print("\nJSON与Pickle的选择建议:")
    print("选择JSON当:")
    print("1. 需要跨语言兼容性")
    print("2. 数据需要人类可读")
    print("3. 处理简单的数据结构")
    print("4. 安全性要求较高")
    print("5. 数据需要网络传输或存储为可读格式")
    
    print("\n选择Pickle当:")
    print("1. 只需Python内部使用")
    print("2. 需要序列化复杂的Python对象")
    print("3. 性能是首要考虑因素")
    print("4. 不需要考虑数据的可读性")
    print("5. 处理循环引用或特殊Python类型")
    
    print("\n安全提示: 不要使用pickle加载来自不可信来源的数据，因为它可以执行任意代码。")

# 运行示例
json_vs_pickle_comparison()
```

### 8.3 JSON与YAML的比较

```python
import json
import yaml
import time
import os

def json_vs_yaml_comparison():
    """JSON与YAML序列化方法的比较"""
    
    print("=== JSON与YAML序列化方法的比较 ===")
    
    try:
        # 准备测试数据
        print("准备测试数据...")
        test_data = {
            "string": "Hello, 世界!",
            "integer": 42,
            "float": 3.14159,
            "boolean": True,
            "none_value": None,
            "list": [1, 2, 3, 4, 5],
            "dict": {"key1": "value1", "key2": [1, 2, 3]},
            "nested": {
                "level1": {
                    "level2": {
                        "level3": "deeply nested"
                    }
                }
            },
            "special_chars": "!@#$%^&*()_+"
        }
        
        # 1. 基本序列化和反序列化比较
        print("\n1. 基本序列化和反序列化:")
        
        # JSON序列化
        json_start = time.time()
        json_data = json.dumps(test_data, indent=2)
        json_dump_time = time.time() - json_start
        
        # YAML序列化
        yaml_start = time.time()
        yaml_data = yaml.dump(test_data, default_flow_style=False, allow_unicode=True)
        yaml_dump_time = time.time() - yaml_start
        
        print(f"JSON序列化大小: {len(json_data)} 字节")
        print(f"YAML序列化大小: {len(yaml_data)} 字节")
        print(f"JSON序列化时间: {json_dump_time*1000:.3f} 毫秒")
        print(f"YAML序列化时间: {yaml_dump_time*1000:.3f} 毫秒")
        
        # JSON反序列化
        json_start = time.time()
        json_loaded = json.loads(json_data)
        json_load_time = time.time() - json_start
        
        # YAML反序列化
        yaml_start = time.time()
        yaml_loaded = yaml.safe_load(yaml_data)
        yaml_load_time = time.time() - yaml_start
        
        print(f"JSON反序列化时间: {json_load_time*1000:.3f} 毫秒")
        print(f"YAML反序列化时间: {yaml_load_time*1000:.3f} 毫秒")
        
        # 2. 可读性和功能比较
        print("\n2. 可读性和功能比较:")
        print("JSON示例:")
        print(json.dumps(test_data, indent=2))
        print("\nYAML示例:")
        print(yaml.dump(test_data, default_flow_style=False, allow_unicode=True))
        
        # 3. 注释支持
        print("\n3. 注释支持:")
        yaml_with_comments = '''
# 这是一个YAML配置文件
# 创建于2023年

name: 张三     # 用户名称
age: 30       # 用户年龄
preferences:  # 用户偏好设置
  theme: dark  # 界面主题
  notifications: true  # 是否启用通知
'''
        
        print("YAML支持注释:")
        print(yaml_with_comments)
        print("\n解析带注释的YAML:")
        parsed_yaml = yaml.safe_load(yaml_with_comments)
        print(parsed_yaml)
        
        print("\nJSON不原生支持注释。")
        
        # 4. 复杂数据结构
        print("\n4. 复杂数据结构处理:")
        # YAML支持锚点和引用，减少重复
        yaml_with_anchors = '''
defaults: &defaults
  host: localhost
  port: 8080
  debug: false

production: *defaults

staging:
  <<: *defaults
  port: 8081
  debug: true
'''
        
        print("YAML支持锚点和引用:")
        print(yaml_with_anchors)
        print("\n解析带锚点的YAML:")
        parsed_yaml = yaml.safe_load(yaml_with_anchors)
        print(yaml.dump(parsed_yaml, default_flow_style=False))
        
        # 5. 文件操作比较
        print("\n5. 文件操作比较:")
        
        json_file = "config.json"
        yaml_file = "config.yaml"
        
        # 写入文件
        json_start = time.time()
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(test_data, f, indent=2)
        json_write_time = time.time() - json_start
        
        yaml_start = time.time()
        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(test_data, f, default_flow_style=False, allow_unicode=True)
        yaml_write_time = time.time() - yaml_start
        
        # 获取文件大小
        json_file_size = os.path.getsize(json_file)
        yaml_file_size = os.path.getsize(yaml_file)
        
        print(f"JSON文件大小: {json_file_size} 字节")
        print(f"YAML文件大小: {yaml_file_size} 字节")
        print(f"JSON写入时间: {json_write_time*1000:.3f} 毫秒")
        print(f"YAML写入时间: {yaml_write_time*1000:.3f} 毫秒")
        
        # 从文件读取
        json_start = time.time()
        with open(json_file, "r", encoding="utf-8") as f:
            json_read_data = json.load(f)
        json_read_time = time.time() - json_start
        
        yaml_start = time.time()
        with open(yaml_file, "r", encoding="utf-8") as f:
            yaml_read_data = yaml.safe_load(f)
        yaml_read_time = time.time() - yaml_start
        
        print(f"JSON读取时间: {json_read_time*1000:.3f} 毫秒")
        print(f"YAML读取时间: {yaml_read_time*1000:.3f} 毫秒")
        
        # 清理测试文件
        for file in [json_file, yaml_file]:
            if os.path.exists(file):
                os.remove(file)
        
        print("\nJSON与YAML的选择建议:")
        print("选择JSON当:")
        print("1. 需要更快的解析速度")
        print("2. 数据需要更紧凑的表示")
        print("3. 与Web API交互（大多数API使用JSON）")
        print("4. 需要更好的跨语言支持")
        print("5. 处理机器生成和消费的数据")
        
        print("\n选择YAML当:")
        print("1. 需要人类友好的配置文件")
        print("2. 需要支持注释")
        print("3. 数据结构更复杂，需要减少重复（使用锚点）")
        print("4. 配置文件需要被手动编辑")
        print("5. 可读性比性能更重要")
        
        print("\n安全提示: 使用yaml.safe_load()而非yaml.load()来防止执行任意代码。")
        
    except ImportError:
        print("无法运行YAML比较示例，请先安装PyYAML库:")
        print("pip install pyyaml")
    except Exception as e:
        print(f"执行过程中出错: {e}")

# 运行示例
json_vs_yaml_comparison()
```

## 9. 最佳实践和注意事项

### 9.1 通用最佳实践

1. **使用适当的函数**：根据需求选择正确的函数 - `dumps`/`loads`用于字符串，`dump`/`load`用于文件。

2. **处理编码问题**：在处理非ASCII字符时，使用`ensure_ascii=False`参数确保正确编码。

3. **错误处理**：始终使用try-except块捕获可能的`JSONDecodeError`异常。

4. **格式化输出**：使用`indent`参数使JSON输出更易读，特别是用于调试或配置文件。

5. **安全处理**：对于来自不可信来源的JSON数据，进行验证和清理。

6. **内存考虑**：处理大型JSON数据时，使用流式处理或分块处理避免内存问题。

### 9.2 常见陷阱和解决方案

```python
import json
import sys

def json_common_pitfalls():
    """JSON处理中的常见陷阱和解决方案"""
    
    print("=== JSON处理中的常见陷阱和解决方案 ===")
    
    # 陷阱1: 非ASCII字符处理
    print("\n陷阱1: 非ASCII字符处理")
    
    # 包含中文的数据
    data_with_unicode = {"name": "张三", "message": "你好，世界!"}
    
    print("默认行为（ensure_ascii=True）:")
    json_str1 = json.dumps(data_with_unicode)
    print(json_str1)
    print("\n设置ensure_ascii=False:")
    json_str2 = json.dumps(data_with_unicode, ensure_ascii=False)
    print(json_str2)
    
    print("\n解决方案: 总是使用ensure_ascii=False来保持非ASCII字符的可读性")
    
    # 陷阱2: 字典键不是字符串
    print("\n陷阱2: 字典键不是字符串")
    
    data_with_nonstring_keys = {
        1: "one",  # 整数键
        2.5: "two_point_five",  # 浮点数键
        (1, 2): "tuple_key"  # 元组键 - 这会导致错误
    }
    
    try:
        print("尝试序列化包含非字符串键的字典:")
        json.dumps(data_with_nonstring_keys)
    except TypeError as e:
        print(f"错误: {e}")
    
    # 解决方案: 转换字典键为字符串
    print("\n解决方案: 转换字典键为字符串")
    try:
        # 处理简单的非字符串键（元组键仍需特殊处理）
        safe_data = {str(key): value for key, value in data_with_nonstring_keys.items() if not isinstance(key, tuple)}
        safe_data["tuple_key"] = data_with_nonstring_keys[(1, 2)]  # 手动处理元组键
        print(f"转换后的安全数据: {safe_data}")
        print(f"序列化结果: {json.dumps(safe_data, ensure_ascii=False)}")
    except Exception as e:
        print(f"处理错误: {e}")
    
    # 陷阱3: 不支持的Python类型
    print("\n陷阱3: 不支持的Python类型")
    
    from datetime import datetime
    from decimal import Decimal
    
    unsupported_data = {
        "datetime": datetime.now(),  # datetime对象
        "decimal": Decimal("123.45"),  # Decimal对象
        "complex": 1 + 2j,  # 复数
        "set": {1, 2, 3}  # 集合
    }
    
    try:
        print("尝试序列化不支持的Python类型:")
        json.dumps(unsupported_data)
    except TypeError as e:
        print(f"错误: {e}")
    
    # 解决方案: 创建自定义编码器
    print("\n解决方案: 使用自定义编码器")
    
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, Decimal):
                return float(obj)  # 注意: 这可能会损失精度
            elif isinstance(obj, set):
                return list(obj)
            raise TypeError(f"无法序列化 {type(obj).__name__} 类型")
    
    try:
        # 处理复数（复数需要特殊处理，或者直接排除）
        safe_data = unsupported_data.copy()
        del safe_data["complex"]  # 移除复数类型
        
        json_str = json.dumps(safe_data, cls=CustomEncoder)
        print(f"序列化结果: {json_str}")
    except Exception as e:
        print(f"处理错误: {e}")
    
    # 陷阱4: 循环引用
    print("\n陷阱4: 循环引用")
    
    dict1 = {"name": "dict1"}
    dict2 = {"name": "dict2"}
    dict1["ref"] = dict2  # dict1引用dict2
    dict2["ref"] = dict1  # dict2引用dict1，形成循环
    
    try:
        print("尝试序列化包含循环引用的数据:")
        json.dumps(dict1)
    except RecursionError as e:
        print(f"错误: 递归深度超过限制（循环引用导致）")
    
    # 解决方案: 检测并处理循环引用
    print("\n解决方案: 检测并处理循环引用")
    
    def serialize_without_cycles(obj, seen=None):
        """序列化对象，避免循环引用"""
        if seen is None:
            seen = set()
        
        if isinstance(obj, dict):
            obj_id = id(obj)
            if obj_id in seen:
                return "[循环引用]"
            seen.add(obj_id)
            result = {}
            for key, value in obj.items():
                result[key] = serialize_without_cycles(value, seen.copy())
            return result
        elif isinstance(obj, list):
            return [serialize_without_cycles(item, seen.copy()) for item in obj]
        elif isinstance(obj, tuple):
            return tuple(serialize_without_cycles(item, seen.copy()) for item in obj)
        else:
            return obj
    
    try:
        safe_data = serialize_without_cycles(dict1)
        print(f"处理后的数据: {safe_data}")
        print(f"序列化结果: {json.dumps(safe_data)}")
    except Exception as e:
        print(f"处理错误: {e}")
    
    # 陷阱5: 浮点数精度问题
    print("\n陷阱5: 浮点数精度问题")
    
    float_data = {
        "value": 0.1 + 0.2  # 这在Python中不完全等于0.3
    }
    
    print(f"原始Python值: {float_data['value']}")
    json_str = json.dumps(float_data)
    print(f"JSON序列化后: {json_str}")
    loaded_data = json.loads(json_str)
    print(f"JSON反序列化后: {loaded_data['value']}")
    print(f"与0.3比较: {loaded_data['value'] == 0.3}")
    
    # 解决方案: 使用Decimal或四舍五入
    print("\n解决方案: 使用Decimal处理精度问题")
    
    from decimal import Decimal, getcontext
    getcontext().prec = 10
    
    # 使用Decimal存储精确值
    decimal_data = {
        "value": float(Decimal("0.1") + Decimal("0.2"))  # 先使用Decimal精确计算
    }
    
    print(f"使用Decimal计算后的值: {decimal_data['value']}")
    print(f"与0.3比较: {abs(decimal_data['value'] - 0.3) < 1e-10}")
    
    # 陷阱6: 超大数值处理
    print("\n陷阱6: 超大数值处理")
    
    large_number = 2 ** 1000  # 一个非常大的整数
    large_data = {"large_number": large_number}
    
    print(f"超大整数: {large_number}")
    print(f"类型: {type(large_number).__name__}")
    
    # 序列化和反序列化
    json_str = json.dumps(large_data)
    print(f"JSON序列化后: {json_str}")
    loaded_data = json.loads(json_str)
    print(f"JSON反序列化后: {loaded_data['large_number']}")
    print(f"类型: {type(loaded_data['large_number']).__name__}")
    print(f"值相等: {loaded_data['large_number'] == large_number}")
    
    print("\n注意: JSON可以表示任意大的整数，但反序列化后在某些语言中可能成为浮点数")
    print("Python中JSON模块会将大整数保持为整数类型，这是Python的优势")
    
    # 陷阱7: 错误处理不充分
    print("\n陷阱7: 错误处理不充分")
    
    invalid_json = '{"name": "John", "age": }'  # 缺少age的值
    
    # 不好的做法
    print("不好的做法（没有错误处理）:")
    try:
        # 这里会出错，但如果没有try-except会导致程序崩溃
        # data = json.loads(invalid_json)
        print("[示例: 没有错误处理会导致程序崩溃]")
    except Exception:
        pass
    
    # 好的做法
    print("\n好的做法（有错误处理）:")
    try:
        data = json.loads(invalid_json)
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        print(f"错误位置: {e.pos}")
        print(f"错误消息: {e.msg}")
        # 可以在这里添加恢复逻辑或提示用户
    
    print("\nJSON处理的最佳实践总结:")
    print("1. 总是处理编码问题，特别是非ASCII字符")
    print("2. 确保字典键都是字符串类型")
    print("3. 为不支持的Python类型创建自定义编码器")
    print("4. 小心处理循环引用，使用适当的检测机制")
    print("5. 对于需要精确计算的场景，使用Decimal类型")
    print("6. 实现充分的错误处理，特别是JSONDecodeError")
    print("7. 处理大型JSON数据时，考虑内存使用和性能")
    print("8. 对来自不可信来源的数据进行安全验证")
    print("9. 选择合适的序列化格式（JSON、Pickle、YAML等）")
    print("10. 对于配置文件，考虑使用yaml.safe_load()以支持注释")

# 运行示例
json_common_pitfalls()
```

## 10. 总结

json模块是Python中处理JSON数据的核心工具，它提供了简单而强大的API来序列化和反序列化数据。通过本模块的学习，我们了解了：

1. **基本用法**：如何使用`dumps`/`loads`和`dump`/`load`函数处理JSON数据

2. **数据类型转换**：Python和JSON之间的类型映射规则

3. **自定义序列化**：如何创建自定义编码器和解码器处理复杂对象

4. **高级应用**：配置管理、API数据处理、数据验证等实际应用场景

5. **性能优化**：处理大型JSON数据的技巧和方法

6. **安全性考虑**：如何安全地处理JSON数据，避免常见的安全风险

7. **比较选择**：与其他序列化方法（如Pickle、YAML）的比较和选择建议

8. **最佳实践**：避免常见陷阱，编写更健壮的JSON处理代码

json模块虽然简单，但在实际应用中非常重要，特别是在Web开发、数据交换和配置管理等场景。掌握json模块的正确使用方法，可以帮助我们更高效、更安全地处理各种数据交换需求。

在使用json模块时，最重要的是要根据具体需求选择合适的方法，并始终关注数据的安全性和完整性。对于复杂的应用场景，可能需要结合其他库（如jsonschema、PyYAML等）来获得更强大的功能。