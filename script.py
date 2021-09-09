import os
import playsound

""" Important

    Requirements:
        - HandBrakeCLI

    This program is suitable for DVD's with the following folder structure

    DVD
     |-----DCIM/
     |-----VIDEO_TS/
               |-----VTS_01_1.VOB
               |-----VTS_01_2.VOB
               |-----....
"""


# Location of the folders of each CD
video_camera_path = "/mnt/2C0A95780A953FAE/prueba_script/"

# Each x is the folder of a CD
for x in os.listdir(video_camera_path):
    input_path = video_camera_path + x + "/" + "VIDEO_TS/"
    output_path = video_camera_path + x + "/" + x

    count = 1
    # Each and is a video file from a CD.
    for y in os.listdir(input_path):
        if "VTS" in y and "VOB" in y:  # Check if it is a video file
            command = 'HandBrakeCLI -i {input} -o {output} --preset="Fast 576p25"'
            command = command.format(
                input='"' + input_path + y + '"',
                output='"' + output_path + " " + str(count) + ".mp4" + '"',
            )
            os.system(command)
            count += 1

    count = 1


# Conversion completed
playsound.playsound("text.mp3")
