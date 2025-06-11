import pandas as pd

def main():
    # Ler o arquivo CSV
    df = pd.read_csv('AIRPOL_data.csv', sep=';')

    # Agrupar os dados por país
    for country in df['Country'].unique():
        # Filtrar os dados para o país atual
        country_data = df[df['Country'] == country]

        # Criar o nome do arquivo de saída
        output_filename = f'AIRPOL_data_{country}.csv'

        # Salvar os dados do país num novo arquivo CSV
        country_data.to_csv(output_filename, sep=';', index=False)

        print(f'Arquivo criado: {output_filename}')


if __name__ == '__main__':
    main()


