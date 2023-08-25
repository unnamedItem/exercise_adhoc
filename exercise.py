lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25),
]


def ordenar(lista_personas):
    """ El metodo debe devolver una lista con las edades ordenadas de menor a mayor"""
    return list(sorted(map(lambda person: person[3], lista_personas), reverse=False))


def convertir_a_diccionario(lista_personas):
    """ Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad """
    return dict(map(lambda person: (person[0], (person[1], person[2], person[3])), lista_personas))


def devolver_edad(lista_personas, dni):
    """ Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido.
    Tip: intentar usar el método convertir_a_diccionario"""
    person_by_dni = convertir_a_diccionario(lista_personas)
    return person_by_dni[dni][2]


def eliminar_repetidos(lista_personas):
    """ El metodo debe devolver los elementos unicos """
    reduced_list = []
    for person in lista_personas:
        dni = person[0]
        is_already_in = dni in list(map(lambda person: person[0], reduced_list))
        if not is_already_in:
            reduced_list.append(person)
    return reduced_list


def separar_por_edad(lista_personas):
    """ Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
    """
    older = [person for person in lista_personas if person[3] >= 25]
    younger = [person for person in lista_personas if person[3] < 25]
    return older, younger


def obtener_promedio(lista):
    """ Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
    def handle_division_by_zero(a, b):
        try:
            return a / b
        except:
            return 0
    return handle_division_by_zero(sum(lista), len(lista))

def main():
    """ Este metodo no debe modificarse y es solo a fines de probar el codigo """
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' %
          convertir_a_diccionario(lista_personas))
    print(' * La edad para dni 55555555 es: %s\n' %
          devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' %
          separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' %
          separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' %
          obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))


main()
