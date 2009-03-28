from Products.CMFCore.utils import getToolByName

def importVarious(context):
    """
    Final PFGDataGrid import steps.
    """
    # Only run step if a flag file is present (e.g. not an extension profile)
    if context.readDataFile('pfgdatagrid-various.txt') is None:
        return
    out = []
    site = context.getSite()
