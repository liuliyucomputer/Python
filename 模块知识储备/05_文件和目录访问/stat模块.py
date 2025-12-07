# Python stat模块详解

import stat
import os
import time
import datetime

# 1. 模块概述
print("=== 1. stat模块概述 ===")
print("stat模块提供了获取和解释文件状态信息的功能，是文件系统操作的重要工具。")
print("该模块的主要特点：")
print("- 获取文件状态信息（大小、权限、修改时间等）")
print("- 解释文件模式（权限、类型）")
print("- 提供文件类型和权限的常量定义")
print("- 支持跨平台的文件状态信息获取")
print("- 与os模块紧密集成，提供更详细的文件信息")
print()

# 2. 文件状态信息
print("=== 2. 文件状态信息 ===")

# 创建一个测试文件和目录
test_dir = "test_stat_dir"
test_file = os.path.join(test_dir, "test_file.txt")

os.makedirs(test_dir, exist_ok=True)
with open(test_file, "w") as f:
    f.write("测试文件内容\n")

print("2.1 获取文件状态：")
# 使用os.stat()获取文件状态信息
file_stat = os.stat(test_file)
dir_stat = os.stat(test_dir)

print(f"  文件状态对象: {file_stat}")
print(f"  目录状态对象: {dir_stat}")
print()

print("2.2 文件状态属性：")
print("   文件状态对象包含以下主要属性：")
print(f"   - st_mode: 文件模式（权限和类型）: {file_stat.st_mode}")
print(f"   - st_ino: inode号: {file_stat.st_ino}")
print(f"   - st_dev: 设备号: {file_stat.st_dev}")
print(f"   - st_nlink: 硬链接数: {file_stat.st_nlink}")
print(f"   - st_uid: 用户ID: {file_stat.st_uid}")
print(f"   - st_gid: 组ID: {file_stat.st_gid}")
print(f"   - st_size: 文件大小（字节）: {file_stat.st_size}")
print(f"   - st_atime: 最后访问时间: {file_stat.st_atime} ({datetime.datetime.fromtimestamp(file_stat.st_atime)})")
print(f"   - st_mtime: 最后修改时间: {file_stat.st_mtime} ({datetime.datetime.fromtimestamp(file_stat.st_mtime)})")
print(f"   - st_ctime: 最后状态更改时间: {file_stat.st_ctime} ({datetime.datetime.fromtimestamp(file_stat.st_ctime)})")

print()

# 3. 文件模式解释
print("=== 3. 文件模式解释 ===")

print("3.1 文件类型：")
print("   stat模块提供了以下文件类型常量：")
print(f"   - stat.S_IFREG: 普通文件: {stat.S_IFREG}")
print(f"   - stat.S_IFDIR: 目录: {stat.S_IFDIR}")
print(f"   - stat.S_IFLNK: 符号链接: {stat.S_IFLNK}")
print(f"   - stat.S_IFCHR: 字符设备: {stat.S_IFCHR}")
print(f"   - stat.S_IFBLK: 块设备: {stat.S_IFBLK}")
print(f"   - stat.S_IFIFO: FIFO: {stat.S_IFIFO}")
print(f"   - stat.S_IFSOCK: 套接字: {stat.S_IFSOCK}")

print()

print("3.2 判断文件类型：")
# 使用stat.S_IS*函数判断文件类型
print(f"  文件 '{test_file}' 的类型：")
print(f"    - 普通文件: {stat.S_ISREG(file_stat.st_mode)}")
print(f"    - 目录: {stat.S_ISDIR(file_stat.st_mode)}")
print(f"    - 符号链接: {stat.S_ISLNK(file_stat.st_mode)}")
print(f"    - 字符设备: {stat.S_ISCHR(file_stat.st_mode)}")
print(f"    - 块设备: {stat.S_ISBLK(file_stat.st_mode)}")
print(f"    - FIFO: {stat.S_ISFIFO(file_stat.st_mode)}")
print(f"    - 套接字: {stat.S_ISSOCK(file_stat.st_mode)}")

print(f"  目录 '{test_dir}' 的类型：")
print(f"    - 普通文件: {stat.S_ISREG(dir_stat.st_mode)}")
print(f"    - 目录: {stat.S_ISDIR(dir_stat.st_mode)}")

print()

print("3.3 文件权限：")
print("   stat模块提供了以下权限常量：")
print("   所有者权限：")
print(f"   - stat.S_IRUSR: 读权限: {stat.S_IRUSR}")
print(f"   - stat.S_IWUSR: 写权限: {stat.S_IWUSR}")
print(f"   - stat.S_IXUSR: 执行权限: {stat.S_IXUSR}")
print(f"   - stat.S_IRWXU: 所有权限: {stat.S_IRWXU}")

print("   组权限：")
print(f"   - stat.S_IRGRP: 读权限: {stat.S_IRGRP}")
print(f"   - stat.S_IWGRP: 写权限: {stat.S_IWGRP}")
print(f"   - stat.S_IXGRP: 执行权限: {stat.S_IXGRP}")
print(f"   - stat.S_IRWXG: 所有权限: {stat.S_IRWXG}")

print("   其他用户权限：")
print(f"   - stat.S_IROTH: 读权限: {stat.S_IROTH}")
print(f"   - stat.S_IWOTH: 写权限: {stat.S_IWOTH}")
print(f"   - stat.S_IXOTH: 执行权限: {stat.S_IXOTH}")
print(f"   - stat.S_IRWXO: 所有权限: {stat.S_IRWXO}")

print("   特殊权限：")
print(f"   - stat.S_ISUID: 设置用户ID位: {stat.S_ISUID}")
print(f"   - stat.S_ISGID: 设置组ID位: {stat.S_ISGID}")
print(f"   - stat.S_ISVTX: 粘滞位: {stat.S_ISVTX}")

print()

print("3.4 解释文件权限：")
# 使用位运算判断文件权限
def get_file_permissions(mode):
    """获取文件权限字符串"""
    # 所有者权限
    user_r = 'r' if mode & stat.S_IRUSR else '-'
    user_w = 'w' if mode & stat.S_IWUSR else '-'
    user_x = 'x' if mode & stat.S_IXUSR else '-'
    
    # 组权限
    group_r = 'r' if mode & stat.S_IRGRP else '-'
    group_w = 'w' if mode & stat.S_IWGRP else '-'
    group_x = 'x' if mode & stat.S_IXGRP else '-'
    
    # 其他用户权限
    other_r = 'r' if mode & stat.S_IROTH else '-'
    other_w = 'w' if mode & stat.S_IWOTH else '-'
    other_x = 'x' if mode & stat.S_IXOTH else '-'
    
    return f"{user_r}{user_w}{user_x}{group_r}{group_w}{group_x}{other_r}{other_w}{other_x}"

file_perm = get_file_permissions(file_stat.st_mode)
dir_perm = get_file_permissions(dir_stat.st_mode)

print(f"  文件 '{test_file}' 的权限: {file_perm}")
print(f"  目录 '{test_dir}' 的权限: {dir_perm}")

print()

# 4. 实用函数
print("=== 4. 实用函数 ===")

print("4.1 stat.filemode()：")
print("   将文件模式转换为可读的字符串表示")
print(f"   文件 '{test_file}' 的模式字符串: {stat.filemode(file_stat.st_mode)}")
print(f"   目录 '{test_dir}' 的模式字符串: {stat.filemode(dir_stat.st_mode)}")

print()

print("4.2 os.stat() vs os.lstat()：")
print("   - os.stat(): 跟随符号链接获取目标文件的状态")
print("   - os.lstat(): 获取符号链接本身的状态")

# 创建一个符号链接示例
if os.name != 'nt':  # Windows下需要管理员权限，跳过
    try:
        link_path = os.path.join(test_dir, "link_to_file.txt")
        os.symlink(test_file, link_path)
        
        # 使用os.stat()获取符号链接指向的文件状态
        link_stat = os.stat(link_path)
        # 使用os.lstat()获取符号链接本身的状态
        link_lstat = os.lstat(link_path)
        
        print(f"   符号链接 '{link_path}' 的状态：")
        print(f"     - os.stat() (跟随链接): {stat.filemode(link_stat.st_mode)}")
        print(f"     - os.lstat() (链接本身): {stat.filemode(link_lstat.st_mode)}")
        print(f"     - 是符号链接: {stat.S_ISLNK(link_lstat.st_mode)}")
        
        # 删除符号链接
        os.unlink(link_path)
    except Exception as e:
        print(f"   创建符号链接时出错: {e}")

print()

print("4.3 文件时间信息：")
print("   文件状态中的时间戳可以通过time模块转换为可读格式")

file_time_info = {
    "访问时间 (atime)": file_stat.st_atime,
    "修改时间 (mtime)": file_stat.st_mtime,
    "状态更改时间 (ctime)": file_stat.st_ctime
}

for time_name, timestamp in file_time_info.items():
    print(f"   - {time_name}: {timestamp}")
    print(f"     - time.ctime(): {time.ctime(timestamp)}")
    print(f"     - datetime: {datetime.datetime.fromtimestamp(timestamp)}")
    print(f"     - ISO格式: {datetime.datetime.fromtimestamp(timestamp).isoformat()}")

print()

# 5. 实际应用示例
print("=== 5. 实际应用示例 ===")

print("5.1 获取文件详细信息：")
def get_file_details(file_path):
    """获取文件的详细信息"""
    try:
        file_stat = os.stat(file_path)
        
        details = {
            "路径": file_path,
            "名称": os.path.basename(file_path),
            "类型": "目录" if stat.S_ISDIR(file_stat.st_mode) else "文件",
            "大小": file_stat.st_size,  # 字节
            "权限": stat.filemode(file_stat.st_mode),
            "所有者ID": file_stat.st_uid,
            "组ID": file_stat.st_gid,
            "修改时间": datetime.datetime.fromtimestamp(file_stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
            "访问时间": datetime.datetime.fromtimestamp(file_stat.st_atime).strftime("%Y-%m-%d %H:%M:%S"),
            "状态更改时间": datetime.datetime.fromtimestamp(file_stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return details
    except Exception as e:
        print(f"   错误: {e}")
        return None

# 获取测试文件和目录的详细信息
file_details = get_file_details(test_file)
dir_details = get_file_details(test_dir)

print(f"  文件详细信息：")
if file_details:
    for key, value in file_details.items():
        print(f"    {key}: {value}")

print()

print(f"  目录详细信息：")
if dir_details:
    for key, value in dir_details.items():
        print(f"    {key}: {value}")

print()

print("5.2 递归计算目录大小：")
def get_directory_size(dir_path):
    """递归计算目录大小"""
    total_size = 0
    
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_stat = os.stat(file_path)
                total_size += file_stat.st_size
            except Exception as e:
                print(f"   无法获取文件大小: {file_path} - {e}")
    
    return total_size

# 计算测试目录的大小
dir_size = get_directory_size(test_dir)
print(f"  目录 '{test_dir}' 的大小: {dir_size} 字节")
print(f"  目录 '{test_dir}' 的大小: {round(dir_size / 1024, 2)} KB")

print()

print("5.3 查找最近修改的文件：")
def find_recently_modified_files(directory, days=1, max_files=10):
    """查找最近修改的文件"""
    cutoff_time = time.time() - (days * 24 * 60 * 60)
    recent_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_stat = os.stat(file_path)
                if file_stat.st_mtime > cutoff_time:
                    recent_files.append((file_path, file_stat.st_mtime))
            except Exception as e:
                print(f"   无法获取文件信息: {file_path} - {e}")
    
    # 按修改时间排序（最新的在前）
    recent_files.sort(key=lambda x: x[1], reverse=True)
    
    # 返回前max_files个文件
    return recent_files[:max_files]

# 查找最近修改的文件
recent_files = find_recently_modified_files(".", days=7, max_files=5)

print(f"  最近7天修改的文件：")
for file_path, mtime in recent_files:
    mtime_str = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
    print(f"    {mtime_str}: {file_path}")

print()

print("5.4 检查文件权限：")
def check_file_permissions(file_path, check_perm):
    """检查文件是否具有指定的权限"""
    try:
        file_stat = os.stat(file_path)
        return (file_stat.st_mode & check_perm) != 0
    except Exception as e:
        print(f"   错误: {e}")
        return False

# 检查文件权限
file_path = test_file
print(f"  文件 '{file_path}' 的权限检查：")
print(f"    - 所有者可读: {check_file_permissions(file_path, stat.S_IRUSR)}")
print(f"    - 所有者可写: {check_file_permissions(file_path, stat.S_IWUSR)}")
print(f"    - 所有者可执行: {check_file_permissions(file_path, stat.S_IXUSR)}")
print(f"    - 组可读: {check_file_permissions(file_path, stat.S_IRGRP)}")
print(f"    - 其他用户可写: {check_file_permissions(file_path, stat.S_IWOTH)}")

print()

print("5.5 批量修改文件权限：")
def batch_change_permissions(directory, pattern, new_perm, recursive=False):
    """批量修改文件权限"""
    import fnmatch
    
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                file_path = os.path.join(root, file)
                try:
                    # 获取当前权限
                    current_stat = os.stat(file_path)
                    current_perm = current_stat.st_mode & 0o777  # 只保留权限部分
                    
                    # 应用新权限
                    new_mode = (current_stat.st_mode & ~0o777) | new_perm
                    os.chmod(file_path, new_mode)
                    
                    count += 1
                    print(f"    修改文件 '{file_path}' 的权限: {oct(current_perm)} -> {oct(new_perm)}")
                except Exception as e:
                    print(f"    错误: {file_path} - {e}")
        
        if not recursive:
            break
    
    print(f"  共修改 {count} 个文件的权限")

# 创建一些测试文件用于批量修改权限
batch_test_dir = os.path.join(test_dir, "batch_test")
os.makedirs(batch_test_dir, exist_ok=True)

for i in range(3):
    batch_test_file = os.path.join(batch_test_dir, f"test_file_{i}.txt")
    with open(batch_test_file, "w") as f:
        f.write(f"测试文件 {i}\n")

# 批量修改文件权限
print(f"  批量修改文件权限：")
batch_change_permissions(batch_test_dir, "*.txt", 0o644, recursive=True)

print()

# 6. 高级技巧
print("=== 6. 高级技巧 ===")

print("6.1 使用stat模块常量创建文件模式：")
# 创建一个文件模式（普通文件，所有者读写，组读，其他读）
file_mode = stat.S_IFREG | stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH
print(f"  创建的文件模式: {oct(file_mode)}")
print(f"  文件模式字符串: {stat.filemode(file_mode)}")

print()

print("6.2 解析文件模式：")
def parse_file_mode(mode):
    """解析文件模式并返回详细信息"""
    details = {
        "文件类型": "",
        "所有者权限": "",
        "组权限": "",
        "其他用户权限": "",
        "特殊权限": ""
    }
    
    # 确定文件类型
    if stat.S_ISREG(mode):
        details["文件类型"] = "普通文件"
    elif stat.S_ISDIR(mode):
        details["文件类型"] = "目录"
    elif stat.S_ISLNK(mode):
        details["文件类型"] = "符号链接"
    elif stat.S_ISCHR(mode):
        details["文件类型"] = "字符设备"
    elif stat.S_ISBLK(mode):
        details["文件类型"] = "块设备"
    elif stat.S_ISFIFO(mode):
        details["文件类型"] = "FIFO"
    elif stat.S_ISSOCK(mode):
        details["文件类型"] = "套接字"
    
    # 确定所有者权限
    owner_perm = []
    if mode & stat.S_IRUSR:
        owner_perm.append("读")
    if mode & stat.S_IWUSR:
        owner_perm.append("写")
    if mode & stat.S_IXUSR:
        owner_perm.append("执行")
    details["所有者权限"] = ", ".join(owner_perm) if owner_perm else "无"
    
    # 确定组权限
    group_perm = []
    if mode & stat.S_IRGRP:
        group_perm.append("读")
    if mode & stat.S_IWGRP:
        group_perm.append("写")
    if mode & stat.S_IXGRP:
        group_perm.append("执行")
    details["组权限"] = ", ".join(group_perm) if group_perm else "无"
    
    # 确定其他用户权限
    other_perm = []
    if mode & stat.S_IROTH:
        other_perm.append("读")
    if mode & stat.S_IWOTH:
        other_perm.append("写")
    if mode & stat.S_IXOTH:
        other_perm.append("执行")
    details["其他用户权限"] = ", ".join(other_perm) if other_perm else "无"
    
    # 确定特殊权限
    special_perm = []
    if mode & stat.S_ISUID:
        special_perm.append("设置用户ID")
    if mode & stat.S_ISGID:
        special_perm.append("设置组ID")
    if mode & stat.S_ISVTX:
        special_perm.append("粘滞位")
    details["特殊权限"] = ", ".join(special_perm) if special_perm else "无"
    
    return details

# 解析文件模式
file_mode = file_stat.st_mode
dir_mode = dir_stat.st_mode

print(f"  文件 '{test_file}' 的模式解析：")
file_mode_details = parse_file_mode(file_mode)
for key, value in file_mode_details.items():
    print(f"    {key}: {value}")

print()

print(f"  目录 '{test_dir}' 的模式解析：")
dir_mode_details = parse_file_mode(dir_mode)
for key, value in dir_mode_details.items():
    print(f"    {key}: {value}")

print()

print("6.3 使用stat模块计算文件哈希值：")
def calculate_file_hash(file_path, hash_algo="sha256"):
    """计算文件的哈希值"""
    import hashlib
    
    try:
        hash_obj = hashlib.new(hash_algo)
        with open(file_path, "rb") as f:
            # 分块读取文件以支持大文件
            for chunk in iter(lambda: f.read(4096), b""):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        print(f"   错误: {e}")
        return None

# 计算文件哈希值
file_hash = calculate_file_hash(test_file, hash_algo="md5")
print(f"  文件 '{test_file}' 的MD5哈希值: {file_hash}")

print()

# 7. 最佳实践
print("=== 7. 最佳实践 ===")

print("1. 使用stat模块常量而不是硬编码数值：")
print("   # 错误：使用硬编码数值")
print("   if mode & 0o100000:  # 普通文件")
print("       pass")
print("   ")
print("   # 正确：使用stat模块常量")
print("   if stat.S_ISREG(mode):  # 普通文件")
print("       pass")

print("\n2. 注意跨平台差异：")
print("   # Windows和Unix系统的文件权限模型不同")
print("   # 在Windows上，有些权限常量可能不生效")
print("   if os.name == 'nt':")
print("       # Windows特定处理")
print("   else:")
print("       # Unix/Linux特定处理")

print("\n3. 错误处理：")
print("   # 获取文件状态时可能会抛出异常")
print("   try:")
print("       file_stat = os.stat(file_path)")
print("   except FileNotFoundError:")
print("       print(f'文件不存在: {file_path}')
print("   except PermissionError:")
print("       print(f'没有权限访问文件: {file_path}')")
print("   except Exception as e:")
print("       print(f'获取文件状态时出错: {e}')")

print("\n4. 使用os.lstat()处理符号链接：")
print("   # 当需要获取符号链接本身的信息时，使用os.lstat()")
print("   if os.path.islink(file_path):")
print("       link_stat = os.lstat(file_path)")
print("       target_stat = os.stat(file_path)")  # 获取链接指向的文件状态

print("\n5. 缓存文件状态信息：")
print("   # 对于频繁访问的文件状态信息，考虑缓存")
print("   file_stat_cache = {}")
print("   ")
print("   def get_cached_file_stat(file_path):")
print("       if file_path not in file_stat_cache:")
print("           file_stat_cache[file_path] = os.stat(file_path)")
print("       return file_stat_cache[file_path]")

print("\n6. 使用with语句处理文件：")
print("   # 结合文件操作和状态检查")
print("   with open(file_path, 'r') as f:")
print("       content = f.read()")
print("   ")
print("   file_stat = os.stat(file_path)")
print("   print(f'文件大小: {file_stat.st_size} 字节')")

print("\n7. 注意文件时间精度：")
print("   # 不同文件系统的时间精度不同")
print("   # 例如，FAT32文件系统的时间精度为2秒")
print("   # 而NTFS和现代Unix文件系统支持纳秒级精度")
print("   file_stat = os.stat(file_path)")
print("   print(f'修改时间 (秒): {file_stat.st_mtime}')")

# 8. 常见错误和陷阱
print("=== 8. 常见错误和陷阱 ===")

print("1. 混淆文件类型常量：")
print("   # 错误：使用错误的文件类型常量")
print("   if mode & stat.S_IFDIR:  # 这会匹配目录，但不是正确的用法")
print("       pass")
print("   ")
print("   # 正确：使用stat.S_IS*函数")
print("   if stat.S_ISDIR(mode):")
print("       pass")

print("\n2. 权限检查错误：")
print("   # 错误：直接比较权限")
print("   if file_stat.st_mode == 0o644:  # 只检查精确匹配，忽略文件类型")
print("       pass")
print("   ")
print("   # 正确：使用位运算检查权限")
print("   if (file_stat.st_mode & 0o777) == 0o644:  # 只检查权限部分")
print("       pass")

print("\n3. Windows上的权限处理：")
print("   # 错误：在Windows上使用Unix权限模型")
print("   # Windows使用不同的权限模型，stat模块的一些权限常量可能不生效")
print("   ")
print("   # 正确：检查操作系统类型")
print("   if os.name == 'nt':")
print("       # 使用Windows API处理权限")
print("       import win32security")
print("       # ...")
print("   else:")
print("       # 使用stat模块处理权限")
print("       # ...")

print("\n4. 符号链接处理：")
print("   # 错误：使用os.stat()获取符号链接本身的状态")
print("   link_stat = os.stat(link_path)  # 获取的是链接指向的文件状态")
print("   ")
print("   # 正确：使用os.lstat()获取符号链接本身的状态")
print("   link_stat = os.lstat(link_path)  # 获取的是符号链接本身的状态")
print("   target_stat = os.stat(link_path)  # 获取的是链接指向的文件状态")

print("\n5. 时间戳转换错误：")
print("   # 错误：假设时间戳是整数")
print("   mtime = int(file_stat.st_mtime)  # 可能丢失精度")
print("   ")
print("   # 正确：保留原始时间戳")
print("   mtime = file_stat.st_mtime  # 保留浮点精度")
print("   mtime_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S.%f')")

print("\n6. 忽略异常处理：")
print("   # 错误：忽略异常")
print("   file_stat = os.stat(file_path)  # 可能抛出异常")
print("   ")
print("   # 正确：处理异常")
print("   try:")
print("       file_stat = os.stat(file_path)")
print("   except FileNotFoundError:")
print("       print(f'文件不存在: {file_path}')")
print("   except PermissionError:")
print("       print(f'没有权限访问文件: {file_path}')")

# 9. 总结
print("=== 9. 总结 ===")
print("stat模块是Python中获取和解释文件状态信息的重要工具，与os模块紧密集成。")
print()
print("主要功能：")
print("- 获取文件的详细状态信息（大小、权限、修改时间等）")
print("- 解释文件模式（权限和类型）")
print("- 提供文件类型和权限的常量定义")
print("- 支持跨平台的文件状态信息获取")
print()
print("优势：")
print("- 提供了统一的接口来获取文件状态信息")
print("- 支持跨平台操作")
print("- 提供了丰富的常量和函数来解释文件模式")
print("- 与Python的其他文件系统模块良好集成")
print()
print("应用场景：")
print("- 文件系统管理工具")
print("- 文件备份和同步工具")
print("- 文件权限管理工具")
print("- 文件分析和统计工具")
print("- 安全审计工具")
print()
print("通过合理使用stat模块，可以编写功能强大的文件系统操作程序，获取和解释文件的详细状态信息。")

# 清理测试文件和目录
import shutil
shutil.rmtree(test_dir)
