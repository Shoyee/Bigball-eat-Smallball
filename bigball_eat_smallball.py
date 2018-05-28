'''
大球吃小球游戏规则:
    点击屏幕任意位置(球的圆心点) 生成一个球 随机颜色 随机半径的球
        检测与屏幕边缘的碰撞
        检测球与球之间的碰撞
            小球和大球进行碰撞  大球把小球吃掉 大球半径加大
'''
#!/usr/bin/env python3
#coding:utf-8
import pygame
import random

class Color(object):
    @classmethod
    def random_color(cls):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        return (red,green,blue)

class Ball(object):
    def __init__(self,x,y,radius,sx,sy,color):
        '''
        初始化球对象的方法
        :param x: 圆心点横坐标
        :param y: 圆心点纵坐标
        :param radius: 半径
        :param sx: 横坐标位移
        :param sy: 纵坐标位移
        :param color: 颜色
        '''
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        #存活状态
        self.alive = True

    def move(self,window):
        self.x += self.sx
        self.y += self.sy

        if self.x - self.radius <= 0 or self.x + self.radius >= window.get_width():
            self.sx = -self.sx

        if self.y - self.radius <= 0 or self.y + self.radius >= window.get_height():
            self.sy = -self.sy

    def eat(self,other_ball):
        if other_ball.alive and self.alive and other_ball != self:
            dx, dy = (self.x - other_ball.x), (self.y - other_ball.y)
            distance = (dx ** 2 + dy ** 2) - (self.radius + other_ball.radius) ** 2
            if distance <= 0 and self.radius > other_ball.radius:
                other_ball.alive = False
                self.radius += int(other_ball.radius * 0.1)

    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)


def main():
    pygame.init()
    screen = pygame.display.set_mode((900,700))
    pygame.display.set_caption("大球吃小球")

    running_flag = True

    ball_lst = []

    while running_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_flag = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                radius = random.randint(10,60)
                color = Color.random_color()
                sx, sy = random.randint(-5,5), random.randint(-5,5)
                ball = Ball(x,y,radius,sx,sy,color)
                ball_lst.append(ball)
        screen.fill((255,255,255))
        for b in ball_lst:
            if b.alive:
                b.draw(screen)
            else:
                ball_lst.remove(b)

        pygame.display.flip()

        pygame.time.delay(50)
        for b in ball_lst:
            b.move(screen)
            for other in ball_lst:
                b.eat(other)

if __name__ == "__main__":
    main()
