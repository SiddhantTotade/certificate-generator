from zdrive import Downloader

output_dir = "drive-files/"

d = Downloader()

folder_id = '1kj4rSLzqMAYScAQgiIg0g_wqtlkIFyNA'

d.downloadFolder(folder_id, destinationFolder=output_dir)
