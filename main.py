import pygame as pg
import mandelbrot_set


def main() -> int:
    width, height = 500, 500
    max_iter = 100

    mandelbrot_points = mandelbrot_set.generate_set(width, height, max_iter)
    print(len(mandelbrot_points))
    pg.init()
    pg.display.set_caption("Fractals")
    window: pg.surface = pg.display.set_mode((width, width))
    clock: pg.time.Clock = pg.time.Clock()

    quit_t: bool = False
    fps = 60

    while not quit_t:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_t = True

        # Render
        window.fill((0, 0, 0))  # Background Color

        for (x, y) in mandelbrot_points:
            window.set_at((x, y), (255, 255, 255))

        pg.display.flip()
        clock.tick(fps)

    pg.quit()
    return 0


if __name__ == "__main__":
    main()
