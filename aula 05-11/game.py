import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))

branco = (255,255,255)
azul = (0,150,150)

pygame.draw.line(DISPLAYSURF, azul, (50,50), (200,50))

xini = 50
xfim = 200

yini = 50
yfim = 50

anda = False

velocidade = 0.1

while True:
	lista = pygame.event.get()
	for evento in lista:
		print evento
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_SPACE:
				DISPLAYSURF.fill(branco)
				pygame.draw.line(DISPLAYSURF, azul, (xini,yini), (xfim,yfim))
			if evento.key == pygame.K_RIGHT:
				anda = True
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()

	if anda == True:
		xini = xini + velocidade
		xfim = xfim + velocidade
		DISPLAYSURF.fill(branco)
		pygame.draw.line(DISPLAYSURF, azul, (xini,yini), (xfim,yfim))

	if xfim >= 400:
		velocidade = -velocidade

	if xini <= 0:
		velocidade = -velocidade

	pygame.display.update()
