import wave
import numpy as np

# Ses parametreleri
sample_rate = 44100  # Örnek hızı (44.1 kHz)
dot_duration = 0.2  # Nokta süresi (saniye)
dash_duration = 0.6  # Uzun çizgi süresi (saniye)
amplitude = 0.7  # Genlik (0-1 aralığında)

# Modülasyon sinyalinin oluşturulması (nokta)
t = np.linspace(0, dot_duration, int(sample_rate * dot_duration), endpoint=False)
modulation_signal_dot = amplitude * np.ones_like(t)

# Nokta taşıyıcı sinyalinin oluşturulması
carrier_signal_dot = np.sin(2 * np.pi * 1000 * t)  # 1000 Hz sinüzoidal sinyal

# Nokta ses dosyasının oluşturulması
dot_data = carrier_signal_dot * modulation_signal_dot
dot_data = dot_data / np.max(np.abs(dot_data))  # Normalize etme

with wave.open('dot.wav', 'w') as wav_file:
    wav_file.setnchannels(1)  # Tek kanallı (mono)
    wav_file.setsampwidth(2)  # 2 byte'lık örnekleme genişliği
    wav_file.setframerate(sample_rate)
    wav_file.writeframes((dot_data * 32767).astype(np.int16))

# Modülasyon sinyalinin oluşturulması (uzun çizgi)
t = np.linspace(0, dash_duration, int(sample_rate * dash_duration), endpoint=False)
modulation_signal_dash = amplitude * np.ones_like(t)

# Uzun çizgi taşıyıcı sinyalinin oluşturulması
carrier_signal_dash = np.sin(2 * np.pi * 1000 * t)  # 1000 Hz sinüzoidal sinyal

# Uzun çizgi ses dosyasının oluşturulması
dash_data = carrier_signal_dash * modulation_signal_dash
dash_data = dash_data / np.max(np.abs(dash_data))  # Normalize etme

with wave.open('dash.wav', 'w') as wav_file:
    wav_file.setnchannels(1)  # Tek kanallı (mono)
    wav_file.setsampwidth(2)  # 2 byte'lık örnekleme genişliği
    wav_file.setframerate(sample_rate)
    wav_file.writeframes((dash_data * 32767).astype(np.int16))
