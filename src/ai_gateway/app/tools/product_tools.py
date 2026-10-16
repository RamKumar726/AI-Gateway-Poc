
from langchain.tools import tool


PRODUCTS = [
    {
        "id": "P101",
        "name": "Cotton T-Shirt",
        "category": "clothing",
        "price": 599,
    },
    {
        "id": "P102",
        "name": "Casual Sneakers",
        "category": "footwear",
        "price": 1499,
    },
]


@tool
def search_products(query: str) -> list[dict]:
    """Search products by name or category."""
    query = query.lower().strip()

    return [
        product
        for product in PRODUCTS
        if query in product["name"].lower()
        or query in product["category"].lower()
    ]


@tool
def get_product_details(product_id: str) -> dict:
    """Get product details using its ID."""
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product

    return {"error": "Product not found"}
