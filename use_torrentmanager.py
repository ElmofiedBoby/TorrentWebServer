from dotenv import dotenv_values
import os

from TorrentManager import TorrentManager

magnet_link = 'magnet:?xt=urn:btih:0E73E3DEB7C248A77C28AB6F6187DD5B488D8D7C&dn=Jujutsu+Kaisen+0+The+Movie+-+Gekijouban+Jujutsu+Kaisen+Zero+%282021%29+%5BBD%5D%5B1080p%5D%5BHEVC+10bit+x265%5D%5BMulti+Sub%5D+-+AnimeTime&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=http%3A%2F%2Fanidex.moe%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce'
download_path = os.path.join(os.getcwd(), 'download')

tm = TorrentManager(download_path, dotenv_values(".env"))

#tm.add_torrent(magnet_link)
#tm.show_torrents()
#tm.delete_all_torrents()
