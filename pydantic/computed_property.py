from pydantic import BaseModel, computed_field


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity

product1 = Product(price=19.99, quantity=3)

print(product1.model_dump())