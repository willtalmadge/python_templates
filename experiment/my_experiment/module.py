import subprocess
import os
import logging

def get_svn_revision(file):
    lines = subprocess.check_output(['svn', 'status', file])
    filename = os.path.split(file)[1]
    for line in lines.splitlines():
        if b'is not a working copy' in line:
            return None
        if filename in line:
            raise RuntimeError('The svn revision of ({0}) cannot be determined since it is not committed.')

    version = subprocess.check_output(['svnversion', file])
    if b'Unversioned' in version:
        return None
    else:
        return int(version)


svn = get_svn_revision(__file__)
logger = logging.getLogger(__name__ + '@' + str(svn))
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s ~ %(name)s ~ %(levelname)s ~ %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info('yo')