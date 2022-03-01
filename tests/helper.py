from time import perf_counter_ns

def print_ruled(message: str, new_line: bool = True) -> None:
    ruller = "-" * int((70 - len(message)) / 2)
    br = "\n" if new_line else ""
    print(f"{br}{ruller} {message} {ruller}")

def benchmark_start() -> float:
    return perf_counter_ns()

def benchmark_stop(start: float) -> None:
    diff = perf_counter_ns() - start
    if diff >= 1_000_000_000:
        print(f"\ttook: {diff / 1_000_000_000 : .2f} seconds")
    elif diff >= 1_000_000:
        print(f"\ttook: {diff / 1_000_000 : .2f} microseconds")
    elif diff >= 1_000:
        print(f"\ttook: {diff / 1_000 : .2f} milliseconds")
    else:
        print(f"\ttook: {diff : .2f} nanoseconds")

