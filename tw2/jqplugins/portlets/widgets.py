
# tw2-proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# imports from this package
from tw2.jqplugins.ui import base as uibase
from tw2.jqplugins.portlets import base as portletsbase
import tw2.jqplugins.ui



class Column(uibase.JQueryUIWidget, twc.DisplayOnlyWidget):
    template = "mako:tw2.jqplugins.portlets.templates.column"
    width = twc.Param(attribute=True)

    def prepare(self):
        self.resources.extend([
            portletsbase.jquery_portlets_css,
            portletsbase.jquery_portlets_js,
        ])
        super(Column, self).prepare()

class ColumnLayout(uibase.JQueryUIWidget, twc.DisplayOnlyWidget):
    template = "mako:tw2.jqplugins.portlets.templates.layout"
    width = twc.Param(attribute=True)

    def prepare(self):
        self.resources.extend([
            portletsbase.jquery_portlets_css,
            portletsbase.jquery_portlets_js,
        ])
        super(ColumnLayout, self).prepare()

class Portlet(uibase.JQueryUIWidget, twc.DisplayOnlyWidget):
    template = "mako:tw2.jqplugins.portlets.templates.portlet"

    title = twc.Param("Title of the portlet.  `str`")
    content = twc.Param("Content of the portlet.  Another widget, or `str`")

    def prepare(self):
        self.resources.extend([
            portletsbase.jquery_portlets_css,
            portletsbase.jquery_portlets_js,
        ])
        super(Portlet, self).prepare()

