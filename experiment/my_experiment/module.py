import subprocess
import os
import logging
import warnings


def guard_svn_id(file, stop_if_not_versioned=False):
    """
    This is a help function that protects against accidentally running experiments with source code that isn't
    checked into source control. This is a problem because it's not reproducible. This function will stop
    the program if the file that calls this is not under version control at all. It will optionally stop the
    program if the file has been modified. It's recommended to set stop_if_not_version based on an environment
    variable. (1 for true, 0 for false).

    The return value of this function is intended to be used as a log name.

    :param file:
    :param stop_if_not_versioned:
    :return:
    """
    if isinstance(stop_if_not_versioned, str):
        if stop_if_not_versioned == '1':
            stop = True
        else:
            stop = False
    else:
        stop = stop_if_not_versioned

    version = subprocess.check_output(['svnversion', file])
    if b'Unversioned' in version:
        raise RuntimeError('The file {0} is unversioned, check it into version control before running'.format(file))
    if b'M' in version:
        msg = 'The file {0} has been modified, but not checked in, check it in before running'.format(file)
        if stop:
            raise RuntimeError(msg)
        else:
            warnings.warn(msg)

    id = file
    lines = subprocess.check_output(['svn', 'status', file])
    for line in lines.splitlines():
        if b'URL:' in line:
            id = line.replace(b'URL: ', b'').strip()

    return '{0}@{1}'.format(id.decode(), version.decode())


logger = logging.getLogger(guard_svn_id(__file__, stop_if_not_versioned=not int(os.environ['DEBUG'])))
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s ~ %(name)s ~ %(levelname)s ~ %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info('yo')
