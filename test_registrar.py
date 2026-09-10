from votacion import registrar_voto, votos, votantes

registrar_voto("cedula123", "Candidato A")
registrar_voto("cedula123", "Candidato B")  # debe rechazar
registrar_voto("cedula456", "Candidato A")

print(votos)
print(votantes)