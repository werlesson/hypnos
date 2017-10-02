# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker

main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar

NavigationLayout:
    id: nav_layout
    MDNavigationDrawer:
        id: nav_drawer
        NavigationDrawerToolbar:
            title: "Navigation Drawer"
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Accordion"
            on_release: app.root.ids.scr_mngr.current = 'accordion'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Bottom Navigation"
            on_release: app.root.ids.scr_mngr.current = 'bottom_navigation'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Bottom Sheets"
            on_release: app.root.ids.scr_mngr.current = 'bottomsheet'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Buttons"
            on_release: app.root.ids.scr_mngr.current = 'button'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Cards"
            on_release: app.root.ids.scr_mngr.current = 'card'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Dialogs"
            on_release: app.root.ids.scr_mngr.current = 'dialog'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Grid lists"
            on_release: app.root.ids.scr_mngr.current = 'grid'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Labels"
            on_release: app.root.ids.scr_mngr.current = 'labels'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Lists"
            on_release: app.root.ids.scr_mngr.current = 'list'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Menus"
            on_release: app.root.ids.scr_mngr.current = 'menu'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Navigation Drawer Widgets"
            on_release: app.root.ids.scr_mngr.current = 'nav_drawer'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Pickers"
            on_release: app.root.ids.scr_mngr.current = 'pickers'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Progress & activity"
            on_release: app.root.ids.scr_mngr.current = 'progress'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Progress bars"
            on_release: app.root.ids.scr_mngr.current = 'progressbars'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Selection controls"
            on_release: app.root.ids.scr_mngr.current = 'selectioncontrols'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Sliders"
            on_release: app.root.ids.scr_mngr.current = 'slider'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Snackbars"
            on_release: app.root.ids.scr_mngr.current = 'snackbar'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Tabs"
            on_release: app.root.ids.scr_mngr.current = 'tabs'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Text fields"
            on_release: app.root.ids.scr_mngr.current = 'textfields'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Themes"
            on_release: app.root.ids.scr_mngr.current = 'theming'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Toolbars"
            on_release: app.root.ids.scr_mngr.current = 'toolbar'

'''


class HypnosApp(App):

    # inserindo tema do KivyMD (Fundo já fica branco)
    theme_cls = ThemeManager()
    previous_date = ObjectProperty()
    # título que se localiza na borda superior da janela
    title = "Hypnos - Software Hoteleiro"

    def build(self):
        main_widget = Builder.load_string(main_widget_kv)

        return main_widget


hypnos = HypnosApp()
hypnos.run()
