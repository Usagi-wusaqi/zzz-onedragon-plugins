# ZZZ-OneDragon 插件仓库

[ZenlessZoneZero-OneDragon](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon) 的第三方插件仓库。

> ⚠️ **注意**：需要 `feat/plugins` 分支或更新版本才能使用插件功能。

## 📦 插件列表

| 插件 | 描述 |
|------|------|
| [example_plugin](plugins/example_plugin) | 示例插件模板 |

## 🔧 如何使用

1. 确保 ZZZ-OneDragon 支持 `plugins/` 目录扫描（需要 `feat/plugins` 分支或更新版本）
2. 下载插件文件夹（如 `example_plugin`）
3. 将插件文件夹放入项目根目录的 `plugins/` 目录
4. 重启 ZZZ-OneDragon
5. 在应用列表中找到新插件

**目录结构：**
```
ZenlessZoneZero-OneDragon/
├── plugins/
│   └── example_plugin/    # 你下载的插件
│       ├── example_plugin_const.py
│       ├── example_plugin_factory.py
│       └── ...
├── src/
└── ...
```

## 📝 如何开发插件

插件必须遵循 `ApplicationPluginManager` 的自动发现规则。

### 插件目录结构

```
plugins/your_plugin/
├── your_plugin_const.py       # 常量定义 (必需)
├── your_plugin_factory.py     # ApplicationFactory 实现 (必需)
├── your_plugin_app.py         # Application 实现
├── __init__.py                # Python 包初始化
└── README.md                  # 插件说明文档
```

**重要命名规则：**
- 工厂文件必须以 `_factory.py` 结尾
- 常量文件命名为 `xxx_const.py`

### const 文件示例

```python
# your_plugin_const.py
APP_ID = "your_plugin"
APP_NAME = "你的插件"
NEED_NOTIFY = False
DEFAULT_GROUP = True  # True: 出现在一条龙列表, False: 不出现
```

### Factory 文件示例

```python
# your_plugin_factory.py
from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_base import Application
from . import your_plugin_const

if TYPE_CHECKING:
    from zzz_od.context.zzz_context import ZContext


class YourPluginFactory(ApplicationFactory):
    """你的插件工厂"""

    def __init__(self, ctx: "ZContext"):
        ApplicationFactory.__init__(
            self,
            app_id=your_plugin_const.APP_ID,
            app_name=your_plugin_const.APP_NAME,
            need_notify=your_plugin_const.NEED_NOTIFY,
            default_group=your_plugin_const.DEFAULT_GROUP,
        )
        self.ctx = ctx

    def create_application(self, instance_idx: int, group_id: str) -> Application:
        from .your_plugin_app import YourPluginApp
        return YourPluginApp(self.ctx, instance_idx, group_id)
```

### Application 文件示例

```python
# your_plugin_app.py
from typing import TYPE_CHECKING

from one_dragon.base.operation.application_base import Application

if TYPE_CHECKING:
    from zzz_od.context.zzz_context import ZContext


class YourPluginApp(Application):
    """你的插件应用"""

    def __init__(self, ctx: "ZContext", instance_idx: int | None = None, group_id: str | None = None):
        Application.__init__(
            self,
            ctx=ctx,
            app_id="your_plugin",
            app_name="你的插件",
            instance_idx=instance_idx,
            group_id=group_id,
        )
        self.ctx = ctx

    def run_application(self):
        """执行插件逻辑"""
        # 你的代码
        pass
```

## 📂 示例插件

仓库中包含一个 `example_plugin` 示例，展示基本的插件结构。

**文件说明：**

| 文件 | 用途 |
|------|------|
| `example_plugin_const.py` | 常量定义 (APP_ID, APP_NAME, DEFAULT_GROUP 等) |
| `example_plugin_factory.py` | 工厂类，负责创建应用实例 |
| `example_plugin_app.py` | 应用类，实现具体逻辑 |
| `__init__.py` | Python 包初始化 |
