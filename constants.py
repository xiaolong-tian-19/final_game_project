SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 350
NUMBER_OF_PIPES = 4
PIPE_SIZE = PIPE_WIDTH, PIPE_HEIGHT = int(SCREEN_WIDTH / NUMBER_OF_PIPES * 1/4), SCREEN_HEIGHT
HEART_SIZE = HEART_WIDTH, HEART_HEIGHT = 20, 20
GAP_SIZE = GAP_WIDTH, GAP_HEIGHT = int(SCREEN_WIDTH / NUMBER_OF_PIPES - PIPE_WIDTH), int(SCREEN_HEIGHT * 3/7)
BIRD_SIZE = BIRD_WIDTH, BIRD_HEIGHT = 20, 20
PORTAL_SIZE = PORTAL_WIDTH, PORTAL_HEIGHT = 50, 50
RING_SIZE = RING_WIDTH, RING_HEIGHT = BIRD_WIDTH, BIRD_HEIGHT / 3
LIEF_SIZE = LIFE_WIDTH, LIFE_HEIGHT = 30, 30
LIEF_POS = LIFE_LEFT, LIFE_TOP = 430, 0
MEDAL_SIZE = MEDAL_WIDTH, MEDAL_HEIGHT = 30, 30
MEDAL_POS = MEDAL_LEFT, MEDAL_TOP = 320, 0
BOARD_SIZE = BOARD_WIDTH, BOARD_HEIGHT = 160, 80
BOARD_POS = BOARD_LEFT, BOARD_TOP = int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)
ACHIEVEMENT_POS = ACHIEVEMENT_LEFT, ACHIEVEMENT_TOP = 268, 205
POINTS_POS = POINTS_RIGHT, POINTS_TOP = 390, 200
BEST_POS = BEST_RIGHT, BEST_TOP = POINTS_RIGHT, POINTS_TOP+30
WORD_SIZE = WORD_WIDTH, WORD_HEIGHT = 200, 50
WORD_POS = WORD_X, WORD_Y = int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 3)
PIPE_VELOCITY = HEART_VELOCITY = PORTAL_VELOCITY = -5
BIRD_ACCELERATION = 1
BIRD_VELOCITY = -5
FPS = 20
SCREEN_COLOR = (200, 200, 200)