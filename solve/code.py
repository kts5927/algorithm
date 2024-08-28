I_tp = 2.0          # 터보펌프의 관성 모멘트 (kg·m²)
N_tp = 0.0          # 초기 각속도 (rad/s)
Gamma_tb = 10.0     # 터빈 토크 (N·m)
Gamma_pump = 3.0    # 펌프 토크 (N·m)
T = 5.0             # 총 시간 (s)
dt = 0.1            # 시간 단계 (s)

# 시간에 따른 변화 저장
times = [0]
omegas = [N_tp]

# Euler 방식으로 시간 단계별 계산
time = 0
while time < T:
    dN_tp_dt = (Gamma_tb - Gamma_pump) / I_tp  # 각가속도 계산
    N_tp += dN_tp_dt * dt                      # 각속도 업데이트
    time += dt
    times.append(time)
    omegas.append(N_tp)

# 결과를 txt 파일로 저장
output_path = 'C:\\Users\\admin\\Desktop\\펌프해석\\산화제펌프\\터보펌프_회전속도_결과.txt'
with open(output_path, 'w') as file:
    for t, omega in zip(times, omegas):
        file.write(f"Time: {t:.1f}s, N_tp: {omega:.2f} rad/s\n")

output_path