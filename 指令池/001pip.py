
"""pip命令深度教学脚本 | pip command advanced tutorial script"""

from __future__ import annotations

from pathlib import Path  # 处理文件路径 | Handle filesystem paths
import json  # 读写 JSON 数据 | Read/write JSON data
from textwrap import dedent  # 整理多行文本缩进 | Normalize multiline string indentation
import subprocess  # 运行子进程执行 pip 等命令 | Run CLI commands via subprocess
import sys  # 获取当前 Python 解释器信息 | Access current Python interpreter info


# ================================
# 1. pip 基础命令表 | Core pip command table
# ================================
# PIP_COMMAND_TABLE 负责展示安装/卸载/查询的典型操作，附双语示例。
# PIP_COMMAND_TABLE describes install/uninstall/list commands with bilingual samples.
PIP_COMMAND_TABLE = dedent(
    """
    【1】安装包 | Install packages
    Command: pip install package==version
    Options:
        --upgrade     升级到最新版本
        --pre         允许安装预发布版
        -r req.txt    根据依赖清单安装
    Examples:
        ① pip install requests==2.32.0 --upgrade
           说明 | Note: 升级网络库 | upgrade network lib
        ② pip install -r requirements/base.txt --pre
           说明 | Note: 测试预发布版 | test pre-release

    【2】卸载包 | Uninstall packages
    Command: pip uninstall package -y
    Scenario: 清理无用依赖或冲突版本。
    Examples:
        ① pip uninstall pandas -y
        ② pip uninstall django==4.2 -y  # 指定版本 remove exact version

    【3】查看已装包 | List installed packages
    Command: pip list --outdated --format=columns
    Tips: 搭配 pip index versions <pkg> 查看可选版本。
    Examples:
        ① pip list --outdated --format=columns
        ② pip index versions fastapi
    """
)


# ================================
# 2. 依赖记录与复现 | Dependency freezing & replay
# ================================
# FREEZE_BLOCK 用于说明 freeze 和 lockfile 的流程，确保环境可重建。
# FREEZE_BLOCK explains freeze + lockfile workflows for reproducible envs.
FREEZE_BLOCK = dedent(
    """
    【4】记录当前依赖 | Freeze current dependencies
    Command: pip freeze > requirements.lock
    Scenario: 锁定可复现环境。
    Examples:
        ① pip freeze > requirements.lock
        ② pip freeze --all > requirements-full.txt

    【5】从锁定文件安装 | Install from lockfile
    Command: pip install -r requirements.lock
    Extension:
        - pip install --no-deps 配合 pip-compile 输出，避免重复解析。
    Examples:
        ① pip install -r requirements.lock --no-deps
        ② pip install --disable-pip-version-check -r prod.lock
    """
)


# ================================
# 3. 仓库与配置 | Index & config management
# ================================
# INDEX_BLOCK 涵盖镜像切换与 pip config 层次，便于企业/校园网场景。
# INDEX_BLOCK covers mirror switches and pip config levels for corp/campus usage.
INDEX_BLOCK = dedent(
    """
    【6】切换仓库 | Switch index
    Command: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pkg
    Option: --trusted-host pypi.tuna.tsinghua.edu.cn
    Examples:
        ① pip install -i https://mirrors.aliyun.com/pypi/simple numpy
        ② pip install somepkg --index-url=https://pypi.org/simple --extra-index-url=https://pypi.tuna.tsinghua.edu.cn/simple

    【7】配置文件管理 | Manage pip.ini/pip.conf
    Command:
        pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
        pip config list
    Levels:
        - global | 系统范围
        - user   | 当前用户
        - site   | 虚拟环境
    Examples:
        ① pip config set user.index-url https://pypi.tuna.tsinghua.edu.cn/simple
        ② pip config get global.trusted-host
    """
)


# ================================
# 4. 缓存与离线 | Cache & offline flow
# ================================
# CACHE_BLOCK 提供缓存查看与离线三步法，帮助弱网环境部署。
# CACHE_BLOCK gives cache inspections + offline 3-step approach for low connectivity.
CACHE_BLOCK = dedent(
    """
    【8】查看缓存目录 | Show cache
    Command: pip cache dir
    Related:
        - pip cache list
        - pip cache remove <pattern>
        - pip cache purge
    Examples:
        ① pip cache dir
        ② pip cache remove numpy --verbose

    【9】离线安装流程 | Offline install flow
    Steps:
        1. 在线机器 pip download -r requirements.txt -d wheelhouse
        2. 拷贝 wheelhouse 到目标环境
        3. pip install --no-index --find-links=wheelhouse -r requirements.txt
    Examples:
        ① pip download fastapi uvicorn -d wheelhouse
        ② pip install --no-index --find-links=wheelhouse fastapi==0.110.0
    """
)


# ================================
# 5. 构建与发布 | Build & publish
# ================================
# BUILD_BLOCK 关注 wheel 构建/验证及 twine 上传，覆盖 CI/CD 流程。
# BUILD_BLOCK focuses on wheel build/validation and twine upload for CI/CD.
BUILD_BLOCK = dedent(
    """
    【10】构建 wheel | Build wheel
    Command: pip wheel . -w dist
    Scenario: 加速部署，避免现场构建。
    Examples:
        ① pip wheel . -w dist --no-deps
        ② pip wheel src/cli -w build/wheels

    【11】检查轮子 | Inspect wheel
    Command: pip install dist/yourpkg.whl --force-reinstall --no-deps
    Extension:
        - python -m twine upload dist/* 上传到 PyPI/私仓。
    Examples:
        ① pip install dist/mypkg-0.1.0-py3-none-any.whl --force-reinstall
        ② pip install --no-deps dist/utils-1.0.0-py3-none-any.whl
    """
)


# ================================
# 6. 调试与诊断 | Debug & diagnose
# ================================
# DEBUG_BLOCK 展示 pip --debug、check、inspect 三种排错手段。
# DEBUG_BLOCK shows three troubleshooting tools: debug, check, inspect.
DEBUG_BLOCK = dedent(
    """
    【12】调试模式 | Debug mode
    Command: pip --debug install somepkg
    Scenario: 捕获解析过程、HTTP 日志。
    Examples:
        ① pip --debug install failingpkg
        ② pip --debug list --verbose

    【13】兼容性检查 | Compatibility check
    Command: pip check
    Scenario: 快速发现依赖冲突。
    Examples:
        ① pip check
        ② pip check --path .venv/Lib/site-packages

    【14】环境扫描 | Environment inspect
    Command: pip inspect --verbose --local
    Output: JSON 结果，便于记录依赖快照。
    Examples:
        ① pip inspect --local --output report.json
        ② pip inspect --path .venv/lib/python3.11/site-packages
    """
)


def run_pip_command(args: list[str]) -> subprocess.CompletedProcess[str]:
    """通过 subprocess 执行 pip | Execute pip via subprocess"""

    # 通过 sys.executable -m pip 避免 PATH 混乱 | use sys.executable -m pip to avoid PATH issues
    return subprocess.run(
        [sys.executable, "-m", "pip", *args],
        check=True,  # check=True: 子进程异常时抛出错误 | raise on non-zero return
        capture_output=True,  # 捕获 stdout/stderr 以供上层函数解析 | capture stdout/stderr for parsing
        text=True,  # 返回字符串而非字节 | decode output into str
    )


def export_dependency_snapshot(path: Path) -> None:
    """导出依赖快照 JSON | Export dependency snapshot"""

    # 使用 pip inspect 输出环境详情，并写入 JSON 方便归档/比对。
    # Use pip inspect to dump env info into JSON for auditing/comparison.
    inspect = run_pip_command(["inspect", "--verbose", "--local"])
    data = json.loads(inspect.stdout)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Snapshot saved to {path}")


CHALLENGES = [
    "如何结合 pip-tools 与 pip install --no-deps 打造稳定部署？",
    "企业内网如何自建 PyPI 镜像并与 pip config 集成？",
    "pip install 遇到 SSL CERTIFICATE_VERIFY_FAILED 时的排查步骤？",
]


def show_challenges() -> None:
    """打印练习题 | Print challenge questions"""

    # 将思考题按编号输出，提示读者拓展练习场景。
    # Enumerate questions to encourage further exploration.
    for idx, q in enumerate(CHALLENGES, start=1):
        print(f"Challenge {idx}: {q}")


if __name__ == "__main__":
    print(PIP_COMMAND_TABLE)  # 打印基础命令段落 | Print base command section
    print(FREEZE_BLOCK)  # 打印依赖冻结段落 | Print freeze section
    print(INDEX_BLOCK)  # 打印镜像与配置段落 | Print index/config section
    print(CACHE_BLOCK)  # 打印缓存与离线段落 | Print cache/offline section
    print(BUILD_BLOCK)  # 打印构建与发布段落 | Print build/publish section
    print(DEBUG_BLOCK)  # 打印调试诊断段落 | Print debug/diagnose section
    show_challenges()
    export_dependency_snapshot(Path("pip_environment_snapshot.json"))




















































































