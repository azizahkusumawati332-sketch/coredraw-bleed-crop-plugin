; Inno Setup Installer Script
; CorelDraw Bleed & Crop Plugin
; For CorelDraw 2024

#define MyAppName "Bleed & Crop Studio Pro"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "CorelDraw Plugins"
#define MyAppURL "https://github.com/azizahkusumawati332-sketch/coredraw-bleed-crop-plugin"
#define MyAppExeName "BleedCropStudio.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
AppId={{5A8F7B2C-9D3E-4F1A-B8C2-7E4D5F6A9B1C}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\CorelDraw\Plugins\BleedCropStudio
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=..\LICENSE
OutputDir=..\dist
OutputBaseFilename=BleedCropStudio-{#MyAppVersion}-Installer
SetupIconFile=..\docs\icon.ico
Compression=lz4
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\{#MyAppExeName}
VersionInfoVersion={#MyAppVersion}
VersionInfoCompany={#MyAppPublisher}
VersionInfoDescription={#MyAppName} for CorelDraw 2024

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "indonesian"; MessagesFile: "compiler:Languages\Indonesian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
Source: "..\src\*"; DestDir: "{app}\src"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\installer\requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\docs\*"; DestDir: "{app}\docs"; Flags: ignoreversion
Source: "..\LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\README.md"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    MsgBox('Bleed & Crop Studio Pro has been successfully installed!' + #13 +
           'Restart CorelDraw to activate the plugin.' + #13 + #13 +
           'Version: {#MyAppVersion}' + #13 +
           'Compatible: CorelDraw 2024',
           'Installation Complete', MB_OK + MB_ICONINFORMATION);
  end;
end;