# Python dbm模块详解

import dbm
import os
import sys
import datetime

# 1. 模块概述
print("=== 1. dbm模块概述 ===")
print("dbm模块提供了一个简单的键值存储系统，基于类Unix的dbm数据库。")
print("该模块是shelve模块的底层实现，提供了更底层的键值存储接口。")
print()
print("主要特点：")
print("- 简单的键值存储接口，类似字典操作")
print("- 基于文件的存储，无需额外的数据库服务")
print("- 键和值必须是字节类型")
print("- 支持不同的dbm实现（dbm.gnu, dbm.ndbm, dbm.dumb等）")
print("- 适合存储大量的键值对，查询速度快")

print()

# 2. dbm模块家族
print("=== 2. dbm模块家族 ===")
print("Python的dbm模块实际上是一个通用接口，支持多种dbm实现：")
print()
print("1. dbm.gnu: GNU dbm实现")
print("   - 支持变长记录")
print("   - 支持事务")
print("   - 提供更丰富的功能")
print()
print("2. dbm.ndbm: NDBM实现")
print("   - 传统的Unix dbm实现")
print("   - 固定大小的记录")
print()
print("3. dbm.dumb: 纯Python实现")
print("   - 不依赖外部库")
print("   - 性能较低，但跨平台兼容性好")
print()
print("4. dbm.dbm: BSD dbm实现")
print("   - 一些系统上的默认实现")
print()
print("当前系统上可用的dbm实现:")
try:
    import dbm.gnu
    print("   - dbm.gnu: 可用")
except ImportError:
    print("   - dbm.gnu: 不可用")

try:
    import dbm.ndbm
    print("   - dbm.ndbm: 可用")
except ImportError:
    print("   - dbm.ndbm: 不可用")

try:
    import dbm.dumb
    print("   - dbm.dumb: 可用")
except ImportError:
    print("   - dbm.dumb: 不可用")

try:
    import dbm.dbm
    print("   - dbm.dbm: 可用")
except ImportError:
    print("   - dbm.dbm: 不可用")

print()
print("默认使用的dbm实现:", dbm._defaultmod.__name__)

print()

# 3. 基本用法
print("=== 3. 基本用法 ===")

# 创建一个测试dbm文件
test_db = "test_dbm.db"

print("3.1 创建和打开dbm数据库：")
# 使用dbm.open()创建或打开一个dbm数据库
# 参数说明：
# - filename: 数据库文件名（不含扩展名）
# - flag: 打开模式，默认为'c'（读写模式，不存在则创建）
# - mode: 文件权限，默认为0o666

try:
    # 创建或打开数据库
    with dbm.open(test_db, 'c') as db:
        print(f"  创建并打开dbm数据库: {test_db}")
        print(f"  数据库类型: {type(db)}")
        print(f"  使用的dbm实现: {db.__module__}")

except Exception as e:
    print(f"  错误: {e}")

print()

print("3.2 添加和修改数据：")
try:
    # 使用上下文管理器打开数据库
    with dbm.open(test_db, 'c') as db:
        # 添加数据（键和值必须是字节类型）
        db[b'string'] = b"Hello, dbm!"
        db[b'integer'] = b"42"
        db[b'float'] = b"3.14159"
        db[b'boolean'] = b"True"
        
        # 修改数据
        db[b'integer'] = b"100"
        
        print(f"  添加和修改数据完成")

except Exception as e:
    print(f"  错误: {e}")

print()

print("3.3 读取数据：")
try:
    # 只读模式打开数据库
    with dbm.open(test_db, 'r') as db:
        # 读取单个值
        print(f"  db[b'string'] = {db[b'string']}")
        print(f"  db[b'integer'] = {db[b'integer']}")
        
        # 检查键是否存在
        print(f"  b'float' in db = {b'float' in db}")
        print(f"  b'nonexistent' in db = {b'nonexistent' in db}")
        
        # 使用get()方法读取值
        print(f"  db.get(b'nonexistent', b'default') = {db.get(b'nonexistent', b'default')}")
        
        # 转换为字符串
        string_value = db[b'string'].decode('utf-8')
        print(f"  转换为字符串: {string_value}")
        
        # 转换为其他类型
        integer_value = int(db[b'integer'].decode('utf-8'))
        print(f"  转换为整数: {integer_value}")
        
        float_value = float(db[b'float'].decode('utf-8'))
        print(f"  转换为浮点数: {float_value}")
        
        boolean_value = db[b'boolean'].decode('utf-8').lower() == 'true'
        print(f"  转换为布尔值: {boolean_value}")

except Exception as e:
    print(f"  错误: {e}")

print()

print("3.4 删除数据：")
try:
    with dbm.open(test_db, 'w') as db:
        # 删除单个键值对
        del db[b'boolean']
        
        # 检查是否已删除
        print(f"  b'boolean' in db = {b'boolean' in db}")
        
        # 尝试读取已删除的键会抛出KeyError
        try:
            value = db[b'boolean']
            print(f"  意外：读取到已删除的键值: {value}")
        except KeyError:
            print(f"  预期：读取已删除的键抛出KeyError")

except Exception as e:
    print(f"  错误: {e}")

print()

print("3.5 遍历数据库：")
try:
    with dbm.open(test_db, 'r') as db:
        print(f"  遍历键:")
        for key in db:
            print(f"    - {key} = {db[key]}")
        
        print()
        print(f"  遍历键值对:")
        # dbm对象支持items()方法
        for key, value in db.items():
            print(f"    - {key.decode('utf-8')}: {value.decode('utf-8')}")
        
        print()
        print(f"  遍历值:")
        for value in db.values():
            print(f"    - {value.decode('utf-8')}")

except Exception as e:
    print(f"  错误: {e}")

print()

print("3.6 数据库信息：")
try:
    with dbm.open(test_db, 'r') as db:
        print(f"  数据库中的键数量: {len(db)}")
        print(f"  数据库类型: {db.__module__}")
        
        # 检查数据库是否只读
        print(f"  数据库是否只读: {'是' if db.readonly else '否'}")

except Exception as e:
    print(f"  错误: {e}")

print()

# 4. 高级特性
print("=== 4. 高级特性 ===")

print("4.1 使用不同的打开模式：")
print("dbm.open()支持多种打开模式：")
print()
print("1. 'r': 只读模式")
print("   - 打开现有数据库进行读取")
print("   - 如果数据库不存在，抛出FileNotFoundError")

print()
print("2. 'w': 读写模式")
print("   - 打开现有数据库进行读写")
print("   - 如果数据库不存在，抛出FileNotFoundError")

print()
print("3. 'c': 读写模式，不存在则创建")
print("   - 打开现有数据库进行读写")
print("   - 如果数据库不存在，创建新的数据库")

print()
print("4. 'n': 读写模式，总是创建新数据库")
print("   - 总是创建新的数据库")
print("   - 如果数据库已存在，覆盖现有数据库")

print()
print("示例：使用'n'模式创建新数据库")
try:
    with dbm.open(test_db + "_new", 'n') as db:
        db[b'key1'] = b'value1'
        db[b'key2'] = b'value2'
        print(f"  创建新数据库并添加数据完成")

except Exception as e:
    print(f"  错误: {e}")

print()

print("4.2 使用特定的dbm实现：")
print("可以直接使用特定的dbm实现模块：")

# 尝试使用dbm.gnu
print("\n尝试使用dbm.gnu：")
try:
    import dbm.gnu
    with dbm.gnu.open(test_db + "_gnu", 'c') as db:
        db[b'key'] = b'value'
        print(f"  使用dbm.gnu创建数据库完成")
        print(f"  数据库类型: {db.__module__}")

except ImportError:
    print(f"  dbm.gnu不可用")
except Exception as e:
    print(f"  错误: {e}")

# 尝试使用dbm.dumb
print("\n尝试使用dbm.dumb：")
try:
    import dbm.dumb
    with dbm.dumb.open(test_db + "_dumb", 'c') as db:
        db[b'key'] = b'value'
        print(f"  使用dbm.dumb创建数据库完成")
        print(f"  数据库类型: {db.__module__}")

except ImportError:
    print(f"  dbm.dumb不可用")
except Exception as e:
    print(f"  错误: {e}")

print()

print("4.3 处理变长记录：")
print("一些dbm实现（如dbm.gnu）支持变长记录：")
try:
    import dbm.gnu
    with dbm.gnu.open(test_db + "_variable", 'c') as db:
        # 存储不同长度的值
        db[b'short'] = b'short'
        db[b'long'] = b'x' * 1000
        
        print(f"  存储短值: {db[b'short']}")
        print(f"  存储长值的长度: {len(db[b'long'])} 字节")
        print(f"  长值的前10个字节: {db[b'long'][:10]}...")

except ImportError:
    print(f"  dbm.gnu不可用，无法演示变长记录")
except Exception as e:
    print(f"  错误: {e}")

print()

# 5. 实际应用示例
print("=== 5. 实际应用示例 ===")

print("5.1 简单的用户会话存储：")

def save_session(session_id, user_id, username, expires_in=3600):
    """保存用户会话"""
    # 计算过期时间
    expires_at = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
    
    # 构建会话数据
    session_data = f"{user_id}:{username}:{expires_at.isoformat()}"
    
    try:
        # 保存到dbm数据库
        with dbm.open("sessions_dbm.db", 'c') as db:
            db[session_id.encode('utf-8')] = session_data.encode('utf-8')
        
        print(f"  会话已保存: {session_id}")
        return True
    
    except Exception as e:
        print(f"  保存会话错误: {e}")
        return False

def get_session(session_id):
    """获取用户会话"""
    try:
        with dbm.open("sessions_dbm.db", 'r') as db:
            session_key = session_id.encode('utf-8')
            
            if session_key not in db:
                return None
            
            # 读取会话数据
            session_data = db[session_key].decode('utf-8')
            
            # 解析会话数据
            user_id, username, expires_at_str = session_data.split(':', 2)
            expires_at = datetime.datetime.fromisoformat(expires_at_str)
            
            # 检查会话是否过期
            if datetime.datetime.now() > expires_at:
                # 会话过期，删除会话
                del db[session_key]
                return None
            
            return {
                'session_id': session_id,
                'user_id': user_id,
                'username': username,
                'expires_at': expires_at
            }
    
    except Exception as e:
        print(f"  获取会话错误: {e}")
        return None

def delete_session(session_id):
    """删除用户会话"""
    try:
        with dbm.open("sessions_dbm.db", 'w') as db:
            session_key = session_id.encode('utf-8')
            
            if session_key in db:
                del db[session_key]
                print(f"  会话已删除: {session_id}")
                return True
            
            return False
    
    except Exception as e:
        print(f"  删除会话错误: {e}")
        return False

# 使用会话存储功能
print(f"  保存会话：")
save_session("session123", "1001", "zhangsan", expires_in=60)

print(f"  获取会话：")
session = get_session("session123")
print(f"    {session}")

print(f"  删除会话：")
delete_session("session123")

# 清理测试文件
if os.path.exists("sessions_dbm.db.db"):
    os.remove("sessions_dbm.db.db")
if os.path.exists("sessions_dbm.db.dat"):
    os.remove("sessions_dbm.db.dat")
    os.remove("sessions_dbm.db.bak")
    os.remove("sessions_dbm.db.dir")

print()

print("5.2 简单的计数器应用：")

def increment_counter(counter_name):
    """增加计数器的值"""
    try:
        with dbm.open("counters.db", 'c') as db:
            counter_key = counter_name.encode('utf-8')
            
            # 获取当前值
            if counter_key in db:
                current_value = int(db[counter_key].decode('utf-8'))
            else:
                current_value = 0
            
            # 增加计数器
            new_value = current_value + 1
            db[counter_key] = str(new_value).encode('utf-8')
            
            print(f"  计数器 '{counter_name}' 已增加到: {new_value}")
            return new_value
    
    except Exception as e:
        print(f"  增加计数器错误: {e}")
        return None

def get_counter(counter_name):
    """获取计数器的值"""
    try:
        with dbm.open("counters.db", 'r') as db:
            counter_key = counter_name.encode('utf-8')
            
            if counter_key in db:
                return int(db[counter_key].decode('utf-8'))
            else:
                return 0
    
    except Exception as e:
        print(f"  获取计数器错误: {e}")
        return None

def reset_counter(counter_name):
    """重置计数器的值"""
    try:
        with dbm.open("counters.db", 'w') as db:
            counter_key = counter_name.encode('utf-8')
            
            if counter_key in db:
                del db[counter_key]
                print(f"  计数器 '{counter_name}' 已重置")
                return True
            
            return False
    
    except Exception as e:
        print(f"  重置计数器错误: {e}")
        return False

# 使用计数器功能
print(f"  增加页面访问计数器：")
increment_counter("page_views")
increment_counter("page_views")
increment_counter("page_views")

print(f"  获取页面访问计数：")
page_views = get_counter("page_views")
print(f"    页面访问次数: {page_views}")

print(f"  重置页面访问计数器：")
reset_counter("page_views")

# 清理测试文件
if os.path.exists("counters.db.db"):
    os.remove("counters.db.db")
if os.path.exists("counters.db.dat"):
    os.remove("counters.db.dat")
    os.remove("counters.db.bak")
    os.remove("counters.db.dir")

print()

print("5.3 简单的URL缩短服务：")

import random
import string

def generate_short_code(length=6):
    """生成随机短码"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(long_url, custom_code=None):
    """缩短URL"""
    try:
        with dbm.open("urls.db", 'c') as db:
            # 检查是否提供了自定义短码
            if custom_code:
                short_code = custom_code
            else:
                # 生成随机短码，确保不重复
                while True:
                    short_code = generate_short_code()
                    if short_code.encode('utf-8') not in db:
                        break
            
            # 保存URL映射
            db[short_code.encode('utf-8')] = long_url.encode('utf-8')
            
            print(f"  URL已缩短: {long_url} -> {short_code}")
            return short_code
    
    except Exception as e:
        print(f"  缩短URL错误: {e}")
        return None

def expand_url(short_code):
    """展开URL"""
    try:
        with dbm.open("urls.db", 'r') as db:
            code_key = short_code.encode('utf-8')
            
            if code_key not in db:
                return None
            
            long_url = db[code_key].decode('utf-8')
            print(f"  URL已展开: {short_code} -> {long_url}")
            return long_url
    
    except Exception as e:
        print(f"  展开URL错误: {e}")
        return None

# 使用URL缩短服务
print(f"  缩短URL：")
short_code1 = shorten_url("https://www.example.com")
short_code2 = shorten_url("https://www.python.org", "python")

print(f"  展开URL：")
expand_url(short_code1)
expand_url(short_code2)

# 清理测试文件
if os.path.exists("urls.db.db"):
    os.remove("urls.db.db")
if os.path.exists("urls.db.dat"):
    os.remove("urls.db.dat")
    os.remove("urls.db.bak")
    os.remove("urls.db.dir")

print()

# 6. 高级技巧
print("=== 6. 高级技巧 ===")

print("6.1 手动管理dbm文件：")
print("手动打开和关闭dbm数据库，确保资源正确释放：")

db = None
try:
    db = dbm.open(test_db + "_manual", 'c')
    
    # 执行操作
    db[b'key'] = b'manual operation'
    print(f"  手动管理: {db[b'key']}")
    
finally:
    # 确保关闭数据库
    if db:
        db.close()
        print(f"  数据库已手动关闭")

print()

print("6.2 使用事务（部分实现支持）：")
print("一些dbm实现（如dbm.gnu）支持事务：")

try:
    import dbm.gnu
    db = dbm.gnu.open(test_db + "_transaction", 'c')
    
    try:
        # 开始事务
        db.start()
        
        # 执行操作
        db[b'trans_key1'] = b'value1'
        db[b'trans_key2'] = b'value2'
        
        # 提交事务
        db.commit()
        print(f"  事务已提交")
        
    except Exception as e:
        # 回滚事务
        db.rollback()
        print(f"  事务已回滚: {e}")
    
    finally:
        db.close()
        
    # 验证数据已保存
    with dbm.gnu.open(test_db + "_transaction", 'r') as db:
        print(f"  事务后的数据: {db[b'trans_key1']}, {db[b'trans_key2']}")
        

except ImportError:
    print(f"  dbm.gnu不可用，无法演示事务")
except Exception as e:
    print(f"  错误: {e}")

print()

print("6.3 批量操作：")
print("使用批量操作提高性能：")

# 创建大量数据
large_data = {f"key_{i}": f"value_{i}" for i in range(100)}

try:
    with dbm.open(test_db + "_large", 'n') as db:
        # 批量添加数据
        for key, value in large_data.items():
            db[key.encode('utf-8')] = value.encode('utf-8')
        
        print(f"  批量添加了 {len(large_data)} 条数据")
        print(f"  数据库中的键数量: {len(db)}")

except Exception as e:
    print(f"  批量操作错误: {e}")

print()

print("6.4 使用dbm.dumb进行跨平台兼容：")
print("dbm.dumb是纯Python实现，确保跨平台兼容性：")

try:
    import dbm.dumb
    
    # 使用dbm.dumb创建数据库
    with dbm.dumb.open(test_db + "_compat", 'n') as db:
        db[b'key1'] = b'value1'
        db[b'key2'] = b'value2'
        
        print(f"  使用dbm.dumb创建的数据库中的键: {[k.decode('utf-8') for k in db]}")
        print(f"  跨平台兼容性数据库创建完成")

except Exception as e:
    print(f"  dbm.dumb操作错误: {e}")

print()

# 7. 最佳实践
print("=== 7. 最佳实践 ===")

print("1. 使用上下文管理器：")
print("   # 正确：使用上下文管理器自动关闭数据库")
print("   with dbm.open('data.db', 'c') as db:")
print("       db[b'key'] = b'value'")
print("   ")
print("   # 错误：忘记关闭数据库")
print("   db = dbm.open('data.db', 'c')")
print("   db[b'key'] = b'value'")
print("   # 忘记关闭，可能导致数据丢失")

print("\n2. 确保键和值是字节类型：")
print("   # 正确：将字符串转换为字节")
print("   key = 'my_key'.encode('utf-8')")
print("   value = 'my_value'.encode('utf-8')")
print("   db[key] = value")
print("   ")
print("   # 错误：直接使用字符串")
print("   db['my_key'] = 'my_value'  # 会抛出TypeError")

print("\n3. 选择合适的dbm实现：")
print("   - 需要高级功能时使用dbm.gnu")
print("   - 需要跨平台兼容时使用dbm.dumb")
print("   - 不确定时使用默认的dbm.open()")

print("\n4. 处理异常：")
print("   try:")
print("       with dbm.open('data.db', 'c') as db:")
print("           db[b'key'] = b'value'")
print("   except dbm.error as e:")
print("       print(f'dbm错误: {e}')")
print("   except Exception as e:")
print("       print(f'其他错误: {e}')")

print("\n5. 定期备份数据库文件：")
print("   import shutil")
print("   # 备份dbm文件")
print("   shutil.copy('data.db.dat', 'data.db.dat.bak')")
print("   shutil.copy('data.db.dir', 'data.db.dir.bak')")
print("   shutil.copy('data.db.bak', 'data.db.bak.bak')")

print("\n6. 限制单个值的大小：")
print("   - dbm适合存储小到中等大小的值")
print("   - 对于大值，考虑使用文件系统存储，并在dbm中存储文件路径")

print("\n7. 关闭自动提交（部分实现支持）：")
print("   # 对于支持事务的实现，可以关闭自动提交提高性能")
print("   import dbm.gnu")
print("   db = dbm.gnu.open('data.db', 'c')")
print("   db.setflags(dbm.gnu.DBM_SYNC)")  # 启用同步标志

# 8. 常见错误和陷阱
print("=== 8. 常见错误和陷阱 ===")

print("1. 使用字符串而非字节：")
print("   # 错误：直接使用字符串作为键或值")
print("   db['string_key'] = 'string_value'")
print("   # 抛出TypeError: dbm mappings have bytes or string elements only")
print("   ")
print("   # 正确：使用字节类型")
print("   db[b'bytes_key'] = b'bytes_value'")

print("\n2. 忘记关闭数据库：")
print("   # 错误：未关闭数据库连接")
print("   db = dbm.open('data.db', 'c')")
print("   db[b'key'] = b'value'")
print("   # 程序结束时可能不会自动关闭")
print("   ")
print("   # 正确：使用上下文管理器或手动关闭")
print("   with dbm.open('data.db', 'c') as db:")
print("       db[b'key'] = b'value'")

print("\n3. 数据库文件权限问题：")
print("   # 可能导致PermissionError")
print("   - 确保当前用户有读写数据库文件的权限")
print("   - 使用mode参数设置合适的文件权限")
print("   with dbm.open('data.db', 'c', mode=0o600) as db:")
print("       pass")

print("\n4. 数据库损坏：")
print("   # 可能导致dbm.error")
print("   - 定期备份数据库文件")
print("   - 避免在写入时中断程序")
print("   - 使用事务（如果支持）")

print("\n5. 不同dbm实现之间的兼容性：")
print("   # 警告：不同dbm实现创建的数据库文件不兼容")
print("   - 避免在不同实现之间切换")
print("   - 如果需要兼容性，使用dbm.dumb")

print("\n6. 键冲突：")
print("   # 错误：覆盖现有键而不知道")
print("   db[b'key'] = b'value1'")
print("   db[b'key'] = b'value2'  # 覆盖了原有值")
print("   ")
print("   # 正确：检查键是否已存在")
print("   if b'key' not in db:")
print("       db[b'key'] = b'value'")

print("\n7. 内存占用过高：")
print("   # 错误：加载大量数据到内存")
print("   all_data = {k: v for k, v in db.items()}  # 可能占用大量内存")
print("   ")
print("   # 正确：逐个处理数据")
print("   for k in db:")
print("       v = db[k]")
print("       # 处理数据")

# 9. 总结
print("=== 9. 总结 ===")
print("dbm模块提供了一个简单高效的键值存储系统，是shelve模块的底层实现。")
print()
print("主要功能：")
print("- 简单的键值存储接口，类似字典操作")
print("- 基于文件的存储，无需额外的数据库服务")
print("- 支持多种dbm实现，满足不同需求")
print("- 键和值必须是字节类型")
print("- 适合存储大量的键值对，查询速度快")
print()
print("应用场景：")
print("- 会话存储")
print("- 计数器应用")
print("- URL缩短服务")
print("- 缓存系统")
print("- 简单的配置存储")
print()
print("通过合理使用dbm模块，可以实现高效的键值存储功能，适用于各种需要快速查询的应用场景。")

# 清理测试文件
for ext in ['.dat', '.bak', '.dir', '.db']:
    if os.path.exists(test_db + ext):
        os.remove(test_db + ext)

# 清理其他测试文件
for db_file in [
    test_db + "_new",
    test_db + "_gnu",
    test_db + "_dumb", 
    test_db + "_variable",
    test_db + "_manual",
    test_db + "_transaction",
    test_db + "_large",
    test_db + "_compat"
]:
    for ext in ['.dat', '.bak', '.dir', '.db', '.pag', '.dir']:
        if os.path.exists(db_file + ext):
            os.remove(db_file + ext)
