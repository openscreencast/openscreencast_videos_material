#!/usr/bin/env python

############################# Info-Video ueber Etcher (etcher.io) erzeugen

# Modul moviepy importieren
from moviepy.editor import *

# Modul gizeh und random importieren
import gizeh
import random


############################# Einstellungen

videodatei = 'etcher.ogv'   # Videodatei
frames = 25                 # Frames pro Sekunde
videobreite = 1280          # in Pixel
videohoehe = 720            # in Pixel
a_bitrate = '192k'          # Audio-Bitrate
v_bitrate = '6000k'         # Video-Bitrate

############################# Funktionen 

# Funktion fuer den Intro-Text in der Mitte
def create_frame_for_intro(t):
    img = gizeh.Surface(videobreite,videohoehe,bg_color=(hgfarbe_r,hgfarbe_g,hgfarbe_b))
    text_img = gizeh.text(text, fontfamily=schrift, fontsize=textgroesse,
               fill=(textfarbe_r,textfarbe_g,textfarbe_b),
               xy=(videobreite/2,videohoehe/2), angle=winkel)
    text_img.draw(img)
    return img.get_npimage()

# Funktion um die Ueberschrift Linux - dd zu erzeugen 
def create_frame_for_maintext_linux(t):
    img = gizeh.Surface(videobreite,videohoehe,bg_color=(hgfarbe_r,hgfarbe_g,hgfarbe_b))
    text_img = gizeh.text('Linux - dd', fontfamily=schrift, fontsize=textgroesse,
               fill=(textfarbe_r,textfarbe_g,textfarbe_b),
               xy=(videobreite/2,videohoehe/2-300), angle=winkel)
    text_img.draw(img)
    return img.get_npimage()

# Funktion um die Ueberschrift Windows - Win32Diskmanager zu erzeugen
def create_frame_for_maintext_win(t):
    img = gizeh.Surface(videobreite,videohoehe,bg_color=(hgfarbe_r,hgfarbe_g,hgfarbe_b))
    text_img = gizeh.text('Windows - Win32Diskmanager', fontfamily=schrift, fontsize=textgroesse,
               fill=(textfarbe_r,textfarbe_g,textfarbe_b),
               xy=(videobreite/2,videohoehe/2-300), angle=winkel)
    text_img.draw(img)
    return img.get_npimage()

# Funktion um die Ueberschrift Etcher (etcher.io) zu erzeugen
def create_frame_for_maintext_etcher(t):
    img = gizeh.Surface(videobreite,videohoehe,bg_color=(hgfarbe_r,hgfarbe_g,hgfarbe_b))
    text_img = gizeh.text('Etcher (etcher.io)', fontfamily=schrift, fontsize=textgroesse,
               fill=(textfarbe_r,textfarbe_g,textfarbe_b),
               xy=(videobreite/2,videohoehe/2-300), angle=winkel)
    text_img.draw(img)
    return img.get_npimage()


# Funktion fuer Image-File und SD-Karte
def create_frame_image_sdkarte(t):
    img = gizeh.Surface(1000,500,bg_color=(1,1,1))
    image_rect = gizeh.rectangle(lx=200, ly=300, xy=(200/2+10,300/2+100), fill=(1,1,1), angle=0, stroke=(0,0,0), stroke_width=1)
    image_text_image = gizeh.text("Image", fontfamily=schrift, fontsize=50,
               fill=(textfarbe_r,textfarbe_g,textfarbe_b),
               xy=(200/2+10,300/2+50), angle=winkel)
    image_text_img = gizeh.text('.img', fontfamily=schrift, fontsize=50,
               fill=(textfarbe_r,textfarbe_g,textfarbe_b),
               xy=(200/2+10,300/2+100), angle=winkel)
    image_text_iso = gizeh.text('.iso', fontfamily=schrift, fontsize=50,
               fill=(textfarbe_r,textfarbe_g,textfarbe_b),
               xy=(200/2+10,300/2+150), angle=winkel)
    sdkarte_rect_aussen = gizeh.rectangle(lx=350, ly=450, xy=(200/2+700,300/2+80), fill=(0.2,0.2,0.2), angle=0)
    sdkarte_rect_innen = gizeh.rectangle(lx=250, ly=320, xy=(200/2+700,300/2+100), fill=(1,1,1), angle=0, stroke=(0,0,0), stroke_width=1)
    sdkarte_rect_rechts = gizeh.rectangle(lx=8, ly=15, xy=(8/2+968,15/2+130), fill=(1,1,1), angle=0)
    sdkarte_rect_links = gizeh.rectangle(lx=8, ly=70, xy=(8/2+625,70/2+120), fill=(1,1,1), angle=0)
    sdkarte_rect_links_lock = gizeh.rectangle(lx=7, ly=35, xy=(7/2+626,35/2+122), fill=(0.5,0.5,0.5), angle=0)
    sdkarte_rect_unten = gizeh.rectangle(lx=200, ly=10, xy=(200/2+700,10/2+430), fill=(0.15,0.15,0.15), angle=0)
    sdkarte_triangle_oben = gizeh.polyline(points=[(920,3), (920+60,3), (920+60,3+60), (920,3)], fill=(1,1,1))

    image = gizeh.Group([image_rect, image_text_image, image_text_img, image_text_iso])
    sdkarte = gizeh.Group([sdkarte_rect_aussen, sdkarte_rect_innen, sdkarte_triangle_oben, sdkarte_rect_rechts, sdkarte_rect_links, sdkarte_rect_links_lock, sdkarte_rect_unten])
    image.draw(img)
    sdkarte.draw(img)
    return img.get_npimage()


# Funktion fuer Image in der SD-Karte
def create_frame_image_in_sdkarte(t):
    img = gizeh.Surface(205,305,bg_color=(1,1,1))
    image_rect = gizeh.rectangle(lx=200, ly=300, xy=(200/2,300/2), fill=(1,1,1), angle=0, stroke=(1-t*1/9,1-t*1/9,1-t*1/9), stroke_width=1)
    image_text_image = gizeh.text("Image", fontfamily=schrift, fontsize=50,
               fill=(1-t*1/18,1-t*1/18,1-t*1/18),
               xy=(200/2,300/2-50), angle=winkel)
    image_text_img = gizeh.text('.img', fontfamily=schrift, fontsize=50,
               fill=(1-t*1/18,1-t*1/18,1-t*1/18),
               xy=(200/2,300/2+0), angle=winkel)
    image_text_iso = gizeh.text('.iso', fontfamily=schrift, fontsize=50,
               fill=(1-t*1/18,1-t*1/18,1-t*1/18),
               xy=(200/2,300/2+50), angle=winkel)
    image = gizeh.Group([image_rect, image_text_image, image_text_img, image_text_iso])
    image.draw(img)
    return img.get_npimage()


# Funktionen fuer Animation - 1 und 0 bewegen sich von der Image-Datei zur SD-Karte
v, s, pos = [], [], []

for i in list(range(0,20)):
    v.append(random.randint(1,10))
    s.append(random.choice(['1','0']))
    pos.append(1)

def bew():
    for i in list(range(0,20)):
        if pos[i]*v[i] >= 380:
            pos[i] = 1;
            v[i] = random.randint(1,10)
            s[i] = random.choice(['1','0'])
        pos[i] = pos[i]+2

def create_frame_send_bit(t):
    img = gizeh.Surface(380,300,bg_color=(1,1,1))
    bew()
    for i in list(range(0,20)):
         x = gizeh.text(s[i], fontfamily=schrift, fontsize=20,
               fill=(0.1,0.1,0.1),
               xy=(pos[i]*v[i],i*10+50), angle=winkel)
         x.draw(img)
    return img.get_npimage()


############ Intro - Text "Etcher (etcher.io)" in der Mitte

# Einstellungen
text = 'Etcher (etcher.io)'               # Text
textgroesse = 100           # Textgroesse in Pixel
textfarbe_r = 0             # Textfarbe R
textfarbe_g = 0             # Textfarbe G
textfarbe_b = 0             # Textfarbe B
schrift = 'FreeSans'        # Schriftart
winkel = 0                  # Winkel
hgfarbe_r = 1               # Hintergrundfarbe R
hgfarbe_g = 1               # Hintergrundfarbe G
hgfarbe_b = 1               # Hintergrundfarbe B
videolaenge = 10             # in Sekunden   

# Video erzeugen
video_intro = VideoClip(create_frame_for_intro, duration=videolaenge) 

############## Text Linux - dd

# Einstellungen
textgroesse = 80           # Textgroesse in Pixel
textfarbe_r = 0.4             # Textfarbe R
textfarbe_g = 0.4             # Textfarbe G
textfarbe_b = 0.4             # Textfarbe B
videolaenge = 9             # in Sekunden   

# Video erzeugen
video_linux_maintext = VideoClip(create_frame_for_maintext_linux, duration=videolaenge) 

video_linux_image_sdkarte = VideoClip(create_frame_image_sdkarte, duration=videolaenge)
video_linux_image_sdkarte = video_linux_image_sdkarte.set_pos((200,200))

video_linux_image_in_sdkarte = VideoClip(create_frame_image_in_sdkarte, duration=videolaenge)
video_linux_image_in_sdkarte = video_linux_image_in_sdkarte.set_pos((900,300))

video_linux_send_bit = VideoClip(create_frame_send_bit, duration=videolaenge)
video_linux_send_bit = video_linux_send_bit.set_pos((420,300))

video_linux = CompositeVideoClip([video_linux_maintext,video_linux_image_sdkarte,video_linux_image_in_sdkarte,video_linux_send_bit])


############## Text Windows - Win32Diskmanager

# Einstellungen
videolaenge = 10             # in Sekunden   

# Video erzeugen
video_win_maintext = VideoClip(create_frame_for_maintext_win, duration=videolaenge) 

video_win_image_sdkarte = VideoClip(create_frame_image_sdkarte, duration=videolaenge)
video_win_image_sdkarte = video_win_image_sdkarte.set_pos((200,200))

video_win_image_in_sdkarte = VideoClip(create_frame_image_in_sdkarte, duration=videolaenge)
video_win_image_in_sdkarte = video_win_image_in_sdkarte.set_pos((900,300))

video_win_send_bit = VideoClip(create_frame_send_bit, duration=videolaenge)
video_win_send_bit = video_win_send_bit.set_pos((420,300))

video_win = CompositeVideoClip([video_win_maintext,video_win_image_sdkarte,video_win_image_in_sdkarte,video_win_send_bit])


############## Text Etcher (etcher.io)

# Einstellungen
videolaenge = 54             # in Sekunden   

# Video erzeugen
video_etcher_maintext = VideoClip(create_frame_for_maintext_etcher, duration=videolaenge) 

video_etcher_image_sdkarte = VideoClip(create_frame_image_sdkarte, duration=videolaenge)
video_etcher_image_sdkarte = video_etcher_image_sdkarte.set_pos((200,200))

video_etcher_image_sdkarte_part = VideoClip(create_frame_image_in_sdkarte, duration=9)
video_etcher_image_in_sdkarte = concatenate_videoclips([video_etcher_image_sdkarte_part,video_etcher_image_sdkarte_part,video_etcher_image_sdkarte_part,video_etcher_image_sdkarte_part,video_etcher_image_sdkarte_part,video_etcher_image_sdkarte_part])
video_etcher_image_in_sdkarte = video_etcher_image_in_sdkarte.set_pos((900,300))

video_etcher_send_bit = VideoClip(create_frame_send_bit, duration=videolaenge)
video_etcher_send_bit = video_etcher_send_bit.set_pos((420,300))

video_etcher = CompositeVideoClip([video_etcher_maintext,video_etcher_image_sdkarte,video_etcher_image_in_sdkarte,video_etcher_send_bit])


################# etcher_.ogg und Video zusammenfuehren

create_video = concatenate_videoclips([video_intro,video_linux,video_win,video_etcher])

etcher_raw = VideoFileClip("etcher_.ogg")
etcher_outro = ImageClip("etcher.png")
etcher_outro = etcher_outro.set_duration(8)

etcher_raw_outro = concatenate_videoclips([etcher_raw,etcher_outro])

video = CompositeVideoClip([etcher_raw_outro,create_video])

################ Video schreiben

video.write_videofile(videodatei, fps=frames, audio_bitrate=a_bitrate, bitrate=v_bitrate)


################## Ende

# Hilfe fuer moviepy: https://zulko.github.io/moviepy/index.html
# Hilfe fuer gizeh: https://github.com/Zulko/gizeh

# create_video_etcher.py
# Lizenz: http://creativecommons.org/publicdomain/zero/1.0/
# Author: openscreencast.de


