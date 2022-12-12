from qbittorrentapi import Client
from qbittorrentapi import LoginFailed

class TorrentManager:
    def __init__(self, download_path, config):
        self.download_path = download_path
        self.config = config
        self.client = qbt_client = Client(
            host=config['QBIT_IP'],
            port=config['QBIT_PORT'],
            username=config['QBIT_USER'],
            password=config['QBIT_PASS'],
        )
        try:
            qbt_client.auth_log_in()
        except LoginFailed as e:
            print(e)

    def show_torrents(self):
        for torrent in self.client.torrents_info():
            print(f'{torrent.hash[-6:]}: {torrent.name} ({torrent.state})')
    
    def add_torrent(self, magnet):
        self.client.torrents_add(urls=magnet, save_path=self.download_path)

    def delete_all_torrents(self):
        self.client.torrents.delete.all()
    