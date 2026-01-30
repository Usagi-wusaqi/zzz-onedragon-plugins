"""示例插件应用。"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application_base import Application
from one_dragon.base.operation.operation_round_result import OperationRoundResult
from one_dragon.utils.log_utils import log

from . import example_plugin_const

if TYPE_CHECKING:
    from zzz_od.context.zzz_context import ZContext


class ExamplePluginApp(Application):
    """示例插件应用。

    这是一个简单的示例，展示如何创建一个基本的应用。
    """

    def __init__(
        self,
        ctx: "ZContext",
        instance_idx: int | None = None,
        group_id: str | None = None,
    ):
        Application.__init__(
            self,
            ctx=ctx,
            app_id=example_plugin_const.APP_ID,
            app_name=example_plugin_const.APP_NAME,
            instance_idx=instance_idx,
            group_id=group_id,
        )
        self.ctx = ctx

    def run_application(self) -> OperationRoundResult:
        """执行插件逻辑。"""
        log.info("示例插件开始执行...")

        # 在这里添加你的插件逻辑
        # 例如：
        # - 截图分析
        # - 自动点击
        # - 数据处理
        # 等等

        log.info("示例插件执行完成！")
        return self.round_success()
