class CarRegistry:
    def generate_id(self, brand: str) -> str:
        return brand.join("YOUYOUYOU")


class Application:
    def register_vehicle(self, brand: str) -> None:
        cr = CarRegistry()
        print(cr.generate_id(brand))


app = Application()
app.register_vehicle("BMW 5")
