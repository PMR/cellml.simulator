import os.path
import zope.component

from paste.httpexceptions import HTTPNotFound
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserPage

from pmr2.app.browser.page import TraversePage
from pmr2.app.workspace.browser.browser import BaseFilePage

path = lambda p: os.path.join(os.path.dirname(__file__), 'template', p)


class CellMLSimulatorFull(TraversePage):
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


class CellMLSimulatorIFrame(TraversePage):
    """\
    The one with the site theme, embedding the full view as an iframe.
    """

    index = ViewPageTemplateFile(path('dojo_iframe_layout.pt'))
    template = ViewPageTemplateFile(path('dojo_iframe.pt'))
    fullview_name = 'cellml_simulator_full'

    @property
    def url_expr_target(self):
        return '/'.join((self.context.absolute_url(), self.fullview_name) +
                        tuple(self.traverse_subpath))


class CellMLSimulatorIFrameLink(BaseFilePage):
    """\
    The one with the site theme, embedding the full view as an iframe.
    """

    template = ViewPageTemplateFile(path('dojo_iframe_link.pt'))
    fullview_name = 'cellml_simulator'

    @property
    def url_expr_target(self):
        return '/'.join((self.context.absolute_url(), self.fullview_name) +
                        tuple(self.traverse_subpath))
