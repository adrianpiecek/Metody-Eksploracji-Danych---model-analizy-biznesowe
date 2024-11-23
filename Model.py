import numpy as np
import pandas as pd
import altair as alt

def read_data_users(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    #co trzecia linijka licząć od pierwszej to pierwszy wymiar (string), co trzecia linijka licząc od drugiej to drugi wymiar to liczba użytkowników (int)
    first_dimension = [lines[i].strip() for i in range(0, len(lines), 3)]   # rok i kwartal
    second_dimension = [int(lines[i].strip()) for i in range(1, len(lines), 3)] # liczba użytkowników

    #return pd.DataFrame(second_dimension, index=first_dimension, columns=['Liczba użytkowników'])
    return np.array(first_dimension), np.array(second_dimension)
    

def read_data_finanse_pracownicy(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # pierwsza liczba każdego wiersza to pierwszy wymiar, reszta to drugi wymiar
    first_dimension = [lines[i].strip().split()[0] for i in range(0, len(lines))] # rok
    second_dimension = [list(map(float, lines[i].strip().split()[1:])) for i in range(0, len(lines))] # przychod zysk zatrudnienie
    return np.array(first_dimension), np.array(second_dimension)
    #return pd.DataFrame(second_dimension, index=first_dimension, columns=['Przychód', 'Zysk', 'Zatrudnienie'])

# Example usage
users_path = './Uzytkownicy.txt'
users_first_dim, users_second_dim = read_data_users(users_path)

finance_path = './Finanse_Pracownicy.txt'
finance_first_dim, finance_second_dim = read_data_finanse_pracownicy(finance_path)
'''
print("UZYTKOWNICY\nkwartał i rok:", users_first_dim)
print("\nliczba uzytkownikow:\n", users_second_dim)

print("\nFINANSE I PRACOWNICY\nrok:", finance_first_dim)
print("\nprzychod, zysk, zatrudnienie:\n", finance_second_dim)
'''
pd.DataFrame(users_second_dim, index=users_first_dim, columns=['Liczba użytkowników'])
pd.DataFrame(finance_second_dim, index=finance_first_dim, columns=['Przychód', 'Zysk', 'Zatrudnienie'])

users_chart = alt.Chart(pd.DataFrame(users_second_dim, index=users_first_dim, columns=['Liczba użytkowników']))
finance_chart = alt.Chart(pd.DataFrame(finance_second_dim, index=finance_first_dim, columns=['Przychód', 'Zysk', 'Zatrudnienie']))

users_chart.mark_line().encode(x=alt.X(users_first_dim, type='ordinal'), y='Liczba użytkowników')
#prezentacja danych finansowych
finance_chart.mark_line().encode(x=alt.X(finance_first_dim, type='ordinal'), y='Przychód')
finance_chart.mark_line().encode(x=alt.X(finance_first_dim, type='ordinal'), y='Zysk')
finance_chart.mark_line().encode(x=alt.X(finance_first_dim, type='ordinal'), y='Zatrudnienie')
#wyświetlanie
users_chart
finance_chart
