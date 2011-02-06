
# TW2 proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# tw2.jquery core imports
from tw2.jquery.base import jQueryJSLink, jQueryPluginLinkMixin
from tw2.jquery.version import JSLinkMixin

# import from *this* package
from tw2.jqplugins.portlets import defaults

### Links, etc...
class jQueryPortletsMixin(jQueryPluginLinkMixin):
    dirname = defaults._portlets_dirname_
    basename='portlets'
    modname = 'tw2.jqplugins.portlets'

class jQueryPortletsJSLink(twc.JSLink, jQueryPortletsMixin):
    subdir = 'js'

class jQueryPortletsCSSLink(jQueryPortletsMixin, twc.CSSLink):
    subdir = 'css'
    extension = 'css'

### Resources
jquery_js = jQueryJSLink()
jquery_portlets_css = jQueryPortletsCSSLink()
jquery_portlets_js = jQueryPortletsJSLink()
