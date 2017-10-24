from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView

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

from controller.ClienteController import ClienteScreen
from controller.FuncionarioController import FuncionarioScreen
from controller.ProdutoController import ProdutoScreen
from controller.ServicoController import ServicoScreen
from controller.EnderecoController import EnderecoScreen


class ScreenManagement(ScreenManager):
    pass


class HypnosApp(App):
    title = 'Hypnos - Software de Gestão Hoteleira'
    theme_cls = ThemeManager()
    theme_cls.theme_style = 'Dark'
    theme_cls.primary_palette = 'Yellow'

    def build(self):
        pass

if __name__ == "__main__":
    HypnosApp().run()
