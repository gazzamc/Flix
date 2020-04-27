"""
    video.py
    contains function that grabs youtube urls
"""

import youtube_dl


def get_video_url(yt_link):
    """ Returns raw video url of youtube video """
    ydl_opts = {
        'quiet': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        try:
            video = ydl.extract_info(yt_link, download=False)
            formats = video.get('formats', [video])

        except youtube_dl.DownloadError:
            return None

    for f in formats:
        """ Get video url """
        if f['ext'] == 'mp4' and f['acodec'] is not None:
            vid_url = f['url']

    return vid_url
