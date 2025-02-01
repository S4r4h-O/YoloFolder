import os
import shutil
import random
import sys
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from ui.mainui import Ui_Dialog  # Importando a UI atualizada

class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura a UI

        # Aplicando tema escuro (Visual Studio Code)
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

        # Conectar botões de seleção de diretório
        self.dirButton1.clicked.connect(lambda: self.abrir_diretorio(self.imageInput))
        self.dirButton2.clicked.connect(lambda: self.abrir_diretorio(self.labelInput))
        self.dirButton3.clicked.connect(lambda: self.abrir_diretorio(self.outInput))

        # Conectar botões aos métodos
        self.buttonBox.accepted.disconnect()  # Remove a conexão padrão
        self.buttonBox.accepted.connect(self.processar_arquivos)
        self.buttonBox.rejected.connect(self.fechar_janela)

    def set_dark_theme(self):
        """ Aplica um tema escuro no PySide6 inspirado no Visual Studio Code. """
        dark_style = """
        QWidget { background-color: #1e1e1e; color: #d4d4d4; font-size: 12pt; }
        QLabel { color: #569cd6; font-size: 11pt; }
        QLineEdit { background-color: #252526; border: 1px solid #3e3e42; padding: 5px; color: #d4d4d4; border-radius: 5px; }
        QToolButton { background-color: #007acc; border-radius: 5px; padding: 6px; color: white; font-weight: bold; }
        QProgressBar { border: 1px solid #007acc; text-align: center; background: #252526; color: #d4d4d4; }
        QProgressBar::chunk { background-color: #569cd6; }
        QDialogButtonBox QPushButton { background-color: #007acc; border-radius: 5px; padding: 6px; color: white; font-weight: bold; }
        """
        self.setStyleSheet(dark_style)

    def abrir_diretorio(self, line_edit):
        """ Abre o explorador de arquivos para selecionar um diretório e insere o caminho no campo correspondente. """
        caminho = QFileDialog.getExistingDirectory(self, "Selecione um diretório")
        if caminho:
            line_edit.setText(caminho)

    def atualizar_slider_label(self):
        """ Atualiza dinamicamente o valor do slider na UI. """
        self.slider_value_label.setText(f"Random %: {self.horizontalSlider.value()}")

    def processar_arquivos(self):
        """ Obtém os caminhos dos diretórios e a porcentagem de divisão de treino/validação. """
        diretorio_imagens = self.imageInput.text()
        diretorio_labels = self.labelInput.text()
        diretorio_saida = self.outInput.text()
        split = self.horizontalSlider.value() / 100  # Converte para um valor entre 0.5 e 0.9

        if not diretorio_imagens or not diretorio_labels or not diretorio_saida:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos antes de continuar!")
            return

        try:
            self.progressBar.setValue(10)  # Inicia a barra em 10%
            criar_estrutura_yolo(diretorio_saida)
            self.progressBar.setValue(30)  # Atualiza para 30%
            self.transferir_arquivos(diretorio_imagens, diretorio_labels, diretorio_saida, split)
            self.progressBar.setValue(100)  # Finaliza em 100%
            QMessageBox.information(self, "Sucesso", "Processo concluído com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao processar arquivos: {e}")
            self.progressBar.setValue(0)  # Resetar em caso de erro

    def transferir_arquivos(self, diretorio_origem_imagens, diretorio_origem_labels, diretorio_destino, split):
        """ Transfere as imagens e rótulos para a estrutura YOLO, separando em treino e validação. """
        if not os.path.exists(diretorio_origem_imagens):
            raise FileNotFoundError(f"Diretório de imagens não encontrado: {diretorio_origem_imagens}")
        
        if not os.path.exists(diretorio_origem_labels):
            raise FileNotFoundError(f"Diretório de labels não encontrado: {diretorio_origem_labels}")

        imagens = [img for img in os.listdir(diretorio_origem_imagens) if img.lower().endswith(('.jpg', '.png'))]

        if not imagens:
            raise ValueError("Nenhuma imagem encontrada no diretório de origem!")

        random.seed(42)  # Mantém a reprodutibilidade
        random.shuffle(imagens)

        num_train = int(split * len(imagens))
        imagens_train = imagens[:num_train]
        imagens_val = imagens[num_train:]

        for img in imagens_train:
            nome_base, _ = os.path.splitext(img)
            shutil.copy2(os.path.join(diretorio_origem_imagens, img), os.path.join(diretorio_destino, 'images/train', img))
            if os.path.exists(os.path.join(diretorio_origem_labels, f"{nome_base}.txt")):
                shutil.copy2(os.path.join(diretorio_origem_labels, f"{nome_base}.txt"), os.path.join(diretorio_destino, 'labels/train', f"{nome_base}.txt"))

        for img in imagens_val:
            nome_base, _ = os.path.splitext(img)
            shutil.copy2(os.path.join(diretorio_origem_imagens, img), os.path.join(diretorio_destino, 'images/val', img))
            if os.path.exists(os.path.join(diretorio_origem_labels, f"{nome_base}.txt")):
                shutil.copy2(os.path.join(diretorio_origem_labels, f"{nome_base}.txt"), os.path.join(diretorio_destino, 'labels/val', f"{nome_base}.txt"))

    def fechar_janela(self):
        """ Fecha a janela quando o botão 'Cancelar' é pressionado. """
        self.close()

def criar_estrutura_yolo(diretorio_base):
    """ Cria a estrutura de diretórios para o YOLO. """
    for d in ['images/train', 'images/val', 'labels/train', 'labels/val']:
        os.makedirs(os.path.join(diretorio_base, d), exist_ok=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
