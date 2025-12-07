# redis模块详解

redis是一个开源的内存数据结构存储，可用作数据库、缓存和消息代理。Python的redis模块提供了与Redis数据库交互的接口，支持所有Redis命令和功能。

## 模块概述

redis模块主要提供以下功能：

- 连接Redis服务器
- 执行Redis命令（字符串、哈希、列表、集合、有序集合等）
- 事务管理
- 管道操作
- 发布/订阅功能
- Lua脚本执行
- 连接池管理
- 数据持久化配置
- 哨兵模式和集群支持

## 安装

使用pip安装redis模块：

```bash
pip install redis
```

## 基本概念

在使用redis模块之前，需要了解几个基本概念：

1. **Connection**: Redis服务器连接
2. **Connection Pool**: 连接池，用于管理多个Redis连接
3. **Key-Value**: Redis的数据存储模型
4. **Data Structures**: Redis支持的数据结构（字符串、哈希、列表、集合、有序集合等）
5. **Pipeline**: 管道，用于批量执行命令
6. **Transaction**: 事务，用于原子性执行多个命令
7. **Pub/Sub**: 发布/订阅，用于消息传递

## 基本用法

### 创建Redis连接

#### 基本连接

```python
import redis

# 创建Redis连接
r = redis.Redis(
    host='localhost',  # Redis服务器地址
    port=6379,         # Redis服务器端口
    db=0,              # 数据库编号
    password=None,     # 密码（如果有）
    decode_responses=True  # 自动解码响应内容为字符串
)

# 测试连接
print("Redis连接成功")
print(f"Redis服务器信息: {r.info('server')}")
```

#### 使用连接池

```python
import redis

# 创建连接池
pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    db=0,
    password=None,
    decode_responses=True,
    max_connections=100  # 最大连接数
)

# 从连接池获取连接
r = redis.Redis(connection_pool=pool)

# 测试连接
print("Redis连接池连接成功")
print(f"Redis服务器信息: {r.info('server')}")
```

#### 配置URL连接

```python
import redis

# 使用URL连接
url = "redis://:password@localhost:6379/0"  # 格式: redis://[:password]@host:port/db
r = redis.from_url(url, decode_responses=True)

# 测试连接
print("Redis URL连接成功")
print(f"Redis服务器信息: {r.info('server')}")
```

### 字符串操作

字符串是Redis最基本的数据类型，一个键对应一个值。

```python
# 设置字符串
r.set('name', 'Alice')
print("设置字符串: name = Alice")

# 获取字符串
name = r.get('name')
print(f"获取字符串: name = {name}")

# 设置多个字符串
r.mset({'age': 30, 'city': 'New York'})
print("设置多个字符串: age = 30, city = New York")

# 获取多个字符串
values = r.mget('name', 'age', 'city')
print(f"获取多个字符串: {values}")

# 追加字符串
r.append('name', ' Smith')
print("追加字符串: name = Alice Smith")

# 获取字符串长度
length = r.strlen('name')
print(f"字符串长度: {length}")

# 原子递增
r.set('counter', 0)
r.incr('counter')
r.incr('counter', 5)
counter = r.get('counter')
print(f"原子递增后: counter = {counter}")

# 原子递减
r.decr('counter', 3)
counter = r.get('counter')
print(f"原子递减后: counter = {counter}")

# 设置带过期时间的字符串
r.setex('temp_key', 10, 'temporary value')  # 10秒后过期
print("设置带过期时间的字符串: temp_key = temporary value (10秒后过期)")

# 检查键是否存在
exists = r.exists('name')
print(f"键name是否存在: {exists}")

# 获取键的过期时间
ttl = r.ttl('temp_key')
print(f"键temp_key的过期时间: {ttl}秒")

# 删除键
r.delete('temp_key')
print("删除键: temp_key")
```

### 哈希操作

哈希是一个键值对集合，适合存储对象。

```python
# 设置哈希字段
r.hset('user:1', 'name', 'Alice')
r.hset('user:1', 'age', 30)
r.hset('user:1', 'city', 'New York')
print("设置哈希字段: user:1 -> name=Alice, age=30, city=New York")

# 获取哈希字段
name = r.hget('user:1', 'name')
print(f"获取哈希字段: user:1.name = {name}")

# 设置多个哈希字段
r.hmset('user:2', {'name': 'Bob', 'age': 25, 'city': 'London'})
print("设置多个哈希字段: user:2 -> name=Bob, age=25, city=London")

# 获取多个哈希字段
values = r.hmget('user:1', ['name', 'age', 'city'])
print(f"获取多个哈希字段: user:1 -> {values}")

# 获取哈希所有字段
fields = r.hkeys('user:1')
print(f"获取哈希所有字段: {fields}")

# 获取哈希所有值
values = r.hvals('user:1')
print(f"获取哈希所有值: {values}")

# 获取哈希所有键值对
data = r.hgetall('user:1')
print(f"获取哈希所有键值对: {data}")

# 检查哈希字段是否存在
exists = r.hexists('user:1', 'name')
print(f"哈希字段name是否存在: {exists}")

# 获取哈希字段数量
count = r.hlen('user:1')
print(f"哈希字段数量: {count}")

# 删除哈希字段
r.hdel('user:1', 'city')
print("删除哈希字段: city")

# 原子递增哈希字段值
r.hincrby('user:1', 'age', 1)
age = r.hget('user:1', 'age')
print(f"原子递增哈希字段后: age = {age}")
```

### 列表操作

列表是一个按插入顺序排序的字符串集合，适合实现队列、栈和列表等数据结构。

```python
# 左侧插入元素
r.lpush('fruits', 'apple')
r.lpush('fruits', 'banana')
r.lpush('fruits', 'orange')
print("左侧插入元素: fruits -> orange, banana, apple")

# 右侧插入元素
r.rpush('fruits', 'grape')
print("右侧插入元素: fruits -> orange, banana, apple, grape")

# 获取列表长度
length = r.llen('fruits')
print(f"列表长度: {length}")

# 获取列表元素（通过索引）
fruit = r.lindex('fruits', 1)
print(f"列表索引1的元素: {fruit}")

# 获取列表元素范围
elements = r.lrange('fruits', 0, -1)
print(f"列表所有元素: {elements}")

# 左侧弹出元素
left_fruit = r.lpop('fruits')
print(f"左侧弹出元素: {left_fruit}")
print(f"剩余元素: {r.lrange('fruits', 0, -1)}")

# 右侧弹出元素
right_fruit = r.rpop('fruits')
print(f"右侧弹出元素: {right_fruit}")
print(f"剩余元素: {r.lrange('fruits', 0, -1)}")

# 插入元素到列表指定位置前
r.linsert('fruits', 'before', 'banana', 'cherry')
print(f"在banana前插入cherry: {r.lrange('fruits', 0, -1)}")

# 插入元素到列表指定位置后
r.linsert('fruits', 'after', 'banana', 'lemon')
print(f"在banana后插入lemon: {r.lrange('fruits', 0, -1)}")

# 修改列表指定索引的元素
r.lset('fruits', 0, 'strawberry')
print(f"修改索引0的元素: {r.lrange('fruits', 0, -1)}")

# 删除列表中指定数量的元素
r.lrem('fruits', 1, 'banana')  # 删除1个banana
print(f"删除1个banana: {r.lrange('fruits', 0, -1)}")

# 修剪列表
r.ltrim('fruits', 0, 1)
print(f"修剪列表到前2个元素: {r.lrange('fruits', 0, -1)}")
```

### 集合操作

集合是一个无序的字符串集合，每个元素都是唯一的。

```python
# 添加元素到集合
r.sadd('colors', 'red')
r.sadd('colors', 'green')
r.sadd('colors', 'blue')
r.sadd('colors', 'red')  # 重复元素不会被添加
print("添加元素到集合: colors -> red, green, blue")

# 获取集合所有元素
colors = r.smembers('colors')
print(f"集合所有元素: {colors}")

# 获取集合大小
size = r.scard('colors')
print(f"集合大小: {size}")

# 检查元素是否在集合中
exists = r.sismember('colors', 'red')
print(f"元素red是否在集合中: {exists}")

# 从集合中移除元素
r.srem('colors', 'green')
print(f"移除元素green后: {r.smembers('colors')}")

# 随机获取集合中的元素
random_color = r.srandmember('colors')
print(f"随机获取元素: {random_color}")

# 随机移除并返回集合中的元素
popped_color = r.spop('colors')
print(f"随机移除并返回元素: {popped_color}")
print(f"剩余元素: {r.smembers('colors')}")

# 创建另一个集合
r.sadd('more_colors', 'blue', 'yellow', 'purple')

# 计算两个集合的交集
intersection = r.sinter('colors', 'more_colors')
print(f"集合交集: {intersection}")

# 计算两个集合的并集
union = r.sunion('colors', 'more_colors')
print(f"集合并集: {union}")

# 计算两个集合的差集
difference = r.sdiff('colors', 'more_colors')
print(f"集合差集: {difference}")

# 将交集存储到新集合
r.sinterstore('common_colors', 'colors', 'more_colors')
print(f"交集存储到新集合: {r.smembers('common_colors')}")
```

### 有序集合操作

有序集合是一个有序的字符串集合，每个元素都有一个分数，用于排序。

```python
# 添加元素到有序集合
r.zadd('scores', {'Alice': 90, 'Bob': 85, 'Charlie': 95, 'David': 80})
print("添加元素到有序集合: scores -> Alice(90), Bob(85), Charlie(95), David(80)")

# 获取有序集合的大小
size = r.zcard('scores')
print(f"有序集合大小: {size}")

# 获取元素的分数
alice_score = r.zscore('scores', 'Alice')
print(f"Alice的分数: {alice_score}")

# 获取元素排名（升序）
alice_rank = r.zrank('scores', 'Alice')  # 从0开始
print(f"Alice的排名（升序）: {alice_rank + 1}")

# 获取元素排名（降序）
alice_rev_rank = r.zrevrank('scores', 'Alice')  # 从0开始
print(f"Alice的排名（降序）: {alice_rev_rank + 1}")

# 获取有序集合元素（升序）
elements = r.zrange('scores', 0, -1, withscores=True)
print(f"有序集合元素（升序）: {elements}")

# 获取有序集合元素（降序）
elements_desc = r.zrevrange('scores', 0, -1, withscores=True)
print(f"有序集合元素（降序）: {elements_desc}")

# 根据分数范围获取元素（升序）
mid_scores = r.zrangebyscore('scores', 85, 90, withscores=True)
print(f"分数在85-90之间的元素: {mid_scores}")

# 根据分数范围获取元素数量
count = r.zcount('scores', 80, 100)
print(f"分数在80-100之间的元素数量: {count}")

# 增加元素的分数
r.zincrby('scores', 5, 'Alice')
print(f"Alice分数增加5后: {r.zscore('scores', 'Alice')}")

# 从有序集合中移除元素
r.zrem('scores', 'David')
print(f"移除David后: {r.zrevrange('scores', 0, -1, withscores=True)}")

# 根据排名范围移除元素
r.zremrangebyrank('scores', 0, 0)  # 移除排名最低的元素
print(f"移除排名最低的元素后: {r.zrevrange('scores', 0, -1, withscores=True)}")

# 根据分数范围移除元素
r.zremrangebyscore('scores', 0, 85)  # 移除分数小于等于85的元素
print(f"移除分数小于等于85的元素后: {r.zrevrange('scores', 0, -1, withscores=True)}")
```

## 高级功能

### 事务管理

Redis事务通过MULTI、EXEC、DISCARD和WATCH命令实现：

```python
# 使用事务
with r.pipeline(transaction=True) as pipe:
    # 开始事务
    pipe.multi()
    
    # 执行多个命令
    pipe.set('key1', 'value1')
    pipe.set('key2', 'value2')
    pipe.hset('user:1', 'name', 'Alice')
    pipe.hincrby('user:1', 'age', 1)
    
    # 执行事务
    results = pipe.execute()
    
    print("事务执行成功")
    print(f"执行结果: {results}")

# 使用WATCH命令监控键变化
try:
    # 监控键
    r.watch('balance')
    
    # 获取当前值
    balance = r.get('balance')
    if balance is None:
        balance = 0
    else:
        balance = int(balance)
    
    # 如果余额足够
    if balance >= 100:
        # 开始事务
        with r.pipeline(transaction=True) as pipe:
            pipe.multi()
            pipe.decrby('balance', 100)
            pipe.incrby('expenses', 100)
            results = pipe.execute()
            print("转账成功")
            print(f"执行结果: {results}")
    else:
        print("余额不足")
except redis.WatchError:
    print("键值被修改，事务被取消")
finally:
    # 取消监控
    r.unwatch()
```

### 管道操作

管道用于批量执行命令，减少网络往返次数：

```python
# 使用管道批量执行命令
with r.pipeline() as pipe:
    # 添加多个命令
    for i in range(1000):
        pipe.set(f'key:{i}', f'value:{i}')
    
    # 执行所有命令
    results = pipe.execute()
    
    print(f"批量设置1000个键值对成功")

# 管道配合事务
with r.pipeline(transaction=True) as pipe:
    pipe.set('user:1:name', 'Alice')
    pipe.set('user:1:age', 30)
    pipe.hset('user:1', 'city', 'New York')
    pipe.lpush('user:1:posts', 'post1', 'post2')
    
    results = pipe.execute()
    print(f"事务执行结果: {results}")
```

### 发布/订阅功能

Redis的发布/订阅功能用于消息传递：

```python
# 发布者示例
import redis
import time

# 创建发布者连接
publisher = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 发布消息
def publish_message(channel, message):
    publisher.publish(channel, message)
    print(f"发布消息到频道{channel}: {message}")

# 发布示例消息
if __name__ == "__main__":
    for i in range(5):
        publish_message('news', f"News update {i}")
        time.sleep(1)
```

```python
# 订阅者示例
import redis

# 创建订阅者连接
subscriber = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 创建订阅对象
pubsub = subscriber.pubsub()

# 订阅频道
pubsub.subscribe('news')

# 订阅模式
pubsub.psubscribe('news:*')

print("订阅者已启动，等待消息...")

# 接收消息
for message in pubsub.listen():
    # 过滤掉订阅确认消息
    if message['type'] == 'message' or message['type'] == 'pmessage':
        if message['type'] == 'message':
            channel = message['channel']
        else:
            channel = message['channel']
            pattern = message['pattern']
        
        data = message['data']
        print(f"收到频道{channel}的消息: {data}")
        
        # 如果收到退出消息，停止订阅
        if data == 'exit':
            print("收到退出命令，停止订阅")
            break
```

### Lua脚本执行

Redis支持执行Lua脚本，用于原子性执行复杂操作：

```python
# 定义Lua脚本
script = """
local key = KEYS[1]
local field = ARGV[1]
local increment = tonumber(ARGV[2])

local current = redis.call('hget', key, field)
if not current then
    current = 0
else
    current = tonumber(current)
end

current = current + increment
redis.call('hset', key, field, current)

return current
"""

# 注册脚本
registered_script = r.register_script(script)

# 执行脚本
result = registered_script(keys=['user:1'], args=['visits', 1])
print(f"执行Lua脚本后: visits = {result}")

# 直接执行脚本
result = r.eval(script, 1, 'user:1', 'visits', 1)
print(f"直接执行Lua脚本后: visits = {result}")
```

### 连接池配置

```python
import redis

# 配置连接池
pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    db=0,
    password=None,
    decode_responses=True,
    max_connections=100,  # 最大连接数
    socket_keepalive=True,  # 启用TCP keepalive
    socket_timeout=30,  # 套接字超时时间（秒）
    socket_connect_timeout=10,  # 连接超时时间（秒）
    retry_on_timeout=False,  # 超时是否重试
    retry_on_error=[redis.exceptions.ConnectionError, redis.exceptions.TimeoutError]  # 出错重试的异常类型
)

# 使用连接池
r = redis.Redis(connection_pool=pool)

# 测试连接
print("Redis连接池配置成功")
print(f"Redis服务器信息: {r.info('server')}")
```

### 哨兵模式支持

```python
import redis

# 哨兵配置
sentinels = [
    ('localhost', 26379),
    ('localhost', 26380),
    ('localhost', 26381)
]

# 创建哨兵连接
from redis.sentinel import Sentinel
sentinel = Sentinel(sentinels, socket_timeout=0.1, decode_responses=True)

# 获取主服务器连接
master = sentinel.master_for('mymaster', socket_timeout=0.1)

# 获取从服务器连接
slave = sentinel.slave_for('mymaster', socket_timeout=0.1)

# 使用主服务器（写操作）
master.set('key', 'value')
print("主服务器写入成功")

# 使用从服务器（读操作）
value = slave.get('key')
print(f"从服务器读取成功: {value}")
```

### 集群支持

```python
import redis

# 集群配置
startup_nodes = [
    {'host': 'localhost', 'port': 7000},
    {'host': 'localhost', 'port': 7001},
    {'host': 'localhost', 'port': 7002}
]

# 创建集群连接
from rediscluster import RedisCluster

# 注意：需要安装rediscluster模块
# pip install redis-py-cluster

rc = RedisCluster(
    startup_nodes=startup_nodes,
    decode_responses=True,
    skip_full_coverage_check=True  # 跳过集群完整性检查（开发环境使用）
)

# 使用集群
rc.set('key', 'value')
value = rc.get('key')
print(f"集群操作成功: {value}")
```

## 实际应用示例

### 示例1：缓存系统

```python
import redis
import time

# 创建Redis连接
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 缓存装饰器
def cache(key_pattern, expire_time=3600):
    """缓存装饰器
    
    Args:
        key_pattern: 缓存键模式，使用{0}、{1}等占位符
        expire_time: 过期时间（秒）
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 生成缓存键
            key = key_pattern.format(*args, **kwargs)
            
            # 尝试从缓存获取
            cached_value = r.get(key)
            if cached_value is not None:
                print(f"从缓存获取结果: {cached_value}")
                return cached_value
            
            # 调用原始函数
            result = func(*args, **kwargs)
            
            # 存储到缓存
            r.setex(key, expire_time, result)
            print(f"结果存储到缓存: {key}")
            
            return result
        return wrapper
    return decorator

# 示例函数
@cache('fibonacci:{0}', expire_time=30)
def fibonacci(n):
    """计算斐波那契数列"""
    print(f"计算斐波那契数列: {n}")
    time.sleep(1)  # 模拟耗时操作
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 测试缓存装饰器
if __name__ == "__main__":
    print("第一次计算斐波那契数列(10):")
    start_time = time.time()
    result = fibonacci(10)
    end_time = time.time()
    print(f"结果: {result}, 耗时: {end_time - start_time:.2f}秒")
    
    print("\n第二次计算斐波那契数列(10):")
    start_time = time.time()
    result = fibonacci(10)
    end_time = time.time()
    print(f"结果: {result}, 耗时: {end_time - start_time:.2f}秒")
    
    print("\n计算斐波那契数列(11):")
    start_time = time.time()
    result = fibonacci(11)
    end_time = time.time()
    print(f"结果: {result}, 耗时: {end_time - start_time:.2f}秒")
```

### 示例2：计数器系统

```python
import redis
import time
from threading import Thread

# 创建Redis连接
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

class Counter:
    def __init__(self, name, redis_conn):
        self.name = name
        self.redis_conn = redis_conn
        self.key = f'counter:{name}'
    
    def increment(self, amount=1):
        """递增计数器"""
        return self.redis_conn.incrby(self.key, amount)
    
    def decrement(self, amount=1):
        """递减计数器"""
        return self.redis_conn.decrby(self.key, amount)
    
    def get_value(self):
        """获取计数器当前值"""
        value = self.redis_conn.get(self.key)
        return int(value) if value is not None else 0
    
    def reset(self):
        """重置计数器"""
        return self.redis_conn.delete(self.key)
    
    def increment_with_expire(self, amount=1, expire_time=3600):
        """递增计数器并设置过期时间"""
        # 使用Lua脚本确保原子性
        script = """
        local key = KEYS[1]
        local amount = tonumber(ARGV[1])
        local expire_time = tonumber(ARGV[2])
        
        local current = redis.call('incrby', key, amount)
        redis.call('expire', key, expire_time)
        
        return current
        """
        
        return self.redis_conn.eval(script, 1, self.key, amount, expire_time)

# 测试计数器
if __name__ == "__main__":
    # 创建计数器
    page_views = Counter('page_views', r)
    
    # 重置计数器
    page_views.reset()
    print("计数器已重置")
    
    # 递增计数器
    for i in range(10):
        value = page_views.increment()
        print(f"递增后的值: {value}")
    
    # 递减计数器
    value = page_views.decrement(3)
    print(f"递减3后的值: {value}")
    
    # 获取当前值
    value = page_views.get_value()
    print(f"当前值: {value}")
    
    # 递增并设置过期时间
    value = page_views.increment_with_expire(5, 60)
    print(f"递增5并设置60秒过期后的值: {value}")
    
    # 多线程测试
    def increment_counter(counter, times):
        for _ in range(times):
            counter.increment()
    
    print("\n多线程测试:")
    counter = Counter('thread_test', r)
    counter.reset()
    
    threads = []
    for i in range(5):
        thread = Thread(target=increment_counter, args=(counter, 200))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    final_value = counter.get_value()
    print(f"最终值: {final_value}, 预期值: 1000")
```

### 示例3：会话管理

```python
import redis
import uuid
import time

# 创建Redis连接
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

class SessionManager:
    def __init__(self, redis_conn, session_timeout=3600):
        self.redis_conn = redis_conn
        self.session_timeout = session_timeout
    
    def create_session(self, user_id, user_data=None):
        """创建会话"""
        # 生成会话ID
        session_id = str(uuid.uuid4())
        
        # 会话数据
        session_data = {
            'user_id': user_id,
            'created_at': time.time(),
            'last_accessed': time.time()
        }
        
        # 添加用户数据
        if user_data:
            session_data.update(user_data)
        
        # 存储会话数据
        key = f'session:{session_id}'
        self.redis_conn.hmset(key, session_data)
        
        # 设置过期时间
        self.redis_conn.expire(key, self.session_timeout)
        
        return session_id
    
    def get_session(self, session_id):
        """获取会话数据"""
        key = f'session:{session_id}'
        session_data = self.redis_conn.hgetall(key)
        
        if not session_data:
            return None
        
        # 更新最后访问时间
        self.redis_conn.hset(key, 'last_accessed', time.time())
        
        # 刷新过期时间
        self.redis_conn.expire(key, self.session_timeout)
        
        # 转换数据类型
        if 'user_id' in session_data:
            session_data['user_id'] = int(session_data['user_id'])
        if 'created_at' in session_data:
            session_data['created_at'] = float(session_data['created_at'])
        if 'last_accessed' in session_data:
            session_data['last_accessed'] = float(session_data['last_accessed'])
        
        return session_data
    
    def update_session(self, session_id, data):
        """更新会话数据"""
        key = f'session:{session_id}'
        
        # 检查会话是否存在
        if not self.redis_conn.exists(key):
            return False
        
        # 更新会话数据
        self.redis_conn.hmset(key, data)
        
        # 更新最后访问时间
        self.redis_conn.hset(key, 'last_accessed', time.time())
        
        # 刷新过期时间
        self.redis_conn.expire(key, self.session_timeout)
        
        return True
    
    def delete_session(self, session_id):
        """删除会话"""
        key = f'session:{session_id}'
        return self.redis_conn.delete(key) > 0
    
    def get_user_sessions(self, user_id):
        """获取用户的所有会话"""
        # 注意：这种方法在生产环境中效率不高，应该使用另一种数据结构来跟踪用户的所有会话
        sessions = []
        
        # 获取所有会话键
        session_keys = self.redis_conn.keys('session:*')
        
        for key in session_keys:
            session_data = self.redis_conn.hgetall(key)
            if session_data and session_data.get('user_id') == str(user_id):
                # 转换会话ID
                session_id = key.split(':')[1]
                session_data['session_id'] = session_id
                
                # 转换数据类型
                if 'user_id' in session_data:
                    session_data['user_id'] = int(session_data['user_id'])
                if 'created_at' in session_data:
                    session_data['created_at'] = float(session_data['created_at'])
                if 'last_accessed' in session_data:
                    session_data['last_accessed'] = float(session_data['last_accessed'])
                
                sessions.append(session_data)
        
        return sessions

# 测试会话管理器
if __name__ == "__main__":
    # 创建会话管理器
    session_manager = SessionManager(r, session_timeout=30)  # 30秒过期
    
    # 创建会话
    user_data = {
        'username': 'alice',
        'email': 'alice@example.com',
        'role': 'user'
    }
    
    session_id = session_manager.create_session(1, user_data)
    print(f"创建会话成功: {session_id}")
    
    # 获取会话
    session_data = session_manager.get_session(session_id)
    print(f"\n获取会话成功: {session_data}")
    
    # 更新会话
    update_data = {
        'role': 'admin'
    }
    
    success = session_manager.update_session(session_id, update_data)
    if success:
        print("\n更新会话成功")
        session_data = session_manager.get_session(session_id)
        print(f"更新后的会话: {session_data}")
    else:
        print("\n更新会话失败")
    
    # 获取用户的所有会话
    user_sessions = session_manager.get_user_sessions(1)
    print(f"\n用户1的所有会话: {user_sessions}")
    
    # 测试会话过期
    print("\n等待35秒测试会话过期...")
    time.sleep(35)
    
    session_data = session_manager.get_session(session_id)
    if session_data:
        print(f"会话未过期: {session_data}")
    else:
        print("会话已过期")
    
    # 删除会话
    success = session_manager.delete_session(session_id)
    if success:
        print("\n删除会话成功")
    else:
        print("\n删除会话失败")
```

## 最佳实践

1. **使用连接池**：使用连接池管理Redis连接，减少连接建立和关闭的开销
2. **设置超时时间**：为Redis连接和命令设置超时时间，避免阻塞
3. **合理使用数据结构**：根据业务需求选择合适的数据结构（字符串、哈希、列表、集合、有序集合等）
4. **设置键过期时间**：为临时数据设置过期时间，避免内存泄漏
5. **使用管道批量执行命令**：减少网络往返次数，提高性能
6. **使用事务保证原子性**：对需要原子性执行的多个命令使用事务
7. **监控Redis性能**：使用INFO命令监控Redis性能指标
8. **合理配置内存**：根据业务需求配置Redis的最大内存和淘汰策略
9. **使用Lua脚本**：对复杂操作使用Lua脚本，减少网络往返次数并保证原子性
10. **安全配置**：设置密码、限制访问IP、使用SSL等

## 与其他模块的关系

- **SQLAlchemy/ORM**：Redis可作为缓存层，与关系型数据库配合使用
- **Celery**：Redis可作为Celery的消息代理和结果后端
- **Flask/Django**：Redis可作为Flask或Django的缓存后端
- **pandas**：可以将Redis数据转换为pandas DataFrame进行数据分析
- **asyncio**：redis模块支持异步操作（redis-py >= 4.0）

## 总结

redis模块是Python中与Redis数据库交互的核心模块，提供了丰富的功能和接口。它支持所有Redis命令和数据结构，包括字符串、哈希、列表、集合、有序集合等。

redis模块的高级功能包括事务管理、管道操作、发布/订阅功能、Lua脚本执行、连接池管理、哨兵模式和集群支持等。这些功能使得redis模块能够满足各种复杂的业务需求。

在实际应用中，redis模块常用于缓存系统、计数器系统、会话管理、消息队列等场景。使用redis模块时，应该遵循最佳实践，如使用连接池、设置超时时间、合理使用数据结构、设置键过期时间等，确保系统的性能和稳定性。

与其他数据库相比，Redis具有以下优点：

- 高性能（内存操作）
- 支持多种数据结构
- 丰富的功能（事务、管道、发布/订阅等）
- 易于扩展（集群支持）
- 低延迟

但它也有一些限制：

- 内存成本高
- 数据持久化相对复杂
- 不支持复杂的查询操作

总的来说，redis模块是Python中处理缓存、计数器、会话管理等场景的强大工具，它可以帮助开发者构建高性能、可扩展的应用程序。