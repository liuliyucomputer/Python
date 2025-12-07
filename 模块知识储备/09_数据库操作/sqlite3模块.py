# sqlite3模块详解

sqlite3模块是Python标准库中内置的轻量级数据库系统，无需额外安装即可使用。它提供了与SQLite数据库交互的接口，允许程序创建、访问和操作SQLite数据库文件。SQLite是一个自包含、零配置、事务性的SQL数据库引擎，数据存储在单个文件中，非常适合小型应用程序和原型开发。

## 模块概述

sqlite3模块主要提供以下功能：

- 连接SQLite数据库
- 创建表和索引
- 执行SQL查询（SELECT、INSERT、UPDATE、DELETE）
- 事务处理
- 参数化查询
- 游标对象管理
- 数据库备份和恢复

## 基本用法

### 导入模块

```python
import sqlite3
```

### 连接数据库

使用`connect()`函数连接到SQLite数据库。如果数据库文件不存在，它会自动创建一个新的数据库文件。

```python
# 连接到数据库文件（如果不存在则创建）
conn = sqlite3.connect('example.db')

# 连接到内存数据库（数据只在内存中，程序结束后消失）
# conn = sqlite3.connect(':memory:')
```

### 创建游标

游标是用于执行SQL语句和获取结果的对象。

```python
cursor = conn.cursor()
```

### 创建表

使用`execute()`方法执行SQL语句创建表。

```python
# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
''')

# 创建索引
cursor.execute('CREATE INDEX IF NOT EXISTS idx_users_email ON users(email)')

# 提交事务
conn.commit()
```

### 插入数据

#### 单条插入

```python
# 插入单条数据
cursor.execute("INSERT INTO users (name, age, email) VALUES ('Alice', 30, 'alice@example.com')")
conn.commit()
```

#### 参数化查询

**注意：这是一个重要的安全措施，防止SQL注入攻击**

```python
# 参数化插入（推荐）
user = ('Bob', 25, 'bob@example.com')
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", user)
conn.commit()

# 或者使用命名参数
user_data = {'name': 'Charlie', 'age': 35, 'email': 'charlie@example.com'}
cursor.execute("INSERT INTO users (name, age, email) VALUES (:name, :age, :email)", user_data)
conn.commit()
```

#### 批量插入

```python
# 批量插入
users = [
    ('David', 28, 'david@example.com'),
    ('Eve', 32, 'eve@example.com'),
    ('Frank', 40, 'frank@example.com')
]

cursor.executemany("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", users)
conn.commit()
```

### 查询数据

#### 查询所有数据

```python
# 查询所有数据
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

#### 查询单条数据

```python
# 查询单条数据
cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
row = cursor.fetchone()
print(row)
```

#### 按条件查询

```python
# 按条件查询
cursor.execute("SELECT * FROM users WHERE age > ?", (30,))
rows = cursor.fetchall()

print("年龄大于30的用户:")
for row in rows:
    print(row)
```

#### 查询部分列

```python
# 查询部分列
cursor.execute("SELECT name, email FROM users WHERE age BETWEEN ? AND ?", (25, 35))
rows = cursor.fetchall()

print("年龄在25-35之间的用户:")
for row in rows:
    print(f"姓名: {row[0]}, 邮箱: {row[1]}")
```

#### 分页查询

```python
# 分页查询（每页2条，第2页）
offset = (2 - 1) * 2
cursor.execute("SELECT * FROM users ORDER BY age DESC LIMIT ? OFFSET ?", (2, offset))
rows = cursor.fetchall()

print("第2页用户数据:")
for row in rows:
    print(row)
```

### 更新数据

```python
# 更新数据
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, 'Alice'))
conn.commit()

# 查看更新结果
cursor.execute("SELECT * FROM users WHERE name = 'Alice'")
print(f"更新后的Alice: {cursor.fetchone()}")
```

### 删除数据

```python
# 删除数据
cursor.execute("DELETE FROM users WHERE name = ?", ('Frank',))
conn.commit()

# 查看删除结果
cursor.execute("SELECT * FROM users WHERE name = 'Frank'")
print(f"删除Frank后: {cursor.fetchone()}")
```

### 使用上下文管理器

使用上下文管理器（with语句）可以自动管理连接和游标，无需手动关闭。

```python
# 使用上下文管理器连接数据库
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # 执行SQL语句
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

# 连接会在with块结束后自动关闭
```

## 高级功能

### 事务处理

SQLite默认会自动提交每个SQL语句，但你也可以手动管理事务。

```python
# 手动管理事务
try:
    # 开始事务（默认自动开始）
    cursor.execute("UPDATE users SET age = age + 1 WHERE name = 'Alice'")
    cursor.execute("UPDATE users SET age = age + 1 WHERE name = 'Bob'")
    
    # 提交事务
    conn.commit()
    print("事务提交成功")
except Exception as e:
    # 回滚事务
    conn.rollback()
    print(f"事务回滚: {e}")
```

### 数据库备份

```python
# 备份数据库
def backup_database(conn, backup_path):
    """备份SQLite数据库"""
    with sqlite3.connect(backup_path) as backup_conn:
        conn.backup(backup_conn)

# 使用
backup_database(conn, 'example_backup.db')
print("数据库备份成功")
```

### 自定义函数

你可以在SQL中使用自定义的Python函数。

```python
# 自定义函数
def calculate_age_category(age):
    if age < 18:
        return '未成年'
    elif age < 30:
        return '青年'
    elif age < 50:
        return '中年'
    else:
        return '老年'

# 注册自定义函数
conn.create_function('age_category', 1, calculate_age_category)

# 在SQL中使用自定义函数
cursor.execute("SELECT name, age, age_category(age) FROM users")
rows = cursor.fetchall()

print("用户年龄分类:")
for row in rows:
    print(f"姓名: {row[0]}, 年龄: {row[1]}, 分类: {row[2]}")
```

### 自定义聚合函数

你可以创建自定义的聚合函数。

```python
# 自定义聚合函数
class Average:
    def __init__(self):
        self.count = 0
        self.total = 0
    
    def step(self, value):
        if value is not None:
            self.total += value
            self.count += 1
    
    def finalize(self):
        if self.count == 0:
            return 0
        return self.total / self.count

# 注册自定义聚合函数
conn.create_aggregate('my_average', 1, Average)

# 在SQL中使用自定义聚合函数
cursor.execute("SELECT my_average(age) FROM users")
average_age = cursor.fetchone()[0]
print(f"用户平均年龄: {average_age:.2f}")
```

### 行工厂

行工厂允许你自定义查询结果的返回格式。

```python
# 使用字典作为行工厂
conn.row_factory = sqlite3.Row

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("使用字典行工厂:")
for row in rows:
    print(f"ID: {row['id']}, 姓名: {row['name']}, 年龄: {row['age']}, 邮箱: {row['email']}")

# 恢复默认行工厂
conn.row_factory = None
```

### 外键约束

默认情况下，SQLite不启用外键约束，你需要手动启用。

```python
# 启用外键约束
conn.execute("PRAGMA foreign_keys = ON")

# 创建部门表
cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

# 创建员工表，包含外键
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE SET NULL
)
''')

# 插入数据
cursor.execute("INSERT INTO departments (name) VALUES ('技术部')")
cursor.execute("INSERT INTO departments (name) VALUES ('市场部')")

cursor.execute("INSERT INTO employees (name, department_id) VALUES ('Alice', 1)")
cursor.execute("INSERT INTO employees (name, department_id) VALUES ('Bob', 2)")

conn.commit()

# 测试外键约束
print("测试外键约束:")
cursor.execute("SELECT e.name, d.name FROM employees e JOIN departments d ON e.department_id = d.id")
rows = cursor.fetchall()

for row in rows:
    print(f"员工: {row[0]}, 部门: {row[1]}")
```

## 实际应用示例

### 示例1：用户管理系统

```python
# 用户管理系统示例
import sqlite3

class UserManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_table()
    
    def _create_table(self):
        """创建用户表"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            ''')
    
    def add_user(self, username, password, email=None):
        """添加用户"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                    (username, password, email)
                )
                conn.commit()
                return True
            except sqlite3.IntegrityError:
                return False
    
    def get_user(self, user_id):
        """根据ID获取用户"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            return cursor.fetchone()
    
    def get_user_by_username(self, username):
        """根据用户名获取用户"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            return cursor.fetchone()
    
    def update_user(self, user_id, password=None, email=None):
        """更新用户信息"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            if password and email:
                cursor.execute(
                    "UPDATE users SET password = ?, email = ? WHERE id = ?",
                    (password, email, user_id)
                )
            elif password:
                cursor.execute(
                    "UPDATE users SET password = ? WHERE id = ?",
                    (password, user_id)
                )
            elif email:
                cursor.execute(
                    "UPDATE users SET email = ? WHERE id = ?",
                    (email, user_id)
                )
            else:
                return False
            
            conn.commit()
            return cursor.rowcount > 0
    
    def delete_user(self, user_id):
        """删除用户"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    def list_users(self, limit=10, offset=0):
        """列出用户（分页）"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users ORDER BY created_at DESC LIMIT ? OFFSET ?",
                (limit, offset)
            )
            return cursor.fetchall()

# 测试
user_manager = UserManager('user_management.db')

# 添加用户
user_manager.add_user('alice', 'password123', 'alice@example.com')
user_manager.add_user('bob', 'password456', 'bob@example.com')
user_manager.add_user('charlie', 'password789')

# 列出用户
print("所有用户:")
for user in user_manager.list_users():
    print(f"ID: {user['id']}, 用户名: {user['username']}, 邮箱: {user['email']}, 创建时间: {user['created_at']}")

# 获取用户
print("\n获取用户:")
user = user_manager.get_user_by_username('alice')
print(f"用户名: {user['username']}, 邮箱: {user['email']}")

# 更新用户
user_manager.update_user(user['id'], email='alice_new@example.com')
updated_user = user_manager.get_user(user['id'])
print(f"\n更新后的邮箱: {updated_user['email']}")

# 删除用户
user_manager.delete_user(user['id'])
print("\n删除用户后:")
for user in user_manager.list_users():
    print(f"ID: {user['id']}, 用户名: {user['username']}")
```

### 示例2：博客系统数据库

```python
# 博客系统数据库示例
import sqlite3

class BlogDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_tables()
    
    def _create_tables(self):
        """创建表结构"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # 创建用户表
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            ''')
            
            # 创建文章表
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author_id INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
            )
            ''')
            
            # 创建评论表
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                post_id INTEGER NOT NULL,
                author_id INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
                FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
            )
            ''')
    
    def create_post(self, title, content, author_id):
        """创建文章"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO posts (title, content, author_id) VALUES (?, ?, ?)",
                (title, content, author_id)
            )
            conn.commit()
            return cursor.lastrowid
    
    def get_post(self, post_id):
        """获取文章"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
            SELECT p.*, u.username as author_name
            FROM posts p
            JOIN users u ON p.author_id = u.id
            WHERE p.id = ?
            ''', (post_id,))
            return cursor.fetchone()
    
    def get_posts(self, limit=10, offset=0):
        """获取文章列表"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
            SELECT p.*, u.username as author_name
            FROM posts p
            JOIN users u ON p.author_id = u.id
            ORDER BY p.created_at DESC
            LIMIT ? OFFSET ?
            ''', (limit, offset))
            return cursor.fetchall()
    
    def add_comment(self, content, post_id, author_id):
        """添加评论"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO comments (content, post_id, author_id) VALUES (?, ?, ?)",
                (content, post_id, author_id)
            )
            conn.commit()
            return cursor.lastrowid
    
    def get_comments(self, post_id):
        """获取文章评论"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
            SELECT c.*, u.username as author_name
            FROM comments c
            JOIN users u ON c.author_id = u.id
            WHERE c.post_id = ?
            ORDER BY c.created_at DESC
            ''', (post_id,))
            return cursor.fetchall()

# 测试
blog_db = BlogDatabase('blog.db')

# 添加用户（这里简化处理，实际应该有密码哈希等）
with sqlite3.connect('blog.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", ('alice', 'alice@example.com', 'password123'))
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", ('bob', 'bob@example.com', 'password456'))
    conn.commit()

# 创建文章
post_id = blog_db.create_post(
    "Python sqlite3模块详解",
    "这是一篇关于Python sqlite3模块的详细教程...",
    1  # alice的用户ID
)

# 获取文章
post = blog_db.get_post(post_id)
print(f"文章标题: {post['title']}")
print(f"作者: {post['author_name']}")
print(f"内容: {post['content'][:50]}...")

# 添加评论
blog_db.add_comment("这篇文章写得很好！", post_id, 2)  # bob的用户ID
blog_db.add_comment("学习到了很多新知识。", post_id, 1)  # alice的用户ID

# 获取评论
print("\n评论:")
for comment in blog_db.get_comments(post_id):
    print(f"{comment['author_name']}: {comment['content']}")
```

## 最佳实践

1. **使用参数化查询**：始终使用参数化查询，避免SQL注入攻击
2. **关闭连接**：使用完数据库连接后，确保关闭连接，或者使用上下文管理器自动关闭
3. **事务管理**：对多个相关操作使用事务，确保数据一致性
4. **索引优化**：为经常查询的列创建索引，提高查询性能
5. **错误处理**：添加适当的错误处理，特别是在事务中
6. **使用row_factory**：使用`sqlite3.Row`作为行工厂，提高代码可读性
7. **备份数据库**：定期备份数据库文件，防止数据丢失
8. **限制结果集**：使用`LIMIT`和`OFFSET`限制结果集大小，避免内存溢出
9. **使用外键约束**：在需要时启用外键约束，确保数据完整性
10. **避免频繁连接**：重用数据库连接，避免频繁创建和关闭连接

## 与其他模块的关系

- **pysqlite**：sqlite3模块实际上是pysqlite的包装器，pysqlite是SQLite数据库的Python绑定
- **sqlalchemy**：sqlalchemy是一个ORM框架，可以与sqlite3一起使用，提供更高级的数据库操作
- **dataset**：dataset是一个简化数据库操作的库，可以基于sqlite3创建数据库和表
- **pandas**：pandas可以从SQLite数据库读取数据并转换为DataFrame，进行数据分析

## 总结

sqlite3模块是Python标准库中内置的轻量级数据库系统，它提供了与SQLite数据库交互的接口。SQLite是一个自包含、零配置、事务性的SQL数据库引擎，数据存储在单个文件中，非常适合小型应用程序和原型开发。

sqlite3模块的主要功能包括连接数据库、创建表、执行SQL查询、事务处理、参数化查询等。它还提供了高级功能，如自定义函数、聚合函数、行工厂、外键约束等。

在实际应用中，sqlite3模块常用于用户管理系统、博客系统、配置存储、数据分析等场景。使用sqlite3模块时，应该遵循最佳实践，如使用参数化查询、关闭连接、事务管理等，确保数据安全和性能。

与其他数据库系统相比，SQLite具有以下优点：

- 无需安装和配置服务器
- 数据存储在单个文件中，便于移植和备份
- 支持完整的SQL语法
- 事务支持
- 轻量级，适合嵌入式应用

但它也有一些限制：

- 不适合高并发场景
- 单进程访问
- 数据库文件大小有限制（理论上为281TB，但实际使用中建议不超过10GB）

总的来说，sqlite3模块是Python中处理小型数据库的理想选择，它简单易用，功能强大，可以满足大多数小型应用程序的需求。