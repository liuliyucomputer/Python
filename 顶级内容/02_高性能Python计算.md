# 高性能Python计算技术

## 1. 性能分析与优化基础

在开始优化Python代码之前，我们需要了解性能瓶颈在哪里，这需要使用性能分析工具。

### 1.1 使用内置的性能分析工具

```python
import cProfile
import pstats
import io

# 使用cProfile分析函数性能
def profile(func):
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats()
        print(s.getvalue())
        return result
    return wrapper

@profile
def slow_function():
    """一个需要优化的慢函数"""
    total = 0
    for i in range(1000000):
        total += i
    return total

slow_function()
```

### 1.2 使用line_profiler分析行级性能

```bash
# 安装line_profiler
pip install line_profiler
```

```python
# 添加装饰器@profile（不需要导入，line_profiler会注入这个装饰器）
@profile
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 在命令行中运行
# kernprof -l -v script_name.py
```

## 2. 优化Python代码

### 2.1 数据结构选择

选择适当的数据结构对性能影响重大：

```python
import time
import random

# 生成测试数据
data = [random.randint(1, 1000000) for _ in range(10000)]
search_items = [random.randint(1, 1000000) for _ in range(1000)]

# 使用列表查找
def search_list():
    start = time.time()
    found = 0
    for item in search_items:
        if item in data:  # O(n)操作
            found += 1
    end = time.time()
    print(f"列表搜索: 找到{found}项，耗时{end - start:.6f}秒")

# 使用集合查找
def search_set():
    # 转换为集合
    data_set = set(data)
    start = time.time()
    found = 0
    for item in search_items:
        if item in data_set:  # O(1)操作
            found += 1
    end = time.time()
    print(f"集合搜索: 找到{found}项，耗时{end - start:.6f}秒")

search_list()  # 较慢
search_set()   # 较快
```

### 2.2 列表推导式和生成器表达式

```python
import time

# 比较不同方法创建平方数列表的性能
def test_square_methods(n):
    # 使用for循环和append
    start = time.time()
    squares1 = []
    for i in range(n):
        squares1.append(i ** 2)
    t1 = time.time() - start
    
    # 使用列表推导式
    start = time.time()
    squares2 = [i ** 2 for i in range(n)]
    t2 = time.time() - start
    
    # 使用map函数
    start = time.time()
    squares3 = list(map(lambda x: x ** 2, range(n)))
    t3 = time.time() - start
    
    print(f"for循环+append: {t1:.6f}秒")
    print(f"列表推导式: {t2:.6f}秒")
    print(f"map+lambda: {t3:.6f}秒")

test_square_methods(10000000)
```

### 2.3 减少函数调用开销

```python
import time

# 测试函数调用开销
def test_function_calls(n):
    # 内联计算
    start = time.time()
    result1 = 0
    for i in range(n):
        result1 += i * i
    t1 = time.time() - start
    
    # 使用函数调用
    def square(x):
        return x * x
    
    start = time.time()
    result2 = 0
    for i in range(n):
        result2 += square(i)
    t2 = time.time() - start
    
    print(f"内联计算: {t1:.6f}秒")
    print(f"函数调用: {t2:.6f}秒")

test_function_calls(10000000)
```

### 2.4 局部变量优于全局变量

```python
import time

# 全局变量
x = 0

def increment_global(n):
    global x
    for i in range(n):
        x += 1

def increment_local(n):
    x = 0
    for i in range(n):
        x += 1
    return x

# 测试性能差异
def compare_variable_scope(n):
    start = time.time()
    increment_global(n)
    t1 = time.time() - start
    
    start = time.time()
    increment_local(n)
    t2 = time.time() - start
    
    print(f"全局变量: {t1:.6f}秒")
    print(f"局部变量: {t2:.6f}秒")

compare_variable_scope(10000000)
```

## 3. NumPy高性能数值计算

NumPy提供了高性能的数值计算能力，大大超过了纯Python实现：

```python
import time
import numpy as np

def compare_numpy_vs_python(n):
    # Python原生列表计算
    start = time.time()
    py_array = list(range(n))
    result_py = [x ** 2 for x in py_array]
    t1 = time.time() - start
    
    # NumPy计算
    start = time.time()
    np_array = np.arange(n)
    result_np = np_array ** 2
    t2 = time.time() - start
    
    print(f"Python列表: {t1:.6f}秒")
    print(f"NumPy数组: {t2:.6f}秒")
    print(f"NumPy比Python快: {t1/t2:.1f}倍")

compare_numpy_vs_python(10000000)
```

### 3.1 NumPy向量化操作

```python
import numpy as np
import time

# 比较循环和向量化操作
def compute_distance_loop(x, y):
    """使用循环计算两点之间的欧几里得距离"""
    n = len(x)
    result = 0
    for i in range(n):
        result += (x[i] - y[i]) ** 2
    return np.sqrt(result)

def compute_distance_vector(x, y):
    """使用NumPy向量化操作计算两点之间的欧几里得距离"""
    return np.sqrt(np.sum((x - y) ** 2))

# 生成测试数据
n = 1000000
x = np.random.random(n)
y = np.random.random(n)

# 测试循环版本
start = time.time()
d1 = compute_distance_loop(x, y)
t1 = time.time() - start

# 测试向量化版本
start = time.time()
d2 = compute_distance_vector(x, y)
t2 = time.time() - start

print(f"循环版本: {t1:.6f}秒")
print(f"向量化版本: {t2:.6f}秒")
print(f"向量化比循环快: {t1/t2:.1f}倍")
```

## 4. Numba JIT编译加速

Numba可以将Python代码编译成机器码，大幅提升性能：

```python
import time
import numpy as np
from numba import jit

# 没有优化的Python函数
def python_sum_array(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

# 使用Numba优化的相同函数
@jit(nopython=True)
def numba_sum_array(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

# 比较性能
def compare_numba_performance(n):
    # 创建测试数据
    data = np.random.random(n)
    
    # 测试Python版本
    start = time.time()
    result1 = python_sum_array(data)
    t1 = time.time() - start
    
    # 测试Numba版本（首次运行包括编译时间）
    start = time.time()
    result2 = numba_sum_array(data)
    t2 = time.time() - start
    
    # 再次测试Numba版本（不包括编译时间）
    start = time.time()
    result3 = numba_sum_array(data)
    t3 = time.time() - start
    
    print(f"Python版本: {t1:.6f}秒")
    print(f"Numba首次运行: {t2:.6f}秒")
    print(f"Numba后续运行: {t3:.6f}秒")
    print(f"Numba比Python快: {t1/t3:.1f}倍")

compare_numba_performance(10000000)
```

### 4.1 Numba并行处理

```python
from numba import jit, prange
import numpy as np
import time

# 串行版本
@jit(nopython=True)
def monte_carlo_pi_serial(nsamples):
    acc = 0
    for i in range(nsamples):
        x = np.random.random()
        y = np.random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

# 并行版本
@jit(nopython=True, parallel=True)
def monte_carlo_pi_parallel(nsamples):
    acc = 0
    # prange替代普通range，启用并行计算
    for i in prange(nsamples):
        x = np.random.random()
        y = np.random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

# 比较性能
def compare_parallel_performance():
    nsamples = 10000000
    
    # 测试串行版本
    start = time.time()
    pi_serial = monte_carlo_pi_serial(nsamples)
    t1 = time.time() - start
    
    # 测试并行版本
    start = time.time()
    pi_parallel = monte_carlo_pi_parallel(nsamples)
    t2 = time.time() - start
    
    print(f"蒙特卡洛方法估计π值:")
    print(f"串行版本: π ≈ {pi_serial:.8f}, 耗时: {t1:.6f}秒")
    print(f"并行版本: π ≈ {pi_parallel:.8f}, 耗时: {t2:.6f}秒")
    print(f"加速比: {t1/t2:.2f}倍")

compare_parallel_performance()
```

## 5. Cython: Python与C的结合

Cython允许将Python代码编译成C，显著提高性能：

```python
# 纯Python版本 (save as fibonacci_py.py)
def fibonacci(n):
    """计算斐波那契数列第n项"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

```cython
# Cython版本 (save as fibonacci_cy.pyx)
def fibonacci(int n):
    """计算斐波那契数列第n项"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

```python
# setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("fibonacci_cy.pyx")
)
```

```bash
# 编译Cython代码
python setup.py build_ext --inplace
```

```python
# 比较性能
import time
from fibonacci_py import fibonacci as fib_py
from fibonacci_cy import fibonacci as fib_cy

def compare_cython_performance():
    n = 30
    
    # 测试Python版本
    start = time.time()
    result1 = fib_py(n)
    t1 = time.time() - start
    
    # 测试Cython版本
    start = time.time()
    result2 = fib_cy(n)
    t2 = time.time() - start
    
    print(f"Python版本: {t1:.6f}秒")
    print(f"Cython版本: {t2:.6f}秒")
    print(f"Cython比Python快: {t1/t2:.1f}倍")

compare_cython_performance()
```

## 6. 并行计算技术

### 6.1 多线程与多进程

```python
import time
import numpy as np
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from functools import partial

def heavy_computation(matrix):
    """执行矩阵操作（CPU密集型）"""
    result = np.linalg.matrix_power(matrix, 2)
    return np.sum(result)

def process_matrices(matrices, executor_type='thread'):
    """处理多个矩阵，使用线程或进程"""
    if executor_type == 'thread':
        executor_class = ThreadPoolExecutor
    else:  # 'process'
        executor_class = ProcessPoolExecutor
    
    start = time.time()
    with executor_class(max_workers=4) as executor:
        results = list(executor.map(heavy_computation, matrices))
    end = time.time()
    
    return results, end - start

# 创建测试数据
n_matrices = 10
size = 500
matrices = [np.random.rand(size, size) for _ in range(n_matrices)]

# 串行处理
start = time.time()
serial_results = [heavy_computation(m) for m in matrices]
serial_time = time.time() - start

# 多线程处理（对于NumPy操作，可能因GIL而没有加速）
thread_results, thread_time = process_matrices(matrices, 'thread')

# 多进程处理
process_results, process_time = process_matrices(matrices, 'process')

print(f"串行处理: {serial_time:.6f}秒")
print(f"多线程处理: {thread_time:.6f}秒, 加速比: {serial_time/thread_time:.2f}倍")
print(f"多进程处理: {process_time:.6f}秒, 加速比: {serial_time/process_time:.2f}倍")
```

### 6.2 使用Dask进行分布式计算

```python
import numpy as np
import time
import dask.array as da

def compare_dask_performance():
    size = 20000
    
    # NumPy计算
    start = time.time()
    x_np = np.random.random((size, size))
    result_np = np.mean(x_np, axis=0)
    np_time = time.time() - start
    
    # Dask计算
    start = time.time()
    x_dask = da.random.random((size, size), chunks=(1000, 1000))
    result_dask = x_dask.mean(axis=0).compute()
    dask_time = time.time() - start
    
    print(f"NumPy计算: {np_time:.6f}秒")
    print(f"Dask计算: {dask_time:.6f}秒")
    print(f"差异: {np.allclose(result_np, result_dask)}")
    
compare_dask_performance()
```

## 7. GPU加速计算

### 7.1 使用RAPIDS进行GPU加速

```python
# 需要安装RAPIDS库：https://rapids.ai/
import cudf
import pandas as pd
import numpy as np
import time

def compare_gpu_cpu_performance():
    # 创建大型数据集
    size = 10000000
    df_cpu = pd.DataFrame({
        'A': np.random.randint(0, 100, size),
        'B': np.random.randint(0, 100, size),
        'C': np.random.random(size)
    })
    
    # CPU操作
    start = time.time()
    result_cpu = df_cpu.groupby(['A', 'B']).C.mean()
    cpu_time = time.time() - start
    
    # 转换到GPU
    start = time.time()
    df_gpu = cudf.DataFrame.from_pandas(df_cpu)
    result_gpu = df_gpu.groupby(['A', 'B']).C.mean().to_pandas()
    gpu_time = time.time() - start
    
    print(f"CPU计算: {cpu_time:.6f}秒")
    print(f"GPU计算: {gpu_time:.6f}秒")
    print(f"GPU比CPU快: {cpu_time/gpu_time:.1f}倍")
    
compare_gpu_cpu_performance()
```

### 7.2 使用CuPy进行NumPy风格的GPU计算

```python
import numpy as np
import cupy as cp
import time

def compare_numpy_cupy():
    size = 8000
    
    # NumPy计算
    start = time.time()
    a_np = np.random.random((size, size))
    b_np = np.random.random((size, size))
    c_np = np.dot(a_np, b_np)
    np_time = time.time() - start
    
    # CuPy计算
    start = time.time()
    a_cp = cp.random.random((size, size))
    b_cp = cp.random.random((size, size))
    c_cp = cp.dot(a_cp, b_cp)
    cp.cuda.Stream.null.synchronize()  # 确保GPU计算完成
    cp_time = time.time() - start
    
    print(f"NumPy矩阵乘法: {np_time:.6f}秒")
    print(f"CuPy矩阵乘法: {cp_time:.6f}秒")
    print(f"CuPy比NumPy快: {np_time/cp_time:.1f}倍")

compare_numpy_cupy()
```

## 8. 实际项目案例：图像处理性能优化

```python
import numpy as np
import time
from PIL import Image
from numba import jit
import cv2

# 加载图像
image_path = "large_image.jpg"  # 替换为实际图像路径
img = np.array(Image.open(image_path))

# 纯Python实现的高斯模糊
def gaussian_blur_python(img, kernel_size=5, sigma=1.0):
    """使用纯Python实现高斯模糊"""
    height, width, channels = img.shape
    result = np.zeros_like(img, dtype=np.float32)
    
    # 创建高斯核
    k = kernel_size // 2
    kernel = np.zeros((kernel_size, kernel_size), dtype=np.float32)
    for i in range(kernel_size):
        for j in range(kernel_size):
            x, y = i - k, j - k
            kernel[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    kernel /= np.sum(kernel)
    
    # 应用卷积
    for c in range(channels):
        for i in range(k, height - k):
            for j in range(k, width - k):
                for ki in range(kernel_size):
                    for kj in range(kernel_size):
                        result[i, j, c] += img[i + ki - k, j + kj - k, c] * kernel[ki, kj]
    
    return result.astype(np.uint8)

# Numba加速版本
@jit(nopython=True)
def gaussian_blur_numba(img, kernel_size=5, sigma=1.0):
    """使用Numba加速的高斯模糊"""
    height, width, channels = img.shape
    result = np.zeros_like(img, dtype=np.float32)
    
    # 创建高斯核
    k = kernel_size // 2
    kernel = np.zeros((kernel_size, kernel_size), dtype=np.float32)
    for i in range(kernel_size):
        for j in range(kernel_size):
            x, y = i - k, j - k
            kernel[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    kernel /= np.sum(kernel)
    
    # 应用卷积
    for c in range(channels):
        for i in range(k, height - k):
            for j in range(k, width - k):
                for ki in range(kernel_size):
                    for kj in range(kernel_size):
                        result[i, j, c] += img[i + ki - k, j + kj - k, c] * kernel[ki, kj]
    
    return result.astype(np.uint8)

# OpenCV实现
def gaussian_blur_cv2(img, kernel_size=5, sigma=1.0):
    """使用OpenCV实现高斯模糊"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)

# 比较性能
def compare_blur_implementations():
    # 裁剪图像以加快测试速度
    test_img = img[:500, :500, :]
    
    # Python版本
    start = time.time()
    blur_python = gaussian_blur_python(test_img)
    t_python = time.time() - start
    
    # Numba版本
    start = time.time()
    blur_numba = gaussian_blur_numba(test_img)
    t_numba = time.time() - start
    
    # OpenCV版本
    start = time.time()
    blur_cv2 = gaussian_blur_cv2(test_img)
    t_cv2 = time.time() - start
    
    print(f"Python实现: {t_python:.6f}秒")
    print(f"Numba实现: {t_numba:.6f}秒, 比Python快{t_python/t_numba:.1f}倍")
    print(f"OpenCV实现: {t_cv2:.6f}秒, 比Python快{t_python/t_cv2:.1f}倍")

compare_blur_implementations()
```

## 9. 性能优化策略总结

1. **总是进行性能分析**：在优化前，使用性能分析工具找出真正的瓶颈
2. **选择合适的数据结构**：不同操作需要不同的数据结构
3. **使用NumPy进行数值计算**：向量化操作比Python循环快得多
4. **考虑JIT编译**：使用Numba可以显著提升数值计算性能
5. **对于CPU密集型任务，使用多进程**：规避GIL限制
6. **对于IO密集型任务，使用异步或多线程**：提高并发性能
7. **考虑GPU加速**：对于大规模数值计算，GPU可提供巨大加速
8. **使用专业库**：尽可能使用优化过的专业库，而不是重新发明轮子
9. **了解并规避Python的性能陷阱**：如全局变量、函数调用开销等
10. **权衡可读性和性能**：不要为了微小的性能提升而牺牲代码可读性

## 10. 实际练习

### 练习1：优化素数计算
实现并比较不同方法计算前N个素数的性能。

### 练习2：实现高性能矩阵运算
使用不同技术（纯Python、NumPy、Numba、CuPy）实现矩阵乘法，并比较性能。

### 练习3：并行处理大数据
实现一个程序，使用多进程并行处理大型文本文件中的单词统计。

### 练习4：图像处理优化
对比使用不同方法（PIL、NumPy、OpenCV）实现图像滤镜的性能差异。
