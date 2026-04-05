from enum import Enum


class EtherBatteryCoordinate(Enum):
    """电池合成坐标枚举类"""
    TAB_MATERIALS = (1605, 124, 1676, 212)       # "材料道具"标签页区域
    TEXT_ETHER_BATTERY = (1405, 191, 1574, 253)  # "以太电池"文本区域
    IMG_PREPAID_CARD = (1371, 651, 1525, 805)    # 储值电卡图像
    TEXT_PREPAID_CARD = (732, 338, 787, 371)     # 储值电卡数量文本
    TEXT_ITEM_PROCESS = (161, 900, 311, 962)     # "道具处理"文本区域
    BTN_SYNTHESIS = (1655, 1006, 1740, 1050)     # "合成"按钮区域
    BTN_CONFIRM = (806, 685, 1120,773)           # "确认"按钮区域
    BTN_INCREASE = (1763, 430, 1843, 513)        # "增加"按钮区域

class HifiMasterCoordinate(Enum):
    """母盘合成坐标枚举类"""
    TEXT_SYNTHESIS = (82, 897, 167, 938)              # "合成"文本区域
    BTN_SYNTHESIS = (74, 825, 168, 910)               # "合成"按钮区域
    BTN_ONE_CLICK_SYNTHESIS = (1110, 721, 1421, 828) # "一键合成"按钮区域
    BTN_CONFIRM = (913, 683, 1038, 770)              # "确认"按钮区域
    TEXT_INSUFFICIENT_MATERIAL = (1475, 911, 1601, 935) # "合成素材不足"文本区域
