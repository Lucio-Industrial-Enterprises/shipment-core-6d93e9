"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Parse a non-negative integer quantity, allowing surrounding whitespace."""
    quantity = int(value.strip())
    if quantity < 0:
        raise ValueError("quantity must be non-negative")
    return quantity
