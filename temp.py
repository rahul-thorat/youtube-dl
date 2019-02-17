import youtube_dl

url=input('ENTER URL:')

#takes url as input

ydl_opts = {
    'format': 'bestaudio/best',       
    'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',        
    'noplaylist' : False,        
    'listformats': True 
}

#listformats only lists the available formats of the video ,doesn't download video

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

#listformats only lists the available formats of the video ,doesn't download video
    
frmt=input("ENTER common format code from given lists : " )

#takes format code as input

ydl_optss = {
    'format': frmt,       
    'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',        
    'noplaylist' : False,  
    
}
 
#takes input format,outtmpl is the destination of video
#noplaylist' : False ensurrres if url is playlist entire playlist is downloaded

with youtube_dl.YoutubeDL(ydl_optss) as ydl:
    ydl.download([url]) 
    
#downloads video using url    