import pyaudio
import wave
import numpy as np


CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 192000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "data/tmp.wav"


p = pyaudio.PyAudio()


for i in range(0, p.get_device_count()):
    print(i, p.get_device_info_by_index(i)[
          'name'], p.get_device_info_by_index(i))


# stream usando o as_loopback para pegar som do SO
stream = p.open(
    format=FORMAT,
    channels=2,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
    input_device_index=1, as_loopback=True)

# stream usando o iput device do meu Microphone
# stream2 = p.open(
#     format=FORMAT,
#     channels=1,
#     rate=RATE,
#     input=True,
#     frames_per_buffer=CHUNK,
#     input_device_index=1)
# as_loopback=False)


frames = []
# frames2 = []


for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    # data2 = stream2.read(CHUNK)
    frames.append(data)
    # frames2.append(data2)


# frames = dados do som as_loopback (Speakers)
frames = b''.join(frames)

# frames2 = dados do som  Microfone
# frames2 = b''.join(frames2)

# decodificando os dados do Speaker
Sdecoded = np.frombuffer(frames, 'int16')

# decodificando o microfone
# Mdecoded = np.frombuffer(frames2, 'int16')

# convertendo os dados do Speaker em um vetor do tipo Numpy (facilitando a vida na hora de pegar os canais de áudio)
Sdecoded = np.array(Sdecoded, dtype='int16')

# pegando os dados do lado direito
direito = Sdecoded[1::2]

# pegando os dados do lado esquerdo
esquerdo = Sdecoded[::2]

# mixando tudo para mono = somar lado direito + lado esquerdo + os dados decofificados do Microfone q já estão em mono
mix = (direito+esquerdo)  # +Mdecoded

# garantindo que nenhum valor extrapole os limites do short int
signal = np.clip(mix, -32767, 32766)

# codificar os dados novamente
encodecoded = wave.struct.pack("%dh" % (len(signal)), *list(signal))


# parar todos os streams e finalizar o pyaudio
stream.stop_stream()
stream.close()
# stream2.stop_stream()
# stream2.close()
p.terminate()


# gravando o áudio mixado em mono
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes((encodecoded))
wf.close()
