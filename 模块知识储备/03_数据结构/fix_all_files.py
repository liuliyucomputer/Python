import os
import re

# 简单的修复函数，专注于修复未闭合的代码块
def fix_file(file_path):
    print(f"正在处理: {file_path}")
    
    # 读取文件内容
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"读取文件失败: {e}")
        return False
    
    # 修复代码块问题 - 确保每个```python后面都有闭合的```
    # 使用更简单的方法统计开闭标记数量
    open_markers = content.count('```python')
    close_markers = content.count('```') - open_markers  # 减去开始标记的数量
    
    # 如果缺少闭合标记，添加它们
    if open_markers > close_markers:
        missing = open_markers - close_markers
        content += '```\n' * missing
        print(f"  添加了 {missing} 个闭合标记")
    
    # 对于heapq模块，单独处理
    if "heapq模块.py" in file_path:
        if "使用注意事项" not in content:
            # 读取文件最后部分来确定添加位置
            lines = content.split('\n')
            # 找到"总结与最佳实践"章节的位置
            summary_index = -1
            for i, line in enumerate(lines):
                if re.match(r'## \d+\. 总结与最佳实践', line):
                    summary_index = i
                    break
            
            # 添加使用注意事项章节
            if summary_index != -1:
                # 创建使用注意事项内容
                use_notes_lines = [
                    '## 5. 使用注意事项',
                    '',
                    '在使用 `heapq` 模块时，有几个重要的注意事项需要牢记，以避免常见的陷阱和性能问题。',
                    '',
                    '### 5.1 堆的特性与限制',
                    '',
                    '- **最小堆性质**：Python的`heapq`默认实现的是最小堆，这意味着堆顶元素始终是最小的。如果需要最大堆，可以通过取负数或使用自定义比较器来实现。',
                    '- **零索引**：与许多堆实现不同，Python的堆使用的是零索引，这意味着对于位置`i`的元素，其左子节点位于`2*i+1`，右子节点位于`2*i+2`。',
                    '- **非完全排序**：堆只保证堆顶元素是最小的，并不保证整个列表是有序的。如果需要有序序列，需要依次弹出元素。',
                    '',
                    '### 5.2 性能考虑',
                    '',
                    '- **初始化开销**：使用`heapify()`将现有列表转换为堆的时间复杂度是O(n)，而逐个插入元素的时间复杂度是O(n log n)，因此在处理已有数据时，`heapify()`通常更高效。',
                    '- **内存占用**：堆操作是在原列表上进行的，不会创建新的数据结构，因此内存效率较高。',
                    '- **大堆处理**：对于非常大的堆，需要注意内存使用和缓存效率问题。在处理大数据集时，考虑使用外部排序或流式处理。',
                    '',
                    '### 5.3 线程安全',
                    '',
                    '- `heapq`模块本身不是线程安全的。在多线程环境中，如果多个线程同时访问同一个堆，需要使用锁机制来确保线程安全。',
                    '- 可以参考前面提到的`ThreadSafePriorityQueue`类，它提供了线程安全的优先队列实现。',
                    '',
                    '### 5.4 数据一致性',
                    '',
                    '- **自定义对象**：当使用自定义对象作为堆元素时，必须确保这些对象实现了适当的比较方法（如`__lt__`），否则可能导致意外的行为或`TypeError`异常。',
                    '- **不可变数据**：为了避免意外修改堆元素的值导致堆属性被破坏，最好使用不可变数据类型或将自定义对象的关键属性设计为只读。',
                    '',
                    '### 5.5 实用建议',
                    '',
                    '- **避免直接访问**：不要直接通过索引访问或修改堆中的元素（除了堆顶元素），这可能会破坏堆的性质。',
                    '- **有序序列合并**：在使用`merge()`函数时，确保输入的序列已经排序，否则结果可能不符合预期。',
                    '- **优先级表示**：对于需要复杂优先级逻辑的场景，考虑使用元组(优先级, 计数器, 值)的形式来避免元素不可比较的问题。',
                    '',
                    '## 6. 总结与最佳实践'
                ]
                
                # 替换原章节
                lines[summary_index] = '\n'.join(use_notes_lines)
                content = '\n'.join(lines)
                print("  添加了使用注意事项章节")
    
    # 保存修复后的文件
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {file_path} 修复完成")
        return True
    except Exception as e:
        print(f"保存文件失败: {e}")
        return False

# 修复所有模块文件
def fix_all_modules():
    modules = [
        "itertools模块.py",
        "operator模块.py",
        "collections模块.py",
        "heapq模块.py",
        "functools模块.py"
    ]
    
    success_count = 0
    for module in modules:
        file_path = os.path.join(os.getcwd(), module)
        if os.path.exists(file_path):
            if fix_file(file_path):
                success_count += 1
        else:
            print(f"❌ 文件不存在: {file_path}")
    
    print(f"\n修复完成！成功修复: {success_count}/{len(modules)}")

if __name__ == "__main__":
    fix_all_modules()