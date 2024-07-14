#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os
""" Fabric script that generates a .tgz archive from web_static."""


def do_pack():
    """Generates a .tgz archive from webstatic folder."""

    if not os.path.exists("versions"):
        os.makedirs("versions")
    now = datetime.now()
    archive_name = now.strftime("web_static_%Y%m%d%H%M%S. tgz")
    archive_path = os.path.join("versions", archive_name)
    result = local(f"tar -cvzf {archive_path} web_static")
    if result.succeeded:
        return archive_path
    else:
        return None
