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

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, mapper

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database

_url = 'sqlite:///database.db'

# cria o engine e o declarative_base
engine = create_engine(_url, echo=True)

Base = declarative_base(bind=engine)


class HypnosApp(App):
    title = 'Hypnos - Software de Gestão Hoteleira'
    theme_cls = ThemeManager()

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Yellow'
#        manager = ScreenManager()
#        manager.add_widget(Dashboard(name='dashboard'))
#        return manager

    def show_example_bottom_sheet(self):
        bs = MDListBottomSheet()
        bs.add_item("Here's an item with text only", lambda x: x)
        bs.add_item("Here's an item with an icon", lambda x: x,
                    icon='clipboard-account')
        bs.add_item("Here's another!", lambda x: x, icon='nfc')
        bs.open()

    def show_example_grid_bottom_sheet(self):
        bs = MDGridBottomSheet()
        bs.add_item("Facebook", lambda x: x,
                    icon_src='./assets/facebook-box.png')
        bs.add_item("YouTube", lambda x: x,
                    icon_src='./assets/youtube-play.png')
        bs.add_item("Twitter", lambda x: x,
                    icon_src='./assets/twitter.png')
        bs.add_item("Da Cloud", lambda x: x,
                    icon_src='./assets/cloud-upload.png')
        bs.add_item("Camera", lambda x: x,
                    icon_src='./assets/camera.png')
        bs.open()

    pass


if __name__ == '__main__':
    if database_exists(engine.url):
        Base.metadata.drop_all()
    # cria as tabelas no banco (caso nao existam)
    Base.metadata.create_all()

    # configure Session class with desired options
    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()

#    pessoa = Pessoa('Cicrano')
#    session.add(pessoa)
#    session.commit()

    HypnosApp().run()
