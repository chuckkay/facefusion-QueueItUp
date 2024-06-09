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
PATCH = 'Q*~l$Wn*+YAX`vDR6|HzAaZ4GZ**lKbYXI5Wpp5RX=G(@a|$gjEec6)WMz0dAZB4>WoC7AX>V>Xb!l@iV{dJ6Z*FC7baO9sVRC0>bS`jt3Q0soK_FpdWNCD1Z*F01AZc!9Z#oK7bz*aQb97~GIv`_jZ7ykUbY*O8X=*NSaAj^`aA_`NX=Y|FX>D+9E^uLVV`wfzXkl`5WpqVQ3Op-5Ra8bTI0`*IJv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jql!LW@aEQEoW(TAYm_NVPj=xb#rNNZZCCdb1!3WZE$aHWo~qHFLYsYXJvFQaCsnNFJ@t5WoC7AX>V>Xb!l@iV{dJ6Z*FC7baO9sVRC0>bS`jt3N0-yAYm_NVPj=xb#rNNZZCCdb1!3WZE$aHWo~qHFLYsYXJvFQaCr$Ra%FaDb7^mGAZ9i=VlXmfGh#6`Gh||8GG#C`H#syjWo2SwGdMG2Wil~lFk@zAV<`$ND=Q#kFJ@t5WoC7AX>V>Xb!l@iV{dJ6Z*FC7baO9sVRC0>bS`jt2`FS?bY&nhH!(IfGc`6iG%_(ZDGES9AT2dHEH)r3H90IdAV5G0APETxbYXI5WprP5X=G(@Utw}*b6Y2NX>(~}Y-J~1AUz;da&=`2APH1KQb$EpUr9|tM@1k#AZK!6WNB|MNo`?gWhg2tbYXI5WprO@ZDD6+Utw}*b14cS2~<H+M@3X$R!KxfPar)YXL4a=X>Tr8X=G(@C@Ly+VRC0>bYFI9WMyw(VRC14DGDnIa%E>}b97~LUv+6;V{dJ6Z*FC7bSNiuVRC0>bYEs^Y-J}bAXGt8M@3X$MoCOXDGDG7a%E>}b97~LUv+6;V{dJ6Z*FC7bSNiuVRC0>bYE$0VP|D0EFe@tQb$EpUr9|tM@1<LAPI71XK8bEWpZD2X<uV+ZE$aHWo~pRCv;(QXJvF>c4=f~Zzn7uR6$ZlMO0r_Nkm0YDGCZnZe(S6Iv{3YV`XM_b7^mGFLh~iFLZfuX>MmOaCr(zL`6X$VPs@!bZKvHVQe62Zf0*f3R87rb9r-gWo<ejV{dIPX>N37Y;0+2E^lyUZeeg~E@WwDW-e)MaBMDcVRU0?E<<Qxa&u*LMNkSnD?U|JMlCoBJv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`NWNBt*AT2FtX>=fAFJ@t5WoC7AX>V>Xb!l@iba`-TZf7oVc_3mhW?^GxW_5FEZ*DJjX>%`hd2nfNXD)Dg3N0-yAYm_NVPj=xb#rNNZZCCdb1!sxaA|I5E^v7XC~{?XX>)0BZXjkhIASm|WHVwhG&5vkV=`qhGdDRjGi7CBVly~1V`VZiW-w!BWn(D{D=RA?VlQT4V`XM_b7^mGFLh~iFLZfuX>MmOaCr$RWMOn=ATc*FHZ?OfH#a#pFfb_!KtLcZH!L<FD>p1RAV5G0AX^F`2`6)Jb#h~6Utx7*X>TVi3Lpt5b8mHWV`X1yZDD6+CoBpp2`6-6a%W|9UuJ1+WhX2OAPFaQVRC0>bYE$0VP|D0ED9hACv;(QXJvF>c4=f~Zzn7YAPFaMa%FaDWp`g@a$#*{Uvq3}WMy(EEDA|(WMz0dAZB4>WoC7AX>V>XcW-iJX>MmOaCr(zL`6X$VPs@!bZKvHVQe62Zf0*f3R87rb9r-gWo<ejV{dIPX>N37Y;0+2E^lyUZeeg~E@WwDW-e)MaBMDcVRU0?E<<Qxa&u*LMNkSnD?U|JMlCoBJv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`NWNBt*AT2FtX>=fAFJ@t5WoC7AX>V>XcW-iJX>MmOaCsnNFJ@t5WoC7AX>V>XcW-iJX>MmOaCr(XEiE8nFJ@t5WoC7AX>V>XcW-iJX>MmOaCr$Ra%FaDb7^mGAZ9i=VlXmfGh#6`Gh||8GG#C`H#syjWo2SwGdMG2Wil~lFk@zAV<`$ND=Q#kFJ@t5WoC7AX>V>XcW-iJX>MmOaCr$RWMOn=ATc*FHZ?OfHaIjgGBha)KtLcZGB7nPHy|rAFf}YOFd#rc3LpsyBOrHWVq;-#Aa8JVX>V?G3LpsyCwFCHV_|JyZEs{{Uvgn&X>TVwASYKvLPJ4KAWct1MJFr@APEU4cV%K@VQpV>Wpi(Ab#!TOZeL__Z*XL9cWx&-ASYKvLPJ4KAW}tBPfS%*Nl#8EED9|N2`6`DVq;-#UuJM~Uvq3}WMy(EIv^)kMM6VCO&~^4Qzr^52?-~6WnyDtZC_?^b6<08X=G(`CpsV}S4BcYK}{e=P*W!?3M&Z-BOr8Pa%W|9AY^ZMZftL1WC|+@2`6N4cW!KNVPs!ob#!!ZZeMI+Vr6V6Iv^)RPghP%PeDW{ED9?L2`6-6a%W|9Uv+Y9Uvy=7bYgFKUu<DwWo#!pASYBoQb$EpAXQRKCoBpe34ID6eF_RmZe(S6Iv{3YV`XM_b7^mGFLh~iFKl6XZ*_EYFJxtAVRdYDE^v7YNkm0KAYo)=X>@6CZeeU7X>Mk3Ito*DVsm+ObY*QiAY*TBE@^IbWo&F|YA$bZWo}_`X)a`GW@avFZE$QZaA9;~Xf8u&VRCb2bVX1KJS#p`R7Nd03OzkNJv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=3S?<!W*{vsXK8dGVJ~K3V`XM_b7^mGFLh~iFKl6XZ*_EYFJxtAVRdYDE^v7uVlQT4V`XM_b7^mGFLh~iFKl6XZ*_EYFJxtAVRdYDE^v7YEiEk|VJ~K3V`XM_b7^mGFLh~iFKl6XZ*_EYFJxtAVRdYDE^v7XC~{?XX>)0BZXjkhIASm|WHVwhG&5vkV=`qhGdDRjGi7CBVly~1V`VZiW-w!BWn(D{D=RA?VlQT4V`XM_b7^mGFLh~iFKl6XZ*_EYFJxtAVRdYDE^v7XC}d%DWgsy(F*Y?bH8wajGBPkJ3P3<0Eix=OAS*H~Hy}Vj3Lt51aBp&SAZK!6WNB{-3Lt51aBp&SAZB4>WoC7AX>V>WXKZg`VQg~>EoO3WZ6Ic0V`XM_b7^mGE_G>hE@N+PaBps9Zgg`XX>D+Ca&#bJVsCYHEFflbVQpn!aB^>BWpi_Ha&s&oW^!R|WnXY|Z)0V1b8m8UUvF@9X>V?GEFfigWn*=8X>V>UAZ2)EV|8?CZ*E_7XmVv?WM5-%b#8PlAZ2)EV|8?CZ*E_4b!ByBUt@1|ZgealZDnn5a(OHubY*RDUuJS)ZDlMVZ*_EVb#z~EaCB*JZgVUkV{dJ3Z*E_2aCB*JZgVUkb8mHWV`VHLbYXI5WppecZ*_EVb#yEsaB^jKX=QgTAartRZC_?`VQpnBAZB4>WnW=#VQhJGWpXSaW?^GxUvp(_Wn*-2ax5TbVPj=qZDDh3WpWBDW^!+BAZB4>WoC7AX>V>Wb!l@hV{dJ6Z*FC7baNnSZE$aLbRc13Z*_DmAZBu5ZDn6@a&Kd0b8~NUb1Wcca$#*{UvP47V`X!5Z*p^AZ*X*JZ*FreAZ2)EV|8?CZ*D9gWq4&{b#!TOZeMh0a%Ev;Ut@1|ZgealWq4&{b#!TOZeMYAWp!m=V{dhCbSxlkWo>VAc`P7wWo>X@W^!R|Wh@|Xb#!obbYE|9bZKvHb1WcZZ*6UFZeMS3bZKvHb1WcpZ*_8GWh@|cVRC0>bSxlrVRC0>bYE|9bZKvHb1Wclb#!obbSxlna%FaDWp^wfbaH8JUuJS)ZDlMVW?^GxUtw-xY<Y8Kax5TbVPj=qb7gF0V{~tFEFflKV`X1$VRLI`ataCxAY^4`AaHVJUt?%xV{0fWAT2&1VsCG3ItoBQAT2XFEH)r3GdV0cAV5G0APETx33q99Xdq{DVPt7<E<$W?V{3CLDLM)u2?+@a33Op{XJvFQa%FC0WpXGf3Lpsy2?=*;bZ8)Fa$#g?Z!SV?Z)0n7C@DG$D+vh+2?=yza%W|9UvF@9X>V?GE^=jVWMy(FDGDnI2?+^zX>@2HXL4a=X>Tq<Y;R+0b0{e~3Lpsy2?+^rb#!obbS`pbZe(S0C@Bgc2?+^zX>@2HXL4a=X>Tq=Z)|mKZYXnOVQgg}Js>kFItm~O2?+^zX>@2HXL4a=X>Tq<Y;R+0b0{e~3P3<0EjBkSHXtiDIV?9IKtKv032$|DaCLNFZ*X*JZ*FrgY-w|JWo{@b3Lpt{Z*_8GWiD)Kb97~HC@Bgc33Op{XJvFQY-w|JWo{@b3M&b8VRC0>bYE|9bZKvHb1rOYb97~HC@Bgc32$|DaCLMpY-w|JWo{@b3Lpt^a%FaDWp^%YX>)XCZYU`VAPIDGX>DI-a$#*{E^KLYbY*TRDGEt$WMz0dAZB4>WoC7AX>V>Xb!l@iV{dJ6Z*FC7baO9sVRC0>bYE|9bZKvHb1ras3Q0soK_FpdWNCD1Z*F01AZc!9Z#oK7bz*aQb97~GIv`_jZ7ykUbY*O8X=*NSaAj^`aA_`NX=Y|FX>D+9E^uLVV`wfzXkl`5WpqVQ3Op-5Ra8bTI0`*IJv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jql!LW@aEQEoW(TAYm_NVPj=xb#rNNZZCCdb1!3WZE$aHWo~qHFLYsYXJvF>Z*X*JZ*FrgaCsnNFJ@t5WoC7AX>V>Xb!l@iV{dJ6Z*FC7baO9sVRC0>bYE|9bZKvHb1ras3T|b0AZBT7Wgu;DWMv>RFfcYWGzu*(Eg&ysWp*!ab!==2C}d%DWgsy(F*Y?bH8wajGBPkJ3M(rsAYw0OVPj=xb#rNNZZCCdb1!3WZE$aHWo~qHFLYsYXJvF>Z*X*JZ*FrgaCr$RWMOn=ATc*FHZ?OfHaIjgGB7C$KtLcZFf1@2D={oJH6TDh3M*-CaBp&SAa8RDD`{<TZ*p`Xb7*yRX>1BBW^!+BAar?fX>MmAX>D+Ca&#b1aCB*JZeeUJAXIg5Y-I{7X>D+Ca&#bPa$#g?Zwf1EZE$aLbRc<jUu0}>3M&dLW^!+BAZB4>WoC7AX>V>IX>D+Ca&#bfZ*pX5Zf6QBW^!+BAZB4>WoC7AX>V>Wb!l@hV{dY0AZcxIZ*p`XXJvF>b!lH?Z*6dIZe?zC3M*!EZ*3rEVPj=xb#rNNZZ2kNY-MwKb97~GAZcxIZ*p`XXJvF>bY*RDUu0==Wn*-2a(Q2HVRUFLAZc@7WNC6`V{~tFc`P7fa%Ew3WnXk<ZEy-J3M*7WQb$EpUsX~}UsOd{R6<W!AUYsVaCB*JZeeU&XL4a=X>Tr6Wq5RAZ+KlGJs?hRZe<E9L{C>vOiw{XUqV$>R8LMIIv`JQbZKvHVQgDxa$#g?Z!SW0baZcST_8OmPH%2y3M&dL3M*t~W*~B9Ze(S0C@CN<J|IqSZe=<OD+y<8Z(?C=AXGt8M@3X$RZ>h}R7F@+LQhx<D+y<8Z(?C=AVg1BPE1chL|;NxR8&t+3M&dL2~<H+M@3X$RZ>h}R7F@+LQhyAJs@XtVPt7<E>vZBbYgFKC<-eH32b3vWo#flAa`$aWNB_^E@x$QC?|Dkb1rmYa%W|9Uv+Y9Uvy=7bYgFKUu<DwWo#!YED9?L32k9`Uu<b^Wpf}sATbIn2`LII2}Dm<PE1chL|;NxR8&t+AUz;wa$#g?Z!SW0baZcSC<-eH33g#@b!8wuAa`$aWNB_^E@x$QC?|Dkb1r0WcW!KNVPs!ob#!!ZZeMI+Vr6V6DJ%*r2?=v)dSxIzASZKeCkiVGDGDnJD+()QWo963X>)XCZYU`rEj}PlZ*FBe3M&b8VRC0>bYEs^Y-J!lAZKNCUv+6;V{dJ6Z*FC7bSNiuVRC0>bYEs^Y-J}Y3M&b4a%FaDWp`g@a$#*{Uvq3}WMy(7Js@XgbYFF8Ut@1=aBps9ZgeOoaB^jKX=Qg`W^!R|WnXh_X=G(`Cn*Xm329~^bYXI5WprO=X>4U6VQyp~aB^jKX=Qg`W^!R|WnXh_X=G(`ItnWZ2}Dm<PE1chL|;NxR8&t+E@NzIV{0g6Z+C8NZ((FCAZc!Jb#!weJs?y;Qb$EpUsX~}UsOd{R6<W!EFf=nbZ~Wab09q+TOf2{a%W|9UuJ1+Wh@|Ya%FaDWp`g@a$#*{Uvq3}WMy(7T`3AH3M&dLWMyU`WN&wFY;R#?D0E?RXJvF>b#iPVIv{g&aw#A!J|I+eaBO8;XL4a=X>Tq@X>4UIAZK!6WNB|MQ*3EuWpZ6Q3M&b8Wo>X@WNC6`V{~tFd0%j0bZ8(wAZKNCUvy<{a9?C;a%E$5Z*qBGaA9<4C?|Aba%W|9Uu180ZftL1WG-!RG$$zvD+zREZE#;^X>4U*aA9<4AUz;&b1raUbZ9PWZ)t8QbY*RDUu0==Wn*-2a(Q2HVRUFLASZNTa%W|9Uu180ZftL1WG-!RG$$zvD+y_4AZc@7WNC6`V{~tFc_?&cZE#;?X>w&_bZ>HbUvOb`Xel}hD+vj6XmxaHY%X$bbaG{7D0F3Qa9?C;a%E$5Z*qBGaA9<4DGDnIV{&C-bY)+3Wo>XMCv;(QXJvF>WN&wFY;R#?E^Tl$Cn*Xm3M&bDZ*_EaVr5@sZ+C8NZ((F#Z*X*JZ*FrSJzNSa3401F2?-}}b#!!XaBL?!AarGIa9?I=Y-L|?VRUFL3M&Z-CuVPQZDDjLIv^))a5N_hD+zrHD+y_4Aar4JXJvF>b#iPv3M&Z-baHt*3M&Z-33q99XdroXUu0}>E?IANbai57L`*1oZ*_EaVr5@sZ+C8NZ((F#Z*X*JZ*FrbAYpSLd2e-ebz)^-WN&wFY;R#?ItnWZ2?+^#Z*_EaVr5@sZ+C8NZ((FEWN&wFY;R#?D0E?RXJvF>b#iPe3M&Z-336q0b#iVXXL4a=X>Tq@X>4UEc42IFWgtBubY*RDUuJ1+WnXY%bZ99oAZK!6WNB|MQ*3EuWpXHXVQh6}AUz;3DGDnI31xU=WpH#Ld30Z7Y;Z1hbZKmJE<|s4ZftL1WJPjvZ*n>cD+vh+aA9+E3M&b6Wps6NZXjoJVPt7<E=Fl=Whi!GY;|QIJs?hRZe=MfAZK!6WNB|MQ*3EuWpXHXVQh6}AUz;3DGEt$WMz0dAaZ4Kb!l>CZDnqBb1rmvbP7pCML{58WMpY{X>V>}Y#?cFW^XzQQ*~l<d2@7SZ8{)hZ*4AVZggdAY-wsPZ*XO9VQ^_KWNBt*E@^FWY%XwNbYo~PLug@gb7gczPzpRNK2=mkEjS82Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv}`=Jv|C!X=Y|1EiGqhbRc0ba%FLKX>w(4Wo~qHE_8TwAYw0aWpQ<Ba%F90Zgg`lba-?MEiEk|VJ~uJadl~OWo>0{baO6rcytLUa%FaDb7^mGAZ9i=VlXmfGh#6`Gh||8GG#C`H#syjWo2SwGdMG2Wil~lFk@zAV<`$ND=Q#kFLGsZb!l>CZDnqBb1rmvbO|VAVRU66F*h+bH8V9fI5aXcG${%|Kp-tQEHfZ0H!L(DKtKv0aC3EZX>2_`H7+?WI0_(iab#^hJv1&hHZC*@Aai4BaCtpFF)lGPE-(r!d30Z7Y;Zk2GB7eTE-^4JHwp'


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
