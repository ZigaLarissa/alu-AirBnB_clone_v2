#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers"""

from fabric import Connection
from datetime import datetime
import os


def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    try:
        # Create the .tgz archive
        with Connection('localhost') as conn:
            conn.local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        print("Error: {}".format(e))
        return None
