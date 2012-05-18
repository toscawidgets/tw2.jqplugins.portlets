tw2.jqplugins.portlets
======================

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _jQuery UI: http://jqueryui.com/
.. _jQuery: http://jquery.com/

tw2.jqplugins.portlets is a `toscawidgets2 (tw2)`_ wrapper for jquery-ui portlets.  Its kind of like the widgets on the customized google homepage.

It was inspired by `this thread <http://groups.google.com/group/jquery-ui/browse_thread/thread/115a480bdd8bc549?pli=1>`_ on the jquery-ui mailing list.

Live Demo
---------
Peep the `live demonstration <http://tw2-demos.threebean.org/module?module=tw2.jqplugins.portlets>`_.

Links
-----
Get the `source from github <http://github.com/toscawidgets/tw2.jqplugins.portlets>`_.

`PyPI page <http://pypi.python.org/pypi/tw2.jqplugins.portlets>`_
and `bugs <http://github.com/toscawidgets/tw2.jqplugins.portlets/issues/>`_

Sampling tw2.jqplugins.portlets in the WidgetBrowser
----------------------------------------------------

The best way to scope out ``tw2.jqplugins.portlets`` is to load its widgets in the
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.jqplugins.portlets/tw2/jqplugins/portlets/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git://github.com/toscawidgets/tw2.jqplugins.portlets.git
    $ cd tw2.jqplugins.portlets
    $ mkvirtualenv tw2.jqplugins.portlets
    (tw2.jqplugins.portlets) $ pip install tw2.devtools
    (tw2.jqplugins.portlets) $ python setup.py develop
    (tw2.jqplugins.portlets) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.
