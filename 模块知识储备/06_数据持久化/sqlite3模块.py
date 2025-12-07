# Python sqlite3模块详解

import sqlite3
import os
import datetime
import json

# 1. 模块概述
print("=== 1. sqlite3模块概述 ===")
print("sqlite3模块提供了对SQLite数据库的接口，SQLite是一个轻量级的嵌入式关系型数据库。")
print()
print("主要特点：")
print("- 零配置：无需安装和配置数据库服务器")
print("- 单个文件：整个数据库存储在单个文件中")
print("- 轻量级：核心库小于1MB")
print("- 支持标准SQL：几乎支持所有SQL92标准")
print("- 事务支持：ACID（原子性、一致性、隔离性、持久性）")
print("- 跨平台：数据库文件可以在不同平台之间共享")
print("- 支持大型数据库：单个数据库文件可以高达2TB")
print()
print("应用场景：")
print("- 小型应用的数据存储")
print("- 移动应用的数据存储")
print("- 临时数据存储")
print("- 原型开发")
print("- 嵌入式系统")

print()

# 2. 基本用法
print("=== 2. 基本用法 ===")

# 创建一个测试数据库
test_db = "test_sqlite3.db"

print("2.1 创建和连接数据库：")
print("   - 连接到SQLite数据库文件")
print("   - 如果文件不存在，会自动创建")

# 连接数据库（创建或打开）
conn = sqlite3.connect(test_db)
print(f"  创建并连接到数据库: {test_db}")
print(f"  连接对象: {conn}")

# 创建游标对象
cur = conn.cursor()
print(f"  游标对象: {cur}")

# 关闭连接
conn.close()
print(f"  数据库连接已关闭")

print()

print("2.2 创建表格：")
try:
    # 使用上下文管理器自动处理连接和游标
    with sqlite3.connect(test_db) as conn:
        cur = conn.cursor()
        
        # 创建表格的SQL语句
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        # 执行SQL语句
        cur.execute(create_table_sql)
        
        # 提交事务
        conn.commit()
        
        print(f"  表格 'users' 创建成功")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("2.3 插入数据：")
try:
    with sqlite3.connect(test_db) as conn:
        cur = conn.cursor()
        
        # 单条插入
        insert_sql = "INSERT INTO users (name, email, age) VALUES (?, ?, ?)"
        cur.execute(insert_sql, ("张三", "zhangsan@example.com", 30))
        
        # 多条插入（使用executemany）
        users = [
            ("李四", "lisi@example.com", 25),
            ("王五", "wangwu@example.com", 35),
            ("赵六", "zhaoliu@example.com", 40)
        ]
        cur.executemany(insert_sql, users)
        
        # 获取最后插入的ID
        last_id = cur.lastrowid
        print(f"  最后插入的记录ID: {last_id}")
        
        # 提交事务（上下文管理器会自动提交）
        conn.commit()
        
        print(f"  插入了 {cur.rowcount} 条记录")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("2.4 查询数据：")
try:
    with sqlite3.connect(test_db) as conn:
        cur = conn.cursor()
        
        # 查询所有记录
        select_all_sql = "SELECT * FROM users"
        cur.execute(select_all_sql)
        
        # 获取所有结果
        rows = cur.fetchall()
        print(f"  查询所有记录 ({len(rows)} 条):")
        for row in rows:
            print(f"    {row}")
        
        print()
        
        # 查询单条记录
        select_one_sql = "SELECT * FROM users WHERE id = ?"
        cur.execute(select_one_sql, (1,))
        row = cur.fetchone()
        print(f"  查询单条记录 (id=1): {row}")
        
        print()
        
        # 带条件查询
        select_where_sql = "SELECT * FROM users WHERE age > ?"
        cur.execute(select_where_sql, (30,))
        rows = cur.fetchall()
        print(f"  查询年龄大于30的用户 ({len(rows)} 条):")
        for row in rows:
            print(f"    {row}")
        
        print()
        
        # 分页查询
        select_limit_sql = "SELECT * FROM users ORDER BY id LIMIT ? OFFSET ?"
        cur.execute(select_limit_sql, (2, 1))  # 每页2条，从第2条开始（偏移1）
        rows = cur.fetchall()
        print(f"  分页查询 (第2页，每页2条):")
        for row in rows:
            print(f"    {row}")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("2.5 更新数据：")
try:
    with sqlite3.connect(test_db) as conn:
        cur = conn.cursor()
        
        # 更新记录
        update_sql = "UPDATE users SET age = ? WHERE id = ?"
        cur.execute(update_sql, (31, 1))  # 将ID为1的用户年龄更新为31
        
        # 提交事务
        conn.commit()
        
        print(f"  更新了 {cur.rowcount} 条记录")
        
        # 验证更新
        cur.execute("SELECT * FROM users WHERE id = ?", (1,))
        updated_row = cur.fetchone()
        print(f"  更新后的记录: {updated_row}")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("2.6 删除数据：")
try:
    with sqlite3.connect(test_db) as conn:
        cur = conn.cursor()
        
        # 删除记录
        delete_sql = "DELETE FROM users WHERE id = ?"
        cur.execute(delete_sql, (4,))  # 删除ID为4的用户
        
        # 提交事务
        conn.commit()
        
        print(f"  删除了 {cur.rowcount} 条记录")
        
        # 验证删除
        cur.execute("SELECT * FROM users")
        remaining_rows = cur.fetchall()
        print(f"  删除后剩余记录 ({len(remaining_rows)} 条):")
        for row in remaining_rows:
            print(f"    {row}")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("2.7 事务处理：")
print("   - SQLite默认自动提交事务")
print("   - 使用BEGIN、COMMIT和ROLLBACK控制事务")

# 创建另一个表格用于演示事务
try:
    with sqlite3.connect(test_db) as conn:
        cur = conn.cursor()
        
        # 创建orders表格
        create_orders_table = """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            total REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """
        
        cur.execute(create_orders_table)
        conn.commit()
        print(f"  表格 'orders' 创建成功")
        
        # 演示事务处理
        try:
            # 开始事务
            conn.execute("BEGIN TRANSACTION")
            
            # 插入订单
            insert_order_sql = "INSERT INTO orders (user_id, product, quantity, total) VALUES (?, ?, ?, ?)"
            cur.execute(insert_order_sql, (1, "Python编程书籍", 1, 89.99))
            
            # 模拟错误
            # raise sqlite3.Error("模拟事务错误")  # 取消注释以测试回滚
            
            # 更新用户数据（模拟购买后积分增加等操作）
            update_user_sql = "UPDATE users SET age = age + 1 WHERE id = ?"
            cur.execute(update_user_sql, (1,))
            
            # 提交事务
            conn.commit()
            print(f"  事务提交成功")
            
        except sqlite3.Error as e:
            # 回滚事务
            conn.rollback()
            print(f"  事务回滚: {e}")
            
        # 验证结果
        cur.execute("SELECT * FROM orders")
        orders = cur.fetchall()
        print(f"  订单记录 ({len(orders)} 条):")
        for order in orders:
            print(f"    {order}")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

# 3. 高级特性
print("=== 3. 高级特性 ===")

print("3.1 数据类型：")
print("SQLite支持以下数据类型：")
print("   - NULL: 空值")
print("   - INTEGER: 整数（1, 2, 3, 4, 6, 8字节，取决于值的大小）")
print("   - REAL: 浮点数（8字节IEEE浮点数）")
print("   - TEXT: 文本字符串（UTF-8, UTF-16BE, UTF-16LE编码）")
print("   - BLOB: 二进制大对象（存储任意二进制数据）")

print()

print("3.2 参数化查询：")
print("   - 使用?占位符防止SQL注入")
print("   - 提高查询性能")

# 演示参数化查询
print("\n演示参数化查询：")
try:
    with sqlite3.connect(test_db) as conn:
        cur = conn.cursor()
        
        # 安全的参数化查询
        user_id = 1
        select_safe_sql = "SELECT * FROM users WHERE id = ?"
        cur.execute(select_safe_sql, (user_id,))
        
        result = cur.fetchone()
        print(f"  安全查询结果: {result}")
        
        # 不安全的字符串拼接（容易SQL注入）
        # 注意：永远不要这样做！
        # unsafe_sql = f"SELECT * FROM users WHERE id = {user_id}"
        # cur.execute(unsafe_sql)
        
        print(f"  参数化查询有效防止SQL注入攻击")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("3.3 批量操作：")
print("   - 使用executemany()方法批量执行SQL语句")
print("   - 提高批量操作的性能")

# 演示批量插入
try:
    with sqlite3.connect(test_db) as conn:
        cur = conn.cursor()
        
        # 批量插入数据
        batch_data = [
            ("小明", "xiaoming@example.com", 20),
            ("小红", "xiaohong@example.com", 22),
            ("小刚", "xiaogang@example.com", 21),
            ("小花", "xiaohua@example.com", 19)
        ]
        
        insert_batch_sql = "INSERT INTO users (name, email, age) VALUES (?, ?, ?)"
        cur.executemany(insert_batch_sql, batch_data)
        
        conn.commit()
        print(f"  批量插入了 {cur.rowcount} 条记录")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("3.4 查询优化：")
print("   - 创建索引提高查询性能")
print("   - 使用EXPLAIN语句分析查询计划")

# 创建索引
try:
    with sqlite3.connect(test_db) as conn:
        cur = conn.cursor()
        
        # 创建email字段的索引
        create_index_sql = "CREATE INDEX IF NOT EXISTS idx_users_email ON users (email)"
        cur.execute(create_index_sql)
        
        conn.commit()
        print(f"  索引 'idx_users_email' 创建成功")
        
        # 分析查询计划
        explain_sql = "EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = ?"
        cur.execute(explain_sql, ("zhangsan@example.com",))
        
        plan = cur.fetchall()
        print(f"  查询计划: {plan}")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("3.5 自定义数据类型：")
print("   - SQLite支持自定义数据类型转换器")
print("   - 使用register_converter()和register_adapter()函数")

# 演示自定义数据类型转换
try:
    with sqlite3.connect(test_db) as conn:
        # 定义JSON转换器
        def adapt_json(data):
            """将Python对象转换为JSON字符串"""
            return json.dumps(data).encode('utf-8')
        
        def convert_json(data):
            """将JSON字符串转换为Python对象"""
            return json.loads(data.decode('utf-8'))
        
        # 注册转换器
        sqlite3.register_adapter(dict, adapt_json)
        sqlite3.register_converter("JSON", convert_json)
        
        # 需要重新连接数据库以应用转换器
        conn.close()
        conn = sqlite3.connect(test_db, detect_types=sqlite3.PARSE_DECLTYPES)
        cur = conn.cursor()
        
        # 创建支持JSON的表格
        create_json_table = """
        CREATE TABLE IF NOT EXISTS user_settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            settings JSON NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """
        
        cur.execute(create_json_table)
        
        # 插入JSON数据
        user_settings = {
            "theme": "dark",
            "language": "zh-CN",
            "notifications": True,
            "email_alerts": False
        }
        
        insert_settings_sql = "INSERT INTO user_settings (user_id, settings) VALUES (?, ?)"
        cur.execute(insert_settings_sql, (1, user_settings))
        
        conn.commit()
        
        # 查询JSON数据
        select_settings_sql = "SELECT * FROM user_settings WHERE user_id = ?"
        cur.execute(select_settings_sql, (1,))
        
        settings = cur.fetchone()
        print(f"  自定义JSON类型查询结果: {settings}")
        print(f"  settings字段类型: {type(settings[2])}")
        print(f"  settings内容: {settings[2]}")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("3.6 事务隔离级别：")
print("SQLite支持以下隔离级别：")
print("   - DEFERRED: 默认隔离级别")
print("   - IMMEDIATE: 立即获取读写锁")
print("   - EXCLUSIVE: 获取排他锁")

# 演示隔离级别设置
try:
    with sqlite3.connect(test_db) as conn:
        # 设置隔离级别
        conn.isolation_level = 'IMMEDIATE'
        print(f"  当前隔离级别: {conn.isolation_level}")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

# 4. 实际应用示例
print("=== 4. 实际应用示例 ===")

print("4.1 简单的用户管理系统：")

class UserManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_tables()
    
    def _create_tables(self):
        """创建必要的表格"""
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            # 创建用户表
            cur.execute("""
            CREATE TABLE IF NOT EXISTS app_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                full_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            conn.commit()
    
    def add_user(self, username, password, email, full_name=None):
        """添加新用户"""
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            try:
                cur.execute(
                    "INSERT INTO app_users (username, password, email, full_name) VALUES (?, ?, ?, ?)",
                    (username, password, email, full_name)
                )
                conn.commit()
                return True
            except sqlite3.IntegrityError:
                return False
    
    def get_user(self, user_id):
        """根据ID获取用户"""
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM app_users WHERE id = ?", (user_id,))
            return cur.fetchone()
    
    def get_user_by_username(self, username):
        """根据用户名获取用户"""
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM app_users WHERE username = ?", (username,))
            return cur.fetchone()
    
    def update_user(self, user_id, **kwargs):
        """更新用户信息"""
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            
            # 构建更新语句
            update_fields = []
            update_values = []
            
            for key, value in kwargs.items():
                if key in ['username', 'password', 'email', 'full_name']:
                    update_fields.append(f"{key} = ?")
                    update_values.append(value)
            
            if not update_fields:
                return False
            
            update_values.append(user_id)
            update_sql = f"UPDATE app_users SET {', '.join(update_fields)} WHERE id = ?"
            
            cur.execute(update_sql, update_values)
            conn.commit()
            
            return cur.rowcount > 0
    
    def delete_user(self, user_id):
        """删除用户"""
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM app_users WHERE id = ?", (user_id,))
            conn.commit()
            return cur.rowcount > 0
    
    def list_users(self, limit=100, offset=0):
        """列出所有用户"""
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM app_users ORDER BY id LIMIT ? OFFSET ?", (limit, offset))
            return cur.fetchall()

# 使用UserManager类
print("  使用UserManager类管理用户：")
user_manager = UserManager(test_db)

# 添加用户
user_manager.add_user("admin", "admin123", "admin@example.com", "系统管理员")
user_manager.add_user("user1", "pass123", "user1@example.com", "普通用户")
print(f"  添加用户成功")

# 获取用户
user = user_manager.get_user_by_username("admin")
print(f"  获取管理员用户: {user}")

# 更新用户
user_manager.update_user(user[0], full_name="超级管理员", password="newpass123")
updated_user = user_manager.get_user(user[0])
print(f"  更新后的用户: {updated_user}")

# 列出用户
users = user_manager.list_users()
print(f"  所有用户 ({len(users)} 条):")
for user in users:
    print(f"    {user}")

print()

print("4.2 简单的博客系统：")

def create_blog_tables(db_path):
    """创建博客系统的表格"""
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        
        # 创建博客表
        cur.execute("""
        CREATE TABLE IF NOT EXISTS blog_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (author_id) REFERENCES app_users (id)
        )
        """
        )
        
        # 创建评论表
        cur.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER NOT NULL,
            author_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (post_id) REFERENCES blog_posts (id),
            FOREIGN KEY (author_id) REFERENCES app_users (id)
        )
        """
        )
        
        conn.commit()
        print(f"  博客系统表格创建成功")

# 创建博客表
create_blog_tables(test_db)

# 添加博客文章
def add_blog_post(db_path, title, content, author_id):
    """添加博客文章"""
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO blog_posts (title, content, author_id) VALUES (?, ?, ?)",
            (title, content, author_id)
        )
        conn.commit()
        return cur.lastrowid

# 添加评论
def add_comment(db_path, post_id, author_id, content):
    """添加评论"""
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO comments (post_id, author_id, content) VALUES (?, ?, ?)",
            (post_id, author_id, content)
        )
        conn.commit()
        return cur.lastrowid

# 获取博客文章及评论
def get_blog_post_with_comments(db_path, post_id):
    """获取博客文章及其所有评论"""
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        
        # 获取文章
        cur.execute("SELECT * FROM blog_posts WHERE id = ?", (post_id,))
        post = cur.fetchone()
        
        if not post:
            return None, None
        
        # 获取评论
        cur.execute("SELECT * FROM comments WHERE post_id = ? ORDER BY created_at", (post_id,))
        comments = cur.fetchall()
        
        return post, comments

# 使用博客系统
print("  使用博客系统：")

# 添加博客文章
post_id = add_blog_post(test_db, "Python sqlite3模块详解", "这是一篇关于sqlite3模块的详细教程...", 1)
print(f"  博客文章添加成功，ID: {post_id}")

# 添加评论
add_comment(test_db, post_id, 2, "这篇文章写得很好！")
add_comment(test_db, post_id, 1, "谢谢支持！")
print(f"  评论添加成功")

# 获取博客文章及评论
post, comments = get_blog_post_with_comments(test_db, post_id)
if post:
    print(f"  博客文章: {post[1]}")
    print(f"  评论 ({len(comments)} 条):")
    for comment in comments:
        print(f"    评论ID {comment[0]}: {comment[3]}")

print()

# 5. 高级技巧
print("=== 5. 高级技巧 ===")

print("5.1 使用内存数据库：")
print("   - 使用':memory:'作为数据库名称创建内存数据库")
print("   - 内存数据库仅在连接期间存在")

# 演示内存数据库
try:
    # 连接到内存数据库
    with sqlite3.connect(':memory:') as conn:
        cur = conn.cursor()
        
        # 创建表格
        cur.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
        
        # 插入数据
        cur.execute("INSERT INTO test (name) VALUES ('内存数据库测试')")
        
        # 查询数据
        cur.execute("SELECT * FROM test")
        result = cur.fetchone()
        
        print(f"  内存数据库测试结果: {result}")
        print(f"  内存数据库连接关闭后数据将丢失")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("5.2 使用PRAGMA语句：")
print("   - PRAGMA语句用于配置SQLite数据库")
print("   - 可以设置各种数据库选项")

# 演示PRAGMA语句
try:
    with sqlite3.connect(test_db) as conn:
        cur = conn.cursor()
        
        # 获取数据库版本
        cur.execute("PRAGMA sqlite_version")
        version = cur.fetchone()[0]
        print(f"  SQLite版本: {version}")
        
        # 获取数据库编码
        cur.execute("PRAGMA encoding")
        encoding = cur.fetchone()[0]
        print(f"  数据库编码: {encoding}")
        
        # 设置外键约束
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("PRAGMA foreign_keys")
        foreign_keys = cur.fetchone()[0]
        print(f"  外键约束: {'开启' if foreign_keys else '关闭'}")
        
        # 获取数据库页面大小
        cur.execute("PRAGMA page_size")
        page_size = cur.fetchone()[0]
        print(f"  数据库页面大小: {page_size} 字节")
        
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("5.3 备份和恢复数据库：")
print("   - 使用.backup()方法备份数据库")
print("   - 使用sqlite3命令行工具或Python代码恢复")

# 演示数据库备份
try:
    # 连接到源数据库
    with sqlite3.connect(test_db) as src_conn:
        # 连接到目标数据库
        with sqlite3.connect(test_db + ".bak") as dest_conn:
            # 备份数据库
            src_conn.backup(dest_conn)
            print(f"  数据库备份成功: {test_db}.bak")
            
            # 验证备份
            dest_cur = dest_conn.cursor()
            dest_cur.execute("SELECT COUNT(*) FROM users")
            user_count = dest_cur.fetchone()[0]
            print(f"  备份数据库中的用户数量: {user_count}")
            
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

print("5.4 使用视图：")
print("   - 视图是虚拟表格，基于SQL查询的结果")
print("   - 可以简化复杂查询")

# 演示创建视图
try:
    with sqlite3.connect(test_db) as conn:
        cur = conn.cursor()
        
        # 创建视图
        create_view_sql = """
        CREATE VIEW IF NOT EXISTS user_with_orders AS
        SELECT u.id, u.name, u.email, COUNT(o.id) AS order_count
        FROM users u
        LEFT JOIN orders o ON u.id = o.user_id
        GROUP BY u.id
        """
        
        cur.execute(create_view_sql)
        conn.commit()
        print(f"  视图 'user_with_orders' 创建成功")
        
        # 查询视图
        cur.execute("SELECT * FROM user_with_orders")
        result = cur.fetchall()
        print(f"  视图查询结果 ({len(result)} 条):")
        for row in result:
            print(f"    {row}")
            
except sqlite3.Error as e:
    print(f"  错误: {e}")

print()

# 6. 最佳实践
print("=== 6. 最佳实践 ===")

print("1. 使用上下文管理器：")
print("   # 正确：使用上下文管理器自动处理连接和事务")
print("   with sqlite3.connect('data.db') as conn:")
print("       cur = conn.cursor()")
print("       cur.execute('INSERT INTO table VALUES (?, ?)', (value1, value2))")
print("   # 自动提交或回滚事务")
print()
print("   # 错误：手动管理连接和事务")
print("   conn = sqlite3.connect('data.db')")
print("   cur = conn.cursor()")
print("   cur.execute('INSERT INTO table VALUES (?, ?)', (value1, value2))")
print("   conn.commit()  # 可能忘记")
print("   conn.close()  # 可能忘记")

print("\n2. 使用参数化查询：")
print("   # 正确：使用参数化查询防止SQL注入")
print("   cur.execute('SELECT * FROM users WHERE id = ?', (user_id,))")
print()
print("   # 错误：使用字符串拼接容易SQL注入")
print("   cur.execute(f'SELECT * FROM users WHERE id = {user_id}')")

print("\n3. 批量操作提高性能：")
print("   # 正确：使用executemany()批量插入")
print("   data = [(1, 'value1'), (2, 'value2'), (3, 'value3')]")
print("   cur.executemany('INSERT INTO table VALUES (?, ?)', data)")
print()
print("   # 错误：循环执行多次插入")
print("   for item in data:")
print("       cur.execute('INSERT INTO table VALUES (?, ?)', item)")

print("\n4. 及时关闭连接：")
print("   # 正确：使用上下文管理器")
print("   with sqlite3.connect('data.db') as conn:")
print("       # 使用连接")
print()
print("   # 正确：手动关闭连接")
print("   conn = sqlite3.connect('data.db')")
print("   try:")
print("       # 使用连接")
print("   finally:")
print("       conn.close()")

print("\n5. 使用索引提高查询性能：")
print("   # 为频繁查询的字段创建索引")
print("   cur.execute('CREATE INDEX IF NOT EXISTS idx_users_email ON users (email)')")
print()
print("   # 避免在小表或不频繁查询的字段上创建索引")

print("\n6. 使用事务处理相关操作：")
print("   # 将相关操作放在一个事务中")
print("   with sqlite3.connect('data.db') as conn:")
print("       try:")
print("           conn.execute('BEGIN TRANSACTION')")
print("           # 执行多个相关操作")
print("           conn.commit()")
print("       except:")
print("           conn.rollback()")

print("\n7. 避免使用SELECT *：")
print("   # 正确：指定需要的字段")
print("   cur.execute('SELECT id, name, email FROM users')")
print()
print("   # 错误：使用SELECT *查询所有字段")
print("   cur.execute('SELECT * FROM users')")

print("\n8. 使用外键约束：")
print("   # 启用外键约束")
print("   conn.execute('PRAGMA foreign_keys = ON')")
print()
print("   # 创建带外键约束的表格")
print("   CREATE TABLE orders (")
print("       id INTEGER PRIMARY KEY,")
print("       user_id INTEGER NOT NULL,")
print("       FOREIGN KEY (user_id) REFERENCES users (id)")
print("   )")

# 7. 常见错误和陷阱
print("=== 7. 常见错误和陷阱 ===")

print("1. SQL注入攻击：")
print("   # 错误：使用字符串拼接构建SQL语句")
print("   user_id = input('请输入用户ID:')")
print("   cur.execute(f'SELECT * FROM users WHERE id = {user_id}')")
print("   # 攻击者可以输入: 1 OR 1=1 --")
print("   # 这会导致查询所有用户数据")
print()
print("   # 正确：使用参数化查询")
print("   user_id = input('请输入用户ID:')")
print("   cur.execute('SELECT * FROM users WHERE id = ?', (user_id,))")

print("\n2. 忘记提交事务：")
print("   # 错误：执行INSERT/UPDATE/DELETE后忘记提交")
print("   with sqlite3.connect('data.db') as conn:")
print("       cur = conn.cursor()")
print("       cur.execute('INSERT INTO users (name) VALUES (?)', ('test',))")
print("   # 默认情况下，上下文管理器会自动提交")
print("   # 但如果显式设置了isolation_level，可能不会自动提交")

print("\n3. 连接泄漏：")
print("   # 错误：未关闭连接")
print("   def get_data():")
print("       conn = sqlite3.connect('data.db')")
print("       cur = conn.cursor()")
print("       cur.execute('SELECT * FROM users')")
print("       return cur.fetchall()")
print("   # 连接未关闭，会导致资源泄漏")
print()
print("   # 正确：使用上下文管理器")
print("   def get_data():")
print("       with sqlite3.connect('data.db') as conn:")
print("           cur = conn.cursor()")
print("           cur.execute('SELECT * FROM users')")
print("           return cur.fetchall()")

print("\n4. 使用错误的数据类型：")
print("   # 错误：将Python对象直接插入数据库")
print("   cur.execute('INSERT INTO users (settings) VALUES (?)', ({'theme': 'dark'},))")
print()
print("   # 正确：将Python对象转换为字符串")
print("   import json")
print("   cur.execute('INSERT INTO users (settings) VALUES (?)', (json.dumps({'theme': 'dark'}),))")

print("\n5. 忽略外键约束：")
print("   # 错误：未启用外键约束")
print("   with sqlite3.connect('data.db') as conn:")
print("       cur = conn.cursor()")
print("       # 插入不存在的用户ID")
print("       cur.execute('INSERT INTO orders (user_id) VALUES (?)', (999,))")
print()
print("   # 正确：启用外键约束")
print("   with sqlite3.connect('data.db') as conn:")
print("       conn.execute('PRAGMA foreign_keys = ON')")
print("       cur = conn.cursor()")
print("       # 插入不存在的用户ID会引发错误")
print("       # cur.execute('INSERT INTO orders (user_id) VALUES (?)', (999,))")

print("\n6. 过度使用索引：")
print("   # 错误：为所有字段创建索引")
print("   cur.execute('CREATE INDEX idx_users_name ON users (name)')")
print("   cur.execute('CREATE INDEX idx_users_age ON users (age)')")
print("   cur.execute('CREATE INDEX idx_users_email ON users (email)')")
print("   # 过多索引会影响插入、更新和删除操作的性能")

print("\n7. 使用大型BLOB数据：")
print("   # 错误：将大型文件存储在BLOB字段中")
print("   with open('large_file.zip', 'rb') as f:")
print("       blob_data = f.read()")
print("   cur.execute('INSERT INTO files (data) VALUES (?)', (blob_data,))")
print()
print("   # 正确：存储文件路径，将文件保存在文件系统中")
print("   file_path = 'large_file.zip'")
print("   cur.execute('INSERT INTO files (path) VALUES (?)', (file_path,))")

# 8. 总结
print("=== 8. 总结 ===")
print("sqlite3模块是Python标准库中功能强大的数据库接口，提供了对SQLite数据库的全面支持。")
print()
print("主要优点：")
print("- 零配置，无需安装和配置数据库服务器")
print("- 单个文件存储，易于管理和备份")
print("- 支持标准SQL和事务")
print("- 跨平台兼容性好")
print("- 轻量级但功能强大")
print()
print("主要功能：")
print("- 数据库连接和管理")
print("- 表格创建和管理")
print("- 数据插入、查询、更新和删除")
print("- 事务处理")
print("- 索引和视图")
print("- 自定义数据类型转换")
print()
print("应用场景：")
print("- 小型应用的数据存储")
print("- 移动应用和嵌入式系统")
print("- 原型开发和测试")
print("- 临时数据存储")
print()
print("通过合理使用sqlite3模块，可以实现高效、可靠的数据存储功能，适用于各种需要轻量级数据库的应用场景。")

# 清理测试文件
if os.path.exists(test_db):
    os.remove(test_db)
if os.path.exists(test_db + ".bak"):
    os.remove(test_db + ".bak")

print("\n测试数据库文件已清理完成。")
