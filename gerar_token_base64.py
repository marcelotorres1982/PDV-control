import base64
import os

# Caminho do token.pickle
token_path = os.path.join('credentials', 'token.pickle')

# Verifica se o arquivo existe
if not os.path.exists(token_path):
    print(f"❌ Arquivo não encontrado: {token_path}")
    print(f"📁 Diretório atual: {os.getcwd()}")
    print(f"📂 Arquivos em credentials/:")
    if os.path.exists('credentials'):
        for file in os.listdir('credentials'):
            print(f"   - {file}")
    exit(1)

# Lê o arquivo binário
print(f"📖 Lendo {token_path}...")
with open(token_path, 'rb') as f:
    token_bytes = f.read()

# Converte para Base64
print("🔄 Convertendo para Base64...")
token_b64 = base64.b64encode(token_bytes).decode('utf-8')

# Salva em arquivo
output_path = 'token_base64.txt'
with open(output_path, 'w') as f:
    f.write(token_b64)

print(f"✅ Token Base64 gerado com sucesso!")
print(f"📄 Arquivo salvo em: {output_path}")
print(f"📏 Tamanho: {len(token_b64)} caracteres")
print(f"\n📋 Primeiros 100 caracteres:")
print(token_b64[:100] + "...")
print(f"\n🎯 COPIE TODO O CONTEÚDO de '{output_path}' para o Streamlit Secrets")