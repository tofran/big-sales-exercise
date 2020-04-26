import string
from time import time

CLIENTS_FILENAME = "data/clients.txt"
SALES_FILENAME = "data/sales.txt"
PRODUCTS_FILENAME = "data/products.txt"


def is_id_valid(client_id, number_of_chars=1):
    number = int(client_id[number_of_chars:])

    return (
        all(
            char in string.ascii_uppercase
            for char in client_id[number_of_chars-1]
        )
        and number >= 1000
        and number <= 9999
    )


def get_valid_sales(produtos, clientes):
    with open(SALES_FILENAME) as f:
        for line in f:
            produto, preco, unidades, is_promo, cliente, mes, filial = line.strip().split(" ")

            if (
                produto in produtos
                and cliente in clientes
            ):
                yield line


def get_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()


def count_valid_products():
    clients = set(
        client_id
        for client_id in get_lines(CLIENTS_FILENAME)
        if is_id_valid(client_id)
    )

    products = set(
        product_id
        for product_id in get_lines(PRODUCTS_FILENAME)
        if is_id_valid(product_id, 2)
    )

    return sum(
        1 for sale in get_valid_sales(products, clients)
    )


def main():
    assert is_id_valid("F9999")
    assert not is_id_valid("F0001")
    assert not is_id_valid("f1001")
    assert is_id_valid("FF9999", 2)
    assert not is_id_valid("FF0111", 2)
    assert not is_id_valid("F00111", 2)

    time_before = time()
    print(count_valid_products())
    print("Took {}".format(time() - time_before))


if __name__ == "__main__":
    main()
