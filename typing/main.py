from typing import List, Dict, Set, Optional, Any, Sequence, Tuple, Callable, TypeVar

x: int = 1
y: str = "tim"


def add_numbers(a:int, b:int, c:int) -> int :
    return sum([a, b, c])

print(add_numbers(1, 2, 3))

arr: list[list[int]] = [[1, 2]]
arr2: List[List[str]] =[["hello", "world"]]

d1: dict[str, str] = {"a": "b"}
d2: Dict[str, int] = {"a": 1}

s1: set[str] = {"a", "b"}
s2: Set[int] = {1, 2}

Vector = List[float]

def foo(v: Vector) -> Vector:
    return v

foo([1.1, 1.2])

Vectors = List[Vector]

def bar(vs: Vectors, idx: int) -> Vector:
    return vs[idx]

bar([[1, 2]], 0)

def baz(output: Optional[bool]=False) -> None:
    print(output)

baz()

def birr(output: Any) -> None:
    print(output)

birr(1)

def fuzz(seq: Sequence[str]) -> None:
    print(seq)

fuzz(["a", "b", "c"])
fuzz(["hello", "world", "!"])
fuzz("hello")

t: tuple = (1, 2, 3, "hello")

t1: tuple[int, str, int] = (1, "helo", 2)
t2: Tuple[str, int, str] = ("hello", 1, "world")


def get_cb(cb: Callable[[int, int], int], arg1: int, arg2: int) -> int:
    return cb(arg1, arg2)

print(get_cb(lambda x, y: x + y, 1, 2))


def ret_add() -> Callable[[int, int], int]:
    return lambda x, y: x + y

adder = ret_add()
print(adder(1, 2))


T = TypeVar('T')

def get_item(lst: list[T], idx: int) -> T:
    return lst[idx]

it = get_item([1, 2, 3], 0)
