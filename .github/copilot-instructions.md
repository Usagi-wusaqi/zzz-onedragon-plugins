---
applyTo: "**"
---

# General Instructions
- **Language**: 请始终使用 **简体中文** 回复。

# Project Context
这是 **ZZZ-OneDragon 插件仓库**，用于存放第三方插件。
- 主仓库: https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon
- 插件安装位置: `zzz_od/plugins/` 目录
- 导入路径格式: `zzz_od.plugins.{plugin_name}`

# Coding Standards
- **Python**: 3.11+，使用现代特性 (`list[str]`, `X | None`)
- **Type Hints**: 所有函数/方法尽量有类型注解
- **Path**: 使用 `pathlib`，不用 `os.path`
- **String**: 使用 f-string
- **Error**: 避免无意义的 try-catch
- **KISS**: 保持简单，不过度设计

# Plugin Structure (必需)
```
my_plugin/
├── __init__.py
├── my_plugin_const.py    # 必需: APP_ID, APP_NAME, DEFAULT_GROUP
├── my_plugin_factory.py  # 必需: 继承 ApplicationFactory
├── my_plugin_app.py      # 应用逻辑
└── my_plugin_run_record.py
```

# Import Rule (重要!)
```python
# ✅ 正确 - 完整路径
from zzz_od.plugins.my_plugin import my_plugin_const
from zzz_od.plugins.my_plugin.my_plugin_app import MyPluginApp

# ❌ 错误 - 相对导入
from . import my_plugin_const
from .my_plugin_app import MyPluginApp
```

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
