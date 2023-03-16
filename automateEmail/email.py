import pyautogui  # pip install pyautogui --user
import time

pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está rodando");
pyautogui.PAUSE = 0.5
#Abrir o google no meu 

pyautogui.press("winleft");
#pyautogui.hotkey("winleft", "r");
pyautogui.write("chrome");
pyautogui.press("enter");
time.sleep(1);
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter");


#clicar no escrever
pyautogui.moveTo(33, 163);
time.sleep(2);
pyautogui.click();
pyautogui.write("ricardoorri@gmail.com")
pyautogui.moveTo(1462, 534);
pyautogui.click();


#clicar no item abaixo
pyautogui.moveTo(1335, 554);
time.sleep(1);
pyautogui.click();
pyautogui.write("Ass: Michael")


pyautogui.moveTo(1311, 660);
time.sleep(1);
pyautogui.click();
pyautogui.write("Este e um email automatico direto do curso de Python");




pyautogui.moveTo(1305, 1003);
time.sleep(1);
Ass:pyautogui.click();




#enquanto arrasto, altero a janela para o google drive
#pyautogui.hotkey("alt" , "tab");
#time.sleep(1);
#soltar o arquivo no google drive
#pyautogui.mouseUp();

#
# pyautogui.hotkey("alt" , "tab");esperar 5 segundos
time.sleep(5);

pyautogui.alert("O código acabou de rodar. Pode usar o computador novamente");