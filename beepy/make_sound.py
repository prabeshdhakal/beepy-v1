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
    sound_names = [
                   "coin",
                   'robot_error',
                   'error',
                   'ping',
                   'ready',
                   'success',
                   'wilhelm'
    ]
    if isinstance(sound, int):
        if sound not in range(1, 8):
            sound = 4
    elif isinstance(sound, str):
        assert sound in sound_names, f'Name "{sound}" does not exists'
        sound = sound_names.index(sound) + 1

    wave_obj_file = wave_dict.get(sound, 'ping.wav')
    WAVE_PATH = os.path.join(AUDIO_DIR, wave_obj_file)

    wave_obj = sa.WaveObject.from_wave_file(WAVE_PATH)
    play_obj = wave_obj.play()
    play_obj.wait_done()
