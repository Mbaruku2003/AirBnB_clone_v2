#!/usr/bin/python3
"""distributes an archive to your web servers."""
from fabric.api import env, put, run
import os
env.hosts = ['54.175.146.193', '54.237.41.19']
env.key_filename = "../.ssh/schhool.pub"


def do_deploy(archive_path):
    """Distributes an archive to web servers."""

    if not os.path.exists(archive_path):
        return False
    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = archive_filename.split(".")[0]
        remote_path = f"/tmp/ {archive_filename}"
        put(archive_path, remote_path)
        release_path = f"/data/web_static/releases/{archive_no_ext}/"
        run(f"mkdir -p {release_path}")
        run(f"tar -xzf {remote_path} -C {release_path}")
        run(f"mv {release_path}web_static/* {release_path}")
        run(f"rm -rf {release_path}web_static")
        run(f"rm {remote_path}")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {release_path} /data/web_static/current")
        return True
    except:
        return False
