"""
Crea una función que ordene y retorne una matriz de números.
- La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
  adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
  o de mayor a menor.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan
  automáticamente.
"""


def order_list(numbers: list, mode: str = "Asc") -> list:
    nums = numbers[:]

    if mode == "Asc":
        for n in range(len(nums)):
            swapped = False
            for j in range(0, len(nums)-n-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                return nums
    elif mode == "Desc":
        for n in range(len(nums)):
            swapped = False
            for j in range(0, len(nums)-n-1):
                if nums[j] < nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                return nums
    else:
        raise ValueError("Mode must be 'Acs' or 'Desc'")


print(order_list([3, 6, 4, 7, 9, 1, 5]))
print(order_list([3, 6, 4, 7, 9, 1, 5], mode="Desc"))
print(order_list([3, 6, 4, 7, 9, 1, 5], mode="Sort"))
