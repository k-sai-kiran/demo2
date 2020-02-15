import sounddevice


class audiorec:
    fs = 44100
    second = 10
    def recordaudio(self):
        print("recording.....")
        record_voice = sounddevice.rec(int(self.second * self.fs),samplerate = self.fs, channels = 1)
        sounddevice.wait()
        return record_voice