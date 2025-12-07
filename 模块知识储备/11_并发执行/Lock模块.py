#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lock模块 - 线程同步的锁机制

Lock模块是threading模块中用于线程同步的核心组件，提供了基本的互斥锁功能。

主要功能包括：
- 互斥锁（Lock）：最基本的锁机制
- 可重入锁（RLock）：允许同一线程多次获取的锁
- 锁的获取和释放
- 上下文管理器支持

使用场景：
- 保护共享资源的访问
- 防止竞态条件
- 确保临界区的原子执行

官方文档：https://docs.python.org/3/library/threading.html#lock-objects
"""

import threading
import time
import random

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. Lock模块基本介绍")
print("=" * 50)
print("Lock模块提供线程同步的锁机制")
print("主要包括Lock（互斥锁）和RLock（可重入锁）")
print("用于保护共享资源，防止竞态条件")
print("支持上下文管理器（with语句）")
print("适用于多线程环境下的资源访问控制")

# ===========================
# 2. 互斥锁 (Lock)
# ===========================
print("\n" + "=" * 50)
print("2. 互斥锁 (Lock)")
print("=" * 50)

# 示例1: 没有锁保护的共享资源访问
print("示例1: 没有锁保护的共享资源访问")

shared_counter = 0
def increment_without_lock():
    global shared_counter
    for _ in range(1000):
        # 模拟一些计算
        temp = shared_counter
        time.sleep(0.0001)  # 增加竞态条件发生的概率
        shared_counter = temp + 1

# 创建多个线程同时修改共享变量
threads = []
for i in range(10):
    thread = threading.Thread(target=increment_without_lock)
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print(f"没有锁保护的结果: {shared_counter}")
print(f"预期结果: {10 * 1000}")
print("可以看到结果小于预期，说明发生了竞态条件")

# 示例2: 使用Lock保护共享资源访问
print("\n示例2: 使用Lock保护共享资源访问")

shared_counter = 0
lock = threading.Lock()

def increment_with_lock():
    global shared_counter
    for _ in range(1000):
        with lock:  # 使用上下文管理器获取和释放锁
            temp = shared_counter
            time.sleep(0.0001)
            shared_counter = temp + 1

# 创建多个线程同时修改共享变量
threads = []
for i in range(10):
    thread = threading.Thread(target=increment_with_lock)
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print(f"有锁保护的结果: {shared_counter}")
print(f"预期结果: {10 * 1000}")
print("结果与预期一致，说明锁成功保护了共享资源")

# 示例3: 手动获取和释放锁
print("\n示例3: 手动获取和释放锁")

manual_lock = threading.Lock()
shared_resource = []

def access_resource(thread_id):
    try:
        # 手动获取锁
        manual_lock.acquire()
        print(f"线程 {thread_id} 获取了锁")
        
        # 访问共享资源
        shared_resource.append(thread_id)
        print(f"线程 {thread_id} 修改了共享资源: {shared_resource}")
        
        # 模拟处理时间
        time.sleep(0.5)
        
    finally:
        # 确保锁被释放
        manual_lock.release()
        print(f"线程 {thread_id} 释放了锁")

# 创建并启动线程
for i in range(3):
    threading.Thread(target=access_resource, args=(i,)).start()
    time.sleep(0.1)

# 等待所有线程完成
time.sleep(3)

# ===========================
# 3. 可重入锁 (RLock)
# ===========================
print("\n" + "=" * 50)
print("3. 可重入锁 (RLock)")
print("=" * 50)

# 示例4: 可重入锁的基本使用
print("示例4: 可重入锁的基本使用")

reentrant_lock = threading.RLock()

def outer_function(thread_id):
    with reentrant_lock:
        print(f"线程 {thread_id} 在外部函数获取了RLock")
        time.sleep(0.2)
        inner_function(thread_id)
        print(f"线程 {thread_id} 在外部函数释放了RLock")

def inner_function(thread_id):
    with reentrant_lock:
        print(f"线程 {thread_id} 在内部函数获取了RLock")
        time.sleep(0.2)
        print(f"线程 {thread_id} 在内部函数释放了RLock")

# 测试RLock
for i in range(2):
    threading.Thread(target=outer_function, args=(i,)).start()
    time.sleep(0.1)

# 等待所有线程完成
time.sleep(3)

# 示例5: Lock与RLock的区别
print("\n示例5: Lock与RLock的区别")

normal_lock = threading.Lock()
reentrant_lock2 = threading.RLock()

def try_normal_lock():
    print("尝试使用普通Lock进行嵌套获取")
    try:
        normal_lock.acquire()
        print("第一次获取Lock成功")
        
        # 尝试再次获取同一个Lock，这会导致死锁
        normal_lock.acquire()
        print("第二次获取Lock成功")
        
    except Exception as e:
        print(f"发生异常: {e}")
    finally:
        # 释放锁
        if normal_lock.locked():
            normal_lock.release()
            print("释放了一个Lock")

def try_reentrant_lock():
    print("\n尝试使用RLock进行嵌套获取")
    try:
        reentrant_lock2.acquire()
        print("第一次获取RLock成功")
        
        # 尝试再次获取同一个RLock，这会成功
        reentrant_lock2.acquire()
        print("第二次获取RLock成功")
        
        # 释放两次锁
        reentrant_lock2.release()
        print("第一次释放RLock")
        reentrant_lock2.release()
        print("第二次释放RLock")
        
    except Exception as e:
        print(f"发生异常: {e}")
    finally:
        # 确保所有锁都被释放
        while reentrant_lock2.locked():
            reentrant_lock2.release()
            print("额外释放了一个RLock")

# 注意：try_normal_lock会导致死锁，这里只演示RLock的使用
# threading.Thread(target=try_normal_lock).start()
try_reentrant_lock()

# ===========================
# 4. 锁的状态查询
# ===========================
print("\n" + "=" * 50)
print("4. 锁的状态查询")
print("=" * 50)

# 示例6: 查询锁的状态
print("示例6: 查询锁的状态")

status_lock = threading.Lock()
print(f"锁是否已被获取: {status_lock.locked()}")

# 获取锁
status_lock.acquire()
print(f"获取锁后，锁是否已被获取: {status_lock.locked()}")

# 释放锁
status_lock.release()
print(f"释放锁后，锁是否已被获取: {status_lock.locked()}")

# 示例7: RLock的拥有者查询
print("\n示例7: RLock的拥有者查询")

owner_lock = threading.RLock()

def check_owner(thread_id):
    with owner_lock:
        print(f"线程 {thread_id} 获取了锁")
        print(f"线程 {thread_id} 是锁的拥有者: {owner_lock._is_owned()}")

# 测试拥有者查询
threading.Thread(target=check_owner, args=(0,)).start()
time.sleep(1)

# ===========================
# 5. 锁的实际应用示例
# ===========================
print("\n" + "=" * 50)
print("5. 锁的实际应用示例")
print("=" * 50)

# 示例8: 银行账户转账（使用锁保护）
print("示例8: 银行账户转账（使用锁保护）")

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()
    
    def deposit(self, amount):
        with self.lock:
            print(f"存款: {amount}, 当前余额: {self.balance}")
            self.balance += amount
            print(f"存款后余额: {self.balance}")
            return self.balance
    
    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"取款: {amount}, 当前余额: {self.balance}")
                self.balance -= amount
                print(f"取款后余额: {self.balance}")
                return True, self.balance
            else:
                print(f"取款失败: 余额不足 {amount}, 当前余额: {self.balance}")
                return False, self.balance
    
    def transfer(self, target_account, amount):
        # 先获取自己的锁，再获取目标账户的锁
        with self.lock:
            success, _ = self.withdraw(amount)
            if success:
                with target_account.lock:
                    target_account.deposit(amount)
                    print(f"转账成功: {amount} 从账户1转到账户2")
                    return True
        return False

# 创建两个银行账户
account1 = BankAccount(1000)
account2 = BankAccount(500)

# 定义转账函数
def transfer_task():
    for _ in range(5):
        amount = random.randint(100, 300)
        account1.transfer(account2, amount)
        time.sleep(0.2)

# 定义存款函数
def deposit_task(account):
    for _ in range(5):
        amount = random.randint(100, 200)
        account.deposit(amount)
        time.sleep(0.1)

# 创建多个线程同时操作账户
threads = [
    threading.Thread(target=transfer_task),
    threading.Thread(target=deposit_task, args=(account1,)),
    threading.Thread(target=deposit_task, args=(account2,))
]

# 启动线程
for thread in threads:
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print(f"最终账户1余额: {account1.balance}")
print(f"最终账户2余额: {account2.balance}")
print(f"总余额: {account1.balance + account2.balance}")
print(f"初始总余额: {1000 + 500}")

# 示例9: 线程安全的计数器类
print("\n示例9: 线程安全的计数器类")

class ThreadSafeCounter:
    def __init__(self, initial_value=0):
        self.value = initial_value
        self.lock = threading.Lock()
    
    def increment(self, delta=1):
        with self.lock:
            self.value += delta
            return self.value
    
    def decrement(self, delta=1):
        with self.lock:
            self.value -= delta
            return self.value
    
    def get_value(self):
        with self.lock:
            return self.value
    
    def reset(self, value=0):
        with self.lock:
            self.value = value
            return self.value

# 使用线程安全的计数器
counter = ThreadSafeCounter()

def count_up():
    for _ in range(1000):
        counter.increment()

def count_down():
    for _ in range(500):
        counter.decrement()

# 创建线程
threads = []
for _ in range(10):
    threads.append(threading.Thread(target=count_up))
for _ in range(5):
    threads.append(threading.Thread(target=count_down))

# 启动线程
for thread in threads:
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print(f"最终计数器值: {counter.get_value()}")
print(f"预期值: {10 * 1000 - 5 * 500} = {10*1000-5*500}")

# 示例10: 多线程文件写入保护
print("\n示例10: 多线程文件写入保护")

# 创建文件锁
file_lock = threading.Lock()

def write_to_file(thread_id):
    with file_lock:
        with open("thread_output.txt", "a") as f:
            f.write(f"线程 {thread_id} 开始写入\n")
            time.sleep(0.1)  # 模拟写入过程
            f.write(f"线程 {thread_id} 完成写入\n")
        print(f"线程 {thread_id} 完成文件写入")

# 启动多个线程写入文件
for i in range(5):
    threading.Thread(target=write_to_file, args=(i,)).start()

# 等待所有线程完成
time.sleep(3)

# ===========================
# 6. 死锁及其避免
# ===========================
print("\n" + "=" * 50)
print("6. 死锁及其避免")
print("=" * 50)

# 示例11: 死锁演示（注释掉以避免实际死锁）
print("示例11: 死锁演示")

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_function1():
    print("线程1: 尝试获取lock1")
    with lock1:
        print("线程1: 获取到lock1")
        time.sleep(0.5)
        
        print("线程1: 尝试获取lock2")
        with lock2:
            print("线程1: 获取到lock2")
    print("线程1: 释放了所有锁")

def thread_function2():
    print("线程2: 尝试获取lock2")
    with lock2:
        print("线程2: 获取到lock2")
        time.sleep(0.5)
        
        print("线程2: 尝试获取lock1")
        with lock1:
            print("线程2: 获取到lock1")
    print("线程2: 释放了所有锁")

print("注意: 以下代码会导致死锁，已注释掉")
print("线程1持有lock1并等待lock2")
print("线程2持有lock2并等待lock1")
print("两者互相等待，导致死锁")

# 不要运行以下代码，会导致死锁
# t1 = threading.Thread(target=thread_function1)
# t2 = threading.Thread(target=thread_function2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# 示例12: 避免死锁 - 按固定顺序获取锁
print("\n示例12: 避免死锁 - 按固定顺序获取锁")

def thread_safe_function1():
    print("线程1: 按顺序获取lock1 -> lock2")
    with lock1:
        print("线程1: 获取到lock1")
        time.sleep(0.5)
        
        with lock2:
            print("线程1: 获取到lock2")
    print("线程1: 释放了所有锁")

def thread_safe_function2():
    print("线程2: 按顺序获取lock1 -> lock2")
    with lock1:  # 同样先获取lock1，再获取lock2
        print("线程2: 获取到lock1")
        time.sleep(0.5)
        
        with lock2:
            print("线程2: 获取到lock2")
    print("线程2: 释放了所有锁")

# 创建并启动线程
t1 = threading.Thread(target=thread_safe_function1)
t2 = threading.Thread(target=thread_safe_function2)
t1.start()
t2.start()

# 等待线程完成
t1.join()
t2.join()

print("按固定顺序获取锁避免了死锁")

# 示例13: 避免死锁 - 使用超时机制
print("\n示例13: 避免死锁 - 使用超时机制")

def thread_with_timeout(thread_id, lock_a, lock_b):
    try:
        # 尝试获取第一个锁，超时1秒
        if lock_a.acquire(timeout=1):
            try:
                print(f"线程 {thread_id}: 获取到第一个锁")
                time.sleep(0.5)
                
                # 尝试获取第二个锁，超时1秒
                if lock_b.acquire(timeout=1):
                    try:
                        print(f"线程 {thread_id}: 获取到第二个锁")
                    finally:
                        lock_b.release()
                else:
                    print(f"线程 {thread_id}: 获取第二个锁超时")
            finally:
                lock_a.release()
        else:
            print(f"线程 {thread_id}: 获取第一个锁超时")
            
    except Exception as e:
        print(f"线程 {thread_id}: 发生异常: {e}")

# 创建新的锁
lock_a = threading.Lock()
lock_b = threading.Lock()

# 启动线程
t1 = threading.Thread(target=thread_with_timeout, args=(1, lock_a, lock_b))
t2 = threading.Thread(target=thread_with_timeout, args=(2, lock_b, lock_a))
t1.start()
t2.start()

# 等待线程完成
t1.join()
t2.join()

print("使用超时机制避免了死锁")

# ===========================
# 7. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("7. 最佳实践")
print("=" * 50)

print("1. 锁的使用原则")
print("   - 只在必要时使用锁")
print("   - 尽量缩小锁的作用范围")
print("   - 避免在持有锁时执行阻塞操作")
print("   - 始终使用try/finally或上下文管理器释放锁")

print("\n2. Lock vs RLock选择")
print("   - 使用Lock：简单的临界区保护，不需要嵌套获取")
print("   - 使用RLock：需要在同一个线程中多次获取锁的情况")
print("   - 注意：RLock的性能略低于Lock")

print("\n3. 死锁避免策略")
print("   - 按固定顺序获取锁")
print("   - 使用超时机制")
print("   - 避免嵌套锁")
print("   - 使用锁的层级")
print("   - 考虑使用更高级的同步原语")

print("\n4. 性能优化")
print("   - 减少锁的持有时间")
print("   - 避免锁竞争")
print("   - 考虑使用无锁数据结构")
print("   - 对于读多写少的场景，考虑使用RLock或Reader-Writer锁")

print("\n5. 调试建议")
print("   - 使用threading模块的调试功能")
print("   - 添加适当的日志记录锁的获取和释放")
print("   - 考虑使用可视化工具分析锁的使用情况")
print("   - 对于复杂情况，考虑使用死锁检测工具")

# ===========================
# 8. 总结
# ===========================
print("\n" + "=" * 50)
print("8. 总结")
print("=" * 50)
print("Lock模块提供了基本的线程同步机制")
print("主要包括Lock（互斥锁）和RLock（可重入锁）")
print("用于保护共享资源，防止竞态条件")

print("\n主要功能:")
print("- 互斥访问共享资源")
print("- 支持上下文管理器")
print("- 可重入锁支持嵌套获取")
print("- 提供锁状态查询")

print("\n应用场景:")
print("- 多线程共享资源访问控制")
print("- 防止竞态条件")
print("- 确保临界区的原子执行")
print("- 多线程文件操作保护")

print("\n使用注意事项:")
print("- 避免死锁")
print("- 最小化锁的作用范围")
print("- 选择合适的锁类型")
print("- 考虑性能影响")

print("\nLock模块是Python多线程编程中确保线程安全的重要工具")
print("合理使用锁可以保护共享资源，避免并发问题")
