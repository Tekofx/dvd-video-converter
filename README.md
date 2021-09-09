<h1 align="center">dvd-video-converter</h1>

Python script that converts .VOB files to mp4

Requirements:
- HandBrakeCLI

This program is suitable for DVD's with the following folder structure:

    Folder
       |--DVD_folder_1
       |    |--DCIM/
       |    |--VIDEO_TS/
       |          |--VTS_01_1.VOB
       |          |--VTS_01_2.VOB
       |          |--....
       |
       |--DVD_folder_2
       |     |--DCIM/
       |     |--VIDEO_TS/
       |         |--VTS_01_1.VOB
       |         |--VTS_01_2.VOB
       |         |--....
        ....

The converted files will be placed inside each DVD_folder_n with the name DVD_folder_n #, being # a number.