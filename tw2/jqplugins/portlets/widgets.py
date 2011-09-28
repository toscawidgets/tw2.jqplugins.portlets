
# tw2-proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# imports from this package
from tw2.jqplugins.ui import base as uibase
from tw2.jqplugins.cookies import base as cookiesbase
from tw2.jqplugins.portlets import base as portletsbase
import tw2.jqplugins.ui



class Column(uibase.JQueryUIWidget, twc.CompoundWidget):
    template = "mako:tw2.jqplugins.portlets.templates.column"
    width = twc.Param(attribute=True, default='100%')

    def prepare(self):
        self.resources.extend([
            portletsbase.jquery_portlets_css,
            portletsbase.jquery_portlets_js,
        ])
        super(Column, self).prepare()

class ColumnLayout(uibase.JQueryUIWidget, twc.CompoundWidget):
    template = "mako:tw2.jqplugins.portlets.templates.layout"
    width = twc.Param(attribute=True, default='100%')
    cookies = twc.Param('Boolean.  Use cookies to restore/save order?',
                        default=True)

    def prepare(self):
        self.resources.extend([
            portletsbase.jquery_portlets_css,
            portletsbase.jquery_portlets_js,
        ])

        if self.cookies:
            self.resources.append(cookiesbase.jquery_cookies_js)

        super(ColumnLayout, self).prepare()

        if self.cookies:
            restore = twc.js_function('restoreOrder')()
            self.add_call(restore)

class Portlet(uibase.JQueryUIWidget, twc.CompoundWidget):
    template = "mako:tw2.jqplugins.portlets.templates.portlet"

    title = twc.Param("Title of the portlet.  `str`")

    def prepare(self):
        self.resources.extend([
            portletsbase.jquery_portlets_css,
            portletsbase.jquery_portlets_js,
        ])
        super(Portlet, self).prepare()

        # tw2.jqplugins.ui already escapes the selector for us but
        # twc.js_function escapes it for us EVEN more.  We gotta tone it down.
        less_escaped_selector = self.selector.replace('\\\\', '\\')
        setupCall = twc.js_function('makeIntoPortlet')(less_escaped_selector)
        self.add_call(setupCall)

