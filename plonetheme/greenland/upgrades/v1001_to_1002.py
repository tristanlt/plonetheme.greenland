from Products.CMFCore.utils import getToolByName

def upgrade_1001_to_1002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile('profile-plonetheme.greenland:default',
                                   'jsregistry', run_dependencies=False,
                                   purge_old=False)
