import os.path
import zope.interface

from plone.z3cform.templates import ZopeTwoFormTemplateFactory
from plone.z3cform.interfaces import IFormWrapper

from pmr2.app.browser.layout import FormWrapper
from pmr2.app.browser.layout import TraverseFormWrapper

path = lambda p: os.path.join(os.path.dirname(__file__), 'template', p)


class IDojoLayoutWrapper(IFormWrapper):
    """
    The interface for the CellML Simulator dojo layout wrapper.
    """

dojo_layout_factory = ZopeTwoFormTemplateFactory(
    path('dojo_layout.pt'), form=IDojoLayoutWrapper)


class DojoLayoutWrapper(FormWrapper):
    """\
    The wrapper itself.
    """
    zope.interface.implements(IDojoLayoutWrapper)


class ICellMLSimulatorIFrameWrapper(IFormWrapper):
    """
    The interface for the CellML Simulator dojo iframe layout wrapper.
    """

cellml_simulator_iframe_layout_factory = ZopeTwoFormTemplateFactory(
    path('dojo_iframe_layout.pt'), form=ICellMLSimulatorIFrameWrapper)


class CellMLSimulatorIFrameWrapper(TraverseFormWrapper):
    """\
    The wrapper itself.
    """
    zope.interface.implements(ICellMLSimulatorIFrameWrapper)
