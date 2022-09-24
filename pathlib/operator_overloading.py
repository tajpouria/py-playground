from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Vector():
    x: float
    y: float

    def __truediv__(self, other: float) -> Vector:
        return Vector(self.x / other, self.y / other)

    
def main() -> None:
    v = Vector(2, 4)
    print(v / 2)
    

if __name__ == "__main__":
    main()

