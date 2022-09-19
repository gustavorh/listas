# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:09:26 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

n = int(input("¿Cuántos números desea ingresar?: "))

lista = []
for n_actuales in range(n):
    num = int(input(f"Ingrese el número {n_actuales+1} de la lista: "))
    lista.append(num)
