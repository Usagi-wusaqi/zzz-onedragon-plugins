# ZZZ-OneDragon 插件仓库

[ZenlessZoneZero-OneDragon](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon) 的插件仓库。

> ⚠️ **注意**：需要支持插件系统的 ZZZ-OneDragon 版本才能使用。

## 如何使用

### 方法一：通过 GUI 导入（推荐）

1. 打开 ZZZ-OneDragon 设置 → 插件管理
2. 点击"导入插件"按钮
3. 选择 `.zip` 格式的插件压缩包
4. 插件会自动解压并注册

### 方法二：手动安装

1. 下载插件文件夹（如 `example_plugin`）
2. 将插件文件夹放入项目的 `plugins/` 目录
3. 重启 ZZZ-OneDragon 或在插件管理界面点击"刷新"

## 特性

- ✅ **相对导入**：`from .utils import xxx`
- ✅ **导入主程序模块**：`from one_dragon.xxx import yyy`, `from zzz_od.xxx import yyy`
- ✅ **支持子包**：可以有多层目录结构

## 加载机制

加载插件时，`plugins/` 目录会被添加到 `sys.path`，使每个插件包成为独立的顶级模块：

```python
# 加载过程
sys.path.insert(0, "project_root/plugins")  # 添加一次

# 插件模块名示例
# plugins/my_plugin/my_plugin_factory.py → my_plugin.my_plugin_factory
```

## 目录结构示例

```
plugins/                          # ← 添加到 sys.path
├── README.md
├── plugin_a/                     # 插件 A
│   ├── __init__.py               # 推荐添加
│   ├── plugin_a_const.py         # 定义 APP_ID, APP_NAME, DEFAULT_GROUP
│   ├── plugin_a_factory.py       # 工厂类（必须以 _factory.py 结尾）
│   ├── plugin_a.py               # 应用实现
│   └── utils/                    # 子包
│       ├── __init__.py
│       └── helper.py
└── plugin_b/                     # 插件 B
    ├── __init__.py
    ├── plugin_b_const.py
    └── plugin_b_factory.py
```

## 开发指南

### 1. 创建插件目录

在 `plugins/` 下创建以插件名命名的目录，如 `plugins/my_plugin/`。

### 2. 定义常量文件

创建 `my_plugin_const.py`，定义应用的基本信息：

```python
# plugins/my_plugin/my_plugin_const.py

APP_ID = "my_plugin"
APP_NAME = "我的插件"
DEFAULT_GROUP = True  # True: 显示在一条龙列表，False: 独立工具

# 插件元数据（可选，用于 GUI 显示）
PLUGIN_AUTHOR = "作者名"
PLUGIN_HOMEPAGE = "https://github.com/author/my_plugin"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "插件功能描述"
```

### 3. 创建工厂类

创建 `my_plugin_factory.py`（**文件名必须以 `_factory.py` 结尾**）：

```python
# plugins/my_plugin/my_plugin_factory.py

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from zzz_od.context.zzz_context import ZContext  # ✅ 导入主程序模块

from . import my_plugin_const      # ✅ 相对导入
from .my_plugin import MyPlugin    # ✅ 相对导入


class MyPluginFactory(ApplicationFactory):
    def __init__(self, ctx: ZContext):
        super().__init__(
            app_id=my_plugin_const.APP_ID,
            app_name=my_plugin_const.APP_NAME,
            default_group=my_plugin_const.DEFAULT_GROUP,
        )
        self.ctx = ctx

    def create_application(self, instance_idx, group_id):
        return MyPlugin(self.ctx)
```

### 4. 实现应用逻辑

```python
# plugins/my_plugin/my_plugin.py

from one_dragon.base.operation.application.application_base import Application
from zzz_od.context.zzz_context import ZContext

from .utils.helper import do_something  # ✅ 相对导入子模块


class MyPlugin(Application):
    def __init__(self, ctx: ZContext):
        super().__init__(ctx, "my_plugin", node_max_retry_times=3)

    def _execute_one_round(self):
        do_something()
        return self.round_success()
```

## 📦 打包插件

将插件目录压缩为 `.zip` 文件即可分发：

```
my_plugin.zip
└── my_plugin/
    ├── __init__.py
    ├── my_plugin_const.py
    ├── my_plugin_factory.py
    └── my_plugin.py
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

### 插件未显示

1. 确保工厂文件以 `_factory.py` 结尾
2. 确保 const 文件包含 `APP_ID`, `APP_NAME`, `DEFAULT_GROUP`
3. 确保添加了 `__init__.py` 以支持相对导入
4. 检查日志获取详细错误信息
5. 尝试在插件管理界面点击"刷新"

## 注意事项

1. **文件命名**：工厂文件必须以 `_factory.py` 结尾
2. **`__init__.py`**：建议添加以支持相对导入
3. **模块名唯一性**：插件包名（目录名）应该唯一，避免与其他插件或主程序模块冲突
4. **备份**：此目录被 `.gitignore` 忽略，请自行备份
5. **热重载**：刷新应用时会自动卸载并重新加载插件模块
