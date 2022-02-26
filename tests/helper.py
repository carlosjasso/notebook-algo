from time import perf_counter

def print_ruled(message: str, new_line: bool = True) -> None:
    ruller = "-" * int((70 - len(message)) / 2)
    br = "\n" if new_line else ""
    print(f"{br}{ruller} {message} {ruller}")

def benchmark_start() -> float:
    return perf_counter()

def benchmark_stop(start: float) -> None:
    diff = perf_counter() - start
    print(f"\ttook: {diff} seconds")
