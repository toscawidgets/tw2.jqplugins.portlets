"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import tw2.core as twc
import tw2.forms as twf
from widgets import Column, ColumnLayout, Portlet


class DemoLayout(ColumnLayout):
    width='900px'

    class col1(Column):
        width='300px'
        class portlet(Portlet):
            title = "Two widgets in a portlet"
            one_widget = twf.Label(text='Some content in a label widget')
            another_widget = twf.Label(text='Some other content in a label')
        
        class whatever(Portlet):
            title = "One widget in a portlet"
            widgetry = twf.Label(text='Some content in a label widget')

    class col2(Column):
        width='300px'
        class portlet(Portlet):
            title = "Another portlet with only one widget"
            widgetry = twf.Label(text='Some content in a label widget')

    class col3(Column):
        width='300px'
        class portlet(Portlet):
            title = "A portlet with a whole form in it.. whoah."
            class Form(twf.TableForm):
                title = twf.TextField(validator=twc.Required)
                director = twf.TextField()
                genre = twf.CheckBoxList(
                    options=['Action', 'Comedy', 'Romance', 'Sci-fi'])
                class cast(twf.GridLayout):
                    extra_reps = 5
                    character = twf.TextField()
