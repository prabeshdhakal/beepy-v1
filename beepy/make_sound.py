import simpleaudio as sa

import os

MODULE_PATH = os.path.dirname(__file__)
AUDIO_DIR = os.path.join(MODULE_PATH, "audio_data")

wave_dict = {
            1:'coin.wav',
            2:'does-not-compute.wav',
            3:'error.wav',
            4:'ping.wav',
            5:'ready.wav',
            6:'success.wav',
            7:'wilhelm.wav'
            }

def beep(sound=1):
    if sound==1 or sound=='coin':
        sound = 1
    elif sound==2 or sound=='robot_error':
        sound = 2
    elif sound==3 or sound=='error':
        sound = 3
    elif sound==4 or sound=='ping':
        sound = 4
    elif sound==5 or sound=='ready':
        sound = 5
    elif sound==6 or sound=='success':
        sound = 6
    elif sound==7 or sound=='wilhelm':
        sound = 7
    else:
        sound = 4

    wave_obj_file = wave_dict[sound]
    WAVE_PATH = os.path.join(AUDIO_DIR, wave_obj_file)

    wave_obj = sa.WaveObject.from_wave_file(WAVE_PATH)
    play_obj = wave_obj.play()
    play_obj.wait_done()
