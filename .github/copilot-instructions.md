---
applyTo: "**"
---

# General Instructions
- **Language**: 请始终使用 **简体中文** 回复。

# Project Context
这是 **ZZZ-OneDragon 应用插件系统** 的设计与插件仓库，为 [ZenlessZoneZero-OneDragon](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon) 提供动态发现和注册应用的机制。
- 支持两种插件来源：**BUILTIN**（`src/zzz_od/application/`）和 **THIRD_PARTY**（`plugins/`）
- 运行时 `plugins/` 目录被添加到 `sys.path`，每个插件包成为独立顶级模块
- 主程序模块可直接导入: `one_dragon.*`, `zzz_od.*`
- 注册入口文件: `repo.json`（插件元信息清单）

# Core Components
- **ApplicationFactoryManager**: 扫描和加载应用工厂（`discover_factories()`）
- **ApplicationFactory**: 应用工厂基类，构造参数: `app_id`, `app_name`, `default_group`, `need_notify`
- **PluginInfo**: 插件元数据模型（`app_id`, `app_name`, `source`, `author`, `version` 等），由 `_register_plugin_metadata()` 自动注册，包含来源和目录信息

# Coding Standards
- **Python**: 3.11+，使用现代特性 (`list[str]`, `X | None`, `from __future__ import annotations`)
- **Type Hints**: 所有函数/方法必须有类型注解
- **Path**: 使用 `pathlib`，不用 `os.path`
- **String**: 使用 f-string
- **Error**: 避免无意义的 try-catch
- **KISS**: 保持简单，不过度设计
- **Lint**: Ruff (`ruff check plugins/ --select E,W,F,I,B,UP,SIM,TID --ignore E501`)

# Plugin Structure
每个插件放在 `plugins/<name>/` 下，参照 `plugins/example_plugin/`：

```
my_plugin/
├── __init__.py               # 包初始化（推荐添加 docstring）
├── my_plugin_const.py        # 必需: APP_ID, APP_NAME, DEFAULT_GROUP, NEED_NOTIFY（字段顺序一致）
├── my_plugin_factory.py      # 必需: 继承 ApplicationFactory (文件名必须以 _factory.py 结尾)
├── my_plugin_app.py          # 应用逻辑，继承 Application
├── my_plugin_config.py       # 可选: 继承 ApplicationConfig，property+setter 模式
├── my_plugin_run_record.py   # 可选: 继承 AppRunRecord，跟踪运行状态
└── sub/                      # 支持嵌套子目录
    ├── __init__.py
    ├── sub_feature_const.py
    ├── sub_feature_factory.py  # 嵌套工厂也会被自动发现
    └── helpers/
        └── utils.py
```

# Import Rules (重要!)
插件内部使用**相对导入**，主程序模块使用**绝对导入**：

```python
# ✅ 插件内部 — 相对导入
from . import my_plugin_const
from .my_plugin_app import MyPluginApp

# ✅ 主程序模块 — 绝对导入
from one_dragon.base.operation.application.application_factory import ApplicationFactory
from zzz_od.context.zzz_context import ZContext

# ✅ TYPE_CHECKING 模式 — 避免循环导入
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from zzz_od.context.zzz_context import ZContext
```

# Key Patterns
- **Factory 延迟导入**: `create_application()` / `create_config()` 内部用 `from .xxx import Xxx` 延迟导入，避免循环依赖
- **Config property**: 用 `self.get(key, default)` 读取，`self.update(key, value)` 写入，自动持久化到 yml
- **DEFAULT_GROUP**: `True` = 出现在一条龙列表（日常任务），`False` = 独立工具
- **NEED_NOTIFY**: `True` = 应用支持发送通知，`False` = 不需要通知（默认）
- **父类初始化**: 使用 `ClassName.__init__(self, ...)` 而非 `super().__init__(...)`

# Critical Rules
1. **一模块一工厂**: 每个 `_factory.py` 文件中只定义一个 `ApplicationFactory` 子类
2. **const 必需字段**: `APP_ID → APP_NAME → DEFAULT_GROUP → NEED_NOTIFY`（顺序一致，详见 `app_const_schema.py`）
3. **APP_ID 唯一性**: 重复的 APP_ID 会被 `_register_plugin_metadata` 检测并拒绝
4. **同目录冲突**: 同一目录下不允许多个 `_factory.py` 或 `_const.py` 文件
5. **热重载**: 第三方插件卸载整个包，内置插件仅卸载 factory 所在的父包

# Code Review Guidelines
**环境假设**: 1080p 分辨率 + PC 平台

**允许**:
- 硬编码像素坐标 (基于 1080p)
- 硬编码键盘按键 (`'`', `'esc'`)
- 简单逻辑中的 Magic Number

**只关注**:
- 严重逻辑错误、死循环
- 运行时崩溃风险
- 资源泄漏

**不关注** (由 Ruff 处理):
- 缩进、空行、格式
- 过度工程化建议
- 非必要的抽象
