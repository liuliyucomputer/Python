# unicodedata模块 - Unicode字符数据库
# 功能作用：提供Unicode字符的数据库访问功能，支持字符属性查询和名称转换
# 使用情景：文本国际化处理、字符规范化、字符属性查询、特殊字符处理
# 注意事项：处理多语言文本时需要注意Unicode规范化形式的选择

import unicodedata
import re

# 模块概述
"""
unicodedata模块提供了对Unicode字符数据库(UCD)的访问，UCD包含了关于Unicode字符的各种属性信息。
主要功能包括：
- 获取字符的名称、类别、数值等属性
- 执行Unicode规范化（NFC、NFD、NFKC、NFKD）
- 查询字符的分解和组合信息
- 获取字符的双向类别、镜像字符等信息

unicodedata模块在处理国际化文本、多语言支持、文本规范化等场景中非常有用。
"""

# 1. 字符属性查询
print("=== 字符属性查询 ===")

# 获取字符名称
print(f"字符'A'的名称: {unicodedata.name('A')}")
print(f"字符'π'的名称: {unicodedata.name('π')}")
print(f"字符'你'的名称: {unicodedata.name('你')}")
print()

# 获取字符类别
print(f"字符'A'的类别: {unicodedata.category('A')}")  # Lu表示大写字母
print(f"字符'a'的类别: {unicodedata.category('a')}")  # Ll表示小写字母
print(f"字符'1'的类别: {unicodedata.category('1')}")  # Nd表示十进制数字
print(f"字符'!'的类别: {unicodedata.category('!')}")  # Po表示标点符号
print(f"字符' '的类别: {unicodedata.category(' ')}")  # Zs表示空白字符
print(f"字符'你'的类别: {unicodedata.category('你')}")  # Lo表示其他字母
print()

# 类别编码含义：
# L: 字母 (Letter)
#   Lu: 大写字母 (Uppercase letter)
#   Ll: 小写字母 (Lowercase letter)
#   Lt: 首字母大写字母 (Titlecase letter)
#   Lm: 修饰字母 (Modifier letter)
#   Lo: 其他字母 (Other letter)
# M: 标记 (Mark)
# N: 数字 (Number)
#   Nd: 十进制数字 (Decimal digit)
#   Nl: 字母数字 (Letter number)
#   No: 其他数字 (Other number)
# P: 标点符号 (Punctuation)
# S: 符号 (Symbol)
# Z: 分隔符 (Separator)
# C: 其他 (Other)

# 获取字符的十进制数值
print(f"字符'1'的数值: {unicodedata.numeric('1')}")
print(f"字符'九'的数值: {unicodedata.numeric('九')}")
print(f"字符'¾'的数值: {unicodedata.numeric('¾')}")
print(f"字符'Ⅳ'的数值: {unicodedata.numeric('Ⅳ')}")  # 罗马数字4
print()

# 获取字符的十进制数字值
print(f"字符'1'的十进制数字值: {unicodedata.digit('1')}")
print(f"字符'9'的十进制数字值: {unicodedata.digit('9')}")
print(f"字符'₉'的十进制数字值: {unicodedata.digit('₉')}")  # 下标9
print()

# 获取字符的整数值
print(f"字符'1'的整数值: {unicodedata.decimal('1')}")
print(f"字符'5'的整数值: {unicodedata.decimal('5')}")
print()

# 2. 根据名称查找字符
print("=== 根据名称查找字符 ===")

# 使用lookup方法根据名称查找字符
print(f"名称为'GREEK SMALL LETTER PI'的字符: {unicodedata.lookup('GREEK SMALL LETTER PI')}")
print(f"名称为'CHINESE CHARACTER FOR ONE'的字符: {unicodedata.lookup('CHINESE CHARACTER FOR ONE')}")
print(f"名称为'PEACE SYMBOL'的字符: {unicodedata.lookup('PEACE SYMBOL')}")
print(f"名称为'SMILING FACE WITH SMILING EYES'的字符: {unicodedata.lookup('SMILING FACE WITH SMILING EYES')}")
print()

# 3. Unicode规范化
print("=== Unicode规范化 ===")

# Unicode规范化形式:
# NFC: 标准等价合成 (Canonical Composition)
# NFD: 标准等价分解 (Canonical Decomposition)
# NFKC: 兼容等价合成 (Compatibility Composition)
# NFKD: 兼容等价分解 (Compatibility Decomposition)

# 示例：处理带有重音符号的字符
composed = 'é'  # 组合字符 e + ´
decomposed = 'e\u0301'  # 分解形式 e + 组合重音符

print(f"原始组合字符: {repr(composed)} - 长度: {len(composed)}")
print(f"原始分解字符: {repr(decomposed)} - 长度: {len(decomposed)}")
print()

# NFC规范化（合成）
nfc_composed = unicodedata.normalize('NFC', composed)
nfc_decomposed = unicodedata.normalize('NFC', decomposed)
print(f"NFC规范化后的组合字符: {repr(nfc_composed)} - 长度: {len(nfc_composed)}")
print(f"NFC规范化后的分解字符: {repr(nfc_decomposed)} - 长度: {len(nfc_decomposed)}")
print(f"NFC规范化后两者是否相等: {nfc_composed == nfc_decomposed}")
print()

# NFD规范化（分解）
nfd_composed = unicodedata.normalize('NFD', composed)
nfd_decomposed = unicodedata.normalize('NFD', decomposed)
print(f"NFD规范化后的组合字符: {repr(nfd_composed)} - 长度: {len(nfd_composed)}")
print(f"NFD规范化后的分解字符: {repr(nfd_decomposed)} - 长度: {len(nfd_decomposed)}")
print(f"NFD规范化后两者是否相等: {nfd_composed == nfd_decomposed}")
print()

# NFKC规范化（兼容等价合成）
# 示例：处理全角数字
full_width = '１２３'  # 全角数字
normal = '123'  # 半角数字

print(f"全角数字: {repr(full_width)}")
print(f"半角数字: {repr(normal)}")
print(f"原始情况下是否相等: {full_width == normal}")
print()

nfkc_full = unicodedata.normalize('NFKC', full_width)
nfkc_normal = unicodedata.normalize('NFKC', normal)
print(f"NFKC规范化后的全角数字: {repr(nfkc_full)}")
print(f"NFKC规范化后的半角数字: {repr(nfkc_normal)}")
print(f"NFKC规范化后两者是否相等: {nfkc_full == nfkc_normal}")
print()

# NFKD规范化（兼容等价分解）
nfkd_full = unicodedata.normalize('NFKD', full_width)
print(f"NFKD规范化后的全角数字: {repr(nfkd_full)}")
print()

# 4. 字符分解信息
print("=== 字符分解信息 ===")

# 获取字符的分解映射
print(f"字符'é'的分解映射: {repr(unicodedata.decomposition('é'))}")
print(f"字符'ñ'的分解映射: {repr(unicodedata.decomposition('ñ'))}")
print(f"字符'€'的分解映射: {repr(unicodedata.decomposition('€'))}")
print(f"字符'⅓'的分解映射: {repr(unicodedata.decomposition('⅓'))}")
print()

# 5. 其他字符属性
print("=== 其他字符属性 ===")

# 获取字符的双向类别
print(f"字符'A'的双向类别: {unicodedata.bidirectional('A')}")
print(f"字符'\u0644'的双向类别: {unicodedata.bidirectional('\u0644')}")  # 阿拉伯字母lam
print()

# 获取字符的镜像字符
print(f"字符'('的镜像字符: {unicodedata.mirror('(')}")
print(f"字符'A'的镜像字符: {unicodedata.mirror('A')}")  # 非镜像字符返回None
print()

# 检查字符是否有组合标记
print(f"字符'a'是否有组合标记: {unicodedata.combining('a')}")
print(f"字符'\u0301'是否有组合标记: {unicodedata.combining('\u0301')}")  # 组合重音符
print()

# 获取East Asian Width属性
print(f"字符'A'的EAW: {unicodedata.east_asian_width('A')}")  # N: 中性
print(f"字符'你'的EAW: {unicodedata.east_asian_width('你')}")  # W: 宽
print(f"字符'ｱ'的EAW: {unicodedata.east_asian_width('ｱ')}")  # F: 全角
print()

# 6. 实际应用示例
def practical_examples():
    """演示实际应用示例"""
    print("=== 实际应用示例 ===")
    
    # 1. 文本规范化以进行比较
    def normalize_text(text):
        """规范化文本以进行比较"""
        # 使用NFKC规范化，处理各种字符变体
        return unicodedata.normalize('NFKC', text)
    
    # 测试不同形式的相同文本
    text_variants = [
        'café',  # 组合字符
        'cafe\u0301',  # 分解形式
        'CAFÉ',  # 大写形式
        'ｃａｆｅ＇',  # 全角字符
    ]
    
    print("文本规范化示例:")
    for i, text in enumerate(text_variants, 1):
        normalized = normalize_text(text)
        print(f"  变体{i}: {repr(text)} -> 规范化: {repr(normalized)}")
    
    # 规范化后比较
    normalized_variants = [normalize_text(t).lower() for t in text_variants]
    print(f"规范化并转小写后，所有变体是否相等: {all(v == normalized_variants[0] for v in normalized_variants)}")
    print()
    
    # 2. 识别和分类字符
    def categorize_text(text):
        """对文本中的字符进行分类统计"""
        categories = {}
        
        for char in text:
            cat = unicodedata.category(char)
            categories[cat] = categories.get(cat, 0) + 1
        
        return categories
    
    mixed_text = "Hello, 世界! 123 π = 3.14159..."
    categories = categorize_text(mixed_text)
    
    print("字符分类统计:")
    for cat, count in categories.items():
        print(f"  类别 {cat}: {count}个字符")
    print()
    
    # 3. 移除组合重音符号
    def remove_diacritics(text):
        """移除文本中的所有组合重音符号"""
        # 首先进行NFD分解，将组合字符分解为基字符和重音符号
        # 然后过滤掉所有组合标记字符
        # 最后进行NFC重新组合
        nfd_form = unicodedata.normalize('NFD', text)
        no_diacritics = ''.join([char for char in nfd_form if not unicodedata.combining(char)])
        return unicodedata.normalize('NFC', no_diacritics)
    
    accented_text = "Café résumé naïve crème brûlée"
    text_without_diacritics = remove_diacritics(accented_text)
    
    print("移除重音符号示例:")
    print(f"  原始文本: {accented_text}")
    print(f"  处理后: {text_without_diacritics}")
    print()
    
    # 4. 全角和半角字符转换
    def to_half_width(text):
        """将全角字符转换为半角字符"""
        return unicodedata.normalize('NFKC', text)
    
    def is_full_width(char):
        """检查字符是否为全角字符"""
        return unicodedata.east_asian_width(char) in ('F', 'W')
    
    mixed_width_text = "ＡＢＣabc１２３123你好"
    half_width_text = to_half_width(mixed_width_text)
    
    print("全角转半角示例:")
    print(f"  原始文本: {mixed_width_text}")
    print(f"  转换后: {half_width_text}")
    
    # 检查字符宽度
    print("  字符宽度检查:")
    for char in mixed_width_text:
        width_type = "全角" if is_full_width(char) else "半角"
        print(f"    '{char}': {width_type}")
    print()
    
    # 5. 清理特殊字符
    def clean_text(text, keep_categories=None):
        """清理文本中的特殊字符，只保留指定类别的字符"""
        if keep_categories is None:
            # 默认保留字母、数字、标点符号和空白字符
            keep_categories = {'Lu', 'Ll', 'Lt', 'Lm', 'Lo', 'Nd', 'Nl', 'No', 'Pc', 'Pd', 'Ps', 'Pe', 'Pi', 'Pf', 'Po', 'Zs'}
        
        return ''.join([char for char in text if unicodedata.category(char) in keep_categories])
    
    dirty_text = "Hello!@#$%^&*() 世界123\t\n\r测试\u0000\u0001特殊字符"
    cleaned_text = clean_text(dirty_text)
    
    print("文本清理示例:")
    print(f"  原始文本: {repr(dirty_text)}")
    print(f"  清理后: {repr(cleaned_text)}")
    print()
    
    # 6. 构建自定义字符映射
    def build_char_mapping(source_chars, target_chars):
        """构建字符映射字典，考虑Unicode规范化"""
        mapping = {}
        
        for s_char, t_char in zip(source_chars, target_chars):
            # 对源字符和目标字符进行规范化
            s_norm = unicodedata.normalize('NFKC', s_char)
            t_norm = unicodedata.normalize('NFKC', t_char)
            mapping[s_norm] = t_norm
        
        return mapping
    
    def apply_mapping(text, mapping):
        """应用字符映射"""
        result = []
        for char in text:
            norm_char = unicodedata.normalize('NFKC', char)
            result.append(mapping.get(norm_char, char))
        return ''.join(result)
    
    # 创建一个简单的映射示例
    source = "abcABC"
    target = "123456"
    char_map = build_char_mapping(source, target)
    
    test_text = "abcABC，aBc"
    mapped_text = apply_mapping(test_text, char_map)
    
    print("字符映射示例:")
    print(f"  映射表: {char_map}")
    print(f"  原始文本: {test_text}")
    print(f"  映射后: {mapped_text}")
    print()
    
    # 7. 计算文本的实际显示宽度
    def get_display_width(text):
        """计算文本的实际显示宽度（考虑全角字符）"""
        width = 0
        for char in text:
            eaw = unicodedata.east_asian_width(char)
            # 全角字符宽度为2，其他为1
            width += 2 if eaw in ('F', 'W') else 1
        return width
    
    # 测试显示宽度
    width_test_cases = [
        "Hello World",
        "你好，世界",
        "Hello 世界",
        "ＡＢＣabc",
    ]
    
    print("文本显示宽度计算:")
    for text in width_test_cases:
        width = get_display_width(text)
        print(f"  '{text}': 显示宽度 = {width}")
    print()
    
    # 8. 生成Unicode字符表
    def generate_unicode_table(start_code, end_code, categories=None):
        """生成Unicode字符表"""
        results = []
        for code in range(start_code, end_code + 1):
            char = chr(code)
            # 过滤类别
            if categories and unicodedata.category(char) not in categories:
                continue
            
            try:
                name = unicodedata.name(char)
                category = unicodedata.category(char)
                results.append((char, code, name, category))
            except ValueError:
                # 有些字符可能没有名称
                pass
        return results
    
    # 生成一些希腊字母
    greek_letters = generate_unicode_table(0x03B1, 0x03C9)  # 小写希腊字母
    
    print("希腊字母Unicode表（部分）:")
    for char, code, name, category in greek_letters[:10]:  # 只显示前10个
        print(f"  {char} (U+{code:04X}) - {name} [{category}]")
    print()
    
    # 9. 检查字符是否为数字
    def is_number(char):
        """检查字符是否为数字（包括各种Unicode数字）"""
        try:
            # 尝试获取字符的数值
            return unicodedata.numeric(char) is not None
        except (TypeError, ValueError):
            return False
    
    # 测试各种数字字符
    number_test_cases = "12345 ½ ¾ ⅓ ⅔ ⅛ ① ② 三 四 伍 拾"
    
    print("数字字符检查:")
    for char in number_test_cases:
        if char.strip():
            is_num = is_number(char)
            numeric_value = unicodedata.numeric(char) if is_num else "N/A"
            print(f"  '{char}': 是数字 = {is_num}, 数值 = {numeric_value}")
    print()
    
    # 10. 规范化文件路径（处理不同形式的字符）
    def normalize_path(path):
        """规范化文件路径中的字符"""
        # 使用NFKC规范化，确保全角字符转为半角
        return unicodedata.normalize('NFKC', path)
    
    paths = [
        "C:\\Users\\User\\Documents\\工作",
        "C：\\Ｕｓｅｒｓ\\Ｕｓｅｒ\\Ｄｏｃｕｍｅｎｔｓ\\工作"
    ]
    
    print("文件路径规范化:")
    for path in paths:
        normalized = normalize_path(path)
        print(f"  原始路径: {path}")
        print(f"  规范化后: {normalized}")
    print()

# 7. 高级用法和技巧
print("=== 高级用法和技巧 ===")

# 1. 自定义字符过滤器
class UnicodeCharFilter:
    """Unicode字符过滤器"""
    
    def __init__(self, allowed_categories=None):
        self.allowed_categories = allowed_categories or {'Lu', 'Ll', 'Nd', 'Zs'}
    
    def filter(self, text):
        """过滤文本，只保留允许的字符类别"""
        return ''.join([char for char in text if unicodedata.category(char) in self.allowed_categories])
    
    def add_category(self, category):
        """添加允许的字符类别"""
        self.allowed_categories.add(category)
    
    def remove_category(self, category):
        """移除允许的字符类别"""
        if category in self.allowed_categories:
            self.allowed_categories.remove(category)

# 使用自定义过滤器
filter = UnicodeCharFilter()
filtered_text = filter.filter("Hello, 世界! 123")
print(f"默认过滤器（字母、数字、空白）: {filtered_text}")

filter.add_category('Po')  # 添加标点符号类别
filtered_text_with_punct = filter.filter("Hello, 世界! 123")
print(f"添加标点符号后: {filtered_text_with_punct}")
print()

# 2. 文本相似度比较（基于规范化）
def text_similarity(text1, text2):
    """计算两个文本的相似度（简单实现）"""
    # 规范化两个文本
    norm1 = unicodedata.normalize('NFKC', text1).lower()
    norm2 = unicodedata.normalize('NFKC', text2).lower()
    
    # 计算最长公共子序列长度
    def lcs_length(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    lcs = lcs_length(norm1, norm2)
    max_len = max(len(norm1), len(norm2))
    
    # 返回相似度（0-1之间）
    return lcs / max_len if max_len > 0 else 1.0

# 测试文本相似度
text1 = "Café au lait"
text2 = "caféaulait"
text3 = "cafe au lait"
text4 = "coffee with milk"

sim12 = text_similarity(text1, text2)
sim13 = text_similarity(text1, text3)
sim14 = text_similarity(text1, text4)

print("文本相似度比较:")
print(f"'{text1}' 与 '{text2}' 的相似度: {sim12:.4f}")
print(f"'{text1}' 与 '{text3}' 的相似度: {sim13:.4f}")
print(f"'{text1}' 与 '{text4}' 的相似度: {sim14:.4f}")
print()

# 3. Unicode文本分词器（简单实现）
def unicode_tokenizer(text):
    """简单的Unicode文本分词器"""
    tokens = []
    current_token = ""
    current_category = None
    
    for char in text:
        cat = unicodedata.category(char)
        # 基本分类：字母、数字、其他
        if cat.startswith('L'):
            new_category = 'letter'
        elif cat.startswith('N'):
            new_category = 'number'
        else:
            new_category = 'other'
        
        if new_category == current_category or current_token == "":
            # 相同类别，继续添加
            current_token += char
            current_category = new_category
        else:
            # 不同类别，保存当前token
            if current_token and current_category != 'other':
                tokens.append(current_token)
            current_token = char if new_category != 'other' else ""
            current_category = new_category
    
    # 添加最后一个token
    if current_token and current_category != 'other':
        tokens.append(current_token)
    
    return tokens

# 测试分词器
mixed_text = "Hello, 世界! 123-test_文本."
tokens = unicode_tokenizer(mixed_text)
print(f"分词结果: {tokens}")
print()

# 4. 字符属性缓存（提高性能）
class UnicodePropertyCache:
    """Unicode字符属性缓存"""
    
    def __init__(self):
        self.category_cache = {}
        self.name_cache = {}
        self.numeric_cache = {}
    
    def get_category(self, char):
        """获取字符类别（带缓存）"""
        if char not in self.category_cache:
            self.category_cache[char] = unicodedata.category(char)
        return self.category_cache[char]
    
    def get_name(self, char):
        """获取字符名称（带缓存）"""
        if char not in self.name_cache:
            try:
                self.name_cache[char] = unicodedata.name(char)
            except ValueError:
                self.name_cache[char] = None
        return self.name_cache[char]
    
    def get_numeric(self, char):
        """获取字符数值（带缓存）"""
        if char not in self.numeric_cache:
            try:
                self.numeric_cache[char] = unicodedata.numeric(char)
            except (TypeError, ValueError):
                self.numeric_cache[char] = None
        return self.numeric_cache[char]
    
    def clear_cache(self):
        """清空缓存"""
        self.category_cache.clear()
        self.name_cache.clear()
        self.numeric_cache.clear()

# 使用属性缓存
cache = UnicodePropertyCache()

# 测试缓存性能
import time

def test_without_cache(text):
    """不使用缓存测试"""
    start = time.time()
    for _ in range(1000):
        for char in text:
            unicodedata.category(char)
    return time.time() - start

def test_with_cache(text, cache):
    """使用缓存测试"""
    start = time.time()
    for _ in range(1000):
        for char in text:
            cache.get_category(char)
    return time.time() - start

# 创建测试文本
import string
test_text = string.ascii_letters + string.digits + "你好，世界！" * 10

time_without = test_without_cache(test_text)
time_with = test_with_cache(test_text, cache)

print("性能测试（获取字符类别）:")
print(f"不使用缓存: {time_without:.6f}秒")
print(f"使用缓存: {time_with:.6f}秒")
print(f"性能提升: {(time_without/time_with):.2f}倍")
print()

# 8. 注意事项和最佳实践
"""
1. **规范化选择**：
   - NFC：用于一般文本存储和显示，保留组合字符
   - NFD：用于文本处理，分解字符便于操作单个标记
   - NFKC：用于搜索、索引和比较，处理兼容字符
   - NFKD：用于需要完全分解的场景

2. **性能考虑**：
   - 频繁调用unicodedata函数可能影响性能，考虑使用缓存
   - 对于大量文本处理，可以批量规范化

3. **字符串比较**：
   - 在比较字符串时，始终先进行规范化处理
   - 不同形式的相同文本（如带重音符号的变体）需要规范化后再比较

4. **文本清洗**：
   - 使用字符类别进行有针对性的文本清洗
   - 注意保留需要的特殊字符

5. **国际化支持**：
   - 考虑不同语言的字符特性
   - 注意右到左语言的双向文本处理

6. **显示宽度**：
   - 在需要精确计算文本显示宽度时，考虑使用east_asian_width
   - 全角字符通常占用两倍宽度

7. **错误处理**：
   - 某些字符可能没有名称或数值，需要捕获ValueError异常
   - 使用try/except块处理可能的异常

8. **版本兼容性**：
   - Unicode标准在不断更新，不同Python版本支持的Unicode版本可能不同
   - 对于特定字符或属性，需要考虑版本兼容性
"""

def demonstrate_best_practices():
    """演示最佳实践"""
    print("=== 最佳实践示例 ===")
    
    # 1. 正确的字符串比较
    print("正确的字符串比较:")
    
    # 两个看起来相同但内部表示不同的字符串
    str1 = "café"  # é作为单个字符
    str2 = "cafe\u0301"  # e后跟组合重音符
    
    print(f"字符串1: {repr(str1)}, 长度: {len(str1)}")
    print(f"字符串2: {repr(str2)}, 长度: {len(str2)}")
    print(f"直接比较结果: {str1 == str2}")  # False
    
    # 规范化后比较
    norm1 = unicodedata.normalize('NFC', str1)
    norm2 = unicodedata.normalize('NFC', str2)
    print(f"NFC规范化后比较: {norm1 == norm2}")  # True
    print()
    
    # 2. 处理文件系统路径时的规范化
    print("文件系统路径规范化:")
    
    def safe_path_compare(path1, path2):
        """安全比较文件路径"""
        # 使用NFKC规范化，处理全角字符等
        norm_path1 = unicodedata.normalize('NFKC', path1)
        norm_path2 = unicodedata.normalize('NFKC', path2)
        # 转换为小写进行大小写不敏感的比较
        return norm_path1.lower() == norm_path2.lower()
    
    path1 = "C:\\Users\\user\\文档"
    path2 = "c：\\ｕｓｅｒｓ\\ＵＳＥＲ\\文档"
    
    print(f"路径1: {path1}")
    print(f"路径2: {path2}")
    print(f"直接比较: {path1 == path2}")  # False
    print(f"安全比较: {safe_path_compare(path1, path2)}")  # True
    print()
    
    # 3. 文本搜索时的规范化
    print("文本搜索时的规范化:")
    
    def normalize_for_search(text):
        """为搜索准备文本"""
        # 使用NFKC规范化，处理各种兼容字符
        # 转换为小写
        # 移除组合重音符号
        text = unicodedata.normalize('NFKD', text)
        text = text.lower()
        text = ''.join([c for c in text if not unicodedata.combining(c)])
        return unicodedata.normalize('NFC', text)
    
    def search_text(text, query):
        """搜索文本，考虑Unicode变体"""
        norm_text = normalize_for_search(text)
        norm_query = normalize_for_search(query)
        return norm_query in norm_text
    
    document = "Café résumé et Crème Brûlée sont des mots français."
    queries = ["cafe", "CAFE", "café", "RESUME", "brûlée"]
    
    print(f"文档: {document}")
    print("搜索结果:")
    for q in queries:
        found = search_text(document, q)
        print(f"  '{q}': {'找到' if found else '未找到'}")
    print()
    
    # 4. 安全的字符属性访问
    print("安全的字符属性访问:")
    
    def safe_get_name(char):
        """安全获取字符名称"""
        try:
            return unicodedata.name(char)
        except ValueError:
            return f"<无名称字符: U+{ord(char):04X}>"
    
    def safe_get_numeric(char):
        """安全获取字符数值"""
        try:
            return unicodedata.numeric(char)
        except (TypeError, ValueError):
            return None
    
    # 测试一些特殊字符
    test_chars = ["A", "π", "你", "\u0000", "\u001F", "🤔"]
    
    print("字符属性安全访问:")
    for char in test_chars:
        name = safe_get_name(char)
        numeric = safe_get_numeric(char)
        print(f"  '{char}' (U+{ord(char):04X}): 名称 = {name}, 数值 = {numeric}")
    print()
    
    # 5. 处理双向文本
    print("处理双向文本:")
    
    def analyze_bidi_text(text):
        """分析双向文本"""
        result = []
        for char in text:
            bidi = unicodedata.bidirectional(char)
            result.append((char, bidi))
        return result
    
    # 包含阿拉伯文和英文的混合文本
    bidi_text = "Hello مرحبا World عالم"
    bidi_analysis = analyze_bidi_text(bidi_text)
    
    print(f"双向文本分析: '{bidi_text}'")
    print("字符双向类别:")
    for char, bidi in bidi_analysis:
        print(f"  '{char}': {bidi}")
    print()
    
    # 6. 清理用户输入
    print("清理用户输入:")
    
    def sanitize_input(text):
        """清理用户输入文本"""
        # 1. 规范化文本
        text = unicodedata.normalize('NFKC', text)
        
        # 2. 移除控制字符（保留换行符和制表符）
        sanitized = []
        for char in text:
            cat = unicodedata.category(char)
            # 移除控制字符（C类），但保留换行和制表符
            if cat.startswith('C') and ord(char) not in (9, 10, 13):
                continue
            sanitized.append(char)
        
        return ''.join(sanitized)
    
    # 包含控制字符和全角字符的输入
    dirty_input = "User\u0007Input\t包含\u0001控制字符和全角ABC"
    clean_input = sanitize_input(dirty_input)
    
    print(f"原始输入: {repr(dirty_input)}")
    print(f"清理后: {repr(clean_input)}")
    print()

# 运行演示代码
if __name__ == "__main__":
    print("Python unicodedata模块演示\n")
    
    # 运行基本演示
    # 实际应用示例
    practical_examples()
    # 高级用法和最佳实践
    demonstrate_best_practices()
    
    print("演示完成！")