"""示例插件运行记录。

展示如何为插件创建运行记录，用于跟踪每日/每周的运行状态。
运行记录会保存到 .log/application_run_record/{instance_idx}/example_plugin.yml

重要：插件内部的导入必须使用完整模块路径 (zzz_od.plugins.xxx)
"""

from one_dragon.base.operation.application_run_record import AppRunRecord
from zzz_od.plugins.example_plugin import example_plugin_const


class ExamplePluginRunRecord(AppRunRecord):
    """示例插件运行记录类。

    继承 AppRunRecord 可以自动跟踪应用的运行状态。
    常用于实现"每日一次"的功能。
    """

    def __init__(
        self, instance_idx: int | None = None, game_refresh_hour_offset: int = 0
    ):
        AppRunRecord.__init__(
            self,
            app_id=example_plugin_const.APP_ID,
            instance_idx=instance_idx,
            game_refresh_hour_offset=game_refresh_hour_offset,
        )

    # ============ 自定义运行记录字段示例 ============

    @property
    def custom_counter(self) -> int:
        """示例：自定义计数器。"""
        return self.get("custom_counter", 0)

    @custom_counter.setter
    def custom_counter(self, new_value: int) -> None:
        self.update("custom_counter", new_value)
