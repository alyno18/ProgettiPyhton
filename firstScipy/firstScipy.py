import numpy as np
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


class SineWave:
    def __init__(self, amplitude, frequency, sampling_rate, duration, phase=0.0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.sampling_rate = sampling_rate
        self.duration = duration
        self.phase = phase
        self.time_index = np.linspace(0, self.duration, int(self.sampling_rate * self.duration))
        print(int(self.sampling_rate * self.duration))

    def sine_wave(self):
        sig = self.amplitude * np.sin(2 * np.pi * self.frequency * self.time_index + self.phase)
        return sig

    def cosine_wave(self):
        sig = self.amplitude * np.cos(2 * np.pi * self.frequency * self.time_index + self.phase)
        return sig

    def get_time_index(self):
        return self.time_index


from scipy import signal

sine_wave_generator = SineWave(amplitude=2.0, frequency=10.0, sampling_rate=200.0, duration=1.0)
sin_wave = sine_wave_generator.sine_wave()
cos_wave = sine_wave_generator.cosine_wave()
fig, ax = plt.subplots(2)
ax[0].plot(sine_wave_generator.get_time_index(), sin_wave)
# ax[0].stem(sine_wave_generator.get_time_index(), sin_wave)
ax[0].set(title="Funzione seno", ylabel="sin[n]")
ax[1].plot(sine_wave_generator.get_time_index(), cos_wave)
# ax[1].stem(sine_wave_generator.get_time_index(), cos_wave)
ax[1].set(title="Funzione coseno", ylabel="cos[n]", xlabel="Timestep n (discreto)")
plt.show()

from scipy import special as sp

sampling_rate = 300.0
duration = 0.5

time_index = np.linspace(-10, 10, int(sampling_rate * duration))
sinc = sp.sinc(time_index)
plt.plot(time_index, sinc)
plt.title("Funzione sinc")
plt.xlabel("Timestep n")
plt.ylabel("sinc(x)")
plt.show()

from scipy.fft import fft, fftfreq, ifft

sampling_rate1 = 200.0
duration1 = 0.5

sine_wave_generator1 = SineWave(amplitude=2.0, frequency=10.0, sampling_rate=sampling_rate1, duration=duration1)
sin_wave1 = sine_wave_generator1.sine_wave()
sin_fft = fft(sin_wave1)
xf = fftfreq(int(sampling_rate1*duration1), 1.0/sampling_rate1)
fig1, ax1 = plt.subplots(3)
ax1[0].plot(sine_wave_generator1.get_time_index(), sin_wave1)
ax1[0].set(title="Funzione seno", ylabel="sin[n]", xlabel="Timestep n")
ax1[1].plot(xf, np.abs(sin_fft))
ax1[1].set(title="fft funzione seno", ylabel="|FFT(sin[n])|", xlabel="frequency")

yinv = ifft(sin_fft)
ax1[2].plot(sine_wave_generator1.get_time_index(), yinv)
ax1[2].set(title="Funzione seno riscostruita con IFFT", xlabel="Timestep n", ylabel="sin[n]")
plt.show()


from scipy import signal

sig = np.repeat([0., 1., 0.], 100)
win = signal.windows.hann(50)
convolution = signal.convolve(sig, win, mode="same") / sum(win)

fig2, ax2 = plt.subplots(3, 1, sharex=True)
ax2[0].plot(sig)
ax2[0].set_title("Original pulse")
ax2[0].margins(0, 0.1)
ax2[1].plot(win)
ax2[1].set_title("Filter impulse response")
ax2[1].margins(0, 0.1)
ax2[2].plot(convolution)
ax2[2].set_title("Filtered sign")
ax2[2].margins(0, 0.1)
plt.show()

sampling_rate2 = 1000
s1 = SineWave(amplitude=1.0, frequency=10, sampling_rate=sampling_rate2, duration=2.0)
s2 = SineWave(amplitude=1.0, frequency=100, sampling_rate=sampling_rate2, duration=2.0)
signal1 = s1.sine_wave()+s2.sine_wave()
b1 = signal.firwin(40, 20, fs=sampling_rate2)
filtered = signal.convolve(signal1, b1, mode="same")
fig3, ax3 =plt.subplots(3)
ax3[0].plot(s1.time_index, signal1)
ax3[0].set(title="Segnale originale", ylabel="s[n]", xlabel="Timestep n")
w1, h1 = signal.freqz(b1)
ax3[2].plot(w1, 20*np.log10(np.abs(h1)), "b")
ax3[2].set(title="Risposta in frequenza del filtro passa banda", ylabel="Modulo(dB)", xlabel="Frequenza (rad/sample)")
plt.grid()
plt.show()


A = np.array([[0, 1], [1, 0]])
B = np.array([[0], [1]])
C = np.array([[1], [0]])
D = np.array([[0]])
sys = signal.StateSpace(A, B, C, D)
print(sys)
print(("Matrice A: \n", sys.A))
print(("Matrice B: \n", sys.B))
print(("Matrice C: \n", sys.C))
print(("Matrice D: \n", sys.D))
print("Poli del sistema: ", sys.poles)
print("Zeri del sistema: ", sys.zeros)
sys_tf = sys.to_tf()
sys_zpk = sys.to_zpk()
print(sys_tf)
print(sys_zpk)


num = [1]
den = [1, 0, -1]

sys1 = signal.TransferFunction(num, den)
print(sys)
sys1_state_space = sys1.to_ss()
sys1_zpk = sys1.to_zpk()
print(sys1_state_space)
print(sys1_zpk)

sys2 = signal.ZerosPolesGain([], [1 -1], [1])
print(sys2)
sys2_state_space = sys2.to_ss()
sys2_tf = sys2.to_tf()
print(sys2_state_space)
print(sys2_tf)


A1 = np.array([[0, 1], [1, 0]])
B1 = np.array([[0], [1]])
C1 = np.array([[1], [0]])
D1 = 0
sys3 = signal.StateSpace(A1, B1, C1, D1)
fig4, ax4 = plt.subplots(2)
w, mag, phase = signal.bode(sys3)
ax4[0].semilogx(w, mag)
ax4[0].grid(True, which="both")
ax4[0].set(title="Diagramma di Bode del modulo", ylabel="dB")
ax4[1].semilogx(w, phase)
ax4[1].grid(True, which="both")
ax4[1].set(title="Diagramma di Bode della fase", xlabel="rad/s", ylabel="gradi")
plt.show()


A2 = np.array([[0., 1.], [1., 0.]])
B2 = np.array([[1.], [0.]])
C2 = np.array([0., 1.])
D2 = [0.]
sys4 = signal.StateSpace(A2, B2, C2, D2)
t, y = signal.step(sys4)
fig5, ax5 = plt.subplots(1)
ax5.plot(t, y)
ax5.set(title="Risposta la gradino", xlabel="Secondi", ylable="y(t)")
plt.show()


sys5 = signal.ZerosPolesGain([], [-1 -10], 1)
t1, y1 = signal.impulse(sys5)
fig6, ax6 = plt.subplots(1)
ax6.plot(t1, y1)
ax6.set(title="Risposta all'impulso", xlabel="Secondi", ylabel="y(t)")
plt.show()


t2 = np.linspace(0, 3, 500, endpoint=False)
u = np.cos(2*np.pi*4*t2)
tout, yout, xout = signal.lsim(sys4, u, t2)
fig7, ax7 = plt.subplots(1)
ax7.plot(t2, yout)
ax7.set(title="Risposta all'ingresso sinusoidale", xlabel="Secondi", ylable="y(t)")
plt.show()

tout1, yout1, xout1 = signal.lsim(sys5, u, t2)
fig8, ax8 = plt.subplots(1)
ax8.plot(t2, yout1)
ax8.set(title="Risposta all'ingresso sinusoidale", xlabel="Secondi", ylable="y(t)")
plt.show()
