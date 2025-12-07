# shelve模块详解

shelve模块是Python标准库中用于实现持久化存储的模块，它提供了一个类似字典的接口，用于将Python对象存储到磁盘文件中。shelve模块基于pickle模块实现，可以存储几乎所有的Python数据类型，包括自定义类的实例。

## 模块概述

shelve模块提供了以下主要功能：

- 提供类似字典的接口，用于持久化存储Python对象
- 支持键值对的存储和检索
- 支持事务处理（自动提交或手动提交）
- 支持并发访问（通过标志参数控制）
- 基于pickle模块，支持几乎所有的Python数据类型

## 基本用法

### 导入模块

```python
import shelve
import os
```

### 创建和打开shelf文件

```python
# 创建或打开一个shelf文件
print("创建和打开shelf文件:")

# 使用with语句打开shelf文件（推荐）
with shelve.open("mydata") as shelf:
    # 向shelf中添加数据
    shelf["name"] = "张三"
    shelf["age"] = 25
    shelf["scores"] = [85, 90, 88]
    shelf["is_student"] = True
    shelf["address"] = {"city": "北京", "district": "朝阳区"}
    
    print("数据已添加到shelf文件")
    print(f"shelf文件中的键: {list(shelf.keys())}")

# 不使用with语句打开shelf文件
print("\n不使用with语句打开shelf文件:")
shelf = shelve.open("mydata")
try:
    # 向shelf中添加数据
    shelf["phone"] = "13800138000"
    print(f"添加phone后的键: {list(shelf.keys())}")
finally:
    # 关闭shelf文件
    shelf.close()
```

### 读取shelf文件中的数据

```python
# 读取shelf文件中的数据
print("\n读取shelf文件中的数据:")

with shelve.open("mydata") as shelf:
    # 获取所有键
    keys = list(shelf.keys())
    print(f"shelf文件中的键: {keys}")
    
    # 读取数据
    for key in keys:
        value = shelf[key]
        print(f"{key}: {value}, 类型: {type(value)}")
    
    # 使用get方法读取数据
    name = shelf.get("name")
    print(f"\n使用get方法获取name: {name}")
    
    # 使用get方法读取不存在的键
    email = shelf.get("email", "未知")
    print(f"使用get方法获取不存在的email: {email}")
```

### 更新shelf文件中的数据

```python
# 更新shelf文件中的数据
print("\n更新shelf文件中的数据:")

with shelve.open("mydata") as shelf:
    # 更新现有键的值
    shelf["age"] = 26
    shelf["scores"] = [88, 92, 90]
    
    # 添加新键值对
    shelf["email"] = "zhangsan@example.com"
    shelf["courses"] = ("数学", "英语", "计算机")
    
    print("数据已更新")
    print(f"更新后的键: {list(shelf.keys())}")
    print(f"更新后的age: {shelf['age']}")
    print(f"更新后的scores: {shelf['scores']}")
    print(f"新增的email: {shelf['email']}")
    print(f"新增的courses: {shelf['courses']}")
```

### 删除shelf文件中的数据

```python
# 删除shelf文件中的数据
print("\n删除shelf文件中的数据:")

with shelve.open("mydata") as shelf:
    # 删除一个键值对
    del shelf["is_student"]
    
    # 使用pop方法删除并返回值
    phone = shelf.pop("phone")
    
    # 使用pop方法删除不存在的键
    address = shelf.pop("address", "未找到")
    
    print("数据已删除")
    print(f"删除后的键: {list(shelf.keys())}")
    print(f"使用pop方法删除的phone: {phone}")
    print(f"使用pop方法删除不存在的address: {address}")
    
    # 清空shelf文件
    shelf.clear()
    print(f"清空后的键: {list(shelf.keys())}")
```

## 高级功能

### 自动提交和手动提交

```python
# 自动提交和手动提交
print("\n自动提交和手动提交:")

# 默认情况下，shelf文件是自动提交的
with shelve.open("mydata") as shelf:
    shelf["key1"] = "value1"
    # 数据会自动保存到文件中

# 使用writeback=True参数打开shelf文件
with shelve.open("mydata", writeback=True) as shelf:
    # 添加数据
    shelf["list_data"] = [1, 2, 3]
    # 修改可变对象
    shelf["list_data"].append(4)
    # 修改会自动保存，因为writeback=True
    
    print(f"修改后的list_data: {shelf['list_data']}")

# 不使用writeback=True参数
with shelve.open("mydata") as shelf:
    # 添加数据
    shelf["dict_data"] = {"name": "张三", "age": 25}
    # 修改可变对象
    shelf["dict_data"]["age"] = 26
    # 修改不会自动保存，因为writeback=False
    
    # 重新获取数据，查看是否修改
    print(f"修改后的dict_data（未自动保存）: {shelf['dict_data']}")
    
    # 需要显式重新赋值才能保存修改
    shelf["dict_data"] = shelf["dict_data"]
    print(f"显式重新赋值后的dict_data: {shelf['dict_data']}")
```

### 自定义类的存储

```python
# 自定义类的存储
print("\n自定义类的存储:")

# 定义一个简单的类
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, address={self.address})"
    
    def greet(self):
        return f"Hello, my name is {self.name}."

# 创建Person对象
person = Person("李四", 30, "上海市浦东新区")
print(f"原始Person对象: {person}")
print(f"Person对象的方法调用: {person.greet()}")

# 将Person对象存储到shelf文件中
with shelve.open("mydata") as shelf:
    shelf["person"] = person
    print("Person对象已存储到shelf文件中")

# 从shelf文件中读取Person对象
with shelve.open("mydata") as shelf:
    loaded_person = shelf["person"]
    print(f"从shelf文件中读取的Person对象: {loaded_person}")
    print(f"读取的Person对象类型: {type(loaded_person)}")
    print(f"读取的Person对象的方法调用: {loaded_person.greet()}")
    
    # 验证对象是否相同
    print(f"原始对象和读取的对象是否相同: {person is loaded_person}")
    print(f"原始对象和读取的对象内容是否相等: {person.__dict__ == loaded_person.__dict__}")
```

### 并发访问控制

```python
# 并发访问控制
print("\n并发访问控制:")

# 打开shelf文件时的标志参数
# 'r' - 只读模式
# 'w' - 读写模式
# 'c' - 读写模式，如果文件不存在则创建（默认）
# 'n' - 读写模式，总是创建新文件

# 使用只读模式打开shelf文件
with shelve.open("mydata", flag='r') as shelf:
    print(f"只读模式下的键: {list(shelf.keys())}")
    # 尝试写入数据会抛出异常
    try:
        shelf["new_key"] = "new_value"
        print("写入成功（这行不应该执行）")
    except Exception as e:
        print(f"写入失败（预期行为）: {e}")

# 使用总是创建新文件的模式
with shelve.open("newdata", flag='n') as shelf:
    shelf["key"] = "value"
    print(f"新创建的shelf文件中的键: {list(shelf.keys())}")

# 删除新创建的文件
for ext in ['.db', '.dat', '.bak']:
    filename = "newdata" + ext
    if os.path.exists(filename):
        os.remove(filename)
```

### 使用sync参数

```python
# 使用sync参数
print("\n使用sync参数:")

# 使用sync=True参数打开shelf文件
with shelve.open("mydata", sync=True) as shelf:
    # 添加数据
    shelf["sync_key"] = "sync_value"
    print(f"使用sync=True添加的键: {shelf['sync_key']}")
    # 数据会立即写入到磁盘

# 使用sync=False参数打开shelf文件（默认）
with shelve.open("mydata", sync=False) as shelf:
    # 添加数据
    shelf["no_sync_key"] = "no_sync_value"
    print(f"使用sync=False添加的键: {shelf['no_sync_key']}")
    # 数据可能不会立即写入到磁盘，而是先缓存
```

## 实际应用示例

### 示例1：用户数据管理

```python
# 用户数据管理
print("\n用户数据管理:")

# 定义用户类
class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = "2023-10-01"
        self.is_active = True
    
    def __str__(self):
        return f"User(user_id={self.user_id}, username={self.username}, email={self.email})"
    
    def update_email(self, new_email):
        self.email = new_email
        return f"邮箱已更新为: {self.email}"

# 创建用户数据管理类
class UserManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.next_user_id = 1
    
    def add_user(self, username, email, password):
        """添加新用户"""
        with shelve.open(self.db_path, writeback=True) as shelf:
            # 获取下一个用户ID
            if "next_user_id" in shelf:
                self.next_user_id = shelf["next_user_id"]
            
            # 创建新用户
            user = User(self.next_user_id, username, email, password)
            
            # 保存用户
            shelf[f"user_{self.next_user_id}"] = user
            
            # 更新下一个用户ID
            self.next_user_id += 1
            shelf["next_user_id"] = self.next_user_id
            
            return user
    
    def get_user(self, user_id):
        """根据用户ID获取用户"""
        with shelve.open(self.db_path) as shelf:
            return shelf.get(f"user_{user_id}")
    
    def get_all_users(self):
        """获取所有用户"""
        users = []
        with shelve.open(self.db_path) as shelf:
            for key in shelf:
                if key.startswith("user_"):
                    users.append(shelf[key])
        return users
    
    def update_user(self, user_id, **kwargs):
        """更新用户信息"""
        with shelve.open(self.db_path, writeback=True) as shelf:
            user_key = f"user_{user_id}"
            if user_key in shelf:
                user = shelf[user_key]
                for key, value in kwargs.items():
                    if hasattr(user, key):
                        setattr(user, key, value)
                return True
            return False
    
    def delete_user(self, user_id):
        """删除用户"""
        with shelve.open(self.db_path) as shelf:
            user_key = f"user_{user_id}"
            if user_key in shelf:
                del shelf[user_key]
                return True
            return False

# 使用用户数据管理类
user_manager = UserManager("users_db")

# 添加新用户
user1 = user_manager.add_user("zhangsan", "zhangsan@example.com", "password123")
user2 = user_manager.add_user("lisi", "lisi@example.com", "password456")
user3 = user_manager.add_user("wangwu", "wangwu@example.com", "password789")

print(f"\n添加的用户:")
print(f"  用户1: {user1}")
print(f"  用户2: {user2}")
print(f"  用户3: {user3}")

# 获取用户
user = user_manager.get_user(1)
print(f"\n获取的用户1: {user}")

# 更新用户信息
user_manager.update_user(1, email="zhangsan_new@example.com", is_active=False)
updated_user = user_manager.get_user(1)
print(f"\n更新后的用户1: {updated_user}")

# 获取所有用户
all_users = user_manager.get_all_users()
print(f"\n所有用户: {len(all_users)}个")
for u in all_users:
    print(f"  - {u}")

# 删除用户
user_manager.delete_user(2)
all_users = user_manager.get_all_users()
print(f"\n删除用户2后剩余: {len(all_users)}个用户")
for u in all_users:
    print(f"  - {u}")
```

### 示例2：会话管理

```python
# 会话管理
print("\n会话管理:")

import time

# 定义会话类
class Session:
    def __init__(self, session_id, user_id, created_at=None, expires_at=None):
        self.session_id = session_id
        self.user_id = user_id
        self.created_at = created_at or time.time()
        self.expires_at = expires_at or (self.created_at + 3600)  # 默认1小时后过期
        self.data = {}
    
    def __str__(self):
        return f"Session(session_id={self.session_id}, user_id={self.user_id}, expires_at={time.ctime(self.expires_at)})")
    
    def is_expired(self):
        """检查会话是否过期"""
        return time.time() > self.expires_at
    
    def extend(self, seconds=3600):
        """延长会话过期时间"""
        self.expires_at = time.time() + seconds
        return self.expires_at

# 定义会话管理类
class SessionManager:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def create_session(self, user_id):
        """创建新会话"""
        # 生成会话ID（简化示例）
        session_id = f"session_{user_id}_{int(time.time())}"
        session = Session(session_id, user_id)
        
        with shelve.open(self.db_path, writeback=True) as shelf:
            shelf[session_id] = session
            
            # 添加到用户会话列表
            user_sessions_key = f"user_sessions_{user_id}"
            user_sessions = shelf.get(user_sessions_key, [])
            user_sessions.append(session_id)
            shelf[user_sessions_key] = user_sessions
        
        return session
    
    def get_session(self, session_id):
        """根据会话ID获取会话"""
        with shelve.open(self.db_path) as shelf:
            session = shelf.get(session_id)
            if session and not session.is_expired():
                return session
            return None
    
    def update_session(self, session_id, **kwargs):
        """更新会话数据"""
        with shelve.open(self.db_path, writeback=True) as shelf:
            if session_id in shelf:
                session = shelf[session_id]
                if not session.is_expired():
                    for key, value in kwargs.items():
                        if key in session.data:
                            session.data[key] = value
                        else:
                            session.data[key] = value
                    return True
            return False
    
    def delete_session(self, session_id):
        """删除会话"""
        with shelve.open(self.db_path, writeback=True) as shelf:
            if session_id in shelf:
                session = shelf[session_id]
                
                # 从用户会话列表中删除
                user_sessions_key = f"user_sessions_{session.user_id}"
                if user_sessions_key in shelf:
                    user_sessions = shelf[user_sessions_key]
                    if session_id in user_sessions:
                        user_sessions.remove(session_id)
                        shelf[user_sessions_key] = user_sessions
                
                # 删除会话
                del shelf[session_id]
                return True
            return False
    
    def delete_expired_sessions(self):
        """删除所有过期会话"""
        deleted_count = 0
        with shelve.open(self.db_path, writeback=True) as shelf:
            keys_to_delete = []
            
            # 找出所有过期会话
            for key in shelf:
                if key.startswith("session_"):
                    session = shelf[key]
                    if session.is_expired():
                        keys_to_delete.append(key)
            
            # 删除过期会话
            for session_id in keys_to_delete:
                session = shelf[session_id]
                
                # 从用户会话列表中删除
                user_sessions_key = f"user_sessions_{session.user_id}"
                if user_sessions_key in shelf:
                    user_sessions = shelf[user_sessions_key]
                    if session_id in user_sessions:
                        user_sessions.remove(session_id)
                        shelf[user_sessions_key] = user_sessions
                
                # 删除会话
                del shelf[session_id]
                deleted_count += 1
        
        return deleted_count

# 使用会话管理类
session_manager = SessionManager("sessions_db")

# 创建会话
session1 = session_manager.create_session(1)
session2 = session_manager.create_session(1)
session3 = session_manager.create_session(2)

print(f"\n创建的会话:")
print(f"  会话1: {session1}")
print(f"  会话2: {session2}")
print(f"  会话3: {session3}")

# 获取会话
retrieved_session = session_manager.get_session(session1.session_id)
print(f"\n获取的会话1: {retrieved_session}")

# 更新会话数据
session_manager.update_session(session1.session_id, username="zhangsan", language="zh-CN")
updated_session = session_manager.get_session(session1.session_id)
print(f"\n更新后的会话1数据: {updated_session.data}")

# 删除会话
session_manager.delete_session(session2.session_id)
print(f"\n删除会话2后，获取会话2: {session_manager.get_session(session2.session_id)}")

# 模拟过期会话（修改过期时间为过去的时间）
with shelve.open("sessions_db", writeback=True) as shelf:
    if session3.session_id in shelf:
        session3 = shelf[session3.session_id]
        session3.expires_at = time.time() - 100  # 100秒前过期

# 检查过期会话
print(f"\n检查过期会话3: {session_manager.get_session(session3.session_id)}")

# 删除所有过期会话
deleted_count = session_manager.delete_expired_sessions()
print(f"删除的过期会话数量: {deleted_count}")
```

### 示例3：配置管理

```python
# 配置管理
print("\n配置管理:")

# 定义配置管理类
class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        # 默认配置
        self.default_config = {
            "app_name": "MyApp",
            "version": "1.0.0",
            "debug": False,
            "server": {
                "host": "localhost",
                "port": 8080
            },
            "database": {
                "host": "localhost",
                "port": 3306
            }
        }
    
    def load_config(self):
        """加载配置"""
        try:
            with shelve.open(self.config_file) as shelf:
                return dict(shelf)
        except Exception as e:
            print(f"加载配置失败，使用默认配置: {e}")
            return self.default_config
    
    def save_config(self, config):
        """保存配置"""
        with shelve.open(self.config_file, flag='n') as shelf:  # 总是创建新文件
            for key, value in config.items():
                shelf[key] = value
        return True
    
    def get_config_value(self, key, default=None):
        """获取配置值"""
        config = self.load_config()
        keys = key.split(".")
        value = config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set_config_value(self, key, value):
        """设置配置值"""
        config = self.load_config()
        keys = key.split(".")
        last_key = keys[-1]
        parent = config
        
        # 找到父级配置
        for k in keys[:-1]:
            if k not in parent:
                parent[k] = {}
            parent = parent[k]
        
        # 设置值
        parent[last_key] = value
        
        # 保存配置
        return self.save_config(config)

# 使用配置管理类
config_manager = ConfigManager("config_db")

# 加载配置
config = config_manager.load_config()
print(f"加载的配置: {config}")

# 获取配置值
app_name = config_manager.get_config_value("app_name")
server_port = config_manager.get_config_value("server.port")
non_existent = config_manager.get_config_value("non.existent.key", "默认值")

print(f"\n获取的配置值:")
print(f"  app_name: {app_name}")
print(f"  server.port: {server_port}")
print(f"  non.existent.key: {non_existent}")

# 设置配置值
config_manager.set_config_value("app_name", "NewApp")
config_manager.set_config_value("debug", True)
config_manager.set_config_value("server.port", 9090)
config_manager.set_config_value("database.username", "root")

# 重新加载配置
new_config = config_manager.load_config()
print(f"\n重新加载的配置: {new_config}")
```

## 最佳实践

1. **使用with语句**：始终使用with语句打开shelf文件，确保文件正确关闭
2. **处理异常**：在进行shelf操作时，捕获并处理可能的异常（如`IOError`、`ValueError`等）
3. **选择合适的键**：使用有意义的键名，避免与内部使用的键名冲突
4. **使用writeback参数**：当需要修改可变对象时，使用writeback=True参数
5. **考虑并发访问**：根据需要选择合适的标志参数，控制并发访问
6. **定期备份**：定期备份重要的shelf文件，以防止数据丢失
7. **注意安全**：与pickle模块一样，不要从不可信的来源加载shelf文件
8. **性能考虑**：对于大型数据集，考虑使用更高效的存储方式
9. **关闭文件**：确保在完成操作后关闭shelf文件，释放资源
10. **文档化**：记录shelf文件的结构和内容，以便于后续维护

## 与其他模块的关系

- **pickle**：shelve模块基于pickle模块实现，使用pickle模块进行对象的序列化和反序列化
- **dbm**：shelve模块使用dbm模块（或其变种）作为底层存储，创建的文件通常有.db、.dat或.bak扩展名
- **json**：json模块用于处理JSON数据，与shelve模块类似，但JSON是文本格式，更安全、更通用，但只支持基本数据类型
- **sqlite3**：sqlite3模块用于操作SQLite数据库，提供了更强大的数据存储和查询功能，但使用起来比shelve模块复杂
- **msgpack**：msgpack是一个第三方库，用于高效的二进制序列化，比pickle更快、更小

## 清理测试文件

```python
# 清理所有测试文件
print("\n清理所有测试文件:")

# 删除shelf文件
for base_name in ["mydata", "users_db", "sessions_db", "config_db"]:
    for ext in ['.db', '.dat', '.bak']:
        filename = base_name + ext
        if os.path.exists(filename):
            os.remove(filename)
            print(f"已删除: {filename}")
```

## 总结

shelve模块是Python标准库中用于实现持久化存储的强大工具，它提供了类似字典的接口，用于将Python对象存储到磁盘文件中。shelve模块基于pickle模块实现，可以存储几乎所有的Python数据类型，包括自定义类的实例。

shelve模块在实际应用中常用于用户数据管理、会话管理、配置管理等场景。它使用简单，功能强大，是Python中实现持久化存储的常用工具之一。

然而，shelve模块也存在一些局限性，如不支持复杂的查询操作，不适合存储大量数据等。对于需要更强大数据存储和查询功能的应用，可以考虑使用数据库系统，如SQLite、MySQL等。