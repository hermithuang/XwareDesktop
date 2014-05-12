# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), "../"))
# BASE_DIR = "/opt/xware_desktop"
TMP_DIR = "/tmp"


XWARED_LOCK = os.path.join(TMP_DIR, "xware_xwared.lock")
XWARED_SOCKET = (os.path.join(TMP_DIR, "xware_xwared.socket"), "AF_UNIX")
XWARED_CONFIG_FILE = os.path.join(BASE_DIR, "xwared.ini")

ETM_CFG_DIR = os.path.join(BASE_DIR, "xware/cfg")
ETM_CFG_FILE = os.path.join(ETM_CFG_DIR, "etm.cfg")
ETM_PATCH_FILE = os.path.join(BASE_DIR, "etmpatch.so")
ETM_COMMANDLINE = (os.path.join(BASE_DIR, "xware/lib/EmbedThunderManager"), "--verbose")

FRONTEND_LOCK = os.path.join(TMP_DIR, "xware_frontend.lock")
FRONTEND_SOCKET = (os.path.join(TMP_DIR, "xware_frontend.socket"), "AF_UNIX")

CONFIG_FILE = os.path.join(BASE_DIR, "settings.ini")
FRONTEND_AUTOSTART_FILE = os.path.expanduser("~/.config/autostart/xware-desktop.desktop")

MOUNTS_FILE = os.path.join(BASE_DIR, "mounts")
MOUNTS_FILE_HEADER = \
    "# This file is automatically generated by Xware Desktop. " \
    "Manually modifying this file via a text editor is not advised.\n"

ETM_MOUNTS_DIR = "/tmp/thunder/volumes/"  # the last slash is needed

PERMISSIONCHECK = os.path.join(BASE_DIR, "permissioncheck")

DESKTOP_FILE_LOCATION = "/usr/share/applications/xware-desktop.desktop"


