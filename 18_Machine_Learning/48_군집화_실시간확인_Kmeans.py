import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sklearn.datasets import make_blobs, make_moons
from sklearn.cluster import DBSCAN, AgglomerativeClustering

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 미리 만들기
X, _ = make_blobs(n_samples=300, centers=3, random_state=42)
X_moon, _ = make_moons(n_samples=300, noise=0.1, random_state=42)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle('군집화 3가지 실시간 비교')

# ==============================================================
# K-Means 용 초기 중심점 설정
# ==============================================================
np.random.seed(42)
centers_km = X[np.random.choice(len(X), 3, replace=False)].copy()
# 랜덤으로 3개 점을 중심점으로 시작

colors3 = ['red', 'blue', 'green']

def get_labels(X, centers):
    # 각 점 → 중심점 3개 거리 계산 → 가장 가까운 그룹 번호 반환
    distances = np.linalg.norm(X[:, np.newaxis] - centers, axis=2)
    return np.argmin(distances, axis=1)

# ==============================================================
# 매 프레임마다 실행되는 함수
# frame = 0, 1, 2, ... 순서로 자동으로 들어옴
# ==============================================================
def update(frame):
    global centers_km  # 전역변수 중심점을 업데이트하기 위해

    # -----------------------------------------------
    # 1번 그래프 : K-Means
    # -----------------------------------------------
    ax1 = axes[0]
    ax1.clear()

    if frame < 10:
        # 처음 10프레임 = K-Means 중심점 이동 과정
        labels = get_labels(X, centers_km)

        for i in range(3):
            mask = labels == i          # i번 그룹인 점들만 골라내기
            ax1.scatter(X[mask, 0], X[mask, 1], c=colors3[i], alpha=0.5, s=30)

        ax1.scatter(centers_km[:, 0], centers_km[:, 1],
                    c='black', marker='X', s=300, zorder=5, label='중심점')
        ax1.set_title(f'K-Means - {frame+1}번째 이동 중')
        ax1.legend()

        # 중심점을 그룹 평균 위치로 이동
        centers_km[:] = np.array([X[labels == i].mean(axis=0) for i in range(3)])

    else:
        # 10프레임 이후 = 완성된 결과 고정
        labels = get_labels(X, centers_km)
        for i in range(3):
            mask = labels == i
            ax1.scatter(X[mask, 0], X[mask, 1], c=colors3[i], alpha=0.5, s=30)
        ax1.scatter(centers_km[:, 0], centers_km[:, 1],
                    c='black', marker='X', s=300, zorder=5, label='중심점')
        ax1.set_title('K-Means - 완성')
        ax1.legend()

    # -----------------------------------------------
    # 2번 그래프 : DBSCAN - 점 하나씩 추가
    # -----------------------------------------------
    ax2 = axes[1]
    ax2.clear()

    # frame 을 0~299 범위로 변환
    n = min(frame * 10 + 1, 300)   # 한 프레임에 10개씩 추가 (빠르게)
    X_part = X_moon[:n]             # n개까지만 잘라서 사용

    if n >= 10:
        # 점이 10개 이상일 때만 DBSCAN 실행 (너무 적으면 오류남)
        db = DBSCAN(eps=0.2, min_samples=5)
        labels_db = db.fit_predict(X_part)
        ax2.scatter(X_part[:, 0], X_part[:, 1], c=labels_db, cmap='Set1', alpha=0.6, s=30)
    else:
        ax2.scatter(X_part[:, 0], X_part[:, 1], c='gray', alpha=0.6, s=30)

    ax2.set_title(f'DBSCAN - {n}개 추가 중')
    ax2.set_xlim(X_moon[:, 0].min() - 0.3, X_moon[:, 0].max() + 0.3)
    ax2.set_ylim(X_moon[:, 1].min() - 0.3, X_moon[:, 1].max() + 0.3)

    # -----------------------------------------------
    # 3번 그래프 : 계층적 군집화 - 점 하나씩 추가
    # -----------------------------------------------
    ax3 = axes[2]
    ax3.clear()

    n2 = min(frame * 10 + 1, 300)  # 한 프레임에 10개씩 추가
    X_part2 = X[:n2]

    if n2 >= 4:
        # 점이 4개 이상일 때만 계층적 군집화 실행
        hc = AgglomerativeClustering(n_clusters=min(3, n2))
        # min(3, n2) → 점이 3개 미만이면 그룹도 그 수만큼만
        labels_hc = hc.fit_predict(X_part2)
        ax3.scatter(X_part2[:, 0], X_part2[:, 1], c=labels_hc, cmap='Set1', alpha=0.6, s=30)
    else:
        ax3.scatter(X_part2[:, 0], X_part2[:, 1], c='gray', alpha=0.6, s=30)

    ax3.set_title(f'계층적 군집화 - {n2}개 추가 중')
    ax3.set_xlim(X[:, 0].min() - 1, X[:, 0].max() + 1)
    ax3.set_ylim(X[:, 1].min() - 1, X[:, 1].max() + 1)

    plt.tight_layout()

ani = animation.FuncAnimation(
    fig,
    update,
    frames=40,      # 총 40프레임
    interval=300,   # 0.3초마다 업데이트
    repeat=False
)

plt.tight_layout()
plt.show()