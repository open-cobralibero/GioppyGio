# -*- coding: UTF-8 -*-
# Written by Madhouse
_BH='networkid'
_BG='attachment; filename=GioppyGioLcn.zip'
_BF='Content-Disposition'
_BE='File setting ricevuto dal Plugin GioppyGio.'
_BD='WURcU1xDS3NWX1lYXR5bWEs='
_BC='WEVCX1pHUEdEQElURVdaXg=='
_BB='VlhfSEdfVVpeVVFeQUBBd0FfUlheFlJeXQ=='
_BA='description'
_B9='australia'
_B8='To be able to download the picons,\nchoose one of the 2 types\n(Sat or DTT) or both!'
_B7='Custom List: No'
_B6='Do you want to restart the GUI?'
_B5='opendroid'
_B4='openblackhole'
_B3='nonsolosat'
_B2='satdreamgr'
_B1='openeight'
_B0='openvision'
_A_='areadeltasat'
_Az='gioppygiohome'
_Ay='/etc/issue'
_Ax='/etc/opkg/all-feed.conf'
_Aw='The channel list (%s) was successfully sent.\nPlease be patient until I process it.\nYou will find it in to the list of settings.\nThank you and regards\n\nGioppyGio'
_Av='text_send'
_Au='uhf_vhf'
_At='DirectionActions'
_As='OkCancelActions'
_Ar='Close'
_Aq='I extract the picons %s'
_Ap='%d of %d kBytes (%.2f%%)'
_Ao='File download error!'
_An='Backup settings channels restore completed successfully'
_Am='rm -r {}backup_setting'
_Al='cp {}backup_setting/etc/enigma2/* /etc/enigma2'
_Ak='{}backup_setting'
_Aj='mkdir {}backup_setting'
_Ai='File setting not found!'
_Ah='Setting channel saved successfully on\n\n%s'
_Ag='/etc/enigma2/lamed*'
_Af='/etc/enigma2/*.radio'
_Ae='key_green'
_Ad='220x132'
_Ac='silver'
_Ab='remote'
_Aa='openpli'
_AZ='GioppyGio V.'
_AY='Unable to communicate with the server,\nplease check your internet connection'
_AX='Settings sent on %s'
_AW='smtp.gmail.com'
_AV='SetupActions'
_AU='ColorActions'
_AT='rm -rf /tmp/picon'
_AS='mv /tmp/picon/'
_AR='/tmp/picon'
_AQ='gioppygio-{}-{}-{}'
_AP='Dtt Italy'
_AO='setupActions'
_AN='progress2'
_AM='/etc/enigma2/*.tv'
_AL='Last backup saved'
_AK='image_stb'
_AJ='autotimer'
_AI=' Ovest'
_AH='URL Error: '
_AG='HTTP Error code: '
_AF='datesend'
_AE='rm -rf '
_AD='key_red'
_AC='Key_Personal'
_AB='red'
_AA='all'
_A9='progresstext2'
_A8='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/Settings/Select'
_A7='http://gioppygio.it/picons-snp/{}/gioppygio-{}-{}-{}.zip'
_A6='Settings & Picons V.%s by GioppyGio'
_A5='Corrupt file setting!'
_A4='/etc/enigma2/whitelist'
_A3='/etc/enigma2/blacklist'
_A2='/etc/enigma2/satellites.xml'
_A1='/etc/enigma2/terrestrial.xml'
_A0='progress'
_z='updatepicons'
_y='cancel'
_x='dtt-italia'
_w='chmod -R 755 '
_v='picon'
_u='{}backup_settings.zip'
_t='yellow'
_s='/media/usb'
_r='/media/usb/'
_q='/media/hdd'
_p='/media/hdd/'
_o='egami'
_n='FLASH'
_m='DVB-T'
_l='%d %B %Y'
_k='/etc/enigma2/backup_settings'
_j='/proc/mounts'
_i='progresstext'
_h='\n'
_g='modpicons'
_f='Elegant Black'
_e='Full Trasparent'
_d='gioppyregular'
_c='restarte2'
_b='importtxt'
_a='importtxtdate'
_Z='menu'
_Y=' '
_X='importpx'
_W='elegant-nero'
_V='/etc/enigma2/GioppyGioLcn.zip'
_U='config'
_T='0'
_S='Last-Modified'
_R='A'
_Q=' Est'
_P='/usr/share/enigma2/'
_O='ful-trs'
_N='/etc/enigma2/send_settings'
_M='/etc/enigma2/gioppygio_picons'
_L='version'
_K='xx'
_J='Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
_I='User-agent'
_H='w'
_G='a'
_F='B'
_E='utf-8'
_D=None
_C='r'
_B=False
_A=True
from.import _
from Components.Label import Label
from Components.ConfigList import ConfigListScreen,ConfigList
from Components.config import config,ConfigSelection,getConfigListEntry,ConfigText,ConfigYesNo,configfile,ConfigSubsection,ConfigInteger
from Components.Sources.List import List
from Components.ActionMap import ActionMap,HelpableActionMap
from Components.MenuList import MenuList
from Components.Pixmap import Pixmap
from Components.Sources.Progress import Progress
from.Moduli.Downloader import downloadWithProgress
from Components.Sources.StaticText import StaticText
from Plugins.Plugin import PluginDescriptor
from Components.MultiContent import MultiContentEntryText
from Components.ScrollLabel import ScrollLabel
from Screens.Standby import TryQuitMainloop
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Console import Console
from enigma import gFont,eTimer,getDesktop,eListboxPythonMultiContent,RT_HALIGN_LEFT,RT_HALIGN_RIGHT,RT_VALIGN_CENTER,RT_HALIGN_CENTER,eDVBDB,eComponentScan
import gettext,time,os,sys
from Screens.VirtualKeyBoard import VirtualKeyBoard
from.Moduli.Setting import*
from.Moduli.Config import*
from.Moduli.Select import*
from.Moduli.TerrestrialScan import TerrestrialScanGio,setParams
from.Moduli.MakeBouquet import MakeBouquet
from.Moduli.ScanDTT import Scandtt
from zipfile import ZipFile
from datetime import date
from base64 import b64encode,b64decode
from Components.NimManager import nimmanager
import ssl,socket
try:from urllib.request import urlopen,Request;from urllib.error import HTTPError,URLError
except ImportError:from urllib2 import urlopen,Request,HTTPError,URLError
try:py_version=sys.version_info.major
except:py_version=3
from enigma import addFont
plugin_fonts='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/font'
try:addFont('%s/arial-bold.ttf'%plugin_fonts,'gioppybold',100,1);addFont('%s/regular.ttf'%plugin_fonts,_d,100,1)
except Exception as ex:print('Font:',ex)
eTnCgFyIasdfghwerDkxGNSqQrtydfgzxcXVOtBjvawzz='11087'
eTnCgFyIasdfghwerDkxGNSqQrtydfgzxszxcXVOtBjvaw='23128'
eTnCgFyIasdfghwerDkxGNSqQrtydfgzxcXVOtBjvaw=eTnCgFyIasdfghwerDkxGNSqQrtydfgzxcXVOtBjvawzz+'&'+eTnCgFyIasdfghwerDkxGNSqQrtydfgzxszxcXVOtBjvaw
eTnCgFyIDkxGNSqQXVOtBjvao=len
eTnCgFyIDkxGNSqQXVOtBjvaW=range
eTnCgFyIDkxGNSqQXVOtBjvaU=chr
eTnCgFyIDkxGNSqQXVOtBjvaH=ord
def eTnCgFyIDkxGNSqQXVOOttBjvaw(s1,s2):
	s1=b64decode(s1.encode(_E)).decode(_E);s2=b64decode(s2.encode(_E)).decode(_E)
	while eTnCgFyIDkxGNSqQXVOtBjvao(s2)<eTnCgFyIDkxGNSqQXVOtBjvao(s1):s2+=s2
	eTnCgFyIDkxGNSqQXVOtBjvaE=''
	for eTnCgFyIDkxGNSqQXVOtBjvaz in eTnCgFyIDkxGNSqQXVOtBjvaW(eTnCgFyIDkxGNSqQXVOtBjvao(s1)):eTnCgFyIDkxGNSqQXVOtBjvaE+=eTnCgFyIDkxGNSqQXVOtBjvaU(eTnCgFyIDkxGNSqQXVOtBjvaH(s1[eTnCgFyIDkxGNSqQXVOtBjvaz])^eTnCgFyIDkxGNSqQXVOtBjvaH(s2[eTnCgFyIDkxGNSqQXVOtBjvaz]))
	return b64encode(eTnCgFyIDkxGNSqQXVOtBjvaE.encode(_E)).decode(_E)
dvbreaderarm='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/ReaderArm/dvbreader.so'
dvbreaderarmaa='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/ReaderArmAA/dvbreader.so'
dvbreaderarmpy2='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/ReaderArmP2/dvbreader.so'
dvbreadermips='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/ReaderMips/dvbreader.so'
dvbreadermipsp2='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/ReaderMipsP2/dvbreader.so'
dvbreaderaarch='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/ReaderAarch/dvbreader.so'
os.system(_w+dvbreaderarm)
os.system(_w+dvbreaderarmaa)
os.system(_w+dvbreaderarmpy2)
os.system(_w+dvbreadermips)
os.system(_w+dvbreadermipsp2)
os.system(_w+dvbreaderaarch)
stb=os.popen('head -n 1 /etc/hostname').read().split()[0]
URL='http://gioppygio.it/update/version.txt'
pathsite='http://gioppygio.it/update/'
plugin_path='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/'
if os.path.exists(_Ax):
	mod_image=os.popen("cat /etc/opkg/all-feed.conf | cut -d'-' -f1").read().split()[1]
	if mod_image==_Aa:os.system('rdate -s ntp1.inrim.it')
elif os.path.exists('/etc/opkg/all.conf'):
	mod_image=os.popen("cat /etc/opkg/all.conf | cut -d'-' -f1").read().split()[1]
	if mod_image==_AA:images_exec='PKTeam Hyperion'
if os.path.exists(_Ay)and os.path.exists(_Ax):
	with open(_Ay,_C)as f:
		for i in f:
			if str(mod_image).lower()in str(i).lower():
				image_exec=str(i).upper().replace('\\N','').replace('\\L','').replace('-RELEASE','').replace(_h,'').replace('  ',_Y)
				if mod_image==_o:
					try:from Components.SystemInfo import BoxInfo;imageDev=' R'+BoxInfo.getItem('imagedevbuild');images_exec=str(image_exec)+imageDev
					except Exception:pass
				else:images_exec=str(image_exec)
			elif mod_image==_Ab:images_exec='COBRALIBEROSAT TEAM'
def DownloadInfo(url):
	try:
		req=Request(url,_D,{_I:_J});context=ssl._create_unverified_context();response=urlopen(req,timeout=5,context=context)
		if py_version==2:link=response.read()
		else:link=response.read().decode(_E)
		response.close();return link
	except HTTPError as e:print(_AG,e.code)
	except URLError as e:print(_AH,e.reason)
	except ssl.SSLError as err:print('SSLError: ',str(err))
	except Exception:pass
if getDesktop(0).size().width()==1920:skins='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Skin/fhd/'
else:skins='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Skin/hd/'
sat=str('\xc2\xb0E')if py_version==2 else'°'
config.picongioppy=ConfigSubsection()
config.picongioppy.main=ConfigYesNo(default=_B)
config.picongioppy.piconsupdate=ConfigYesNo(default=_B)
config.picongioppy.type=ConfigSelection(default=_O,choices=[(_O,_(_e)),(_W,_(_f)),(_Ac,_('Silver')),(_o,_('Style Egami'))])
config.picongioppy.dest=ConfigSelection(default=_P,choices=[(_P,_('Internal memory (Flash)')),(_p,_(_q)),(_r,_(_s))])
config.picongioppy.dimens=ConfigSelection(default=_Ad,choices=[(_Ad,_(_Ad)),('417x250',_('417x250'))])
config.picongioppy.sat_value=ConfigYesNo(default=_B)
config.picongioppy.sat=ConfigSelection(default='4.8-est',choices=[('4.8-est',_('4.8'+sat+_Q)),('9-est',_('9.0'+sat+_Q)),('13-est',_('13.0'+sat+_Q)),('16-est',_('16.0'+sat+_Q)),('19-est',_('19.2'+sat+_Q)),('23-est',_('23.5'+sat+_Q)),('26-est',_('26.0'+sat+_Q)),('28-est',_('28.2'+sat+_Q)),('31-est',_('31.5'+sat+_Q)),('36-est',_('36.0'+sat+_Q)),('39-est',_('39.0'+sat+_Q)),('42-est',_('42.0'+sat+_Q)),('0.8-ovest',_('0.8'+sat+_AI)),('5-ovest',_('5.0'+sat+_AI)),('7.0-ovest',_('7.0'+sat+_AI)),('30-ovest',_('30.0'+sat+_AI))])
config.picongioppy.dtt=ConfigYesNo(default=_B)
config.picongioppy.dttmod=ConfigSelection(default=_x,choices=[(_x,_('All Regions'))])
class MenuListGioB(MenuList):
	def __init__(self,list,enableWrapAround=_A):
		MenuList.__init__(self,list,enableWrapAround,eListboxPythonMultiContent);screenwidth=getDesktop(0).size().width()
		if screenwidth and screenwidth==1920:self.l.setFont(0,gFont(_d,32));self.l.setFont(1,gFont(_d,24));self.l.setItemHeight(80)
		else:self.l.setFont(0,gFont(_d,20));self.l.setFont(1,gFont(_d,14));self.l.setItemHeight(50)
class MenuListGioA(MenuList):
	def __init__(self,list,enableWrapAround=_A):
		MenuList.__init__(self,list,enableWrapAround,eListboxPythonMultiContent);screenwidth=getDesktop(0).size().width()
		if screenwidth and screenwidth==1920:self.l.setFont(0,gFont(_d,32));self.l.setFont(1,gFont(_d,24));self.l.setItemHeight(80)
		else:self.l.setFont(0,gFont(_d,20));self.l.setFont(1,gFont(_d,14));self.l.setItemHeight(50)
def OnDsl():
	try:req=Request('http://gioppygio.it',_D,{_I:_J});context=ssl._create_unverified_context();response=urlopen(req,timeout=5,context=context);return _A
	except URLError as Error:
		if isinstance(Error.reason,socket.timeout):print('URL ERROR: ',Error)
		return _B
	except HTTPError as Error:
		if isinstance(Error.reason,socket.timeout):print('HTTPError: ',Error)
		return _B
	except socket.timeout as Error:print('socket.timeout: ',Error);return _B
	except Exception:return _B
class intro_gioppy(Screen):
	def __init__(self,session):
		self.session=session
		if getDesktop(0).size().width()==1920:skin=skins+'IntroGioppyfhd.xml'
		else:skin=skins+'IntroGioppyhd.xml'
		with open(skin,_C)as f:self.skin=f.read()
		Screen.__init__(self,session);self.onLayoutFinish.append(self.setMenu)
	def setMenu(self):self.Timer=eTimer();self.Timer.callback.append(self.controlloInternet);self.Timer.start(100,_A)
	def controlloInternet(self):
		if OnDsl():self.session.openWithCallback(self.close,MenuGio)
		else:self.session.openWithCallback(self.VerifyStart,MessageBox,_('You are not connected to the internet\nwould you like to continue?'),MessageBox.TYPE_YESNO)
	def VerifyStart(self,result):
		if result is _A:self.session.open(MenuGio);self.close()
		else:self.close()
class MenuGio(Screen):
	def __init__(self,session):
		A='team';self.session=session
		if getDesktop(0).size().width()==1920:skin=skins+'MenuGiofhd.xml'
		else:skin=skins+'MenuGiohd.xml'
		with open(skin,_C)as f:self.skin=f.read()
		Screen.__init__(self,session);self['actions']=HelpableActionMap(self,_Az,{'backup':self.Backup,'restore':self.Restore,'ok':self.keyOK,'up':self.keyUp,'pageUp':self.PageUp,'down':self.keyDown,'pageDown':self.PageDown,'blue':self.Auto,'green':self.dttscanner,_t:self.Select,_y:self.exitplug,'info':self.updateonline,'tv':self.changelog,'left':self.keyRightLeft,'right':self.keyRightLeft,_Z:self.keyMenu,'info_tester':self.Info_Tester,_AB:self.exitplug},-1);self[_AJ]=Label('');self['namesat']=Label('');self['dateDow']=Label('');self['Key_Red']=Label(_('Exit'));self[_Ae]=Label(_('Scan LCN Dtt'));self['export']=Label(_('Export settings'));self['import']=Label(_('Import settings'));self[_z]=Label('');self[_X]=Pixmap();self[_X].hide();self[_a]=Label('');self[_b]=Label('');self.check_filesZip();self[_AC]=Label('');self[_L]=Label('');self['key_help']=Label('ChangeLog');self[_A0]=Progress();self[_i]=StaticText();self['Key_Menu']=Label(_('PICONS'));self['Key_Info']=Label(_('Info Plugin'));self[_AK]=Pixmap()
		if mod_image:self[A]=Label(_('Image running: %s')%images_exec)
		else:self[A]=Label('')
		self['model_stb']=Label(_('Model Stb: %s')%str(stb).upper());self[_R]=MenuListGioA([]);self[_F]=MenuListGioB([]);self[_F].selectionEnabled(1);self[_R].selectionEnabled(1);self.currentlist=_F;self.ServerOn=_A;self.DubleClick=_A;self.MenuA();self.List=DownloadSetting();self.MenuB();self.xtimer=eTimer();self.timer=eTimer();self.stimer=eTimer();self.stimer.callback.append(self.update_on);self.timer.callback.append(self.update_off);self.timerpicon=eTimer();self.stimerpicon=eTimer();self.stimerpicon.callback.append(self.update_on_picon);self.timerpicon.callback.append(self.update_off_picon);self.iTimer=eTimer();self.iTimer.callback.append(self.keyRightLeft);self.iTimer.start(1000,_A);self.iTimer1=eTimer();self.iTimer1.callback.append(self.StartSetting);self.OnWriteAuto=eTimer();self.OnWriteAuto.callback.append(self.WriteAuto);self.StopAutoWrite=_B;self.ExitPlugin=eTimer();self.ExitPlugin.callback.append(self.PluginClose);self.onShown.append(self.ReturnSelect);self.onShown.append(self.Info)
		try:self.xtimer.callback.append(self.check_update)
		except:self.xtimer_conn=self.xtimer.timeout.connect(self.check_update)
		self.xtimer.start(0,_A);self.onFirstExecBegin.append(self.check_module)
	def check_module(self):
		check_module=_A
		try:import requests
		except Exception as e:print('Requests: ',e);check_module=_B
		if check_module is _B:os.chmod('/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/check_module.sh',493);cmd1='. /usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/check_module.sh';self.session.open(Console,title=_('Checking Python Module'),cmdlist=[cmd1],closeOnSuccess=_A)
		else:0
	def check_filesZip(self):
		check=_B
		if os.path.exists(_j):
			fd=open(_j,_C)
			for line in fd:
				l=line.split()
				if len(l)>1 and l[1]==_q:check=_A;self.device_hdd_usb=_p
				if len(l)>1 and l[1]==_s:check=_A;self.device_hdd_usb=_r
			fd.close()
		if check==_A:
			try:
				if os.path.exists(_u.format(self.device_hdd_usb)):
					self[_X].show()
					if os.path.exists(_k):
						with open(_k,_C)as f:dates=f.read()
						self[_a].setText(_('%s')%dates);self[_b].setText(_(_AL))
					else:self[_a].setText('');self[_b].setText('')
				else:self[_X].hide()
			except:pass
		else:0
	def Backup(self):
		if not glob.glob(_AM):self.session.open(MessageBox,_('There is no settings channel installed\n\nPlease install a settings channel first\nin order to make the backup'),MessageBox.TYPE_INFO);return
		self.session.openWithCallback(self.Backupdop,MessageBox,_('Would you like to backup setup channels?'),MessageBox.TYPE_YESNO)
	def Backupdop(self,answer):
		if answer is _A:
			check=_B;self.check_hdd=_B;self.check_usb=_B
			if os.path.exists(_j):
				fd=open(_j,_C)
				for line in fd:
					l=line.split()
					if len(l)>1 and l[1]==_q:check=_A;self.check_hdd=_A;self.device_hdd_usb=_p
					if len(l)>1 and l[1]==_s:check=_A;self.check_usb=_A;self.device_hdd_usb=_r
				fd.close()
			if check==_B:self.session.open(MessageBox,_('Connect a Usb/Hdd device and mount it as /media/hdd or /media/usb'),MessageBox.TYPE_INFO)
			elif self.check_hdd==_A and self.check_usb==_A:self.ChoiceBackup();return
			else:
				try:
					backup_setting=_u.format(self.device_hdd_usb)
					if os.path.exists(backup_setting):os.remove(backup_setting)
					with ZipFile(backup_setting,mode=_H)as archive:
						for file in glob.glob(_AM):archive.write(file)
					with ZipFile(backup_setting,mode=_G)as archive:
						for file in glob.glob(_Af):archive.write(file)
					with ZipFile(backup_setting,mode=_G)as archive:
						for file in glob.glob(_Ag):archive.write(file)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A1):terrestr=_A1;archive.write(terrestr)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A2):satellites_file=_A2;archive.write(satellites_file)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A3):black=_A3;archive.write(black)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A4):white=_A4;archive.write(white)
					if os.path.exists(backup_setting):
						date_now=date.today()
						with open(_k,_H)as f:f.write(date_now.strftime(_l))
						with open(_k,_C)as f:dates=f.read()
						self[_a].setText(_('%s')%dates);self[_b].setText(_(_AL));self[_X].show()
					else:self[_a].setText('');self[_b].setText('');self[_X].hide()
					self.session.open(MessageBox,_(_Ah)%self.device_hdd_usb,MessageBox.TYPE_INFO,timeout=5)
				except:self.session.open(MessageBox,_(_A5),MessageBox.TYPE_INFO)
	def ChoiceBackup(self):text=_('Choose the device where you want to backup the setting channels.');choices=[(_(_q),'hdd'),(_(_s),'usb')];self.session.openWithCallback(self.choiceBacktype,MessageBox,text,list=choices)
	def choiceBacktype(self,choice):
		if choice:
			ChoiceHDD='hdd'in choice;ChoiceUSB='usb'in choice
			if ChoiceHDD:
				self.device_hdd_usb=_p
				try:
					backup_setting=_u.format(self.device_hdd_usb)
					if os.path.exists(backup_setting):os.remove(backup_setting)
					with ZipFile(backup_setting,mode=_H)as archive:
						for file in glob.glob(_AM):archive.write(file)
					with ZipFile(backup_setting,mode=_G)as archive:
						for file in glob.glob(_Af):archive.write(file)
					with ZipFile(backup_setting,mode=_G)as archive:
						for file in glob.glob(_Ag):archive.write(file)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A1):terrestr=_A1;archive.write(terrestr)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A2):satellites_file=_A2;archive.write(satellites_file)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A3):black=_A3;archive.write(black)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A4):white=_A4;archive.write(white)
					if os.path.exists(backup_setting):
						date_now=date.today()
						with open(_k,_H)as f:f.write(date_now.strftime(_l))
						with open(_k,_C)as f:dates=f.read()
						self[_a].setText(_('%s')%dates);self[_b].setText(_(_AL));self[_X].show()
					else:self[_a].setText('');self[_b].setText('');self[_X].hide()
					self.session.open(MessageBox,_(_Ah)%self.device_hdd_usb,MessageBox.TYPE_INFO,timeout=5)
				except:self.session.open(MessageBox,_(_A5),MessageBox.TYPE_INFO)
			elif ChoiceUSB:
				self.device_hdd_usb=_r
				try:
					backup_setting=_u.format(self.device_hdd_usb)
					if os.path.exists(backup_setting):os.remove(backup_setting)
					with ZipFile(backup_setting,mode=_H)as archive:
						for file in glob.glob(_AM):archive.write(file)
					with ZipFile(backup_setting,mode=_G)as archive:
						for file in glob.glob(_Af):archive.write(file)
					with ZipFile(backup_setting,mode=_G)as archive:
						for file in glob.glob(_Ag):archive.write(file)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A1):terrestr=_A1;archive.write(terrestr)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A2):satellites_file=_A2;archive.write(satellites_file)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A3):black=_A3;archive.write(black)
					with ZipFile(backup_setting,mode=_G)as archive:
						if os.path.exists(_A4):white=_A4;archive.write(white)
					if os.path.exists(backup_setting):
						date_now=date.today()
						with open(_k,_H)as f:f.write(date_now.strftime(_l))
						with open(_k,_C)as f:dates=f.read()
						self[_a].setText(_('%s')%dates);self[_b].setText(_(_AL));self[_X].show()
					else:self[_a].setText('');self[_b].setText('');self[_X].hide()
					self.session.open(MessageBox,_(_Ah)%self.device_hdd_usb,MessageBox.TYPE_INFO,timeout=5)
				except:self.session.open(MessageBox,_(_A5),MessageBox.TYPE_INFO)
	def Restore(self):self.session.openWithCallback(self.Restoredop,MessageBox,_('Would you like to restore the setup channels backup?'),MessageBox.TYPE_YESNO)
	def Restoredop(self,answer):
		if answer is _A:
			check=_B;self.check_hdd=_B;self.check_usb=_B
			if os.path.exists(_j):
				fd=open(_j,_C)
				for line in fd:
					l=line.split()
					if len(l)>1 and l[1]==_q:check=_A;self.check_hdd=_A;self.device_hdd_usb=_p
					if len(l)>1 and l[1]==_s:check=_A;self.check_usb=_A;self.device_hdd_usb=_r
				fd.close()
			if check==_B:self.session.open(MessageBox,_('Connect a Usb/Hdd device and mount it as /Media/Hdd or Media/Usb'),MessageBox.TYPE_INFO);return
			else:
				if self.check_hdd==_A and os.path.exists('/media/hdd/backup_settings.zip')and self.check_usb==_A and os.path.exists('/media/usb/backup_settings.zip'):self.restoreBackupChoice();return
				backup_setting=_u.format(self.device_hdd_usb)
				if not os.path.exists(backup_setting):self.session.open(MessageBox,_(_Ai),MessageBox.TYPE_INFO);return
				else:
					try:
						os.system(_Aj.format(self.device_hdd_usb))
						with ZipFile(backup_setting,_C)as zip_rest:zip_rest.extractall(_Ak.format(self.device_hdd_usb))
						os.system(_Al.format(self.device_hdd_usb));os.system(_Am.format(self.device_hdd_usb));eDVBDB.getInstance().reloadServicelist();eDVBDB.getInstance().reloadBouquets();self.session.open(MessageBox,_(_An),MessageBox.TYPE_INFO,timeout=5)
					except:self.session.open(MessageBox,_(_A5),MessageBox.TYPE_INFO)
	def restoreBackupChoice(self):text=_('Choose the device where to restore the setting channels.');choices=[(_(_q),'hdd'),(_(_s),'usb')];self.session.openWithCallback(self.choiceBackRestore,MessageBox,text,list=choices)
	def choiceBackRestore(self,choice):
		if choice:
			ChoiceHDD='hdd'in choice;ChoiceUSB='usb'in choice
			if ChoiceHDD:
				self.device_hdd_usb=_p;backup_setting=_u.format(self.device_hdd_usb)
				if not os.path.exists(backup_setting):self.session.open(MessageBox,_(_Ai),MessageBox.TYPE_INFO);return
				else:
					try:
						os.system(_Aj.format(self.device_hdd_usb))
						with ZipFile(backup_setting,_C)as zip_rest:zip_rest.extractall(_Ak.format(self.device_hdd_usb))
						os.system(_Al.format(self.device_hdd_usb));os.system(_Am.format(self.device_hdd_usb));eDVBDB.getInstance().reloadServicelist();eDVBDB.getInstance().reloadBouquets();self.session.open(MessageBox,_(_An),MessageBox.TYPE_INFO,timeout=5)
					except:self.session.open(MessageBox,_(_A5),MessageBox.TYPE_INFO)
			if ChoiceUSB:
				self.device_hdd_usb=_r;backup_setting=_u.format(self.device_hdd_usb)
				if not os.path.exists(backup_setting):self.session.open(MessageBox,_(_Ai),MessageBox.TYPE_INFO);return
				else:
					try:
						os.system(_Aj.format(self.device_hdd_usb))
						with ZipFile(backup_setting,_C)as zip_rest:zip_rest.extractall(_Ak.format(self.device_hdd_usb))
						os.system(_Al.format(self.device_hdd_usb));os.system(_Am.format(self.device_hdd_usb));eDVBDB.getInstance().reloadServicelist();eDVBDB.getInstance().reloadBouquets();self.session.open(MessageBox,_(_An),MessageBox.TYPE_INFO,timeout=5)
					except:self.session.open(MessageBox,_(_A5),MessageBox.TYPE_INFO)
	def Info_Tester(self):self.session.open(TesterImage)
	def dttscanner(self):
		A="No DVB-T tuner available so don't load"
		if mod_image==_A_ or mod_image==_Ab or mod_image==_Aa or mod_image=='teamblue'or mod_image==_B0 or mod_image==_o or mod_image==_B1 or mod_image=='opennfr'or mod_image=='openhdf'or mod_image=='openspa'or mod_image=='openvix'or mod_image=='pure2'or mod_image==_B2 or mod_image==_B3 or mod_image==_B4 or mod_image=='openbh'or mod_image==_B5 or mod_image=='opentr'or mod_image==_AA:
			if nimmanager.hasNimType(_m):self.TerrestrialScanMain()
			else:self.session.open(MessageBox,_(A),MessageBox.TYPE_INFO)
		elif nimmanager.hasNimType(_m)and not nimmanager.getEnabledNimListOfType(_m):self.session.open(MessageBox,_('Tuner present but not configured\nConfigure the tuner as (DVB-T) and run GioppyGio plugin again'),MessageBox.TYPE_INFO)
		elif nimmanager.hasNimType(_m)and nimmanager.getEnabledNimListOfType(_m):self.TerrestrialScanMain()
		else:self.session.open(MessageBox,_(A),MessageBox.TYPE_INFO)
	def TerrestrialScanMain(self):self.session.open(DTTTerrestrialScan)
	def changelog(self):self.session.open(ChangeLog)
	def check_update(self):
		C='/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Panel/noimage.png';B='http://images.mynonpublic.com/openatv/nightly/_boximages/ax61.png';A='http://images.mynonpublic.com/openatv/nightly/_boximages/mutant51.png';self.path_model='/usr/share/enigma2/%s.png'%str(stb);image_stb_atv='/tmp/stb.png'
		if str(stb)=='h9sse'or str(stb)=='h92hse'or str(stb)=='h9se'or str(stb)=='h9combose':url_image_atv='http://images.mynonpublic.com/openatv/nightly/_boximages/zgemmah9sse.png'
		elif str(stb)=='h7':url_image_atv='http://images.mynonpublic.com/openatv/nightly/_boximages/zgemmah7.png'
		elif str(stb)=='h5':url_image_atv='http://images.mynonpublic.com/openatv/nightly/_boximages/zgemmah5.png'
		elif str(stb)=='h3':url_image_atv='http://images.mynonpublic.com/openatv/nightly/_boximages/zgemmah2h.png'
		elif str(stb)=='h4':url_image_atv='http://images.mynonpublic.com/openatv/nightly/_boximages/zgemmah4.png'
		elif str(stb)=='h9':url_image_atv='http://images.mynonpublic.com/openatv/nightly/_boximages/zgemmah9t.png'
		elif str(stb)=='hd51':url_image_atv=A
		elif str(stb)=='ax51':url_image_atv=A
		elif str(stb)=='mutant51':url_image_atv=A
		elif str(stb)=='ax61':url_image_atv=B
		elif str(stb)=='hd61':url_image_atv=B
		elif str(stb)=='h9combo':url_image_atv='http://images.mynonpublic.com/openatv/nightly/_boximages/zgemma%s.png'%stb
		elif str(stb)=='multiboxse'or str(stb)=='maxytecmultise':url_image_atv='http://images.mynonpublic.com/openatv/nightly/_boximages/maxytecmultise.png'
		elif str(stb)=='multibox':url_image_atv='http://images.mynonpublic.com/openatv/nightly/_boximages/maxytecmulti.png'
		else:url_image_atv='http://images.mynonpublic.com/openatv/nightly/_boximages/%s.png'%stb
		if not os.path.exists(self.path_model):
			if os.path.exists(image_stb_atv):self.path_model=image_stb_atv
			else:
				try:
					url=urlopen(url_image_atv,timeout=5).read()
					with open(image_stb_atv,'wb')as f:f.write(url)
					self.path_model=image_stb_atv
				except HTTPError as e:print(_AG,e.code);self.path_model=C
				except URLError as e:print(_AH,e.reason);self.path_model=C
		self[_AK].instance.setScale(1);self[_AK].instance.setPixmapFromFile(self.path_model);self[_AK].instance.show();self.downvr=DownloadInfo(URL)
		try:
			if float(self.downvr)>float(version):self.update_on()
			elif float(self.downvr)==float(version):self[_L].setText(_(_A6)%version)
			else:self[_L].setText(_('Beta version!'))
		except:self[_L].setText(_(_A6)%version)
		if os.path.exists(_M):
			if config.picongioppy.piconsupdate.value==_A:
				urlsat=_A7.format(config.picongioppy.dimens.value,config.picongioppy.type.value,config.picongioppy.dimens.value,config.picongioppy.sat.value);urldtt=_A7.format(config.picongioppy.dimens.value,config.picongioppy.type.value,config.picongioppy.dimens.value,config.picongioppy.dttmod.value)
				if config.picongioppy.sat_value.value==_A and config.picongioppy.dtt.value==_A:
					try:
						req=Request(urlsat,_D,{_I:_J});context=ssl._create_unverified_context()
						with urlopen(req,timeout=5,context=context)as response:last_modified_sat=response.headers[_S]
						req_dtt=Request(urldtt,_D,{_I:_J});context=ssl._create_unverified_context()
						with urlopen(req_dtt,timeout=5,context=context)as response:last_modified_dtt=response.headers[_S]
						with open(_M,_C)as f:
							list_date=[]
							for line in f:list_date.append(line)
							if last_modified_sat+_h!=list_date[0]and last_modified_dtt==list_date[1]:self.update_on_picon();return
							elif last_modified_sat+_h==list_date[0]and last_modified_dtt!=list_date[1]:self.update_on_picon();return
							elif last_modified_sat+_h==list_date[0]and last_modified_dtt==list_date[1]:0
					except Exception:pass
				if config.picongioppy.sat_value.value==_B and config.picongioppy.dtt.value==_A:
					try:
						req_dtt=Request(urldtt,_D,{_I:_J});context=ssl._create_unverified_context()
						with urlopen(req_dtt,timeout=5,context=context)as response:last_modified_dtt=response.headers[_S]
						with open(_M,_C)as f:
							if last_modified_dtt!=f.readline():self.update_on_picon()
					except Exception:pass
				if config.picongioppy.sat_value.value==_A and config.picongioppy.dtt.value==_B:
					try:
						req_sat=Request(urlsat,_D,{_I:_J});context=ssl._create_unverified_context()
						with urlopen(req_sat,timeout=5,context=context)as response:last_modified_sat=response.headers[_S]
						with open(_M,_C)as f:
							if last_modified_sat!=f.readline():self.update_on_picon()
					except Exception:pass
				if config.picongioppy.sat_value.value==_B and config.picongioppy.dtt.value==_B:0
		else:0
		self.xtimer.stop()
	def update_on(self):
		if str(stb).startswith('vu'):self[_L].setText(_('New V.%s Press HELP to update')%self.downvr)
		else:self[_L].setText(_('New V.%s Press INFO to update')%self.downvr)
		self.timer.start(1000,1)
	def update_off(self):self[_L].setText('');self.stimer.start(1000,1)
	def update_on_picon(self):self[_a].setText('');self[_b].setText('');self[_X].hide();self[_z].setText(_('Picons update\nPress the MENU key\nto update'));self.timerpicon.start(1500,1)
	def update_off_picon(self):self[_z].setText('');self.stimerpicon.start(1000,1)
	def updateonline(self):
		if float(self.downvr)>float(version):self.dlfile='/tmp/gioppygio.ipk';self.updateurl=pathsite+'enigma2-plugin-extensions-gioppygio_'+self.downvr+'_all.ipk';self.download=downloadWithProgress(self.updateurl,self.dlfile);self.download.addProgress(self.downloadProgress);self.download.start().addCallback(self.downloadFinished).addErrback(self.downloadFailed)
		else:0
	def downloadFinished(self,string):
		A='Install update...';self[_L].setText(_(A))
		if os.path.exists('/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/Settings/Date'):os.system('cp /usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/Settings/Date /tmp')
		if os.path.exists(_A8):os.system('cp /usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Moduli/Settings/Select /tmp')
		if os.path.exists(_M):os.system('cp /etc/enigma2/gioppygio_picons /tmp')
		if os.path.exists(_N):os.system('cp /etc/enigma2/send_settings /tmp')
		cmd4='opkg --force-reinstall --force-overwrite install /tmp/gioppygio.ipk';self.session.openWithCallback(self.RestartGUI,Console,title=_(A),cmdlist=[cmd4],closeOnSuccess=_A)
	def RestartGUI(self,string=''):msg=_(_B6);self.session.openWithCallback(self.FinishGUi,MessageBox,msg,MessageBox.TYPE_YESNO,default=_A)
	def FinishGUi(self,answer):
		if answer is _A:config.picongioppy.type.save();config.picongioppy.dest.save();config.picongioppy.dimens.save();config.picongioppy.sat.save();config.picongioppy.dtt.save();config.picongioppy.main.save();config.picongioppy.dttmod.save();config.picongioppy.sat_value.save();config.picongioppy.piconsupdate.save();configfile.save();self.session.open(TryQuitMainloop,3)
		else:0
	def downloadFailed(self,failure_instance=_D,error_message=''):
		text=_(_Ao)
		if error_message==''and failure_instance is not _D:error_message=failure_instance.getErrorMessage();text+=': '+error_message
		self[_L].setText(text)
	def downloadProgress(self,recvbytes,totalbytes):self[_A0].value=int(100*recvbytes/float(totalbytes));self[_i].text=_Ap%(recvbytes/1024,totalbytes/1024,100*recvbytes/float(totalbytes))
	def keyMenu(self):self.session.open(picons)
	def PluginClose(self):
		try:self.ExitPlugin.stop()
		except:pass
		self.close()
	def exitplug(self):
		if self.DubleClick:self.ExitPlugin.start(10,_A);self.DubleClick=_B
		else:self.PluginClose()
	def Select(self):
		Type,AutoTimer,Personal,NumberSat,NameSat,Date,NumberDtt,DowDate,NameInfo=Load()
		if str(Personal).strip()==_T:
			os.system('rm -rf /etc/enigma2/*.del')
			if str(Date).strip()==_T:self.session.open(MessageBox,_('You have no GioppyGio channel list installed\n\ninstall one to proceed with customization'),MessageBox.TYPE_ERROR);return
			else:self[_AC].setText(_('Custom List: Yes'));Personal='1';self.session.open(MenuSelect);WriteSave(Type,AutoTimer,Personal,NumberSat,NameSat,Date,NumberDtt,DowDate,NameInfo)
		else:self.session.openWithCallback(self.removepersonalizebouquet,MessageBox,_('Do you want to remove the selected bouquets from the plugin list?'),MessageBox.TYPE_YESNO)
	def removepersonalizebouquet(self,result):
		if result is _A:Type,AutoTimer,Personal,NumberSat,NameSat,Date,NumberDtt,DowDate,NameInfo=Load();self[_AC].setText(_(_B7));Personal=_T;open(_A8,_H).close();WriteSave(Type,AutoTimer,Personal,NumberSat,NameSat,Date,NumberDtt,DowDate,NameInfo)
		else:0
	def ReturnSelect(self):
		Type,AutoTimer,Personal,NumberSat,NameSat,Date,NumberDtt,DowDate,NameInfo=Load()
		if not os.path.exists(_A8)or os.path.getsize(_A8)<20:self[_AC].setText(_(_B7));WriteSave(Type,AutoTimer,_T,NumberSat,NameSat,Date,NumberDtt,DowDate,NameInfo)
	def Auto(self):
		if self.StopAutoWrite:return
		self.StopAutoWrite=_A;iTimerClass.StopTimer();self.Type,AutoTimer,self.Personal,self.NumberSat,self.NameSat,self.Date,self.NumberDtt,self.DowDate,self.NameInfo=Load()
		if int(AutoTimer)==0:self[_AJ].setText(_('Auto Update: Yes'));self.jAutoTimer=1;iTimerClass.TimerSetting()
		else:self[_AJ].setText(_('Auto Update: No'));self.jAutoTimer=0
		self.OnWriteAuto.start(1000,_A)
	def WriteAuto(self):self.StopAutoWrite=_B;WriteSave(self.Type,self.jAutoTimer,self.Personal,self.NumberSat,self.NameSat,self.Date,self.NumberDtt,self.DowDate,self.NameInfo)
	def Info(self):
		A='Yes';Type,AutoTimer,Personal,NumberSat,NameSat,Date,NumberDtt,DowDate,NameInfo=Load()
		if int(AutoTimer)==0:TypeTimer=_('No')
		else:TypeTimer=_(A)
		if int(Personal)==0:jPersonal=_('No')
		else:jPersonal=_(A)
		if str(Date)==_T:newdate=''
		else:newdate=' - '+ConverDate(Date)
		if str(DowDate)==_T:newDowDate=_('Last Update: Never')
		else:newDowDate=_('Last Update: ')+DowDate
		self[_AC].setText(_('Custom List: ')+jPersonal);self[_AJ].setText(_('Auto Update: ')+TypeTimer);self['namesat'].setText(NameInfo+newdate);self['dateDow'].setText(newDowDate)
	def hauptListEntryMenuA(self,name,type):
		res=[(name,type)]
		if getDesktop(0).size().width()==1920:res.append(MultiContentEntryText(pos=(60,11),size=(230,45),font=0,text=name,flags=RT_HALIGN_CENTER));res.append(MultiContentEntryText(pos=(0,0),size=(8,0),font=0,text=type,flags=RT_HALIGN_LEFT))
		else:res.append(MultiContentEntryText(pos=(5,11),size=(230,45),font=0,text=name,flags=RT_HALIGN_CENTER));res.append(MultiContentEntryText(pos=(0,0),size=(8,0),font=0,text=type,flags=RT_HALIGN_LEFT))
		return res
	def hauptListEntryMenuB(self,NumberSat,Name,jData,NumberDtt):
		res=[(NumberSat,Name,jData,NumberDtt)]
		if getDesktop(0).size().width()==1920:
			if NumberDtt==_K:res.append(MultiContentEntryText(pos=(10,11),size=(750,35),font=0,text=Name,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=jData,flags=RT_HALIGN_RIGHT));res.append(MultiContentEntryText(pos=(10,11),size=(460,35),font=0,text=Name,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(600,11),size=(120,35),font=0,text=jData,flags=RT_HALIGN_RIGHT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=NumberDtt,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=NumberSat,flags=RT_HALIGN_LEFT))
			else:res.append(MultiContentEntryText(pos=(20,11),size=(850,45),font=0,text=Name,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=jData,flags=RT_HALIGN_RIGHT));res.append(MultiContentEntryText(pos=(20,11),size=(650,45),font=0,text=Name,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(600,11),size=(200,45),font=0,text=jData,flags=RT_HALIGN_RIGHT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=NumberDtt,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=NumberSat,flags=RT_HALIGN_LEFT))
		elif NumberDtt==_K:res.append(MultiContentEntryText(pos=(20,11),size=(850,35),font=0,text=Name,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=jData,flags=RT_HALIGN_RIGHT));res.append(MultiContentEntryText(pos=(20,11),size=(460,45),font=0,text=Name,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(320,11),size=(200,45),font=0,text=jData,flags=RT_HALIGN_RIGHT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=NumberDtt,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=NumberSat,flags=RT_HALIGN_LEFT))
		else:res.append(MultiContentEntryText(pos=(20,11),size=(850,45),font=0,text=Name,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=jData,flags=RT_HALIGN_RIGHT));res.append(MultiContentEntryText(pos=(20,11),size=(460,45),font=0,text=Name,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(320,11),size=(200,45),font=0,text=jData,flags=RT_HALIGN_RIGHT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=NumberDtt,flags=RT_HALIGN_LEFT));res.append(MultiContentEntryText(pos=(0,0),size=(0,0),font=0,text=NumberSat,flags=RT_HALIGN_LEFT))
		return res
	def MenuA(self):self.jA=[];self.jA.append(self.hauptListEntryMenuA('Mono + DTT','mono'));self.jA.append(self.hauptListEntryMenuA('Dual + DTT','dual'));self.jA.append(self.hauptListEntryMenuA('Trial','trial'));self.jA.append(self.hauptListEntryMenuA('Quadri','quadri'));self.jA.append(self.hauptListEntryMenuA('Motor + DTT','motor'));self.jA.append(self.hauptListEntryMenuA('DTT','digitale'));self[_R].setList(self.jA)
	def MenuB(self):
		self.jB=[]
		if not self.DubleClick:self.ServerOn=_B;self.jB.append(self.hauptListEntryMenuB('',_(''),_K,_K));self.jB.append(self.hauptListEntryMenuB('',_(''),_K,_K));self.jB.append(self.hauptListEntryMenuB('',_(''),_K,_K));self.jB.append(self.hauptListEntryMenuB('',_(''),_K,_K));self.jB.append(self.hauptListEntryMenuB('',_(''),_K,_K));self.jB.append(self.hauptListEntryMenuB('',_(''),_K,_K));self[_F].setList(self.jB);return
		for(NumberSat,NameSat,LinkSat,DateSat,NumberDtt,NameDtt,LinkDtt,DateDtt)in self.List:
			if NameSat.lower().find(self[_R].getCurrent()[0][1])!=-1:
				if str(NameDtt)!=_T:
					jData=str(DateSat)
					if int(DateDtt)>int(DateSat):jData=str(DateDtt)
					self.jB.append(self.hauptListEntryMenuB(NumberSat,NameSat.split('(')[0]+' + '+NameDtt,ConverDate(str(jData)),NumberDtt))
				else:self.jB.append(self.hauptListEntryMenuB(NumberSat,NameSat,ConverDate(str(DateSat)),_T))
		if not self.jB:self.jB.append(self.hauptListEntryMenuB(_(''),_(_Y),'',''));self.jB.append(self.hauptListEntryMenuB(_(''),_('Server down for maintenance'),'',''));self.jB.append(self.hauptListEntryMenuB(_(''),_('If there is an update, run it!'),'',''));self[_F].setList(self.jB);self.ServerOn=_B;self.MenuA();return
		self[_F].setList(self.jB)
	def keyOK(self):
		if not self.ServerOn:return
		if self.currentlist==_R:self.currentlist=_F;self[_F].selectionEnabled(1);self[_R].selectionEnabled(0);return
		Type,self.AutoTimer,self.Personal,NumberSat,NameSat,self.Date,NumberDtt,self.DowDate,NameInfo=Load();self.name=self[_F].getCurrent()[0][1];self.NumberSat=self[_F].getCurrent()[0][0];self.NumberDtt=self[_F].getCurrent()[0][3];self.jType='1'
		if self.name.lower().find('dtt')!=-1:self.jType=_T
		try:nData=int(self.Date)
		except:nData=0
		try:njData=int(self[_F].getCurrent()[0][2].replace('-',''))
		except:njData=999999
		if NameSat!=self.name or Type!=self.jType:
			if str(self.Personal).strip()=='1':self.Personal=_T
			open(_A8,_H).close();self.session.openWithCallback(self.OnDownload,MessageBox,_('The new configurations are saved\nSetting: %s\nDate: %s\nThe choice is different from the previous\nDo you want to proceed with the manual upgrade?')%(self.name,self[_F].getCurrent()[0][2]),MessageBox.TYPE_YESNO,timeout=20)
		elif njData>nData:
			if str(self.Personal).strip()=='1':self.Personal=_T
			open(_A8,_H).close();self.session.openWithCallback(self.OnDownload,MessageBox,_('The new configurations are saved\nSetting: %s\nDate: %s \n The new setting has a more recent date\nDo you want to proceed with the manual upgrade?')%(self.name,self[_F].getCurrent()[0][2]),MessageBox.TYPE_YESNO,timeout=20)
		else:self.session.openWithCallback(self.OnDownloadForce,MessageBox,_('Setting already updated, you want to upgrade anyway?'),MessageBox.TYPE_YESNO,timeout=20)
	def OnDownloadForce(self,conf):
		if conf:self.OnDownload(_A,_B)
	def StartSetting(self):iTimerClass.StopTimer();iTimerClass.startTimerSetting(_A)
	def OnDownload(self,conf,noForce=_A):
		if conf:
			if noForce:WriteSave(self.jType,self.AutoTimer,self.Personal,self.NumberSat,self.name,self.Date,self.NumberDtt,self.DowDate,self.name)
			self.iTimer1.start(100,_A)
		else:WriteSave(self.jType,self.AutoTimer,self.Personal,self.NumberSat,self.name,_T,self.NumberDtt,self.DowDate,self.name)
		self.Info()
	def keyUp(self):
		self[self.currentlist].up()
		if self.currentlist==_R:self.MenuB()
	def keyDown(self):
		self[self.currentlist].down()
		if self.currentlist==_R:self.MenuB()
	def PageUp(self):self[_F].pageUp()
	def PageDown(self):self[_F].pageDown()
	def keyRightLeft(self):
		self[_R].selectionEnabled(0);self[_F].selectionEnabled(0)
		if self.currentlist==_R:
			if not self.ServerOn:return
			self.currentlist=_F;self[_F].selectionEnabled(1);self.MenuB()
		else:self.currentlist=_R;self[_R].selectionEnabled(1)
class picons(Screen,ConfigListScreen):
	def __init__(self,session):
		if getDesktop(0).size().width()==1920:skin=skins+'piconsfhd.xml'
		else:skin=skins+'piconshd.xml'
		with open(skin,_C)as f:self.skin=f.read()
		Screen.__init__(self,session);self.timer=eTimer();self.stimer=eTimer();self.stimer.callback.append(self.restart_on);self.timer.callback.append(self.restart_off);self.timerpicon=eTimer();self.stimerpicon=eTimer();self.stimerpicon.callback.append(self.update_on_picon);self.timerpicon.callback.append(self.update_off_picon);self[_AD]=Label(_('Exit'));self[_Ae]=Label(_('Save | Install'));self['key_yellow']=Label(_('Restart E2'));self['key_blue']=Label(_('Delete Picons'));self['key_help']=Label(_('Picons News'));self[_z]=Label('');self[_A0]=Progress();self[_i]=StaticText();self[_AN]=Progress();self[_A9]=StaticText();self[_g]=Pixmap();self[_c]=Label();self.status=_B;self.status2=_B;self.status_download=_B;self.status2_download=_B;self[_L]=Label(_(_A6)%version);self[_AO]=HelpableActionMap(self,_Az,{_AB:self.close_screen_picon,_y:self.close_screen_picon,'ok':self.passok,'green':self.piconsyesno,_t:self.RestartGUI,'blue':self.deletepicons,'tv':self.ChangeLogPicons});self.list=[];self.getConfig();ConfigListScreen.__init__(self,self.list);self.onLayoutFinish.append(self.showpicons);self.timershow()
	def timershow(self):self.TimerShow=eTimer();self.TimerShow.callback.append(self.UpdatePicons);self.TimerShow.start(100,_A)
	def passok(self):0
	def piconsyesno(self):
		if config.picongioppy.dtt.value==_B and config.picongioppy.sat_value.value==_B and config.picongioppy.main.value==_A:self.RestartGUI();return
		if config.picongioppy.dtt.value==_B and config.picongioppy.sat_value.value==_B:self.session.open(MessageBox,_(_B8),MessageBox.TYPE_ERROR);return
		if config.picongioppy.dtt.value==_A and config.picongioppy.sat_value.value==_A:msg=_('Do you want to install the picons\n\nModel: {}\nSatellites: {}\nDTT: {}\nDestination: {}\nResolution: {}').format(config.picongioppy.type.value.replace(_O,_(_e)).replace(_W,_(_f)),config.picongioppy.sat.value,config.picongioppy.dttmod.value.replace(_x,_(_AP)),config.picongioppy.dest.value.replace(_P,_n),config.picongioppy.dimens.value)
		if config.picongioppy.dtt.value==_B and config.picongioppy.sat_value.value==_A:msg=_('Do you want to install the picons\n\nModel: {}\nSatellites: {}\nDestination: {}\nResolution: {}').format(config.picongioppy.type.value.replace(_O,_(_e)).replace(_W,_(_f)),config.picongioppy.sat.value,config.picongioppy.dest.value.replace(_P,_n),config.picongioppy.dimens.value)
		if config.picongioppy.dtt.value==_A and config.picongioppy.sat_value.value==_B:msg=_('Do you want to install the picons\n\nModel: {}\nDTT: {}\nDestination: {}\nResolution: {}').format(config.picongioppy.type.value.replace(_O,_(_e)).replace(_W,_(_f)),config.picongioppy.dttmod.value.replace(_x,_(_AP)),config.picongioppy.dest.value.replace(_P,_n),config.picongioppy.dimens.value)
		self.session.openWithCallback(self.inst_pic,MessageBox,msg,MessageBox.TYPE_YESNO)
	def deletepicons(self):
		A="You don't have any picons installed!"
		if os.path.isdir(str(config.picongioppy.dest.value+_v)):
			ListPicons=glob.glob(str(config.picongioppy.dest.value+'picon/*.png'))
			if ListPicons:self.session.openWithCallback(self.deleteall,MessageBox,_('Do you want to delete all picons\n\nModel: {}\nDestination: {}\nResolution: {}').format(config.picongioppy.type.value.replace(_O,_(_e)).replace(_W,_(_f)),config.picongioppy.dest.value.replace(_P,_n),config.picongioppy.dimens.value),MessageBox.TYPE_YESNO,default=_B)
			else:self.session.open(MessageBox,_(A),MessageBox.TYPE_ERROR)
		else:self.session.open(MessageBox,_(A),MessageBox.TYPE_ERROR)
	def deleteall(self,answer):
		if answer is _A:cmd=_AE+config.picongioppy.dest.value+'picon/*';self.session.openWithCallback(self.messagedel,Console,title=_('Delete all picons...'),cmdlist=[cmd],closeOnSuccess=_A)
		else:0
	def messagedel(self,string=''):self.session.open(MessageBox,_('Picons\n\nModel: {}\nDestination: {}\nResolution: {}\nremoved!').format(config.picongioppy.type.value.replace(_O,_(_e)).replace(_W,_(_f)),config.picongioppy.dest.value.replace(_P,_n),config.picongioppy.dimens.value),MessageBox.TYPE_INFO,timeout=5)
	def ChangeLogPicons(self):self.session.open(PiconsNews)
	def restart_on(self):self[_c].setText(_('* Remember to restart enigma2'));self.timer.start(1000,1)
	def restart_off(self):self[_c].setText('');self.stimer.start(1000,1)
	def RestartGUI(self):msg=_(_B6);self.session.openWithCallback(self.FinishGUi,MessageBox,msg,MessageBox.TYPE_YESNO)
	def FinishGUi(self,answer):
		config.picongioppy.type.save();config.picongioppy.dest.save();config.picongioppy.dimens.save();config.picongioppy.sat.save();config.picongioppy.dtt.save();config.picongioppy.main.save();config.picongioppy.dttmod.save();config.picongioppy.sat_value.save();config.picongioppy.piconsupdate.save();configfile.save()
		if answer is _A:self.session.open(TryQuitMainloop,3)
		else:0
	def getConfig(self):
		self.list=[];self.list.append(getConfigListEntry(_('Select the model:'),config.picongioppy.type));self.list.append(getConfigListEntry(_('Select the destination:'),config.picongioppy.dest));self.list.append(getConfigListEntry(_('Select the size:'),config.picongioppy.dimens));self.list.append(getConfigListEntry(_('Satellite Picons'),config.picongioppy.sat_value))
		if config.picongioppy.sat_value.value:self.list.append(getConfigListEntry(_('Select the satellite:'),config.picongioppy.sat))
		self.list.append(getConfigListEntry(_('Picons DTT Italy'),config.picongioppy.dtt));self.list.append(getConfigListEntry(_('Check update picons'),config.picongioppy.piconsupdate));self.list.append(getConfigListEntry(_('Show in main menu'),config.picongioppy.main))
	def showpicons(self):
		if getDesktop(0).size().width()==1920:
			if config.picongioppy.type.value==_O:self[_g].instance.setPixmapFromFile('/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Panel/full-trs.png')
			if config.picongioppy.type.value==_W:self[_g].instance.setPixmapFromFile('/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Panel/elegant-nero.png')
			if config.picongioppy.type.value==_Ac:self[_g].instance.setPixmapFromFile('/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Panel/silver.png')
			if config.picongioppy.type.value==_o:self[_g].instance.setPixmapFromFile('/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Panel/egami.png')
		else:
			if config.picongioppy.type.value==_O:self[_g].instance.setPixmapFromFile('/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Panel/full-trshd.png')
			if config.picongioppy.type.value==_W:self[_g].instance.setPixmapFromFile('/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Panel/elegant-nerohd.png')
			if config.picongioppy.type.value==_Ac:self[_g].instance.setPixmapFromFile('/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Panel/silverhd.png')
			if config.picongioppy.type.value==_o:self[_g].instance.setPixmapFromFile('/usr/lib/enigma2/python/Plugins/Extensions/GioppyGio/Panel/egamihd.png')
	def UpdatePicons(self):
		if os.path.exists(_M):
			if config.picongioppy.piconsupdate.value==_A:
				urlsat=_A7.format(config.picongioppy.dimens.value,config.picongioppy.type.value,config.picongioppy.dimens.value,config.picongioppy.sat.value);urldtt=_A7.format(config.picongioppy.dimens.value,config.picongioppy.type.value,config.picongioppy.dimens.value,config.picongioppy.dttmod.value)
				if config.picongioppy.sat_value.value==_A and config.picongioppy.dtt.value==_A:
					try:
						req_sat=Request(urlsat,_D,{_I:_J});context=ssl._create_unverified_context()
						with urlopen(req_sat,timeout=5,context=context)as response:last_modified_sat=response.headers[_S]
						req_dtt=Request(urldtt,_D,{_I:_J});context=ssl._create_unverified_context()
						with urlopen(req_dtt,timeout=5,context=context)as response:last_modified_dtt=response.headers[_S]
						with open(_M,_C)as f:
							list_date=[]
							for line in f:list_date.append(line)
							if last_modified_sat+_h!=list_date[0]and last_modified_dtt==list_date[1]:self.update_on_picon();return
							elif last_modified_sat+_h==list_date[0]and last_modified_dtt!=list_date[1]:self.update_on_picon();return
							elif last_modified_sat+_h==list_date[0]and last_modified_dtt==list_date[1]:0
					except Exception:pass
				if config.picongioppy.sat_value.value==_B and config.picongioppy.dtt.value==_A:
					try:
						req_dtt=Request(urldtt,_D,{_I:_J});context=ssl._create_unverified_context()
						with urlopen(req_dtt,timeout=5,context=context)as response:last_modified_dtt=response.headers[_S]
						with open(_M,_C)as f:
							if last_modified_dtt!=f.readline():self.update_on_picon()
					except Exception:pass
				if config.picongioppy.sat_value.value==_A and config.picongioppy.dtt.value==_B:
					try:
						req_sat=Request(urlsat,_D,{_I:_J});context=ssl._create_unverified_context()
						with urlopen(req_sat,timeout=5,context=context)as response:last_modified_sat=response.headers[_S]
						with open(_M,_C)as f:
							if last_modified_sat!=f.readline():self.update_on_picon()
					except Exception:pass
				if config.picongioppy.sat_value.value==_B and config.picongioppy.dtt.value==_B:0
		else:0
	def update_on_picon(self):self[_z].setText(_('Picons update, press green button to update'));self.timerpicon.start(1500,1)
	def update_off_picon(self):self[_z].setText('');self.stimerpicon.start(1000,1)
	def changedEntry(self):self.getConfig();self[_U].setList(self.list)
	def keyLeft(self):ConfigListScreen.keyLeft(self);self.showpicons();self.changedEntry()
	def keyRight(self):ConfigListScreen.keyRight(self);self.showpicons();self.changedEntry()
	def inst_pic(self,result):
		if result is _A:
			config.picongioppy.type.save();config.picongioppy.dest.save();config.picongioppy.dimens.save();config.picongioppy.sat.save();config.picongioppy.dtt.save();config.picongioppy.main.save();config.picongioppy.dttmod.save();config.picongioppy.sat_value.save();config.picongioppy.piconsupdate.save();configfile.save()
			if config.picongioppy.dest.value==_p or config.picongioppy.dest.value==_r or config.picongioppy.dest.value==_P:
				check=_B
				if config.picongioppy.dest.value==_P:check=_A
				if os.path.exists(_j):
					fd=open(_j,_C)
					for line in fd:
						l=line.split()
						if len(l)>1 and l[1]==_q:check=_A
						if len(l)>1 and l[1]==_s:check=_A
					fd.close()
				if check==_B:self.session.open(MessageBox,_('Sorry, there is not any connected devices in your STB.\nPlease connect HDD\nand mount it in the /media/hdd\nto install the Picons!'),MessageBox.TYPE_INFO)
				else:
					if config.picongioppy.dtt.value==_A and config.picongioppy.sat_value.value==_A:self.session.openWithCallback(self.start_inst,MessageBox,_('Install Picons\n\nModel: {}\nSatellites: {}\nDTT: {}\nDestination: {}\nResolution: {}').format(config.picongioppy.type.value.replace(_O,_(_e)).replace(_W,_(_f)),config.picongioppy.sat.value,config.picongioppy.dttmod.value.replace(_x,_(_AP)),config.picongioppy.dest.value.replace(_P,_n),config.picongioppy.dimens.value),MessageBox.TYPE_INFO,timeout=4)
					if config.picongioppy.dtt.value==_B and config.picongioppy.sat_value.value==_A:self.session.openWithCallback(self.start_inst,MessageBox,_('Install Picons\n\nModel: {}\nSatellites: {}\nDestination: {}\nResolution: {}').format(config.picongioppy.type.value.replace(_O,_(_e)).replace(_W,_(_f)),config.picongioppy.sat.value,config.picongioppy.dest.value.replace(_P,_n),config.picongioppy.dimens.value),MessageBox.TYPE_INFO,timeout=4)
					if config.picongioppy.dtt.value==_A and config.picongioppy.sat_value.value==_B:self.session.openWithCallback(self.start_inst,MessageBox,_('Install Picons\n\nModel: {}\nDTT: {}\nDestination: {}\nResolution: {}').format(config.picongioppy.type.value.replace(_O,_(_e)).replace(_W,_(_f)),config.picongioppy.dttmod.value.replace(_x,_(_AP)),config.picongioppy.dest.value.replace(_P,_n),config.picongioppy.dimens.value),MessageBox.TYPE_INFO,timeout=4)
					if config.picongioppy.dtt.value==_B and config.picongioppy.sat_value.value==_B:self.session.open(MessageBox,_(_B8),MessageBox.TYPE_ERROR)
	def start_inst(self,string=''):
		A='Download picons %s'
		if not os.path.exists(config.picongioppy.dest.value+_v):os.system('mkdir '+config.picongioppy.dest.value+_v)
		self.dlfile='/tmp/piconsat.zip';self.dlfiledtt='/tmp/picondtt.zip';urlsat=_A7.format(config.picongioppy.dimens.value,config.picongioppy.type.value,config.picongioppy.dimens.value,config.picongioppy.sat.value);urldtt=_A7.format(config.picongioppy.dimens.value,config.picongioppy.type.value,config.picongioppy.dimens.value,config.picongioppy.dttmod.value)
		if config.picongioppy.dtt.value==_B and config.picongioppy.sat_value.value==_A:
			if config.picongioppy.piconsupdate.value==_A:
				try:
					req_sat=Request(urlsat,_D,{_I:_J});context=ssl._create_unverified_context()
					with urlopen(req_sat,timeout=5,context=context)as response:last_modified_sat=response.headers[_S]
					with open(_M,_H)as f:f.write(last_modified_sat)
				except Exception:pass
			self.download=downloadWithProgress(urlsat,self.dlfile);self.download.addProgress(self.downloadProgress);self[_c].setText(_(A)%config.picongioppy.type.value);self.status_download=_A;self.download.start().addCallback(self.downloadFinished).addErrback(self.downloadFailed)
		if config.picongioppy.dtt.value==_A and config.picongioppy.sat_value.value==_A:
			if config.picongioppy.piconsupdate.value==_A:
				try:
					req_sat=Request(urlsat,_D,{_I:_J});context=ssl._create_unverified_context()
					with urlopen(req_sat,timeout=5,context=context)as response:last_modified_sat=response.headers[_S]
					req_dtt=Request(urldtt,_D,{_I:_J});context=ssl._create_unverified_context()
					with urlopen(req_dtt,timeout=5,context=context)as response:last_modified_dtt=response.headers[_S]
					with open(_M,_H)as f:f.write(last_modified_sat)
					with open(_M,_G)as f:f.write(_h+last_modified_dtt)
				except Exception:pass
			self.download=downloadWithProgress(urlsat,self.dlfile);self.download.addProgress(self.downloadProgress);self.downloads=downloadWithProgress(urldtt,self.dlfiledtt);self.downloads.addProgress(self.downloadProgressdtt);self[_c].setText(_(A)%config.picongioppy.type.value);self.status_download=_A;self.status2_download=_A;self.download.start().addCallback(self.downloadFinishedd).addErrback(self.downloadFailed);self.downloads.start().addCallback(self.downloadFinisheds).addErrback(self.downloadFailed)
		if config.picongioppy.dtt.value==_A and config.picongioppy.sat_value.value==_B:
			if config.picongioppy.piconsupdate.value==_A:
				try:
					req_dtt=Request(urldtt,_D,{_I:_J});context=ssl._create_unverified_context()
					with urlopen(req_dtt,timeout=5,context=context)as response:last_modified_dtt=response.headers[_S]
					with open(_M,_H)as f:f.write(last_modified_dtt)
				except Exception:pass
			self.downloads=downloadWithProgress(urldtt,self.dlfiledtt);self.downloads.addProgress(self.downloadProgressdtt);self[_c].setText(_(A)%config.picongioppy.type.value);self.status2_download=_A;self.downloads.start().addCallback(self.downloadFinisheddt).addErrback(self.downloadFailed)
	def downloadFailed(self,failure_instance=_D,error_message=''):
		text=_(_Ao);self[_c].setText(_('Picons %s download error!')%config.picongioppy.type.value)
		if error_message==''and failure_instance is not _D:error_message=failure_instance.getErrorMessage();text+=': '+error_message;self.session.open(MessageBox,_(_Ao),MessageBox.TYPE_ERROR)
	def downloadProgress(self,recvbytes,totalbytes):self[_A0].value=int(100*recvbytes/float(totalbytes));self[_i].text=_Ap%(recvbytes/1024,totalbytes/1024,100*recvbytes/float(totalbytes))
	def downloadProgressdtt(self,recvbytes,totalbytes):self[_AN].value=int(100*recvbytes/float(totalbytes));self[_A9].text=_Ap%(recvbytes/1024,totalbytes/1024,100*recvbytes/float(totalbytes))
	def downloadFinished(self,string):self[_c].setText(_(_Aq)%config.picongioppy.type.value);move_picons=_AQ.format(config.picongioppy.type.value,config.picongioppy.dimens.value,config.picongioppy.sat.value);z=ZipFile(self.dlfile,_C);z.extractall(_AR);os.system(_AS+move_picons+'/*'+_Y+config.picongioppy.dest.value+_v);os.system(_AE+self.dlfile);os.system(_AT);self.RestartE2();z.close()
	def downloadFinisheddt(self,string):
		if os.path.exists(self.dlfiledtt):self.status=_A;self.finish_restart_dtt()
	def finish_restart_dtt(self):
		move_piconsdtt=_AQ.format(config.picongioppy.type.value,config.picongioppy.dimens.value,config.picongioppy.dttmod.value)
		if self.status==_A:self[_c].setText(_(_Aq)%config.picongioppy.type.value);z=ZipFile(self.dlfiledtt,_C);z.extractall(_AR);os.system(_AS+move_piconsdtt+'/*'+_Y+config.picongioppy.dest.value+_v);os.system(_AE+self.dlfiledtt);os.system(_AT);self.RestartE2();z.close()
	def downloadFinishedd(self,string):
		if os.path.exists(self.dlfile):self.status=_A;self.finish_restart()
	def downloadFinisheds(self,string):
		if os.path.exists(self.dlfiledtt):self.status2=_A;self.finish_restart()
	def finish_restart(self):
		move_piconsdtt=_AQ.format(config.picongioppy.type.value,config.picongioppy.dimens.value,config.picongioppy.dttmod.value);move_picons=_AQ.format(config.picongioppy.type.value,config.picongioppy.dimens.value,config.picongioppy.sat.value)
		if self.status==_A and self.status2==_A:self[_c].setText(_(_Aq)%config.picongioppy.type.value);z=ZipFile(self.dlfiledtt,_C);z.extractall(_AR);os.system(_AS+move_piconsdtt+'/*'+_Y+config.picongioppy.dest.value+_v);os.system(_AE+self.dlfiledtt);os.system(_AT);zs=ZipFile(self.dlfile,_C);zs.extractall(_AR);os.system(_AS+move_picons+'/*'+_Y+config.picongioppy.dest.value+_v);os.system(_AE+self.dlfile);os.system(_AT);self.RestartE2();z.close();zs.close()
	def RestartE2(self):msg=_('Download successful\n\nDo you want to restart the GUI\nto apply the changes?');self.session.openWithCallback(self.Finish,MessageBox,msg,MessageBox.TYPE_YESNO)
	def Finish(self,answer):
		C='DTT ';B=' installed';A='Picons '
		if answer is _A:self.session.open(TryQuitMainloop,3)
		else:
			self.status=_B;self.status2=_B;self.status_download=_B;self.status2_download=_B
			if config.picongioppy.dtt.value==_A and config.picongioppy.sat_value.value==_A:self.restart_on();self[_i].text=A+config.picongioppy.type.value+_Y+config.picongioppy.sat.value+_(B);self[_A9].text=A+config.picongioppy.type.value+_Y+C+config.picongioppy.dttmod.value+_(B)
			elif config.picongioppy.dtt.value==_A and config.picongioppy.sat_value.value==_B:self.restart_on();self[_A9].text=A+config.picongioppy.type.value+_Y+C+config.picongioppy.dttmod.value+_(B)
			elif config.picongioppy.dtt.value==_B and config.picongioppy.sat_value.value==_A:self.restart_on();self[_i].text=A+config.picongioppy.type.value+_Y+config.picongioppy.sat.value+_(B)
	def close_screen_picon(self):
		config.picongioppy.type.save();config.picongioppy.dest.save();config.picongioppy.dimens.save();config.picongioppy.sat.save();config.picongioppy.dtt.save();config.picongioppy.main.save();config.picongioppy.dttmod.save();config.picongioppy.sat_value.save();config.picongioppy.piconsupdate.save();configfile.save()
		if self.status_download==_A or self.status2_download==_A:self.session.openWithCallback(self.close_screen_picon_callback,MessageBox,_('Do you want to stop the download?'),MessageBox.TYPE_YESNO)
		else:self.close()
	def close_screen_picon_callback(self,answer):
		if answer is _A:
			if self.status_download==_A and self.status2_download==_A:self.download.stop();self.downloads.stop();self[_A0].value=int(0);self[_i].text='';self[_AN].value=int(0);self[_A9].text='';self.close()
			if self.status_download==_A and self.status2_download==_B:self.download.stop();self[_A0].value=int(0);self[_i].text='';self.close()
			if self.status_download==_B and self.status2_download==_A:self.downloads.stop();self[_AN].value=int(0);self[_A9].text='';self.close()
class ChangeLog(Screen):
	def __init__(self,session):
		if getDesktop(0).size().width()==1920:skin=skins+'ChangeLogfhd.xml'
		else:skin=skins+'ChangeLoghd.xml'
		f=open(skin,_C);self.skin=f.read();f.close();Screen.__init__(self,session);self.session=session;self.timer=eTimer();self[_AD]=StaticText(_(_Ar));self[_Z]=ScrollLabel();self[_L]=Label(_(_A6)%version);self[_AO]=ActionMap([_As,_AU,_At,_AV],{_AB:self.Cancel,'up':self[_Z].pageUp,'down':self[_Z].pageDown,_y:self.Cancel},-1)
		try:self.timer.callback.append(self.changeL)
		except:self.timer_conn=self.timer.timeout.connect(self.changeL)
		self.timer.start(100,1)
	def Cancel(self):self.close()
	def changeL(self):
		A='http://gioppygio.it/update/changelog_eng.txt';leng=config.osd.language.value
		if leng=='it_IT':url='http://gioppygio.it/update/changelog.txt'
		elif leng=='en_US':url=A
		else:url=A
		try:req=Request(url,_D,{_I:_J});context=ssl._create_unverified_context();changelog=urlopen(req,timeout=5,context=context);line=changelog.read();read_changelog=str(line.decode(_E))
		except HTTPError as e:print(_AG,e.code);read_changelog=''
		except URLError as e:print(_AH,e.reason);read_changelog=''
		except Exception:read_changelog=''
		self[_Z].setText(read_changelog)
class TesterImage(Screen):
	def __init__(self,session):
		if getDesktop(0).size().width()==1920:skin=skins+'TesterImagefhd.xml'
		else:skin=skins+'TesterImagehd.xml'
		f=open(skin,_C);self.skin=f.read();f.close();Screen.__init__(self,session);self.session=session;self[_AD]=StaticText(_(_Ar));self['tested']=Label(_('TESTED ON'));self['special']=Label(_('My thanks go to those who support me, and appreciate my work (hobby) every day.'));self[_AO]=ActionMap([_As,_AU,_At,_AV],{_AB:self.Cancel,_y:self.Cancel},-1)
	def Cancel(self):self.close()
class PiconsNews(Screen):
	def __init__(self,session):
		if getDesktop(0).size().width()==1920:skin=skins+'LogPiconsfhd.xml'
		else:skin=skins+'LogPiconshd.xml'
		f=open(skin,_C);self.skin=f.read();f.close();Screen.__init__(self,session);self.session=session;self.timer=eTimer();self[_AD]=StaticText(_(_Ar));self[_Z]=ScrollLabel();self[_L]=Label(_(_A6)%version);self[_AO]=ActionMap([_As,_AU,_At,_AV],{_AB:self.Cancel,'up':self[_Z].pageUp,'down':self[_Z].pageDown,_y:self.Cancel},-1)
		try:self.timer.callback.append(self.changeL)
		except:self.timer_conn=self.timer.timeout.connect(self.changeL)
		self.timer.start(100,1)
	def Cancel(self):self.close()
	def changeL(self):
		url='http://gioppygio.it/update/changelogpicons.txt'
		try:req=Request(url,_D,{_I:_J});context=ssl._create_unverified_context();changelogpicons=urlopen(req,timeout=5,context=context);line=changelogpicons.read();read_changelogpicons=str(line.decode(_E))
		except HTTPError as e:print(_AG,e.code);read_changelogpicons=''
		except URLError as e:print(_AH,e.reason);read_changelogpicons=''
		except Exception:read_changelogpicons=''
		self[_Z].setText(read_changelogpicons)
config.plugins.TerrestrialScan=ConfigSubsection()
config.plugins.TerrestrialScan.networkid_bool=ConfigYesNo(default=_B)
config.plugins.TerrestrialScan.networkid=ConfigInteger(default=0,limits=(0,65535))
config.plugins.TerrestrialScan.clearallservices=ConfigYesNo(default=_A)
config.plugins.TerrestrialScan.onlyfree=ConfigYesNo(default=_B)
config.plugins.TerrestrialScan.skipT2=ConfigYesNo(default=_B)
uhf_vhf_choices=[(_Au,_('UHF/VHF Europe')),('uhf',_('UHF Europe')),('uhf_short',_('UHF Europe channels 21-49')),(_B9,_('Australia generic'))]
try:
	if nimmanager.getTerrestrialsList():uhf_vhf_choices.append(('xml',_('From XML')))
except ImportError:pass
config.plugins.TerrestrialScan.uhf_vhf=ConfigSelection(default=_Au,choices=uhf_vhf_choices)
config.plugins.TerrestrialScan.makebouquet=ConfigYesNo(default=_A)
config.plugins.TerrestrialScan.makeradiobouquet=ConfigYesNo(default=_B)
config.plugins.TerrestrialScan.makexmlfile=ConfigYesNo(default=_A)
config.plugins.TerrestrialScan.lcndescriptor=ConfigSelection(default=131,choices=[(131,'0x83'),(135,'0x87')])
config.plugins.TerrestrialScan.channel_list_id=ConfigInteger(default=0,limits=(0,65535))
config.plugins.TerrestrialScan.stabliseTime=ConfigSelection(default=2,choices=[(i,'%d'%i)for i in range(2,11)])
class DTTTerrestrialScan(ConfigListScreen,Screen):
	def __init__(self,session):
		if getDesktop(0).size().width()==1920:skin=skins+'DTTfhd.xml'
		else:skin=skins+'DTThd.xml'
		f=open(skin,_C);self.skin=f.read();f.close();Screen.__init__(self,session);self.setup_title=_('GioppyGio - Terrestrial Scanner');Screen.setTitle(self,self.setup_title);self[_L]=Label(_(_A6)%version);self[_t]=Pixmap();self[_t].hide();self.onChangedEntry=[];self.session=session;ConfigListScreen.__init__(self,[],session=session,on_change=self.changedEntry);self['actions2']=ActionMap([_AV,_AU],{_Z:self.keyCancel,_y:self.keyCancel,'save':self.keyGo,_t:self.sendEmail},-2);self[_AD]=StaticText(_('Exit'));self[_Ae]=StaticText(_('Scan'));self[_BA]=Label('');self[_AF]=Label('');self[_Av]=Label('');self.transponders_unique={};self.session.postScanService=self.session.nav.getCurrentlyPlayingServiceOrGroup();self.dvbt_capable_nims=[]
		for nim in nimmanager.nim_slots:
			if self.config_mode(nim)!='nothing':
				if nim.isCompatible(_m)or nim.isCompatible('DVB-S')and nim.canBeCompatible(_m):self.dvbt_capable_nims.append(nim.slot)
		nim_list=[];nim_list.append((-1,_('Automatic')))
		for x in self.dvbt_capable_nims:nim_list.append((nimmanager.nim_slots[x].slot,nimmanager.nim_slots[x].friendly_full_description))
		self.scan_nims=ConfigSelection(choices=nim_list);self.createSetup()
		if not self.selectionChanged in self[_U].onSelectionChanged:self[_U].onSelectionChanged.append(self.selectionChanged)
		self.selectionChanged()
	def sendEmail(self):
		A='/var/run/resolvconf/interfaces'
		if os.path.exists(_V):
			tun_vpn=_B
			if'openvpn'in str(os.listdir('/var/run')):
				try:
					check_tun=os.popen('ip tuntap show').read().split()[0]
					if'tun0:'in check_tun:tun_vpn=_A
				except IndexError:pass
			if os.path.exists(A):
				if'wg0'in str(os.listdir(A)):
					try:
						check_wireguard=os.popen('wg show').read().split()
						if'handshake:'in check_wireguard:tun_vpn=_A
					except IndexError:pass
			if tun_vpn==_B:self.session.openWithCallback(self.sendInput,MessageBox,_('Do you want to send the Dtt Scan to GioppyGio?\nIn the next step, write your City/Province and your name (NikName)'),MessageBox.TYPE_YESNO,default=_B)
			else:self.session.open(MessageBox,_('Please disable the VPN to be able to send the list to GioppyGio'),MessageBox.TYPE_INFO)
		else:0
	def sendInput(self,result):
		if result:email=_('Write (Ex: Naples - Gioppy)');self.session.openWithCallback(self.send_email,VirtualKeyBoard,title=email,text='')
		else:0
	def send_email(self,word=_D):
		self.A=word
		if self.A is not _D and len(self.A):
			excluded_words=['vaffa','fanculo','idiota','vaffanculo','imbecille','coglione','puttana','scemo','cretino','merda','bastardo','figliodiputtana','figlio di puttana','cerebroleso','ignorante','schifo','suca','frocio','ricchione','culo','cazzo','pene','sperma','fallo','maroni','merdaccia','merdata','merdoso','minchia','inchiappettare','inculata','inculato','ingroppare','stronzo','minkia','minkiaa','kazzo','buttana','buttanazza','fuck off','idiot','fuck it','jerk','whore','fool','shit','bastard','son of a bitch','brain damaged','ignorant','crap','fagot','asshole','ass','dick','penis','sperm','foul','fuck','bugger','buggered','demented','pussyhole','porn','porn hub','hub','porno']
			for keyword_excluded in excluded_words:
				if keyword_excluded in self.A.lower():self.session.open(MessageBox,_('Watch out! You are using (%s) as an inappropriate word or expression')%keyword_excluded,MessageBox.TYPE_INFO);return
			try:
				if os.path.exists(_N):os.remove(_N)
				from smtplib import SMTP_SSL,SMTPConnectError,SMTPServerDisconnected;from email.mime.application import MIMEApplication;from email.mime.multipart import MIMEMultipart;from email.mime.text import MIMEText;date_now=date.today();mail_content=self.A;py=sys.version;html='\n\t\t\t\t\t<html>\n\t\t\t\t\t\t<body>\n\t\t\t\t\t\t\t<h1>File Settings ricevuto dal plugin GioppyGio Versione %s</h1><br>\n\t\t\t\t\t\t\t<b>Settings channel: %s</b><br>\n\t\t\t\t\t\t\t<b>Ricevuto in data: %s</b><br><br>\n\t\t\t\t\t\t\t<h1>INFORMAZIONI DECODER</h1><br>\n\t\t\t\t\t\t\t<b>Modello Decoder: %s</b><br>\n\t\t\t\t\t\t\t<b>Team Image: %s</b><br>\n\t\t\t\t\t\t\t<b>Versione python: %s</b>\n\t\t\t\t\t\t</body>\n\t\t\t\t\t</html>\n\t\t\t\t\t'%(version,mail_content,date_now.strftime(_l),str(stb).upper(),images_exec,py);sender1=b64decode(eTnCgFyIDkxGNSqQXVOOttBjvaw(_BB,b64encode(eTnCgFyIasdfghwerDkxGNSqQrtydfgzxcXVOtBjvaw.encode(_E)).decode(_E)));sender2=sender1.decode(_E);sender_address=str(sender2);sender_pass1=b64decode(eTnCgFyIDkxGNSqQXVOOttBjvaw(_BC,b64encode(eTnCgFyIasdfghwerDkxGNSqQrtydfgzxcXVOtBjvaw.encode(_E)).decode(_E)));sender_pass2=sender_pass1.decode(_E);sender_pass=str(sender_pass2);receiver_address1=b64decode(eTnCgFyIDkxGNSqQXVOOttBjvaw(_BD,b64encode(eTnCgFyIasdfghwerDkxGNSqQrtydfgzxcXVOtBjvaw.encode(_E)).decode(_E)));receiver_address2=receiver_address1.decode(_E);receiver_address=str(receiver_address2);message=MIMEMultipart();message['From']=sender_address;message['To']=receiver_address;message['Subject']=_BE;message.attach(MIMEText(html,'html'));file_zip=open(_V,'rb');file_attachment=MIMEApplication(file_zip.read());file_attachment.add_header(_BF,_BG);message.attach(file_attachment);context=ssl.create_default_context()
				if py_version==2:session=SMTP_SSL(_AW,465)
				else:session=SMTP_SSL(_AW,465,context=context)
				session.login(sender_address,sender_pass);text=message.as_string();session.sendmail(sender_address,receiver_address,text);session.quit();os.remove(_V);self.hide_png()
				with open(_N,_H)as f:f.write(date_now.strftime(_l))
				with open(_N,_C)as f:dates=f.read()
				self[_AF].setText(_(_AX)%dates);self.session.open(MessageBox,_(_Aw)%self.A,MessageBox.TYPE_INFO)
			except SMTPConnectError:self.session.open(MessageBox,_(_AY),MessageBox.TYPE_INFO)
			except SMTPServerDisconnected:print(_AY);self.resendemail()
		else:self.session.open(MessageBox,_('Please write the name of the City/Province'),MessageBox.TYPE_INFO)
	def resendemail(self):
		try:
			if os.path.exists(_N):os.remove(_N)
			from smtplib import SMTP_SSL,SMTPConnectError,SMTPServerDisconnected;from email.mime.application import MIMEApplication;from email.mime.multipart import MIMEMultipart;from email.mime.text import MIMEText;date_now=date.today();mail_content=self.A;py=sys.version;html='\n\t\t\t\t<html>\n\t\t\t\t\t<body>\n\t\t\t\t\t\t<h1>File Settings ricevuto dal plugin GioppyGio Versione %s</h1><br>\n\t\t\t\t\t\t<b>Settings channel: %s</b><br>\n\t\t\t\t\t\t<b>Ricevuto in data: %s</b><br><br>\n\t\t\t\t\t\t<h1>INFORMAZIONI DECODER</h1><br>\n\t\t\t\t\t\t<b>Modello Decoder: %s</b><br>\n\t\t\t\t\t\t<b>Team Image: %s</b><br>\n\t\t\t\t\t\t<b>Versione python: %s</b>\n\t\t\t\t\t</body>\n\t\t\t\t</html>\n\t\t\t\t'%(version,mail_content,date_now.strftime(_l),str(stb).upper(),images_exec,py);sender1=b64decode(eTnCgFyIDkxGNSqQXVOOttBjvaw(_BB,b64encode(eTnCgFyIasdfghwerDkxGNSqQrtydfgzxcXVOtBjvaw.encode(_E)).decode(_E)));sender2=sender1.decode(_E);sender_address=str(sender2);sender_pass1=b64decode(eTnCgFyIDkxGNSqQXVOOttBjvaw(_BC,b64encode(eTnCgFyIasdfghwerDkxGNSqQrtydfgzxcXVOtBjvaw.encode(_E)).decode(_E)));sender_pass2=sender_pass1.decode(_E);sender_pass=str(sender_pass2);receiver_address1=b64decode(eTnCgFyIDkxGNSqQXVOOttBjvaw(_BD,b64encode(eTnCgFyIasdfghwerDkxGNSqQrtydfgzxcXVOtBjvaw.encode(_E)).decode(_E)));receiver_address2=receiver_address1.decode(_E);receiver_address=str(receiver_address2);message=MIMEMultipart();message['From']=sender_address;message['To']=receiver_address;message['Subject']=_BE;message.attach(MIMEText(html,'html'));file_zip=open(_V,'rb');file_attachment=MIMEApplication(file_zip.read());file_attachment.add_header(_BF,_BG);message.attach(file_attachment);context=ssl.create_default_context()
			if py_version==2:session=SMTP_SSL(_AW,465)
			else:session=SMTP_SSL(_AW,465,context=context)
			session.login(sender_address,sender_pass);text=message.as_string();session.sendmail(sender_address,receiver_address,text);session.quit();os.remove(_V);self.hide_png()
			with open(_N,_H)as f:f.write(date_now.strftime(_l))
			with open(_N,_C)as f:dates=f.read()
			self[_AF].setText(_(_AX)%dates);self.session.open(MessageBox,_(_Aw)%self.A,MessageBox.TYPE_INFO)
		except SMTPConnectError:self.session.open(MessageBox,_(_AY),MessageBox.TYPE_INFO)
		except SMTPServerDisconnected:
			print(_AY)
			if mod_image.lower()==_A_ or mod_image.lower()==_Ab or mod_image.lower()==_Aa or mod_image.lower()==_o or mod_image.lower()=='openatv'or mod_image.lower()=='teamblue'or mod_image.lower()==_B0 or mod_image.lower()==_o or mod_image.lower()==_B1 or mod_image.lower()=='opennfr'or mod_image.lower()=='openhdf'or mod_image.lower()=='openspa'or mod_image.lower()=='openvix'or mod_image.lower()=='pure2'or mod_image.lower()==_B2 or mod_image.lower()==_B3 or mod_image.lower()==_B4 or mod_image.lower()=='openbh'or mod_image.lower()==_B5 or mod_image.lower()=='opentr'or mod_image.lower()==_AA:
				if os.path.exists(_V):os.remove(_V)
				self.hide_png()
				with open(_N,_H)as f:f.write(date_now.strftime(_l))
				with open(_N,_C)as f:dates=f.read()
				self[_AF].setText(_(_AX)%dates);self.session.open(MessageBox,_(_Aw)%self.A,MessageBox.TYPE_INFO)
	def show_png(self):self[_t].show();self[_Av].setText(_('Send the scan to GioppyGio'))
	def hide_png(self):self[_t].hide();self[_Av].setText('')
	def createSetup(self):
		self.indent='- ';setup_list=[];setup_list.append(getConfigListEntry(_('Tuner'),self.scan_nims,_('Select a tuner that is configured for terrestrial scans. "Automatic" will pick the highest spec available tuner.')));setup_list.append(getConfigListEntry(_('Bandplan'),config.plugins.TerrestrialScan.uhf_vhf,_('Most transmitters in European countries only have TV channels in the UHF band. Select "UHF Europe channels 21-49" in countries that are now using channels 50+ for GSM. Select "From XML" to access bandplans that are preloaded on the device.')))
		if config.plugins.TerrestrialScan.uhf_vhf.value=='xml':self.setTerrestrialLocationEntries();setup_list.append(self.terrestrialCountriesEntry);setup_list.append(self.terrestrialRegionsEntry)
		setup_list.append(getConfigListEntry(_('Clear before scan'),config.plugins.TerrestrialScan.clearallservices,_('If you select "yes" all stored terrestrial channels will be deleted before starting the current search.')))
		if config.plugins.TerrestrialScan.uhf_vhf.value not in(_B9,):setup_list.append(getConfigListEntry(_('Skip T2'),config.plugins.TerrestrialScan.skipT2,_('If you know for sure there are no T2 multiplexes in your area select yes. This will speed up scan time.')))
		setup_list.append(getConfigListEntry(_('Only free scan'),config.plugins.TerrestrialScan.onlyfree,_('If you select "yes" the scan will only save channels that are not encrypted; "no" will find encrypted and non-encrypted channels.')));setup_list.append(getConfigListEntry(_('Restrict search to single ONID'),config.plugins.TerrestrialScan.networkid_bool,_('Select "Yes" to restrict the search to multiplexes that belong to a single original network ID (ONID). Select "No" to search all ONIDs.')))
		if config.plugins.TerrestrialScan.networkid_bool.value:setup_list.append(getConfigListEntry(self.indent+_('ONID to search'),config.plugins.TerrestrialScan.networkid,_('Enter the original network ID (ONID) of the multiplexes you wish to restrict the search to. UK terrestrial television normally ONID "9018".')))
		setup_list.append(getConfigListEntry(_('Create terrestrial bouquet'),config.plugins.TerrestrialScan.makebouquet,_('If you select "yes" and LCNs are found in the NIT, the scan will create a bouquet of terrestrial channels in LCN order and add it to the bouquet list.')))
		if config.plugins.TerrestrialScan.makebouquet.value:
			setup_list.append(getConfigListEntry(self.indent+_('Create separate radio bouquet'),config.plugins.TerrestrialScan.makeradiobouquet,_('If you select "yes" and radio services are fond these will be place in a separate bouquet. Otherwise TV and radio services will be placed in a combined bouquet.')));setup_list.append(getConfigListEntry(self.indent+_('LCN Descriptor'),config.plugins.TerrestrialScan.lcndescriptor,_('Select the LCN descriptor used in your area. 0x83 is the default DVB standard descriptor. 0x87 is used in some Scandinavian countries.')))
			if config.plugins.TerrestrialScan.lcndescriptor.value==135:setup_list.append(getConfigListEntry(self.indent+self.indent+_('Channel list ID'),config.plugins.TerrestrialScan.channel_list_id,_('Enter channel list ID used in your area. If you are not sure enter zero.')))
		if config.plugins.TerrestrialScan.uhf_vhf.value!='xml':setup_list.append(getConfigListEntry(_('Create terrestrial.xml file'),config.plugins.TerrestrialScan.makexmlfile,_('Select "yes" to create a custom terrestrial.xml file and install it in /etc/enigma2 for system scans to use.')))
		setup_list.append(getConfigListEntry(_('Signal quality stabisation time (secs)'),config.plugins.TerrestrialScan.stabliseTime,_('Period of time to wait for the tuner to stabalise before taking a signal quality reading. 2 seconds is good for most hardware but some may require longer.')));self[_U].list=setup_list;self[_U].l.setList(setup_list)
	def setTerrestrialLocationEntries(self):
		slotid=self.dvbt_capable_nims[0]if self.scan_nims.value<0 else self.scan_nims.value;nimConfig=nimmanager.nim_slots[slotid].config
		if not hasattr(self,'terrestrialCountriesEntry'):terrestrialcountrycodelist=nimmanager.getTerrestrialsCountrycodeList();terrestrialcountrycode=nimmanager.getTerrestrialCountrycode(slotid);default=terrestrialcountrycode in terrestrialcountrycodelist and terrestrialcountrycode or _D;choices=[(_AA,_('All'))]+sorted([(x,self.countrycodeToCountry(x))for x in terrestrialcountrycodelist],key=lambda listItem:listItem[1]);self.terrestrialCountries=ConfigSelection(default=default,choices=choices);self.terrestrialCountriesEntry=getConfigListEntry(self.indent+_('Country'),self.terrestrialCountries,_("Select your country. If not available select 'all'."))
		if self.terrestrialCountries.value==_AA:
			try:terrstrialNames=[x[0]for x in sorted(sorted(nimmanager.getTerrestrialsList(),key=lambda listItem:listItem[0]),key=lambda listItem:self.countrycodeToCountry(listItem[2]))]
			except ImportError:pass
		else:terrstrialNames=sorted([x[0]for x in nimmanager.getTerrestrialsByCountrycode(self.terrestrialCountries.value)])
		try:NConfig=nimConfig.terrestrial.value
		except:NConfig=nimConfig.dvbt.terrestrial.value
		default=NConfig in terrstrialNames and NConfig or _D;self.terrestrialRegions=ConfigSelection(default=default,choices=terrstrialNames);self.terrestrialRegionsEntry=getConfigListEntry(self.indent+_('Region'),self.terrestrialRegions,_("Select your region. If not available change 'Country' to 'all' and select one of the default alternatives."))
	def countrycodeToCountry(self,cc):
		if not hasattr(self,'countrycodes'):
			self.countrycodes={}
			try:
				from Tools.CountryCodes import ISO3166
				for country in ISO3166:self.countrycodes[country[2]]=country[0]
			except ImportError:
				from Components.International import international
				for country in international.COUNTRY_DATA.values():self.countrycodes[country[international.COUNTRY_ALPHA3]]=country[international.COUNTRY_TRANSLATED]
		if cc.upper()in self.countrycodes:return self.countrycodes[cc.upper()]
		return cc
	def selectionChanged(self):
		if os.path.exists(_V):self.show_png()
		else:self.hide_png()
		if os.path.exists(_N):
			with open(_N,_C)as f:dates=f.read();self[_AF].setText(_(_AX)%dates)
		self[_BA].setText(self[_U].getCurrent()[2])
	def changedEntry(self):
		for x in self.onChangedEntry:x()
	def getCurrentEntry(self):return self[_U].getCurrent()[0]
	def getCurrentValue(self):return str(self[_U].getCurrent()[1].getText())
	def createSummary(self):from Screens.Setup import SetupSummary;return SetupSummary
	def keyGo(self):
		if os.path.exists(_V):os.remove(_V);self.hide_png()
		for x in self[_U].list:x[1].save()
		configfile.save();self.startScan()
	def startScan(self):
		args={'feid':int(self.scan_nims.value),_Au:config.plugins.TerrestrialScan.uhf_vhf.value,_BH:int(config.plugins.TerrestrialScan.networkid.value),'restrict_to_networkid':config.plugins.TerrestrialScan.networkid_bool.value,'stabliseTime':config.plugins.TerrestrialScan.stabliseTime.value,'skipT2':config.plugins.TerrestrialScan.skipT2.value}
		if config.plugins.TerrestrialScan.uhf_vhf.value=='xml':args['country']=self.terrestrialCountries.value;args['region']=self.terrestrialRegions.value
		self.session.openWithCallback(self.terrestrialScanCallback,TerrestrialScanGio,args)
	def keyCancel(self):
		if self[_U].isChanged():self.session.openWithCallback(self.cancelCallback,MessageBox,_('Really close without saving settings?'))
		else:self.cancelCallback(_A)
	def keyLeft(self):ConfigListScreen.keyLeft(self);self.newConfig()
	def keyRight(self):ConfigListScreen.keyRight(self);self.newConfig()
	def keySelect(self):ConfigListScreen.keySelect(self);self.newConfig()
	def newConfig(self):
		cur=self[_U].getCurrent()
		if len(cur)>1:
			if cur[1]in(config.plugins.TerrestrialScan.uhf_vhf,getattr(self,'terrestrialCountries',_D),config.plugins.TerrestrialScan.networkid_bool,config.plugins.TerrestrialScan.makebouquet,config.plugins.TerrestrialScan.lcndescriptor):self.createSetup()
	def cancelCallback(self,answer):
		if answer:
			for x in self[_U].list:x[1].cancel()
			self.close(_B)
	def terrestrialScanCallback(self,answer=_D):
		print('answer',answer)
		if answer:
			self.feid=answer[0];self.transponders_unique=answer[1]
			if config.plugins.TerrestrialScan.makebouquet.value or config.plugins.TerrestrialScan.makexmlfile.value:self.session.openWithCallback(self.MakeBouquetCallback,MakeBouquet,{'feid':self.feid,'transponders_unique':self.transponders_unique,'FTA_only':config.plugins.TerrestrialScan.onlyfree.value,'makebouquet':config.plugins.TerrestrialScan.makebouquet.value,'makexmlfile':config.plugins.TerrestrialScan.makexmlfile.value,'lcndescriptor':config.plugins.TerrestrialScan.lcndescriptor.value,'channel_list_id':config.plugins.TerrestrialScan.channel_list_id.value})
			else:self.doServiceSearch()
		else:self.session.nav.playService(self.session.postScanService)
	def MakeBouquetCallback(self,answer=_D):
		print('answer',answer)
		if answer:self.feid=answer[0];self.transponders_unique=answer[1];self.doServiceSearch()
		else:self.session.nav.playService(self.session.postScanService)
	def doServiceSearch(self):
		tlist=[]
		for transponder in self.transponders_unique:tlist.append(setParams(self.transponders_unique[transponder]['frequency'],self.transponders_unique[transponder]['system'],self.transponders_unique[transponder]['bandwidth']))
		self.startServiceSearch(tlist,self.feid)
	def startServiceSearch(self,tlist,feid):
		flags=0
		if config.plugins.TerrestrialScan.clearallservices.value:flags|=eComponentScan.scanRemoveServices
		else:flags|=eComponentScan.scanDontRemoveUnscanned
		if config.plugins.TerrestrialScan.onlyfree.value:flags|=eComponentScan.scanOnlyFree
		networkid=0;self.session.openWithCallback(self.startServiceSearchCallback,Scandtt,[{'transponders':tlist,'feid':feid,'flags':flags,_BH:networkid}])
	def startServiceSearchCallback(self,answer=_D):
		C='/etc/enigma2/lamedb';B='/etc/enigma2/bouquets.tv';A='/etc/enigma2/userbouquet.TerrestrialScan.tv'
		if os.path.exists(A)and os.path.exists(B)and os.path.exists(C):
			if py_version==2:zipObj=ZipFile(_V,_H)
			else:zipObj=ZipFile(_V,_H,strict_timestamps=_B)
			zipObj.write(A);zipObj.write(B);zipObj.write(C);zipObj.close();self.show_png()
		else:0
		self.session.nav.playService(self.session.postScanService)
		if answer:self.close(_A)
	def config_mode(self,nim):
		try:return nim.config_mode
		except AttributeError:return nim.isCompatible(_m)and nim.config_mode_dvbt or'nothing'
jsession=_D
iTimerClass=GioppyGioSettings(jsession)
def SessionStart(reason,**kwargs):
	A='session'
	if reason==0:iTimerClass.gotSession(kwargs[A])
	jsession=kwargs[A]
iTimerClass=GioppyGioSettings(jsession)
def AutoStart(reason,**kwargs):
	if reason==1:iTimerClass.StopTimer()
def mainmenu(menu_id,**kwargs):
	if menu_id=='mainmenu':return[(_(_AZ+version),Main,'GioppyGio',40)]
	else:return[]
def Main(session,**kwargs):session.open(intro_gioppy)
def Plugins(**kwargs):
	A='Channel Settings and Picons';list=[]
	if getDesktop(0).size().width()==1920:list.append(PluginDescriptor(name=_AZ+version,description=_(A),icon='plugin.png',where=[PluginDescriptor.WHERE_EXTENSIONSMENU,PluginDescriptor.WHERE_PLUGINMENU],fnc=Main))
	else:list.append(PluginDescriptor(name=_AZ+version,description=_(A),icon='pluginhd.png',where=[PluginDescriptor.WHERE_EXTENSIONSMENU,PluginDescriptor.WHERE_PLUGINMENU],fnc=Main))
	list.append(PluginDescriptor(where=PluginDescriptor.WHERE_SESSIONSTART,fnc=SessionStart));list.append(PluginDescriptor(where=PluginDescriptor.WHERE_AUTOSTART,fnc=AutoStart))
	if config.picongioppy.main.getValue():list.append(PluginDescriptor(name=_AZ+version,description=_(A),where=PluginDescriptor.WHERE_MENU,fnc=mainmenu,needsRestart=_A))
	return list
