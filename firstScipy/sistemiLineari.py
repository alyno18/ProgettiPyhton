import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

A = np.array([[0, 1], [1, 0]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])
sys = signal.StateSpace(A, B, C, D)
print(sys)
print("Matrice A: \n", sys.A)
print("Matrice B: \n", sys.B)
print("Matrice C: ", sys.C)
print("Matrice D: ", sys.D)
print("Poli del sistema: ", sys.poles)
print("Zeri del sistema: ", sys.zeros)
sys_tf = sys.to_tf()
sys_zpk = sys.to_zpk()
print(sys_tf)
print(sys_zpk)

num = [1]
den = [1, 0, -1]

sys1 = signal.TransferFunction(num, den)
print(sys1)
sys1_state_space = sys1.to_ss()
sys1_zpk = sys1.to_zpk()
print(sys1_state_space)
print(sys1_zpk)

sys2 = signal.ZerosPolesGain([], [1, -1], [1])
print(sys2)
sys2_state_space = sys2.to_ss()
sys2_tf = sys2.to_tf()
print(sys2_state_space)
print(sys2_tf)

# diagramma di Bode

A1 = np.array([[0, 1], [1, 0]])
B1 = np.array([[0], [1]])
C1 = np.array([1, 0])
D1 = 0
sys3 = signal.StateSpace(A1, B1, C1, D1)
fig1, ax1 = plt.subplots(2)
w, mag, phase = signal.bode(sys3)
ax1[0].semilogx(w, mag)
ax1[0].grid(True, which="both")
ax1[0].set(title="Diagramma di Bode del modulo", ylabel="dB")
ax1[1].semilogx(w, phase)
ax1[1].grid(True, which="both")
ax1[1].set(title="Diagramma di Bode della fase", xlabel="rad/s", ylabel="gradi°")
plt.show()


# sistemi lineari
A2 = np.array([[0., 1.], [1., 0.]])
B2 = np.array([[1.], [0.]])
C2 = np.array([0., 1.])
D2 = [0.]
sys4 = signal.StateSpace(A2, B2, C2, D2)
sys5 = signal.ZerosPolesGain([], [-1, - 10], 1)

# risposta al gradino StateSpace
t, y = signal.step(sys4)
fig2, ax2 = plt.subplots(1)
ax2.plot(t, y)
ax2.set(title="Risposta al gradino", xlabel="Secondi", ylabel="y(t)")
plt.show()

# risposta al gradino ZerosPolesGain
t1, y1 = signal.step(sys5)
fig3, ax3 = plt.subplots(1)
ax3.plot(t1, y1)
ax3.set(title="Risposta al gradino", xlabel="Secondi", ylabel="y(t)")
plt.show()

# risposta all'impulso StateSpace
t2, y2 = signal.impulse(sys4)
fig4, ax4 = plt.subplots(1)
ax4.plot(t2, y2)
ax4.set(title="Risposta all'impulso", xlabel="Secondi", ylabel="y(t)")
plt.show()

# risposta all'impulso ZerosPolesGain
t3, y3 = signal.impulse(sys5)
fig5, ax5 = plt.subplots(1)
ax5.plot(t3, y3)
ax5.set(title="Risposta all'impulso", xlabel="Secondi", ylabel="y(t)")
plt.show()


t4 = np.linspace(0, 3, 500, endpoint=False)
u = np.cos(2*np.pi*4*t4)

# risposta all'ingresso sinusoidale StateSpace
tout, yout, xout = signal.lsim(sys4, u, t4)
fig6, ax6 = plt.subplots(1)
ax6.plot(t4, yout)
ax6.set(title="Risposta all'ingresso sinusoidale", xlabel="Secondi", ylabel="y(t)")
plt.show()

# risposta all'ingresso sinusoidale ZerosPolesGain
tout1, yout1, xout1 = signal.lsim(sys5, u, t4)
fig7, ax7 = plt.subplots(1)
ax7.plot(t4, yout1)
ax7.set(title="Risposta all'ingresso sinusoidale", xlabel="Secondi", ylabel="y(t)")
plt.show()

# esempio circuito RLC: TF, zeri, poli e guadagno
print("esempio circuito RLC: TF, zeri, poli e guadagno")
A3 = np.array([[-1., -1., 0.], [1., -1., 1.], [0., 1., -1.]])
B3 = np.array([[1.], [0.], [0.]])
C3 = np.array([0., 1., -1.])
D3 = [0.]

sys6 = signal.StateSpace(A3, B3, C3, D3)
print(sys6.to_zpk())
print(sys6.to_tf())

w1, mag1, phase1 = signal.bode(sys6)
fig8, ax8 = plt.subplots(2)
ax8[0].semilogx(w1, mag1)
ax8[0].grid(True, which="both")
ax8[0].set(title="Diagramma di Bode del modulo", ylabel="dB")
ax8[1].semilogx(w1, phase1)
ax8[1].grid(True, which='both')
ax8[1].set(title="Diagramma di Bode della fase", xlabel="rad/s", ylabel="gradi°")
plt.show()

tout2, yout2 = signal.impulse(sys6)
fig9, ax9 = plt.subplots(1)
ax9.plot(tout2, yout2)
ax9.set(title="Risposta all'impulso", xlabel="Secondi", ylabel="y(t)")
plt.show()

tout3, yout3 = signal.step(sys6)
fig11, ax11 = plt.subplots(1)
ax11.plot(tout3, yout3)
ax11.set(title="Risposta al gradino", xlabel="Secondi", ylabel="y(t)")
plt.show()

t5 = np.linspace(0, 20, 2000)

u1 = np.sin(1*t5)  # w=1
tout4, yout4, xout4 = signal.lsim(sys6, u1, t5)
fig22, ax22 = plt.subplots(1)
ax22.plot(tout4, yout4)
ax22.set(title="Risposta all'ingresso sinusoidale w=1", xlabel="Secondi", ylabel="y(t)")
plt.show()

u2 = np.sin(10*t5)  # w=10
tout5, yout5, xout5 = signal.lsim(sys6, u2, t5)
fig33, ax33 = plt.subplots(1)
ax33.plot(tout5, yout5)
ax33.set(title="Risposta all'ingresso sinusoidale w=10", xlabel="Secondi", ylabel="y(t)")
plt.show()

u3 = np.sin(100*t5)  # w=10
tout6, yout6, xout6 = signal.lsim(sys6, u3, t5)
fig44, ax44 = plt.subplots(1)
ax44.plot(tout6, yout6)
ax44.set(title="Risposta all'ingresso sinusoidale w=100", xlabel="Secondi", ylabel="y(t)")
plt.show()
