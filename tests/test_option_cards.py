from __future__ import annotations

from PySide6.QtWidgets import QWidget
from qfluentwidgets import RoundMenu

from app.client import profileFamilies, profileVersions
from app.view.components.option_cards import PROFILE_FAMILY_LABELS, buildProfileMenu


def test_profile_menu_builds_versions_on_demand(qapp):
    """137 个版本不能在建菜单时全部建完，展开对应子菜单再补。"""
    parent = QWidget()
    menu = buildProfileMenu(parent, lambda value: None)

    family = profileFamilies()[0]
    submenu = next(
        m for m in parent.findChildren(RoundMenu)
        if m is not menu and m.title() == PROFILE_FAMILY_LABELS[family]
    )
    assert len(submenu.actions()) == 1

    submenu.aboutToShow.emit()

    assert len(submenu.actions()) == 1 + len(profileVersions(family))
