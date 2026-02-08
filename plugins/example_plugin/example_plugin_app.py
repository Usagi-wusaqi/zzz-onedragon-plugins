"""示例插件应用。

演示如何创建一个基本的 ZZZ-OneDragon 插件应用。
"""

from one_dragon.base.operation.application_base import Application
from one_dragon.base.operation.operation_node import operation_node
from one_dragon.base.operation.operation_round_result import OperationRoundResult
from zzz_od.context.zzz_context import ZContext

from . import example_plugin_const


class ExamplePluginApp(Application):
    """示例插件应用。

    这是一个简单的示例，展示如何创建一个基本的应用。
    使用节点编排模式：通过 @operation_node 定义节点，通过 handle_init 中的 add_edge 定义执行流程。
    """

    def __init__(self, ctx: ZContext):
        Application.__init__(
            self,
            ctx=ctx,
            app_id=example_plugin_const.APP_ID,
            op_name=example_plugin_const.APP_NAME,
        )

    def handle_init(self):
        """初始化节点编排。"""
        Application.handle_init(self)

    @operation_node(name="示例步骤", is_start_node=True)
    def example_step(self) -> OperationRoundResult:
        """示例步骤：在这里实现你的应用逻辑。"""
        # 在这里实现你的应用逻辑
        return self.round_success()
