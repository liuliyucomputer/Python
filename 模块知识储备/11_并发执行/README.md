# 11_并发执行

## 目录简介

本目录包含Python中用于并发执行的核心模块文档和示例代码。并发是指在同一时间处理多个任务的能力，是提高程序性能和响应速度的关键技术之一。

## 目录结构

本目录包含以下模块的文档和示例：

- `threading模块.py`: 多线程编程
- `multiprocessing模块.py`: 多进程编程
- `concurrent.futures模块.py`: 高级并发编程接口
- `asyncio模块.py`: 异步编程
- `queue模块.py`: 线程安全的队列
- `Lock模块.py`: 线程同步锁
- `Condition模块.py`: 线程条件变量

## 核心模块说明

### threading模块
提供多线程编程的支持，允许程序同时执行多个线程，适用于I/O密集型任务。

### multiprocessing模块
提供多进程编程的支持，允许程序同时执行多个进程，适用于CPU密集型任务。

### concurrent.futures模块
提供高级并发编程接口，简化多线程和多进程编程，包含ThreadPoolExecutor和ProcessPoolExecutor。

### asyncio模块
提供异步编程支持，基于事件循环和协程，适用于高并发I/O密集型任务。

### queue模块
提供线程安全的队列实现，用于线程间通信和数据共享。

### Lock模块
提供线程同步锁，防止多个线程同时访问共享资源导致的数据竞争。

### Condition模块
提供线程条件变量，允许线程等待特定条件满足后再继续执行。

## 学习路径

1. **threading模块**: 学习多线程基础概念和使用方法
2. **queue模块**: 学习线程安全的数据结构
3. **Lock和Condition模块**: 学习线程同步机制
4. **multiprocessing模块**: 学习多进程编程
5. **concurrent.futures模块**: 学习高级并发编程接口
6. **asyncio模块**: 学习异步编程和协程

## 示例代码使用方法

每个模块文件都包含详细的文档和示例代码，可以直接运行：

```bash
python threading模块.py
python multiprocessing模块.py
# 其他模块类似
```

## 注意事项

1. **多线程与多进程的选择**: I/O密集型任务使用多线程，CPU密集型任务使用多进程
2. **线程安全**: 确保多线程环境下共享资源的访问是线程安全的
3. **死锁**: 避免线程间的死锁情况
4. **异步编程**: 理解事件循环和协程的概念
5. **性能考量**: 根据任务类型选择合适的并发模型

## 参考资源

- [Python官方文档 - 多线程](https://docs.python.org/3/library/threading.html)
- [Python官方文档 - 多进程](https://docs.python.org/3/library/multiprocessing.html)
- [Python官方文档 - concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [Python官方文档 - asyncio](https://docs.python.org/3/library/asyncio.html)
