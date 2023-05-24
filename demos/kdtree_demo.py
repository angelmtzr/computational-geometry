from random import randint, seed


def build_tree(*, dim, data, ndims):
    if len(data) == 1:
        return data
    datos_s = sorted(data, key=lambda x: x[dim])
    mediana = (len(datos_s) - 1) // 2
    datos_izq = datos_s[:mediana + 1]
    datos_der = datos_s[mediana + 1:]
    return (datos_s[mediana],
            build_tree(dim=(dim + 1) % ndims, data=datos_izq, ndims=ndims),
            build_tree(dim=(dim + 1) % ndims, data=datos_der, ndims=ndims)
            )


def range_search(kdtree, dim, rango, ndims):
    inf, sup = rango[dim]
    punto = kdtree[0]
    if len(kdtree) == 1:
        for i in range(ndims):
            inf, sup = rango[i]
            if inf > punto[i] or sup < punto[i]:
                break
        else:
            return kdtree[0]
        return
    if inf <= punto[dim]:
        return range_search(kdtree[1], (dim + 1) % ndims, rango, ndims)
    if sup >= punto[dim]:
        return range_search(kdtree[2], (dim + 1) % ndims, rango, ndims)


def kdtree_demo():
    seed(50771708)
    data = [(randint(0, 200), randint(0, 200), randint(0, 200))
            for _ in range(100)]
    kdtree = build_tree(dim=0, data=data, ndims=3)
    rango = ((0, 100), (80, 135), (120, 180))
    print(range_search(kdtree, 0, rango, 3))


if __name__ == '__main__':
    kdtree_demo()
