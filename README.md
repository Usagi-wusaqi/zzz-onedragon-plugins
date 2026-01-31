# ZZZ-OneDragon 插件仓库

[ZenlessZoneZero-OneDragon](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon) 的插件仓库。

> ⚠️ **注意**：需要支持插件系统的 ZZZ-OneDragon 版本才能使用。

## 📦 插件列表

| 插件 | 版本 | 描述 | 作者 |
|------|------|------|------|
| [example_plugin](plugins/example_plugin) | 1.0.0 | 示例插件模板 | Usagi-wusaqi |

## 🔧 如何使用

### 方法一：通过 GUI 导入（推荐）

1. 打开 ZZZ-OneDragon 设置 → 插件管理
2. 点击"导入插件"按钮
3. 选择 `.zip` 格式的插件压缩包
4. 插件会自动解压并注册

### 方法二：手动安装

1. 下载插件文件夹（如 `example_plugin`）
2. 将插件文件夹放入项目的 `src/zzz_od/plugins/` 目录
3. 重启 ZZZ-OneDragon 或在插件管理界面点击"刷新"

**目录结构：**

```
ZenlessZoneZero-OneDragon/
├── src/
│   └── zzz_od/
│       └── plugins/           # 插件目录
│           └── example_plugin/
│               ├── __init__.py
│               ├── example_plugin_const.py
│               ├── example_plugin_factory.py
│               └── example_plugin_app.py
└── ...
```

## 📝 如何开发插件

插件必须遵循 `ApplicationPluginManager` 的自动发现规则。

### 插件目录结构

```
your_plugin/
├── __init__.py                # Python 包初始化
├── your_plugin_const.py       # 常量定义 (必需)
├── your_plugin_factory.py     # ApplicationFactory 实现 (必需)
├── your_plugin_app.py         # Application 实现
├── your_plugin_config.py      # 配置类 (可选)
├── your_plugin_run_record.py  # 运行记录类 (可选)
└── README.md                  # 插件说明文档 (建议)
```

**重要命名规则：**
- 工厂文件必须以 `_factory.py` 结尾
- 常量文件命名为 `xxx_const.py`

### const 文件示例

```python
# your_plugin_const.py

# ============ 核心常量 (必需) ============
APP_ID = "your_plugin"
APP_NAME = "你的插件"
DEFAULT_GROUP = True  # True: 出现在一条龙列表, False: 不出现

# ============ 插件元数据 (可选，用于 GUI 显示) ============
PLUGIN_AUTHOR = "作者名"
PLUGIN_HOMEPAGE = "https://github.com/author/your_plugin"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "插件功能描述"
```

### Factory 文件示例

```python
# your_plugin_factory.py
from __future__ import annotations

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory

# ✅ 正确 - 使用完整模块路径导入
from zzz_od.plugins.your_plugin import your_plugin_const

if TYPE_CHECKING:
    from zzz_od.context.zzz_context import ZContext


class YourPluginFactory(ApplicationFactory):
    """你的插件工厂"""

    def __init__(self, ctx: ZContext):
        ApplicationFactory.__init__(
            self,
            app_id=your_plugin_const.APP_ID,
            app_name=your_plugin_const.APP_NAME,
            default_group=your_plugin_const.DEFAULT_GROUP,
        )
        self.ctx: ZContext = ctx

    def create_application(self, instance_idx: int, group_id: str):
        # ✅ 正确 - 使用完整模块路径导入
        from zzz_od.plugins.your_plugin.your_plugin_app import YourPluginApp
        return YourPluginApp(self.ctx)
```

### Application 文件示例

```python
# your_plugin_app.py
from one_dragon.base.operation.application.application_base import ApplicationBase
from zzz_od.context.zzz_context import ZContext


class YourPluginApp(ApplicationBase):
    """你的插件应用"""

    def __init__(self, ctx: ZContext):
        ApplicationBase.__init__(self, ctx)

    def handle_init(self):
        pass

    def handle_start(self):
        # 在这里实现你的应用逻辑
        pass

    def handle_stop(self):
        pass
```

## ⚠️ 导入规则（重要）

**插件内部的导入必须使用完整模块路径：**

```python
# ✅ 正确 - 使用完整路径
from zzz_od.plugins.your_plugin import your_plugin_const
from zzz_od.plugins.your_plugin.your_plugin_app import YourPluginApp

# ❌ 错误 - 使用相对导入（会导致 ModuleNotFoundError）
from . import your_plugin_const
from .your_plugin_app import YourPluginApp
```

## 📦 打包插件

将插件目录压缩为 `.zip` 文件即可分发：

```
your_plugin.zip
└── your_plugin/
    ├── __init__.py
    ├── your_plugin_const.py
    ├── your_plugin_factory.py
    └── your_plugin_app.py
```

## 🔄 应用分组

### 默认组应用 (DEFAULT_GROUP=True)

- 会出现在"一条龙"运行列表中
- 可以被用户排序和启用/禁用
- 适用于：体力刷本、咖啡店、邮件等日常任务

### 非默认组应用 (DEFAULT_GROUP=False)

- 不会出现在"一条龙"运行列表中
- 作为独立工具使用
- 适用于：自动战斗、闪避助手、截图工具等

## 📂 示例插件

仓库中包含一个完整的 `example_plugin` 示例，展示基本的插件结构。

| 文件 | 用途 |
|------|------|
| `__init__.py` | Python 包初始化 |
| `example_plugin_const.py` | 常量定义 (APP_ID, APP_NAME, DEFAULT_GROUP, 元数据) |
| `example_plugin_factory.py` | 工厂类，负责创建应用实例 |
| `example_plugin_app.py` | 应用类，实现具体逻辑 |
| `example_plugin_config.py` | 配置类，持久化用户设置 |
| `example_plugin_run_record.py` | 运行记录类，跟踪运行状态 |

## ❓ 常见问题

### ModuleNotFoundError

检查你的导入语句是否使用了完整路径 `zzz_od.plugins.xxx`，不要使用相对导入。

### 插件未显示

1. 确保工厂文件以 `_factory.py` 结尾
2. 确保 const 文件包含 `APP_ID`, `APP_NAME`, `DEFAULT_GROUP`
3. 检查日志获取详细错误信息
4. 尝试在插件管理界面点击"刷新"

## 📌 注意事项

1. **目录命名**：插件目录名应与插件 ID 一致
2. **文件命名**：工厂文件必须以 `_factory.py` 结尾
3. **const 文件**：必须定义 `APP_ID`, `APP_NAME`, `DEFAULT_GROUP` 常量
4. **导入路径**：所有导入必须使用 `zzz_od.plugins.xxx` 完整路径
5. **元数据**：建议填写 `PLUGIN_AUTHOR`、`PLUGIN_VERSION` 等元数据以便用户识别
6. **错误处理**：加载失败的工厂会被跳过并记录警告日志
