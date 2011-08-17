from pmr2.app.workspace.browser.interfaces import *


class RendererDictionary(object):

    zope.interface.implements(IRendererDictionary)

    def match(self, data):
        mimetype = data['mimetype']()
        if mimetype and data['file'].endswith('reference-description.json'):
            return 'cellml_simulator_link'

        return None
