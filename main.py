from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import streamlit as st
import io

# palavras sobrepor imagem







def cria_assinatura(nome_funcionario,cargo,telefone,ramal):
    cor = "black"
    #abrir imagem
    imagem = Image.open('ass-modelo.PNG')
    #abrir para sobreposição
    draw = ImageDraw.Draw(imagem)
    # setar qual a fonte usar e tamanho
    fonte_negrito = ImageFont.truetype('GOTHICb.TTF', 15)
    fonte_padrao = ImageFont.truetype('GOTHIC.TTF', 13)
    # sobrepor texto na imagem
    draw.text((197,9),nome_funcionario,fill=cor,font=fonte_negrito)
    draw.text((197,28),cargo,fill=cor,font=fonte_padrao)
    draw.text((197,45),telefone,fill=cor,font=fonte_padrao)
    draw.text((378,45),ramal,fill=cor,font=fonte_padrao)
    # salvar imagem
    #imagem.save(f'{nome_funcionario}.PNG')
    #imagem.show()
    st.image([imagem]) # Exibe a imagem na tela
    return imagem




def main_loop():

    nome_funcionario = st.sidebar.text_input("Nome do colaborador",)
    cargo = st.sidebar.text_input("Cargo do colaborador",)
    telefone = "+55 (11) 2490 - 2000 – Ramal"
    ramal = st.sidebar.text_input("Ramal",)
    imagem = cria_assinatura(nome_funcionario,cargo,telefone,ramal)
    
    
    # # Convertendo a imagem para bytes
    img_bytes = io.BytesIO()
    imagem.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    # # Botão de download
    st.download_button(
        label="Baixar imagem",
        data=img_bytes,
        file_name=nome_funcionario +".png",
        mime="image/png"
    )
# with open("flower.png", "rb") as file:
#     btn = st.download_button(
#             label="Download image",
#             data=file,
#             file_name="flower.png",
#             mime="image/png"
#           )
    
if __name__ == '__main__':
    main_loop()    