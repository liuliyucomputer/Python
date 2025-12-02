#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
数据结构模块综合示例代码

本文件演示了如何组合使用Python的多个数据结构模块（itertools、operator、collections、heapq、functools）
来解决实际的复杂问题，展示它们协同工作的强大能力。

作者: Python数据结构教程
日期: 2023-11-28
"""

import itertools
import operator
import collections
import heapq
import functools
import time
import random
from pprint import pprint


def example_data_processing_pipeline():
    """示例1: 高效数据处理管道"""
    print("=== 示例1: 高效数据处理管道 ===")
    
    # 模拟电商订单数据
    print("生成模拟电商订单数据...")
    
    # 生成模拟数据
    def generate_order_data(num_orders=1000):
        """生成模拟订单数据"""
        products = ["手机", "笔记本电脑", "耳机", "平板电脑", "智能手表", 
                   "相机", "游戏机", "显示器", "键盘", "鼠标"]
        customers = [f"customer_{i}" for i in range(1, 51)]
        
        orders = []
        for i in range(1, num_orders + 1):
            customer = random.choice(customers)
            # 每个订单1-3个商品
            num_items = random.randint(1, 3)
            order_items = []
            
            for _ in range(num_items):
                product = random.choice(products)
                # 商品价格基于商品类型，添加一些随机波动
                base_price = {
                    "手机": 5000,
                    "笔记本电脑": 8000,
                    "耳机": 800,
                    "平板电脑": 3000,
                    "智能手表": 1500,
                    "相机": 6000,
                    "游戏机": 2500,
                    "显示器": 1200,
                    "键盘": 300,
                    "鼠标": 150
                }[product]
                
                price = round(base_price * (0.9 + random.random() * 0.2), 2)  # 价格在90%-110%之间波动
                quantity = random.randint(1, 3)
                
                order_items.append({
                    "product": product,
                    "price": price,
                    "quantity": quantity
                })
            
            # 随机订单日期（过去30天内）
            days_ago = random.randint(0, 30)
            order_date = f"2023-11-{30-days_ago:02d}"
            
            # 订单总金额
            total_amount = sum(item["price"] * item["quantity"] for item in order_items)
            
            orders.append({
                "order_id": f"ORD-{i:04d}",
                "customer_id": customer,
                "order_date": order_date,
                "items": order_items,
                "total_amount": round(total_amount, 2)
            })
        
        return orders
    
    # 生成订单数据
    orders = generate_order_data(1000)
    print(f"生成了{len(orders)}条订单数据")
    print("示例订单:")
    pprint(orders[0])
    print()
    
    # 1. 数据提取和转换
    print("1. 数据提取和转换:")
    
    # 提取所有订单商品记录
    def extract_order_items(orders):
        """从订单数据中提取所有商品记录"""
        for order in orders:
            for item in order["items"]:
                yield {
                    "order_id": order["order_id"],
                    "customer_id": order["customer_id"],
                    "order_date": order["order_date"],
                    "product": item["product"],
                    "price": item["price"],
                    "quantity": item["quantity"],
                    "item_total": round(item["price"] * item["quantity"], 2)
                }
    
    order_items = list(extract_order_items(orders))
    print(f"提取了{len(order_items)}条商品记录")
    print("示例商品记录:")
    pprint(order_items[0])
    print()
    
    # 2. 按产品分组并计算统计信息
    print("2. 按产品分组并计算统计信息:")
    
    # 使用itertools.groupby分组
    # 首先按产品排序
    sorted_items = sorted(order_items, key=operator.itemgetter("product"))
    
    # 使用functools.reduce计算每个产品的统计信息
    def calculate_product_stats(items):
        """计算产品统计信息"""
        if not items:
            return None
        
        # 使用reduce计算总销售额和总数量
        def stats_accumulator(acc, item):
            acc["total_revenue"] += item["item_total"]
            acc["total_quantity"] += item["quantity"]
            acc["order_count"] += 1
            acc["prices"].append(item["price"])
            return acc
        
        initial_acc = {
            "product": items[0]["product"],
            "total_revenue": 0.0,
            "total_quantity": 0,
            "order_count": 0,
            "prices": []
        }
        
        stats = functools.reduce(stats_accumulator, items, initial_acc)
        
        # 计算平均价格
        stats["avg_price"] = round(sum(stats["prices"]) / len(stats["prices"]), 2)
        del stats["prices"]  # 删除中间数据
        
        return stats
    
    # 按产品分组并计算统计信息
    product_stats = []
    for product, items_iter in itertools.groupby(sorted_items, key=operator.itemgetter("product")):
        items = list(items_iter)
        stats = calculate_product_stats(items)
        if stats:
            product_stats.append(stats)
    
    # 按销售额排序
    product_stats.sort(key=operator.itemgetter("total_revenue"), reverse=True)
    
    print("产品销售统计（按销售额排序）:")
    for i, stats in enumerate(product_stats[:5], 1):
        print(f"{i}. {stats['product']}:")
        print(f"   总销售额: ¥{stats['total_revenue']:.2f}")
        print(f"   总销量: {stats['total_quantity']}件")
        print(f"   订单数: {stats['order_count']}单")
        print(f"   平均价格: ¥{stats['avg_price']:.2f}")
    print()
    
    # 3. 客户购买行为分析
    print("3. 客户购买行为分析:")
    
    # 按客户ID分组
    sorted_by_customer = sorted(order_items, key=operator.itemgetter("customer_id"))
    
    # 计算每个客户的统计信息
    customer_stats = []
    for customer, items_iter in itertools.groupby(sorted_by_customer, key=operator.itemgetter("customer_id")):
        items = list(items_iter)
        
        # 使用Counter统计客户购买的产品种类
        product_counter = collections.Counter(item["product"] for item in items)
        
        # 计算总消费
        total_spent = sum(item["item_total"] for item in items)
        
        # 计算购买次数（按订单ID去重）
        order_ids = {item["order_id"] for item in items}
        purchase_count = len(order_ids)
        
        customer_stats.append({
            "customer_id": customer,
            "total_spent": round(total_spent, 2),
            "purchase_count": purchase_count,
            "avg_order_value": round(total_spent / purchase_count, 2),
            "unique_products": len(product_counter),
            "favorite_product": product_counter.most_common(1)[0][0] if product_counter else "N/A"
        })
    
    # 找出消费最高的客户
    top_customers = heapq.nlargest(5, customer_stats, key=operator.itemgetter("total_spent"))
    
    print("最高消费客户（前5名）:")
    for i, customer in enumerate(top_customers, 1):
        print(f"{i}. {customer['customer_id']}:")
        print(f"   总消费: ¥{customer['total_spent']:.2f}")
        print(f"   购买次数: {customer['purchase_count']}次")
        print(f"   平均订单价值: ¥{customer['avg_order_value']:.2f}")
        print(f"   购买产品种类: {customer['unique_products']}种")
        print(f"   最爱产品: {customer['favorite_product']}")
    print()
    
    # 4. 时间序列分析
    print("4. 时间序列分析:")
    
    # 按日期分组
    sorted_by_date = sorted(order_items, key=operator.itemgetter("order_date"))
    
    # 计算每日销售额
    daily_sales = []
    for date, items_iter in itertools.groupby(sorted_by_date, key=operator.itemgetter("order_date")):
        items = list(items_iter)
        daily_revenue = sum(item["item_total"] for item in items)
        daily_orders = {item["order_id"] for item in items}
        
        daily_sales.append({
            "date": date,
            "revenue": round(daily_revenue, 2),
            "order_count": len(daily_orders),
            "item_count": len(items)
        })
    
    # 计算移动平均（7天）
    daily_sales.sort(key=operator.itemgetter("date"))
    revenues = [day["revenue"] for day in daily_sales]
    
    # 使用itertools的滑动窗口计算移动平均
    if len(revenues) >= 7:
        # 使用functools.reduce计算窗口内的和
        window_sums = []
        for window in itertools.windowed(revenues, 7):
            window_sum = functools.reduce(operator.add, window)
            window_sums.append(round(window_sum / 7, 2))
        
        # 添加移动平均到结果中
        for i in range(6, len(daily_sales)):
            daily_sales[i]["7_day_avg"] = window_sums[i-6]
    
    print("最近7天销售数据:")
    for day in daily_sales[-7:]:
        ma_info = f", 7天平均: ¥{day.get('7_day_avg', 'N/A'):.2f}" if '7_day_avg' in day else ""
        print(f"  {day['date']}: ¥{day['revenue']:.2f}, 订单数: {day['order_count']}, 商品数: {day['item_count']}{ma_info}")
    print()
    
    # 5. 商品关联性分析（简单版）
    print("5. 商品关联性分析:")
    
    # 收集同一订单中的商品对
    product_pairs = []
    for order in orders:
        products = [item["product"] for item in order["items"]]
        # 只考虑包含多个商品的订单
        if len(products) > 1:
            # 使用itertools.combinations生成所有商品对
            pairs = itertools.combinations(sorted(products), 2)
            product_pairs.extend(pairs)
    
    # 计算商品对的出现频率
    pair_counter = collections.Counter(product_pairs)
    total_orders_with_pairs = sum(1 for order in orders if len(order["items"]) > 1)
    
    # 计算置信度并排序
    pair_confidence = []
    for (product_a, product_b), count in pair_counter.items():
        # 计算product_a出现的总次数
        a_count = sum(1 for item in order_items if item["product"] == product_a)
        
        # 计算置信度：P(B|A) = 同时购买A和B的订单数 / 购买A的订单数
        confidence = count / a_count if a_count > 0 else 0
        
        pair_confidence.append({
            "pair": (product_a, product_b),
            "count": count,
            "confidence": confidence,
            "support": count / total_orders_with_pairs
        })
    
    # 按置信度排序
    pair_confidence.sort(key=operator.itemgetter("confidence"), reverse=True)
    
    print("商品关联规则（按置信度排序，前5条）:")
    for i, rule in enumerate(pair_confidence[:5], 1):
        a, b = rule["pair"]
        print(f"{i}. 购买{a}的客户同时购买{b}:")
        print(f"   置信度: {rule['confidence']:.2%} (同时购买次数: {rule['count']})")
        print(f"   支持度: {rule['support']:.2%}")
    
    print("\n数据处理管道完成！")
    print()


def example_task_scheduling_system():
    """示例2: 优先级任务调度系统"""
    print("=== 示例2: 优先级任务调度系统 ===")
    
    # 1. 定义任务类
    print("1. 定义任务类和调度器...")
    
    # 使用namedtuple定义任务
    Task = collections.namedtuple('Task', ['priority', 'timestamp', 'task_id', 'description', 'func', 'args', 'kwargs'])
    
    # 任务状态枚举
    class TaskStatus:
        PENDING = "pending"
        RUNNING = "running"
        COMPLETED = "completed"
        FAILED = "failed"
    
    class TaskScheduler:
        def __init__(self):
            # 使用heapq实现优先队列
            self.task_queue = []
            # 使用defaultdict跟踪任务状态
            self.task_status = collections.defaultdict(lambda: TaskStatus.PENDING)
            # 使用Counter生成唯一任务ID
            self.task_counter = itertools.count(1)
            # 使用deque实现任务历史记录
            self.history = collections.deque(maxlen=100)
            # 使用LruCache缓存任务结果
            self.results = functools.lru_cache(maxsize=100)(self._get_result)
        
        def _get_result(self, task_id):
            """获取任务结果的内部方法（用于缓存）"""
            for record in self.history:
                if record['task_id'] == task_id:
                    return record.get('result')
            return None
        
        def add_task(self, priority, description, func, *args, **kwargs):
            """添加任务到调度队列"""
            # 优先级数字越小，优先级越高
            task_id = next(self.task_counter)
            timestamp = time.time()
            
            # 创建任务对象（优先级取负数是因为heapq是最小堆）
            task = Task(-priority, timestamp, task_id, description, func, args, kwargs)
            
            # 添加到优先队列
            heapq.heappush(self.task_queue, task)
            
            # 记录状态
            self.task_status[task_id] = TaskStatus.PENDING
            
            print(f"添加任务: #{task_id} '{description}' (优先级: {priority})")
            return task_id
        
        def schedule_task(self, priority, delay_seconds, description, func, *args, **kwargs):
            """安排延迟执行的任务"""
            def delayed_func():
                print(f"执行延迟任务: '{description}'")
                return func(*args, **kwargs)
            
            # 创建一个包装函数来模拟延迟
            def wrapper():
                time.sleep(delay_seconds)
                return delayed_func()
            
            return self.add_task(priority, f"DELAYED({delay_seconds}s): {description}", wrapper)
        
        def run_next(self):
            """执行下一个优先级最高的任务"""
            if not self.task_queue:
                print("任务队列为空")
                return None
            
            # 获取优先级最高的任务
            task = heapq.heappop(self.task_queue)
            priority, timestamp, task_id, description, func, args, kwargs = task
            
            print(f"开始执行任务: #{task_id} '{description}'")
            self.task_status[task_id] = TaskStatus.RUNNING
            
            start_time = time.time()
            result = None
            error = None
            
            try:
                # 执行任务
                result = func(*args, **kwargs)
                status = TaskStatus.COMPLETED
                print(f"任务 #{task_id} 完成")
            except Exception as e:
                error = str(e)
                status = TaskStatus.FAILED
                print(f"任务 #{task_id} 失败: {error}")
            
            end_time = time.time()
            execution_time = end_time - start_time
            
            # 记录到历史
            self.history.append({
                'task_id': task_id,
                'description': description,
                'priority': -priority,  # 恢复原始优先级
                'timestamp': timestamp,
                'start_time': start_time,
                'end_time': end_time,
                'execution_time': execution_time,
                'status': status,
                'result': result,
                'error': error
            })
            
            # 更新状态
            self.task_status[task_id] = status
            
            # 清除缓存，以便下次能获取最新结果
            self.results.cache_clear()
            
            return {
                'task_id': task_id,
                'status': status,
                'execution_time': execution_time,
                'result': result,
                'error': error
            }
        
        def run_all(self, max_tasks=None):
            """执行所有任务，或最多执行max_tasks个任务"""
            tasks_run = 0
            
            while self.task_queue and (max_tasks is None or tasks_run < max_tasks):
                self.run_next()
                tasks_run += 1
            
            print(f"总共执行了 {tasks_run} 个任务")
            return tasks_run
        
        def get_task_status(self, task_id):
            """获取任务状态"""
            return self.task_status.get(task_id, "未知任务")
        
        def get_task_result(self, task_id):
            """获取任务结果"""
            return self.results(task_id)
        
        def get_statistics(self):
            """获取调度器统计信息"""
            # 使用Counter统计各种状态的任务数
            status_counter = collections.Counter(self.task_status.values())
            
            # 计算历史任务的平均执行时间
            completed_tasks = [t for t in self.history if t['status'] == TaskStatus.COMPLETED]
            avg_execution_time = sum(t['execution_time'] for t in completed_tasks) / len(completed_tasks) if completed_tasks else 0
            
            # 按优先级统计任务
            priority_counter = collections.Counter()
            for record in self.history:
                priority_counter[record['priority']] += 1
            
            return {
                'queue_length': len(self.task_queue),
                'status_counts': dict(status_counter),
                'total_tasks': len(self.task_status),
                'completed_tasks': len(completed_tasks),
                'avg_execution_time': avg_execution_time,
                'priority_distribution': dict(priority_counter)
            }
    
    # 2. 创建示例任务函数
    print("\n2. 创建示例任务函数...")
    
    def task_quick(task_name):
        """快速任务"""
        print(f"执行快速任务: {task_name}")
        time.sleep(0.1)  # 模拟短暂工作
        return f"快速任务 '{task_name}' 完成"
    
    def task_medium(task_name, iterations=1000000):
        """中等耗时任务"""
        print(f"执行中等任务: {task_name} (迭代{iterations}次)")
        # 模拟一些计算工作
        result = 0
        for i in range(iterations):
            result += i * i
        time.sleep(0.3)  # 额外延迟
        return f"中等任务 '{task_name}' 完成，结果={result}"
    
    def task_heavy(task_name, sleep_time=1.0):
        """耗时任务"""
        print(f"执行耗时任务: {task_name} (睡眠{sleep_time}秒)")
        time.sleep(sleep_time)
        return f"耗时任务 '{task_name}' 完成"
    
    def task_with_error(task_name):
        """会失败的任务"""
        print(f"执行可能失败的任务: {task_name}")
        raise ValueError(f"任务 '{task_name}' 故意失败")
    
    # 3. 演示调度器使用
    print("\n3. 演示任务调度器...")
    
    # 创建调度器
    scheduler = TaskScheduler()
    
    # 添加不同优先级的任务
    print("\n添加任务:")
    scheduler.add_task(1, "系统备份", task_heavy, "系统备份")
    scheduler.add_task(5, "日志清理", task_medium, "日志清理")
    scheduler.add_task(3, "数据同步", task_medium, "数据同步", iterations=500000)
    scheduler.add_task(10, "生成报告", task_quick, "每日报告")
    scheduler.add_task(1, "数据库索引优化", task_heavy, "数据库优化", sleep_time=1.5)
    scheduler.add_task(2, "错误任务演示", task_with_error, "错误演示")
    scheduler.schedule_task(4, 0.5, "延迟任务", task_quick, "延迟报告")
    
    # 运行一个任务
    print("\n运行单个任务:")
    result = scheduler.run_next()
    print(f"结果: {result}")
    
    # 运行所有任务
    print("\n运行所有剩余任务:")
    scheduler.run_all()
    
    # 获取统计信息
    print("\n调度器统计信息:")
    stats = scheduler.get_statistics()
    pprint(stats)
    
    # 4. 高级功能演示 - 周期性任务
    print("\n4. 高级功能 - 周期性任务模拟:")
    
    # 创建新的调度器实例演示周期性任务
    periodic_scheduler = TaskScheduler()
    
    # 使用itertools.count模拟周期性任务
    def create_periodic_task(name, interval, max_runs=3):
        """创建周期性任务"""
        run_counter = itertools.count(1)
        
        def periodic_func():
            run_num = next(run_counter)
            print(f"执行周期性任务: {name} (第{run_num}次运行)")
            
            # 如果还没达到最大运行次数，安排下一次运行
            if run_num < max_runs:
                print(f"安排{name}在{interval}秒后再次运行")
                time.sleep(0.1)  # 小延迟确保任务正确添加
                periodic_scheduler.add_task(3, f"{name} (周期{interval}s)", periodic_func)
            
            return f"{name} 第{run_num}次运行完成"
        
        return periodic_func
    
    # 创建并添加周期性任务
    periodic_task1 = create_periodic_task("CPU监控", 0.5, max_runs=3)
    periodic_task2 = create_periodic_task("内存检查", 0.3, max_runs=3)
    
    periodic_scheduler.add_task(3, "CPU监控 (首次)", periodic_task1)
    periodic_scheduler.add_task(3, "内存检查 (首次)", periodic_task2)
    
    # 运行周期性任务
    print("\n运行周期性任务:")
    time.sleep(0.5)  # 等待延迟任务被添加
    periodic_scheduler.run_all()
    
    print("\n任务调度系统演示完成！")
    print()


def example_search_engine_ranking():
    """示例3: 搜索引擎排名系统模拟"""
    print("=== 示例3: 搜索引擎排名系统模拟 ===")
    
    # 1. 定义文档和查询
    print("1. 创建模拟文档集合...")
    
    # 模拟网页文档
    documents = [
        {
            "id": 1,
            "title": "Python编程入门教程",
            "content": "Python是一种广泛使用的解释型、高级和通用的编程语言。Python的设计哲学强调代码的可读性和简洁的语法。Python支持多种编程范式，包括面向对象、命令式、函数式和过程式编程。Python解释器可在许多操作系统上使用，官方CPython实现是开源软件。",
            "url": "https://example.com/python-basics",
            "authority": 9.2,  # 域名权重
            "backlinks": 125  # 反向链接数
        },
        {
            "id": 2,
            "title": "Python高级特性详解",
            "content": "Python提供了许多高级特性，如装饰器、生成器、迭代器、上下文管理器等。这些特性使得Python代码更加简洁、优雅和高效。本教程将深入讲解这些高级特性的使用方法和最佳实践。",
            "url": "https://example.com/python-advanced",
            "authority": 8.7,
            "backlinks": 98
        },
        {
            "id": 3,
            "title": "Python数据分析入门",
            "content": "Python在数据分析领域有着广泛的应用。主要的数据分析库包括NumPy、Pandas、Matplotlib等。这些库提供了强大的数据处理和可视化功能，使得数据分析工作变得更加简单和高效。",
            "url": "https://example.com/python-data-analysis",
            "authority": 8.9,
            "backlinks": 112
        },
        {
            "id": 4,
            "title": "Python网络爬虫开发",
            "content": "使用Python可以轻松开发网络爬虫，从网页中提取有用的信息。常用的爬虫库包括Requests、BeautifulSoup、Scrapy等。本教程将介绍如何使用这些库开发高效的网络爬虫。",
            "url": "https://example.com/python-web-scraping",
            "authority": 8.5,
            "backlinks": 87
        },
        {
            "id": 5,
            "title": "Python机器学习实践",
            "content": "Python是机器学习领域最流行的编程语言之一。主要的机器学习库包括Scikit-learn、TensorFlow、PyTorch等。这些库提供了丰富的算法和工具，使得机器学习模型的开发和部署变得更加简单。",
            "url": "https://example.com/python-machine-learning",
            "authority": 9.5,
            "backlinks": 187
        },
        {
            "id": 6,
            "title": "Python自动化测试",
            "content": "Python可以用于自动化测试，包括单元测试、集成测试和端到端测试。主要的测试框架包括unittest、pytest、Selenium等。这些工具使得测试工作变得更加自动化和高效。",
            "url": "https://example.com/python-automation-testing",
            "authority": 8.2,
            "backlinks": 76
        },
        {
            "id": 7,
            "title": "Python Web开发框架对比",
            "content": "Python有许多流行的Web开发框架，如Django、Flask、FastAPI等。本教程将对比这些框架的特点、优缺点和适用场景，帮助你选择最适合的框架进行Web开发。",
            "url": "https://example.com/python-web-frameworks",
            "authority": 8.8,
            "backlinks": 103
        },
        {
            "id": 8,
            "title": "Python性能优化技巧",
            "content": "虽然Python以开发效率著称，但在某些场景下性能可能成为瓶颈。本教程将介绍各种Python性能优化技巧，包括算法优化、数据结构选择、使用编译扩展等方法，帮助你编写高效的Python代码。",
            "url": "https://example.com/python-performance-optimization",
            "authority": 9.0,
            "backlinks": 118
        }
    ]
    
    print(f"创建了{len(documents)}篇模拟文档")
    print("示例文档:")
    pprint(documents[0])
    print()
    
    # 2. 实现文档预处理
    print("2. 文档预处理...")
    
    def preprocess_text(text):
        """文本预处理：分词、转小写、去除停用词"""
        # 简单分词（实际应用中应该使用更复杂的分词算法）
        import re
        words = re.findall(r'\b\w+\b', text.lower())
        
        # 简单停用词列表
        stopwords = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'about', 'as', 'is', 'are', 'was', 'were',
            'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
            'did', 'doing', 'will', 'would', 'could', 'should', 'may', 'might',
            'must', 'shall', 'this', 'that', 'these', 'those', 'it', 'its', 'it\'s',
            'you', 'your', 'yours', 'i', 'me', 'my', 'mine', 'we', 'our', 'ours',
            'they', 'them', 'their', 'theirs', 'he', 'him', 'his', 'she', 'her',
            'hers', 'which', 'who', 'whom', 'whose', 'what', 'where', 'when', 'why',
            'how'
        }
        
        # 过滤停用词
        return [word for word in words if word not in stopwords and len(word) > 1]
    
    # 预处理所有文档
    processed_docs = []
    for doc in documents:
        processed_doc = doc.copy()
        processed_doc['tokens'] = preprocess_text(doc['title'] + ' ' + doc['content'])
        processed_docs.append(processed_doc)
    
    print("预处理后的文档示例（tokens字段）:")
    print(processed_docs[0]['tokens'][:10], "...")
    print()
    
    # 3. 构建倒排索引
    print("3. 构建倒排索引...")
    
    # 使用defaultdict构建倒排索引
    inverted_index = collections.defaultdict(list)
    
    # 为每个词建立文档ID映射
    for doc in processed_docs:
        # 使用Counter统计词频
        term_freq = collections.Counter(doc['tokens'])
        
        for term, freq in term_freq.items():
            inverted_index[term].append((doc['id'], freq, doc['tokens'].index(term) if term in doc['tokens'] else -1))
    
    print(f"倒排索引包含{len(inverted_index)}个词条")
    print("示例词条的倒排索引（'python'）:")
    for doc_id, freq, pos in inverted_index['python'][:5]:  # 只显示前5个
        print(f"  文档{doc_id}: 频率={freq}, 首次位置={pos}")
    print()
    
    # 4. 实现搜索和排名算法
    print("4. 实现搜索和排名算法...")
    
    class SearchEngine:
        def __init__(self, documents, inverted_index):
            self.documents = {doc['id']: doc for doc in documents}
            self.inverted_index = inverted_index
            self.total_docs = len(documents)
        
        def search(self, query, top_k=5):
            """搜索查询并返回排名结果"""
            # 预处理查询
            query_tokens = preprocess_text(query)
            
            if not query_tokens:
                return []
            
            print(f"搜索查询: '{query}'")
            print(f"查询词: {query_tokens}")
            
            # 计算文档相关性分数
            doc_scores = collections.defaultdict(float)
            doc_details = {}
            
            # 对每个查询词计算TF-IDF分数
            for term in query_tokens:
                if term not in self.inverted_index:
                    continue
                
                # 计算IDF
                doc_freq = len(self.inverted_index[term])
                idf = math.log(self.total_docs / (doc_freq + 1)) + 1  # 平滑处理
                
                # 对包含该词的每个文档计算分数
                for doc_id, term_freq, position in self.inverted_index[term]:
                    doc = self.documents[doc_id]
                    
                    # 计算TF
                    tf = term_freq / len(doc['tokens']) if doc['tokens'] else 0
                    
                    # 计算TF-IDF分数
                    tf_idf_score = tf * idf
                    
                    # 添加标题匹配的权重
                    title_boost = 2.0 if term in preprocess_text(doc['title']) else 1.0
                    
                    # 添加位置权重（越靠前的词权重越高）
                    position_weight = 1.0 / (position + 1) if position >= 0 else 0.5
                    
                    # 累计分数
                    doc_scores[doc_id] += tf_idf_score * title_boost * position_weight
                    
                    # 记录文档详情
                    if doc_id not in doc_details:
                        doc_details[doc_id] = doc
            
            # 应用PageRank风格的权重（基于权威性和反向链接）
            for doc_id in list(doc_scores.keys()):
                doc = doc_details[doc_id]
                
                # 计算权威性分数
                authority_score = (doc['authority'] / 10.0) * 0.3
                
                # 计算反向链接分数（归一化）
                max_backlinks = max(doc['backlinks'] for doc in self.documents.values())
                backlink_score = (doc['backlinks'] / max_backlinks) * 0.2 if max_backlinks > 0 else 0
                
                # 组合最终分数
                doc_scores[doc_id] = doc_scores[doc_id] * 0.5 + authority_score + backlink_score
            
            # 排序并返回结果
            sorted_results = sorted(doc_scores.items(), key=operator.itemgetter(1), reverse=True)
            
            # 格式化返回结果
            results = []
            for doc_id, score in sorted_results[:top_k]:
                doc = doc_details[doc_id]
                results.append({
                    'doc_id': doc_id,
                    'title': doc['title'],
                    'url': doc['url'],
                    'snippet': self._generate_snippet(doc, query_tokens),
                    'score': round(score, 4)
                })
            
            return results
        
        def _generate_snippet(self, doc, query_tokens, max_length=150):
            """为文档生成包含查询词的摘要"""
            # 简单实现：找到第一个查询词并提取前后文
            content = doc['content']
            
            # 查找任何查询词的第一次出现
            snippet_start = 0
            for token in query_tokens:
                # 在原始内容中查找（不区分大小写）
                token_lower = token.lower()
                pos = content.lower().find(token_lower)
                if pos >= 0:
                    # 尝试找到一个合适的句子开始位置
                    snippet_start = max(0, pos - 50)
                    break
            
            # 提取摘要
            snippet = content[snippet_start:snippet_start + max_length]
            
            # 如果不是从开头开始，添加省略号
            if snippet_start > 0:
                snippet = "..." + snippet
            
            # 如果不是到结尾，添加省略号
            if snippet_start + max_length < len(content):
                snippet = snippet + "..."
            
            # 高亮查询词
            for token in query_tokens:
                # 简单的大小写不敏感替换
                import re
                snippet = re.sub(f'({re.escape(token)})', r'<b>\1</b>', snippet, flags=re.IGNORECASE)
            
            return snippet
        
        def advanced_search(self, query, filters=None, sort_by=None):
            """高级搜索功能"""
            # 获取基本搜索结果
            results = self.search(query, top_k=len(self.documents))
            
            # 应用过滤条件
            if filters:
                if 'min_authority' in filters:
                    min_auth = filters['min_authority']
                    results = [r for r in results if self.documents[r['doc_id']]['authority'] >= min_auth]
                
                if 'min_backlinks' in filters:
                    min_back = filters['min_backlinks']
                    results = [r for r in results if self.documents[r['doc_id']]['backlinks'] >= min_back]
            
            # 应用排序
            if sort_by:
                if sort_by == 'authority':
                    results.sort(key=lambda x: self.documents[x['doc_id']]['authority'], reverse=True)
                elif sort_by == 'backlinks':
                    results.sort(key=lambda x: self.documents[x['doc_id']]['backlinks'], reverse=True)
                elif sort_by == 'relevance':
                    # 默认相关性排序已经完成
                    pass
            
            return results[:5]  # 返回前5个结果
        """会失败的任务"""
        print(f"执行可能失败的任务: {task_name}")
        raise ValueError(f"任务 '{task_name}' 故意失败")
    
    # 3. 演示调度器使用
    print("\n3. 演示任务调度器...")
    
    # 创建调度器
    scheduler = TaskScheduler()
    
    # 添加不同优先级的任务
    print("\n添加任务:")
    scheduler.add_task(1, "系统备份", task_heavy, "系统备份")
    scheduler.add_task(5, "日志清理", task_medium, "日志清理")
    scheduler.add_task(3, "数据同步", task_medium, "数据同步", iterations=500000)
    scheduler.add_task(10, "生成报告", task_quick, "每日报告")
    scheduler.add_task(1, "数据库索引优化", task_heavy, "数据库优化", sleep_time=1.5)
    scheduler.add_task(2, "错误任务演示", task_with_error, "错误演示")
    scheduler.schedule_task(4, 0.5, "延迟任务", task_quick, "延迟报告")
    
    # 运行一个任务
    print("\n运行单个任务:")
    result = scheduler.run_next()
    print(f"结果: {result}")
    
    # 运行所有任务
    print("\n运行所有剩余任务:")
    scheduler.run_all()
    
    # 获取统计信息
    print("\n调度器统计信息:")
    stats = scheduler.get_statistics()
    pprint(stats)
    
    # 4. 高级功能演示 - 周期性任务
    print("\n4. 高级功能 - 周期性任务模拟:")
    
    # 创建新的调度器实例演示周期性任务
    periodic_scheduler = TaskScheduler()
    
    # 使用itertools.count模拟周期性任务
    def create_periodic_task(name, interval, max_runs=3):
        """创建周期性任务"""
        run_counter = itertools.count(1)
        
        def periodic_func():
            run_num = next(run_counter)
            print(f"执行周期性任务: {name} (第{run_num}次运行)")
            
            # 如果还没达到最大运行次数，安排下一次运行
            if run_num < max_runs:
                print(f"安排{name}在{interval}秒后再次运行")
                time.sleep(0.1)  # 小延迟确保任务正确添加
                periodic_scheduler.add_task(3, f"{name} (周期{interval}s)", periodic_func)
            
            return f"{name} 第{run_num}次运行完成"
        
        return periodic_func
    
    # 创建并添加周期性任务
    periodic_task1 = create_periodic_task("CPU监控", 0.5, max_runs=3)
    periodic_task2 = create_periodic_task("内存检查", 0.3, max_runs=3)
    
    periodic_scheduler.add_task(3, "CPU监控 (首次)", periodic_task1)
    periodic_scheduler.add_task(3, "内存检查 (首次)", periodic_task2)
    
    # 运行周期性任务
    print("\n运行周期性任务:")
    time.sleep(0.5)  # 等待延迟任务被添加
    periodic_scheduler.run_all()
    
    print("\n任务调度系统演示完成！")
    print()


def example_search_engine_ranking():
    """示例3: 搜索引擎排名系统模拟"""
    print("=== 示例3: 搜索引擎排名系统模拟 ===")
    
    # 1. 定义文档和查询
    print("1. 创建模拟文档集合...")
    
    # 模拟网页文档
    documents = [
        {
            "id": 1,
            "title": "Python编程入门教程",
            "content": "Python是一种广泛使用的解释型、高级和通用的编程语言。Python的设计哲学强调代码的可读性和简洁的语法。Python支持多种编程范式，包括面向对象、命令式、函数式和过程式编程。Python解释器可在许多操作系统上使用，官方CPython实现是开源软件。",
            "url": "https://example.com/python-basics",
            "authority": 9.2,  # 域名权重
            "backlinks": 125  # 反向链接数
        },
        {
            "id": 2,
            "title": "Python高级特性详解",
            "content": "Python提供了许多高级特性，如装饰器、生成器、迭代器、上下文管理器等。这些特性使得Python代码更加简洁、优雅和高效。本教程将深入讲解这些高级特性的使用方法和最佳实践。",
            "url": "https://example.com/python-advanced",
            "authority": 8.7,
            "backlinks": 98
        },
        {
            "id": 3,
            "title": "Python数据分析入门",
            "content": "Python在数据分析领域有着广泛的应用。主要的数据分析库包括NumPy、Pandas、Matplotlib等。这些库提供了强大的数据处理和可视化功能，使得数据分析工作变得更加简单和高效。",
            "url": "https://example.com/python-data-analysis",
            "authority": 8.9,
            "backlinks": 112
        },
        {
            "id": 4,
            "title": "Python网络爬虫开发",
            "content": "使用Python可以轻松开发网络爬虫，从网页中提取有用的信息。常用的爬虫库包括Requests、BeautifulSoup、Scrapy等。本教程将介绍如何使用这些库开发高效的网络爬虫。",
            "url": "https://example.com/python-web-scraping",
            "authority": 8.5,
            "backlinks": 87
        },
        {
            "id": 5,
            "title": "Python机器学习实践",
            "content": "Python是机器学习领域最流行的编程语言之一。主要的机器学习库包括Scikit-learn、TensorFlow、PyTorch等。这些库提供了丰富的算法和工具，使得机器学习模型的开发和部署变得更加简单。",
            "url": "https://example.com/python-machine-learning",
            "authority": 9.5,
            "backlinks": 187
        },
        {
            "id": 6,
            "title": "Python自动化测试",
            "content": "Python可以用于自动化测试，包括单元测试、集成测试和端到端测试。主要的测试框架包括unittest、pytest、Selenium等。这些工具使得测试工作变得更加自动化和高效。",
            "url": "https://example.com/python-automation-testing",
            "authority": 8.2,
            "backlinks": 76
        },
        {
            "id": 7,
            "title": "Python Web开发框架对比",
            "content": "Python有许多流行的Web开发框架，如Django、Flask、FastAPI等。本教程将对比这些框架的特点、优缺点和适用场景，帮助你选择最适合的框架进行Web开发。",
            "url": "https://example.com/python-web-frameworks",
            "authority": 8.8,
            "backlinks": 103
        },
        {
            "id": 8,
            "title": "Python性能优化技巧",
            "content": "虽然Python以开发效率著称，但在某些场景下性能可能成为瓶颈。本教程将介绍各种Python性能优化技巧，包括算法优化、数据结构选择、使用编译扩展等方法，帮助你编写高效的Python代码。",
            "url": "https://example.com/python-performance-optimization",
            "authority": 9.0,
            "backlinks": 118
        }
    ]
    
    print(f"创建了{len(documents)}篇模拟文档")
    print("示例文档:")
    pprint(documents[0])
    print()
    
    # 2. 实现文档预处理
    print("2. 文档预处理...")
    
    def preprocess_text(text):
        """文本预处理：分词、转小写、去除停用词"""
        # 简单分词（实际应用中应该使用更复杂的分词算法）
        import re
        words = re.findall(r'\b\w+\b', text.lower())
        
        # 简单停用词列表
        stopwords = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'about', 'as', 'is', 'are', 'was', 'were',
            'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
            'did', 'doing', 'will', 'would', 'could', 'should', 'may', 'might',
            'must', 'shall', 'this', 'that', 'these', 'those', 'it', 'its', 'it\'s',
            'you', 'your', 'yours', 'i', 'me', 'my', 'mine', 'we', 'our', 'ours',
            'they', 'them', 'their', 'theirs', 'he', 'him', 'his', 'she', 'her',
            'hers', 'which', 'who', 'whom', 'whose', 'what', 'where', 'when', 'why',
            'how'
        }
        
        # 过滤停用词
        return [word for word in words if word not in stopwords and len(word) > 1]
    
    # 预处理所有文档
    processed_docs = []
    for doc in documents:
        processed_doc = doc.copy()
        processed_doc['tokens'] = preprocess_text(doc['title'] + ' ' + doc['content'])
        processed_docs.append(processed_doc)
    
    print("预处理后的文档示例（tokens字段）:")
    print(processed_docs[0]['tokens'][:10], "...")
    print()
    
    # 3. 构建倒排索引
    print("3. 构建倒排索引...")
    
    # 使用defaultdict构建倒排索引
    inverted_index = collections.defaultdict(list)
    
    # 为每个词建立文档ID映射
    for doc in processed_docs:
        # 使用Counter统计词频
        term_freq = collections.Counter(doc['tokens'])
        
        for term, freq in term_freq.items():
            inverted_index[term].append((doc['id'], freq, doc['tokens'].index(term) if term in doc['tokens'] else -1))
    
    print(f"倒排索引包含{len(inverted_index)}个词条")
    print("示例词条的倒排索引（'python'）:")
    for doc_id, freq, pos in inverted_index['python'][:5]:  # 只显示前5个
        print(f"  文档{doc_id}: 频率={freq}, 首次位置={pos}")
    print()
    
    # 4. 实现搜索和排名算法
    print("4. 实现搜索和排名算法...")
    
    class SearchEngine:
        def __init__(self, documents, inverted_index):
            self.documents = {doc['id']: doc for doc in documents}
            self.inverted_index = inverted_index
            self.total_docs = len(documents)
        
        def search(self, query, top_k=5):
            """搜索查询并返回排名结果"""
            # 预处理查询
            query_tokens = preprocess_text(query)
            
            if not query_tokens:
                return []
            
            print(f"搜索查询: '{query}'")
            print(f"查询词: {query_tokens}")
            
            # 计算文档相关性分数
            doc_scores = collections.defaultdict(float)
            doc_details = {}
            
            # 对每个查询词计算TF-IDF分数
            for term in query_tokens:
                if term not in self.inverted_index:
                    continue
                
                # 计算IDF
                doc_freq = len(self.inverted_index[term])
                idf = math.log(self.total_docs / (doc_freq + 1)) + 1  # 平滑处理
                
                # 对包含该词的每个文档计算分数
                for doc_id, term_freq, position in self.inverted_index[term]:
                    doc = self.documents[doc_id]
                    
                    # 计算TF
                    tf = term_freq / len(doc['tokens']) if doc['tokens'] else 0
                    
                    # 计算TF-IDF分数
                    tf_idf_score = tf * idf
                    
                    # 添加标题匹配的权重
                    title_boost = 2.0 if term in preprocess_text(doc['title']) else 1.0
                    
                    # 添加位置权重（越靠前的词权重越高）
                    position_weight = 1.0 / (position + 1) if position >= 0 else 0.5
                    
                    # 累计分数
                    doc_scores[doc_id] += tf_idf_score * title_boost * position_weight
                    
                    # 记录文档详情
                    if doc_id not in doc_details:
                        doc_details[doc_id] = doc
            
            # 应用PageRank风格的权重（基于权威性和反向链接）
            for doc_id in list(doc_scores.keys()):
                doc = doc_details[doc_id]
                
                # 计算权威性分数
                authority_score = (doc['authority'] / 10.0) * 0.3
                
                # 计算反向链接分数（归一化）
                max_backlinks = max(doc['backlinks'] for doc in self.documents.values())
                backlink_score = (doc['backlinks'] / max_backlinks) * 0.2 if max_backlinks > 0 else 0
                
                # 组合最终分数
                doc_scores[doc_id] = doc_scores[doc_id] * 0.5 + authority_score + backlink_score
            
            # 排序并返回结果
            sorted_results = sorted(doc_scores.items(), key=operator.itemgetter(1), reverse=True)
            
            # 格式化返回结果
            results = []
            for doc_id, score in sorted_results[:top_k]:
                doc = doc_details[doc_id]
                results.append({
                    'doc_id': doc_id,
                    'title': doc['title'],
                    'url': doc['url'],
                    'snippet': self._generate_snippet(doc, query_tokens),
                    'score': round(score, 4)
                })
            
            return results
        
        def _generate_snippet(self, doc, query_tokens, max_length=150):
            """为文档生成包含查询词的摘要"""
            # 简单实现：找到第一个查询词并提取前后文
            content = doc['content']
            
            # 查找任何查询词的第一次出现
            snippet_start = 0
            for token in query_tokens:
                # 在原始内容中查找（不区分大小写）
                token_lower = token.lower()
                pos = content.lower().find(token_lower)
                if pos >= 0:
                    # 尝试找到一个合适的句子开始位置
                    snippet_start = max(0, pos - 50)
                    break
            
            # 提取摘要
            snippet = content[snippet_start:snippet_start + max_length]
            
            # 如果不是从开头开始，添加省略号
            if snippet_start > 0:
                snippet = "..." + snippet
            
            # 如果不是到结尾，添加省略号
            if snippet_start + max_length < len(content):
                snippet = snippet + "..."
            
            # 高亮查询词
            for token in query_tokens:
                # 简单的大小写不敏感替换
                import re
                snippet = re.sub(f'({re.escape(token)})', r'<b>\1</b>', snippet, flags=re.IGNORECASE)
            
            return snippet
        
        def advanced_search(self, query, filters=None, sort_by=None):
            """高级搜索功能"""
            # 获取基本搜索结果
            results = self.search(query, top_k=len(self.documents))
            
            # 应用过滤条件
            if filters:
                if 'min_authority' in filters:
                    min_auth = filters['min_authority']
                    results = [r for r in results if self.documents[r['doc_id']]['authority'] >= min_auth]
                
                if 'min_backlinks' in filters:
                    min_back = filters['min_backlinks']
                    results = [r for r in results if self.documents[r['doc_id']]['backlinks'] >= min_back]
            
            # 应用排序
            if sort_by:
                if sort_by == 'authority':
                    results.sort(key=lambda x: self.documents[x['doc_id']]['authority'], reverse=True)
                elif sort_by == 'backlinks':
                    results.sort(key=lambda x: self.documents[x['doc_id']]['backlinks'], reverse=True)
                elif sort_by == 'relevance':
                    # 默认相关性排序已经完成
                    pass
            
            return results[:5]  # 返回前5个结果
    
    # 5. 执行搜索演示
    print("5. 执行搜索演示...")
    
    # 创建搜索引擎实例
    search_engine = SearchEngine(processed_docs, inverted_index)
    
    # 执行简单搜索
    print("\n5.1 简单搜索:")
    print("\n查询1: 'Python 机器学习'")
    results = search_engine.search("Python 机器学习")
    
    print(f"\n找到{len(results)}个结果:")
    for i, result in enumerate(results, 1):
        print(f"\n排名{i}: {result['title']}")
        print(f"  URL: {result['url']}")
        print(f"  分数: {result['score']}")
        print(f"  摘要: {result['snippet']}")
    
    # 执行另一个搜索
    print("\n\n查询2: 'Python Web开发'")
    results = search_engine.search("Python Web开发")
    
    print(f"\n找到{len(results)}个结果:")
    for i, result in enumerate(results, 1):
        print(f"\n排名{i}: {result['title']}")
        print(f"  URL: {result['url']}")
        print(f"  分数: {result['score']}")
    
    # 执行高级搜索
    print("\n\n5.2 高级搜索:")
    print("\n高级查询: 'Python 教程' (域名权重>=9.0, 按反向链接排序)")
    results = search_engine.advanced_search(
        "Python 教程", 
        filters={"min_authority": 9.0}, 
        sort_by="backlinks"
    )
    
    print(f"\n找到{len(results)}个结果:")
    for i, result in enumerate(results, 1):
        doc = processed_docs[result['doc_id'] - 1]  # 文档ID从1开始
        print(f"\n排名{i}: {result['title']}")
        print(f"  URL: {result['url']}")
        print(f"  分数: {result['score']}")
        print(f"  域名权重: {doc['authority']}")
        print(f"  反向链接: {doc['backlinks']}")
    
    print("\n搜索引擎排名系统演示完成！")
    print()


def example_machine_learning_pipeline():
    """示例4: 机器学习数据处理管道"""
    print("=== 示例4: 机器学习数据处理管道 ===")
    
    # 1. 生成模拟数据集
    print("1. 生成模拟数据集...")
    
    import random
    
    # 生成模拟客户数据
    def generate_customer_data(n_samples=1000):
        """生成模拟客户数据"""
        # 可能的特征值
        age_ranges = [(18, 25), (26, 35), (36, 45), (46, 55), (56, 70)]
        genders = ['男', '女']
        regions = ['华东', '华南', '华北', '华中', '西南', '西北', '东北']
        income_ranges = [(0, 5000), (5000, 10000), (10000, 20000), (20000, 50000), (50000, 100000)]
        marital_statuses = ['未婚', '已婚', '离婚', '丧偶']
        education_levels = ['高中及以下', '大专', '本科', '硕士', '博士']
        
        data = []
        for i in range(n_samples):
            age_range = random.choice(age_ranges)
            age = random.randint(age_range[0], age_range[1])
            
            gender = random.choice(genders)
            region = random.choice(regions)
            
            income_range = random.choice(income_ranges)
            income = random.randint(income_range[0], income_range[1])
            
            # 根据年龄、收入等生成更真实的消费数据
            # 年龄和消费金额的关系（中年消费力较强）
            age_factor = 1.0
            if 26 <= age <= 55:
                age_factor = 1.5
            elif age > 55:
                age_factor = 1.2
                
            # 收入和消费金额的关系
            income_factor = income / 10000.0
            
            # 消费频率（次/月）
            purchase_frequency = max(1, int(random.normalvariate(8, 4) * age_factor))
            
            # 平均消费金额
            avg_purchase_amount = max(100, int(random.normalvariate(1000, 500) * income_factor * random.uniform(0.8, 1.2)))
            
            # 总消费金额
            total_spend = purchase_frequency * avg_purchase_amount
            
            # 最近一次购买时间（天）
            days_since_last_purchase = min(30, max(1, int(random.exponential(7))))
            
            # 客户价值分数（基于RFM模型简单计算）
            recency_score = 10 - (days_since_last_purchase / 3)
            frequency_score = min(10, purchase_frequency)
            monetary_score = min(10, total_spend / 1000)
            customer_value = (recency_score + frequency_score + monetary_score) / 3
            
            # 流失概率（基于最近购买时间和购买频率）
            churn_probability = min(1.0, days_since_last_purchase / 30 * 0.5 + (10 - frequency_score) / 10 * 0.5)
            
            # 标记为高价值客户（价值分数>7）
            is_high_value = customer_value > 7
            
            # 标记为流失风险客户（流失概率>0.7）
            is_churn_risk = churn_probability > 0.7
            
            data.append({
                'customer_id': f'C{i+1:06d}',
                'age': age,
                'gender': gender,
                'region': region,
                'income': income,
                'marital_status': random.choice(marital_statuses),
                'education_level': random.choice(education_levels),
                'purchase_frequency': purchase_frequency,
                'avg_purchase_amount': avg_purchase_amount,
                'total_spend': total_spend,
                'days_since_last_purchase': days_since_last_purchase,
                'customer_value': round(customer_value, 2),
                'churn_probability': round(churn_probability, 2),
                'is_high_value': is_high_value,
                'is_churn_risk': is_churn_risk
            })
        
        return data
    
    # 生成模拟数据
    customer_data = generate_customer_data(1000)
    
    print(f"生成了{len(customer_data)}条客户数据")
    print("示例数据:")
    pprint(customer_data[0])
    print()
    
    # 2. 实现数据处理管道
    print("2. 实现数据处理管道...")
    
    class DataPipeline:
        def __init__(self):
            self.steps = []
        
        def add_step(self, name, func, **kwargs):
            """添加处理步骤"""
            self.steps.append((name, func, kwargs))
            return self
        
        def process(self, data):
            """执行整个处理管道"""
            result = data
            
            for name, func, kwargs in self.steps:
                print(f"执行步骤: {name}")
                result = func(result, **kwargs)
            
            return result
    
    # 3. 定义处理函数
    
    # 数据清洗函数
    def clean_data(data, drop_duplicates=True):
        """清洗数据"""
        # 简单实现：去重（基于customer_id）
        if drop_duplicates:
            seen_ids = set()
            cleaned = []
            
            for record in data:
                if record['customer_id'] not in seen_ids:
                    seen_ids.add(record['customer_id'])
                    cleaned.append(record)
            
            print(f"数据清洗: 删除了{len(data) - len(cleaned)}条重复记录")
            return cleaned
        
        return data
    
    # 特征工程函数
    def feature_engineering(data):
        """特征工程"""
        # 对每条记录添加新特征
        for record in data:
            # 年龄分组
            age = record['age']
            if age < 26:
                record['age_group'] = '青年'
            elif age < 46:
                record['age_group'] = '中年'
            else:
                record['age_group'] = '老年'
            
            # 收入分组
            income = record['income']
            if income < 10000:
                record['income_group'] = '低收入'
            elif income < 30000:
                record['income_group'] = '中等收入'
            else:
                record['income_group'] = '高收入'
            
            # 消费能力评分（0-100）
            record['spending_power'] = min(100, int(record['total_spend'] / 500))
            
            # RFM特征
            record['recency_segment'] = '高' if record['days_since_last_purchase'] < 7 else '中' if record['days_since_last_purchase'] < 15 else '低'
            record['frequency_segment'] = '高' if record['purchase_frequency'] > 10 else '中' if record['purchase_frequency'] > 5 else '低'
            record['monetary_segment'] = '高' if record['total_spend'] > 10000 else '中' if record['total_spend'] > 5000 else '低'
            
            # RFM组合标签
            record['rfm_segment'] = f"{record['recency_segment']}{record['frequency_segment']}{record['monetary_segment']}"
        
        print("特征工程: 已添加年龄分组、收入分组、消费能力评分、RFM分段等特征")
        return data
    
    # 数据转换函数
    def transform_data(data):
        """数据转换"""
        # 将类别特征转换为数值特征（简单编码）
        # 性别编码
        gender_map = {'男': 0, '女': 1}
        # 区域编码（按字母顺序）
        region_map = {region: i for i, region in enumerate(sorted(set(r['region'] for r in data)))}        
        # 婚姻状况编码
        marital_map = {'未婚': 0, '已婚': 1, '离婚': 2, '丧偶': 3}
        # 教育水平编码
        education_map = {'高中及以下': 0, '大专': 1, '本科': 2, '硕士': 3, '博士': 4}
        # 年龄段编码
        age_group_map = {'青年': 0, '中年': 1, '老年': 2}
        # 收入组编码
        income_group_map = {'低收入': 0, '中等收入': 1, '高收入': 2}
        # RFM分段编码
        segment_map = {'低': 0, '中': 1, '高': 2}
        
        for record in data:
            record['gender_encoded'] = gender_map[record['gender']]
            record['region_encoded'] = region_map[record['region']]
            record['marital_encoded'] = marital_map[record['marital_status']]
            record['education_encoded'] = education_map[record['education_level']]
            record['age_group_encoded'] = age_group_map[record['age_group']]
            record['income_group_encoded'] = income_group_map[record['income_group']]
            record['recency_encoded'] = segment_map[record['recency_segment']]
            record['frequency_encoded'] = segment_map[record['frequency_segment']]
            record['monetary_encoded'] = segment_map[record['monetary_segment']]
        
        print("数据转换: 已将类别特征转换为数值编码")
        return data
    
    # 数据标准化函数
    def normalize_data(data, numerical_fields=None):
        """数据标准化"""
        if numerical_fields is None:
            numerical_fields = ['age', 'income', 'purchase_frequency', 'avg_purchase_amount', 'total_spend']
        
        # 计算每个字段的均值和标准差
        stats = {}
        for field in numerical_fields:
            values = [record[field] for record in data]
            mean_val = sum(values) / len(values)
            variance = sum((x - mean_val) ** 2 for x in values) / len(values)
            std_dev = math.sqrt(variance)
            
            stats[field] = (mean_val, std_dev)
            
            # 标准化每个值
            for record in data:
                if std_dev > 0:
                    record[f'{field}_normalized'] = (record[field] - mean_val) / std_dev
                else:
                    record[f'{field}_normalized'] = 0
        
        print(f"数据标准化: 已标准化{len(numerical_fields)}个数值字段")
        return data
    
    # 4. 数据聚合和分析函数
    
    def aggregate_by_segment(data, segment_field='rfm_segment'):
        """按段聚合数据"""
        # 使用defaultdict聚合数据
        segment_stats = collections.defaultdict(lambda: {
            'count': 0,
            'total_spend': 0,
            'avg_spend': 0,
            'total_customers': 0,
            'high_value_count': 0,
            'churn_risk_count': 0
        })
        
        # 聚合
        for record in data:
            segment = record[segment_field]
            stats = segment_stats[segment]
            
            stats['count'] += 1
            stats['total_spend'] += record['total_spend']
            stats['high_value_count'] += 1 if record['is_high_value'] else 0
            stats['churn_risk_count'] += 1 if record['is_churn_risk'] else 0
        
        # 计算平均值
        for segment, stats in segment_stats.items():
            stats['avg_spend'] = stats['total_spend'] / stats['count'] if stats['count'] > 0 else 0
            stats['high_value_ratio'] = stats['high_value_count'] / stats['count'] if stats['count'] > 0 else 0
            stats['churn_risk_ratio'] = stats['churn_risk_count'] / stats['count'] if stats['count'] > 0 else 0
        
        print(f"按{segment_field}聚合: 发现{len(segment_stats)}个不同的客户段")
        return segment_stats
    
    # 5. 创建和执行数据管道
    print("3. 创建并执行数据处理管道...")
    
    pipeline = DataPipeline()
    pipeline.add_step("数据清洗", clean_data)
    pipeline.add_step("特征工程", feature_engineering)
    pipeline.add_step("数据转换", transform_data)
    pipeline.add_step("数据标准化", normalize_data)
    
    # 执行管道
    processed_data = pipeline.process(customer_data)
    
    # 6. 分析结果
    print("\n4. 分析结果...")
    
    # 按RFM段聚合
    rfm_segments = aggregate_by_segment(processed_data, 'rfm_segment')
    
    print("\nRFM客户段分析:")
    for segment, stats in sorted(rfm_segments.items()):
        print(f"\n段 {segment}:")
        print(f"  客户数: {stats['count']}")
        print(f"  平均消费: {stats['avg_spend']:.2f}")
        print(f"  高价值客户比例: {stats['high_value_ratio']:.2%}")
        print(f"  流失风险比例: {stats['churn_risk_ratio']:.2%}")
    
    # 按年龄段分析
    age_segments = aggregate_by_segment(processed_data, 'age_group')
    
    print("\n按年龄段分析:")
    for segment, stats in age_segments.items():
        print(f"\n{segment}:")
        print(f"  客户数: {stats['count']}")
        print(f"  平均消费: {stats['avg_spend']:.2f}")
        print(f"  高价值客户比例: {stats['high_value_ratio']:.2%}")
    
    # 7. 客户分群
    print("\n5. 客户分群和营销策略建议...")
    
    def get_customer_segment_strategy(segment, stats):
        """根据客户段提供营销策略建议"""
        # RFM段的首字母表示最近购买（R）
        recency = segment[0]
        
        # 营销策略映射
        strategies = {
            '高高高': "重要价值客户 - 提供VIP服务、专属优惠、忠诚度计划",
            '高中高': "重要发展客户 - 增加互动、个性化推荐",
            '高低高': "重要保持客户 - 防止流失、主动联系",
            '高高低': "新客户 - 提升消费频次、交叉销售",
            '中高高': "重要挽留客户 - 重新激活、特别优惠",
            '中中高': "一般价值客户 - 常规营销、会员活动",
            '中低高': "潜在价值客户 - 提升体验、个性化服务",
            '中中中': "一般客户 - 常规营销、季节性促销",
            '中低中': "低活跃客户 - 限时优惠、新产品推广",
            '中低低': "流失风险客户 - 挽回计划、特别折扣",
            '低高高': "休眠高价值客户 - 唤醒活动、特别邀请",
            '低中高': "休眠一般客户 - 定期提醒、优惠促销",
            '低低高': "休眠低价值客户 - 低成本营销、自动化沟通",
            '低低中': "低价值客户 - 低成本营销、客户教育",
            '低低低': "流失客户 - 重新获取计划、市场调研"
        }
        
        return strategies.get(segment, "根据具体情况制定策略")
    
    print("客户段营销策略建议:")
    for segment, stats in sorted(rfm_segments.items()):
        if stats['count'] > 0:  # 只显示有客户的段
            strategy = get_customer_segment_strategy(segment, stats)
            print(f"\n{segment}段 ({stats['count']}客户): {strategy}")
    
    print("\n机器学习数据处理管道演示完成！")
    print()


def example_advanced_caching_system():
    """示例5: 高级缓存系统"""
    print("=== 示例5: 高级缓存系统 ===")
    
    # 1. 实现多级缓存系统
    print("1. 实现多级缓存系统...")
    
    class CacheEntry:
        """缓存条目"""
        def __init__(self, key, value, expiry=None):
            self.key = key
            self.value = value
            self.created_at = time.time()
            self.last_accessed = time.time()
            self.access_count = 1
            self.expiry = expiry  # 过期时间（Unix时间戳）
        
        def is_expired(self):
            """检查条目是否过期"""
            return self.expiry is not None and time.time() > self.expiry
        
        def access(self):
            """访问缓存条目，更新统计信息"""
            self.last_accessed = time.time()
            self.access_count += 1
            return self.value
        
        def __lt__(self, other):
            """用于优先级队列排序（按最后访问时间）"""
            return self.last_accessed < other.last_accessed
    
    class LRUCache:
        """LRU（最近最少使用）缓存实现"""
        def __init__(self, capacity=100):
            self.capacity = capacity
            self.cache = {}  # 键到缓存条目的映射
            self.order = collections.OrderedDict()  # 用于LRU顺序
        
        def get(self, key):
            """获取缓存项"""
            if key not in self.cache:
                return None
            
            entry = self.cache[key]
            
            # 检查过期
            if entry.is_expired():
                self.delete(key)
                return None
            
            # 更新访问信息
            entry.access()
            
            # 更新LRU顺序
            self.order.move_to_end(key)
            
            return entry.value
        
        def set(self, key, value, expiry=None):
            """设置缓存项"""
            # 如果键已存在，先删除
            if key in self.cache:
                self.delete(key)
            
            # 如果缓存已满，删除最久未使用的项
            if len(self.cache) >= self.capacity:
                oldest_key, _ = self.order.popitem(last=False)
                del self.cache[oldest_key]
            
            # 创建新条目
            entry = CacheEntry(key, value, expiry)
            self.cache[key] = entry
            self.order[key] = entry.last_accessed
        
        def delete(self, key):
            """删除缓存项"""
            if key in self.cache:
                del self.cache[key]
                if key in self.order:
                    del self.order[key]
        
        def clear(self):
            """清空缓存"""
            self.cache.clear()
            self.order.clear()
        
        def size(self):
            """获取缓存大小"""
            return len(self.cache)
        
        def get_stats(self):
            """获取缓存统计信息"""
            if not self.cache:
                return {}
            
            entries = list(self.cache.values())
            oldest = min(entries, key=lambda e: e.created_at)
            newest = max(entries, key=lambda e: e.created_at)
            most_accessed = max(entries, key=lambda e: e.access_count)
            
            return {
                'total_entries': len(entries),
                'oldest_entry_age': time.time() - oldest.created_at,
                'newest_entry_age': time.time() - newest.created_at,
                'most_accessed_key': most_accessed.key,
                'most_accessed_count': most_accessed.access_count
            }
    
    class LFUCache:
        """LFU（最少使用频率）缓存实现"""
        def __init__(self, capacity=100):
            self.capacity = capacity
            self.cache = {}  # 键到缓存条目的映射
            self.freq_map = collections.defaultdict(collections.OrderedDict)  # 频率到条目的映射
            self.min_freq = 0
        
        def get(self, key):
            """获取缓存项"""
            if key not in self.cache:
                return None
            
            entry = self.cache[key]
            
            # 检查过期
            if entry.is_expired():
                self.delete(key)
                return None
            
            # 更新频率
            self._update_frequency(entry)
            
            # 更新访问信息
            entry.access()
            
            return entry.value
        
        def set(self, key, value, expiry=None):
            """设置缓存项"""
            if self.capacity == 0:
                return
            
            # 如果键已存在，先删除
            if key in self.cache:
                self.delete(key)
            
            # 如果缓存已满，删除频率最低的项
            if len(self.cache) >= self.capacity:
                # 获取最小频率的OrderedDict
                lfu_dict = self.freq_map[self.min_freq]
                # 删除最久未使用的项
                oldest_key, _ = lfu_dict.popitem(last=False)
                del self.cache[oldest_key]
                
                # 如果最小频率的OrderedDict为空，删除它
                if not lfu_dict:
                    del self.freq_map[self.min_freq]
            
            # 创建新条目，频率为1
            entry = CacheEntry(key, value, expiry)
            self.cache[key] = entry
            self.freq_map[1][key] = entry
            self.min_freq = 1  # 新项的频率一定是最小的
        
        def delete(self, key):
            """删除缓存项"""
            if key in self.cache:
                entry = self.cache[key]
                freq = entry.access_count - 1  # 因为刚创建时access_count是1
                
                # 从频率映射中删除
                if freq in self.freq_map:
                    del self.freq_map[freq][key]
                    # 如果该频率的OrderedDict为空，删除它
                    if not self.freq_map[freq]:
                        del self.freq_map[freq]
                        # 如果删除的是最小频率，更新最小频率
                        if freq == self.min_freq and self.freq_map:
                            self.min_freq = min(self.freq_map.keys())
                
                # 从缓存中删除
                del self.cache[key]
        
        def _update_frequency(self, entry):
            """更新条目的频率"""
            key = entry.key
            old_freq = entry.access_count - 1  # 因为刚访问过，所以减1
            new_freq = entry.access_count
            
            # 从旧频率中移除
            if old_freq in self.freq_map:
                if key in self.freq_map[old_freq]:
                    del self.freq_map[old_freq][key]
                    # 如果旧频率的OrderedDict为空，删除它
                    if not self.freq_map[old_freq]:
                        del self.freq_map[old_freq]
                        # 如果删除的是最小频率，更新最小频率
                        if old_freq == self.min_freq:
                            self.min_freq = min(self.freq_map.keys()) if self.freq_map else 0
            
            # 添加到新频率
            self.freq_map[new_freq][key] = entry
            
            # 如果是新的最小频率，更新min_freq
            if self.min_freq == 0 or new_freq < self.min_freq:
                self.min_freq = new_freq
        
        def clear(self):
            """清空缓存"""
            self.cache.clear()
            self.freq_map.clear()
            self.min_freq = 0
        
        def size(self):
            """获取缓存大小"""
            return len(self.cache)
        
        def get_stats(self):
            """获取缓存统计信息"""
            if not self.cache:
                return {}
            
            entries = list(self.cache.values())
            oldest = min(entries, key=lambda e: e.created_at)
            newest = max(entries, key=lambda e: e.created_at)
            most_accessed = max(entries, key=lambda e: e.access_count)
            
            return {
                'total_entries': len(entries),
                'oldest_entry_age': time.time() - oldest.created_at,
                'newest_entry_age': time.time() - newest.created_at,
                'most_accessed_key': most_accessed.key,
                'most_accessed_count': most_accessed.access_count,
                'min_frequency': self.min_freq if self.freq_map else 0,
                'frequency_distribution': {freq: len(items) for freq, items in self.freq_map.items()}
            }
    
    class MultiLevelCache:
        """多级缓存系统"""
        def __init__(self):
            # L1: 小容量，高性能缓存（LRU）
            self.l1 = LRUCache(capacity=10)
            # L2: 中等容量，普通缓存（LRU）
            self.l2 = LRUCache(capacity=50)
            # L3: 大容量，LFU缓存（适合长期保存热点数据）
            self.l3 = LFUCache(capacity=200)
            
            # 统计信息
            self.hits = {
                'l1': 0,
                'l2': 0,
                'l3': 0,
                'miss': 0
            }
        
        def get(self, key):
            """获取缓存项，从L1到L3依次查找"""
            # 先查L1
            value = self.l1.get(key)
            if value is not None:
                self.hits['l1'] += 1
                return value
            
            # 再查L2
            value = self.l2.get(key)
            if value is not None:
                self.hits['l2'] += 1
                # 提升到L1
                self.l1.set(key, value)
                return value
            
            # 最后查L3
            value = self.l3.get(key)
            if value is not None:
                self.hits['l3'] += 1
                # 提升到L2和L1
                self.l2.set(key, value)
                self.l1.set(key, value)
                return value
            
            # 缓存未命中
            self.hits['miss'] += 1
            return None
        
        def set(self, key, value, expiry=None, level=None):
            """设置缓存项"""
            if level == 'l1':
                # 只设置到L1
                self.l1.set(key, value, expiry)
            elif level == 'l2':
                # 设置到L1和L2
                self.l1.set(key, value, expiry)
                self.l2.set(key, value, expiry)
            else:
                # 默认设置到所有级别
                self.l1.set(key, value, expiry)
                self.l2.set(key, value, expiry)
                self.l3.set(key, value, expiry)
        
        def delete(self, key):
            """删除缓存项"""
            self.l1.delete(key)
            self.l2.delete(key)
            self.l3.delete(key)
        
        def clear(self):
            """清空所有缓存"""
            self.l1.clear()
            self.l2.clear()
            self.l3.clear()
            # 重置统计信息
            for k in self.hits:
                self.hits[k] = 0
        
        def get_stats(self):
            """获取缓存统计信息"""
            total = sum(self.hits.values())
            hit_rate = (total - self.hits['miss']) / total if total > 0 else 0
            
            return {
                'hit_rate': hit_rate,
                'hits': self.hits,
                'l1_stats': self.l1.get_stats(),
                'l2_stats': self.l2.get_stats(),
                'l3_stats': self.l3.get_stats()
            }
    
    # 2. 实现缓存装饰器
    print("2. 实现缓存装饰器...")
    
    # 使用functools.wraps和lru_cache的思想，但使用我们自己的缓存系统
    def cached_function(cache, expiry=None, key_generator=None):
        """函数缓存装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 生成缓存键
                if key_generator:
                    cache_key = key_generator(*args, **kwargs)
                else:
                    # 简单的键生成器
                    cache_key = f"{func.__name__}:{args}:{kwargs}"
                
                # 尝试从缓存获取
                result = cache.get(cache_key)
                if result is not None:
                    return result
                
                # 缓存未命中，执行函数
                result = func(*args, **kwargs)
                
                # 存入缓存
                cache.set(cache_key, result, expiry)
                
                return result
            
            return wrapper
        
        return decorator
    
    # 3. 演示缓存系统
    print("3. 演示缓存系统...")
    
    # 创建多级缓存
    multi_cache = MultiLevelCache()
    
    # 定义一些模拟的耗时操作函数
    @cached_function(multi_cache, expiry=5)  # 5秒后过期
    def expensive_computation(x, y):
        """模拟耗时计算"""
        print(f"执行耗时计算: {x} + {y}")
        time.sleep(0.1)  # 模拟耗时操作
        return x + y
    
    @cached_function(multi_cache)
    def get_user_data(user_id):
        """模拟获取用户数据"""
        print(f"从数据库获取用户{user_id}的数据")
        time.sleep(0.2)  # 模拟数据库查询
        return {
            'id': user_id,
            'name': f'用户{user_id}',
            'email': f'user{user_id}@example.com',
            'created_at': time.time() - random.randint(100000, 1000000)
        }
    
    @cached_function(multi_cache, key_generator=lambda product_id: f"product:{product_id}")
    def get_product_info(product_id):
        """模拟获取产品信息"""
        print(f"从数据库获取产品{product_id}的信息")
        time.sleep(0.15)  # 模拟数据库查询
        return {
            'id': product_id,
            'name': f'产品{product_id}',
            'price': random.randint(100, 1000),
            'stock': random.randint(0, 1000)
        }
    
    # 4. 执行模拟操作
    print("4. 执行缓存性能测试...")
    
    # 测试基本缓存功能
    print("\n4.1 基本缓存功能测试:")
    
    # 首次调用（应该执行）
    print("首次调用 expensive_computation(1, 2):")
    result1 = expensive_computation(1, 2)
    print(f"结果: {result1}")
    
    # 再次调用相同参数（应该从缓存获取）
    print("\n再次调用 expensive_computation(1, 2):")
    result2 = expensive_computation(1, 2)
    print(f"结果: {result2}")
    
    # 调用不同参数（应该执行）
    print("\n调用 expensive_computation(3, 4):")
    result3 = expensive_computation(3, 4)
    print(f"结果: {result3}")
    
    # 测试用户数据缓存
    print("\n4.2 用户数据缓存测试:")
    
    # 多次获取同一用户数据
    for i in range(3):
        print(f"\n第{i+1}次获取用户100的信息:")
        user_data = get_user_data(100)
        print(f"用户数据: {user_data['name']}")
    
    # 获取不同用户数据
    print("\n获取用户101的信息:")
    user_data = get_user_data(101)
    print(f"用户数据: {user_data['name']}")
    
    # 5. 压力测试
    print("\n5. 缓存压力测试...")
    
    # 记录开始时间
    start_time = time.time()
    
    # 执行多次缓存操作
    operations = 1000
    print(f"执行{operations}次缓存操作...")
    
    # 使用itertools生成测试参数
    for i, (x, y) in enumerate(itertools.product(range(20), range(10)), 1):
        # 访问计算结果
        expensive_computation(x, y)
        
        # 访问一些用户数据
        if i % 5 == 0:
            user_id = (i // 5) % 30
            get_user_data(user_id)
        
        # 访问一些产品信息
        if i % 7 == 0:
            product_id = (i // 7) % 50
            get_product_info(product_id)
        
        if i >= operations:
            break
    
    # 计算耗时
    elapsed_time = time.time() - start_time
    print(f"压力测试完成，耗时: {elapsed_time:.2f}秒")
    
    # 6. 显示缓存统计信息
    print("\n6. 缓存统计信息:")
    
    stats = multi_cache.get_stats()
    print(f"缓存命中率: {stats['hit_rate']:.2%}")
    print("\n命中分布:")
    print(f"  L1缓存命中: {stats['hits']['l1']}")
    print(f"  L2缓存命中: {stats['hits']['l2']}")
    print(f"  L3缓存命中: {stats['hits']['l3']}")
    print(f"  缓存未命中: {stats['hits']['miss']}")
    
    print("\nL1缓存统计:")
    l1_stats = stats['l1_stats']
    print(f"  条目数: {l1_stats.get('total_entries', 0)}")
    print(f"  最常访问键: {l1_stats.get('most_accessed_key', 'N/A')} (访问{l1_stats.get('most_accessed_count', 0)}次)")
    
    print("\nL3缓存频率分布:")
    freq_dist = stats['l3_stats'].get('frequency_distribution', {})
    for freq, count in sorted(freq_dist.items())[:10]:  # 只显示前10个
        print(f"  访问频率{freq}: {count}个条目")
    
    print("\n高级缓存系统演示完成！")
    print()


# 运行所有综合示例
def run_all_examples():
    """运行所有综合示例"""
    print("===== Python数据结构模块综合应用示例 =====\n")
    
    # 运行各个示例
    try:
        example_data_processing_pipeline()
        print("=" * 80)
        print()
        
        example_task_scheduling_system()
        print("=" * 80)
        print()
        
        example_search_engine_ranking()
        print("=" * 80)
        print()
        
        example_machine_learning_pipeline()
        print("=" * 80)
        print()
        
        example_advanced_caching_system()
        print("=" * 80)
        print()
        
        print("✅ 所有综合示例运行完成！")
    
    except Exception as e:
        print(f"❌ 运行示例时出错: {e}")
        import traceback
        traceback.print_exc()


# 如果直接运行此文件，则执行所有示例
if __name__ == "__main__":
    run_all_examples()
    print("5. 执行搜索演示...")
    
    # 创建搜索引擎实例
    import math
    search_engine = SearchEngine(processed_docs, inverted_index)
    
    # 测试不同查询
    queries = [
        "Python编程",
        "Python数据分析",
        "Python性能优化"
    ]
    
    for query in queries:
        print(f"\n执行查询: '{query}'")
        results = search_engine.search(query)
        
        print(f"找到{len(results)}个结果:")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result['title']}")
            print(f"   URL: {result['url']}")
            print(f"   相关度: {result['score']}")
            print(f"   摘要: {result['snippet']}")
    
    # 测试高级搜索
    print("\n6. 执行高级搜索演示...")
    
    print("搜索'Python'，要求域名权重≥9.0:")
    advanced_results = search_engine.advanced_search("Python", filters={'min_authority': 9.0})
    
    for i, result in enumerate(advanced_results, 1):
        doc = processed_docs[result['doc_id'] - 1]  # 文档ID从1开始
        print(f"\n{i}. {result['title']}")
        print(f"   URL: {result['url']}")
        print(f"   域名权重: {doc['authority']}")
        print(f"   反向链接: {doc['backlinks']}")
    
    print("\n搜索'Python开发'，按反向链接数排序:")
    backlink_results = search_engine.advanced_search("Python开发", sort_by='backlinks')
    
    for i, result in enumerate(backlink_results, 1):
        doc = processed_docs[result['doc_id'] - 1]
        print(f"\n{i}. {result['title']}")
        print(f"   URL: {result['url']}")
        print(f"   反向链接: {doc['backlinks']}")
    
    print("\n搜索引擎演示完成！")
    print()


def example_machine_learning_pipeline():
    """示例4: 机器学习数据处理管道"""
    print("=== 示例4: 机器学习数据处理管道 ===")
    
    # 1. 生成模拟数据集
    print("1. 生成模拟机器学习数据集...")
    
    def generate_sample_data(n_samples=1000):
        """生成模拟的机器学习数据集"""
        random.seed(42)  # 设置随机种子以保证结果可重复
        
        data = []
        for i in range(n_samples):
            # 生成特征
            age = random.randint(18, 80)
            income = random.randint(20000, 150000)
            credit_score = random.randint(300, 850)
            debt_ratio = random.uniform(0.1, 0.8)
            employment_years = random.randint(0, 40)
            loan_amount = random.randint(5000, 100000)
            
            # 模拟一些缺失值
            has_missing = random.random() < 0.05  # 5%的概率有缺失值
            
            if has_missing:
                # 随机选择一个特征设置为None
                missing_feature = random.choice(['income', 'credit_score', 'debt_ratio', 'employment_years'])
                if missing_feature == 'income':
                    income = None
                elif missing_feature == 'credit_score':
                    credit_score = None
                elif missing_feature == 'debt_ratio':
                    debt_ratio = None
                elif missing_feature == 'employment_years':
                    employment_years = None
            
            # 生成目标变量（贷款违约概率）
            # 简单的逻辑：年龄越大、收入越高、信用分数越高、债务比率越低、就业年限越长，违约概率越低
            default_prob = 0.5
            if age is not None:
                default_prob -= (age - 50) * 0.002
            if income is not None:
                default_prob -= (income - 85000) * 0.000001
            if credit_score is not None:
                default_prob -= (credit_score - 575) * 0.001
            if debt_ratio is not None:
                default_prob += (debt_ratio - 0.45) * 0.3
            if employment_years is not None:
                default_prob -= (employment_years - 20) * 0.005
            
            # 确保概率在合理范围内
            default_prob = max(0.01, min(0.99, default_prob))
            
            # 生成二分类目标
            default = 1 if random.random() < default_prob else 0
            
            data.append({
                'id': i + 1,
                'age': age,
                'income': income,
                'credit_score': credit_score,
                'debt_ratio': debt_ratio,
                'employment_years': employment_years,
                'loan_amount': loan_amount,
                'default': default
            })
        
        return data
    
    # 生成数据集
    dataset = generate_sample_data(1000)
    print(f"生成了{len(dataset)}条样本数据")
    print("示例数据:")
    pprint(dataset[:2])
    print()
    
    # 2. 数据预处理管道
    print("2. 实现数据预处理管道...")
    
    class DataPreprocessor:
        def __init__(self):
            self.statistics = None
        
        def fit(self, data):
            """计算数据统计信息"""
            # 按特征收集有效值
            features = ['age', 'income', 'credit_score', 'debt_ratio', 'employment_years', 'loan_amount']
            feature_values = {feature: [] for feature in features}
            
            for record in data:
                for feature in features:
                    if record[feature] is not None:
                        feature_values[feature].append(record[feature])
            
            # 计算统计信息
            self.statistics = {}
            for feature, values in feature_values.items():
                if values:
                    self.statistics[feature] = {
                        'mean': sum(values) / len(values),
                        'median': sorted(values)[len(values) // 2],
                        'std': math.sqrt(sum((x - sum(values) / len(values)) ** 2 for x in values) / len(values)),
                        'min': min(values),
                        'max': max(values)
                    }
            
            return self
        
        def transform(self, data, impute_strategy='mean'):
            """转换数据"""
            if not self.statistics:
                raise ValueError("需要先调用fit方法")
            
            transformed_data = []
            for record in data:
                transformed_record = record.copy()
                
                # 处理缺失值
                for feature in ['age', 'income', 'credit_score', 'debt_ratio', 'employment_years']:
                    if transformed_record[feature] is None:
                        if impute_strategy == 'mean':
                            transformed_record[feature] = self.statistics[feature]['mean']
                        elif impute_strategy == 'median':
                            transformed_record[feature] = self.statistics[feature]['median']
                
                # 特征工程
                # 年龄分组
                age = transformed_record['age']
                transformed_record['is_young'] = 1 if age < 30 else 0
                transformed_record['is_middle_aged'] = 1 if 30 <= age < 60 else 0
                transformed_record['is_senior'] = 1 if age >= 60 else 0
                
                # 收入分组
                income = transformed_record['income']
                transformed_record['income_level_low'] = 1 if income < 50000 else 0
                transformed_record['income_level_middle'] = 1 if 50000 <= income < 100000 else 0
                transformed_record['income_level_high'] = 1 if income >= 100000 else 0
                
                # 信用评分分组
                credit = transformed_record['credit_score']
                transformed_record['credit_good'] = 1 if credit >= 670 else 0
                transformed_record['credit_fair'] = 1 if 580 <= credit < 670 else 0
                transformed_record['credit_poor'] = 1 if credit < 580 else 0
                
                # 债务收入比
                if transformed_record['income'] > 0:
                    transformed_record['debt_to_income'] = transformed_record['debt_ratio'] * transformed_record['income'] / 10000
                else:
                    transformed_record['debt_to_income'] = 0
                
                # 贷款收入比
                if transformed_record['income'] > 0:
                    transformed_record['loan_to_income'] = transformed_record['loan_amount'] / transformed_record['income']
                else:
                    transformed_record['loan_to_income'] = 0
                
                # 就业稳定性
                emp_years = transformed_record['employment_years']
                transformed_record['employment_stable'] = 1 if emp_years >= 2 else 0
                transformed_record['employment_long_term'] = 1 if emp_years >= 5 else 0
                
                transformed_data.append(transformed_record)
            
            return transformed_data
        
        def fit_transform(self, data, impute_strategy='mean'):
            """合并fit和transform"""
            return self.fit(data).transform(data, impute_strategy)
    
    # 3. 数据探索和分析
    print("3. 数据探索和分析...")
    
    # 统计基本信息
    def analyze_data(data):
        # 统计缺失值
        missing_counts = collections.defaultdict(int)
        total_records = len(data)
        
        for record in data:
            for key, value in record.items():
                if value is None:
                    missing_counts[key] += 1
        
        print("缺失值统计:")
        for feature, count in missing_counts.items():
            percent = (count / total_records) * 100
            print(f"  {feature}: {count} ({percent:.2f}%)")
        
        # 统计目标变量分布
        default_count = sum(1 for record in data if record['default'] == 1)
        non_default_count = total_records - default_count
        
        print("\n目标变量分布:")
        print(f"  违约数量: {default_count} ({default_count/total_records*100:.2f}%)")
        print(f"  正常数量: {non_default_count} ({non_default_count/total_records*100:.2f}%)")
        
        # 统计各年龄段违约率
        age_groups = collections.defaultdict(lambda: {'total': 0, 'default': 0})
        
        for record in data:
            if record['age'] is not None:
                if record['age'] < 30:
                    group = '<30'
                elif record['age'] < 45:
                    group = '30-44'
                elif record['age'] < 60:
                    group = '45-59'
                else:
                    group = '60+'
                
                age_groups[group]['total'] += 1
                age_groups[group]['default'] += record['default']
        
        print("\n各年龄段违约率:")
        for group in sorted(age_groups.keys()):
            stats = age_groups[group]
            if stats['total'] > 0:
                default_rate = (stats['default'] / stats['total']) * 100
                print(f"  {group}岁: {default_rate:.2f}% ({stats['default']}/{stats['total']})")
    
    # 执行数据分析
    analyze_data(dataset)
    
    # 4. 实现机器学习管道
    print("\n4. 实现机器学习管道...")
    
    # 简单的机器学习模型和评估函数
    def train_model(X_train, y_train, model_type='simple'):
        """训练简单模型（这里只是模拟）"""
        print(f"训练{model_type}模型...")
        time.sleep(0.5)  # 模拟训练时间
        
        # 模拟模型参数（实际应用中会返回真实模型）
        if model_type == 'simple':
            # 简单规则模型
            print("使用简单规则模型")
            return {'type': 'rule_based'}
        else:
            # 复杂模型
            print("使用复杂模型")
            return {'type': 'complex'}
    
    def evaluate_model(model, X_test, y_test):
        """评估模型（这里只是模拟）"""
        print("评估模型...")
        time.sleep(0.3)  # 模拟评估时间
        
        # 生成模拟评估指标
        if model['type'] == 'rule_based':
            accuracy = 0.72
            precision = 0.65
            recall = 0.58
            f1_score = 0.61
        else:
            accuracy = 0.78
            precision = 0.71
            recall = 0.65
            f1_score = 0.68
        
        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1_score
        }
    
    # 5. 执行完整的数据处理和建模流程
    print("\n5. 执行完整的数据处理和建模流程...")
    
    # 数据分割（模拟训练集和测试集）
    train_size = int(0.8 * len(dataset))
    train_data = dataset[:train_size]
    test_data = dataset[train_size:]
    
    print(f"训练集大小: {len(train_data)}")
    print(f"测试集大小: {len(test_data)}")
    
    # 数据预处理
    preprocessor = DataPreprocessor()
    train_processed = preprocessor.fit_transform(train_data)
    test_processed = preprocessor.transform(test_data)
    
    print(f"预处理后训练集特征数量: {len(train_processed[0]) - 2}")  # 减去id和default
    
    # 准备特征和标签
    def prepare_features(data):
        features = []
        labels = []
        
        for record in data:
            # 提取特征（排除id和default）
            feature_vector = [
                record['age'], record['income'], record['credit_score'], 
                record['debt_ratio'], record['employment_years'], record['loan_amount'],
                record['is_young'], record['is_middle_aged'], record['is_senior'],
                record['income_level_low'], record['income_level_middle'], record['income_level_high'],
                record['credit_good'], record['credit_fair'], record['credit_poor'],
                record['debt_to_income'], record['loan_to_income'],
                record['employment_stable'], record['employment_long_term']
            ]
            features.append(feature_vector)
            labels.append(record['default'])
        
        return features, labels
    
    X_train, y_train = prepare_features(train_processed)
    X_test, y_test = prepare_features(test_processed)
    
    # 训练和评估模型
    print("\n训练和评估简单模型:")
    simple_model = train_model(X_train, y_train, model_type='simple')
    simple_metrics = evaluate_model(simple_model, X_test, y_test)
    
    print("简单模型评估指标:")
    for metric, value in simple_metrics.items():
        print(f"  {metric}: {value:.4f}")
    
    print("\n训练和评估复杂模型:")
    complex_model = train_model(X_train, y_train, model_type='complex')
    complex_metrics = evaluate_model(complex_model, X_test, y_test)
    
    print("复杂模型评估指标:")
    for metric, value in complex_metrics.items():
        print(f"  {metric}: {value:.4f}")
    
    # 6. 模型解释和特征重要性
    print("\n6. 模型解释和特征重要性...")
    
    # 模拟特征重要性（实际应用中会使用真实的特征重要性计算）
    feature_names = [
        'age', 'income', 'credit_score', 'debt_ratio', 'employment_years', 'loan_amount',
        'is_young', 'is_middle_aged', 'is_senior',
        'income_level_low', 'income_level_middle', 'income_level_high',
        'credit_good', 'credit_fair', 'credit_poor',
        'debt_to_income', 'loan_to_income',
        'employment_stable', 'employment_long_term'
    ]
    
    # 生成模拟特征重要性
    import numpy as np
    np.random.seed(42)
    importances = np.random.rand(len(feature_names))
    
    # 让某些特征的重要性更高，使其看起来更合理
    important_indices = [2, 4, 14, 15]  # credit_score, employment_years, credit_poor, debt_to_income
    for idx in important_indices:
        importances[idx] *= 1.5
    
    # 归一化
    importances = importances / importances.sum()
    
    # 排序并显示前10个重要特征
    feature_importance_pairs = list(zip(feature_names, importances))
    feature_importance_pairs.sort(key=operator.itemgetter(1), reverse=True)
    
    print("特征重要性（前10名）:")
    for i, (feature, importance) in enumerate(feature_importance_pairs[:10], 1):
        print(f"  {i}. {feature}: {importance:.4f}")
    
    print("\n机器学习管道演示完成！")
    print()


def example_advanced_caching_system():
    """示例5: 高级缓存系统实现"""
    print("=== 示例5: 高级缓存系统实现 ===")
    
    # 1. 实现多级缓存系统
    print("1. 实现多级缓存系统...")
    
    class CacheLevel:
        L1 = "L1"  # 最快，最小
        L2 = "L2"  # 中等，中等
        L3 = "L3"  # 最慢，最大
    
    class AdvancedCache:
        def __init__(self, l1_size=100, l2_size=500, l3_size=2000, l1_ttl=60, l2_ttl=300, l3_ttl=1800):
            """初始化多级缓存系统"""
            # L1缓存：使用functools.lru_cache的思想，但实现我们自己的LRU缓存
            self.l1_cache = collections.OrderedDict()
            self.l1_size = l1_size
            self.l1_ttl = l1_ttl
            
            # L2缓存：更大但访问稍慢
            self.l2_cache = collections.OrderedDict()
            self.l2_size = l2_size
            self.l2_ttl = l2_ttl
            
            # L3缓存：最大但访问最慢
            self.l3_cache = collections.OrderedDict()
            self.l3_size = l3_size
            self.l3_ttl = l3_ttl
            
            # 缓存统计信息
            self.stats = collections.defaultdict(int)
            
            # 使用Counter生成缓存统计
            self.hit_counts = collections.Counter()
            self.miss_counts = collections.Counter()
            
            # 使用deque记录最近访问的键
            self.recent_keys = collections.deque(maxlen=1000)
        
        def _get_with_expiry(self, cache, key):
            """从缓存中获取值，并检查是否过期"""
            if key not in cache:
                return None
            
            value, expiry_time = cache[key]
            current_time = time.time()
            
            # 如果过期，删除并返回None
            if current_time > expiry_time:
                del cache[key]
                return None
            
            return value
        
        def _put_with_expiry(self, cache, key, value, ttl, max_size):
            """将值放入缓存，并设置过期时间"""
            expiry_time = time.time() + ttl
            
            # 如果键已存在，先删除（以便将其移到最近使用）
            if key in cache:
                del cache[key]
            # 如果缓存已满，删除最久未使用的项
            elif len(cache) >= max_size:
                cache.popitem(last=False)
            
            # 添加到缓存末尾（最近使用）
            cache[key] = (value, expiry_time)
        
        def get(self, key):
            """从缓存中获取值，按L1->L2->L3顺序查找"""
            self.stats['total_gets'] += 1
            current_time = time.time()
            
            # 记录最近访问的键
            self.recent_keys.append((current_time, key))
            
            # 1. 检查L1缓存
            value = self._get_with_expiry(self.l1_cache, key)
            if value is not None:
                self.stats['l1_hits'] += 1
                self.hit_counts[CacheLevel.L1] += 1
                # 为了演示，我们不把L1的命中提升到更高层次
                return value
            
            # 2. 检查L2缓存
            value = self._get_with_expiry(self.l2_cache, key)
            if value is not None:
                self.stats['l2_hits'] += 1
                self.hit_counts[CacheLevel.L2] += 1
                # 提升到L1缓存
                self._put_with_expiry(self.l1_cache, key, value, self.l1_ttl, self.l1_size)
                return value
            
            # 3. 检查L3缓存
            value = self._get_with_expiry(self.l3_cache, key)
            if value is not None:
                self.stats['l3_hits'] += 1
                self.hit_counts[CacheLevel.L3] += 1
                # 提升到L2缓存
                self._put_with_expiry(self.l2_cache, key, value, self.l2_ttl, self.l2_size)
                # 提升到L1缓存
                self._put_with_expiry(self.l1_cache, key, value, self.l1_ttl, self.l1_size)
                return value
            
            # 缓存未命中
            self.stats['cache_misses'] += 1
            self.miss_counts['all'] += 1
            return None
        
        def put(self, key, value, level=CacheLevel.L3):
            """将值放入指定级别的缓存"""
            self.stats['total_puts'] += 1
            
            # 根据级别放入不同缓存
            if level == CacheLevel.L1:
                self._put_with_expiry(self.l1_cache, key, value, self.l1_ttl, self.l1_size)
                self.stats['l1_puts'] += 1
            elif level == CacheLevel.L2:
                self._put_with_expiry(self.l2_cache, key, value, self.l2_ttl, self.l2_size)
                self._put_with_expiry(self.l1_cache, key, value, self.l1_ttl, self.l1_size)  # 同时放入L1
                self.stats['l2_puts'] += 1
            else:  # L3
                self._put_with_expiry(self.l3_cache, key, value, self.l3_ttl, self.l3_size)
                self._put_with_expiry(self.l2_cache, key, value, self.l2_ttl, self.l2_size)  # 同时放入L2
                self._put_with_expiry(self.l1_cache, key, value, self.l1_ttl, self.l1_size)  # 同时放入L1
                self.stats['l3_puts'] += 1
        
        def invalidate(self, key):
            """使指定键的缓存失效"""
            for cache in [self.l1_cache, self.l2_cache, self.l3_cache]:
                if key in cache:
                    del cache[key]
            
            self.stats['invalidations'] += 1
        
        def clear(self, level=None):
            """清除指定级别的缓存"""
            if level == CacheLevel.L1 or level is None:
                self.l1_cache.clear()
                self.stats['l1_clears'] += 1
            
            if level == CacheLevel.L2 or level is None:
                self.l2_cache.clear()
                self.stats['l2_clears'] += 1
            
            if level == CacheLevel.L3 or level is None:
                self.l3_cache.clear()
                self.stats['l3_clears'] += 1
        
        def get_stats(self):
            """获取缓存统计信息"""
            total_hits = self.stats['l1_hits'] + self.stats['l2_hits'] + self.stats['l3_hits']
            total_ops = self.stats['total_gets']
            hit_rate = total_hits / total_ops if total_ops > 0 else 0
            
            return {
                'total_gets': self.stats['total_gets'],
                'total_puts': self.stats['total_puts'],
                'l1_hits': self.stats