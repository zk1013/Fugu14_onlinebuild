# This Repo is forked from LinusHenze/Fugu14. I modified some so that it can use codemagic to online build and you dont need to install local XCODE.
# DO IT AT YOUR OWN RISK. DO NOT ABUSE USE THE PLATFORM
# Requirement
- A mac (Yes yes I know. Though most of the processes are done online, this tutorial still require a mac environment to install. So please use VM or Hackintosh if you are Windows/Linux)
- VNC client
- Download ipsw, it should match your device and ios version
- extract ipsw, extract the largest dmg, obtain the **[dmg_root]/Applications/Spotlight.app/Spotlight** file, upload it to **[your_forked_repo]/tools/**
- DONT USE SSH TO BUILD, IT WILL FAIL BECAUSE THE KEYCHAIN WONT UNLOCK USING SSH.
# Shall we start?
- Fork this repo.
- Login https://codemagic.io/start/ with your github account, you can bind the forked repo to the apps for quick start.
- Start a build, it will be halted up until you mkdir DONE under ~/clone. Before continue, you should config everything properly.
- VNC to the Remote server.
- Open Finder, navigate to **~/clone/arm/iOS/Fugu14App/**, open **Fugu14App.xcodeproj**
- In Xcode, click Fugu14 on the left-side panel(top-most item of the tree view). In the middle pannel, click **Signing & Capabilities**. You will notice there are errors about signing.
- Click team, add team, login with your Apple id.
- Change the bundle name with a random one, Xcode will automatically generate a free provision.
- If no warnings or errors, close xcode. Open terminal.
- In terminal, run **security find-identity**, note down the long Hex value of your certificate(usually only one)
- In your github, do the following:
- modify the ios_install.py line 29 csIdentity = "[long Hex value of your certificate]", commit changes.
- make a dir called DONE in the root of repo
- return back to the remote VNC, in the terminal, cd clone
- git pull
- Then cross your finger, one the compile is done, there will be two .ipa file.
# Fugu14 - Untethered iOS 14 Jailbreak

Fugu14 is an (incomplete) iOS 14 Jailbreak, including an untether (persistence), kernel exploit, kernel PAC bypass and PPL bypass.
The CVE numbers of the vulnerabilities are: CVE-2021-30740, CVE-2021-30768, CVE-2021-30769, CVE-2021-30770 and CVE-2021-30773.

# Supported Devices/iOS Versions

Fugu14 *should* support all arm64e devices (iPhone XS and newer) on iOS 14.3 - 14.5.1.  
Support for lower versions (down to 14.2) can be added by editing `arm/shared/ClosurePwn/Sources/ClosurePwn/PwnClosure.swift` and `arm/shared/KernelExploit/Sources/KernelExploit/offsets.swift`.  

arm64 devices are not supported because the exploit to install the Fugu14 App does not work on these devices.  
However, it is in theory possible to install the untether on them (e.g. via checkra1n).  
Note that all of this code was written specifically for arm64e, so some changes are required to add arm64 support to the untether.

# Features

- The kernel exploit is extremely reliable (it will never trigger a kernel panic)
- A simple TCP shell is available on port 1337
- Trustcaches put in `/.Fugu14Untether/trustcaches/` will be loaded automatically
- Executables put in `/.Fugu14Untether/autorun/` will be launched during boot (make sure to also create a trust cache for your executable!)
- Supports [Siguza's](https://twitter.com/s1guza) [libkrw](https://github.com/Siguza/libkrw) library (load `/usr/lib/libkrw/libFugu14Krw.dylib` and call `krw_initializer`)
- (Jailbreak Developers: You can make your jailbreak untethered just by creating a CLI version that supports libkrw, copying it to `/.Fugu14Untether/autorun/` and writing a trust cache to `/.Fugu14Untether/trustcaches/`)

# WARNING

- Messing around with the untether may BOOTLOOP your device
- The fast untether (disabled unless you edit the source code) HAS NOT BEEN TESTED ON A REAL DEVICE -- DO NOT USE IT
- Additionally, the fast untether (in case it actually works) is more UNSAFE than the "slow" untether
- Developers: PLEASE TEST ANY CHANGES YOU MAKE TO THE UNTETHER ON A VIRTUAL DEVICE FIRST

# Building and Running

Requirements:
- You need a supported device running a supported iOS version (see above)
- The device must be connected via USB
- You need the IPSW for your device, *unzipped*
- You need to have Xcode installed
- You need to have iproxy and ideviceinstaller installed (brew install usbmuxd ideviceinstaller)

To build and run the iOS Jailbreak, all you have to do is run the `ios_install.py` script and follow the instructions.
In case you get a code signing error, open `arm/iOS/Fugu14App/Fugu14App.xcodeproj` and edit the code signing options.

# Recovery

So you didn't read the warning section and your device is now in a bootloop. Let's hope you didn't enable the fast untether.  
Anyway, before updating your device to the latest iOS version, try the following first:

1. Install irecovery on your computer
2. Connect your device via USB and boot into the recovery mode
3. Run `irecovery -s` on your computer, then enter the following commands:
- setenv boot-args no_untether
- saveenv
- reboot
4. Your device should now boot again. If it doesn't, repeat step two again, run `irecovery -s` and then enter these commands:
- setenv boot-args untether_force_restore
- saveenv
- reboot
5. Device still won't boot? Then you'll have to update it to the latest version unfortunately :/

# Credits

Like most software, Fugu14 contains (derived) code which was written by others.  
I would therefore like to thank the people below for open-sourcing their code:

- [Samuel Groß](https://twitter.com/5aelo): SLOP technique (as used in the dyld exploit) and the JavaScript Int64 library (+ utils)

Currently, the remount patch has copyright issues which I'm trying to resolve ASAP. Apparently, multiple parties think the code is theirs so I don't know what to do right now. I just write this here and hope no one DMCA's me.

Fugu14 also includes various header files from Apple.  

For more information, please see credits.txt.

# License

Fugu14 is released under the MIT license. Please see the `LICENSE` file for more information.
