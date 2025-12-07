# psycopg2模块详解

psycopg2是Python中用于连接PostgreSQL数据库的第三方库，它是Python和PostgreSQL之间最流行的适配器之一。psycopg2实现了Python数据库API规范(Python DB API 2.0)，提供了与PostgreSQL数据库交互的高效接口。

## 模块概述

psycopg2模块主要提供以下功能：

- 连接PostgreSQL数据库
- 创建和管理游标
- 执行SQL查询（SELECT、INSERT、UPDATE、DELETE）
- 事务处理
- 参数化查询
- 错误处理
- 连接池支持
- 二进制数据支持
- 大对象处理
- 异步支持（通过扩展模块）

## 安装

psycopg2不是Python标准库，需要使用pip安装：

```bash
pip install psycopg2-binary
```

**注意：** psycopg2-binary是预编译的二进制包，包含了所有依赖，适合快速安装和开发使用。如果需要自定义编译或在生产环境中使用，可以安装psycopg2：

```bash
pip install psycopg2
```

安装psycopg2需要PostgreSQL开发文件（libpq-dev），在Ubuntu上可以使用以下命令安装：

```bash
sudo apt-get install libpq-dev
```

## 基本用法

### 导入模块

```python
import psycopg2
```

### 连接数据库

使用`connect()`函数连接到PostgreSQL数据库。需要提供数据库的主机名、用户名、密码、数据库名等参数。

```python
# 连接数据库
try:
    conn = psycopg2.connect(
        host='localhost',      # 数据库主机地址
        user='postgres',       # 数据库用户名
        password='password',   # 数据库密码
        dbname='test_db',      # 数据库名称
        port=5432,             # 数据库端口（默认5432）
        # sslmode='require'     # SSL模式（可选）
    )
    print("数据库连接成功")
except psycopg2.Error as e:
    print(f"数据库连接失败: {e}")
```

### 创建游标

游标是用于执行SQL语句和获取结果的对象。

```python
# 创建游标对象
with conn.cursor() as cursor:
    print("游标创建成功")
```

### 创建表

使用`execute()`方法执行SQL语句创建表。

```python
# 创建表
try:
    with conn.cursor() as cursor:
        # 创建表的SQL语句
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            age INTEGER,
            email VARCHAR(100) UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        '''
        # 执行SQL语句
        cursor.execute(create_table_sql)
    # 提交事务
    conn.commit()
    print("表创建成功")
except psycopg2.Error as e:
    print(f"创建表失败: {e}")
    conn.rollback()
```

### 插入数据

#### 单条插入

```python
# 插入单条数据
try:
    with conn.cursor() as cursor:
        # SQL插入语句
        sql = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)"
        # 执行SQL语句
        cursor.execute(sql, ('Alice', 30, 'alice@example.com'))
    # 提交事务
    conn.commit()
    print(f"插入成功，影响行数: {cursor.rowcount}")
except psycopg2.Error as e:
    print(f"插入失败: {e}")
    conn.rollback()
```

#### 批量插入

```python
# 批量插入数据
try:
    with conn.cursor() as cursor:
        # SQL插入语句
        sql = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)"
        # 批量数据
        data = [
            ('Bob', 25, 'bob@example.com'),
            ('Charlie', 35, 'charlie@example.com'),
            ('David', 40, 'david@example.com'),
            ('Eve', 28, 'eve@example.com')
        ]
        # 执行批量插入
        cursor.executemany(sql, data)
    # 提交事务
    conn.commit()
    print(f"批量插入成功，影响行数: {cursor.rowcount}")
except psycopg2.Error as e:
    print(f"批量插入失败: {e}")
    conn.rollback()
```

### 查询数据

#### 查询所有数据

```python
# 查询所有数据
try:
    with conn.cursor() as cursor:
        # SQL查询语句
        sql = "SELECT * FROM users"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有结果
        results = cursor.fetchall()
        
        print("所有用户数据:")
        for row in results:
            print(f"ID: {row[0]}, 姓名: {row[1]}, 年龄: {row[2]}, 邮箱: {row[3]}, 创建时间: {row[4]}")
except psycopg2.Error as e:
    print(f"查询失败: {e}")
```

#### 查询单条数据

```python
# 查询单条数据
try:
    with conn.cursor() as cursor:
        # SQL查询语句
        sql = "SELECT * FROM users WHERE id = %s"
        # 执行SQL语句
        cursor.execute(sql, (1,))
        # 获取单条结果
        result = cursor.fetchone()
        
        if result:
            print(f"查询结果: ID={result[0]}, 姓名={result[1]}, 年龄={result[2]}")
        else:
            print("未找到数据")
except psycopg2.Error as e:
    print(f"查询失败: {e}")
```

#### 按条件查询

```python
# 按条件查询
try:
    with conn.cursor() as cursor:
        # SQL查询语句
        sql = "SELECT * FROM users WHERE age > %s AND age < %s ORDER BY age ASC"
        # 执行SQL语句
        cursor.execute(sql, (25, 40))
        # 获取结果
        results = cursor.fetchall()
        
        print("年龄在25-40之间的用户:")
        for row in results:
            print(f"ID: {row[0]}, 姓名: {row[1]}, 年龄: {row[2]}")
except psycopg2.Error as e:
    print(f"查询失败: {e}")
```

#### 分页查询

```python
# 分页查询
try:
    page = 1       # 当前页码
    per_page = 2   # 每页数量
    offset = (page - 1) * per_page
    
    with conn.cursor() as cursor:
        # SQL查询语句
        sql = "SELECT * FROM users ORDER BY created_at DESC LIMIT %s OFFSET %s"
        # 执行SQL语句
        cursor.execute(sql, (per_page, offset))
        # 获取结果
        results = cursor.fetchall()
        
        print(f"第{page}页用户数据:")
        for row in results:
            print(f"ID: {row[0]}, 姓名: {row[1]}, 创建时间: {row[4]}")
except psycopg2.Error as e:
    print(f"查询失败: {e}")
```

### 更新数据

```python
# 更新数据
try:
    with conn.cursor() as cursor:
        # SQL更新语句
        sql = "UPDATE users SET age = %s, email = %s WHERE name = %s"
        # 执行SQL语句
        cursor.execute(sql, (31, 'alice_new@example.com', 'Alice'))
    # 提交事务
    conn.commit()
    print(f"更新成功，影响行数: {cursor.rowcount}")
except psycopg2.Error as e:
    print(f"更新失败: {e}")
    conn.rollback()
```

### 删除数据

```python
# 删除数据
try:
    with conn.cursor() as cursor:
        # SQL删除语句
        sql = "DELETE FROM users WHERE name = %s"
        # 执行SQL语句
        cursor.execute(sql, ('David',))
    # 提交事务
    conn.commit()
    print(f"删除成功，影响行数: {cursor.rowcount}")
except psycopg2.Error as e:
    print(f"删除失败: {e}")
    conn.rollback()
```

### 关闭连接

使用完数据库后，应该关闭连接。

```python
# 关闭连接
conn.close()
print("数据库连接已关闭")
```

## 高级功能

### 事务处理

psycopg2默认是自动提交事务的，你可以通过设置`autocommit=False`来手动管理事务。

```python
# 手动管理事务
try:
    # 关闭自动提交
    conn.autocommit = False
    
    with conn.cursor() as cursor:
        # 执行多个操作
        cursor.execute("INSERT INTO users (name, age, email) VALUES (%s, %s, %s)", ('Frank', 33, 'frank@example.com'))
        cursor.execute("UPDATE users SET age = age + 1 WHERE name = 'Bob'")
        cursor.execute("DELETE FROM users WHERE name = 'Eve'")
    
    # 提交事务
    conn.commit()
    print("事务提交成功")
except psycopg2.Error as e:
    # 回滚事务
    conn.rollback()
    print(f"事务回滚: {e}")
finally:
    # 恢复自动提交
    conn.autocommit = True
```

### 序列值获取

对于使用SERIAL类型的主键，可以使用`RETURNING`子句获取插入的ID值。

```python
# 获取插入的ID值
try:
    with conn.cursor() as cursor:
        # 使用RETURNING子句
        sql = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s) RETURNING id"
        cursor.execute(sql, ('Grace', 29, 'grace@example.com'))
        user_id = cursor.fetchone()[0]
    
    conn.commit()
    print(f"插入成功，用户ID: {user_id}")
except psycopg2.Error as e:
    conn.rollback()
    print(f"插入失败: {e}")
```

### 批量插入优化

对于大量数据的插入，可以使用`execute_values()`函数（psycopg2.extras模块）进行优化。

```python
from psycopg2.extras import execute_values

# 批量插入优化
try:
    with conn.cursor() as cursor:
        # 大量数据
        data = [(f'User_{i}', 20 + i % 30, f'user{i}@example.com') for i in range(1000)]
        
        # 使用execute_values()函数
        sql = "INSERT INTO users (name, age, email) VALUES %s"
        execute_values(cursor, sql, data)
    
    conn.commit()
    print(f"批量插入成功，影响行数: 1000")
except psycopg2.Error as e:
    conn.rollback()
    print(f"批量插入失败: {e}")
```

### 服务器端游标

对于大量数据的查询，可以使用服务器端游标（named cursor）来减少内存使用。

```python
# 使用服务器端游标
try:
    # 创建命名游标
    with conn.cursor(name='large_result_set') as cursor:
        # 执行查询
        cursor.execute("SELECT * FROM users")
        
        # 一次获取100行
        while True:
            rows = cursor.fetchmany(100)
            if not rows:
                break
            
            # 处理数据
            for row in rows:
                print(f"ID: {row[0]}, 姓名: {row[1]}")
                # 这里可以添加更多处理逻辑
except psycopg2.Error as e:
    print(f"查询失败: {e}")
```

### 字典游标

使用`DictCursor`可以返回字典类型的结果，其中键是列名。

```python
from psycopg2.extras import DictCursor

# 使用字典游标
try:
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        # 执行查询
        cursor.execute("SELECT * FROM users LIMIT 3")
        results = cursor.fetchall()
        
        print("使用字典游标:")
        for row in results:
            print(f"ID: {row['id']}, 姓名: {row['name']}, 邮箱: {row['email']}")
except psycopg2.Error as e:
    print(f"查询失败: {e}")
```

### 大对象处理

对于大文件（如图像、视频等），可以使用PostgreSQL的大对象功能。

```python
# 大对象处理
try:
    with conn.cursor() as cursor:
        # 创建大对象
        cursor.execute("SELECT lo_create(0)")
        oid = cursor.fetchone()[0]
        
        # 写入数据
        lobj = conn.lobject(oid, mode='wb')
        lobj.write(b'Hello, PostgreSQL Large Object!')
        lobj.close()
        
        # 保存大对象ID到表中
        cursor.execute("INSERT INTO files (name, content_oid) VALUES (%s, %s)", ('test.txt', oid))
    
    conn.commit()
    print(f"大对象创建成功，OID: {oid}")
    
    # 读取大对象
    with conn.cursor() as cursor:
        cursor.execute("SELECT content_oid FROM files WHERE name = %s", ('test.txt',))
        oid = cursor.fetchone()[0]
        
        lobj = conn.lobject(oid, mode='rb')
        content = lobj.read()
        lobj.close()
        
        print(f"读取大对象内容: {content.decode('utf-8')}")
        
        # 删除大对象
        cursor.execute("SELECT lo_unlink(%s)", (oid,))
        cursor.execute("DELETE FROM files WHERE name = %s", ('test.txt',))
    
    conn.commit()
    print("大对象删除成功")
except psycopg2.Error as e:
    conn.rollback()
    print(f"大对象处理失败: {e}")
```

**注意：** 上面的示例假设已创建了files表：

```sql
CREATE TABLE IF NOT EXISTS files (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    content_oid OID NOT NULL
)
```

### 连接池

对于高并发应用，使用连接池可以提高性能。psycopg2本身不提供连接池功能，但可以与第三方库如`psycopg2-pool`或`DBUtils`一起使用。

```bash
pip install psycopg2-pool
```

```python
from psycopg2.pool import SimpleConnectionPool

# 创建连接池
pool = SimpleConnectionPool(
    minconn=1,           # 最小连接数
    maxconn=10,          # 最大连接数
    host='localhost',
    user='postgres',
    password='password',
    dbname='test_db',
    port=5432
)

# 从连接池获取连接
try:
    conn = pool.getconn()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users LIMIT 2")
        results = cursor.fetchall()
        for row in results:
            print(f"ID: {row[0]}, 姓名: {row[1]}")
finally:
    # 释放连接到连接池
    pool.putconn(conn)

# 关闭连接池
pool.closeall()
```

### 异步支持

psycopg2提供了异步扩展`psycopg2.extensions.async_connections`，可以在异步应用中使用。

```bash
pip install psycopg2-binary asyncio
```

```python
import asyncio
from psycopg2.extensions import connection
from psycopg2.extras import DictCursor

async def get_users():
    """异步获取用户数据"""
    # 创建异步连接
    conn = connection()
    conn.connect(
        host='localhost',
        user='postgres',
        password='password',
        dbname='test_db',
        port=5432
    )
    
    try:
        # 创建异步游标
        cursor = conn.cursor(cursor_factory=DictCursor)
        await asyncio.to_thread(cursor.execute, "SELECT * FROM users LIMIT 5")
        
        # 获取结果
        results = await asyncio.to_thread(cursor.fetchall)
        
        print("异步获取用户数据:")
        for row in results:
            print(f"ID: {row['id']}, 姓名: {row['name']}")
    finally:
        # 关闭连接
        conn.close()

# 运行异步函数
asyncio.run(get_users())
```

**注意：** 上面的示例是一个简单的异步包装，更完整的异步支持可以使用`asyncpg`库。

## 实际应用示例

### 示例1：用户管理系统

```python
import psycopg2
from psycopg2.extras import DictCursor, execute_values

class UserManager:
    def __init__(self, db_config):
        self.db_config = db_config
        self._create_tables()
    
    def _connect(self):
        """创建数据库连接"""
        return psycopg2.connect(**self.db_config)
    
    def _create_tables(self):
        """创建表结构"""
        try:
            conn = self._connect()
            with conn.cursor() as cursor:
                # 创建用户表
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    email VARCHAR(100) UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_login TIMESTAMP
                )
                ''')
                
                # 创建角色表
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS roles (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) UNIQUE NOT NULL
                )
                ''')
                
                # 创建用户角色关系表
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_roles (
                    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                    role_id INTEGER REFERENCES roles(id) ON DELETE CASCADE,
                    PRIMARY KEY (user_id, role_id)
                )
                ''')
                
                # 插入默认角色
                cursor.execute("INSERT INTO roles (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", ('admin',))
                cursor.execute("INSERT INTO roles (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", ('user',))
            
            conn.commit()
            print("表结构创建成功")
        except psycopg2.Error as e:
            print(f"创建表结构失败: {e}")
        finally:
            conn.close()
    
    def create_user(self, username, password, email=None):
        """创建用户"""
        try:
            conn = self._connect()
            with conn.cursor() as cursor:
                # 插入用户
                cursor.execute(
                    "INSERT INTO users (username, password, email) VALUES (%s, %s, %s) RETURNING id",
                    (username, password, email)
                )
                user_id = cursor.fetchone()[0]
                
                # 分配默认角色
                cursor.execute("SELECT id FROM roles WHERE name = 'user'")
                role_id = cursor.fetchone()[0]
                cursor.execute(
                    "INSERT INTO user_roles (user_id, role_id) VALUES (%s, %s)",
                    (user_id, role_id)
                )
            
            conn.commit()
            print(f"用户创建成功，ID: {user_id}")
            return True, user_id
        except psycopg2.Error as e:
            print(f"创建用户失败: {e}")
            return False, None
        finally:
            conn.close()
    
    def get_user(self, user_id):
        """获取用户信息"""
        try:
            conn = self._connect()
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                # 获取用户基本信息
                cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
                user = cursor.fetchone()
                
                if not user:
                    return False, "用户不存在"
                
                # 获取用户角色
                cursor.execute('''
                SELECT r.name FROM roles r JOIN user_roles ur ON r.id = ur.role_id WHERE ur.user_id = %s
                ''', (user_id,))
                roles = [row[0] for row in cursor.fetchall()]
                user['roles'] = roles
            
            return True, user
        except psycopg2.Error as e:
            print(f"获取用户信息失败: {e}")
            return False, None
        finally:
            conn.close()
    
    def batch_create_users(self, users_data):
        """批量创建用户"""
        try:
            conn = self._connect()
            with conn.cursor() as cursor:
                # 批量插入用户
                sql = "INSERT INTO users (username, password, email) VALUES %s RETURNING id"
                execute_values(cursor, sql, users_data)
                user_ids = [row[0] for row in cursor.fetchall()]
                
                # 分配默认角色
                cursor.execute("SELECT id FROM roles WHERE name = 'user'")
                role_id = cursor.fetchone()[0]
                
                # 批量插入用户角色关系
                role_data = [(user_id, role_id) for user_id in user_ids]
                sql = "INSERT INTO user_roles (user_id, role_id) VALUES %s"
                execute_values(cursor, sql, role_data)
            
            conn.commit()
            print(f"批量创建用户成功，创建了 {len(user_ids)} 个用户")
            return True, user_ids
        except psycopg2.Error as e:
            print(f"批量创建用户失败: {e}")
            return False, None
        finally:
            conn.close()

# 测试
if __name__ == "__main__":
    # 数据库配置
    db_config = {
        'host': 'localhost',
        'user': 'postgres',
        'password': 'password',
        'dbname': 'test_db',
        'port': 5432
    }
    
    user_manager = UserManager(db_config)
    
    # 创建单个用户
    user_manager.create_user('alice', 'password123', 'alice@example.com')
    
    # 批量创建用户
    users_data = [
        ('bob', 'password456', 'bob@example.com'),
        ('charlie', 'password789', 'charlie@example.com'),
        ('david', 'password101', 'david@example.com')
    ]
    user_manager.batch_create_users(users_data)
    
    # 获取用户信息
    success, user = user_manager.get_user(1)
    if success:
        print(f"用户信息: {user}")
```

### 示例2：在线商店数据库

```python
import psycopg2
from psycopg2.extras import DictCursor
from datetime import datetime

class StoreDB:
    def __init__(self, db_config):
        self.db_config = db_config
        self.conn = psycopg2.connect(**db_config)
        self._create_tables()
    
    def __del__(self):
        self.conn.close()
    
    def _create_tables(self):
        """创建表结构"""
        try:
            with self.conn.cursor() as cursor:
                # 创建产品表
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT,
                    price NUMERIC(10, 2) NOT NULL,
                    stock INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                ''')
                
                # 创建订单表
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS orders (
                    id SERIAL PRIMARY KEY,
                    customer_name VARCHAR(100) NOT NULL,
                    customer_email VARCHAR(100),
                    total_amount NUMERIC(10, 2) NOT NULL,
                    status VARCHAR(20) DEFAULT 'pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                ''')
                
                # 创建订单详情表
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS order_items (
                    id SERIAL PRIMARY KEY,
                    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
                    product_id INTEGER REFERENCES products(id) ON DELETE SET NULL,
                    quantity INTEGER NOT NULL,
                    unit_price NUMERIC(10, 2) NOT NULL
                )
                ''')
            
            self.conn.commit()
            print("商店表结构创建成功")
        except psycopg2.Error as e:
            print(f"创建商店表结构失败: {e}")
    
    def add_product(self, name, description, price, stock):
        """添加产品"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO products (name, description, price, stock) VALUES (%s, %s, %s, %s) RETURNING id",
                    (name, description, price, stock)
                )
                product_id = cursor.fetchone()[0]
            
            self.conn.commit()
            print(f"产品添加成功，ID: {product_id}")
            return True, product_id
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"添加产品失败: {e}")
            return False, None
    
    def create_order(self, customer_name, customer_email, items):
        """创建订单"""
        try:
            # 开始事务
            self.conn.autocommit = False
            
            with self.conn.cursor() as cursor:
                # 计算总金额
                total_amount = 0
                for product_id, quantity in items.items():
                    # 查询产品信息
                    cursor.execute("SELECT price, stock FROM products WHERE id = %s", (product_id,))
                    product = cursor.fetchone()
                    if not product:
                        raise ValueError(f"产品不存在: {product_id}")
                    
                    price, stock = product
                    if stock < quantity:
                        raise ValueError(f"产品库存不足: {product_id}")
                    
                    total_amount += price * quantity
                
                # 创建订单
                cursor.execute(
                    "INSERT INTO orders (customer_name, customer_email, total_amount) VALUES (%s, %s, %s) RETURNING id",
                    (customer_name, customer_email, total_amount)
                )
                order_id = cursor.fetchone()[0]
                
                # 添加订单项
                for product_id, quantity in items.items():
                    # 查询产品价格
                    cursor.execute("SELECT price FROM products WHERE id = %s", (product_id,))
                    unit_price = cursor.fetchone()[0]
                    
                    # 添加订单项
                    cursor.execute(
                        "INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (%s, %s, %s, %s)",
                        (order_id, product_id, quantity, unit_price)
                    )
                    
                    # 更新产品库存
                    cursor.execute("UPDATE products SET stock = stock - %s WHERE id = %s", (quantity, product_id))
            
            # 提交事务
            self.conn.commit()
            print(f"订单创建成功，ID: {order_id}")
            return True, order_id
        except (psycopg2.Error, ValueError) as e:
            # 回滚事务
            self.conn.rollback()
            print(f"创建订单失败: {e}")
            return False, None
        finally:
            # 恢复自动提交
            self.conn.autocommit = True
    
    def get_order(self, order_id):
        """获取订单详情"""
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cursor:
                # 获取订单基本信息
                cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
                order = cursor.fetchone()
                
                if not order:
                    return False, "订单不存在"
                
                # 获取订单详情
                cursor.execute('''
                SELECT oi.*, p.name as product_name
                FROM order_items oi
                JOIN products p ON oi.product_id = p.id
                WHERE oi.order_id = %s
                ''', (order_id,))
                items = cursor.fetchall()
                order['items'] = items
            
            return True, order
        except psycopg2.Error as e:
            print(f"获取订单详情失败: {e}")
            return False, None

# 测试
if __name__ == "__main__":
    # 数据库配置
    db_config = {
        'host': 'localhost',
        'user': 'postgres',
        'password': 'password',
        'dbname': 'test_db',
        'port': 5432
    }
    
    store_db = StoreDB(db_config)
    
    # 添加产品
    store_db.add_product('笔记本电脑', '高性能笔记本电脑', 5999.99, 10)
    store_db.add_product('手机', '智能手机', 2999.99, 50)
    store_db.add_product('耳机', '无线耳机', 299.99, 100)
    
    # 创建订单
    items = {
        1: 1,  # 1台笔记本电脑
        3: 2   # 2个耳机
    }
    success, order_id = store_db.create_order('John Doe', 'john@example.com', items)
    
    if success:
        # 获取订单详情
        success, order = store_db.get_order(order_id)
        if success:
            print("\n订单详情:")
            print(f"订单ID: {order['id']}")
            print(f"客户: {order['customer_name']}")
            print(f"邮箱: {order['customer_email']}")
            print(f"总金额: ${order['total_amount']}")
            print(f"状态: {order['status']}")
            print(f"创建时间: {order['created_at']}")
            print("\n订单项:")
            for item in order['items']:
                print(f"- {item['product_name']}: {item['quantity']}个 × ${item['unit_price']} = ${item['quantity'] * item['unit_price']}")
```

## 最佳实践

1. **使用参数化查询**：始终使用参数化查询，避免SQL注入攻击
2. **连接池**：对于高并发应用，使用连接池提高性能
3. **错误处理**：添加适当的错误处理，特别是在事务中
4. **关闭连接**：使用完数据库连接后，确保关闭连接
5. **事务管理**：对多个相关操作使用事务，确保数据一致性
6. **索引优化**：为经常查询的列创建索引，提高查询性能
7. **批量插入优化**：对于大量数据的插入，使用`execute_values()`函数
8. **服务器端游标**：对于大量数据的查询，使用服务器端游标减少内存使用
9. **使用RETURNING**：使用`RETURNING`子句获取插入的ID值
10. **避免N+1查询问题**：使用JOIN查询减少数据库查询次数
11. **定期备份**：定期备份数据库，防止数据丢失

## 与其他模块的关系

- **sqlalchemy**：sqlalchemy是一个ORM框架，可以与psycopg2一起使用，提供更高级的数据库操作
- **django.db**：Django框架的数据库模块可以配置使用psycopg2作为PostgreSQL的后端
- **flask_sqlalchemy**：Flask框架的扩展，可以与psycopg2一起使用，提供ORM功能
- **dataset**：dataset是一个简化数据库操作的库，可以基于psycopg2创建数据库和表
- **pandas**：pandas可以从PostgreSQL数据库读取数据并转换为DataFrame，进行数据分析

## 总结

psycopg2是Python中用于连接PostgreSQL数据库的第三方库，它是Python和PostgreSQL之间最流行的适配器之一。psycopg2实现了Python数据库API规范，提供了与PostgreSQL数据库交互的高效接口。

psycopg2模块的主要功能包括连接数据库、创建表、执行SQL查询、事务处理、参数化查询等。它还提供了高级功能，如批量插入优化、服务器端游标、字典游标、大对象处理等。

在实际应用中，psycopg2模块常用于用户管理系统、在线商店、内容管理系统等场景。使用psycopg2模块时，应该遵循最佳实践，如使用参数化查询、关闭连接、事务管理等，确保数据安全和性能。

与其他数据库系统相比，PostgreSQL具有以下优点：

- 强大的SQL支持
- 可靠性高
- 支持复杂查询和高级数据类型
- 开源免费
- 支持JSON数据类型
- 良好的并发性能

但它也有一些限制：

- 需要安装和配置PostgreSQL服务器
- 相比SQLite，配置和管理更复杂
- 对于小型应用，可能过于重量级

总的来说，psycopg2模块是Python中处理PostgreSQL数据库的理想选择，它简单易用，功能强大，可以满足大多数应用程序的需求。