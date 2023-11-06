# Zadanie 2

def calculate_density(mass, volume, unit_mass='kg', unit_volume='m^3'):
    """
    Oblicza gęstość materiału dla zadanej masy i objętości.
    
    Umożliwia konwersję między jednostkami masy (kg, g) i objętości (m^3, cm^3).
    Zwraca gęstość w jednostkach kg/m^3.
    
    Parameters:
    mass : float
        Masa materiału, domyślnie w kilogramach.
    volume : float
        Objętość materiału, domyślnie w metrach sześciennych.
    unit_mass : str, optional
        Jednostka masy, domyślnie 'kg', opcjonalnie 'g'.
    unit_volume : str, optional
        Jednostka objętości, domyślnie 'm^3', opcjonalnie 'cm^3'.

    Returns:
    float
        Gęstość materiału w kg/m^3

    Raises:
    NotImplementedError
        Jeśli jednostki masy lub objętości nie są obsługiwane.
    ValueError
        Jeśli podana objętość jest równa zero, uniemożliwiając obliczenie gęstości.

    Przykład użycia:
    >>> calculate_density(1000, 1e6, 'g', 'cm^3')
    1.0  # wynik w kg/m^3
    """
    pass
