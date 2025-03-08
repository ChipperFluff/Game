import arcade

class Master(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, fullscreen=True)
        self.background_color = arcade.color.WHITE

    def on_draw(self):
        self.clear()
        arcade.draw_text('Master', 400, 300, font_size=50, anchor_x='center', color=arcade.color.BLACK)

def main():
    window = Master()
    arcade.run()

if __name__ == '__main__':
    main()
    