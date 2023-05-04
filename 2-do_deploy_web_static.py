#!/usr/bin/env python3
"""
compress web static package
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['100.25.19.204', '54.157.159.85']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploy web files to server
    """
    try:
        if not path.exists(archive_path):
            return False

        # upload archive
        put(archive_path, '/tmp/')

        # create target dir
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'
            .format(timestamp))

        # uncompress archive and delete .tgz
        run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/web_static_{}/'
            .format(path.basename(archive_path), timestamp))

        # remove archive
        run('sudo rm /tmp/{}'.format(path.basename(archive_path)))

        # move contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'
            .format(timestamp))

        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        run('sudo ln -s /data/web_static/releases/web_static_{}/ \
/data/web_static/current'.format(timestamp))

        return True

    except (FabricException, SystemExit) as e:
        print("Exception occurred: {}".format(e))
        return False

