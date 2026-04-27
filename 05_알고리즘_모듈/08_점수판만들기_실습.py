import random
import pygame

pygame.init()
화면 = pygame.display.set_mode((800, 600))
pygame.display.set_caption("별 먹기 게임")
시계 = pygame.time.Clock()

# 색상 및 초기값
검정, 빨강, 노랑, 흰색 = (0,0,0), (255,0,0), (255,255,0), (255,255,255)
공_x, 공_y, 공크기, 속도 = 400, 300, 20, 7
별크기, 점수 = 10, 5 # 시작 점수를 5점으로 설정해볼게요

# 폰트 설정 (한글 깨짐 방지: 시스템 폰트 사용 예시)
폰트 = pygame.font.SysFont('malgungothic', 36)

# 별 초기 위치 & 시간 설정
별_x = random.randint(별크기, 800 - 별크기)
별_y = random.randint(별크기, 600 - 별크기)
별_생성시간 = pygame.time.get_ticks() # 별이 만들어진 시점 (ms 단위)

실행중 = True
while 실행중:
    현재시간 = pygame.time.get_ticks()

    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT:
            실행중 = False

    # 공 이동
    키 = pygame.key.get_pressed()
    if 키[pygame.K_LEFT]:  공_x -= 속도
    if 키[pygame.K_RIGHT]: 공_x += 속도
    if 키[pygame.K_UP]:    공_y -= 속도
    if 키[pygame.K_DOWN]:  공_y += 속도

    공_x = max(공크기, min(800 - 공크기, 공_x))
    공_y = max(공크기, min(600 - 공크기, 공_y))

    # [알고리즘 1] 충돌 계산 (피타고라스 정리)
    거리 = ((공_x - 별_x)**2 + (공_y - 별_y)**2) ** 0.5
    if 거리 < 공크기 + 별크기:
        점수 += 1
        별_x = random.randint(별크기, 800 - 별크기)
        별_y = random.randint(별크기, 600 - 별크기)
        별_생성시간 = 현재시간 # 먹었으니 시간 리셋

    # [알고리즘 2] 시간 초과 감지 (3초 제한)
    if 현재시간 - 별_생성시간 > 3000:
        점수 -= 1
        별_x = random.randint(별크기, 800 - 별크기)
        별_y = random.randint(별크기, 600 - 별크기)
        별_생성시간 = 현재시간 # 실패했으니 시간 리셋

    # [알고리즘 3] 게임 종료 조건
    if 점수 <= 0:
        print("게임 오버!")
        실행중 = False

    # 화면 그리기
    화면.fill(검정)
    pygame.draw.circle(화면, 빨강, (공_x, 공_y), 공크기)
    pygame.draw.circle(화면, 노랑, (별_x, 별_y), 별크기)

    # 점수 표시 (한글 출력)
    점수판 = 폰트.render(f"현재 점수: {점수}", True, 흰색)
    화면.blit(점수판, (10, 10))

    pygame.display.flip()
    시계.tick(60)

pygame.quit()