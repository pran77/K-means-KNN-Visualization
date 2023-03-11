import pygame
import math
from pygame import gfxdraw
import random

pygame.init()
background_colour = (255, 255, 255)
(width, height) = (1000, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('K-means KNN')
screen.fill(background_colour)
pygame.display.flip()
running = True

points = []
centroids = []
number_of_points = 1


def knn(p, input_point, k_value, np):      # np = number of points
    dist = []
    xo = input_point[0]
    yo = input_point[1]
    for i in range(np):
        xi = p[i][0]
        yi = p[i][1]
        _class = p[i][2]
        d = math.sqrt((xo - xi)**2 + (yo - yi)**2)
        dist.append([d, _class, xi, yi])

    dist = sorted(dist)

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in range(k_value):
        if dist[i][1] == 'C1':
            cnt1 += 1
        elif dist[i][1] == 'C2':
            cnt2 += 1
        else:
            cnt3 += 1

        xi = dist[i][2]
        yi = dist[i][3]
        pygame.draw.line(screen, (50, 50, 50), (xo, yo), (xi, yi), width=2)
        pygame.display.update()

    maxi = max(cnt1, cnt2, cnt3)
    if maxi == cnt1:
        gfxdraw.aacircle(screen, xo, yo, 5, (255, 0, 0))
        pygame.display.update()
    elif maxi == cnt2:
        gfxdraw.aacircle(screen, xo, yo, 5, (0, 255, 0))
        pygame.display.update()
    else:
        gfxdraw.aacircle(screen, xo, yo, 5, (0, 0, 255))
        pygame.display.update()

    return


def draw_point(point, col):
    points.append(point)
    xx = int(point[0])
    yy = int(point[1])
    gfxdraw.aacircle(screen, xx, yy, 5, col)
    gfxdraw.filled_circle(screen, xx, yy, 5, col)
    pygame.display.update()
    return


def generate_random_centroids(kkk, _points):
    st = set()
    while len(st) != kkk:
        ind = random.randint(0, len(_points))
        st.add(ind)

    for ind in st:
        center = [_points[ind][0], _points[ind][1]]
        centroids.append(center)

    return centroids


def k_means(data_points, kk):
    _centroids = generate_random_centroids(kk, points)
    number_of_iterations = 0
    while number_of_iterations < 50:
        for i in range(len(data_points)):
            c1 = tuple(_centroids[0])
            c2 = tuple(_centroids[1])
            c3 = tuple(_centroids[2])
            ls = [data_points[i][0], data_points[i][1]]
            p = tuple(ls)

            d1 = math.dist(c1, p)
            d2 = math.dist(c2, p)
            d3 = math.dist(c3, p)

            mini = min(d1, d2, d3)
            if mini == d1:
                draw_point(data_points[i], (255, 0, 0))
                data_points[i][2] = 'C1'
                draw_point(_centroids[0], (255, 255, 255))
                _centroids[0][0] = (_centroids[0][0]+data_points[i][0])/2
                _centroids[0][1] = (_centroids[0][1]+data_points[i][1])/2
                draw_point(_centroids[0], (255, 255, 0))
            elif mini == d2:
                draw_point(data_points[i], (0, 255, 0))
                data_points[i][2] = 'C2'
                draw_point(_centroids[1], (255, 255, 255))
                _centroids[1][0] = (_centroids[1][0]+data_points[i][0])/2
                _centroids[1][1] = (_centroids[1][1]+data_points[i][1])/2
                draw_point(_centroids[1], (255, 255, 0))
            else:
                draw_point(data_points[i], (0, 0, 255))
                data_points[i][2] = 'C3'
                draw_point(_centroids[2], (255, 255, 255))
                _centroids[2][0] = (_centroids[2][0]+data_points[i][0])/2
                _centroids[2][1] = (_centroids[2][1]+data_points[i][1])/2
                draw_point(_centroids[2], (255, 255, 0))

        pygame.display.update()
        number_of_iterations += 1

        return


no_of_points = int(input('Enter no_of_points : '))
counter = 1
while running:
    for event in pygame.event.get():
        pygame.event.pump()
        if event.type == pygame.MOUSEBUTTONDOWN and counter == 1:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = list(mouse_pos)
            mouse_pos.append('C')
            if number_of_points <= no_of_points:
                draw_point(mouse_pos, (0, 0, 0))
                number_of_points += 1
            elif number_of_points == no_of_points+1:
                counter += 1

        if event.type == pygame.MOUSEBUTTONDOWN and counter == 2:
            k_means(points, 3)
            counter += 1

        if event.type == pygame.MOUSEBUTTONDOWN and counter == 3:
            k = int(input('Enter k value: '))
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = list(mouse_pos)
            draw_point(mouse_pos, (0, 0, 0))
            pygame.event.pump()
            knn(points, mouse_pos, k, no_of_points)
            counter += 1

        if event.type == pygame.QUIT:
            running = False


print(points)
