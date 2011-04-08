import os.path
import zope.component

from paste.httpexceptions import HTTPNotFound
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserPage
from plone.z3cform import layout

from pmr2.app.browser.layout import TraverseFormWrapper
from pmr2.app.browser.page import TraversePage

from cellml.simulator.layout import CellMLSimulatorIFrameWrapper


path = lambda p: os.path.join(os.path.dirname(__file__), 'template', p)


class CellMLSimulatorFullView(TraversePage):
    """\
    The source text viewer class.
    """

    template = ViewPageTemplateFile(path('dojo_template.pt'))
    default_json_name = 'reference-description.json'

    @property
    def target_view(self):
        # This can change in the future.
        return 'rawfile'

    @property
    def url_expr_json(self):
        return '/'.join((self.context.absolute_url(), self.target_view) +
                        tuple(self.traverse_subpath))

    def update(self):
        base, filename = self.url_expr_json.rsplit('/', 1)
        if not filename == self.default_json_name:
            # this view is not applicable)
            raise HTTPNotFound(filename)
        # javascript code for the renderer does not compensate for the
        # lack of trailing slash.
        self.srcBaseURL = base + '/'

    def render(self):
        return self.template()


class CellMLSimulatorIFrame(CellMLSimulatorFullView):
    """\
    The one with the site theme, embedding the full view as an iframe.
    """

    template = ViewPageTemplateFile(path('dojo_iframe.pt'))
    fullview_name = 'cellml_simulator_full'

    @property
    def url_expr_target(self):
        return '/'.join((self.context.absolute_url(), self.fullview_name) +
                        tuple(self.traverse_subpath))

CellMLSimulatorIFrameView = layout.wrap_form(CellMLSimulatorIFrame,
    __wrapper_class=CellMLSimulatorIFrameWrapper)
