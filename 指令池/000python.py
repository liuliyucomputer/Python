"""Python命令全景教学脚本 | Python Command Full Tutorial Script
整合常用 CLI 指令、使用场景、案例以及举一反三思考，帮助快速掌握并迁移到真实项目。
Aggregate CLI commands, scenarios, examples, and reflective prompts for fast mastery.
"""

from __future__ import annotations

from pathlib import Path  # 路径处理工具 | Path handling utility
import subprocess  # 运行子进程执行命令 | Execute CLI commands via subprocess
import sys  # 访问当前解释器与路径信息 | Access interpreter & path info
from textwrap import dedent  # 整理多行字符串缩进 | Normalize multiline indentation

# ================================
# 1. 基础环境命令 | Basic environment commands
# ================================
# BASIC_COMMANDS：集中展示最常用的 python CLI 操作，便于快速查阅。
# BASIC_COMMANDS: collect essential python CLI actions for quick lookup.
BASIC_COMMANDS = dedent(
    """
    【1】查看 Python 版本 | Check Python version
    Command: python --version
    Scenario: 确认解释器版本，避免多版本冲突。
    Examples:
        ① PS> python --version   # Windows
           输出 | Output: Python 3.12.2
        ② $ python3 --version    # Linux/macOS
           输出 | Output: Python 3.10.13

    【2】进入交互式解释器 | Enter interactive REPL
    Command: python  或  python -q（安静模式）
    Scenario: 快速测试语法/调用 help()。
    Tips:
        - exit() 或 Ctrl+Z/Ctrl+D 退出。
    Examples:
        ① PS> python            -> >>> print("hi")
        ② $ python -q           -> >>> help(str)

    【3】执行脚本文件 | Run script file
    Command: python script.py [args]
    Scenario: 启动主程序或一次性脚本。
    Examples:
        ① PS> python tools/build_assets.py --minify
        ② $ python manage.py migrate --settings=prod
    """
)

# ================================
# 2. 模块直接运行 | Run modules directly
# ================================
# MODULE_COMMANDS：演示以 "python -m" 方式运行包模块及测试工具。
# MODULE_COMMANDS: showcases running package modules and test tools via "python -m".
MODULE_COMMANDS = dedent(
    """
    【4】运行包内模块 | Run package module
    Command: python -m package.module [args]
    Scenario: 保持包结构，避免手动修改 PYTHONPATH。
    Examples:
        ① PS> python -m http.server 8000  # 临时静态服务 temp static server
        ② $ python -m venv --help         # 查看模块说明 show module help

    【5】单元测试自动化 | Automate unit tests
    Command: python -m unittest discover -s tests -p "test_*.py"
    Scenario: 执行全量测试确保质量。
    Extension:
        - 搭配 python -m pytest 使用第三方框架。
    Examples:
        ① $ python -m unittest tests.test_api
        ② $ python -m unittest discover -s src/tests -p "*_spec.py"
    """
)

# ================================
# 3. 虚拟环境管理 | Virtual environment management
# ================================
# VENV_SECTION：指导如何创建/激活虚拟环境并核验依赖，确保隔离性。
# VENV_SECTION: explains creating/activating venv and validating deps for isolation.
VENV_SECTION = dedent(
    """
    【6】创建虚拟环境 | Create venv
    Command: python -m venv .venv
    Scenario: 为项目隔离依赖。
    Tips:
        - Windows 激活：.venv\\Scripts\\activate
        - macOS/Linux：source .venv/bin/activate
    Examples:
        ① PS> python -m venv .venv && .venv\\Scripts\\activate
        ② $ python3 -m venv /envs/blog && source /envs/blog/bin/activate
        ③ PS> python -m venv .venv --system-site-packages
        ④ $ python3 -m venv /envs/project --prompt project-env

    【7】验证依赖 | Validate dependencies
    Command: python -m pip list  或  python -m pip check
    Scenario: 安装后确认版本/依赖冲突。
    Examples:
        ① PS> python -m pip list --outdated
        ② $ python -m pip check | grep "requires"
    """
)

# ================================
# 4. 常用内置模块工具 | Handy built-in tools
# ================================
# BUILT_IN_TOOLS：列出常用标准库命令式工具，满足临时服务与分析需求。
# BUILT_IN_TOOLS: highlights stdlib command-like utilities for quick services & profiling.
BUILTIN_TOOLS = dedent(
    """
    【8】临时 HTTP 服务 | Temporary HTTP server
    Command: python -m http.server 9000 --directory public
    Scenario: 分享静态导出结果、调试前端。
    Extension:
        - --bind 0.0.0.0 允许局域网访问。
    Examples:
        ① PS> python -m http.server 8080 --directory dist
        ② $ python -m http.server 9000 --bind 0.0.0.0

    【9】性能剖析 | Performance profiling
    Command: python -m cProfile -o stats.out script.py
    Scenario: 找到性能瓶颈。
    Next step:
        - 使用 snakeviz stats.out 进行可视化分析。
    Examples:
        ① $ python -m cProfile -o stats.out app.py
        ② PS> python -m cProfile -m module.entry --sort=tottime

    【10】构建可执行归档 | Build executable archive
    Command: python -m zipapp src -o app.pyz -m "main:run"
    Scenario: 打包可移植应用。
    Examples:
        ① $ python -m zipapp project -o build/app.pyz
        ② PS> python -m zipapp src -m "cli:main" -o tools/cli.pyz
    """
)


def demo_unicode_print() -> None:
    """示例：打印中英文信息 | Demo: print bilingual info"""

    # 直接输出双语文本，提示终端环境是否支持 Unicode。
    # Print bilingual text to verify terminal Unicode support.
    print("Hello, Python CLI! | 你好，Python 命令行！")


def demo_subprocess_version() -> str:
    """示例：通过 subprocess 读取版本 | Demo: read version via subprocess"""

    # 使用 sys.executable 保证与当前进程一致 | Guarantees same interpreter via sys.executable
    result = subprocess.run(
        [sys.executable, "--version"],
        capture_output=True,  # 捕获输出，便于进一步处理 | capture output for reuse
        text=True,
        check=True,
    )
    return result.stdout.strip()


# ================================
# 5. 举一反三思考 | Transfer thinking prompts
# ================================
TRANSFER_QUESTIONS = [
    "如何使用 python -m ensurepip 在离线环境初始化 pip？",
    "多解释器系统中如何显式指定 python 可执行路径？",
    "怎样结合任务计划 (Task Scheduler/cron) 定期执行 python -m job？",
]


def show_transfer_questions() -> None:
    """打印思考题 | Print reflective questions"""

    # enumerate 带 start=1，方便与文案编号对应 | start=1 keeps numbering consistent with text
    for idx, question in enumerate(TRANSFER_QUESTIONS, start=1):
        print(f"Q{idx}: {question}")


def save_handout(path: Path) -> None:
    """保存讲义文本 | Save handout text"""

    # 将多段教学文字拼接，方便生成离线笔记 | Join sections to create offline notes
    content = "\n".join([BASIC_COMMANDS, MODULE_COMMANDS, VENV_SECTION, BUILTIN_TOOLS])
    path.write_text(content, encoding="utf-8")
    print(f"Handout exported to {path}")


if __name__ == "__main__":
    print(BASIC_COMMANDS)  # 输出基础命令教学 | Print basic command guide
    print(MODULE_COMMANDS)  # 输出模块运行教学 | Print module-running guide
    print(VENV_SECTION)  # 输出虚拟环境章节 | Print venv section
    print(BUILTIN_TOOLS)  # 输出内置工具章节 | Print built-in tools section
    demo_unicode_print()
    print(f"Current Python Version (subprocess): {demo_subprocess_version()}")
    show_transfer_questions()
    save_handout(Path("python_cli_handout.txt"))