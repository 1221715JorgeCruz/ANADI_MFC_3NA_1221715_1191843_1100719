import pandas as pd

def main():

    # Carregar o dataset
    df = pd.read_csv('AIRPOL_data.csv', sep=';', decimal=',')

    # Listar países únicos
    print("Países disponíveis no dataset:")
    print(df['Country'].unique())

    # Filtrar para Southern Europe
    southern_europe = ['Greece', 'Spain', 'Italy', 'Portugal']
    df_south = df[df['Country'].isin(southern_europe)].rename(columns={'Value': 'Premature_Deaths'})

    # Verificar o tamanho do DataFrame filtrado
    print(f"\nNúmero de linhas após filtragem para Southern Europe: {len(df_south)}")
    if len(df_south) == 0:
        print("Erro: Nenhum dado encontrado para os países especificados. Verifique os nomes dos países.")
    else:
        print("Primeiras linhas do DataFrame filtrado:")
        print(df_south.head())


if __name__ == '__main__':
    main()