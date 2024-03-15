import cv2
from pyzbar.pyzbar import decode
import pygame
import sys

def display_content(content):
    # В данном примере просто печатаем содержимое метки
    print("Содержимое метки:", content)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("AR Scanner")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        for code in decode(frame):
            content = code.data.decode('utf-8')
            display_content(content)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        pygame_frame = pygame.surfarray.make_surface(frame)
        screen.blit(pygame_frame, (0, 0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                cap.release()
                sys.exit()

if __name__ == "__main__":
    main()
