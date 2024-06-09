#!/usr/bin/env python3

import base64
import subprocess
import sys
import tempfile

subprocess.call([ 'pip', 'install' , 'inquirer', '-q' ])

import inquirer

from facefusion import logger, metadata

NAME = 'PATCH'
VERSION = '2.6.0'

PRE_PATCH = 'Q*~l$Wn*+YAX`vDR6|HzAaG%HV`w0AY;SaP3N0-y3Q2BcWq3LuW?^GxW_5FEZ*DJea&Kd0b8~NUb1!CcVQpnEba`-TZfA2YaCr(zL`6X$VPs@!bZKvHVQe62Zf0*f3R87rb9r-gWo<ejV{dIPX>N37Y;0+2E^lyUZeeg~E@WwDW-e)MaBMDcVRU0?E<<Qxa&u*LMNkSnD?U|JMlCoBJv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`NWNBt*AT2FtX>=fAFJ@t5WoC7AX>V>XaB^>BWpi_Ha&s?ca$#*{FLZfuX>Mn8E^v7uVlQT4V`XM_b7^mGFK}{iV`X!5Z*p@lW^!R|WiNDjaA|I5b1ras3N0-yAYm_NVPj=xb#rNNZZB|hZ)0V1b8m8UFJ^LKZDlWXd2nfNXLBxac?l?TWp-(EX>V>IV`XM!GG<{kF=Q|{W;QrxH#0V4G-NPiF*ao}VK`wlV>vZBHeoe5DGDnqD<EPoW?^GxW_5FEZ*DJea&Kd0b8~NUb1!CcVQpnEba`-TZfA2YaCr$RWMOn=ATc*FHZ(UlI5IIbHZv&-KtLcZGdV0XAS*LDEH*SCKtKv02`6)Jb#h~6Utx7*X>VU<a$#*{Cm=c?L3LzlZ$@%qZDlM9APFaQVRC0>bYFI9b7^mGUuJS)ZDl7QIv`eQb7^mGMsi_oWeOmDDGDnJD<cXkBMK`c3M(TDD<cXkBOp*gR6|HDQ%p}(Eino!BMK`c3M(TDD<cXkBMK`c3M(TDD<cXkBMK`c3M(TZP(f5fNG(%LPgE^33M(TDD<cXkBMK`c3M(TDD<cXkBMK`c3M(TDD<cXkBOp*gR6|HDQ%p}(Ei(!$BMK`c3M(TDD<cXkBMK`c3M(TDD<cXkBMK`c3M(TZP(f5fNG(%LPgE^53M(TDD<cXkBMK`c3M(TDD<cXkBMK`c3M(TDD<cXkBOp*gR6|HDQ%p}(Ej0=&BMK`c3M(TDD<cXkBMK`c3M(TDD<cXkBMK`c3Q2BcWq3LuW?^GxW_5FEZ*DJea&Kd0b8~NUb1!CcVQpnEV`y(_V`XzLaCr(zL`6X$VPs@!bZKvHVQe62Zf0*f3R87rb9r-gWo<ejV{dIPX>N37Y;0+2E^lyUZeeg~E@WwDW-e)MaBMDcVRU0?E<<Qxa&u*LMNkSnD?U|JMlCoBJv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`NWNBt*AT2FtX>=fAFJ@t5WoC7AX>V>XaB^>BWpi_Ha&s?ca$#*{FJowLX=7z`E^v7uVlQT4V`XM_b7^mGFK}{iV`X!5Z*p@lW^!R|WiMlBZ)sy?b1ras3N0-yAYm_NVPj=xb#rNNZZB|hZ)0V1b8m8UFJ^LKZDlWGXm4p_WpgfYc?l?TWp-(EX>V>IV`XM!GG<{kF=Q|{W;QrxH#0V4G-NPiF*ao}VK`wlV>vZBHeoe5DGDnqD<EPoW?^GxW_5FEZ*DJea&Kd0b8~NUb1!CcVQpnEV`y(_V`XzLaCr$RWMOn=ATc*FHZ(UlI5IIbH908?KtLcZF*GbQAS*F6EH*SCKtKv0W?^GxUuAA+VQyn(a$jO>Wo~3&a$#;~Wgt2rOlfm;TWM}|T_8OmV{&C-bY)*@ZggLAVQyz-C@?G_F)%PJATcQlAZBu5ZDn6$Z)|UJX?kUHUt(-!Ze(9_VQyz-AUYsSX>)X2X>N2~AUz;sa%Ew3WnXD-bYF5|Zf9jEFf1T3Ffc42F)0clW^!R|WnX1(Xkl(+WpZC)Y-Mg_Uvgn?XJsHdAWUg<bX#d|bX_1lAY*c6VRU6*X>N31a$#;~WhgK#ATcm7EFdu{3M&dLBMK`c3M(TDD<cXkBMK`cAW%V6Lr5)COixrTF$yaq3M(TDD<cXkBMK`c3M(TDD<cXkBMK`c3M(TDD<dFKK~zIXEmKTSR4p<JD<cXkBMK`c3M(TDD<cXkBMK`c3M(TDD<cXkBMK`cAW%V6Lr5)COixrTGYTss3M(TDD<cXkBMK`c3M(TDD<cXkBMK`c3M(TDD<dFKK~zIXEmKTSR4p_LD<cXkBMK`c3M(TDD<cXkBMK`c3M(TDD<cXkBMK`cAW%V6Lr5)COixrTH3};u3M(TDD<cXkBMK`c3M(TDD<cXkBMK`c3M(TD'
PATCH = 'Q*~l$Wn*+YAX`vDR6|HzAaHMRb!=gBAa!taV_|G%a&rnTEiDR3Ze(S6Iv{3YV`XM_b7^mGFK}{iV`X!5Z*p@lW^!R|WiM@SWOZz1b1!CcVQpn!Wo~F;ZewL~E^v7YNkm0KAYo)=X>@6CZeeU7X>Mk3Ito*DVsm+ObY*QiAY*TBE@^IbWo&F|YA$bZWo}_`X)a`GW@avFZE$QZaA9;~Xf8u&VRCb2bVX1KJS#p`R7Nd03OzkNJv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=3S?<!W*{vsXK8dGVJ~K3V`XM_b7^mGFK}{iV`X!5Z*p@lW^!R|WiM@SWOZz1b1!CcVQpn!Wo~F;ZewL~E^v7uVlQT4V`XM_b7^mGFK}{iV`X!5Z*p@lW^!R|WiM@SWOZz1b1!CcVQpn!Wo~F;ZewL~E^v7YEiEk|VJ~K3V`XM_b7^mGFK}{iV`X!5Z*p@lW^!R|WiM@SWOZz1b1!CcVQpn!Wo~F;ZewL~E^v7XC~{?XX>)0BZXjkhIASm|WHVwhG&5vkV=`qhGdDRjGi7CBVly~1V`VZiW-w!BWn(D{D=RA?VlQT4V`XM_b7^mGFK}{iV`X!5Z*p@lW^!R|WiM@SWOZz1b1!CcVQpn!Wo~F;ZewL~E^v7XC}d%DWgsy(F*Y<fH8(IcI5;*b3P3<0EjcwTHXtiGH7qnSAV5G0APEU4aA9<4CpsW<Wpi(Ac4c33Wo%(|X?A5_aA9<4C?_s1FD_wob7gdMFKusRWo&aVb!>EUVPA7-VRCR^cr-3=Zf<xdDJ%*g2?-~2X?kTRIv^-9GB_+CI4mGEDJ%*g2?-~2V_|G%CpsWB3M&bHED9?LCuVPNY-nL}WO-k5Wo=<&a%o?9G$%R=D+zlFD+viFb#iPcIv^)#baZfYIxjD1b!TU3Zf9m;V`VO5Z!czHV`XM_b7^mGFKusRWo&aVa%FRGY<6WYZDDC{FJ^CVY-nL}WO-k5Wo=<&a%o?9G%jy$Zg?jw3M&Z-CvahOXeT-#a%FRGY<6W|a%F5`bZK^FUvOb`XecKxE-x-&b8}^Mb1!XgWMyn~FJ^CVY-nL}WO-k5Wo=<&a%o?9G%jy$Zg?jtED9?L2`6)DdSxd%ASf|1I4mGIEFd%~ED9?L2`6)7VQgh5Iv_L(D+zrp3M&aGZf$F1Uvp_;cwcxlCpro%3401F2?-~4a%?9$ASY;abZ~PzFE40yXJ=_{XJ%nzWiDfHFJ@t5WoC7AX>V>XZEs{{Y;!MiWpi(Ac4aSZVQFqJZf$F1Uvp_;cwcxlE^lsbcqc3hD+viFaA9<4CpsW<Wpi(Ac4c33Wo%(|X?A5_aA9<4C?_s1FD_wob7gdMFKusRWo&aVZf$F1Uvp_;cwcxlE^lsbcqb_=3M&Z-Cv$0fWhXiyC^0fPEFd^6AT%i~3M&Z-Cv#(AY-J}pAT$aq34JUID+woZWnpYzcV%K<aA<FIZ(n#cCpro%3401F2?-~4a%?9$ASY;abZ~PzFE40yXJ=_{XJ%nzWiDfHFJ@t5WoC7AX>V>XZEs{{Y;!MiWpi(Ac4aSZVQFqJa%Ev`Uw36<UvOw|bZ=jHG%jy$Zg?jw3M&Z-CvahOXeT-#a%FRGY<6W|a%F5`bZK^FUvOb`XecKxE-x-&b8}^Mb1!XgWMyn~FLGsJY+rX}Vqb7*Z**^8cr-3=Zf<xdDJ%*r2?-~2X?kTRIv^-EG%O%AEFdx|ED9?L2`6)7VQgh5Iv_L(D+zrp3M&aGa%Ev`X>)XGV_$M*b7Ns_WpZD5G$%R=D+zlFD+viFb#iPcIv^)#baZfYIxjD1b!TU3Zf9m;V`VO5Z!czHV`XM_b7^mGFKusRWo&aVa%FRGY<6WYZDDC{FLGsJY-w|JX=7h<WpiU;Y-Ms^cr-3=Zf<xdED9?L2`6x2bZ93!AaZ4MZ)|pDUvgz^VRUJBWnXY%bZ96iE-o)FVRLh3baO9lZ)9a`b1!mbVQgu0bZKK>a%FR4VQgh`UwAYwZ*FdQCn+onD+viFb7^{ICpsV~F)}zTAUG@_G$||!D+viFb7Ns_WhXiyGzu#TeJlzq2`6)RX>KxKb8=sJG$%R=D+zlFD+viFb#iPcIv^)#baZfYIxjD1b!TU3Zf9m;V`VO5Z!czHV`XM_b7^mGFKusRWo&aVa%FRGY<6WYZDDC{FLQTkZZcnUa$k5fE^lsbcqc3hD+viFaA9<4CpsW<Wpi(Ac4c33Wo%(|X?A5_aA9<4C?_s1FD_wob7gdMFKusRWo&aVb9ZTOGGB9YUwAYwZ*FdQCn+onD+viFb7^{ICpsV~F)}zTAUG@_G$||!D+viFb7Ns_WhXiyGzuUIeF`9b3LsBVR7p=xQy@AZPjGZ;Z*F01TTgIwX>V?GS7~%;O>bmnY+WEdAWm;?WeQ1dWMz0dAZB4>WoC7AX>V>XaB^>BWpi_Ha&s?ca$#*{FLZfuX>Mn8E^v7YNkm0KAYo)=X>@6CZeeU7X>Mk3Ito*DVsm+ObY*QiAY*TBE@^IbWo&F|YA$bZWo}_`X)a`GW@avFZE$QZaA9;~Xf8u&VRCb2bVX1KJS#p`R7Nd03OzkNJv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=3S?<!W*{vsXK8dGVJ~K3V`XM_b7^mGFK}{iV`X!5Z*p@lW^!R|WiNDjaA|I5b1rasAYw0OVPj=xb#rNNZZB|hZ)0V1b8m8UFJ^LKZDlWXd2nfNXLBxac?vBpEg)epW?^GxW_5FEZ*DJea&Kd0b8~NUb1!CcVQpnEba`-TZfA2YaCr$Ra%FaDb7^mGAZ9i=VlXmfGh#6`Gh||8GG#C`H#syjWo2SwGdMG2Wil~lFk@zAV<`$ND=Q#kFJ@t5WoC7AX>V>XaB^>BWpi_Ha&s?ca$#*{FLZfuX>Mn8E^v7XC}d%DWgsy(F*Y<fH8(RfH#jpX3P3<0EjBnTIUp-GI4n6JKtKv0BMKlR3LqmOP(f5fNG(%LPgE^43N0fFEh7poBMK{Ka&K)Qba`-TZf78AZE$aLbRbo3X>V={D+(({a$#*{MQ&(eZewL~O>bmnY#==#Rc>i-Zd)Kma$#*{MQ&(eZewL~O>bmnY%Cy5X>?_BVQgC`W^Zq7Xkl_>d0%p6ZDC__X<v9WCoCW*Zf$F1Uvp_;cwcxlCoCW*a%Ev`Uw36<UvOw|bZ=jHG$$+|Cvs(BY-w|JX=7h<WpiU;Y-Ms^cr+(0ASZKoX>KxKb8=sJG$&mkT?!y03Lqm2AR`J%Ze(S6Iv{3YV`XM_b7^mGFK}{iV`X!5Z*p@lW^!R|WiMlBZ)sy?b1ras3Q0soK_FpdWNCD1Z*F01AZc!9Z#oK7bz*aQb97~GIv`_jZ7ykUbY*O8X=*NSaAj^`aA_`NX=Y|FX>D+9E^uLVV`wfzXkl`5WpqVQ3Op-5Ra8bTI0`*IJv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jql!LW@aEQEoW(TAYm_NVPj=xb#rNNZZB|hZ)0V1b8m8UFJ^LKZDlWGXm4p_WpgfYc_3mhW?^GxW_5FEZ*DJea&Kd0b8~NUb1!CcVQpnEV`y(_V`XzLaCr(XEiE8nFJ@t5WoC7AX>V>XaB^>BWpi_Ha&s?ca$#*{FJowLX=7z`E^v7XC~{?XX>)0BZXjkhIASm|WHVwhG&5vkV=`qhGdDRjGi7CBVly~1V`VZiW-w!BWn(D{D=RA?VlQT4V`XM_b7^mGFK}{iV`X!5Z*p@lW^!R|WiMlBZ)sy?b1ras2`FS?bY&nhH!(IeI5jsjG&eXiDGES9AT2aAEH@x4G&3wWAV5G0AR`JOBMKlRAW%V6Lr5)COixrTGYTyu3M*!EVQpn!Wo~F;ZewL~Uu|z>Wo&aUWq5RDZe%E1ASY&TZ)|8`a%6d5a%F8{V{&O<cr+(0ASZ5ZYh+(@X<>L@cr+(0ASZHVVQgP_Wny1&Xm50HUwAYpEFdRxWnpY-b98BAUvg!0V_|G%a$k5fCoCW*b9ZTOGGB9YUwAYpAYCa6AR`JOBMKlR3I'


def pre_check() -> None:
	if VERSION != metadata.METADATA.get('version'):
		logger.warn('Patch does not match version!', NAME)
		sys.exit(1)


def apply_patch() -> bool:
	subprocess.run([ 'git', 'clean', 'facefusion', '-f' ], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

	with tempfile.NamedTemporaryFile(mode = 'w', newline = '\n', delete = False) as pre_patch_file:
		pre_patch_file.write(base64.b85decode(PRE_PATCH).decode('utf-8'))
	pre_patch_process = subprocess.run([ 'git', 'apply', '--whitespace', 'fix', pre_patch_file.name ], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

	with tempfile.NamedTemporaryFile(mode = 'w', newline = '\n', delete = False) as patch_file:
		patch_file.write(base64.b85decode(PATCH).decode('utf-8'))
	patch_process = subprocess.run([ 'git', 'apply', '--whitespace', 'fix', patch_file.name ], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

	subprocess.run([ 'git', 'add', 'facefusion' ], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

	if pre_patch_process.returncode == 0:
		logger.info('Preparation applied!', NAME)
	else:
		logger.error('Preparation skipped!', NAME)

	if patch_process.returncode == 0:
		logger.info('Patch applied!', NAME)
		return True
	logger.error('Patch not applied!', NAME)
	return False


def undo_patch () -> bool:
	with tempfile.NamedTemporaryFile(mode = 'w', newline = '\n', delete = False) as patch_file:
		patch_file.write(base64.b85decode(PATCH).decode('utf-8'))
	process = subprocess.run([ 'git', 'apply', '--whitespace', 'fix', '--reverse', patch_file.name ], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

	if process.returncode == 0:
		logger.info('Patch undone!', NAME)
		return True
	logger.error('Patch not undone!', NAME)
	return False


def restore_codebase() -> bool:
	process = subprocess.run([ 'git', 'reset', '--hard' ], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

	if process.returncode == 0:
		logger.info('Codebase restored!', NAME)
		return True
	logger.error('Codebase not restored!', NAME)
	return False


if __name__ == '__main__':
	logger.init('info')
	pre_check()

	choices =\
	[
		'Apply patch',
		'Undo patch',
		'Restore codebase',
		'Quit'
	]
	answers = inquirer.prompt(
	[
		inquirer.List('action', message = 'Select your action', choices=choices)
	])

	if answers and answers['action'] == choices[0]:
		if not apply_patch():
			subprocess.run([sys.executable] + sys.argv)
	elif answers and answers['action'] == choices[1]:
		undo_patch()
		subprocess.run([ sys.executable ] + sys.argv)
	elif answers and answers['action'] == choices[2]:
		restore_codebase()
		subprocess.run([sys.executable] + sys.argv)
