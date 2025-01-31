import os
import shutil
import random
import sys
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import Qt
from ui.newmainui import Ui_Dialog  # Importando a UI atualizada

class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura a UI

        # Aplicando tema escuro
        self.set_dark_theme()

        # Inicializa a barra de progresso
        self.progressBar.setValue(0)

        # Configuração do slider (valores entre 50 e 90)
        self.horizontalSlider.setMinimum(50)
        self.horizontalSlider.setMaximum(90)
        self.horizontalSlider.setValue(70)  # Valor inicial padrão: 70%
        self.horizontalSlider.setTickPosition(self.horizontalSlider.TickPosition.TicksBelow)
        self.horizontalSlider.setTickInterval(5)

        # Criar um label para exibir o valor do slider dinamicamente
        self.slider_value_label = self.label_5  # Usa a label existente
        self.slider_value_label.setText(f"Random %: {self.horizontalSlider.value()}")

        # Conectar o slider a uma função para atualizar o valor dinamicamente
        self.horizontalSlider.valueChanged.connect(self.atualizar_slider_label)

        # Conectar botões aos métodos
        self.buttonBox.accepted.connect(self.processar_arquivos)
        self.buttonBox.rejected.connect(self.fechar_janela)

    def atualizar_slider_label(self):
        """ Atualiza dinamicamente o valor do slider na UI. """
        self.slider_value_label.setText(f"Random %: {self.horizontalSlider.value()}")

    def processar_arquivos(self):
        """
        Obtém os caminhos dos diretórios e a porcentagem de divisão de treino/validação.
        """
        diretorio_imagens = self.imageInput.text()
        diretorio_labels = self.labelInput.text()
        diretorio_saida = self.outInput.text()
        split = self.horizontalSlider.value() / 100  # Converte para um valor entre 0.5 e 0.9

        if not diretorio_imagens or not diretorio_labels or not diretorio_saida:
            print("Preencha todos os campos antes de continuar!")
            return

        try:
            self.progressBar.setValue(10)  # Inicia a barra em 10%
            criar_estrutura_yolo(diretorio_saida)
            self.progressBar.setValue(30)  # Atualiza para 30%
            self.transferir_arquivos(diretorio_imagens, diretorio_labels, diretorio_saida, split)
            self.progressBar.setValue(100)  # Finaliza em 100%
            print("Processo concluído com sucesso!")
        except Exception as e:
            print(f"Erro ao processar arquivos: {e}")
            self.progressBar.setValue(0)  # Resetar em caso de erro

    def transferir_arquivos(self, diretorio_origem_imagens, diretorio_origem_labels, diretorio_destino, split):
        """
        Transfere as imagens e rótulos para a estrutura YOLO, separando em treino e validação
        de acordo com a porcentagem definida pelo usuário.
        """
        if not os.path.exists(diretorio_origem_imagens):
            raise FileNotFoundError(f"Diretório de imagens não encontrado: {diretorio_origem_imagens}")
        
        if not os.path.exists(diretorio_origem_labels):
            raise FileNotFoundError(f"Diretório de labels não encontrado: {diretorio_origem_labels}")

        imagens = [img for img in os.listdir(diretorio_origem_imagens) if img.lower().endswith(('.jpg', '.png'))]

        if not imagens:
            raise ValueError("Nenhuma imagem encontrada no diretório de origem!")

        random.seed(42)  # Mantém a reprodutibilidade
        random.shuffle(imagens)

        total_imagens = len(imagens)
        num_train = int(split * total_imagens)  # Ajusta a divisão conforme o usuário

        imagens_train = imagens[:num_train]
        imagens_val = imagens[num_train:]

        total_processos = len(imagens_train) + len(imagens_val)
        progresso_atual = 30  # Inicia em 30%
        incremento = 70 / total_processos  # Divide os 70% restantes

        def copiar_arquivos(imagens_lista, tipo):
            nonlocal progresso_atual  # Permite modificar a variável externa
            for img in imagens_lista:
                nome_base, _ = os.path.splitext(img)

                caminho_imagem = os.path.join(diretorio_origem_imagens, img)
                caminho_destino_imagem = os.path.join(diretorio_destino, 'images', tipo, img)
                shutil.copy2(caminho_imagem, caminho_destino_imagem)

                caminho_label = os.path.join(diretorio_origem_labels, f"{nome_base}.txt")
                if os.path.exists(caminho_label):
                    caminho_destino_label = os.path.join(diretorio_destino, 'labels', tipo, f"{nome_base}.txt")
                    shutil.copy2(caminho_label, caminho_destino_label)

                progresso_atual += incremento
                self.progressBar.setValue(int(progresso_atual))  # Atualiza a barra de progresso

        copiar_arquivos(imagens_train, 'train')
        copiar_arquivos(imagens_val, 'val')

    def fechar_janela(self):
        """ Fecha a janela quando o botão 'Cancelar' é pressionado """
        self.close()

    def set_dark_theme(self):
        """ Aplica um tema escuro no PySide6. """
        dark_style = """
        QWidget {
            background-color: #282a36;
            color: #f8f8f2;
            font-size: 12pt;
        }
        QLabel {
            color: #ff79c6;
            font-size: 11pt;
        }
        QLineEdit {
            background-color: #44475a;
            border: 1px solid #6272a4;
            padding: 5px;
            color: #f8f8f2;
            border-radius: 5px;
        }
        QSlider::groove:horizontal {
            border: 1px solid #ff79c6;
            height: 5px;
            background: #44475a;
        }
        QSlider::handle:horizontal {
            background: #ff79c6;
            border: 1px solid #ff79c6;
            width: 15px;
            margin: -5px 0;
            border-radius: 7px;
        }
        QDialogButtonBox QPushButton {
            background-color: #50fa7b;
            border-radius: 5px;
            padding: 6px;
            color: #282a36;
            font-weight: bold;
        }
        QProgressBar {
            border: 1px solid #ff79c6;
            text-align: center;
            background: #44475a;
            color: #f8f8f2;
        }
        QProgressBar::chunk {
            background-color: #50fa7b;
        }
        """
        self.setStyleSheet(dark_style)


def criar_estrutura_yolo(diretorio_base):
    """
    Cria a estrutura de diretórios para o treinamento do YOLO.
    """
    diretorios = [
        os.path.join(diretorio_base, 'images', 'train'),
        os.path.join(diretorio_base, 'images', 'val'),
        os.path.join(diretorio_base, 'labels', 'train'),
        os.path.join(diretorio_base, 'labels', 'val')
    ]

    for diretorio in diretorios:
        os.makedirs(diretorio, exist_ok=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
