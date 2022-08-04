def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit ()

             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit ()

    game.Display.fill(WHITE)
print("PAUSED", BLACK, -100)