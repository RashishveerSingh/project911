def square_and_filter_odd_even(start, end):
    for i in range(start, end + 1):
        square = i ** 2
        print(f"Even square: {square}" if square % 2 == 0 else f"Odd square: {square}")

square_and_filter_odd_even(1, 10)