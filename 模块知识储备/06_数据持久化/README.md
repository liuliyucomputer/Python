# Python 数据持久化模块知识储备

## 目录简介

本目录包含 Python 中用于数据持久化的核心模块的详细文档和示例代码。数据持久化是指将内存中的数据保存到持久存储设备（如磁盘）上，以便在程序重启或系统关闭后能够恢复数据。

## 目录结构

本目录计划包含以下模块的详细文档：

1. [pickle模块.py](./pickle模块.py) - Python 对象的序列化和反序列化
2. [shelve模块.py](./shelve模块.py) - 简单的键值存储系统
3. [dbm模块.py](./dbm模块.py) - 数据库管理模块系列
4. [sqlite3模块.py](./sqlite3模块.py) - SQLite 数据库接口

## 核心模块说明

### 1. pickle模块

`pickle` 模块提供了 Python 对象的序列化和反序列化功能，允许将复杂的 Python 对象转换为字节流，以便存储或传输，然后再将字节流转换回原始对象。

**主要功能：**
- 对象的序列化（pickling）
- 对象的反序列化（unpickling）
- 支持几乎所有 Python 数据类型
- 提供多种协议版本

### 2. shelve模块

`shelve` 模块提供了一个简单的键值存储系统，基于 `dbm` 模块构建，允许使用字符串键来访问 Python 对象。

**主要功能：**
- 简单的键值存储接口
- 自动处理对象的序列化和反序列化
- 支持类似字典的操作
- 基于文件的存储

### 3. dbm模块

`dbm` 模块是 Python 中数据库管理模块的抽象层，提供了访问不同数据库实现的统一接口。

**主要功能：**
- 键值对存储
- 支持多种数据库实现（dbm.ndbm, dbm.gnu, dbm.dumb等）
- 自动选择可用的数据库实现
- 基于文件的存储

### 4. sqlite3模块

`sqlite3` 模块提供了 SQLite 数据库的接口，允许创建和操作关系型数据库。

**主要功能：**
- 轻量级关系型数据库
- 无需独立的数据库服务器
- 支持 SQL 查询语言
- 事务支持
- 基于文件的存储

## 学习路径

建议按照以下顺序学习本目录中的模块：

1. **pickle模块** - 理解 Python 对象的序列化和反序列化
2. **shelve模块** - 学习简单的键值存储系统
3. **dbm模块** - 了解底层的数据库管理系统
4. **sqlite3模块** - 掌握关系型数据库的基本操作

## 示例代码使用方法

每个模块文档都包含详细的示例代码，您可以直接运行这些代码来理解模块的使用方法。

```bash
# 运行pickle模块示例
python pickle模块.py

# 运行shelve模块示例
python shelve模块.py

# 运行dbm模块示例
python dbm模块.py

# 运行sqlite3模块示例
python sqlite3模块.py
```

## 注意事项

1. **安全问题**：
   - 不要反序列化来自不可信源的 pickle 数据，可能导致安全漏洞
   - 使用 sqlite3 时注意 SQL 注入攻击

2. **性能考虑**：
   - pickle 适用于小到中等规模的数据
   - 对于大规模数据，考虑使用更专业的数据库系统
   - 频繁访问的数据可以考虑缓存

3. **跨平台兼容性**：
   - 不同版本的 Python 可能使用不同的 pickle 协议
   - sqlite3 数据库文件在不同平台上可以通用

4. **数据备份**：
   - 定期备份持久化的数据文件
   - 对于重要数据，考虑使用事务和恢复机制

## 参考资源

- [Python 官方文档 - pickle模块](https://docs.python.org/zh-cn/3/library/pickle.html)
- [Python 官方文档 - shelve模块](https://docs.python.org/zh-cn/3/library/shelve.html)
- [Python 官方文档 - dbm模块](https://docs.python.org/zh-cn/3/library/dbm.html)
- [Python 官方文档 - sqlite3模块](https://docs.python.org/zh-cn/3/library/sqlite3.html)
- [SQLite 官方网站](https://www.sqlite.org/)

---

**作者：** Python 模块知识储备项目组  
**创建时间：** 2023-10-01  
**最后更新：** 2023-10-01
