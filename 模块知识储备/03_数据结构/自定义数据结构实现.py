# Python自定义数据结构实现

"""
本文件展示如何在Python中实现各种常见的自定义数据结构，
包括链表、树、图等，以及它们的基本操作和应用场景。
Python标准库提供了许多内置数据结构，但在某些特定场景下，
我们可能需要实现自定义数据结构来满足特定需求。

主要内容包括：
- 链表（单链表、双链表、循环链表）
- 栈和队列的自定义实现
- 二叉树及遍历算法
- 图及其表示方法
- 哈希表实现
- 自定义数据结构的应用场景
"""

# 1. 链表实现

print("=== 1. 链表实现 ===")

## 1.1 单链表

class ListNode:
    """单链表节点类"""
    def __init__(self, value=0, next=None):
        self.value = value  # 节点值
        self.next = next    # 指向下一个节点的引用

class SinglyLinkedList:
    """单链表类"""
    def __init__(self):
        self.head = None  # 头节点
        self.size = 0     # 链表大小
    
    def is_empty(self):
        """检查链表是否为空"""
        return self.head is None
    
    def append(self, value):
        """在链表末尾添加元素"""
        new_node = ListNode(value)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def prepend(self, value):
        """在链表头部添加元素"""
        new_node = ListNode(value, self.head)
        self.head = new_node
        self.size += 1
    
    def insert(self, index, value):
        """在指定位置插入元素"""
        if index <= 0:
            self.prepend(value)
        elif index >= self.size:
            self.append(value)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node = ListNode(value, current.next)
            current.next = new_node
            self.size += 1
    
    def remove(self, value):
        """删除第一个匹配的值"""
        if self.is_empty():
            return False
        
        # 如果头节点是要删除的节点
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return True
        
        # 查找要删除的节点
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        
        # 如果找到匹配的节点
        if current.next:
            current.next = current.next.next
            self.size -= 1
            return True
        
        return False
    
    def find(self, value):
        """查找元素是否存在"""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def __str__(self):
        """返回链表的字符串表示"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)
    
    def __len__(self):
        """返回链表长度"""
        return self.size

# 单链表示例
sll = SinglyLinkedList()
for i in range(5):
    sll.append(i)
print(f"创建的单链表: {sll}")
print(f"单链表长度: {len(sll)}")

sll.prepend(-1)
print(f"头部添加-1后的链表: {sll}")

sll.insert(3, 99)
print(f"在位置3插入99后的链表: {sll}")

sll.remove(2)
print(f"删除值为2后的链表: {sll}")

print(f"查找值为99: {sll.find(99)}")
print(f"查找值为100: {sll.find(100)}")

## 1.2 双链表

class DListNode:
    """双链表节点类"""
    def __init__(self, value=0, prev=None, next=None):
        self.value = value  # 节点值
        self.prev = prev    # 指向前一个节点的引用
        self.next = next    # 指向下一个节点的引用

class DoublyLinkedList:
    """双链表类"""
    def __init__(self):
        self.head = None  # 头节点
        self.tail = None  # 尾节点
        self.size = 0     # 链表大小
    
    def is_empty(self):
        """检查链表是否为空"""
        return self.head is None
    
    def append(self, value):
        """在链表末尾添加元素"""
        new_node = DListNode(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def prepend(self, value):
        """在链表头部添加元素"""
        new_node = DListNode(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def remove(self, value):
        """删除第一个匹配的值"""
        if self.is_empty():
            return False
        
        # 如果头节点是要删除的节点
        if self.head.value == value:
            if self.head == self.tail:  # 只有一个节点
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return True
        
        # 如果尾节点是要删除的节点
        if self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return True
        
        # 查找要删除的节点
        current = self.head.next
        while current != self.tail and current.value != value:
            current = current.next
        
        # 如果找到匹配的节点
        if current.value == value:
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
            return True
        
        return False
    
    def __str__(self):
        """返回链表的字符串表示（从头到尾）"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " <-> ".join(elements)
    
    def __len__(self):
        """返回链表长度"""
        return self.size

# 双链表示例
dll = DoublyLinkedList()
for i in range(5):
    dll.append(i)
print(f"\n创建的双链表: {dll}")
print(f"双链表长度: {len(dll)}")

dll.prepend(-1)
dll.append(10)
print(f"添加元素后的双链表: {dll}")

dll.remove(0)
print(f"删除值为0后的双链表: {dll}")

dll.remove(10)
print(f"删除值为10后的双链表: {dll}")

## 1.3 循环链表

class CircularLinkedList:
    """循环单链表类"""
    def __init__(self):
        self.head = None  # 头节点
        self.size = 0     # 链表大小
    
    def is_empty(self):
        """检查链表是否为空"""
        return self.head is None
    
    def append(self, value):
        """在链表末尾添加元素"""
        new_node = ListNode(value)
        
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head  # 循环指向自身
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head  # 新节点指向头节点形成循环
        
        self.size += 1
    
    def prepend(self, value):
        """在链表头部添加元素"""
        new_node = ListNode(value)
        
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            self.head = new_node
            current.next = self.head  # 尾节点指向新的头节点
        
        self.size += 1
    
    def remove(self, value):
        """删除第一个匹配的值"""
        if self.is_empty():
            return False
        
        # 特殊情况：只有一个节点
        if self.head.next == self.head and self.head.value == value:
            self.head = None
            self.size -= 1
            return True
        
        # 情况1：头节点是要删除的节点
        if self.head.value == value:
            # 找到尾节点
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            self.size -= 1
            return True
        
        # 情况2：在链表中间查找要删除的节点
        current = self.head
        while current.next != self.head and current.next.value != value:
            current = current.next
        
        # 如果找到匹配的节点
        if current.next.value == value:
            current.next = current.next.next
            self.size -= 1
            return True
        
        return False
    
    def __str__(self):
        """返回链表的字符串表示"""
        if self.is_empty():
            return ""
            
        elements = []
        current = self.head
        while True:
            elements.append(str(current.value))
            current = current.next
            if current == self.head:  # 回到起点，结束循环
                break
        return " -> ".join(elements) + " -> (回到头部)"
    
    def __len__(self):
        """返回链表长度"""
        return self.size

# 循环链表示例
cll = CircularLinkedList()
for i in range(5):
    cll.append(i)
print(f"\n创建的循环链表: {cll}")
print(f"循环链表长度: {len(cll)}")

cll.prepend(-1)
print(f"头部添加-1后的循环链表: {cll}")

cll.remove(2)
print(f"删除值为2后的循环链表: {cll}")

# 2. 栈和队列的自定义实现

print("\n=== 2. 栈和队列的自定义实现 ===")

## 2.1 栈的基于链表实现

class StackLinkedList:
    """基于链表实现的栈"""
    def __init__(self):
        self.top = None  # 栈顶节点
        self.size = 0    # 栈大小
    
    def is_empty(self):
        """检查栈是否为空"""
        return self.top is None
    
    def push(self, value):
        """压栈操作"""
        new_node = ListNode(value, self.top)
        self.top = new_node
        self.size += 1
    
    def pop(self):
        """弹栈操作"""
        if self.is_empty():
            raise IndexError("栈为空，无法弹出元素")
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value
    
    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空，无法查看元素")
        return self.top.value
    
    def __len__(self):
        """返回栈的大小"""
        return self.size
    
    def __str__(self):
        """返回栈的字符串表示"""
        elements = []
        current = self.top
        while current:
            elements.append(str(current.value))
            current = current.next
        return "Stack: " + " -> ".join(elements)

# 栈示例
stack = StackLinkedList()
for i in range(5):
    stack.push(i)
print(f"创建的栈: {stack}")
print(f"栈大小: {len(stack)}")
print(f"栈顶元素: {stack.peek()}")

print(f"弹出元素: {stack.pop()}")
print(f"弹出后栈: {stack}")

## 2.2 队列的基于链表实现

class QueueLinkedList:
    """基于链表实现的队列"""
    def __init__(self):
        self.front = None  # 队列前端
        self.rear = None   # 队列后端
        self.size = 0      # 队列大小
    
    def is_empty(self):
        """检查队列是否为空"""
        return self.front is None
    
    def enqueue(self, value):
        """入队操作"""
        new_node = ListNode(value)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
    
    def dequeue(self):
        """出队操作"""
        if self.is_empty():
            raise IndexError("队列为空，无法出队")
        
        value = self.front.value
        self.front = self.front.next
        
        # 如果队列为空，更新rear
        if self.front is None:
            self.rear = None
        
        self.size -= 1
        return value
    
    def peek(self):
        """查看队首元素"""
        if self.is_empty():
            raise IndexError("队列为空，无法查看元素")
        return self.front.value
    
    def __len__(self):
        """返回队列的大小"""
        return self.size
    
    def __str__(self):
        """返回队列的字符串表示"""
        if self.is_empty():
            return "Queue: empty"
            
        elements = []
        current = self.front
        while current:
            elements.append(str(current.value))
            current = current.next
        return "Queue: " + " -> ".join(elements)

# 队列示例
queue = QueueLinkedList()
for i in range(5):
    queue.enqueue(i)
print(f"\n创建的队列: {queue}")
print(f"队列大小: {len(queue)}")
print(f"队首元素: {queue.peek()}")

print(f"出队元素: {queue.dequeue()}")
print(f"出队后队列: {queue}")

# 3. 二叉树实现

print("\n=== 3. 二叉树实现 ===")

class TreeNode:
    """二叉树节点类"""
    def __init__(self, value=0, left=None, right=None):
        self.value = value  # 节点值
        self.left = left    # 左子节点
        self.right = right  # 右子节点

class BinaryTree:
    """二叉树类"""
    def __init__(self, root=None):
        self.root = root  # 根节点
    
    def insert_level_order(self, value):
        """按层序插入元素"""
        if not self.root:
            self.root = TreeNode(value)
            return
        
        # 使用队列进行层序遍历
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            
            # 如果左子节点为空，插入左子节点
            if not node.left:
                node.left = TreeNode(value)
                return
            # 如果右子节点为空，插入右子节点
            elif not node.right:
                node.right = TreeNode(value)
                return
            # 否则将子节点加入队列
            else:
                queue.append(node.left)
                queue.append(node.right)
    
    def inorder_traversal(self):
        """中序遍历（左-根-右）"""
        result = []
        
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        
        _inorder(self.root)
        return result
    
    def preorder_traversal(self):
        """前序遍历（根-左-右）"""
        result = []
        
        def _preorder(node):
            if node:
                result.append(node.value)
                _preorder(node.left)
                _preorder(node.right)
        
        _preorder(self.root)
        return result
    
    def postorder_traversal(self):
        """后序遍历（左-右-根）"""
        result = []
        
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)
        
        _postorder(self.root)
        return result
    
    def level_order_traversal(self):
        """层序遍历"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.value)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result
    
    def height(self):
        """计算树的高度"""
        def _height(node):
            if not node:
                return 0
            return max(_height(node.left), _height(node.right)) + 1
        
        return _height(self.root)
    
    def size(self):
        """计算树中节点的数量"""
        def _size(node):
            if not node:
                return 0
            return _size(node.left) + _size(node.right) + 1
        
        return _size(self.root)

# 二叉树示例
tree = BinaryTree()
for i in range(1, 11):
    tree.insert_level_order(i)

print(f"二叉树高度: {tree.height()}")
print(f"二叉树节点数量: {tree.size()}")
print(f"中序遍历: {tree.inorder_traversal()}")
print(f"前序遍历: {tree.preorder_traversal()}")
print(f"后序遍历: {tree.postorder_traversal()}")
print(f"层序遍历: {tree.level_order_traversal()}")

# 4. 图的实现

print("\n=== 4. 图的实现 ===")

## 4.1 邻接表实现

class GraphAdjacencyList:
    """基于邻接表实现的图"""
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed  # 是否为有向图
    
    def add_vertex(self, vertex):
        """添加顶点"""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1):
        """添加边"""
        # 确保顶点存在
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        # 添加从vertex1到vertex2的边
        self.graph[vertex1].append((vertex2, weight))
        
        # 如果是无向图，同时添加从vertex2到vertex1的边
        if not self.directed:
            self.graph[vertex2].append((vertex1, weight))
    
    def get_vertices(self):
        """获取所有顶点"""
        return list(self.graph.keys())
    
    def get_edges(self):
        """获取所有边"""
        edges = []
        for vertex, neighbors in self.graph.items():
            for neighbor, weight in neighbors:
                edges.append((vertex, neighbor, weight))
        return edges
    
    def dfs(self, start_vertex):
        """深度优先搜索"""
        visited = set()
        result = []
        
        def _dfs(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    _dfs(neighbor)
        
        if start_vertex in self.graph:
            _dfs(start_vertex)
        return result
    
    def bfs(self, start_vertex):
        """广度优先搜索"""
        if start_vertex not in self.graph:
            return []
        
        visited = set([start_vertex])
        result = [start_vertex]
        queue = [start_vertex]
        
        while queue:
            vertex = queue.pop(0)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    result.append(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def __str__(self):
        """返回图的字符串表示"""
        result = []
        for vertex, neighbors in self.graph.items():
            neighbor_str = [f"{neighbor}({weight})" for neighbor, weight in neighbors]
            result.append(f"{vertex}: {', '.join(neighbor_str)}")
        return "\n".join(result)

# 创建无向图示例
graph = GraphAdjacencyList(directed=False)

# 添加边
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('D', 'E')

print("无向图结构:")
print(graph)

print(f"\n所有顶点: {graph.get_vertices()}")
print(f"所有边: {graph.get_edges()}")
print(f"从顶点A开始的DFS: {graph.dfs('A')}")
print(f"从顶点A开始的BFS: {graph.bfs('A')}")

# 5. 哈希表实现

print("\n=== 5. 哈希表实现 ===")

class HashTable:
    """简单的哈希表实现，使用链地址法解决冲突"""
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # 初始化桶
    
    def _hash_function(self, key):
        """简单的哈希函数"""
        # 对于字符串，计算字符的ASCII值之和
        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        # 对于其他类型，使用Python内置的哈希函数
        return hash(key) % self.size
    
    def put(self, key, value):
        """插入或更新键值对"""
        index = self._hash_function(key)
        
        # 检查键是否已存在
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # 更新值
                return
        
        # 键不存在，添加新的键值对
        self.table[index].append((key, value))
    
    def get(self, key):
        """获取键对应的值"""
        index = self._hash_function(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        # 键不存在，返回None
        return None
    
    def remove(self, key):
        """删除键值对"""
        index = self._hash_function(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        
        # 键不存在
        return False
    
    def contains(self, key):
        """检查键是否存在"""
        index = self._hash_function(key)
        
        for k, _ in self.table[index]:
            if k == key:
                return True
        
        return False
    
    def __str__(self):
        """返回哈希表的字符串表示"""
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                bucket_str = [f"{k}:{v}" for k, v in bucket]
                result.append(f"{i}: {', '.join(bucket_str)}")
        return "\n".join(result)

# 哈希表示例
hash_table = HashTable(size=8)

# 添加键值对
hash_table.put("name", "John")
hash_table.put("age", 30)
hash_table.put("city", "New York")
hash_table.put("job", "Developer")
hash_table.put("email", "john@example.com")

print("哈希表内容:")
print(hash_table)

# 获取值
print(f"\nname: {hash_table.get('name')}")
print(f"age: {hash_table.get('age')}")
print(f"country: {hash_table.get('country')}")  # 不存在的键

# 更新值
hash_table.put("age", 31)
print(f"更新后的age: {hash_table.get('age')}")

# 检查键是否存在
print(f"city存在: {hash_table.contains('city')}")
print(f"country存在: {hash_table.contains('country')}")

# 删除键值对
hash_table.remove("job")
print(f"\n删除job后的哈希表:")
print(hash_table)

# 6. 自定义数据结构的应用场景

print("\n=== 6. 自定义数据结构的应用场景 ===")

"""
以下是自定义数据结构的一些典型应用场景：

1. 链表的应用场景：
   - 实现文件系统的目录结构
   - 实现浏览器的历史记录功能（前进/后退）
   - 实现音乐播放器的播放列表
   - 适合需要频繁插入/删除操作但不需要随机访问的场景

2. 栈的应用场景：
   - 表达式求值和括号匹配
   - 函数调用和递归实现
   - 撤销/重做操作
   - 浏览器的历史记录（使用两个栈）

3. 队列的应用场景：
   - 任务调度系统
   - 打印队列
   - 缓冲区管理
   - 广度优先搜索算法

4. 树的应用场景：
   - 数据库索引（B树/B+树）
   - 文件系统目录结构
   - XML/HTML解析（DOM树）
   - 决策树和机器学习算法

5. 图的应用场景：
   - 社交网络分析
   - 地图和路由规划（最短路径）
   - 网络拓扑结构
   - 依赖关系分析

6. 哈希表的应用场景：
   - 缓存系统
   - 数据库索引
   - 查找表
   - 计数器和频率统计
"""

print("6.1 链表应用场景")
print("- 实现文件系统的目录结构")
print("- 实现浏览器的历史记录功能（前进/后退）")
print("- 实现音乐播放器的播放列表")
print("- 适合需要频繁插入/删除操作但不需要随机访问的场景")

print("\n6.2 栈应用场景")
print("- 表达式求值和括号匹配")
print("- 函数调用和递归实现")
print("- 撤销/重做操作")
print("- 浏览器的历史记录（使用两个栈）")

print("\n6.3 队列应用场景")
print("- 任务调度系统")
print("- 打印队列")
print("- 缓冲区管理")
print("- 广度优先搜索算法")

print("\n6.4 树应用场景")
print("- 数据库索引（B树/B+树）")
print("- 文件系统目录结构")
print("- XML/HTML解析（DOM树）")
print("- 决策树和机器学习算法")

print("\n6.5 图应用场景")
print("- 社交网络分析")
print("- 地图和路由规划（最短路径）")
print("- 网络拓扑结构")
print("- 依赖关系分析")

print("\n6.6 哈希表应用场景")
print("- 缓存系统")
print("- 数据库索引")
print("- 查找表")
print("- 计数器和频率统计")

# 7. 综合应用示例：表达式计算器

print("\n=== 7. 综合应用示例：表达式计算器 ===")

class ExpressionCalculator:
    """简易表达式计算器，支持四则运算和括号"""
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    
    def evaluate(self, expression):
        """计算表达式的值"""
        # 使用两个栈：一个存储数字，一个存储操作符
        num_stack = StackLinkedList()
        op_stack = StackLinkedList()
        
        i = 0
        while i < len(expression):
            char = expression[i]
            
            # 跳过空格
            if char == ' ':
                i += 1
                continue
            
            # 如果是数字，解析完整的数字
            elif char.isdigit() or char == '.':
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                num = float(expression[i:j])
                num_stack.push(num)
                i = j
                continue
            
            # 如果是左括号，入栈
            elif char == '(':
                op_stack.push(char)
            
            # 如果是右括号，计算括号内的表达式
            elif char == ')':
                while op_stack and op_stack.peek() != '(':
                    self._apply_operation(num_stack, op_stack.pop())
                op_stack.pop()  # 弹出左括号
            
            # 如果是操作符
            elif char in self.operators:
                # 当栈顶操作符优先级大于等于当前操作符时，先计算栈顶操作
                while (op_stack and op_stack.peek() != '(' and 
                       self.operators[op_stack.peek()] >= self.operators[char]):
                    self._apply_operation(num_stack, op_stack.pop())
                op_stack.push(char)
            
            i += 1
        
        # 处理剩余的操作符
        while op_stack:
            self._apply_operation(num_stack, op_stack.pop())
        
        # 最终结果应该在数字栈的栈顶
        return num_stack.pop()
    
    def _apply_operation(self, num_stack, operator):
        """应用操作符到栈顶的两个数字"""
        if len(num_stack) < 2:
            raise ValueError("无效的表达式")
        
        b = num_stack.pop()
        a = num_stack.pop()
        
        if operator == '+':
            num_stack.push(a + b)
        elif operator == '-':
            num_stack.push(a - b)
        elif operator == '*':
            num_stack.push(a * b)
        elif operator == '/':
            if b == 0:
                raise ValueError("除零错误")
            num_stack.push(a / b)

# 测试表达式计算器
calc = ExpressionCalculator()

# 测试表达式
expressions = [
    "3 + 4",
    "3 + 4 * 2",
    "(3 + 4) * 2",
    "3 * (4 + 2)",
    "10 / 2 + 3",
    "10 / (2 + 3)",
    "3.5 + 2.5 * 2"
]

for expr in expressions:
    try:
        result = calc.evaluate(expr)
        print(f"{expr} = {result}")
    except Exception as e:
        print(f"计算 '{expr}' 时出错: {e}")

# 8. 总结

print("\n=== 8. 自定义数据结构实现总结 ===")

print("1. 选择数据结构的考虑因素：")
print("   - 操作的频率和类型（插入、删除、查找等）")
print("   - 数据的大小和特性")
print("   - 内存使用限制")
print("   - 实现的复杂度")

print("\n2. 自定义实现 vs 使用内置数据结构：")
print("   - Python内置数据结构通常已经过高度优化")
print("   - 在大多数情况下，使用内置数据结构会更高效")
print("   - 自定义数据结构适用于：")
print("     - 学习和理解数据结构的工作原理")
print("     - 需要特定功能或优化的场景")
print("     - 实现Python标准库中没有的数据结构")

print("\n3. 实现自定义数据结构的最佳实践：")
print("   - 确保代码清晰、可读和可维护")
print("   - 添加适当的错误处理和边界条件检查")
print("   - 考虑性能优化，但避免过早优化")
print("   - 编写测试用例验证实现的正确性")
print("   - 考虑使用Python内置数据结构作为底层实现")

print("\n4. 性能考虑：")
print("   - 链表适合频繁的插入和删除操作，但查找性能较差")
print("   - 树结构适合层次化数据和快速查找")
print("   - 图结构适合表示复杂的关系网络")
print("   - 哈希表提供快速的查找、插入和删除操作，但内存占用较大")

"""
本文件详细介绍了如何在Python中实现各种常见的数据结构，包括链表、栈、队列、二叉树、图和哈希表等。

自定义数据结构的实现不仅帮助我们理解这些数据结构的工作原理，还可以根据特定需求进行定制和优化。
在实际应用中，我们应该根据具体场景选择合适的数据结构，并在大多数情况下优先考虑使用Python内置的数据结构，
因为它们通常已经过高度优化，性能更好，而且使用起来更方便。

当内置数据结构无法满足特定需求时，或者我们需要更深入地理解数据结构的实现原理时，
自定义数据结构的知识就显得尤为重要。
"""
