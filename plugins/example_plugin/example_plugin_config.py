"""示例插件配置。

展示如何为插件创建可持久化的配置。
配置文件会保存到 config/{instance_idx}/{group_id}/example_plugin.yml
"""

from one_dragon.base.operation.application.application_config import ApplicationConfig

from . import example_plugin_const


class ExamplePluginConfig(ApplicationConfig):
    """示例插件配置类。

    继承 ApplicationConfig 可以自动将配置保存到 yml 文件。
    """

    def __init__(self, instance_idx: int, group_id: str):
        ApplicationConfig.__init__(
            self,
            instance_idx=instance_idx,
            app_id=example_plugin_const.APP_ID,
            group_id=group_id,
        )

    # ============ 配置项示例 ============

    @property
    def example_option(self) -> str:
        """示例配置项：字符串类型。"""
        return self.get("example_option", "默认值")

    @example_option.setter
    def example_option(self, new_value: str) -> None:
        self.update("example_option", new_value)

    @property
    def example_number(self) -> int:
        """示例配置项：数字类型。"""
        return self.get("example_number", 10)

    @example_number.setter
    def example_number(self, new_value: int) -> None:
        self.update("example_number", new_value)

    @property
    def example_enabled(self) -> bool:
        """示例配置项：布尔类型。"""
        return self.get("example_enabled", True)

    @example_enabled.setter
    def example_enabled(self, new_value: bool) -> None:
        self.update("example_enabled", new_value)
