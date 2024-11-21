import numpy as np
import pandas as pd
import altair as alt

def read_data_users(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    first_dimension = [lines[i].strip() for i in range(0, len(lines), 3)] # kwartał i rok
    second_dimension = [float(lines[i].strip()) for i in range(1, len(lines), 3)] # liczba użytkowników
    
    return np.array(first_dimension), np.array(second_dimension)

def read_data_finanse_pracownicy(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # pierwsza liczba każdego wiersza to pierwszy wymiar, reszta to drugi wymiar
    first_dimension = [lines[i].strip().split()[0] for i in range(0, len(lines))] # rok
    second_dimension = [list(map(float, lines[i].strip().split()[1:])) for i in range(0, len(lines))] # przychod zysk zatrudnienie
    return np.array(first_dimension), np.array(second_dimension)

# Example usage
users_path = './Uzytkownicy.txt'
users_first_dim, users_second_dim = read_data_users(users_path)

finance_path = './Finanse_Pracownicy.txt'
finance_first_dim, finance_second_dim = read_data_finanse_pracownicy(finance_path)

print("UZYTKOWNICY\nkwartał i rok:", users_first_dim)
print("\nliczba uzytkownikow:\n", users_second_dim)

print("\nFINANSE I PRACOWNICY\nrok:", finance_first_dim)
print("\nprzychod, zysk, zatrudnienie:\n", finance_second_dim)

