# Python shelve模块详解

import shelve
import os
import datetime

# 1. 模块概述
print("=== 1. shelve模块概述 ===")
print("shelve模块提供了一个简单的键值存储系统，基于dbm模块构建，允许使用字符串键来访问Python对象。")
print("该模块的主要特点：")
print("- 简单的键值存储接口，类似字典操作")
print("- 自动处理对象的序列化和反序列化")
print("- 基于文件的存储，无需额外的数据库服务")
print("- 支持事务操作（通过上下文管理器）")
print("- 支持并发访问（取决于底层dbm实现）")
print()

# 2. 基本用法
print("=== 2. 基本用法 ===")

# 创建一个测试shelf文件
test_shelf = "test_shelf.db"

print("2.1 创建和打开shelf：")
# 使用shelve.open()创建或打开一个shelf文件
with shelve.open(test_shelf) as s:
    print(f"  创建并打开shelf文件: {test_shelf}")
    print(f"  shelf对象类型: {type(s)}")

print()

print("2.2 添加和修改数据：")
# 使用上下文管理器打开shelf
with shelve.open(test_shelf) as s:
    # 添加数据（类似字典操作）
    s['string'] = "Hello, shelve!"
    s['list'] = [1, 2, 3, 4, 5]
    s['dict'] = {'name': '张三', 'age': 30, 'city': '北京'}
    s['tuple'] = (10, 20, 30)
    s['int'] = 42
    s['float'] = 3.14159
    s['bool'] = True
    s['none'] = None
    
    # 修改数据
    s['int'] = 100
    s['list'].append(6)  # 注意：这种方式不会自动保存到shelf！
    
    # 正确的修改方式
    my_list = s['list']
    my_list.append(7)
    s['list'] = my_list  # 需要重新赋值
    
    print(f"  添加和修改数据完成")

print()

print("2.3 读取数据：")
with shelve.open(test_shelf) as s:
    # 读取单个值
    print(f"  s['string'] = {s['string']}")
    print(f"  s['int'] = {s['int']}")
    print(f"  s['list'] = {s['list']}")
    
    # 检查键是否存在
    print(f"  'dict' in s = {'dict' in s}")
    print(f"  'nonexistent_key' in s = {'nonexistent_key' in s}")
    
    # 使用get()方法读取值
    print(f"  s.get('nonexistent_key', '默认值') = {s.get('nonexistent_key', '默认值')}")

print()

print("2.4 删除数据：")
with shelve.open(test_shelf) as s:
    # 删除单个键值对
    del s['bool']
    
    # 检查是否已删除
    print(f"  'bool' in s = {'bool' in s}")
    
    # 清空shelf
    # s.clear()  # 取消注释以清空shelf

print()

print("2.5 遍历shelf：")
with shelve.open(test_shelf) as s:
    print(f"  遍历键:")
    for key in s:
        print(f"    - {key}")
    
    print(f"  遍历键值对:")
    for key, value in s.items():
        print(f"    - {key}: {value}")
    
    print(f"  遍历值:")
    for value in s.values():
        print(f"    - {value}")

print()

# 3. 高级特性
print("=== 3. 高级特性 ===")

print("3.1 写回模式：")
print("   默认情况下，shelve模块不会自动保存对可变对象（如列表、字典）的修改。")
print("   可以使用writeback=True参数启用写回模式。")

with shelve.open(test_shelf, writeback=True) as s:
    # 启用writeback=True后，可以直接修改可变对象
    s['list'].append(8)
    s['dict']['email'] = "zhangsan@example.com"
    
    print(f"  使用writeback=True后，直接修改列表: {s['list']}")
    print(f"  使用writeback=True后，直接修改字典: {s['dict']}")

print()

print("3.2 自定义类的存储：")
# 定义一个自定义类
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.created_at = datetime.datetime.now()
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"
    
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

# 存储自定义类实例
with shelve.open(test_shelf) as s:
    # 创建Person实例
    person = Person("李四", 25, "lisi@example.com")
    
    # 存储Person实例
    s['person'] = person
    
    print(f"  存储自定义类实例: {person}")

# 读取自定义类实例
with shelve.open(test_shelf) as s:
    # 读取Person实例
    loaded_person = s['person']
    
    print(f"  读取自定义类实例: {loaded_person}")
    print(f"  调用实例方法: {loaded_person.greet()}")
    print(f"  实例类型: {type(loaded_person)}")

print()

print("3.3 多个键值对的原子操作：")
# 使用上下文管理器可以确保多个操作的原子性
with shelve.open(test_shelf) as s:
    # 同时修改多个键值对
    s['counter'] = s.get('counter', 0) + 1
    s['last_updated'] = datetime.datetime.now()
    
    print(f"  计数器值: {s['counter']}")
    print(f"  最后更新时间: {s['last_updated']}")

print()

# 4. 实用函数和参数
print("=== 4. 实用函数和参数 ===")

print("4.1 shelve.open()函数：")
print("   打开或创建一个shelf文件")
print("   参数：")
print("   - filename: shelf文件的名称（不含扩展名）")
print("   - flag: 打开模式，默认为'c'（读写模式）")
print("     - 'r': 只读模式")
print("     - 'w': 只写模式")
print("     - 'c': 读写模式，不存在则创建")
print("     - 'n': 读写模式，总是创建新文件")
print("   - protocol: 序列化协议版本，默认为pickle.HIGHEST_PROTOCOL")
print("   - writeback: 是否启用写回模式，默认为False")
print("   - writeback参数说明：")
print("     - writeback=True: 启用写回模式，自动保存对可变对象的修改")
print("     - writeback=False: 禁用写回模式，需要手动保存对可变对象的修改")
print("     - 注意：writeback=True会使用更多内存，因为它会缓存所有访问过的对象")

print()

print("4.2 shelf对象的方法：")
print("   shelf对象支持类似字典的方法：")
print("   - s[key]: 获取键对应的值")
print("   - s[key] = value: 设置键对应的值")
print("   - del s[key]: 删除键值对")
print("   - key in s: 检查键是否存在")
print("   - s.keys(): 返回所有键的视图")
print("   - s.values(): 返回所有值的视图")
print("   - s.items(): 返回所有键值对的视图")
print("   - s.get(key, default): 获取键对应的值，不存在则返回默认值")
print("   - s.pop(key, default): 删除并返回键对应的值")
print("   - s.clear(): 清空所有键值对")
print("   - s.close(): 关闭shelf文件")

print()

# 5. 实际应用示例
print("=== 5. 实际应用示例 ===")

print("5.1 用户会话管理：")
def create_session(session_id, user_id, username, expires_in=3600):
    """创建用户会话"""
    session = {
        'session_id': session_id,
        'user_id': user_id,
        'username': username,
        'created_at': datetime.datetime.now(),
        'expires_at': datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
    }
    
    with shelve.open("sessions.db") as s:
        s[session_id] = session
    
    return session

def get_session(session_id):
    """获取用户会话"""
    with shelve.open("sessions.db") as s:
        session = s.get(session_id)
        
        # 检查会话是否过期
        if session and session['expires_at'] < datetime.datetime.now():
            # 会话过期，删除会话
            del s[session_id]
            return None
        
        return session

def delete_session(session_id):
    """删除用户会话"""
    with shelve.open("sessions.db") as s:
        if session_id in s:
            del s[session_id]
            return True
        return False

# 使用会话管理功能
print(f"  创建会话：")
session = create_session("session123", 1001, "zhangsan", expires_in=60)
print(f"    {session}")

print(f"  获取会话：")
loaded_session = get_session("session123")
print(f"    {loaded_session}")

print(f"  删除会话：")
result = delete_session("session123")
print(f"    删除结果: {result}")

# 清理会话文件
if os.path.exists("sessions.db.dat"):
    os.remove("sessions.db.dat")
    os.remove("sessions.db.bak")
    os.remove("sessions.db.dir")

print()

print("5.2 简单的配置管理：")
def save_config(config_name, config_data):
    """保存配置数据"""
    with shelve.open("configurations.db") as s:
        s[config_name] = config_data
    
    print(f"  配置 '{config_name}' 已保存")

def load_config(config_name, default=None):
    """加载配置数据"""
    with shelve.open("configurations.db") as s:
        return s.get(config_name, default)

def update_config(config_name, key, value):
    """更新配置数据"""
    with shelve.open("configurations.db") as s:
        if config_name in s:
            config = s[config_name]
            config[key] = value
            s[config_name] = config
            print(f"  配置 '{config_name}' 的 '{key}' 已更新为 '{value}'")
            return True
        return False

# 使用配置管理功能
# 保存应用配置
app_config = {
    'app_name': 'MyApp',
    'version': '1.0.0',
    'debug': True,
    'log_level': 'INFO',
    'max_users': 1000
}

save_config("app", app_config)

# 加载配置
loaded_config = load_config("app")
print(f"  加载的配置: {loaded_config}")

# 更新配置
update_config("app", "debug", False)
update_config("app", "max_users", 2000)

# 再次加载配置
updated_config = load_config("app")
print(f"  更新后的配置: {updated_config}")

# 清理配置文件
if os.path.exists("configurations.db.dat"):
    os.remove("configurations.db.dat")
    os.remove("configurations.db.bak")
    os.remove("configurations.db.dir")

print()

print("5.3 简单的缓存系统：")
def cache_data(key, data, expiration=300):
    """缓存数据"""
    cache_item = {
        'data': data,
        'timestamp': datetime.datetime.now(),
        'expiration': expiration
    }
    
    with shelve.open("cache.db") as s:
        s[key] = cache_item
    
    print(f"  数据已缓存到键 '{key}'，过期时间: {expiration} 秒")

def get_cached_data(key):
    """获取缓存数据"""
    with shelve.open("cache.db") as s:
        if key in s:
            cache_item = s[key]
            
            # 检查是否过期
            age = (datetime.datetime.now() - cache_item['timestamp']).total_seconds()
            if age > cache_item['expiration']:
                # 数据过期，删除缓存
                del s[key]
                return None
            
            return cache_item['data']
    
    return None

def invalidate_cache(key):
    """使缓存失效"""
    with shelve.open("cache.db") as s:
        if key in s:
            del s[key]
            return True
    return False

def clear_expired_cache():
    """清理过期缓存"""
    count = 0
    with shelve.open("cache.db") as s:
        for key in list(s.keys()):
            cache_item = s[key]
            age = (datetime.datetime.now() - cache_item['timestamp']).total_seconds()
            if age > cache_item['expiration']:
                del s[key]
                count += 1
    
    print(f"  清理了 {count} 个过期缓存项")
    return count

# 使用缓存系统
# 缓存数据
cache_data("user:1001", {"id": 1001, "name": "张三", "email": "zhangsan@example.com"}, expiration=10)

# 获取缓存数据
cached_user = get_cached_data("user:1001")
print(f"  获取缓存数据: {cached_user}")

# 清理过期缓存
clear_expired_cache()

# 再次获取缓存数据（应该已过期）
cached_user_expired = get_cached_data("user:1001")
print(f"  缓存过期后获取数据: {cached_user_expired}")

# 清理缓存文件
if os.path.exists("cache.db.dat"):
    os.remove("cache.db.dat")
    os.remove("cache.db.bak")
    os.remove("cache.db.dir")

print()

# 6. 高级技巧
print("=== 6. 高级技巧 ===")

print("6.1 使用writeback=True处理可变对象：")
# 启用writeback模式可以自动保存对可变对象的修改
with shelve.open(test_shelf, writeback=True) as s:
    # 直接修改列表
    s['dynamic_list'] = [1, 2, 3]
    s['dynamic_list'].append(4)  # 启用writeback后，不需要重新赋值
    s['dynamic_list'].extend([5, 6])  # 可以直接修改
    
    print(f"  启用writeback后直接修改列表: {s['dynamic_list']}")

print()

print("6.2 使用pickle协议版本：")
# 指定pickle协议版本
with shelve.open(test_shelf, protocol=pickle.HIGHEST_PROTOCOL) as s:
    # 存储数据
    s['large_object'] = {f'key_{i}': f'value_{i}' for i in range(100)}
    
    print(f"  使用最高pickle协议存储大对象完成")

print()

print("6.3 手动管理shelf文件：")
# 手动打开和关闭shelf文件
s = shelve.open(test_shelf)
try:
    # 执行操作
    s['manual_key'] = "手动管理shelf"
    print(f"  手动管理shelf: s['manual_key'] = {s['manual_key']}")
finally:
    # 确保关闭shelf文件
s.close()

print()

print("6.4 使用不同的dbm实现：")
# 注意：在不同平台上，默认的dbm实现可能不同
print(f"  当前系统上shelve使用的dbm模块: {shelve._default_dbmmodule.__name__}")

# 可以通过指定dbmmodule参数来使用特定的dbm实现
# 例如：
# import dbm.gnu
# shelve.open(test_shelf, dbmmodule=dbm.gnu)

print()

# 7. 最佳实践
print("=== 7. 最佳实践 ===")

print("1. 使用上下文管理器：")
print("   # 正确：使用上下文管理器自动关闭shelf")
print("   with shelve.open('data.db') as s:")
print("       s['key'] = value")
print("   ")
print("   # 错误：忘记关闭shelf")
print("   s = shelve.open('data.db')")
print("   s['key'] = value")
print("   # 忘记关闭，可能导致数据丢失")

print("\n2. 注意可变对象的修改：")
print("   # 错误：直接修改可变对象")
print("   with shelve.open('data.db') as s:")
print("       s['list'].append(4)  # 不会自动保存")
print("   ")
print("   # 正确：重新赋值可变对象")
print("   with shelve.open('data.db') as s:")
print("       my_list = s['list']")
print("       my_list.append(4)")
print("       s['list'] = my_list  # 重新赋值")
print("   ")
print("   # 或使用writeback=True")
print("   with shelve.open('data.db', writeback=True) as s:")
print("       s['list'].append(4)  # 自动保存")

print("\n3. 使用有意义的键名：")
print("   # 错误：使用无意义的键名")
print("   s['a'] = 1")
print("   ")
print("   # 正确：使用有意义的键名")
print("   s['user:1001'] = user_data")
print("   s['config:app:debug'] = True")

print("\n4. 处理并发访问：")
print("   # 注意：shelve模块的并发访问支持取决于底层的dbm实现")
print("   # 对于需要高并发的应用，考虑使用其他数据库解决方案")
print("   # 或使用文件锁定机制")

print("\n5. 定期清理过期数据：")
print("   # 对于有过期时间的数据，定期清理过期项")
print("   def clean_expired_data():")
print("       with shelve.open('data.db') as s:")
print("           for key in list(s.keys()):")
print("               item = s[key]")
print("               if item['expires_at'] < datetime.datetime.now():")
print("                   del s[key]")

print("\n6. 备份shelf文件：")
print("   # 定期备份shelf文件以防止数据丢失")
print("   import shutil")
print("   shutil.copy('data.db.dat', 'data.db.dat.bak')")
print("   shutil.copy('data.db.dir', 'data.db.dir.bak')")
print("   shutil.copy('data.db.bak', 'data.db.bak.bak')")

print("\n7. 限制shelf的大小：")
print("   # 定期检查shelf文件的大小，防止过大")
print("   import os")
print("   if os.path.getsize('data.db.dat') > 10 * 1024 * 1024:  # 10MB")
print("       # 清理或归档数据")

# 8. 常见错误和陷阱
print("=== 8. 常见错误和陷阱 ===")

print("1. 忘记关闭shelf文件：")
print("   # 错误：忘记关闭shelf文件")
print("   s = shelve.open('data.db')")
print("   s['key'] = value")
print("   # 程序结束时可能不会自动关闭")
print("   ")
print("   # 正确：使用上下文管理器或手动关闭")
print("   with shelve.open('data.db') as s:")
print("       s['key'] = value")

print("\n2. 直接修改可变对象：")
print("   # 错误：直接修改可变对象不会自动保存")
print("   with shelve.open('data.db') as s:")
print("       s['list'].append(4)")
print("   ")
print("   # 正确：重新赋值或使用writeback=True")
print("   with shelve.open('data.db') as s:")
print("       my_list = s['list']")
print("       my_list.append(4)")
print("       s['list'] = my_list")

print("\n3. 键必须是字符串类型：")
print("   # 错误：使用非字符串类型作为键")
print("   with shelve.open('data.db') as s:")
print("       s[123] = value  # 会抛出TypeError")
print("   ")
print("   # 正确：使用字符串类型作为键")
print("   with shelve.open('data.db') as s:")
print("       s['123'] = value")

print("\n4. 内存占用过高：")
print("   # 错误：启用writeback=True后处理大量数据")
print("   with shelve.open('data.db', writeback=True) as s:")
print("       for i in range(100000):")
print("           s[f'key_{i}'] = f'value_{i}'  # 内存占用会很高")
print("   ")
print("   # 正确：禁用writeback或分批处理")
print("   with shelve.open('data.db') as s:")
print("       for i in range(100000):")
print("           s[f'key_{i}'] = f'value_{i}'")

print("\n5. 并发访问问题：")
print("   # 错误：在多个线程或进程中同时写入shelf")
print("   # 可能导致数据损坏或不一致")
print("   ")
print("   # 正确：使用锁或考虑其他数据库解决方案")
print("   import threading")
print("   lock = threading.Lock()")
print("   ")
print("   with lock:")
print("       with shelve.open('data.db') as s:")
print("           s['key'] = value")

print("\n6. 数据持久化问题：")
print("   # 错误：假设所有操作都会立即持久化到磁盘")
print("   with shelve.open('data.db') as s:")
print("       s['key'] = value")
print("   # 实际可能在关闭时才写入磁盘")
print("   ")
print("   # 正确：确保使用上下文管理器或手动关闭")

# 9. 总结
print("=== 9. 总结 ===")
print("shelve模块是Python中一个简单易用的键值存储系统，基于dbm模块构建，允许使用字符串键来访问Python对象。")
print()
print("主要功能：")
print("- 简单的键值存储接口，类似字典操作")
print("- 自动处理对象的序列化和反序列化")
print("- 基于文件的存储，无需额外的数据库服务")
print("- 支持事务操作和并发访问")
print()
print("优势：")
print("- 易于使用，API简单直观")
print("- 无需额外安装依赖")
print("- 自动处理对象的序列化")
print("- 适合小型应用和快速原型开发")
print()
print("应用场景：")
print("- 用户会话管理")
print("- 简单的配置存储")
print("- 缓存系统")
print("- 小型应用的数据存储")
print("- 快速原型开发")
print()
print("注意事项：")
print("- 不要在高并发环境下使用")
print("- 避免存储过大的数据")
print("- 注意可变对象的修改方式")
print("- 定期备份数据文件")

print("\n通过合理使用shelve模块，可以快速实现简单的数据持久化功能，适用于小型应用和快速开发场景。")

# 清理测试文件
if os.path.exists(f"{test_shelf}.dat"):
    os.remove(f"{test_shelf}.dat")
    if os.path.exists(f"{test_shelf}.bak"):
        os.remove(f"{test_shelf}.bak")
    if os.path.exists(f"{test_shelf}.dir"):
        os.remove(f"{test_shelf}.dir")
