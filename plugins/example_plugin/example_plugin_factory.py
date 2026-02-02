"""示例插件工厂。

工厂文件必须以 _factory.py 结尾才能被自动发现。
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_config import ApplicationConfig
from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord

from . import example_plugin_const

if TYPE_CHECKING:
    from zzz_od.context.zzz_context import ZContext


class ExamplePluginFactory(ApplicationFactory):
    """示例插件工厂。"""

    def __init__(self, ctx: ZContext):
        ApplicationFactory.__init__(
            self,
            app_id=example_plugin_const.APP_ID,
            app_name=example_plugin_const.APP_NAME,
            default_group=example_plugin_const.DEFAULT_GROUP,
        )
        self.ctx: ZContext = ctx

    def create_application(self, instance_idx: int, group_id: str):
        from .example_plugin_app import ExamplePluginApp

        return ExamplePluginApp(self.ctx)

    def create_config(self, instance_idx: int, group_id: str) -> ApplicationConfig:
        from .example_plugin_config import ExamplePluginConfig

        return ExamplePluginConfig(instance_idx, group_id)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from .example_plugin_run_record import ExamplePluginRunRecord

        return ExamplePluginRunRecord(
            instance_idx=instance_idx,
            game_refresh_hour_offset=self.ctx.game_account_config.game_refresh_hour_offset,
        )
