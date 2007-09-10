###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2007, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
""" Portal class

$Id: ZentinelPortal.py,v 1.17 2004/04/08 15:35:25 edahl Exp $
"""

import os

import Globals

from AccessControl.User import manage_addUserFolder
from AccessControl import getSecurityManager

from Products.Sessions.BrowserIdManager import constructBrowserIdManager
from Products.Sessions.SessionDataManager import constructSessionDataManager

from Products.CMFCore.PortalObject import PortalObjectBase
from Products.CMFCore import PortalFolder
from Products.CMFCore.utils import getToolByName

from Products.ZenUtils import Security

from ZenossSecurity import *


class ZentinelPortal ( PortalObjectBase ):
    """
    The *only* function this class should have is to help in the setup
    of a new ZentinelPortal. It should not assist in the functionality at all.
    """
    meta_type = 'ZentinelPortal'

    _properties = (
        {'id':'title', 'type':'string'},
        {'id':'description', 'type':'text'},
        )
    title = ''
    description = ''

    def __init__( self, id, title='' ):
        PortalObjectBase.__init__( self, id, title )


    def isManager(self, obj=None):
        """
        Return true if user is authenticated and has Manager role.
        """
        user = self.dmd.ZenUsers.getUser()
        if user: 
            return user.has_role(("Manager", ZEN_MANAGER_ROLE), obj)


    def has_role(self, role, userid=None, obj=None):
        """Check to see of a user has a role.
        """
        user = self.dmd.ZenUsers.getUser(userid)
        if user: return user.has_role(role, obj)


    def has_permission(self, perm, userid=None, obj=None):
        """Check to see of a user has a permission.
        """
        user = self.dmd.ZenUsers.getUser(userid)
        if user: return user.has_permission(perm, obj)



Globals.InitializeClass(ZentinelPortal)


class PortalGenerator:

    klass = ZentinelPortal

    def setupTools(self, p):
        """Set up initial tools"""
        addCMFCoreTool = p.manage_addProduct['CMFCore'].manage_addTool
        addCMFCoreTool('CMF Skins Tool', None)


    def setupMailHost(self, p):
        p.manage_addProduct['MailHost'].manage_addMailHost(
            'MailHost', smtp_host='localhost')


    def setupUserFolder(self, p):
        #p.manage_addProduct['OFSP'].manage_addUserFolder()
        Security.createPASFolder(p)
        Security.setupPASFolder(p)


    def setupCookieAuth(self, p):
        # XXX PAS is handling this now, right?
        #p.manage_addProduct['CMFCore'].manage_addCC(
        #    id='cookie_authentication')
        pass


    def setupRoles(self, p):
        # Set up the suggested roles.
        p.__ac_roles__ += (ZEN_USER_ROLE, ZEN_MANAGER_ROLE,)


    def setupPermissions(self, p):
        # Set up some suggested role to permission mappings.
        mp = p.manage_permission
        mp(ZEN_CHANGE_SETTINGS, ['ZenManager', 'Owner','Manager',],     1)
        mp(ZEN_CHANGE_DEVICE, ['ZenManager', 'Owner','Manager',],     1)
        mp(ZEN_MANAGE_DMD, ['ZenManager', 'Owner','Manager',],     1)
        mp(ZEN_DELETE, [ZEN_MANAGER_ROLE, 'Owner','Manager',],     1)
        mp(ZEN_ADD, [ZEN_MANAGER_ROLE, 'Owner','Manager',],     1)
        mp('View',[ZEN_USER_ROLE,ZEN_MANAGER_ROLE,'Manager','Owner'])
        mp('View History',[ZEN_USER_ROLE, ZEN_MANAGER_ROLE, 'Manager',], 1)
        mp(ZEN_COMMON,[ZEN_USER_ROLE, ZEN_MANAGER_ROLE,'Manager', 'Owner'], 1)


    def setupDefaultSkins(self, p):
        from Products.CMFCore.DirectoryView import addDirectoryViews
        ps = getToolByName(p, 'portal_skins')
        addDirectoryViews(ps, 'skins', globals())
        ps.manage_addProduct['OFSP'].manage_addFolder(id='custom')
        ps.addSkinSelection('Basic', "custom, zenmodel", make_default=1)
        p.setupCurrentSkin()


    def setupSessionManager(self, p):
        """build a session manager and brower id manager for zport"""
        constructBrowserIdManager(p, cookiepath="/zport")
        constructSessionDataManager(p, "session_data_manager",
                    title="Session Data Manager",
                    path='/temp_folder/session_data')


    def setup(self, p, create_userfolder):
        if create_userfolder:
            self.setupUserFolder(p)
        #self.setupCookieAuth(p)
        self.setupTools(p)
        self.setupMailHost(p)
        self.setupRoles(p)
        self.setupPermissions(p)
        self.setupDefaultSkins(p)
        self.setupSessionManager(p)


    def create(self, parent, id, create_userfolder):
        id = str(id)
        portal = self.klass(id=id)
        parent._setObject(id, portal)
        # Return the fully wrapped object.
        p = parent.this()._getOb(id)
        self.setup(p, create_userfolder)
        return p


    def setupDefaultProperties(self, p, title, description,
                               email_from_address, email_from_name,
                               validate_email,
                               ):
        p._setProperty('email_from_address', email_from_address, 'string')
        p._setProperty('email_from_name', email_from_name, 'string')
        p._setProperty('validate_email', validate_email and 1 or 0, 'boolean')
        p.title = title
        p.description = description


manage_addZentinelPortal = Globals.HTMLFile('dtml/addPortal', globals())
manage_addZentinelPortal.__name__ = 'addPortal'

def manage_addZentinelPortal(self, id="zport", title='Zentinel Portal',
                         description='',
                         create_userfolder=True,
                         email_from_address='postmaster@localhost',
                         email_from_name='Portal Administrator',
                         validate_email=0, RESPONSE=None):
    '''
    Adds a portal instance.
    '''
    gen = PortalGenerator()
    from string import strip
    id = strip(id)
    p = gen.create(self, id, create_userfolder)
    gen.setupDefaultProperties(p, title, description,
                               email_from_address, email_from_name,
                               validate_email)
    if RESPONSE is not None:
        RESPONSE.redirect(self.absolute_url()+'/manage_main')
