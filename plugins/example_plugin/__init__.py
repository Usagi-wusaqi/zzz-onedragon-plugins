"""示例插件包。

这是一个演示如何创建 ZZZ-OneDragon 插件的示例模板。

插件开发规范:
- 插件内部使用相对导入: from . import xxx, from .xxx import yyy
- 主程序模块使用绝对导入: from one_dragon.xxx import yyy, from zzz_od.xxx import yyy
- 工厂文件必须以 _factory.py 结尾
- const 文件必须定义 APP_ID, APP_NAME, DEFAULT_GROUP, NEED_NOTIFY
- 建议定义 PLUGIN_AUTHOR, PLUGIN_VERSION 等元数据
"""
