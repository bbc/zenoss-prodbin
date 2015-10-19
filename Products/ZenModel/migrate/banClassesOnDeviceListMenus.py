##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2007, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


import Migrate

import Globals

import logging
log = logging.getLogger("zen.migrate")

from Products.ZenModel.ZenossSecurity import MANAGER_ROLE, MANAGE_NOTIFICATION_SUBSCRIPTIONS, MANAGE_TRIGGER, NOTIFICATION_SUBSCRIPTION_MANAGER_ROLE, NOTIFICATION_UPDATE_ROLE, NOTIFICATION_VIEW_ROLE, OWNER_ROLE, TRIGGER_MANAGER_ROLE, TRIGGER_UPDATE_ROLE, TRIGGER_VIEW_ROLE, UPDATE_NOTIFICATION, UPDATE_TRIGGER, VIEW_NOTIFICATION, VIEW_TRIGGER, ZEN_ADD, ZEN_ADMINISTRATORS_EDIT, ZEN_ADMINISTRATORS_VIEW, ZEN_ADMIN_DEVICE, ZEN_CHANGE_ADMIN_OBJECTS, ZEN_CHANGE_ALERTING_RULES, ZEN_CHANGE_DEVICE, ZEN_CHANGE_DEVICE_PRODSTATE, ZEN_CHANGE_EVENT_VIEWS, ZEN_CHANGE_SETTINGS, ZEN_COMMON, ZEN_DEFINE_COMMANDS_EDIT, ZEN_DEFINE_COMMANDS_VIEW, ZEN_DELETE, ZEN_DELETE_DEVICE, ZEN_EDIT_LOCAL_TEMPLATES, ZEN_EDIT_USER, ZEN_EDIT_USERGROUP, ZEN_MAINTENANCE_WINDOW_EDIT, ZEN_MAINTENANCE_WINDOW_VIEW, ZEN_MANAGER_ROLE, ZEN_MANAGE_DEVICE, ZEN_MANAGE_DEVICE_STATUS, ZEN_MANAGE_DMD, ZEN_MANAGE_EVENTMANAGER, ZEN_MANAGE_EVENTS, ZEN_RUN_COMMANDS, ZEN_SEND_EVENTS, ZEN_UPDATE, ZEN_USER_ROLE, ZEN_VIEW, ZEN_VIEW_HISTORY, ZEN_VIEW_MODIFICATIONS, ZEN_ZPROPERTIES_EDIT, ZEN_ZPROPERTIES_VIEW

class BanClassesOnDeviceListMenus(Migrate.Step):
    version = Migrate.Version(2, 1, 0)

    def cutover(self, dmd):  
        # Build menus
        dmd.buildMenus({
'Manage': [  
        {  'action': 'dialog_changeClass',
        'allowed_classes': ('Device', 'OperatingSystem'),
        'description': 'Change Class...',
        'id': 'changeClass',
        'isdialog': True,
        'ordering': 85.0,
        'permissions': (ZEN_ADMIN_DEVICE,) },
        {  'action': 'dialog_renameDevice',
        'allowed_classes': ('Device', 'OperatingSystem'),
        'description': 'Rename Device...',
        'id': 'renameDevice',
        'isdialog': True,
        'ordering': 30.0,
        'permissions': (ZEN_ADMIN_DEVICE,) },
        {  'action': 'dialog_deleteDevice',
        'allowed_classes': ('Device', 'OperatingSystem'),
        'description': 'Delete Device...',
        'id': 'deleteDevice',
        'isdialog': True,
        'ordering': 4.0,
        'permissions': (ZEN_ADMIN_DEVICE,) },
        {  'action': 'dialog_clearHeartbeats',
        'allowed_classes': ('Device', 'OperatingSystem'),
        'description': 'Clear Heartbeats...',
        'id': 'clearHeartbeats',
        'isdialog': True,
        'ordering': 5.0,
        'permissions': (ZEN_MANAGE_DEVICE,) },
        {  'action': 'dialog_resetIp',
        'allowed_classes': ('Device', 'OperatingSystem', 'DeviceClass',),
        'description': 'Reset IP...',
        'id': 'resetIp',
        'isdialog': True,
        'ordering': 50.0,
        'permissions': (ZEN_ADMIN_DEVICE,) },
        {  'action': 'collectDevice', 
        'allowed_classes': ( 'Device', 'OperatingSystem'), 
        'description': 'Model Device', 
        'id': 'modelDevice', 
        'ordering': 88.0, 
        'permissions': (ZEN_MANAGE_DEVICE,) },
        {  'action': 'dialog_lockDevices',
        'allowed_classes': ( 'DeviceClass',),
        'description': 'Lock Devices...',
        'id': 'lockDevices',
        'isdialog': True,
        'ordering': 86.0,
        'permissions': (ZEN_MANAGE_DEVICE,) },
        {  'action': 'manage_snmpCommunity',
        'allowed_classes': ( 'Device', 'OperatingSystem', 'DeviceClass',),
        'description': 'Reset Community',
        'id': 'resetCommunity',
        'ordering': 12.0,
        'permissions': (ZEN_MANAGE_DEVICE,) },
        {  'action': 'dialog_lock',
        'allowed_classes': [ 'Device',
                    'OperatingSystem',
                    'WinService',
                    'FileSystem',
                    'HardDisk',
                    'IpInterface',
                    'IpService',
                    'OSProcess',
                    'IpRouteEntry'],
        'description': 'Lock...',
        'id': 'lockObject',
        'isdialog': True,
        'ordering': 15.0,
        'permissions': (ZEN_MANAGE_DEVICE,) },
        {  'action': 'pushConfig',
        'allowed_classes': ['DeviceClass', 'Device'],
        'description': 'Push Changes',
        'id': 'pushConfig',
        'ordering': 10.0,
        'permissions': (ZEN_MANAGE_DEVICE,) },
        {  'action': '../pushConfig',
        'allowed_classes': ['OperatingSystem'],
        'description': 'Push Changes',
        'id': 'pushConfig_os',
        'ordering': 10.0,
        'permissions': (ZEN_MANAGE_DEVICE,) } ], 
'Device_list': [  
        {  'action': 'dialog_setProductionState',
        'banned_classes': ['Monitor'],
        'description': 'Set Production State...',
        'id': 'setProductionState',
        'isdialog': True,
        'ordering': 80.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setPriority',
        'banned_classes': ['Monitor'],
        'description': 'Set Priority...',
        'id': 'setPriority',
        'isdialog': True,
        'ordering': 70.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_moveDevices',
        'banned_classes': ['Monitor'],
        'description': 'Move to Class...',
        'id': 'moveclass',
        'isdialog': True,
        'ordering': 50.0,
        'permissions': (ZEN_ADMIN_DEVICE,) },
        {  'action': 'dialog_setGroups',
        'banned_classes': ['Monitor'],
        'description': 'Set Groups...',
        'id': 'setGroups',
        'isdialog': True,
        'ordering': 40.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setSystems',
        'banned_classes': ['Monitor'],
        'description': 'Set Systems...',
        'id': 'setSystems',
        'isdialog': True,
        'ordering': 30.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setLocation',
        'banned_classes': ['Monitor'],
        'description': 'Set Location...',
        'id': 'setLocation',
        'isdialog': True,
        'ordering': 20.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setPerformanceMonitor',
        'banned_classes': ['StatusMonitorConf'],
        'description': 'Set Perf Monitor...',
        'id': 'setPerformanceMonitor',
        'isdialog': True,
        'ordering': 15.0,
        'permissions': (ZEN_MANAGE_DMD,) },
        {  'action': 'dialog_removeDevices',
        'description': 'Delete devices...',
        'id': 'removeDevices',
        'isdialog': True,
        'ordering': 10.0,
        'permissions': (ZEN_ADMIN_DEVICE,) },
        {  'action': 'dialog_lockDevices',
        'banned_classes': ['Monitor'],
        'description': 'Lock devices...',
        'id': 'lockDevices',
        'isdialog': True,
        'ordering': 2.0,
        'permissions': (ZEN_MANAGE_DEVICE,) },
        {  'action': 'dialog_setStatusMonitors',
        'banned_classes': ['PerformanceConf'],
        'description': 'Set Status Monitors...',
        'id': 'setStatusMonitors',
        'isdialog': True,
        'ordering': 11.0,
        'permissions': (ZEN_MANAGE_DMD,) } ],
'DeviceGrid_list': [
        {  'action': 'dialog_setProductionState_grid',
        'description': 'Set Production State...',
        'id': 'setProductionState_grid',
        'isdialog': True,
        'ordering': 80.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setPriority_grid',
        'description': 'Set Priority...',
        'id': 'setPriority',
        'isdialog': True,
        'ordering': 70.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_moveDevices_grid',
        'description': 'Move to Class...',
        'id': 'moveclass_grid',
        'isdialog': True,
        'ordering': 50.0,
        'permissions': (ZEN_ADMIN_DEVICE,) },
        {  'action': 'dialog_setGroups_grid',
        'description': 'Set Groups...',
        'id': 'setGroups_grid',
        'isdialog': True,
        'ordering': 40.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setSystems_grid',
        'description': 'Set Systems...',
        'id': 'setSystems_grid',
        'isdialog': True,
        'ordering': 30.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setLocation_grid',
        'description': 'Set Location...',
        'id': 'setLocation_grid',
        'isdialog': True,
        'ordering': 20.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setPerformanceMonitor_grid',
        'description': 'Set Perf Monitor...',
        'id': 'setPerformanceMonitor_grid',
        'isdialog': True,
        'ordering': 15.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_removeDevices_grid',
        'description': 'Delete devices...',
        'id': 'removeDevices_grid',
        'isdialog': True,
        'ordering': 10.0,
        'permissions': (ZEN_ADMIN_DEVICE,) },
        {  'action': 'dialog_lockDevices_grid',
        'description': 'Lock devices...',
        'id': 'lockDevices_grid',
        'isdialog': True,
        'ordering': 2.0,
        'permissions': (ZEN_MANAGE_DEVICE,) } ],   
'Edit': [  
        {  'action': 'dialog_setProductionState_global',
        'allowed_classes': ( 'DeviceClass',
            'DeviceGroup',
            'Location',
            'System'),
        'description': 'Set Production State...',
        'id': 'setProductionState',
        'isdialog': True,
        'ordering': 80.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setPriority_global',
        'allowed_classes': ( 'DeviceClass',
            'DeviceGroup',
            'Location',
            'System'), 
        'description': 'Set Priority...',
        'id': 'setPriority',
        'isdialog': True,
        'ordering': 70.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setGroups_global',
        'allowed_classes': ( 'DeviceClass',
            'DeviceGroup',
            'Location',
            'System'), 
        'description': 'Set Groups...',
        'id': 'setGroups',
        'isdialog': True,
        'ordering': 40.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setSystems_global',
        'allowed_classes': ( 'DeviceClass',
            'DeviceGroup',
            'Location',
            'System'),  
        'description': 'Set Systems...',
        'id': 'setSystems',
        'isdialog': True,
        'ordering': 30.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action': 'dialog_setLocation_global',
        'description': 'Set Location...',
        'allowed_classes': ( 'DeviceClass',
            'DeviceGroup',
            'Location',
            'System'),  
        'id': 'setLocation',
        'isdialog': True,
        'ordering': 20.0,
        'permissions': (ZEN_CHANGE_DEVICE,) },
        {  'action':'dialog_setPerformanceMonitor_global',
        'description': 'Set Perf Monitor...',
        'id': 'setPerformanceMonitor',
        'allowed_classes': ( 'DeviceClass',
            'DeviceGroup',
            'Location',
            'System'),
        'isdialog': True,
        'ordering': 15.0,
        'permissions': (ZEN_CHANGE_DEVICE,) } ], 
'More': [ {  'action': 'viewHistory',
        'allowed_classes': ['Device', 
            'System', 
            'DeviceGroup', 
            'Location', 
            'DeviceClass',
            'EventClass'], 
        'description': 'Modifications',
        'id': 'viewHistory',
        'ordering': 2.0,
        'permissions': (ZEN_VIEW_HISTORY,) }, 
        {  'action': '../viewHistory',
        'allowed_classes': ['OperatingSystem'],
        'description': 'Modifications',
        'id': 'viewHistory_os',
        'ordering': 2.0,
        'permissions': (ZEN_VIEW_HISTORY,) },
        {  'action'        : 'editEventClassTransform',
        'id'            : 'transform',
        'allowed_classes': ['EventClass'],
        'description': 'Transform',
        'ordering': 2.1,
        'permissions'   : (ZEN_CHANGE_DEVICE,) }, 
        {  'action': 'zSortableProperty?prop=zCollectorPlugins',
        'allowed_classes': ['Device', 'DeviceClass'],
        'description': 'Collector Plugins',
        'id': 'collectorPlugins',
        'ordering': 20.0,
        'permissions': (ZEN_ZPROPERTIES_VIEW,) },
        {  'action': 'zPropertyEdit',
        'allowed_classes': [ 'Device',],
        'description': 'zProperties',
        'id': 'zPropertyEdit',
        'ordering': 85.0,
        'permissions': (ZEN_ZPROPERTIES_VIEW,) },
        {  'action': '../zPropertyEdit',
        'allowed_classes': ['OperatingSystem'],
        'description': 'zProperties',
        'id': 'zPropertyEdit_os',
        'ordering': 85.0,
        'permissions': (ZEN_ZPROPERTIES_VIEW,) },
        {  'action': 'deviceManagement',
        'allowed_classes': ['Device', 'DeviceClass'],
        'description': 'Administration',
        'id': 'deviceManagement',
        'ordering': 50.0,
        'permissions': (ZEN_MANAGE_DEVICE,) },
        {  'action': '../deviceManagement',
        'allowed_classes': ['OperatingSystem'],
        'description': 'Administration',
        'id': 'deviceManagement_os',
        'ordering': 50.0,
        'permissions': (ZEN_MANAGE_DEVICE,) },
        {  'action': 'zPropOverridden',
        'allowed_classes': ['DeviceClass', 'EventClass'],
        'description': 'Overridden Objects',
        'id': 'overriddenObjects',
        'ordering': 21.0,
        'permissions': (ZEN_ZPROPERTIES_VIEW,) } ], 
        })

BanClassesOnDeviceListMenus()
