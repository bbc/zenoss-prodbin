##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2007, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


import Migrate

from Products.ZenModel.ZenossSecurity import MANAGER_ROLE, ZEN_DELETE_DEVICE, ZEN_MANAGER_ROLE, ZEN_USER_ROLE


class DeleteDevicePermission(Migrate.Step):

    version = Migrate.Version(2, 5, 0)

    def cutover(self, dmd):
        dmd.zport.manage_permission(ZEN_DELETE_DEVICE,
                        [ZEN_USER_ROLE, ZEN_MANAGER_ROLE, MANAGER_ROLE], 1)


DeleteDevicePermission()
