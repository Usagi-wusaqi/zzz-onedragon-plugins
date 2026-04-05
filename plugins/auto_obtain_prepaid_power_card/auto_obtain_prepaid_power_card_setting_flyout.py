from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from one_dragon.utils.i18_utils import gt
from one_dragon_qt.utils.config_utils import get_prop_adapter
from one_dragon_qt.widgets.column import Column
from one_dragon_qt.widgets.setting_card.editable_combo_box_setting_card import EditableComboBoxSettingCard
from one_dragon_qt.widgets.setting_card.switch_setting_card import SwitchSettingCard
from . import auto_obtain_prepaid_power_card_const
from ..auto_obtain_prepaid_power_card_config import (
    AutoObtainPrepaidPowerCardConfig, OutpostLogisticsObtainNumber, MonthlyRestockObtainNumber, FadingSignalObtainNumber
)


if TYPE_CHECKING:
    from zzz_od.context.zzz_context import ZContext


class AutoObtainPrepaidPowerCardDialog(AppSettingFlyout):

    def _setup_ui(self, layout) -> None:

        self.outpost_logistics = SwitchSettingCard(icon=FluentIcon.SHOPPING_CART, title='后勤商店')
        self.outpost_logistics.value_changed.connect(self._on_outpost_logistics_toggled)
        layout.add_widget(self.outpost_logistics)

        self.outpost_logistics_obtain_number = EditableComboBoxSettingCard(
            icon=FluentIcon.GAME, title=gt('后勤商店获取数量'),
            options_enum=OutpostLogisticsObtainNumber,
        )
        layout.add_widget(self.outpost_logistics_obtain_number)

        self.monthly_restock = SwitchSettingCard(icon=FluentIcon.SHOPPING_CART, title='情报板商店')
        self.monthly_restock.value_changed.connect(self._on_monthly_restock_toggled)
        layout.add_widget(self.monthly_restock)

        self.monthly_restock_obtain_number = EditableComboBoxSettingCard(
            icon=FluentIcon.GAME, title=gt('情报板商店获取数量'),
            options_enum=MonthlyRestockObtainNumber,
        )
        layout.add_widget(self.monthly_restock_obtain_number)

        self.fading_signal = SwitchSettingCard(icon=FluentIcon.SHOPPING_CART, title='信号残响')
        self.fading_signal.value_changed.connect(self._on_signal_shop_toggled)
        layout.add_widget(self.fading_signal)

        self.fading_signal_obtain_number = EditableComboBoxSettingCard(
            icon=FluentIcon.GAME, title=gt('信号残响获取数量'),
            options_enum=FadingSignalObtainNumber,
        )
        layout.add_widget(self.fading_signal_obtain_number)


    def init_config(self) -> None:
        config: AutoObtainPrepaidPowerCardConfig = self.ctx.run_context.get_config(
            app_id=auto_obtain_prepaid_power_card_const.APP_ID,
            instance_idx=self.ctx.current_instance_idx,
            group_id=self.group_id,
        )
        self.outpost_logistics.init_with_adapter(get_prop_adapter(config, 'outpost_logistics'))
        self.outpost_logistics_obtain_number.init_with_adapter(get_prop_adapter(config, 'outpost_logistics_obtain_number'))
        self.monthly_restock.init_with_adapter(get_prop_adapter(config, 'monthly_restock'))
        self.monthly_restock_obtain_number.init_with_adapter(get_prop_adapter(config, 'monthly_restock_obtain_number'))
        self.fading_signal.init_with_adapter(get_prop_adapter(config, "fading_signal"))
        self.fading_signal_obtain_number.init_with_adapter(get_prop_adapter(config, "fading_signal_obtain_number"))

        # 初始化时根据当前配置设置可用性
        self._on_outpost_logistics_toggled(config.outpost_logistics)
        self._on_monthly_restock_toggled(config.monthly_restock)
        self._on_signal_shop_toggled(config.fading_signal)

    def _on_outpost_logistics_toggled(self, checked: bool) -> None:
        # 如果开启后勤商店自动购买储值电卡 启用相关控件 否则禁用
        self.outpost_logistics_obtain_number.setEnabled(checked)

    def _on_monthly_restock_toggled(self, checked: bool) -> None:
        # 如果开启情报板商店自动购买储值电卡 启用相关控件 否则禁用
        self.monthly_restock_obtain_number.setEnabled(checked)

    def _on_signal_shop_toggled(self, checked: bool) -> None:
        # 如果开启信号残响自动购买储值电卡 启用相关控件 否则禁用
        self.fading_signal_obtain_number.setEnabled(checked)