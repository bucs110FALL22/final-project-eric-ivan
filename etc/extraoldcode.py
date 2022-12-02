  # while self.playing:
        #     # check players input events
        #     self.check_events()
        #     # breaks loop but does not turn game off
        #     if self.START_KEY:
        #         self.playing = False
        #     # our canvas
        #     self.display.fill(self.BLACK)
        #     # text, size, x, y
        #     self.draw_text('Thanks for Playing', 20, self.DISPLAY_WIDTH / 2,
        #                    self.DISPLAY_HEIGHT / 2)
        #     # aligns display with window
        #     self.window.blit(self.display, (0, 0))
        #     pygame.display.update()  # physically moves image to display screen
        #     self.reset_keys()