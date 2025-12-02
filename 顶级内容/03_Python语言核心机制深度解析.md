# Python语言核心机制深度解析

## 1. Python解释器原理与实现

### 1.1 Python解释器工作流程
**[标识: CORE-INTERPRETER-001]**

Python解释器是执行Python代码的核心组件，其工作流程包括词法分析、语法分析、编译和执行四个主要阶段。

```python
# Python解释器工作流程示意图

# 1. 词法分析：将源代码转换为token序列
# 源代码：x = 1 + 2
# Token序列：[NAME('x'), '=', NUMBER('1'), '+', NUMBER('2')]

# 2. 语法分析：构建抽象语法树(AST)
import ast

source_code = "x = 1 + 2"
ast_tree = ast.parse(source_code)
print("抽象语法树:")
print(ast.dump(ast_tree, indent=2))

# 3. 编译阶段：将AST转换为字节码
import dis

code_obj = compile(source_code, '<string>', 'exec')
print("\n字节码:")
dis.dis(code_obj)

# 4. 执行阶段：解释器执行字节码
namespace = {}
exec(code_obj, namespace)
print(f"\n执行结果: x = {namespace['x']}")
```

### 1.2 主要解释器实现比较
**[标识: CORE-INTERPRETER-002]**

Python有多种解释器实现，每种实现都有其特定的设计目标和性能特点。

```python
# 解释器实现比较示例

# 1. CPython - 官方实现
# 特点：C语言编写，最成熟的实现，拥有最广泛的第三方库支持

# 2. Jython - 基于Java的实现
# 特点：与Java无缝集成，可以使用Java类库，适合企业级应用

# 3. IronPython - 基于.NET的实现
# 特点：与.NET框架集成，适合Windows平台开发

# 4. PyPy - 即时编译(JIT)实现
# 特点：显著提高执行速度，通常比CPython快数倍

# 性能测试示例（在不同解释器中执行）

import time

def test_performance(n=10000000):
    """测试简单循环性能"""
    start = time.time()
    total = 0
    for i in range(n):
        total += i
    end = time.time()
    print(f"循环计算结果: {total}")
    print(f"执行时间: {end - start:.4f}秒")

# 在CPython中执行
print("CPython性能测试:")
test_performance(10000000)

# 在PyPy中执行相同代码通常会快2-10倍
```

## 2. 全局解释器锁(GIL)

### 2.1 GIL的工作原理
**[标识: CORE-GIL-001]**

全局解释器锁(Global Interpreter Lock)是CPython解释器中的一个关键机制，它确保在同一时间只有一个线程执行Python字节码。

```python
# GIL工作原理示例

import threading
import time

# 全局变量
counter = 0

def increment(n):
    """递增计数器"""
    global counter
    for _ in range(n):
        counter += 1

def decrement(n):
    """递减计数器"""
    global counter
    for _ in range(n):
        counter -= 1

# 测试单线程性能
start = time.time()
increment(10000000)
end = time.time()
print(f"单线程执行时间: {end - start:.4f}秒")
counter = 0

# 测试多线程性能（CPU密集型任务）
start = time.time()
t1 = threading.Thread(target=increment, args=(5000000,))
t2 = threading.Thread(target=decrement, args=(5000000,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(f"多线程执行时间: {end - start:.4f}秒")
print(f"最终计数器值: {counter}")  # 应该为0

# 注意：在CPython中，由于GIL的存在，多线程在CPU密集型任务上几乎没有性能提升
# 但在I/O密集型任务上，多线程仍然有效，因为线程等待I/O时会释放GIL
```

### 2.2 GIL对多线程性能的影响与解决方案
**[标识: CORE-GIL-002]**

GIL在CPU密集型任务中会限制多线程的性能，了解其影响并采取适当的解决方案至关重要。

```python
# GIL影响与解决方案示例

# 1. 使用多进程而非多线程（绕过GIL）
from multiprocessing import Process, Value

def increment_mp(shared_counter, n):
    """使用多进程递增计数器"""
    for _ in range(n):
        with shared_counter.get_lock():
            shared_counter.value += 1

# 创建共享内存值
shared_counter = Value('i', 0)

# 测试多进程性能
start = time.time()
p1 = Process(target=increment_mp, args=(shared_counter, 5000000))
p2 = Process(target=increment_mp, args=(shared_counter, 5000000))
p1.start()
p2.start()
p1.join()
p2.join()
end = time.time()
print(f"多进程执行时间: {end - start:.4f}秒")
print(f"最终计数器值: {shared_counter.value}")

# 2. 使用Numba绕过GIL（适合数值计算）
try:
    from numba import jit, prange
    
    @jit(nopython=True, parallel=True)
    def compute_parallel(n):
        """使用Numba并行计算"""
        total = 0
        for i in prange(n):
            total += i * i
        return total
    
    # 预热
    _ = compute_parallel(1000)
    
    # 性能测试
    start = time.time()
    result = compute_parallel(10000000)
    end = time.time()
    print(f"Numba并行执行时间: {end - start:.4f}秒")
    print(f"计算结果: {result}")
except ImportError:
    print("Numba未安装，请使用 'pip install numba' 安装")

# 3. 使用C扩展模块（如Cython）
# 示例代码（需要单独编译）
'''
# example.pyx
cdef int cython_compute(int n):
    cdef int i, total = 0
    for i in range(n):
        total += i * i
    return total
'''

# 4. 异步编程（asyncio）- 适合I/O密集型任务
import asyncio

async def async_task(name, iterations):
    """异步任务示例"""
    print(f"任务 {name} 开始")
    # 模拟I/O操作
    await asyncio.sleep(1)
    total = 0
    for i in range(iterations):
        total += i
    print(f"任务 {name} 完成，结果: {total}")
    return total

async def main():
    # 并发执行多个异步任务
    results = await asyncio.gather(
        async_task("A", 1000000),
        async_task("B", 1000000),
        async_task("C", 1000000)
    )
    print(f"所有任务完成，总结果: {sum(results)}")

# 运行异步主函数
try:
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"异步执行时间: {end - start:.4f}秒")
except RuntimeError:
    # 在某些环境中可能需要不同的异步运行方式
    print("异步执行环境受限")
```

## 3. Python内存管理机制

### 3.1 内存分配与回收策略
**[标识: CORE-MEMORY-001]**

Python使用分层内存分配器和引用计数机制来管理内存，了解这些机制有助于编写更高效的代码。

```python
# 内存管理机制示例

import sys
import gc
import tracemalloc

# 1. 引用计数基础

class TestObject:
    def __init__(self, name):
        self.name = name
        print(f"创建对象: {name}")
    
    def __del__(self):
        print(f"销毁对象: {self.name}")

# 测试引用计数
def test_reference_counting():
    print("\n=== 测试引用计数 ===")
    # 创建对象
    obj = TestObject("A")
    print(f"初始引用计数: {sys.getrefcount(obj) - 1}")  # -1因为getrefcount本身也增加了一个引用
    
    # 增加引用
    ref1 = obj
    print(f"增加引用后: {sys.getrefcount(obj) - 1}")
    
    # 增加更多引用
    ref2 = obj
    print(f"再次增加引用后: {sys.getrefcount(obj) - 1}")
    
    # 删除引用
    del ref1
    print(f"删除一个引用后: {sys.getrefcount(obj) - 1}")
    
    # 清除所有引用
    print("清除所有引用...")
    del ref2
    del obj
    print("引用计数测试完成")

# 2. 内存分配跟踪
def test_memory_allocation():
    print("\n=== 测试内存分配 ===")
    
    # 启动内存分配跟踪
    tracemalloc.start()
    
    # 分配一些内存
    small_list = [i for i in range(100)]
    large_list = [i for i in range(100000)]
    
    # 获取当前内存分配快照
    current, peak = tracemalloc.get_traced_memory()
    print(f"当前内存使用: {current / 1024 / 1024:.2f} MB")
    print(f"峰值内存使用: {peak / 1024 / 1024:.2f} MB")
    
    # 获取内存分配的详细信息
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    
    print("\n前10个内存消耗位置:")
    for stat in top_stats[:10]:
        print(stat)
    
    # 停止内存跟踪
    tracemalloc.stop()
    
    # 释放内存
    del small_list
    del large_list

# 3. 垃圾回收机制
def test_garbage_collection():
    print("\n=== 测试垃圾回收 ===")
    
    # 禁用自动垃圾回收
    gc.disable()
    
    # 创建循环引用
    class Node:
        def __init__(self, name):
            self.name = name
            self.ref = None
    
    # 创建循环引用
    node1 = Node("Node1")
    node2 = Node("Node2")
    node1.ref = node2
    node2.ref = node1
    
    # 获取当前垃圾回收统计
    print(f"垃圾回收前对象数: {len(gc.get_objects())}")
    print(f"未收集的对象数: {len(gc.garbage)}")
    
    # 删除对外部对象的引用，但循环引用仍然存在
    del node1
    del node2
    
    # 手动执行垃圾回收
    print("执行垃圾回收...")
    collected = gc.collect()
    print(f"收集的对象数: {collected}")
    print(f"未收集的对象数: {len(gc.garbage)}")
    print(f"垃圾回收后对象数: {len(gc.get_objects())}")
    
    # 重新启用自动垃圾回收
    gc.enable()

# 4. 内存池机制

# Python的内存分配器使用内存池来管理小对象分配，减少系统调用
def demonstrate_memory_pool():
    print("\n=== 演示内存池机制 ===")
    
    # 小对象分配通常从内存池获取
    small_objects = [object() for _ in range(10000)]
    print(f"创建了{len(small_objects)}个小对象")
    
    # 大对象直接从系统分配
    large_data = b'x' * 1024 * 1024  # 1MB数据
    print(f"创建了一个大对象，大小约{len(large_data)/1024/1024:.2f}MB")
    
    # 释放内存
    del small_objects
    del large_data
    print("对象已删除")

# 运行所有测试
test_reference_counting()
test_memory_allocation()
test_garbage_collection()
demonstrate_memory_pool()
```

### 3.2 内存优化技巧
**[标识: CORE-MEMORY-002]**

通过理解Python的内存管理机制，可以采用多种策略来优化程序的内存使用。

```python
# 内存优化技巧示例

import sys
import array
import numpy as np
from functools import lru_cache
import gc

# 1. 使用更高效的数据结构
def optimize_data_structures():
    print("\n=== 数据结构内存优化 ===")
    
    # 列表 vs 数组（对于同类型数据）
    list_of_ints = [i for i in range(10000)]
    array_of_ints = array.array('i', range(10000))  # 'i'表示有符号整数
    np_array_of_ints = np.array(range(10000), dtype=np.int32)
    
    print(f"列表内存占用: {sys.getsizeof(list_of_ints)} 字节")
    print(f"数组内存占用: {sys.getsizeof(array_of_ints)} 字节")
    print(f"NumPy数组内存占用: {sys.getsizeof(np_array_of_ints)} 字节")
    print(f"优化比例: 列表/数组 = {sys.getsizeof(list_of_ints) / sys.getsizeof(array_of_ints):.2f}倍")
    
    # 字典 vs 元组（对于只读数据）
    dict_data = {f'key_{i}': i for i in range(1000)}
    tuple_pairs = tuple((f'key_{i}', i) for i in range(1000))
    
    print(f"\n字典内存占用: {sys.getsizeof(dict_data)} 字节")
    print(f"元组内存占用: {sys.getsizeof(tuple_pairs)} 字节")
    
    # 清除
    del list_of_ints, array_of_ints, np_array_of_ints, dict_data, tuple_pairs

# 2. 使用生成器节省内存
def optimize_with_generators():
    print("\n=== 生成器内存优化 ===")
    
    # 创建一个大列表 vs 生成器
    def large_list():
        return [i * i for i in range(1000000)]
    
    def large_generator():
        for i in range(1000000):
            yield i * i
    
    # 测量列表内存
    list_obj = large_list()
    print(f"列表内存占用: {sys.getsizeof(list_obj)} 字节")
    
    # 测量生成器内存（生成器本身非常小）
    gen_obj = large_generator()
    print(f"生成器内存占用: {sys.getsizeof(gen_obj)} 字节")
    print(f"优化比例: 列表/生成器 = {sys.getsizeof(list_obj) / sys.getsizeof(gen_obj):.2f}倍")
    
    # 清除
    del list_obj

# 3. 缓存优化
def optimize_with_caching():
    print("\n=== 缓存优化 ===")
    
    # 无缓存的递归函数
    def fibonacci_no_cache(n):
        if n <= 1:
            return n
        return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)
    
    # 有缓存的递归函数
    @lru_cache(maxsize=None)
    def fibonacci_with_cache(n):
        if n <= 1:
            return n
        return fibonacci_with_cache(n-1) + fibonacci_with_cache(n-2)
    
    # 测量内存使用
    import time
    
    # 测试无缓存版本（只测试小数值以避免等待时间过长）
    start_time = time.time()
    result_no_cache = fibonacci_no_cache(30)
    no_cache_time = time.time() - start_time
    print(f"无缓存计算fib(30)结果: {result_no_cache}, 时间: {no_cache_time:.4f}秒")
    
    # 测试有缓存版本
    start_time = time.time()
    result_with_cache = fibonacci_with_cache(30)
    with_cache_time = time.time() - start_time
    print(f"有缓存计算fib(30)结果: {result_with_cache}, 时间: {with_cache_time:.4f}秒")
    print(f"性能提升: {no_cache_time / with_cache_time:.2f}倍")
    
    # 对于大数值，缓存版本仍然快速
    start_time = time.time()
    result_with_cache = fibonacci_with_cache(100)
    with_cache_big_time = time.time() - start_time
    print(f"有缓存计算fib(100)结果: {result_with_cache}, 时间: {with_cache_big_time:.4f}秒")
    
    # 清除缓存
    fibonacci_with_cache.cache_clear()

# 4. 对象池模式
def object_pool_optimization():
    print("\n=== 对象池优化 ===")
    
    class ObjectPool:
        def __init__(self, create_func, max_size=100):
            self.create_func = create_func
            self.max_size = max_size
            self.pool = []
        
        def get(self):
            if self.pool:
                return self.pool.pop()
            return self.create_func()
        
        def release(self, obj):
            if len(self.pool) < self.max_size:
                # 重置对象状态
                obj.clear()
                self.pool.append(obj)
    
    class Buffer:
        def __init__(self):
            self.data = bytearray(1024)  # 1KB缓冲区
        
        def clear(self):
            self.data = bytearray(1024)  # 重置数据
    
    # 创建对象池
    buffer_pool = ObjectPool(Buffer, max_size=50)
    
    # 使用对象池获取和释放对象
    buffers = []
    for _ in range(100):
        # 从池中获取对象
        buffer = buffer_pool.get()
        # 使用缓冲区（这里只是示例）
        buffer.data[0] = 1
        buffers.append(buffer)
    
    print(f"创建了100个缓冲区对象")
    print(f"池中剩余对象数: {len(buffer_pool.pool)}")
    
    # 释放对象回池中
    for buffer in buffers[:50]:
        buffer_pool.release(buffer)
    
    print(f"释放50个对象到池中")
    print(f"池中对象数: {len(buffer_pool.pool)}")
    
    # 清除
    del buffers, buffer_pool

# 5. 弱引用避免内存泄漏
def weak_reference_optimization():
    print("\n=== 弱引用优化 ===")
    
    import weakref
    
    # 创建一个大对象
    class LargeObject:
        def __init__(self):
            self.data = bytearray(10 * 1024 * 1024)  # 10MB数据
    
    # 创建弱引用字典
    weak_ref_dict = weakref.WeakValueDictionary()
    
    # 创建并存储对象
    obj = LargeObject()
    weak_ref_dict['key1'] = obj
    
    # 验证对象在字典中
    print(f"对象在字典中: {'key1' in weak_ref_dict}")
    
    # 删除原始引用，弱引用不会阻止对象被回收
    print("删除原始引用...")
    del obj
    
    # 强制垃圾回收
    gc.collect()
    
    # 验证对象已从字典中移除
    print(f"对象在字典中: {'key1' in weak_ref_dict}")

# 运行所有优化测试
optimize_data_structures()
optimize_with_generators()
optimize_with_caching()
object_pool_optimization()
weak_reference_optimization()
```

## 4. Python执行模型与字节码

### 4.1 Python字节码深入分析
**[标识: CORE-BYTECODE-001]**

Python字节码是解释器执行的中间表示，了解字节码可以帮助理解Python代码的实际执行过程。

```python
# Python字节码分析示例

import dis
import types

# 1. 简单函数的字节码分析
def simple_function(a, b):
    result = a + b
    return result * 2

print("=== 简单函数字节码 ===")
dis.dis(simple_function)

# 2. 控制流字节码分析
def control_flow_example(x):
    if x > 10:
        return "大于10"
    elif x < 5:
        return "小于5"
    else:
        return "介于5和10之间"

print("\n=== 控制流字节码 ===")
dis.dis(control_flow_example)

# 3. 循环字节码分析
def loop_example(n):
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += i
    return total

print("\n=== 循环字节码 ===")
dis.dis(loop_example)

# 4. 类方法字节码分析
class TestClass:
    def __init__(self, value):
        self.value = value
    
    def add(self, other):
        return self.value + other
    
    @staticmethod
    def static_add(a, b):
        return a + b
    
    @classmethod
    def class_method(cls):
        return "这是类方法"

print("\n=== 实例方法字节码 ===")
dis.dis(TestClass.add)

print("\n=== 静态方法字节码 ===")
dis.dis(TestClass.static_add)

print("\n=== 类方法字节码 ===")
dis.dis(TestClass.class_method)

# 5. 闭包字节码分析
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

print("\n=== 闭包字节码 ===")
dis.dis(outer_function)

# 获取内部函数并分析
closure_func = outer_function(10)
print("\n=== 内部函数字节码 ===")
dis.dis(closure_func)

# 查看闭包变量
print(f"\n闭包变量: {closure_func.__closure__[0].cell_contents}")

# 6. 生成器字节码分析
def generator_example(n):
    for i in range(n):
        yield i * 2

print("\n=== 生成器字节码 ===")
dis.dis(generator_example)

# 7. 动态字节码生成与执行
def dynamic_bytecode_example():
    print("\n=== 动态字节码生成 ===")
    
    # 定义源代码
    source_code = '''
def dynamic_function(a, b):
    return a * b + 10
'''
    
    # 编译源代码为代码对象
    code_obj = compile(source_code, '<dynamic>', 'exec')
    
    # 在命名空间中执行代码对象
    namespace = {}
    exec(code_obj, namespace)
    
    # 获取编译后的函数
    dynamic_func = namespace['dynamic_function']
    
    # 分析字节码
    print("动态生成函数的字节码:")
    dis.dis(dynamic_func)
    
    # 测试函数
    result = dynamic_func(5, 3)
    print(f"函数执行结果: {result}")

# 8. 字节码优化技巧
def bytecode_optimization():
    print("\n=== 字节码优化技巧 ===")
    
    # 常量折叠 - Python解释器会在编译时计算常量表达式
    def constant_folding():
        return 2 * 3 * 4 * 5  # 编译时会计算为120
    
    print("常量折叠示例:")
    dis.dis(constant_folding)
    
    # 局部变量访问比全局变量访问更快
    global_var = 100
    
    def global_access():
        total = 0
        for _ in range(1000):
            total += global_var  # 访问全局变量
        return total
    
    def local_access():
        local_var = global_var  # 复制到局部变量
        total = 0
        for _ in range(1000):
            total += local_var  # 访问局部变量
        return total
    
    print("\n全局变量访问字节码:")
    dis.dis(global_access)
    
    print("\n局部变量访问字节码:")
    dis.dis(local_access)
    
    # 性能测试
    import time
    
    start = time.time()
    for _ in range(10000):
        global_access()
    global_time = time.time() - start
    
    start = time.time()
    for _ in range(10000):
        local_access()
    local_time = time.time() - start
    
    print(f"\n全局变量访问时间: {global_time:.6f}秒")
    print(f"局部变量访问时间: {local_time:.6f}秒")
    print(f"性能提升: {global_time / local_time:.2f}倍")

# 运行所有字节码分析
dynamic_bytecode_example()
bytecode_optimization()
```

### 4.2 上下文管理器与with语句
**[标识: CORE-CONTEXT-001]**

上下文管理器是Python中一种优雅的资源管理机制，通过`with`语句实现自动资源获取和释放。

```python
# 上下文管理器深入解析

# 1. 基本上下文管理器实现（使用类）
class FileHandler:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        """进入上下文时调用"""
        print(f"打开文件: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file  # 返回的对象会被with语句的as部分接收
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时调用"""
        print(f"关闭文件: {self.filename}")
        self.file.close()
        
        # 如果返回True，则异常会被抑制
        # 如果返回False或None，则异常会被传播
        return False

# 使用自定义上下文管理器
print("=== 使用类实现的上下文管理器 ===")
try:
    with FileHandler("example.txt", "w") as f:
        f.write("Hello, Context Manager!")
        # 故意引发异常测试__exit__
        # raise ValueError("测试异常处理")
except Exception as e:
    print(f"捕获到异常: {e}")

# 2. 使用contextlib简化上下文管理器实现
from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode='r'):
    """使用装饰器实现上下文管理器"""
    print(f"打开文件: {filename}")
    try:
        file = open(filename, mode)
        yield file  # yield的值会被with语句的as部分接收
    finally:
        print(f"关闭文件: {filename}")
        file.close()

# 使用装饰器实现的上下文管理器
print("\n=== 使用装饰器实现的上下文管理器 ===")
try:
    with managed_file("example.txt", "a") as f:
        f.write("\nAppended text using contextmanager!")
except Exception as e:
    print(f"捕获到异常: {e}")

# 3. 嵌套上下文管理器
print("\n=== 嵌套上下文管理器 ===")

class ResourceA:
    def __enter__(self):
        print("获取资源A")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("释放资源A")
        return False
    
    def do_something(self):
        print("使用资源A")

class ResourceB:
    def __enter__(self):
        print("获取资源B")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("释放资源B")
        return False
    
    def do_something(self):
        print("使用资源B")

# 嵌套with语句
print("\n方法1: 嵌套with语句")
with ResourceA() as a:
    with ResourceB() as b:
        a.do_something()
        b.do_something()

# Python 3.1+的多上下文管理器语法
print("\n方法2: 多上下文管理器语法")
with ResourceA() as a, ResourceB() as b:
    a.do_something()
    b.do_something()

# 4. contextlib中的其他实用工具
from contextlib import closing, suppress, redirect_stdout, redirect_stderr
import io
import sys

# closing - 确保对象被关闭
print("\n=== contextlib.closing ===")

class NetworkConnection:
    def __init__(self, address):
        self.address = address
        print(f"连接到: {address}")
    
    def send(self, data):
        print(f"发送数据到 {self.address}: {data}")
    
    def close(self):
        print(f"关闭连接: {self.address}")

# 使用closing确保连接被关闭
with closing(NetworkConnection("example.com")) as conn:
    conn.send("Hello, Server!")

# suppress - 抑制特定异常
print("\n=== contextlib.suppress ===")

with suppress(FileNotFoundError):
    # 如果文件不存在，不会抛出异常
    with open("non_existent_file.txt") as f:
        content = f.read()
    print("这段代码不会执行")
print("继续执行后续代码")

# redirect_stdout - 重定向标准输出
print("\n=== contextlib.redirect_stdout ===")

output_buffer = io.StringIO()
with redirect_stdout(output_buffer):
    print("这段输出会被重定向到缓冲区")
    print("而不是显示在控制台")

# 获取重定向的输出
redirected_output = output_buffer.getvalue()
print(f"从缓冲区获取的输出: '{redirected_output.strip()}'")

# 5. 自定义复合上下文管理器
print("\n=== 自定义复合上下文管理器 ===")

class TransactionManager:
    """数据库事务管理器示例"""
    
    def __init__(self, db):
        self.db = db
        self.committed = False
    
    def __enter__(self):
        print("开始事务")
        self.db.begin_transaction()
        return self
    
    def commit(self):
        print("提交事务")
        self.db.commit_transaction()
        self.committed = True
    
    def rollback(self):
        print("回滚事务")
        self.db.rollback_transaction()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 如果没有显式提交且没有异常，则自动提交
        if not self.committed and exc_type is None:
            self.commit()
        # 如果有异常，则回滚
        elif exc_type is not None:
            self.rollback()
        print("事务结束")
        return False  # 不抑制异常

# 模拟数据库类
class MockDatabase:
    def begin_transaction(self):
        print("数据库开始事务")
    
    def commit_transaction(self):
        print("数据库提交事务")
    
    def rollback_transaction(self):
        print("数据库回滚事务")
    
    def execute(self, query):
        print(f"执行SQL: {query}")

# 使用事务管理器
db = MockDatabase()

print("\n正常事务示例:")
try:
    with TransactionManager(db) as tx:
        db.execute("INSERT INTO users VALUES (1, 'Alice')")
        db.execute("UPDATE accounts SET balance = balance - 100 WHERE user_id = 1")
        tx.commit()  # 显式提交
except Exception as e:
    print(f"捕获到异常: {e}")

print("\n异常事务示例:")
try:
    with TransactionManager(db) as tx:
        db.execute("INSERT INTO users VALUES (2, 'Bob')")
        # 故意引发异常
        raise ValueError("模拟数据库错误")
        db.execute("这行代码不会执行")
except Exception as e:
    print(f"捕获到异常: {e}")
```

## 5. Python 2与Python 3的核心差异

### 5.1 语法与语言特性差异
**[标识: CORE-DIFFERENCE-001]**

Python 3引入了许多语法改进和语言特性变化，了解这些差异有助于编写兼容的代码。

```python
# Python 2与Python 3核心差异示例

# 注意：以下代码分别展示Python 2和Python 3的特性，不能在同一解释器中全部执行

# 1. 打印函数

# Python 2:
# print "Hello, World!"
# print "Multiple", "arguments", "like", "this"

# Python 3:
print("Hello, World!")
print("Multiple", "arguments", "like", "this")

# 2. 整数除法

# Python 2:
# 3 / 2  # 返回 1 (整数除法)
# 3 // 2  # 返回 1 (地板除法)
# 3.0 / 2  # 返回 1.5 (浮点除法)

# Python 3:
print(3 / 2)  # 返回 1.5 (浮点除法)
print(3 // 2)  # 返回 1 (地板除法)

# 3. 字符串与字节

# Python 2:
# str 类型是字节字符串
# unicode 类型是Unicode字符串

# Python 3:
print(type("Hello"))  # <class 'str'> - Unicode字符串
print(type(b"Hello"))  # <class 'bytes'> - 字节字符串

# 编码/解码示例
text = "你好，世界"
encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')
print(f"原始文本: {text}")
print(f"编码后: {encoded}")
print(f"解码后: {decoded}")

# 4. 迭代器行为

# Python 2:
# range(10) 返回列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# xrange(10) 返回迭代器

# Python 3:
print(type(range(10)))  # <class 'range'> - 类似于Python 2的xrange
print(list(range(5)))  # 转换为列表: [0, 1, 2, 3, 4]

# 5. 异常处理

# Python 2:
# try:
#     x = 1 / 0
# except ZeroDivisionError, e:
#     print "Error:", e

# Python 3:
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# 6. next()函数与迭代器

# Python 2:
# iter_obj.next()  # 调用迭代器的next方法

# Python 3:
iter_obj = iter([1, 2, 3])
print(next(iter_obj))  # 使用内置的next()函数
print(next(iter_obj))
print(next(iter_obj))

# 7. 函数参数

# Python 2:
# def func(a, b, *args, **kwargs):
#     pass

# Python 3: 支持仅限关键字参数
def func(a, b, *, c=None):  # c是仅限关键字参数
    print(f"a={a}, b={b}, c={c}")

func(1, 2, c=3)  # 正确
# func(1, 2, 3)  # 错误：c必须作为关键字参数传递

# 8. 非局部变量声明

# Python 2:
# 没有nonlocal关键字，只能在闭包中修改可变对象

# Python 3:
def outer():
    x = 10
    def inner():
        nonlocal x  # 声明x为非局部变量
        x += 5
        print(f"内部函数: x = {x}")
    inner()
    print(f"外部函数: x = {x}")

outer()

# 9. 类定义

# Python 2:
# class OldStyleClass:  # 旧式类
#     pass
# 
# class NewStyleClass(object):  # 新式类需要显式继承object
#     pass

# Python 3:
class MyClass:  # 所有类默认都是新式类
    pass

print(MyClass.__mro__)  # 查看方法解析顺序

# 10. 高级解包

# Python 2:
# 不支持扩展的解包语法

# Python 3:
a, *b, c = [1, 2, 3, 4, 5]
print(f"a = {a}, b = {b}, c = {c}")  # a = 1, b = [2, 3, 4], c = 5

# 11. 字典合并

# Python 2:
# 字典合并需要使用update方法

# Python 3.5+:
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(f"合并后的字典: {merged_dict}")

# 12. 异步语法支持

# Python 2:
# 不支持原生异步语法

# Python 3.5+:
# async def async_function():
#     await some_async_operation()

# 13. 类型注解

# Python 2:
# 不支持原生类型注解

# Python 3.5+:
def typed_function(x: int, y: str) -> bool:
    return y in str(x)

print(typed_function(123, "2"))  # True
print(typed_function.__annotations__)
```

### 5.2 兼容性策略与最佳实践
**[标识: CORE-DIFFERENCE-002]**

在需要同时支持Python 2和Python 3的项目中，采用适当的兼容性策略至关重要。

```python
# Python 2与Python 3兼容性最佳实践

# 1. 使用__future__导入确保Python 2行为更接近Python 3
# 在Python 2文件的顶部添加:
# from __future__ import (absolute_import, division, print_function, unicode_literals)

# 2. 使用six库实现兼容性
# 安装: pip install six

# 示例:
'''
import six

# 字符串处理
if six.PY2:
    text_type = unicode
    binary_type = str
else:
    text_type = str
    binary_type = bytes

# 迭代器处理
for item in six.iteritems(some_dict):
    pass

# 异常处理
try:
    pass
except Exception as e:  # Python 3语法
except Exception, e:  # Python 2语法
    pass
'''

# 3. 使用future库提供更多Python 3功能到Python 2
# 安装: pip install future

# 4. 使用兼容型导入

def compatibility_imports():
    try:
        # Python 3
        from urllib.request import urlopen
        from urllib.error import URLError
    except ImportError:
        # Python 2
        from urllib2 import urlopen, URLError
    
    try:
        # Python 3
        from configparser import ConfigParser
    except ImportError:
        # Python 2
        from ConfigParser import ConfigParser
    
    try:
        # Python 3
        from io import StringIO, BytesIO
    except ImportError:
        # Python 2
        from StringIO import StringIO
        from io import BytesIO
    
    return urlopen, URLError, ConfigParser, StringIO, BytesIO

# 5. 兼容型代码示例
def compatibility_example():
    # 获取兼容的导入
    urlopen, URLError, ConfigParser, StringIO, BytesIO = compatibility_imports()
    
    # 字符串处理兼容性
    def to_unicode(text):
        """将输入转换为Unicode字符串"""
        try:
            # Python 2
            if isinstance(text, str):
                return text.decode('utf-8')
            elif isinstance(text, unicode):
                return text
        except NameError:
            # Python 3
            if isinstance(text, bytes):
                return text.decode('utf-8')
            elif isinstance(text, str):
                return text
        return str(text)
    
    def to_bytes(text):
        """将输入转换为字节字符串"""
        try:
            # Python 2
            if isinstance(text, unicode):
                return text.encode('utf-8')
            elif isinstance(text, str):
                return text
        except NameError:
            # Python 3
            if isinstance(text, str):
                return text.encode('utf-8')
            elif isinstance(text, bytes):
                return text
        return bytes(str(text), 'utf-8')
    
    # 测试字符串转换
    test_str = "你好，世界"
    unicode_str = to_unicode(test_str)
    bytes_str = to_bytes(test_str)
    
    print(f"原始字符串类型: {type(test_str).__name__}")
    print(f"Unicode转换后类型: {type(unicode_str).__name__}")
    print(f"字节转换后类型: {type(bytes_str).__name__}")
    
    # 异常处理兼容性
try:
    # 代码执行
    pass
except Exception as e:  # Python 3语法
    # 在Python 2中，这会将异常赋值给变量e
    error_message = str(e)

# 6. 测试策略
'''
# 使用tox进行多版本测试
# tox.ini配置示例:
'''

# 7. 逐步迁移策略
'''
1. 首先让代码在Python 2.7上运行良好
2. 添加__future__导入
3. 使用兼容性库(six, future)
4. 运行测试确保在Python 2.7上仍然正常工作
5. 在Python 3环境中测试并修复问题
6. 持续维护双版本兼容性直到完全迁移到Python 3
'''

# 8. 常见兼容性陷阱及解决方案

def compatibility_pitfalls():
    """常见兼容性陷阱及解决方案"""
    
    # 陷阱1: 整数除法
    # 解决方案: 使用from __future__ import division
    
    # 陷阱2: 字符串和字节混用
    # 解决方案: 显式编码/解码，使用to_unicode()和to_bytes()辅助函数
    
    # 陷阱3: 迭代器和列表
    # 解决方案: 需要列表时显式转换，如list(range(10))
    
    # 陷阱4: 异常处理语法
    # 解决方案: 使用Python 3语法，它在Python 2.6+上也可以工作
    
    # 陷阱5: 类定义
    # 解决方案: 在Python 2中显式继承object，在Python 3中无需担心
    
    # 陷阱6: next()方法
    # 解决方案: 使用内置的next()函数，它在两个版本中都可用
    
    print("Python 2与Python 3兼容性陷阱及解决方案总结完成")

# 运行兼容性示例
compatibility_example()
compatibility_pitfalls()

# 9. 推荐的迁移工具
'''
- futurize: 将Python 2代码转换为兼容Python 2和3的代码
- modernize: 将Python 2代码现代化，使用six库
- 2to3: 将Python 2代码转换为Python 3代码（不保持向后兼容）
'''

# 10. 完全迁移到Python 3后的清理
'''
1. 移除__future__导入
2. 移除six库的使用，使用Python 3原生功能
3. 更新类型注解
4. 使用Python 3特有的功能（如f-string、异步语法等）
'''

print("\nPython 2与Python 3兼容性策略和最佳实践示例完成")
```