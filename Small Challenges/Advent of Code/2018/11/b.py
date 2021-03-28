# Requires numpy
import numpy as np

INPUT = 7347

# Generate board: individually for each square
def generate_board(seed):
    board = [[0 for x in range(300)] for y in range(300)]
    for x in range(300):
        for y in range(300):
            raw_val = ((x+1)+10)*(seed + (y+1)*((x+1)+10))
            board[y][x] = ((raw_val // 100) % 10) - 5
    return board

# FFT method - convolve in freq. domain and convert bacl
# Some adjustments are hardcoded - e.g. (maxs - 2)
if __name__ == "__main__":
    board = generate_board(INPUT)
    board_array = np.array(board)

    # Max properties
    max_val = 0
    max_pos = (-1,-1)
    best_size = 0

    # Kernel size: 1 - 300
    for sz in range(1,300):
        # Generate kernel as np array
        kernel = np.array([[1 if x < sz and y < sz else 0
                   for x in range(300)] for y in range(300)])

        # Frequency domain
        b_fft = np.fft.fft2(board_array)
        k_fft = np.fft.fft2(kernel)

        # Convolve and invert
        result = np.fft.ifft2(np.multiply(b_fft, k_fft))

        # Test maximum of convolution
        if result.max() > max_val:
            max_val = result.max()
            max_pos = np.unravel_index(result.argmax(), result.shape)
            best_size = sz

    # Print max. note the index adjustment, due to flipping of kernel in
    # convolution. So top left becomes bottom right, which needs to be reversed
    max_pos = (max_pos[0]-(best_size-1) + 1, max_pos[1] - (best_size-1) + 1)
    print((max_pos[1], max_pos[0], best_size))

    
