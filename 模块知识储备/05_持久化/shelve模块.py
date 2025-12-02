"""
# shelve模块详解：Python对象的持久化字典存储

shelve模块是Python的标准库，它提供了一个简单的持久化方案，允许你将Python对象存储到文件中，并在需要时检索它们。shelve本质上是一个持久化的类字典对象，它内部使用pickle来序列化和反序列化对象，同时提供了一个类似字典的接口来访问这些对象。

## 1. 核心功能概览

shelve模块的主要功能包括：

1. **持久化存储**：将Python对象存储到磁盘文件中
2. **字典式接口**：提供类似字典的get/set/delete操作
3. **自动序列化/反序列化**：内部使用pickle处理对象的序列化
4. **键值对存储**：以键值对形式组织数据
5. **事务支持**：支持简单的事务操作

## 2. 基本使用

### 2.1 打开和关闭shelf

```python
import shelve
import os

def basic_shelf_operations():
    # 文件名
    shelf_file = 'test_shelf.db'
    
    print(f"=== 基本的shelf操作演示 ===")
    
    # 打开shelf（默认以读写模式打开）
    print(f"\n1. 打开shelf文件: {shelf_file}")
    with shelve.open(shelf_file) as shelf:
        # 显示初始状态
        print(f"   初始项目数: {len(shelf)}")
        print(f"   初始键列表: {list(shelf.keys())}")
        
        # 添加项目（字典式赋值）
        print("\n2. 添加项目...")
        shelf['string'] = "Hello, shelve!"
        shelf['integer'] = 42
        shelf['float'] = 3.14159
        shelf['list'] = [1, 2, 3, 4, 5]
        shelf['dict'] = {'name': '张三', 'age': 30}
        
        # 查看更新后的状态
        print(f"   更新后项目数: {len(shelf)}")
        print(f"   更新后键列表: {list(shelf.keys())}")
        
        # 访问项目（字典式访问）
        print("\n3. 访问项目:")
        print(f"   string: {shelf['string']}")
        print(f"   integer: {shelf['integer']}")
        print(f"   dict: {shelf['dict']}")
        
        # 检查键是否存在
        print("\n4. 检查键存在性:")
        print(f"   'string' 存在: {'string' in shelf}")
        print(f"   'nonexistent' 存在: {'nonexistent' in shelf}")
        
        # 使用get方法安全访问
        print("\n5. 使用get方法:")
        print(f"   'string' 值: {shelf.get('string')}")
        print(f"   'nonexistent' 默认值: {shelf.get('nonexistent', '默认值')}")
        
        # 删除项目
        print("\n6. 删除项目:")
        del shelf['integer']
        print(f"   删除 'integer' 后，键列表: {list(shelf.keys())}")
    
    # 注意：with语句结束后，shelf会自动关闭
    print(f"\n7. shelf已自动关闭")
    
    # 重新打开查看持久化效果
    print(f"\n8. 重新打开shelf验证持久化:")
    with shelve.open(shelf_file) as shelf:
        print(f"   项目数: {len(shelf)}")
        print(f"   键列表: {list(shelf.keys())}")
        print(f"   'string' 值: {shelf['string']}")
        print(f"   'integer' 已被删除: {'integer' not in shelf}")
    
    # 清理测试文件
    print(f"\n9. 清理测试文件")
    # 在不同平台上，shelve可能创建多个文件
    for ext in ['db', 'bak', 'dat', 'dir']:
        file_path = f"{shelf_file}.{ext}"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"   删除: {file_path}")

# 运行示例
basic_shelf_operations()
```

### 2.2 写入回显控制

shelve模块提供了`writeback`参数来控制对象的写入行为：

```python
import shelve
import os

def writeback_demo():
    shelf_file = 'writeback_test.db'
    
    print(f"=== writeback参数演示 ===")
    
    # 演示不使用writeback
    print("\n1. 不使用writeback:")
    with shelve.open(shelf_file) as shelf:
        # 添加一个可变对象（列表）
        shelf['list'] = [1, 2, 3]
        print(f"   初始列表: {shelf['list']}")
        
        # 修改列表（这种修改不会自动保存！）
        list_obj = shelf['list']
        list_obj.append(4)
        print(f"   修改后的内存中列表: {list_obj}")
        print(f"   shelf中的列表(未更新): {shelf['list']}")  # 还是[1, 2, 3]
        
        # 要保存修改，必须显式重新赋值
        shelf['list'] = list_obj
        print(f"   重新赋值后shelf中的列表: {shelf['list']}")  # 现在是[1, 2, 3, 4]
    
    # 演示使用writeback
    print("\n2. 使用writeback=True:")
    with shelve.open(shelf_file, writeback=True) as shelf:
        print(f"   打开时的列表: {shelf['list']}")
        
        # 使用writeback=True时，修改可变对象会自动跟踪
        list_obj = shelf['list']
        list_obj.append(5)
        print(f"   修改后的内存中列表: {list_obj}")
        # 不需要显式重新赋值，但需要等待sync()或close()
        print(f"   修改后立即读取: {shelf['list']}")  # writeback=True会缓存对象
        
        # 显式同步（可选）
        print("   执行sync()")
        shelf.sync()
        print(f"   sync后的值: {shelf['list']}")
    
    # 验证持久化
    print("\n3. 验证持久化:")
    with shelve.open(shelf_file) as shelf:
        print(f"   最终保存的列表: {shelf['list']}")  # 应该是[1, 2, 3, 4, 5]
    
    # 清理
    for ext in ['db', 'bak', 'dat', 'dir']:
        file_path = f"{shelf_file}.{ext}"
        if os.path.exists(file_path):
            os.remove(file_path)

# 运行示例
writeback_demo()
```

## 3. 高级使用

### 3.1 自定义对象的存储

shelve可以存储自定义类的实例，就像pickle一样：

```python
import shelve
import os
import time

def custom_objects_shelve():
    shelf_file = 'custom_objects.db'
    
    # 定义自定义类
    class Person:
        def __init__(self, name, age, email):
            self.name = name
            self.age = age
            self.email = email
            self.creation_time = time.time()
        
        def birthday(self):
            """庆祝生日，年龄加1"""
            self.age += 1
            print(f"{self.name} 生日快乐! 现在 {self.age} 岁了。")
        
        def __repr__(self):
            return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"
    
    # 定义另一个类
    class AddressBook:
        def __init__(self):
            self.entries = {}
        
        def add_person(self, person_id, person):
            self.entries[person_id] = person
            print(f"添加联系人: {person_id} -> {person.name}")
        
        def get_person(self, person_id):
            return self.entries.get(person_id)
        
        def list_people(self):
            return list(self.entries.items())
        
        def __repr__(self):
            return f"AddressBook({len(self.entries)}个联系人)"
    
    print(f"=== 自定义对象存储演示 ===")
    
    # 创建并存储对象
    print("\n1. 创建并存储对象:")
    with shelve.open(shelf_file, writeback=True) as shelf:
        # 创建Person实例
        alice = Person("Alice", 30, "alice@example.com")
        bob = Person("Bob", 25, "bob@example.com")
        
        # 直接存储Person实例
        shelf['alice'] = alice
        shelf['bob'] = bob
        print(f"   存储了两个Person实例")
        
        # 创建并存储AddressBook
        address_book = AddressBook()
        address_book.add_person(1, alice)
        address_book.add_person(2, bob)
        
        shelf['address_book'] = address_book
        print(f"   存储了AddressBook: {address_book}")
    
    # 重新加载并使用对象
    print("\n2. 重新加载并使用对象:")
    with shelve.open(shelf_file, writeback=True) as shelf:
        # 加载Person实例
        loaded_alice = shelf['alice']
        loaded_bob = shelf['bob']
        
        print(f"   加载的Alice: {loaded_alice}")
        print(f"   加载的Bob: {loaded_bob}")
        
        # 使用对象方法
        loaded_alice.birthday()
        
        # 加载AddressBook
        loaded_address_book = shelf['address_book']
        print(f"   加载的通讯录: {loaded_address_book}")
        
        # 使用AddressBook方法
        print("   通讯录中的联系人:")
        for person_id, person in loaded_address_book.list_people():
            print(f"     {person_id}: {person}")
        
        # 添加新联系人
        charlie = Person("Charlie", 35, "charlie@example.com")
        loaded_address_book.add_person(3, charlie)
        shelf['charlie'] = charlie  # 也单独存储
    
    # 最终验证
    print("\n3. 最终验证:")
    with shelve.open(shelf_file) as shelf:
        print(f"   shelf中的键: {list(shelf.keys())}")
        print(f"   Alice的最新信息: {shelf['alice']}")
        print(f"   通讯录联系人数量: {len(shelf['address_book'].entries)}")
    
    # 清理
    for ext in ['db', 'bak', 'dat', 'dir']:
        file_path = f"{shelf_file}.{ext}"
        if os.path.exists(file_path):
            os.remove(file_path)

# 运行示例
custom_objects_shelve()
```

### 3.2 事务和并发

shelve模块对事务的支持有限，但可以通过一些技术实现简单的事务功能：

```python
import shelve
import os
import time

def transaction_demo():
    shelf_file = 'transaction_test.db'
    
    print(f"=== 简单事务演示 ===")
    
    # 初始化shelf
    with shelve.open(shelf_file) as shelf:
        shelf['balance'] = 1000
        shelf['transactions'] = []
        print(f"初始化账户，余额: {shelf['balance']}")
    
    # 定义事务函数
    def transfer_money(from_account, to_account, amount):
        """模拟转账事务"""
        try:
            with shelve.open(shelf_file, writeback=True) as shelf:
                # 检查余额
                if shelf['balance'] < amount:
                    raise ValueError("余额不足")
                
                # 记录事务前状态
                before_balance = shelf['balance']
                
                # 执行转账
                shelf['balance'] -= amount
                shelf['transactions'].append({
                    'type': 'transfer',
                    'from': from_account,
                    'to': to_account,
                    'amount': amount,
                    'timestamp': time.time(),
                    'success': True
                })
                
                # 模拟一些处理时间
                time.sleep(0.1)
                
                # 验证事务
                assert shelf['balance'] == before_balance - amount
                
                print(f"转账成功: {amount} 从 {from_account} 到 {to_account}")
                print(f"新余额: {shelf['balance']}")
                return True
                
        except Exception as e:
            print(f"转账失败: {e}")
            # 由于使用了with语句，shelf会自动关闭，未提交的更改不会保存
            return False
    
    # 定义存款函数
    def deposit(amount):
        """模拟存款事务"""
        try:
            with shelve.open(shelf_file, writeback=True) as shelf:
                shelf['balance'] += amount
                shelf['transactions'].append({
                    'type': 'deposit',
                    'amount': amount,
                    'timestamp': time.time(),
                    'success': True
                })
                print(f"存款成功: {amount}")
                print(f"新余额: {shelf['balance']}")
                return True
        except Exception as e:
            print(f"存款失败: {e}")
            return False
    
    # 执行事务
    print("\n执行事务:")
    
    # 成功的转账
    transfer_money("账户A", "账户B", 200)
    
    # 存款
    deposit(500)
    
    # 失败的转账（余额不足）
    transfer_money("账户A", "账户C", 2000)  # 这应该会失败
    
    # 验证最终状态
    print("\n验证最终状态:")
    with shelve.open(shelf_file) as shelf:
        print(f"最终余额: {shelf['balance']}")
        print(f"交易记录数量: {len(shelf['transactions'])}")
        print("交易记录:")
        for i, tx in enumerate(shelf['transactions'], 1):
            print(f"  {i}. {tx['type']} - {tx['amount']} ({'成功' if tx['success'] else '失败'})")
    
    # 清理
    for ext in ['db', 'bak', 'dat', 'dir']:
        file_path = f"{shelf_file}.{ext}"
        if os.path.exists(file_path):
            os.remove(file_path)

# 运行示例
transaction_demo()
```

## 4. 高级应用示例

### 4.1 简单的对象数据库

```python
import shelve
import os
import uuid
import time
from pathlib import Path

def simple_object_database():
    """简单的对象数据库实现"""
    
    class SimpleDB:
        def __init__(self, db_path="simple_db"):
            """初始化数据库"""
            self.db_path = Path(db_path)
            self.db_path.mkdir(exist_ok=True)
            self.current_table = None
            self.shelf = None
        
        def open_table(self, table_name):
            """打开指定表"""
            if self.shelf is not None:
                self.shelf.close()
            
            table_path = self.db_path / table_name
            self.shelf = shelve.open(str(table_path), writeback=True)
            self.current_table = table_name
            print(f"打开表: {table_name}")
            return self
        
        def close(self):
            """关闭数据库"""
            if self.shelf is not None:
                self.shelf.close()
                self.shelf = None
                self.current_table = None
                print("数据库已关闭")
        
        def __enter__(self):
            """上下文管理器支持"""
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            """退出上下文时关闭"""
            self.close()
        
        def insert(self, data, key=None):
            """插入记录"""
            if self.shelf is None:
                raise RuntimeError("没有打开的表")
            
            # 如果没有提供键，生成一个UUID
            if key is None:
                key = str(uuid.uuid4())
            
            # 添加元数据
            record = {
                'data': data,
                'created_at': time.time(),
                'updated_at': time.time(),
                'id': key
            }
            
            self.shelf[key] = record
            print(f"插入记录: {key}")
            return key
        
        def get(self, key):
            """获取记录"""
            if self.shelf is None:
                raise RuntimeError("没有打开的表")
            
            record = self.shelf.get(key)
            return record['data'] if record else None
        
        def update(self, key, data):
            """更新记录"""
            if self.shelf is None:
                raise RuntimeError("没有打开的表")
            
            if key not in self.shelf:
                return False
            
            record = self.shelf[key]
            record['data'] = data
            record['updated_at'] = time.time()
            self.shelf[key] = record
            print(f"更新记录: {key}")
            return True
        
        def delete(self, key):
            """删除记录"""
            if self.shelf is None:
                raise RuntimeError("没有打开的表")
            
            if key in self.shelf:
                del self.shelf[key]
                print(f"删除记录: {key}")
                return True
            return False
        
        def find_all(self):
            """查找所有记录"""
            if self.shelf is None:
                raise RuntimeError("没有打开的表")
            
            results = []
            for key, record in self.shelf.items():
                results.append((key, record['data']))
            return results
        
        def find_by(self, predicate):
            """根据条件查找记录"""
            if self.shelf is None:
                raise RuntimeError("没有打开的表")
            
            results = []
            for key, record in self.shelf.items():
                if predicate(record['data']):
                    results.append((key, record['data']))
            return results
        
        def count(self):
            """获取记录数量"""
            if self.shelf is None:
                raise RuntimeError("没有打开的表")
            
            return len(self.shelf)
        
        def clear(self):
            """清空表"""
            if self.shelf is None:
                raise RuntimeError("没有打开的表")
            
            for key in list(self.shelf.keys()):
                del self.shelf[key]
            print("表已清空")
    
    # 测试简单对象数据库
    print("=== 简单对象数据库测试 ===")
    
    # 使用上下文管理器
    with SimpleDB() as db:
        # 打开表
        db.open_table("users")
        
        # 插入记录
        print("\n1. 插入用户记录:")
        user1_id = db.insert({"name": "张三", "age": 30, "email": "zhangsan@example.com"})
        user2_id = db.insert({"name": "李四", "age": 25, "email": "lisi@example.com"})
        user3_id = db.insert({"name": "王五", "age": 35, "email": "wangwu@example.com"})
        
        # 获取记录
        print("\n2. 获取记录:")
        user1 = db.get(user1_id)
        print(f"   用户1: {user1}")
        
        # 更新记录
        print("\n3. 更新记录:")
        db.update(user1_id, {"name": "张三", "age": 31, "email": "zhangsan_new@example.com"})
        updated_user1 = db.get(user1_id)
        print(f"   更新后用户1: {updated_user1}")
        
        # 条件查询
        print("\n4. 条件查询:")
        young_users = db.find_by(lambda user: user['age'] < 32)
        print(f"   32岁以下的用户 ({len(young_users)}个):")
        for uid, user in young_users:
            print(f"     {uid}: {user['name']} - {user['age']}岁")
        
        # 查询所有记录
        print("\n5. 查询所有记录:")
        all_users = db.find_all()
        print(f"   总用户数: {len(all_users)}")
        for uid, user in all_users:
            print(f"     {uid}: {user['name']}")
        
        # 删除记录
        print("\n6. 删除记录:")
        db.delete(user2_id)
        
        # 再次查询所有记录
        print("\n7. 删除后再次查询:")
        all_users = db.find_all()
        print(f"   删除后总用户数: {len(all_users)}")
    
    # 测试表的持久化
    print("\n8. 测试表的持久化:")
    with SimpleDB() as db:
        db.open_table("users")
        print(f"   持久化后的用户数: {db.count()}")
        
        # 清理
        print("\n9. 清理测试数据")
        db.close()
        
        # 删除数据库文件
        import shutil
        db_dir = Path("simple_db")
        if db_dir.exists():
            shutil.rmtree(db_dir)
            print(f"   删除数据库目录: {db_dir}")

# 运行示例
simple_object_database()
```

### 4.2 缓存系统实现

```python
import shelve
import os
import time
from pathlib import Path

def shelf_cache_system():
    """基于shelve的缓存系统"""
    
    class ShelfCache:
        def __init__(self, cache_dir="cache", default_ttl=3600):
            """初始化缓存系统"""
            self.cache_dir = Path(cache_dir)
            self.cache_dir.mkdir(exist_ok=True)
            self.default_ttl = default_ttl  # 默认过期时间（秒）
            self.cache_file = str(self.cache_dir / "cache")
            self.shelf = None
        
        def _open(self, writeback=True):
            """打开shelf"""
            if self.shelf is None:
                self.shelf = shelve.open(self.cache_file, writeback=writeback)
            return self.shelf
        
        def close(self):
            """关闭缓存"""
            if self.shelf is not None:
                self.shelf.close()
                self.shelf = None
        
        def __enter__(self):
            """支持上下文管理器"""
            self._open()
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            """退出上下文时关闭"""
            self.close()
        
        def set(self, key, value, ttl=None):
            """设置缓存项"""
            shelf = self._open()
            
            # 如果没有指定TTL，使用默认值
            if ttl is None:
                ttl = self.default_ttl
            
            # 创建缓存项
            cache_item = {
                'value': value,
                'expires_at': time.time() + ttl
            }
            
            shelf[key] = cache_item
            return True
        
        def get(self, key, default=None):
            """获取缓存项"""
            shelf = self._open(writeback=False)
            
            # 检查键是否存在
            if key not in shelf:
                return default
            
            # 获取缓存项
            cache_item = shelf[key]
            
            # 检查是否过期
            if time.time() > cache_item['expires_at']:
                # 删除过期项
                self._open().pop(key, None)  # 确保以写模式打开
                return default
            
            return cache_item['value']
        
        def delete(self, key):
            """删除缓存项"""
            shelf = self._open()
            if key in shelf:
                del shelf[key]
                return True
            return False
        
        def clear(self):
            """清空所有缓存"""
            shelf = self._open()
            shelf.clear()
            return True
        
        def clear_expired(self):
            """清理过期的缓存项"""
            shelf = self._open()
            expired_keys = []
            
            # 找出所有过期的键
            for key, item in shelf.items():
                if time.time() > item['expires_at']:
                    expired_keys.append(key)
            
            # 删除过期项
            for key in expired_keys:
                del shelf[key]
            
            return expired_keys
        
        def exists(self, key):
            """检查键是否存在且未过期"""
            return self.get(key) is not None
        
        def size(self):
            """获取缓存项数量"""
            shelf = self._open(writeback=False)
            return len(shelf)
    
    # 测试缓存系统
    print("=== ShelfCache缓存系统测试 ===")
    
    # 使用上下文管理器
    with ShelfCache(default_ttl=5) as cache:  # 默认TTL为5秒
        print("1. 设置缓存项:")
        cache.set("key1", "普通缓存值")
        cache.set("key2", {"复杂": "对象"}, ttl=2)  # 2秒后过期
        cache.set("key3", [1, 2, 3, 4, 5], ttl=10)  # 10秒后过期
        
        print(f"   当前缓存大小: {cache.size()}")
        
        print("\n2. 获取缓存项:")
        print(f"   key1: {cache.get('key1')}")
        print(f"   key2: {cache.get('key2')}")
        print(f"   key3: {cache.get('key3')}")
        print(f"   不存在的键: {cache.get('nonexistent', '默认值')}")
        
        print("\n3. 检查键存在性:")
        print(f"   key1 存在: {cache.exists('key1')}")
        print(f"   nonexistent 存在: {cache.exists('nonexistent')}")
        
        print("\n4. 等待key2过期 (2秒)...")
        time.sleep(2)
        
        print("\n5. 检查过期项:")
        print(f"   key2 (已过期): {cache.get('key2', '已过期')}")
        print(f"   key3 (未过期): {cache.get('key3')}")
        
        print("\n6. 清理过期项:")
        expired = cache.clear_expired()
        print(f"   清理了 {len(expired)} 个过期项: {expired}")
        print(f"   当前缓存大小: {cache.size()}")
        
        print("\n7. 删除缓存项:")
        cache.delete("key1")
        print(f"   删除key1后，缓存大小: {cache.size()}")
        print(f"   key1现在: {cache.get('key1', '已删除')}")
        
        print("\n8. 测试持久化:")
        # 关闭并重新打开以测试持久化
    
    # 重新打开缓存验证持久化
    print("\n9. 重新打开缓存验证持久化:")
    with ShelfCache() as cache:
        print(f"   持久化后的缓存大小: {cache.size()}")
        print(f"   key3 (应该还在): {cache.get('key3')}")
        
        # 清理
        print("\n10. 清理缓存:")
        cache.clear()
        print(f"   清空后缓存大小: {cache.size()}")
    
    # 删除缓存文件
    cache_dir = Path("cache")
    if cache_dir.exists():
        import shutil
        shutil.rmtree(cache_dir)
        print(f"\n11. 删除缓存目录: {cache_dir}")

# 运行示例
shelf_cache_system()
```

### 4.3 配置管理系统

```python
import shelve
import os
import json
from pathlib import Path

def configuration_manager():
    """基于shelve的配置管理系统"""
    
    class ConfigManager:
        def __init__(self, config_file="config"):
            """初始化配置管理器"""
            self.config_file = config_file
            self.shelf = None
            self._open()
        
        def _open(self):
            """打开配置文件"""
            if self.shelf is None:
                self.shelf = shelve.open(self.config_file, writeback=True)
        
        def close(self):
            """关闭配置文件"""
            if self.shelf is not None:
                self.shelf.close()
                self.shelf = None
        
        def __enter__(self):
            """支持上下文管理器"""
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            """退出上下文时关闭"""
            self.close()
        
        def set(self, key, value, section="default"):
            """设置配置项"""
            # 确保section存在
            if section not in self.shelf:
                self.shelf[section] = {}
            
            # 设置值
            self.shelf[section][key] = value
            print(f"设置配置: {section}.{key} = {value}")
            return True
        
        def get(self, key, default=None, section="default"):
            """获取配置项"""
            # 检查section是否存在
            if section not in self.shelf:
                return default
            
            # 返回值或默认值
            return self.shelf[section].get(key, default)
        
        def get_section(self, section="default"):
            """获取整个配置节"""
            return self.shelf.get(section, {})
        
        def delete(self, key, section="default"):
            """删除配置项"""
            if section in self.shelf and key in self.shelf[section]:
                del self.shelf[section][key]
                print(f"删除配置: {section}.{key}")
                
                # 如果section为空，可以选择删除它
                if not self.shelf[section]:
                    del self.shelf[section]
                    print(f"删除空配置节: {section}")
                
                return True
            return False
        
        def delete_section(self, section):
            """删除整个配置节"""
            if section in self.shelf:
                del self.shelf[section]
                print(f"删除配置节: {section}")
                return True
            return False
        
        def list_sections(self):
            """列出所有配置节"""
            return list(self.shelf.keys())
        
        def list_keys(self, section="default"):
            """列出指定配置节的所有键"""
            if section in self.shelf:
                return list(self.shelf[section].keys())
            return []
        
        def export_to_json(self, filename="config_export.json"):
            """导出配置到JSON文件"""
            # 构建完整配置字典
            config_data = {}
            for section, values in self.shelf.items():
                config_data[section] = values.copy()
            
            # 写入JSON文件
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, ensure_ascii=False, indent=2)
            
            print(f"配置已导出到: {filename}")
            return True
        
        def import_from_json(self, filename="config_export.json"):
            """从JSON文件导入配置"""
            try:
                # 读取JSON文件
                with open(filename, 'r', encoding='utf-8') as f:
                    config_data = json.load(f)
                
                # 导入配置
                for section, values in config_data.items():
                    self.shelf[section] = values.copy()
                
                print(f"配置已从: {filename} 导入")
                return True
                
            except Exception as e:
                print(f"导入配置失败: {e}")
                return False
        
        def clear(self):
            """清空所有配置"""
            self.shelf.clear()
            print("所有配置已清空")
            return True
    
    # 测试配置管理系统
    print("=== 配置管理系统测试 ===")
    
    # 使用上下文管理器
    with ConfigManager("app_config") as config:
        # 设置配置
        print("1. 设置基本配置:")
        config.set("app_name", "MyApp")
        config.set("version", "1.0.0")
        config.set("debug", True)
        
        # 设置不同部分的配置
        print("\n2. 设置多部分配置:")
        # 数据库配置
        config.set("host", "localhost", section="database")
        config.set("port", 5432, section="database")
        config.set("username", "admin", section="database")
        
        # UI配置
        config.set("theme", "dark", section="ui")
        config.set("font_size", 14, section="ui")
        config.set("notifications", True, section="ui")
        
        # 获取配置
        print("\n3. 获取配置:")
        print(f"   应用名称: {config.get('app_name')}")
        print(f"   数据库主机: {config.get('host', section='database')}")
        print(f"   UI主题: {config.get('theme', section='ui')}")
        print(f"   不存在的配置: {config.get('nonexistent', '默认值')}")
        
        # 列出配置信息
        print("\n4. 列出配置信息:")
        print(f"   配置节列表: {config.list_sections()}")
        print(f"   默认配置键: {config.list_keys()}")
        print(f"   UI配置键: {config.list_keys(section='ui')}")
        
        # 获取整个配置节
        print("\n5. 获取整个配置节:")
        db_config = config.get_section("database")
        print(f"   数据库配置: {db_config}")
        
        # 删除配置项
        print("\n6. 删除配置项:")
        config.delete("debug")
        print(f"   删除后的debug值: {config.get('debug', '已删除')}")
        
        # 导出配置
        print("\n7. 导出配置到JSON:")
        config.export_to_json("app_config.json")
        
    # 重新打开配置验证持久化
    print("\n8. 重新打开配置验证持久化:")
    with ConfigManager("app_config") as config:
        print(f"   持久化后的配置节: {config.list_sections()}")
        print(f"   应用名称: {config.get('app_name')}")
        print(f"   数据库端口: {config.get('port', section='database')}")
        
        # 测试导入配置
        print("\n9. 修改配置后测试导入:")
        config.set("version", "2.0.0")  # 修改版本
        print(f"   修改后的版本: {config.get('version')}")
        
        # 从JSON导入（应该恢复原始配置）
        config.import_from_json("app_config.json")
        print(f"   导入后的版本: {config.get('version')}")
        
        # 清理
        print("\n10. 清理测试数据:")
        config.clear()
    
    # 删除配置文件
    for ext in ['', '.bak', '.dat', '.dir', '.db']:
        file_path = f"app_config{ext}"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"   删除配置文件: {file_path}")
    
    # 删除导出的JSON文件
    if os.path.exists("app_config.json"):
        os.remove("app_config.json")
        print(f"   删除JSON文件: app_config.json")

# 运行示例
configuration_manager()
```

## 5. 性能考量

使用shelve模块时，以下是一些性能考量：

1. **writeback参数的影响**：
   - `writeback=True`会使shelve在内存中缓存所有访问过的对象，这会增加内存使用量
   - `writeback=True`简化了可变对象的修改，但可能导致性能下降，特别是对于大型数据库
   - 对于频繁修改的小型数据集，writeback=True可能更方便
   - 对于大型数据集或内存受限的环境，writeback=False可能更高效

2. **sync()调用**：
   - 当使用writeback=True时，定期调用sync()可以避免一次性写入过多数据
   - sync()会将缓存的对象写回到磁盘，但不会清空缓存

3. **数据库大小**：
   - shelve适合中小型数据集
   - 对于大型数据集，考虑使用更专业的数据库解决方案

4. **并发访问**：
   - shelve不是线程安全的，多线程环境中需要额外的同步机制
   - 多进程环境中使用shelve可能导致数据损坏

5. **文件系统性能**：
   - shelve的性能受文件系统性能影响
   - 在SSD上使用shelve比在HDD上更快

让我们通过一个性能测试来比较不同使用方式的性能差异：

```python
import shelve
import os
import time

def performance_test():
    """shelve性能测试"""
    
    def cleanup_files():
        """清理测试文件"""
        for ext in ['', '.bak', '.dat', '.dir', '.db']:
            file_path = f"performance_test{ext}"
            if os.path.exists(file_path):
                os.remove(file_path)
    
    # 清理之前的测试文件
    cleanup_files()
    
    print("=== shelve性能测试 ===")
    
    # 测试参数
    num_items = 10000
    small_data = "x" * 100  # 100字节的数据
    medium_data = {"id": 1, "name": "test", "data": [i for i in range(100)]}  # 中等复杂度对象
    
    # 测试1: writeback=False，显式更新
    print("\n测试1: writeback=False，显式更新")
    
    start_time = time.time()
    with shelve.open("performance_test", writeback=False) as shelf:
        # 写入数据
        write_start = time.time()
        for i in range(num_items):
            shelf[f"item_{i}"] = small_data
        write_time = time.time() - write_start
        
        # 更新数据（需要显式赋值）
        update_start = time.time()
        for i in range(num_items):
            item = shelf[f"item_{i}"]
            # 模拟修改
            modified = item + "_updated"
            shelf[f"item_{i}"] = modified
        update_time = time.time() - update_start
        
        # 读取数据
        read_start = time.time()
        for i in range(num_items):
            _ = shelf[f"item_{i}"]
        read_time = time.time() - read_start
    
    total_time = time.time() - start_time
    print(f"  总时间: {total_time:.4f} 秒")
    print(f"  写入时间: {write_time:.4f} 秒 ({num_items/write_time:.0f} 项/秒)")
    print(f"  更新时间: {update_time:.4f} 秒 ({num_items/update_time:.0f} 项/秒)")
    print(f"  读取时间: {read_time:.4f} 秒 ({num_items/read_time:.0f} 项/秒)")
    
    # 清理
    cleanup_files()
    
    # 测试2: writeback=True，自动更新
    print("\n测试2: writeback=True，自动更新")
    
    start_time = time.time()
    with shelve.open("performance_test", writeback=True) as shelf:
        # 写入数据
        write_start = time.time()
        for i in range(num_items):
            shelf[f"item_{i}"] = small_data
        write_time = time.time() - write_start
        
        # 更新数据（自动跟踪）
        update_start = time.time()
        for i in range(num_items):
            item = shelf[f"item_{i}"]
            # 注意：对于字符串等不可变类型，这种修改不会生效
            # 但为了公平比较，我们仍然这样做
            # 对于可变类型，这里的修改会被自动跟踪
        update_time = time.time() - update_start
        
        # 读取数据
        read_start = time.time()
        for i in range(num_items):
            _ = shelf[f"item_{i}"]
        read_time = time.time() - read_start
    
    total_time = time.time() - start_time
    print(f"  总时间: {total_time:.4f} 秒")
    print(f"  写入时间: {write_time:.4f} 秒 ({num_items/write_time:.0f} 项/秒)")
    print(f"  更新时间: {update_time:.4f} 秒 ({num_items/update_time:.0f} 项/秒)")
    print(f"  读取时间: {read_time:.4f} 秒 ({num_items/read_time:.0f} 项/秒)")
    
    # 清理
    cleanup_files()
    
    # 测试3: 使用复杂对象
    print("\n测试3: 使用复杂对象 (writeback=True)")
    
    start_time = time.time()
    with shelve.open("performance_test", writeback=True) as shelf:
        # 写入复杂对象
        write_start = time.time()
        for i in range(num_items // 10):  # 减少项目数以加快测试
            item = medium_data.copy()
            item["id"] = i
            shelf[f"complex_item_{i}"] = item
        write_time = time.time() - write_start
        
        # 更新复杂对象（可变对象，writeback会自动跟踪）
        update_start = time.time()
        for i in range(num_items // 10):
            item = shelf[f"complex_item_{i}"]
            item["data"].append(999)  # 修改可变列表
        update_time = time.time() - update_start
        
        # 读取并验证更新
        verify_start = time.time()
        updated_count = 0
        for i in range(num_items // 10):
            item = shelf[f"complex_item_{i}"]
            if 999 in item["data"]:
                updated_count += 1
        verify_time = time.time() - verify_start
    
    total_time = time.time() - start_time
    print(f"  总时间: {total_time:.4f} 秒")
    print(f"  写入时间: {write_time:.4f} 秒 ({(num_items/10)/write_time:.0f} 项/秒)")
    print(f"  更新时间: {update_time:.4f} 秒 ({(num_items/10)/update_time:.0f} 项/秒)")
    print(f"  验证时间: {verify_time:.4f} 秒")
    print(f"  成功更新: {updated_count}/{num_items//10}")
    
    # 清理
    cleanup_files()
    
    print("\n性能测试总结:")
    print("1. writeback=False 适合：")
    print("   - 内存受限的环境")
    print("   - 以读取操作为主的场景")
    print("   - 不常修改可变对象的情况")
    print("2. writeback=True 适合：")
    print("   - 需要频繁修改可变对象的场景")
    print("   - 开发便捷性优先于性能的情况")
    print("   - 小型数据集")

# 运行性能测试
performance_test()
```

## 6. 安全性考虑

由于shelve内部使用pickle进行序列化，它继承了pickle的安全风险：

1. **反序列化攻击风险**：
   - 不要从不可信来源加载shelve数据库
   - 反序列化不可信数据可能导致任意代码执行

2. **文件权限**：
   - 确保shelve文件有适当的权限设置
   - 在多用户环境中，限制对shelve文件的访问

3. **数据加密**：
   - 对于敏感数据，考虑在存储前进行加密
   - 可以使用Python的cryptography库进行加密

让我们看一个简单的安全示例：

```python
import shelve
import os
from cryptography.fernet import Fernet

def secure_shelve_example():
    """安全使用shelve的示例"""
    
    # 生成加密密钥（在实际应用中，应该安全存储这个密钥）
    key = Fernet.generate_key()
    cipher = Fernet(key)
    print(f"生成加密密钥: {key.decode()}")
    
    # 定义加密和解密函数
    def encrypt_data(data):
        """加密数据"""
        import pickle
        # 先序列化，再加密
        serialized = pickle.dumps(data)
        encrypted = cipher.encrypt(serialized)
        return encrypted
    
    def decrypt_data(encrypted_data):
        """解密数据"""
        import pickle
        # 先解密，再反序列化
        decrypted = cipher.decrypt(encrypted_data)
        deserialized = pickle.loads(decrypted)
        return deserialized
    
    # 文件名
    shelf_file = 'secure_shelf'
    
    print("\n=== 安全shelve示例 ===")
    print("注意：这只是一个基本示例，实际应用中需要更完善的密钥管理")
    
    # 模拟敏感数据
    sensitive_data = {
        'username': 'admin',
        'password_hash': 'hashed_password_123',  # 实际应该存储哈希值，不是明文
        'api_keys': {
            'service1': 'api_key_123',
            'service2': 'api_key_456'
        },
        'personal_info': {
            'name': '张三',
            'phone': '13800138000',
            'email': 'zhangsan@example.com'
        }
    }
    
    print("\n1. 加密并存储敏感数据:")
    with shelve.open(shelf_file) as shelf:
        # 加密数据并存储
        encrypted = encrypt_data(sensitive_data)
        shelf['encrypted_data'] = encrypted
        print(f"   加密后数据长度: {len(encrypted)} 字节")
        print(f"   数据已存储到: {shelf_file}")
    
    print("\n2. 读取并解密数据:")
    with shelve.open(shelf_file) as shelf:
        # 读取加密数据
        encrypted = shelf['encrypted_data']
        
        # 解密数据
        decrypted_data = decrypt_data(encrypted)
        
        print(f"   解密成功，数据类型: {type(decrypted_data).__name__}")
        print(f"   用户名: {decrypted_data['username']}")
        print(f"   API密钥数量: {len(decrypted_data['api_keys'])}")
        print(f"   个人信息: {decrypted_data['personal_info']['name']}")
    
    print("\n3. 安全注意事项:")
    print("   - 密钥管理是关键，不要将密钥硬编码在代码中")
    print("   - 考虑使用环境变量或专门的密钥管理服务")
    print("   - 定期轮换密钥")
    print("   - 对于非常敏感的数据，考虑使用更专业的加密方案")
    
    # 清理
    for ext in ['', '.bak', '.dat', '.dir', '.db']:
        file_path = f"{shelf_file}{ext}"
        if os.path.exists(file_path):
            os.remove(file_path)
    
    print("\n4. 已清理测试文件")

# 运行示例
secure_shelve_example()
```

## 7. 与其他持久化方案的比较

| 持久化方案 | 优点 | 缺点 | 适用场景 |
|-----------|------|------|----------|
| shelve | 简单易用，类字典接口，支持复杂对象 | 线程安全问题，性能有限，不支持查询 | 小型应用，配置存储，对象缓存 |
| pickle | 支持几乎所有Python对象，简单 | 不安全，不可跨语言，不支持查询 | 对象序列化，程序状态保存 |
| SQLite | 功能强大，支持SQL查询，事务 | 更复杂，需要SQL知识 | 结构化数据，复杂查询，中型应用 |
| JSON | 跨语言，人类可读，安全 | 不支持复杂Python对象，较慢 | 配置文件，API交互，数据交换 |
| YAML | 人类可读，配置友好 | 解析较慢，第三方依赖 | 配置文件，文档 |
| CSV | 简单，广泛支持，表格数据 | 仅支持简单数据类型，无类型信息 | 表格数据，导入导出 |
| Redis | 高性能，内存数据库，丰富数据结构 | 内存开销，需要额外服务 | 缓存，会话管理，实时数据 |
| MongoDB | 文档数据库，灵活模式，强大查询 | 资源消耗，学习曲线 | 非结构化数据，大数据量 |

## 8. 常见问题和解决方案

1. **问题**：修改可变对象后，更改没有保存
   **解决方案**：使用writeback=True或显式重新赋值

2. **问题**：shelve文件在不同平台间不兼容
   **解决方案**：确保在所有平台上使用相同版本的Python，或考虑使用更通用的格式如JSON

3. **问题**：并发访问导致数据损坏
   **解决方案**：在多线程环境中使用锁，多进程环境中避免同时访问

4. **问题**：内存使用过高
   **解决方案**：使用writeback=False，定期调用sync()，或考虑使用其他存储方案

5. **问题**：shelf文件过大
   **解决方案**：定期清理过期数据，考虑使用压缩，或升级到更专业的数据库

## 9. 总结

shelve模块提供了一种简单而强大的方式来持久化Python对象。它结合了字典的易用性和pickle的灵活性，使得对象的存储和检索变得非常简单。

主要优势：
- 简单易用的字典式接口
- 支持几乎所有Python数据类型和自定义对象
- 不需要手动序列化/反序列化
- 适合快速原型开发和小型应用

主要限制：
- 不适合高并发环境
- 性能不如专用数据库
- 存在安全风险（同pickle）
- 不支持复杂查询

在实际应用中，shelve是小型应用、原型开发、配置管理和简单数据缓存的理想选择。对于需要更强大功能、更好性能或更高安全性的场景，应该考虑使用专门的数据库解决方案。

通过合理使用writeback参数、定期维护和适当的安全措施，可以充分利用shelve的优势，同时避免其潜在的问题。