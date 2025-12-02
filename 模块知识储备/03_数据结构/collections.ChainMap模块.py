# collections.ChainMap模块 - Python标准库中的映射链

"""
 collections.ChainMap是Python标准库中提供的一种数据结构，
它允许多个字典或其他映射组合在一起，形成一个单一的、可更新的映射视图。

ChainMap维护一个映射列表，并按照列表顺序搜索键。如果在多个映射中都有同一个键，
则返回第一个映射（最前面的映射）中的值。

这种数据结构在处理嵌套配置、默认值和作用域（如变量查找）等场景中特别有用。
"""

# 1. 核心功能介绍

print("=== 1. 核心功能介绍 ===")
print("\ncollections.ChainMap模块提供了以下主要功能:")
print("1. 将多个字典组合成单一的映射视图")
print("2. 按顺序搜索键，前面的映射优先")
print("3. 支持所有标准字典操作（查找、插入、删除等）")
print("4. 可以通过属性访问底层映射列表")
print("5. 提供创建子上下文的方法，便于处理嵌套作用域")

# 2. 基本操作

print("\n=== 2. 基本操作 ===")

# 导入ChainMap
from collections import ChainMap

print("\n2.1 创建ChainMap")
print("可以通过多种方式创建ChainMap:")

# 从多个字典创建
user_config = {"theme": "dark", "font_size": 12, "show_notifications": True}
system_config = {"theme": "light", "font_size": 10, "max_connections": 100}
default_config = {"theme": "default", "font_size": 12, "show_notifications": False}

# 创建ChainMap
config = ChainMap(user_config, system_config, default_config)
print(f"用户配置: {user_config}")
print(f"系统配置: {system_config}")
print(f"默认配置: {default_config}")
print(f"ChainMap: {config}")

# 从单个字典创建
cm1 = ChainMap({"a": 1})
print(f"单个字典ChainMap: {cm1}")

# 创建空ChainMap
cm2 = ChainMap()
print(f"空ChainMap: {cm2}")

print("\n2.2 访问元素")
print("ChainMap的访问方式与普通字典类似:")

config = ChainMap(user_config, system_config, default_config)

# 通过键访问值
print(f"theme: {config['theme']}")  # 从user_config中获取
print(f"font_size: {config['font_size']}")  # 从user_config中获取
print(f"max_connections: {config['max_connections']}")  # 从system_config中获取

# 使用get方法访问（与字典相同）
print(f"show_notifications: {config.get('show_notifications')}")  # 从user_config中获取
print(f"unknown_key: {config.get('unknown_key', 'default_value')}")  # 使用默认值

# 检查键是否存在
print(f"'theme'在ChainMap中: {'theme' in config}")
print(f"'unknown_key'在ChainMap中: {'unknown_key' in config}")

print("\n2.3 修改操作")
print("ChainMap的修改操作只影响第一个映射（maps[0]）:")

config = ChainMap(user_config, system_config, default_config)
print(f"修改前: {config}")

# 添加新键值对
config["new_setting"] = "new_value"
print(f"添加new_setting后: {config}")
print(f"user_config被修改: {user_config}")

# 修改现有键（只修改第一个映射中存在的键）
config["theme"] = "custom"
print(f"修改theme后: {config}")
print(f"user_config被修改: {user_config}")
print(f"system_config未被修改: {system_config}")

# 删除键（只能删除第一个映射中的键）
del config["show_notifications"]
print(f"删除show_notifications后: {config}")
print(f"user_config被修改: {user_config}")

print("\n2.4 查看底层映射")
print("ChainMap的maps属性返回包含所有映射的列表:")

config = ChainMap(user_config, system_config, default_config)
print(f"底层映射列表: {config.maps}")
print(f"第一个映射(用户配置): {config.maps[0]}")
print(f"第二个映射(系统配置): {config.maps[1]}")
print(f"映射数量: {len(config.maps)}")

print("\n2.5 映射操作")
print("ChainMap支持许多标准字典操作:")

config = ChainMap(user_config, system_config, default_config)

# 获取所有键（从所有映射中）
print(f"所有键: {list(config.keys())}")

# 获取所有值（从所有映射中，键重复时只取第一个）
print(f"所有值: {list(config.values())}")

# 获取所有项（键值对）
print(f"所有项: {list(config.items())}")

# 获取ChainMap中不同键的数量
print(f"不同键的数量: {len(config)}")

# 更新ChainMap（只更新第一个映射）
config.update({"font_size": 14, "new_param": "new_value"})
print(f"更新后的ChainMap: {config}")
print(f"更新后的第一个映射: {config.maps[0]}")

# 清空ChainMap（只清空第一个映射）
# config.clear()  # 取消注释以测试
# print(f"清空后的ChainMap: {config}")
# print(f"清空后的第一个映射: {config.maps[0]}")

# 3. 高级用法

print("\n=== 3. 高级用法 ===")

print("\n3.1 创建子上下文")
print("使用new_child()方法可以创建一个包含新映射的子上下文:")

# 创建基本配置
base_config = {"theme": "default", "font_size": 12}

# 创建ChainMap
config = ChainMap(base_config)
print(f"基础配置: {config}")

# 创建子上下文
child_config = config.new_child({"theme": "dark", "debug": True})
print(f"子上下文配置: {child_config}")
print(f"子上下文的底层映射: {child_config.maps}")

# 子上下文中的修改不会影响父上下文
child_config["font_size"] = 14
print(f"修改后的子上下文: {child_config}")
print(f"父上下文保持不变: {config}")

print("\n3.2 获取父上下文")
print("使用parents属性可以获取不包含第一个映射的ChainMap:")

config = ChainMap(user_config, system_config, default_config)
print(f"完整配置: {config}")

# 获取父上下文（不包含user_config）
parent_config = config.parents
print(f"父上下文（无用户配置）: {parent_config}")
print(f"父上下文的底层映射: {parent_config.maps}")

# 测试查找（会跳过user_config）
print(f"父上下文中的theme: {parent_config['theme']}")  # 应该从system_config获取

print("\n3.3 合并ChainMap")
print("可以将多个ChainMap合并或添加到现有ChainMap:")

# 创建两个ChainMap
cm1 = ChainMap({"a": 1, "b": 2})
cm2 = ChainMap({"c": 3, "d": 4})

# 创建新的ChainMap，合并两个ChainMap的所有映射
cm_combined = ChainMap(*(cm1.maps + cm2.maps))
print(f"合并后的ChainMap: {cm_combined}")

# 另一种方式：使用new_child()
cm_combined2 = cm1.new_child()
cm_combined2.maps.extend(cm2.maps)
print(f"使用extend合并后的ChainMap: {cm_combined2}")

print("\n3.4 自定义映射类型")
print("ChainMap可以与自定义映射类型一起使用:")

from collections import UserDict

class LoggingDict(UserDict):
    """
    记录所有操作的字典子类
    """
    
    def __getitem__(self, key):
        print(f"获取键 '{key}'的值")
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        print(f"设置键 '{key}'的值为 '{value}'")
        return super().__setitem__(key, value)

# 创建自定义映射
log_dict = LoggingDict({"x": 10, "y": 20})
normal_dict = {"z": 30}

# 创建包含自定义映射的ChainMap
cm = ChainMap(log_dict, normal_dict)
print(f"访问x: {cm['x']}")
print(f"访问z: {cm['z']}")
cm["x"] = 15  # 这会调用LoggingDict的__setitem__

print("\n3.5 递归ChainMap")
print("可以创建递归的ChainMap结构，用于复杂的嵌套配置:")

def create_nested_config(base_config, overrides):
    """
    创建嵌套的配置ChainMap
    
    Args:
        base_config: 基础配置字典
        overrides: 覆盖配置字典列表
    
    Returns:
        嵌套的ChainMap
    """
    # 从最后一个覆盖配置开始，向前构建ChainMap
    result = ChainMap(base_config)
    for override in reversed(overrides):
        result = result.new_child(override)
    return result

# 创建测试配置
base = {"app_name": "MyApp", "version": "1.0", "debug": False}
env_dev = {"debug": True, "log_level": "DEBUG"}
env_prod = {"debug": False, "log_level": "INFO", "max_connections": 100}
feature_flags = {"new_ui": True, "experimental_features": False}

# 创建嵌套配置
dev_config = create_nested_config(base, [env_dev, feature_flags])
prod_config = create_nested_config(base, [env_prod])

print(f"开发环境配置: {dev_config}")
print(f"生产环境配置: {prod_config}")

print("\n3.6 与dict的转换")
print("ChainMap可以转换为普通字典，但会丢失多映射的结构:")

config = ChainMap(user_config, system_config, default_config)
print(f"ChainMap: {config}")

# 转换为普通字典（只保留每个键的第一个值）
config_dict = dict(config)
print(f"转换为字典: {config_dict}")

# 转换回ChainMap
new_config = ChainMap(config_dict)
print(f"转换回ChainMap: {new_config}")

# 4. 实际应用场景

print("\n=== 4. 实际应用场景 ===")

print("\n4.1 配置管理")
print("ChainMap非常适合处理具有优先级的配置系统:")
print("  - 命令行参数 > 环境变量 > 配置文件 > 默认配置")

# 示例：配置管理
print("\n示例: 配置管理系统")

default_settings = {"host": "localhost", "port": 8000, "debug": False}
config_file = {"host": "example.com", "port": 8080}
env_vars = {"debug": True}
cmd_args = {"port": 9000}

# 创建配置ChainMap
config = ChainMap(cmd_args, env_vars, config_file, default_settings)
print(f"最终配置: {config}")
print(f"host: {config['host']}")
print(f"port: {config['port']}")
print(f"debug: {config['debug']}")

print("\n4.2 作用域查找")
print("在实现编程语言解释器或脚本引擎时，ChainMap可以用于处理变量的作用域查找:")
print("  - 局部变量 > 闭包变量 > 全局变量 > 内置变量")

# 示例：简单的变量作用域
print("\n示例: 变量作用域模拟")

local_vars = {"x": 10, "y": 20}
closure_vars = {"y": 200, "z": 300}
global_vars = {"z": 30, "w": 40}
builtin_vars = {"w": 400, "print": print}

# 创建作用域ChainMap
scope = ChainMap(local_vars, closure_vars, global_vars, builtin_vars)
print(f"查找x: {scope.get('x')} (局部变量)")
print(f"查找y: {scope.get('y')} (局部变量覆盖闭包变量)")
print(f"查找z: {scope.get('z')} (闭包变量覆盖全局变量)")
print(f"查找w: {scope.get('w')} (全局变量覆盖内置变量)")

print("\n4.3 上下文管理")
print("在需要临时修改配置的场景中，可以使用ChainMap创建临时上下文:")

# 示例：临时上下文修改
print("\n示例: 临时上下文修改")

def process_data(data, config):
    # 创建临时配置上下文
    temp_config = config.new_child({"timeout": 30, "retry_count": 3})
    print(f"处理数据时使用的配置: {temp_config}")
    # 模拟数据处理
    return f"处理完成，数据长度: {len(data)}, 超时设置: {temp_config['timeout']}"

# 基础配置
base_config = {"timeout": 10, "retry_count": 1}
config = ChainMap(base_config)

# 不修改基础配置的情况下处理数据
result = process_data([1, 2, 3, 4, 5], config)
print(f"处理结果: {result}")
print(f"基础配置保持不变: {config}")

print("\n4.4 默认值处理")
print("ChainMap可以优雅地处理默认值，避免在代码中使用大量的get()方法:")

# 示例：默认值处理
print("\n示例: 默认值处理")

user_preferences = {"theme": "dark", "font_size": 14}
default_preferences = {
    "theme": "light", 
    "font_size": 12, 
    "language": "en", 
    "notifications": True
}

# 合并用户偏好和默认值
prefs = ChainMap(user_preferences, default_preferences)
print(f"主题: {prefs['theme']}")
print(f"字体大小: {prefs['font_size']}")
print(f"语言: {prefs['language']}")
print(f"通知: {prefs['notifications']}")

print("\n4.5 多级缓存")
print("ChainMap可以用于实现简单的多级缓存系统:")
print("  - 内存缓存 > 磁盘缓存 > 远程缓存")

# 示例：简单的多级缓存
print("\n示例: 多级缓存模拟")

memory_cache = {"key1": "value1"}
disk_cache = {"key2": "value2", "key3": "value3"}
remote_cache = {"key4": "value4", "key5": "value5"}

# 创建缓存ChainMap
cache = ChainMap(memory_cache, disk_cache, remote_cache)

# 缓存查找
def get_from_cache(key):
    if key in cache:
        value = cache[key]
        # 将找到的值移到内存缓存（最近使用）
        if key not in memory_cache:
            memory_cache[key] = value
        return value
    return None

print(f"查找key1: {get_from_cache('key1')}")
print(f"查找key3: {get_from_cache('key3')}")
print(f"查找key5: {get_from_cache('key5')}")
print(f"查找不存在的键: {get_from_cache('nonexistent')}")

# 现在key3应该在memory_cache中了
print(f"更新后的内存缓存: {memory_cache}")

# 5. 性能分析

print("\n=== 5. 性能分析 ===")

print("\n5.1 时间复杂度")
print("ChainMap的主要操作时间复杂度:")
print("  - 查找操作(get, []): O(k)，其中k是映射的数量，最坏情况下需要搜索所有映射")
print("  - 修改操作(setitem, delitem): O(1)，只影响第一个映射")
print("  - 新增映射(new_child): O(1)")
print("  - 获取父上下文(parents): O(1)")

print("\n5.2 与合并字典的比较")
print("与使用字典更新方法合并字典相比:")
print("  - ChainMap不会创建新的字典，而是维护现有字典的视图，内存效率更高")
print("  - ChainMap中的更改会反映到底层字典，而合并字典是静态的")
print("  - 对于频繁查找但映射数量较少的场景，ChainMap性能较好")
print("  - 对于大量映射或频繁查找不存在的键的场景，ChainMap可能不如合并字典高效")

print("\n5.3 最佳实践")
print("为了获得最佳性能:")
print("  - 经常访问的映射应该放在ChainMap的前面")
print("  - 限制ChainMap中的映射数量")
print("  - 对于只读操作，可以考虑使用合并字典代替ChainMap")
print("  - 对于需要频繁修改和保持映射分离的场景，ChainMap是更好的选择")

# 6. 使用注意事项

print("\n=== 6. 使用注意事项 ===")

print("\n6.1 修改底层字典的影响")
print("ChainMap只是底层字典的视图，如果直接修改底层字典，ChainMap的内容也会相应改变:")

user_config = {"theme": "dark"}
system_config = {"theme": "light"}
config = ChainMap(user_config, system_config)
print(f"初始ChainMap: {config}")

# 直接修改底层字典
user_config["theme"] = "custom"
print(f"修改底层字典后: {config}")

print("\n6.2 修改只影响第一个映射")
print("对ChainMap的修改操作（如__setitem__, __delitem__, update等）只会影响第一个映射:")

config = ChainMap(user_config, system_config)
print(f"修改前: {config}")

# 尝试修改一个只在第二个映射中存在的键
config["new_key"] = "new_value"
print(f"修改后: {config}")
print(f"第一个映射: {user_config}")
print(f"第二个映射: {system_config}")  # 不受影响

print("\n6.3 键重复的处理")
print("当多个映射包含相同的键时，ChainMap总是返回第一个映射中的值:")

config = ChainMap({"a": 1}, {"a": 2}, {"a": 3})
print(f"有重复键的ChainMap: {config}")
print(f"获取'a': {config['a']} (来自第一个映射)")

print("\n6.4 迭代行为")
print("ChainMap的迭代操作会返回所有映射中的键，但会跳过重复的键:")

config = ChainMap({"a": 1, "b": 2}, {"b": 20, "c": 30}, {"c": 300, "d": 400})
print(f"ChainMap: {config}")
print(f"键迭代: {list(config.keys())}")  # 每个键只出现一次
print(f"值迭代: {list(config.values())}")  # 对应键的第一个值
print(f"项迭代: {list(config.items())}")  # 每个键值对只出现一次

print("\n6.5 序列化限制")
print("ChainMap对象默认不能直接序列化为JSON或pickle，需要先转换为普通字典:")

try:
    import json
    config = ChainMap({"a": 1}, {"b": 2})
    # 这会引发TypeError
    # json.dumps(config)
    print("ChainMap不能直接序列化为JSON")
    
    # 正确的做法是先转换为字典
    config_dict = dict(config)
    print(f"转换为字典后可以序列化: {json.dumps(config_dict)}")
except ImportError:
    print("JSON模块不可用")

# 7. 综合示例：多级配置管理系统

print("\n=== 7. 综合示例：多级配置管理系统 ===")

print("\n实现一个使用ChainMap的多级配置管理系统，支持配置的加载、覆盖和合并:")

from collections import ChainMap
import os
import json
import configparser

def load_json_config(file_path):
    """
    从JSON文件加载配置
    
    Args:
        file_path: JSON文件路径
    
    Returns:
        配置字典，如果文件不存在返回空字典
    """
    if not os.path.exists(file_path):
        return {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading JSON config {file_path}: {e}")
        return {}

def load_ini_config(file_path):
    """
    从INI文件加载配置
    
    Args:
        file_path: INI文件路径
    
    Returns:
        配置字典，如果文件不存在返回空字典
    """
    if not os.path.exists(file_path):
        return {}
    
    try:
        config = configparser.ConfigParser()
        config.read(file_path, encoding='utf-8')
        
        # 转换为字典
        result = {}
        for section in config.sections():
            result[section] = dict(config[section])
        
        # 将顶层配置项也添加到结果中
        for key in config['DEFAULT']:
            result[key] = config['DEFAULT'][key]
            
        return result
    except (configparser.Error, IOError) as e:
        print(f"Error loading INI config {file_path}: {e}")
        return {}

def load_env_config(prefix="APP_"):
    """
    从环境变量加载配置
    
    Args:
        prefix: 环境变量前缀
    
    Returns:
        配置字典
    """
    result = {}
    for key, value in os.environ.items():
        if key.startswith(prefix):
            # 移除前缀并转换为小写作为键
            config_key = key[len(prefix):].lower()
            # 尝试类型转换
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            else:
                try:
                    # 尝试转换为整数
                    value = int(value)
                except ValueError:
                    try:
                        # 尝试转换为浮点数
                        value = float(value)
                    except ValueError:
                        # 保持为字符串
                        pass
            result[config_key] = value
    return result

class ConfigManager:
    """
    多级配置管理系统
    使用ChainMap管理不同来源的配置，按优先级合并
    """
    
    def __init__(self):
        """
        初始化配置管理器
        """
        # 默认配置
        self.default_config = {
            "app_name": "MyApp",
            "version": "1.0.0",
            "debug": False,
            "log_level": "INFO",
            "timeout": 30,
            "retry_count": 3,
            "database": {
                "host": "localhost",
                "port": 5432,
                "user": "postgres",
                "password": "",
                "dbname": "myapp"
            },
            "api": {
                "base_url": "http://localhost:8000",
                "timeout": 10
            }
        }
        
        # 配置来源
        self.config_sources = {
            "default": self.default_config,
            "system": {},  # 系统级配置
            "user": {},    # 用户级配置
            "env": {},     # 环境变量
            "runtime": {}  # 运行时配置（最高优先级）
        }
        
        # 创建ChainMap
        self.config = ChainMap(
            self.config_sources["runtime"],
            self.config_sources["env"],
            self.config_sources["user"],
            self.config_sources["system"],
            self.config_sources["default"]
        )
    
    def load_system_config(self, file_path):
        """
        加载系统级配置
        
        Args:
            file_path: 配置文件路径
        """
        if file_path.endswith('.json'):
            self.config_sources["system"] = load_json_config(file_path)
        elif file_path.endswith('.ini'):
            self.config_sources["system"] = load_ini_config(file_path)
        else:
            print(f"Unsupported config file format: {file_path}")
    
    def load_user_config(self, file_path):
        """
        加载用户级配置
        
        Args:
            file_path: 配置文件路径
        """
        if file_path.endswith('.json'):
            self.config_sources["user"] = load_json_config(file_path)
        elif file_path.endswith('.ini'):
            self.config_sources["user"] = load_ini_config(file_path)
        else:
            print(f"Unsupported config file format: {file_path}")
    
    def load_env_config(self, prefix="APP_"):
        """
        从环境变量加载配置
        
        Args:
            prefix: 环境变量前缀
        """
        self.config_sources["env"] = load_env_config(prefix)
    
    def set_runtime_config(self, runtime_config):
        """
        设置运行时配置
        
        Args:
            runtime_config: 运行时配置字典
        """
        self.config_sources["runtime"].update(runtime_config)
    
    def get(self, key, default=None):
        """
        获取配置项
        
        Args:
            key: 配置键，可以使用点表示法访问嵌套配置，如 "database.host"
            default: 默认值
        
        Returns:
            配置值
        """
        # 支持点表示法访问嵌套配置
        if '.' in key:
            parts = key.split('.')
            value = self.config
            try:
                for part in parts:
                    value = value[part]
                return value
            except (KeyError, TypeError):
                return default
        
        # 普通键访问
        return self.config.get(key, default)
    
    def set(self, key, value):
        """
        设置运行时配置项
        
        Args:
            key: 配置键，可以使用点表示法访问嵌套配置
            value: 配置值
        """
        # 支持点表示法设置嵌套配置
        if '.' in key:
            parts = key.split('.')
            config = self.config_sources["runtime"]
            
            # 遍历除最后一部分外的所有部分
            for part in parts[:-1]:
                if part not in config:
                    config[part] = {}
                config = config[part]
            
            # 设置最后一部分的值
            config[parts[-1]] = value
        else:
            # 普通键设置
            self.config_sources["runtime"][key] = value
    
    def get_config_source(self, source_name):
        """
        获取指定来源的配置
        
        Args:
            source_name: 配置来源名称 ("default", "system", "user", "env", "runtime")
        
        Returns:
            配置字典
        """
        if source_name in self.config_sources:
            return self.config_sources[source_name]
        raise ValueError(f"Unknown config source: {source_name}")
    
    def to_dict(self):
        """
        将配置转换为普通字典
        
        Returns:
            合并后的配置字典
        """
        # 这里我们需要深度合并，而不仅仅是浅拷贝
        import copy
        
        def deep_merge(dest, src):
            """
            深度合并两个字典
            """
            for key, value in src.items():
                if key in dest and isinstance(dest[key], dict) and isinstance(value, dict):
                    deep_merge(dest[key], value)
                else:
                    dest[key] = copy.deepcopy(value)
            return dest
        
        # 从低优先级到高优先级合并
        result = copy.deepcopy(self.config_sources["default"])
        deep_merge(result, self.config_sources["system"])
        deep_merge(result, self.config_sources["user"])
        deep_merge(result, self.config_sources["env"])
        deep_merge(result, self.config_sources["runtime"])
        
        return result
    
    def __str__(self):
        """
        返回配置的字符串表示
        """
        return str(self.to_dict())

# 演示多级配置管理系统
print("\n演示多级配置管理系统:")

# 创建配置管理器
config_manager = ConfigManager()

# 打印默认配置
print("\n默认配置:")
print(config_manager)

# 加载用户配置（模拟环境，实际使用时替换为真实文件路径）
# 这里我们直接设置字典来模拟加载
user_config = {
    "app_name": "CustomApp",
    "debug": True,
    "database": {
        "host": "db.example.com",
        "user": "customuser"
    }
}
config_manager.config_sources["user"] = user_config

# 加载环境变量配置（模拟环境）
env_config = {
    "log_level": "DEBUG",
    "timeout": 60,
    "database": {
        "password": "secretpassword",
        "port": 5433
    }
}
config_manager.config_sources["env"] = env_config

# 设置运行时配置
config_manager.set_runtime_config({
    "version": "1.0.1",
    "api": {
        "base_url": "https://api.example.com"
    }
})

# 打印合并后的配置
print("\n合并后的配置:")
print(config_manager)

# 使用get方法获取配置
print("\n使用get方法获取配置:")
print(f"app_name: {config_manager.get('app_name')}")
print(f"debug: {config_manager.get('debug')}")
print(f"log_level: {config_manager.get('log_level')}")
print(f"database.host: {config_manager.get('database.host')}")
print(f"database.port: {config_manager.get('database.port')}")
print(f"database.password: {config_manager.get('database.password')}")
print(f"api.base_url: {config_manager.get('api.base_url')}")
print(f"不存在的配置: {config_manager.get('nonexistent', 'default_value')}")

# 使用set方法设置运行时配置
print("\n使用set方法设置运行时配置:")
config_manager.set("timeout", 120)
config_manager.set("database.dbname", "production_db")
config_manager.set("new_setting", "new_value")

# 再次获取配置
print(f"更新后的timeout: {config_manager.get('timeout')}")
print(f"更新后的database.dbname: {config_manager.get('database.dbname')}")
print(f"新设置: {config_manager.get('new_setting')}")

# 查看不同来源的配置
print("\n不同来源的配置:")
print(f"默认配置中的database: {config_manager.get_config_source('default').get('database')}")
print(f"用户配置中的database: {config_manager.get_config_source('user').get('database')}")
print(f"环境变量中的database: {config_manager.get_config_source('env').get('database')}")

# 8. 总结

print("\n=== 8. 总结 ===")

print("\ncollections.ChainMap是Python标准库中提供的一种强大的数据结构，它允许多个字典组合成单一的映射视图。")

print("\n主要功能:")
print("1. 维护多个映射的视图，按顺序搜索键")
print("2. 支持所有标准字典操作")
print("3. 提供创建子上下文和获取父上下文的方法")
print("4. 对底层映射的修改会实时反映在ChainMap中")
print("5. 支持复杂的嵌套配置和作用域管理")

print("\n优势:")
print("1. 不需要创建新的合并字典，内存效率高")
print("2. 可以保持原始字典的分离，便于独立更新")
print("3. 提供优雅的方式处理多级配置和默认值")
print("4. 子上下文机制使临时修改配置变得简单")
print("5. 实现了完整的字典接口，使用方式与普通字典一致")

print("\n应用场景:")
print("1. 多级配置管理（命令行参数 > 环境变量 > 配置文件 > 默认配置）")
print("2. 作用域查找（局部变量 > 闭包变量 > 全局变量 > 内置变量）")
print("3. 上下文管理和临时配置修改")
print("4. 默认值处理和配置继承")
print("5. 多级缓存系统的实现")
print("6. 配置覆盖和合并的场景")

print("\n使用建议:")
print("1. 将频繁访问的映射放在ChainMap的前面以提高查找效率")
print("2. 限制映射数量，避免查找性能下降")
print("3. 注意修改操作只会影响第一个映射")
print("4. 对于需要序列化为JSON等格式的场景，记得先转换为字典")
print("5. 结合new_child()和parents属性，可以灵活管理嵌套上下文")

print("\n通过合理使用collections.ChainMap，可以在Python中优雅地处理各种需要多级配置和映射组合的场景，")
print("特别是在构建具有复杂配置需求的应用程序时，ChainMap提供了一种简洁而强大的解决方案。")
