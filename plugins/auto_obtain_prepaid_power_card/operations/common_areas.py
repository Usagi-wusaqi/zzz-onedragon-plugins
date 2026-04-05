from enum import Enum


class CommonCoordinate(Enum):
    """三个商店共用的屏幕坐标枚举。"""

    # 共用的按钮
    BTN_INCREASE = (1246, 644, 1302, 703)  # 增加按钮
    BTN_CONFIRM = (1079, 737, 1170, 794)  # 确认按钮

    # 共用的文本区域
    TEXT_CURRENCY = (1650, 35, 1772, 66)  # 零号业绩/贡献点数/信号残响
    TEXT_SOLDOUT = (924, 591, 994, 621)   # 已售罄


class OutpostLogisticsCoordinate(Enum):
    """后勤商店屏幕坐标枚举。"""

    # 快捷手册-作战界面（用于点击进入后勤商店）
    BTN_LOGISTICS_SHOP = (836, 409, 1131, 535)

    # 后勤商店界面
    TEXT_PREPAID_CARD = (387, 115, 1801, 195)  # 储值电卡文本
    ITEM_LIST = (387, 130, 1830, 950)  # 道具列表区域


class MonthlyRestockCoordinate(Enum):
    """情报板商店屏幕坐标枚举。"""

    # 功能导览
    TEXT_INTEL_BOARD = (1398, 666, 1525, 863)  # 情报板文本按钮

    # 情报板界面
    TAB_INTEL_BOARD = (1394, 31, 1508, 68)  # 情报板TAB
    BTN_POINT_EXCHANGE = (954, 991, 1242, 1064)  # 点数兑换按钮

    # 情报板商店界面
    TEXT_PREPAID_CARD = (464, 137, 582, 182)  # 储值电卡文本
    ITEM_LIST = (387, 130, 1830, 950)  # 道具列表区域


class FadingSignalCoordinate(Enum):
    """信号残响屏幕坐标枚举。"""

    # 菜单界面
    BOTTOM_STORE = (200, 924, 1728, 1058)  # 底部商城按钮

    # 商城界面
    TAB_SIGNAL_LIST = (126, 550, 238, 595)  # 信源清单TAB

    # 信源清单界面
    TOP_FADING_SIGNAL = (1302, 131, 1443, 195)  # 顶部信号残响按钮

    # 信号残响界面
    TEXT_PREPAID_CARD = (484, 233, 1760, 305)  # 储值电卡文本
    ITEM_LIST = (454, 220, 1794, 939)  # 道具列表区域