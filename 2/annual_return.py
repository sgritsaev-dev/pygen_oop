def annual_return(start, percent, years):
    for _ in range(years):
        start = start + start * percent * 0.01
        yield start


for value in annual_return(70000, 8, 10):
    print(round(value))
