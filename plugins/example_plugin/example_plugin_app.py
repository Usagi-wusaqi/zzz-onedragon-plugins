"""示例插件应用。

演示如何创建一个基本的 ZZZ-OneDragon 插件应用。
"""

from one_dragon.base.operation.application.application_base import ApplicationBase
from zzz_od.context.zzz_context import ZContext


class ExamplePluginApp(ApplicationBase):
    """示例插件应用。

    这是一个简单的示例，展示如何创建一个基本的应用。
    """

    def __init__(self, ctx: ZContext):
        ApplicationBase.__init__(self, ctx)

    def handle_init(self):
        pass

    def handle_start(self):
        # 在这里实现你的应用逻辑
        pass

    def handle_stop(self):
        pass
