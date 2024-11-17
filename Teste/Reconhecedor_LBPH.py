import cv2
import os
import sys
from bd.operacoes_funcionario import mostrar_nome_funcionario, obter_funcionario_por_id
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui')))
from ui.main import MainWindow  
from PySide6.QtWidgets import QApplication



detectorFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.LBPHFaceRecognizer.create()
reconhecedor.read("classificadorLBPH.yml")
largura, altura = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture(0)

def abrir_interface(id_funcionario, nome_funcionario, nivel_acesso):
    # Inicializa a aplicação e a janela
    app = QApplication(sys.argv)
    window = MainWindow() 
    camera.release()
    cv2.destroyAllWindows()
    window.show()

    # Funções para serem chamadas na inicialização da interface
    window.atualizar_dados(id_funcionario, nome_funcionario, nivel_acesso)
    window.definir_permissoes()
    window.configurar_combobox_nivel()

    # Inicia o loop da aplicação
    app.exec()

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale (imagemCinza, scaleFactor=1.5, minSize=(30,30))

    for (x, y, l, a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
        cv2.rectangle(imagem, (x,y), (x + l, y + a), (0, 0, 255), 2)
        id, confianca = reconhecedor.predict(imagemFace)
        nome_tuple = mostrar_nome_funcionario(id)
        nome = nome_tuple[0] if nome_tuple else "Desconhecido"

        cv2.putText(imagem, nome, (x, y + (a + 30)), font, 2, (0,0,255))
        cv2.putText(imagem, str(confianca), (x, y + (a + 50)), font, 1, (0,0,255))

    cv2.imshow("Face", imagem)

    if id != -1:
        resultado = obter_funcionario_por_id(id)
        if resultado:
            id_funcionario, nome_funcionario, nivel_acesso = resultado
            abrir_interface(id_funcionario, nome_funcionario, nivel_acesso)  # Passa os dados fo funfionário autenticado para a interface

            

    if cv2.waitKey(1) == ord ("q"):
        break

