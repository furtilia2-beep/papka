from pygame import*
window = display.set_mode((700,500))
display.set_caption('тест')
background = transform.scale(image.load('giga.webp'),(700,500))




game = True
while game:
    window.blit(background,(0,0))


    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()


































