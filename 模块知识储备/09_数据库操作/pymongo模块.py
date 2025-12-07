# pymongo模块详解

pymongo是Python中用于与MongoDB数据库交互的官方驱动程序。MongoDB是一个面向文档的NoSQL数据库，使用JSON格式的文档存储数据。pymongo提供了与MongoDB交互的全面接口，支持所有MongoDB功能。

## 模块概述

pymongo模块主要提供以下功能：

- 连接MongoDB服务器
- 管理数据库和集合
- 插入、查询、更新和删除文档
- 索引管理
- 聚合操作
- 事务支持
- 批量操作
- 连接池管理
- 副本集和分片集群支持
- 认证和授权
- 数据验证

## 安装

使用pip安装pymongo模块：

```bash
pip install pymongo
```

对于需要连接MongoDB Atlas或使用高级功能，可以安装pymongo[srv]：

```bash
pip install pymongo[srv]
```

## 基本概念

在使用pymongo模块之前，需要了解几个基本概念：

1. **Database**: MongoDB中的数据库
2. **Collection**: 数据库中的集合，类似于关系型数据库中的表
3. **Document**: 集合中的文档，类似于关系型数据库中的行，使用BSON（二进制JSON）格式存储
4. **Field**: 文档中的字段，类似于关系型数据库中的列
5. **Index**: 索引，用于提高查询性能
6. **Cursor**: 游标，用于遍历查询结果
7. **Replica Set**: 副本集，用于数据冗余和高可用性
8. **Sharded Cluster**: 分片集群，用于水平扩展

## 基本用法

### 创建MongoDB连接

#### 基本连接

```python
from pymongo import MongoClient

# 创建MongoDB连接
client = MongoClient('mongodb://localhost:27017/')

# 测试连接
print("MongoDB连接成功")
print(f"MongoDB服务器信息: {client.server_info()}")

# 关闭连接
client.close()
```

#### 使用上下文管理器

```python
from pymongo import MongoClient

# 使用上下文管理器创建连接
with MongoClient('mongodb://localhost:27017/') as client:
    # 测试连接
    print("MongoDB连接成功")
    print(f"MongoDB服务器信息: {client.server_info()}")
# 连接会自动关闭
```

#### 连接到指定数据库

```python
from pymongo import MongoClient

# 创建连接并选择数据库
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # 或 client.mydatabase

# 列出所有数据库
databases = client.list_database_names()
print(f"所有数据库: {databases}")

# 检查数据库是否存在
if 'mydatabase' in databases:
    print("数据库mydatabase已存在")
else:
    print("数据库mydatabase不存在")

client.close()
```

#### 连接到副本集

```python
from pymongo import MongoClient

# 连接到副本集
client = MongoClient([
    'mongodb://localhost:27017/',
    'mongodb://localhost:27018/',
    'mongodb://localhost:27019/'
], replicaSet='myReplicaSet')

# 测试连接
print("MongoDB副本集连接成功")
print(f"主节点: {client.primary}")
print(f"从节点: {client.secondaries}")

client.close()
```

#### 连接到分片集群

```python
from pymongo import MongoClient

# 连接到分片集群（通过mongos路由）
client = MongoClient('mongodb://localhost:27017/')

# 测试连接
print("MongoDB分片集群连接成功")

client.close()
```

#### 连接认证

```python
from pymongo import MongoClient

# 使用URI连接并认证
client = MongoClient('mongodb://username:password@localhost:27017/')

# 或使用authenticate方法
client = MongoClient('mongodb://localhost:27017/')
db = client['admin']
db.authenticate('username', 'password')

# 测试连接
print("MongoDB认证连接成功")

client.close()
```

### 集合操作

#### 创建集合

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

# 创建集合
collection = db['mycollection']  # 或 db.mycollection

# 列出所有集合
collections = db.list_collection_names()
print(f"所有集合: {collections}")

# 检查集合是否存在
if 'mycollection' in collections:
    print("集合mycollection已存在")
else:
    print("集合mycollection不存在")

# 使用create_collection方法创建集合（可指定选项）
collection2 = db.create_collection('mycollection2', capped=True, size=100000)
print("创建capped集合成功")

client.close()
```

#### 删除集合

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

# 删除集合
result = db['mycollection2'].drop()
if result:
    print("集合mycollection2删除成功")
else:
    print("集合mycollection2删除失败")

client.close()
```

### 文档操作

#### 插入文档

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 插入单个文档
user = {
    'name': 'Alice',
    'email': 'alice@example.com',
    'age': 30,
    'city': 'New York',
    'hobbies': ['reading', 'traveling', 'photography']
}

result = collection.insert_one(user)
print(f"插入单个文档成功，ID: {result.inserted_id}")

# 插入多个文档
users = [
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'age': 25,
        'city': 'London',
        'hobbies': ['gaming', 'sports']
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'age': 35,
        'city': 'Paris',
        'hobbies': ['cooking', 'painting']
    },
    {
        'name': 'David',
        'email': 'david@example.com',
        'age': 28,
        'city': 'Tokyo',
        'hobbies': ['coding', 'movies']
    }
]

result = collection.insert_many(users)
print(f"插入多个文档成功，IDs: {result.inserted_ids}")

client.close()
```

#### 查询文档

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 查询单个文档
user = collection.find_one()
print(f"查询第一个文档: {user}")

# 根据条件查询单个文档
user = collection.find_one({'name': 'Alice'})
print(f"根据name查询文档: {user}")

# 根据ID查询文档
from bson.objectid import ObjectId

user = collection.find_one({'_id': ObjectId('60a1b2c3d4e5f67890123456')})
print(f"根据ID查询文档: {user}")

# 查询多个文档
users = collection.find()
print("查询所有文档:")
for user in users:
    print(user)

# 根据条件查询多个文档
users = collection.find({'age': {'$gt': 25}})  # 年龄大于25
print("\n查询年龄大于25的文档:")
for user in users:
    print(user)

# 高级查询
users = collection.find({
    'city': {'$in': ['New York', 'London']},  # 城市在New York或London
    'age': {'$gte': 25, '$lte': 35}  # 年龄在25到35之间
})
print("\n查询城市在New York或London且年龄在25到35之间的文档:")
for user in users:
    print(user)

# 使用正则表达式查询
users = collection.find({'name': {'$regex': '^A'}})  # 名字以A开头
print("\n查询名字以A开头的文档:")
for user in users:
    print(user)

# 查询嵌套字段
user = collection.find_one({'hobbies': 'reading'})  # 查询爱好包含reading的文档
print(f"\n查询爱好包含reading的文档: {user}")

client.close()
```

#### 更新文档

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 更新单个文档
result = collection.update_one(
    {'name': 'Alice'},
    {'$set': {'age': 31, 'city': 'Boston'}}  # 更新年龄和城市
)
print(f"更新单个文档成功，匹配: {result.matched_count}，修改: {result.modified_count}")

# 更新多个文档
result = collection.update_many(
    {'age': {'$lt': 30}},
    {'$inc': {'age': 1}}  # 年龄加1
)
print(f"更新多个文档成功，匹配: {result.matched_count}，修改: {result.modified_count}")

# 替换文档（除了_id字段）
result = collection.replace_one(
    {'name': 'Charlie'},
    {
        'name': 'Charlie',
        'email': 'charlie.new@example.com',
        'age': 36,
        'city': 'Berlin',
        'hobbies': ['cooking', 'painting', 'hiking']
    }
)
print(f"替换文档成功，匹配: {result.matched_count}，修改: {result.modified_count}")

# 更新操作符示例
collection.update_one(
    {'name': 'Bob'},
    {
        '$set': {'email': 'bob.updated@example.com'},
        '$inc': {'age': 2},
        '$push': {'hobbies': 'music'},
        '$addToSet': {'skills': 'Python'},
        '$rename': {'city': 'location'}
    }
)
print("使用多种更新操作符更新文档成功")

client.close()
```

#### 删除文档

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 删除单个文档
result = collection.delete_one({'name': 'David'})
print(f"删除单个文档成功，删除: {result.deleted_count}")

# 删除多个文档
result = collection.delete_many({'age': {'$gt': 30}})
print(f"删除多个文档成功，删除: {result.deleted_count}")

# 删除所有文档
result = collection.delete_many({})
print(f"删除所有文档成功，删除: {result.deleted_count}")

client.close()
```

### 高级查询

#### 排序

```python
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 按年龄升序排序
users = collection.find().sort('age', ASCENDING)
print("按年龄升序排序:")
for user in users:
    print(user)

# 按年龄降序排序
users = collection.find().sort('age', DESCENDING)
print("\n按年龄降序排序:")
for user in users:
    print(user)

# 多字段排序
users = collection.find().sort([
    ('city', ASCENDING),
    ('age', DESCENDING)
])
print("\n按城市升序、年龄降序排序:")
for user in users:
    print(user)

client.close()
```

#### 限制和跳过

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 限制结果数量
users = collection.find().limit(2)
print("限制结果数量为2:")
for user in users:
    print(user)

# 跳过指定数量的结果
users = collection.find().skip(2)
print("\n跳过前2个结果:")
for user in users:
    print(user)

# 分页查询
page_size = 2
page_number = 2
users = collection.find().skip((page_number - 1) * page_size).limit(page_size)
print(f"\n第{page_number}页，每页{page_size}条记录:")
for user in users:
    print(user)

client.close()
```

#### 投影

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 查询所有文档，但只返回name和email字段（不返回_id字段）
users = collection.find({}, {'_id': 0, 'name': 1, 'email': 1})
print("只返回name和email字段:")
for user in users:
    print(user)

# 查询所有文档，不返回email字段
users = collection.find({}, {'email': 0})
print("\n不返回email字段:")
for user in users:
    print(user)

client.close()
```

#### 计数

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 计数所有文档
count = collection.count_documents({})
print(f"文档总数: {count}")

# 计数符合条件的文档
count = collection.count_documents({'age': {'$gt': 25}})
print(f"年龄大于25的文档数量: {count}")

client.close()
```

#### 聚合

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 计算平均年龄
pipeline = [
    {'$group': {'_id': None, 'average_age': {'$avg': '$age'}}}
]

result = list(collection.aggregate(pipeline))
print(f"平均年龄: {result[0]['average_age']}")

# 按城市分组并计算每个城市的用户数量
pipeline = [
    {'$group': {'_id': '$city', 'count': {'$sum': 1}}}
]

result = list(collection.aggregate(pipeline))
print("\n按城市分组的用户数量:")
for item in result:
    print(f"{item['_id']}: {item['count']}人")

# 高级聚合
pipeline = [
    {'$match': {'age': {'$gte': 25}}},  # 筛选年龄大于等于25的用户
    {'$group': {'_id': '$city', 'count': {'$sum': 1}, 'average_age': {'$avg': '$age'}}},  # 按城市分组
    {'$sort': {'count': -1}},  # 按用户数量降序排序
    {'$limit': 5}  # 只返回前5个结果
]

result = list(collection.aggregate(pipeline))
print("\n高级聚合结果:")
for item in result:
    print(f"城市: {item['_id']}, 用户数量: {item['count']}, 平均年龄: {item['average_age']:.2f}")

client.close()
```

### 索引操作

#### 创建索引

```python
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 创建单字段索引
result = collection.create_index([('name', ASCENDING)])
print(f"创建单字段索引成功: {result}")

# 创建复合索引
result = collection.create_index([('city', ASCENDING), ('age', DESCENDING)])
print(f"创建复合索引成功: {result}")

# 创建唯一索引
result = collection.create_index([('email', ASCENDING)], unique=True)
print(f"创建唯一索引成功: {result}")

# 创建文本索引
result = collection.create_index([('name', 'text'), ('city', 'text')])
print(f"创建文本索引成功: {result}")

# 创建TTL索引（文档过期时间）
result = collection.create_index([('created_at', ASCENDING)], expireAfterSeconds=3600)  # 1小时后过期
print(f"创建TTL索引成功: {result}")

client.close()
```

#### 列出索引

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 列出所有索引
indexes = collection.list_indexes()
print("所有索引:")
for index in indexes:
    print(index)

client.close()
```

#### 删除索引

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 删除指定索引
result = collection.drop_index('name_1')
print(f"删除索引成功: {result}")

# 删除所有非_id索引
result = collection.drop_indexes()
print("删除所有非_id索引成功")

client.close()
```

### 事务

```python
from pymongo import MongoClient
from pymongo.errors import PyMongoError

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

# 开启事务
with client.start_session() as session:
    with session.start_transaction():
        try:
            # 在事务中执行操作
            db['users'].insert_one({'name': 'Transaction User', 'age': 30}, session=session)
            db['orders'].insert_one({'user_id': 1, 'product': 'Laptop', 'amount': 1000}, session=session)
            
            # 提交事务（自动）
            print("事务提交成功")
        except PyMongoError as e:
            # 事务会自动回滚
            print(f"事务执行失败，自动回滚: {e}")

client.close()
```

### 批量操作

```python
from pymongo import MongoClient
from pymongo import InsertOne, DeleteOne, UpdateOne

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 创建批量操作列表
operations = [
    InsertOne({'name': 'Batch User 1', 'age': 25}),
    InsertOne({'name': 'Batch User 2', 'age': 30}),
    UpdateOne({'name': 'Alice'}, {'$set': {'age': 32}}),
    DeleteOne({'name': 'Bob'})
]

# 执行批量操作
result = collection.bulk_write(operations)
print(f"批量操作成功")
print(f"插入: {result.inserted_count}")
print(f"更新: {result.modified_count}")
print(f"删除: {result.deleted_count}")

client.close()
```

## 实际应用示例

### 示例1：用户管理系统

```python
from pymongo import MongoClient
from pymongo import ASCENDING
from bson.objectid import ObjectId

class UserManager:
    def __init__(self, db_url='mongodb://localhost:27017/', db_name='usermanagement', collection_name='users'):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        
        # 创建索引
        self.collection.create_index([('email', ASCENDING)], unique=True)
        self.collection.create_index([('username', ASCENDING)], unique=True)
    
    def create_user(self, username, email, password, name, age=None, city=None):
        """创建用户"""
        user = {
            'username': username,
            'email': email,
            'password': password,  # 注意：实际应用中应该加密存储密码
            'name': name,
            'age': age,
            'city': city,
            'created_at': datetime.datetime.utcnow(),
            'updated_at': datetime.datetime.utcnow()
        }
        
        result = self.collection.insert_one(user)
        return str(result.inserted_id)
    
    def get_user(self, user_id):
        """根据ID获取用户"""
        try:
            user = self.collection.find_one({'_id': ObjectId(user_id)})
            if user:
                user['_id'] = str(user['_id'])
            return user
        except Exception as e:
            print(f"获取用户失败: {e}")
            return None
    
    def get_user_by_email(self, email):
        """根据邮箱获取用户"""
        user = self.collection.find_one({'email': email})
        if user:
            user['_id'] = str(user['_id'])
        return user
    
    def get_users(self, filter={}, page=1, page_size=10):
        """获取用户列表"""
        skip = (page - 1) * page_size
        users = self.collection.find(filter).skip(skip).limit(page_size)
        
        result = []
        for user in users:
            user['_id'] = str(user['_id'])
            result.append(user)
        
        return result
    
    def update_user(self, user_id, update_data):
        """更新用户"""
        update_data['updated_at'] = datetime.datetime.utcnow()
        
        result = self.collection.update_one(
            {'_id': ObjectId(user_id)},
            {'$set': update_data}
        )
        
        return result.modified_count > 0
    
    def delete_user(self, user_id):
        """删除用户"""
        result = self.collection.delete_one({'_id': ObjectId(user_id)})
        return result.deleted_count > 0
    
    def get_user_count(self, filter={}):
        """获取用户数量"""
        return self.collection.count_documents(filter)
    
    def close(self):
        """关闭连接"""
        self.client.close()

# 测试用户管理系统
if __name__ == "__main__":
    import datetime
    
    # 创建用户管理器
    user_manager = UserManager()
    
    # 创建用户
    user_id = user_manager.create_user(
        username='alice123',
        email='alice@example.com',
        password='password123',
        name='Alice Smith',
        age=30,
        city='New York'
    )
    print(f"创建用户成功，ID: {user_id}")
    
    # 根据ID获取用户
    user = user_manager.get_user(user_id)
    print(f"\n根据ID获取用户: {user}")
    
    # 根据邮箱获取用户
    user = user_manager.get_user_by_email('alice@example.com')
    print(f"\n根据邮箱获取用户: {user}")
    
    # 更新用户
    update_data = {
        'age': 31,
        'city': 'Boston'
    }
    success = user_manager.update_user(user_id, update_data)
    if success:
        user = user_manager.get_user(user_id)
        print(f"\n更新用户成功: {user}")
    else:
        print("\n更新用户失败")
    
    # 获取用户列表
    users = user_manager.get_users(page=1, page_size=5)
    print(f"\n用户列表: {users}")
    
    # 获取用户数量
    count = user_manager.get_user_count()
    print(f"\n用户总数: {count}")
    
    # 删除用户
    success = user_manager.delete_user(user_id)
    if success:
        print("\n删除用户成功")
    else:
        print("\n删除用户失败")
    
    # 关闭连接
    user_manager.close()
```

### 示例2：博客系统

```python
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from bson.objectid import ObjectId
import datetime

class BlogSystem:
    def __init__(self, db_url='mongodb://localhost:27017/', db_name='blogsystem'):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        
        # 初始化集合
        self.users_collection = self.db['users']
        self.posts_collection = self.db['posts']
        self.comments_collection = self.db['comments']
        
        # 创建索引
        self.users_collection.create_index([('email', ASCENDING)], unique=True)
        self.posts_collection.create_index([('title', 'text'), ('content', 'text')])
        self.posts_collection.create_index([('author_id', ASCENDING)])
        self.comments_collection.create_index([('post_id', ASCENDING)])
        self.comments_collection.create_index([('author_id', ASCENDING)])
    
    # 用户相关方法
    def create_user(self, email, password, name):
        """创建用户"""
        user = {
            'email': email,
            'password': password,  # 注意：实际应用中应该加密存储密码
            'name': name,
            'created_at': datetime.datetime.utcnow()
        }
        
        result = self.users_collection.insert_one(user)
        return str(result.inserted_id)
    
    def get_user(self, user_id):
        """获取用户"""
        user = self.users_collection.find_one({'_id': ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])
        return user
    
    # 文章相关方法
    def create_post(self, author_id, title, content, tags=None):
        """创建文章"""
        post = {
            'author_id': ObjectId(author_id),
            'title': title,
            'content': content,
            'tags': tags or [],
            'views': 0,
            'likes': 0,
            'created_at': datetime.datetime.utcnow(),
            'updated_at': datetime.datetime.utcnow()
        }
        
        result = self.posts_collection.insert_one(post)
        return str(result.inserted_id)
    
    def get_post(self, post_id):
        """获取文章"""
        post = self.posts_collection.find_one({'_id': ObjectId(post_id)})
        if post:
            post['_id'] = str(post['_id'])
            post['author_id'] = str(post['author_id'])
        return post
    
    def get_posts(self, filter={}, page=1, page_size=10, sort_by='created_at', sort_order=DESCENDING):
        """获取文章列表"""
        skip = (page - 1) * page_size
        posts = self.posts_collection.find(filter).sort(sort_by, sort_order).skip(skip).limit(page_size)
        
        result = []
        for post in posts:
            post['_id'] = str(post['_id'])
            post['author_id'] = str(post['author_id'])
            result.append(post)
        
        return result
    
    def update_post(self, post_id, update_data):
        """更新文章"""
        update_data['updated_at'] = datetime.datetime.utcnow()
        
        result = self.posts_collection.update_one(
            {'_id': ObjectId(post_id)},
            {'$set': update_data}
        )
        
        return result.modified_count > 0
    
    def delete_post(self, post_id):
        """删除文章"""
        # 开启事务
        with self.client.start_session() as session:
            with session.start_transaction():
                try:
                    # 删除文章
                    result = self.posts_collection.delete_one({'_id': ObjectId(post_id)}, session=session)
                    
                    # 删除相关评论
                    self.comments_collection.delete_many({'post_id': ObjectId(post_id)}, session=session)
                    
                    return result.deleted_count > 0
                except Exception as e:
                    print(f"删除文章失败: {e}")
                    return False
    
    def increment_post_views(self, post_id):
        """增加文章浏览量"""
        result = self.posts_collection.update_one(
            {'_id': ObjectId(post_id)},
            {'$inc': {'views': 1}}
        )
        return result.modified_count > 0
    
    # 评论相关方法
    def create_comment(self, post_id, author_id, content):
        """创建评论"""
        comment = {
            'post_id': ObjectId(post_id),
            'author_id': ObjectId(author_id),
            'content': content,
            'created_at': datetime.datetime.utcnow()
        }
        
        result = self.comments_collection.insert_one(comment)
        return str(result.inserted_id)
    
    def get_comments(self, post_id, page=1, page_size=10):
        """获取文章评论"""
        skip = (page - 1) * page_size
        comments = self.comments_collection.find({'post_id': ObjectId(post_id)})
        comments = comments.sort('created_at', ASCENDING).skip(skip).limit(page_size)
        
        result = []
        for comment in comments:
            comment['_id'] = str(comment['_id'])
            comment['post_id'] = str(comment['post_id'])
            comment['author_id'] = str(comment['author_id'])
            result.append(comment)
        
        return result
    
    def close(self):
        """关闭连接"""
        self.client.close()

# 测试博客系统
if __name__ == "__main__":
    # 创建博客系统
    blog_system = BlogSystem()
    
    # 创建用户
    user_id = blog_system.create_user(
        email='user@example.com',
        password='password123',
        name='Test User'
    )
    print(f"创建用户成功，ID: {user_id}")
    
    # 创建文章
    post_id = blog_system.create_post(
        author_id=user_id,
        title='MongoDB教程',
        content='这是一篇关于MongoDB的教程文章...',
        tags=['MongoDB', '数据库', 'NoSQL']
    )
    print(f"创建文章成功，ID: {post_id}")
    
    # 获取文章
    post = blog_system.get_post(post_id)
    print(f"\n获取文章: {post}")
    
    # 增加文章浏览量
    blog_system.increment_post_views(post_id)
    post = blog_system.get_post(post_id)
    print(f"\n增加浏览量后: 浏览量 = {post['views']}")
    
    # 创建评论
    comment_id = blog_system.create_comment(
        post_id=post_id,
        author_id=user_id,
        content='这篇文章写得很好！'
    )
    print(f"\n创建评论成功，ID: {comment_id}")
    
    # 获取评论
    comments = blog_system.get_comments(post_id)
    print(f"\n文章评论: {comments}")
    
    # 获取文章列表
    posts = blog_system.get_posts(page=1, page_size=5)
    print(f"\n文章列表: {posts}")
    
    # 删除文章
    success = blog_system.delete_post(post_id)
    if success:
        print("\n删除文章成功")
    else:
        print("\n删除文章失败")
    
    # 关闭连接
    blog_system.close()
```

## 最佳实践

1. **使用连接池**：pymongo默认使用连接池，无需手动创建
2. **合理使用索引**：为查询频繁的字段创建索引，提高查询性能
3. **限制返回字段**：使用投影限制返回的字段数量，减少网络传输
4. **批量操作**：使用bulk_write批量执行操作，减少网络往返次数
5. **使用上下文管理器**：确保连接正确关闭
6. **事务处理**：对需要原子性的操作使用事务
7. **数据验证**：在应用层或使用MongoDB的schema validation验证数据
8. **安全配置**：使用认证、授权、加密等安全措施
9. **监控性能**：使用MongoDB的监控工具监控性能指标
10. **合理设计数据模型**：根据业务需求设计合适的数据模型，避免过度嵌套

## 与其他模块的关系

- **sqlalchemy**：pymongo用于NoSQL数据库，sqlalchemy用于关系型数据库
- **pandas**：可以将MongoDB数据转换为pandas DataFrame进行数据分析
- **Django/Flask**：pymongo可作为Django或Flask的数据库后端
- **Celery**：MongoDB可作为Celery的消息代理和结果后端

## 总结

pymongo模块是Python中与MongoDB数据库交互的官方驱动程序，提供了全面的功能和接口。它支持所有MongoDB命令和功能，包括连接管理、数据库和集合操作、文档CRUD、索引管理、聚合操作、事务处理、批量操作等。

pymongo模块的高级功能包括副本集和分片集群支持、连接认证、数据验证、文本搜索等。这些功能使得pymongo模块能够满足各种复杂的业务需求。

在实际应用中，pymongo模块常用于Web应用、大数据处理、实时分析、内容管理系统等场景。使用pymongo模块时，应该遵循最佳实践，如使用连接池、合理使用索引、限制返回字段、批量操作、事务处理等，确保系统的性能和稳定性。

与其他数据库相比，MongoDB具有以下优点：

- 灵活的文档模型
- 高性能（内存操作、索引等）
- 可扩展性（副本集、分片集群）
- 丰富的查询语言
- 支持多种数据类型

但它也有一些限制：

- 不支持复杂的事务（在版本4.0之前）
- 不支持JOIN操作
- 数据一致性模型与关系型数据库不同

总的来说，pymongo模块是Python中处理NoSQL数据库的强大工具，它可以帮助开发者构建高性能、可扩展的应用程序。