from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}

#=========================================================================================#

url = "https://owasp.org/www-community/attacks/xss/"

#=========================================================================================#

output_file = "codigos PHP.txt"  # Nome do arquivo de saída

try:
    page = requests.get(url, headers=headers)
    page.raise_for_status()
    
    soup = BeautifulSoup(page.content, 'html.parser')
    code_blocks = soup.find_all('div', class_='highlight')

    # Abrir o arquivo para escrita
    with open(output_file, 'a', encoding='utf-8') as file:
        for block in code_blocks:
            code = block.find('code').get_text(strip=False)
            file.write(code.strip() + "\n")  # Escreve o código
            file.write("\n" + "-"*50 + "\n\n")  # Separador

    print(f"Exemplos salvos em: {output_file}")

except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
except IOError as e:
    print(f"Erro ao escrever no arquivo: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")