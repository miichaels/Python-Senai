import pyautogui  # pip install pyautogui --user
import time

pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está rodando");
pyautogui.PAUSE = 0.5
#Abrir o google no meu 

#pyautogui.press("winleft");
pyautogui.hotkey("winleft", "r");
pyautogui.write("chrome");
pyautogui.press("enter");
time.sleep(1);
pyautogui.write("https://drive.google.com/drive/folders/161uXKUOPWr1LCWgTfl0d_SvEIE3Ufm9l")
pyautogui.press("enter");

#entrar na área de trabalho
pyautogui.hotkey("winleft" , "d")
#clicar no arquivo que quero fazer backup e arraster
pyautogui.moveTo(872, 107);
pyautogui.mouseDown();
pyautogui.moveTo(694, 441);

#enquanto arrasto, altero a janela para o google drive
pyautogui.hotkey("alt" , "tab");
time.sleep(1);
#soltar o arquivo no google drive
pyautogui.mouseUp();

#esperar 5 segundos
time.sleep(5);

pyautogui.alert("O código acabou de rodar. Pode usar o computador novamente");

