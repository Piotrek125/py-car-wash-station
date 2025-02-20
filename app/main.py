class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car: list[Car]) -> float:
        income = 0.0
        for vehicle in Car:
            if self.clean_power > self.clean_rate:
                income += self.calculate_washing_price(car)


    def calculate_washing_price(self, car: Car) -> float:
        price = (self.comfort_class * (self.clean_power - self.clean_mark) *
                (self.average_rating / self.distance_from_city_center))
        return round(price, 1)

    def wash_single_car(self, car:Car) -> None:
        if  self.clean_power > self.clean_mark:
            self.clean_power = self.clean_mark

    def rate_service( self, single_rating: int) -> None:
        self.count_of_ratings += 1
        overall_rating = self.count_of_ratings * self.average_rating
        self.average_rating = overall_rating / self.count_of_ratings
