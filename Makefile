#Makefile for pythonforyouandme

XML_LANG	= en-US
DOCNAME		= pythonforyouandme
PRODUCT	= Documentation
#BRAND		= FIX_ME!

#OTHER_LANGS	= as-IN bn-IN de-DE es-ES fr-FR gu-IN hi-IN it-IT ja-JP kn-IN ko-KR ml-IN mr-IN or-IN pa-IN pt-BR ru-RU si-LK ta-IN te-IN zh-CN zh-TW
OTHER_LANGS	= ml-IN 
TRANSLATIONS	= $(XML_LANG) $(OTHER_LANGS)

COMMON_CONFIG  = /usr/share/publican
include $(COMMON_CONFIG)/make/Makefile.common

