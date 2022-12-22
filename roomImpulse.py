# convolution_reverb('sounds\snare.wav', 'sounds\s1r2.wav', 'sounds\snare_IR.wav')

import numpy as np
from wave import open
import soundfile
import os

class Wave:
    def __init__(self, data, frame_rate):
        self.data = normalize(data)
        self.frame_rate = frame_rate

    def make_spectrum(self):
        amplitudes = np.fft.rfft(self.data)
        frequencies = np.fft.rfftfreq(len(self.data), 1 / self.frame_rate)

        return Spectrum(amplitudes, frequencies, self.frame_rate)

    def zero_padding(self, n):
        zeros = np.zeros(n)
        zeros[:len(self.data)] = self.data

        self.data = zeros

    def write(self, file):
        reader = open(file, 'w')

        reader.setnchannels(1)
        reader.setsampwidth(2)
        reader.setframerate(self.frame_rate)

        frames = self.quantize().tobytes()
        reader.writeframes(frames)

        reader.close()

    def quantize(self):
        if max(self.data) > 1 or min(self.data) < -1:
            self.data = normalize(self.data)

        return (self.data * 32767).astype(np.int16)


class Spectrum:
    def __init__(self, amplitudes, frequencies, frame_rate):
        self.amplitudes = np.asanyarray(amplitudes)
        self.frequencies = np.asanyarray(frequencies)
        self.frame_rate = frame_rate

    def __mul__(self, other):
        return Spectrum(self.amplitudes * other.amplitudes, self.frequencies, self.frame_rate)

    def make_wave(self):
        return Wave(np.fft.irfft(self.amplitudes), self.frame_rate)


def convert_wav(file):
    data, samprate = soundfile.read(file)
    soundfile.write(file, data, samprate, subtype='PCM_16')


def read_wave(file):
    reader = open(file)

    _, sampwidth, framerate, nframes, _, _ = reader.getparams()
    frames = reader.readframes(nframes)

    reader.close()

    dtypes = {1: np.int8, 2: np.int16, 4: np.int32}

    if sampwidth not in dtypes:
        raise ValueError('unsupported sample width')

    data = np.frombuffer(frames, dtype=dtypes[sampwidth])

    num_channels = reader.getnchannels()
    if num_channels == 2:
        data = data[::2]

    return Wave(data, framerate)


def normalize(data):
    high, low = abs(max(data)), abs(min(data))
    return data / max(high, low)


def convolution_reverb(audio_file, ir_file, output_file):
    convert_wav(audio_file)
    convert_wav(ir_file)

    audio = read_wave(audio_file)
    ir = read_wave(ir_file)

    if len(audio.data) > len(ir.data):
        ir.zero_padding(len(audio.data))

    else:
        audio.zero_padding(len(ir.data))

    ir_spectrum = ir.make_spectrum()
    audio_spectrum = audio.make_spectrum()

    convolution = audio_spectrum * ir_spectrum
    wave = convolution.make_wave()
    wave.write(output_file)


room_impulse_list = ['auditorium', 'hall', 'church', 'summer_park', 'stairway', 'factory',
                     'dungeon', 'kiln', 'tunnel', 'winter_park', 'studio', 'chamber']

sounds_list       = ['hi hat', 'snare', 'kick', 'crash', 'clap', 'tom']

def convolve():
    for sound in sounds_list:
        sound_path = 'sounds/'+sound+'.wav'
        for room in room_impulse_list:
            room_path = 'IR/'+room+'.wav'
            resultant_path = os.getcwd()+ '\\IR\\convolved\\' + sound
            if(not os.path.isfile(os.path.join(resultant_path , sound + '_' + room + '.wav'))):
                if(not os.path.isdir(resultant_path)):
                    os.mkdir(resultant_path)
                convolution_reverb(sound_path, room_path, os.path.join(resultant_path , sound + '_' + room + '.wav'))

convolve()