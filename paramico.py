from typing import Union, Any, List

from paramiko import SFTPClient, SSHClient, AutoAddPolicy
from pathlib import Path
from operator import attrgetter

hostname = 'yourhostname'
username = 'yourusername'
password = 'yourpassword'

class Client(SFTPClient):

    def put(self, localpath: Union[str, Path], remotepath: Union[str, Path], callback=None,
            confirm=True) -> str:
        return super().put(str(localpath), str(remotepath), callback, confirm)

    def get(self, remotepath: Union[str, Path], localpath: Union[str, Path], callback=None,
            prefetch=True) -> str:
        return super().get(str(remotepath), str(localpath), callback, prefetch)

    def _adjust_cwd(self, path: Union[str, Path]) -> str:
        return super()._adjust_cwd(str(path))

    def get_last_filename(self, path: Union[str, Path]) -> str:
        return self.listdir(path, True)[0]

    def listdir(self, path: Union[str, Path], sort: bool = False) -> List[Any]:
        return [f.filename for f in self.listdir_attr(path, sort)]

    def listdir_attr(self, path: Union[str, Path], sort: bool = False) -> List[Any]:
        filelist = super(Client, self).listdir_attr(path)
        if sort:
            filelist = sorted(filelist, key=attrgetter('st_mtime'))
            return filelist[::-1]
        else:
            return filelist


if __name__ == '__main__':
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password, look_for_keys=False,
                allow_agent=False)
    ftp = SFTPClient.from_transport(ssh.get_transport())
    direct = Client.from_transport(ssh.get_transport())
    path = Path('/home/ulyana/Загрузки/')
    print(direct.listdir(path, True))
    print(direct.listdir_attr(path))
    print(direct.get_last_filename(path))
