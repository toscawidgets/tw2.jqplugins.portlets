"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import tw2.forms as twf
from widgets import Column, ColumnLayout, Portlet


class DemoLayout(ColumnLayout):
    width='600px'

    class col1(Column):
        width='200px'
        class portlet1(Portlet):
            title = "Some title"
            content = "Some content"
        
        class portlet2(Portlet):
            title = "Some title"
            content = "Some content"

    class col2(Column):
        width='200px'
        class portlet3(Portlet):
            title = "Some title"
            content = "Some content"

    class col3(Column):
        width='200px'

        class portlet4(Portlet):
            title = "Some title"
            content = "Some content"
