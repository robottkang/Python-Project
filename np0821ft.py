import numpy as np
import matplotlib.pyplot as plt

# 파라미터 설정
sampling_rate = 1000  # 샘플링 주파수 (Hz)
duration = 1  # 파형의 지속 시간 (초)
num_samples = int(sampling_rate * duration)
time = np.linspace(0, duration, num_samples, endpoint=False)

# 주기가 다른 사인파 생성
frequencies = [5, 20, 50, 100, 200]  # 주파수 (Hz)
waves = []
for freq in frequencies:
    wave = np.sin(2 * np.pi * freq * time)
    waves.append(wave)

# 파형 그래프 표시 (원본)
plt.figure(figsize=(12, 10))
for i, wave in enumerate(waves):
    plt.subplot(len(frequencies), 4, i * 4 + 1)
    plt.plot(time, wave)
    plt.title(f'Original Wave - Frequency {frequencies[i]} Hz')
plt.tight_layout()
plt.show()
# 푸리에 트랜스폼 수행
fft_results = []
for wave in waves:
    fft_result = np.fft.fft(wave)
    fft_results.append(fft_result)

# 푸리에 변환된 결과 그래프 표시
plt.figure(figsize=(12, 10))
for i, fft_result in enumerate(fft_results):
    freqs = np.fft.fftfreq(num_samples, 1 / sampling_rate)
    plt.subplot(len(frequencies), 4, i * 4 + 1)
    plt.plot(freqs, np.abs(fft_result))
    plt.title(f'Frequency Domain - Frequency {frequencies[i]} Hz')
plt.tight_layout()
plt.show()
# 모든 푸리에 변환 결과를 합치고 역 푸리에 변환
summed_fft_result = np.sum(fft_results, axis=0)
restored_wave = np.fft.ifft(summed_fft_result)

# 역 푸리에 변환 결과 그래프 표시
plt.figure(figsize=(12, 5))
plt.plot(time, restored_wave.real)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Restored Wave from Summed Fourier Transform Results')
plt.tight_layout()

plt.show()


# 특정 주파수 제거
frequency_to_remove = [200, -200, 100, -100, 50, -50]  # 제거할 주파수 (Hz)
for fft_result in fft_results:
    freqs = np.fft.fftfreq(num_samples, 1 / sampling_rate)
    for freq_to_remove in frequency_to_remove:
        index_to_remove = np.argmin(np.abs(freqs - freq_to_remove))
        fft_result[index_to_remove] = 0


# 푸리에 변환된 결과 그래프 표시
plt.figure(figsize=(12, 10))
for i, fft_result in enumerate(fft_results):
    freqs = np.fft.fftfreq(num_samples, 1 / sampling_rate)
    plt.subplot(len(frequencies), 4, i * 4 + 1)
    plt.plot(freqs, np.abs(fft_result))
    plt.title(f'Frequency Domain - Frequency {frequencies[i]} Hz')
plt.tight_layout()
plt.show()
# 모든 푸리에 변환 결과를 합치고 역 푸리에 변환
summed_fft_result = np.sum(fft_results, axis=0)
restored_wave = np.fft.ifft(summed_fft_result)





# 역 푸리에 변환 결과 그래프 표시
plt.figure(figsize=(12, 5))
plt.plot(time, restored_wave.real)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Restored Wave from Summed Fourier Transform Results')
plt.tight_layout()

plt.show()