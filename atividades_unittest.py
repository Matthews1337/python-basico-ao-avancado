def comer(comida, eh_saudavel):
    
    if eh_saudavel:
        motivo ='quero manter a forma'
    else:
        motivo ='a gente vive uma vez'

    return f"Estou comendo {comida} porque {motivo}"

def dormir(num_horas):
    if num_horas > 8:
        return f"Ptz dormi {num_horas} horas, estou atrasado"
    else:
        return f"Continuo cansado após dormir por {num_horas} horas"
        