import os
import win32api
import win32com.client
from win32com.client import constants as c


def get_user_name() -> str:
    """ユーザ名

    :return: ユーザ名
    :rtype: str
    """
    return os.getlogin()


def get_domain_name() -> str:
    """ドメイン名

    :return: ドメイン名
    :rtype: str
    """
    return win32api.GetDomainName()


if __name__ == '__main__':
    print(get_user_name())
    print(get_domain_name())

    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(".", "root\\cimv2")
    colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_ComputerSystem")
    print('')
    for objItem in colItems:
        print(f'AdminPasswordStatus: {objItem.AdminPasswordStatus}')
        print(f'AutomaticResetBootOption: {objItem.AutomaticResetBootOption}')
        print(f'AutomaticResetCapability: {objItem.AutomaticResetCapability}')
        print(f'BootOptionOnLimit: {objItem.BootOptionOnLimit}')
        print(f'BootOptionOnWatchDog: {objItem.BootOptionOnWatchDog}')
        print(f'BootROMSupported: {objItem.BootROMSupported}')
        print(f'BootupState: {objItem.BootupState}')
        print(f'Caption: {objItem.Caption}')
        print(f'ChassisBootupState: {objItem.ChassisBootupState}')
        print(f'CreationClassName: {objItem.CreationClassName}')
        print(f'CurrentTimeZone: {objItem.CurrentTimeZone}')
        print(f'DaylightInEffect: {objItem.DaylightInEffect}')
        print(f'Description: {objItem.Description}')
        print(f'DNSHostName: {objItem.DNSHostName}')
        print(f'Domain: {objItem.Domain}')
        print(f'DomainRole: {objItem.DomainRole}')
        print(f'EnableDaylightSavingsTime: {objItem.EnableDaylightSavingsTime}')
        print(f'FrontPanelResetStatus: {objItem.FrontPanelResetStatus}')
        print(f'InfraredSupported: {objItem.InfraredSupported}')
        print(f'InstallDate: {objItem.InstallDate}')
        print(f'KeyboardPasswordStatus: {objItem.KeyboardPasswordStatus}')
        print(f'LastLoadInfo: {objItem.LastLoadInfo}')
        print(f'Manufacturer: {objItem.Manufacturer}')
        print(f'Model: {objItem.Model}')
        print(f'Name: {objItem.Name}')
        print(f'NameFormat: {objItem.NameFormat}')
        print(f'NetworkServerModeEnabled: {objItem.NetworkServerModeEnabled}')
        print(f'NumberOfProcessors: {objItem.NumberOfProcessors}')
        print(f'PartOfDomain: {objItem.PartOfDomain}')
        print(f'PauseAfterReset: {objItem.PauseAfterReset}')
        print(f'PowerManagementSupported: {objItem.PowerManagementSupported}')
        print(f'PowerOnPasswordStatus: {objItem.PowerOnPasswordStatus}')
        print(f'PowerState: {objItem.PowerState}')
        print(f'PowerSupplyState: {objItem.PowerSupplyState}')
        print(f'PrimaryOwnerContact: {objItem.PrimaryOwnerContact}')
        print(f'PrimaryOwnerName: {objItem.PrimaryOwnerName}')
        print(f'ResetCapability: {objItem.ResetCapability}')
        print(f'ResetCount: {objItem.ResetCount}')
        print(f'ResetLimit: {objItem.ResetLimit}')
        print(f'Status: {objItem.Status}')
        print(f'SupportContactDescription: {objItem.SupportContactDescription}')
        print(f'SystemStartupDelay: {objItem.SystemStartupDelay}')
        print(f'SystemStartupSetting: {objItem.SystemStartupSetting}')
        print(f'SystemType: {objItem.SystemType}')
        print(f'ThermalState: {objItem.ThermalState}')
        print(f'TotalPhysicalMemory: {objItem.TotalPhysicalMemory}')
        print(f'UserName: {objItem.UserName}')
        print(f'WakeUpType: {objItem.WakeUpType}')
        print(f'Workgroup: {objItem.Workgroup}')
