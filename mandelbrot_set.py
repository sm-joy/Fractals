from complex_number import Complex
from tqdm import tqdm


def map_value(value, old_min, old_max, new_min, new_max) -> float:
    return (value - old_min) / (old_max - old_min) * (new_max - new_min) + new_min


def in_mandelbrot_set(c: Complex, max_iter: int = 1000) -> bool:
    z: Complex = Complex(0, 0)
    for _ in range(max_iter):
        z = (z*z) + c
        if z.modulus() > 2:
            return False
    return True


def generate_set(width: int, height: int, max_iter: int) -> list[tuple[int, int]]:
    mandelbro_set: list[tuple[int, int]] = []
    with tqdm(total=width*height, desc="Generating Mandelbrot Set") as pbar:
        for x in range(width):
            for y in range(height):
                c = Complex(map_value(x, 0, width, -2, 2), map_value(y, 0, height, -2, 2))
                if in_mandelbrot_set(c, max_iter):
                    mandelbro_set.append((x,y))
                pbar.update(1)
    return mandelbro_set
