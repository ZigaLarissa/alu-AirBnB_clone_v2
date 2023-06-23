#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers"""
from invoke import run
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    run("mkdir -p versions")
    run("tar -czvf {} web_static".format(archive_path))

    return archive_path
