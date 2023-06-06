from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import datetime
import functools


#bora pra essa desgraça

gerenciadorDeTelas = ScreenManager()
telaCalendario = Screen(name = 'telaCalendario')
telaEventos = Screen(name = 'telaEventos')
gerenciadorDeTelas.add_widget(telaCalendario)
gerenciadorDeTelas.add_widget(telaEventos)



class TelaPrincipal(BoxLayout):
    pass
    

class Dia():
    def __init__(self, data, mes, diaDaSemana):
        self.dia = data
        self.mes = mes
        self.diaDaSemana = diaDaSemana
        self.evento = ''
    

class Mes():
    def criandoDias(self):
        for i in range(int(self.numDias)):
            self.dias.append(Dia(i+1, self.numMes, ((self.primeiroDia+i-1)%7)))


    def __init__(self, nomeDoMes, numMes, numDias, primeiroDia):
        self.nomeDoMes = nomeDoMes
        self.numMes = numMes
        self.numDias = numDias
        self.primeiroDia = primeiroDia
        self.dias = []
        self.criandoDias()
        
hj = [] 
hj.append(int(str(datetime.date.today())[:4]))
hj.append(int(str(datetime.date.today())[5:7]))
hj.append(int(str(datetime.date.today())[8:]))

meses = [Mes('Janeiro', 1, 31, 1), Mes('Fevereiro', 2, 28, 4), Mes('Março', 3, 31, 4),
         Mes('Abril', 4, 30, 7), Mes('Maio', 5, 31, 2), Mes('Junho', 6, 30, 7),
         Mes('Julho', 7, 31, 7), Mes('Agosto', 8, 31, 7), Mes('Setembro', 9, 30, 7),
         Mes('Outubro', 10, 31, 7), Mes('Novembro', 11, 30, 7), Mes('Dezembro', 12, 31, 7)]

for i in meses:
    if i.numMes == hj[1]:
        mes = i


class ClienteKivyApp(App):
    def trocadorDeTela(self, *args):
        args = args[0]     
        print(args)
        if gerenciadorDeTelas.current == 'telaEventos':
            gerenciadorDeTelas.current = 'telaCalendario'
        else:
            gerenciadorDeTelas.current = 'telaEventos'
    

    def salvaEvento(self):
        self.self.guardaEvento.text

    def build(self):
        t = TelaPrincipal(padding = [50,50,50,50])
        self.calendario = GridLayout(rows= 7, cols = 7)
        self.calendario.add_widget(Button(text = 'D', background_color =(0, 0, 1, 1)))
        self.calendario.add_widget(Button(text = 'S', background_color =(0, 0, 1, 1)))
        self.calendario.add_widget(Button(text = 'T', background_color =(0, 0, 1, 1)))
        self.calendario.add_widget(Button(text = 'Q', background_color =(0, 0, 1, 1)))
        self.calendario.add_widget(Button(text = 'Q', background_color =(0, 0, 1, 1)))
        self.calendario.add_widget(Button(text = 'S', background_color =(0, 0, 1, 1)))
        self.calendario.add_widget(Button(text = 'S', background_color =(0, 0, 1, 1)))

        if mes.primeiroDia != 1:
            for i in range(mes.primeiroDia-1):
                self.calendario.add_widget(BoxLayout())
        for i in range(mes.numDias):
            if mes.numMes == hj[1] and mes.dias[i].dia == hj[2]:
                self.calendario.add_widget(Button(text = str(mes.dias[i].dia), background_color = (0, 1, 0, 1), on_release = functools.partial(self.trocadorDeTela, [i+1, mes.dias[i].evento])))
            elif mes.numMes == hj[1] and mes.dias[i].dia < hj[2]:
                self.calendario.add_widget(Button(text = str(mes.dias[i].dia), background_color = (1, 0, 0, 1), on_release  = functools.partial(self.trocadorDeTela, [i+1, mes.dias[i].evento])))
            else:    
                self.calendario.add_widget(Button(text = str(mes.dias[i].dia), on_release = functools.partial(self.trocadorDeTela, [i+1, mes.dias[i].evento])))
        self.guardaEvento = TextInput()
        telaEventos.add_widget(self.guardaEvento)
        telaEventos.add_widget(Button(text = 'Voltar', on_release = self.trocadorDeTela, size_hint = [0.2, 0.08], pos_hint = {'botton': 0.1, 'x': 0.8}))
        telaEventos.add_widget(Button(text = 'Salvar', on_release = self.trocadorDeTela, size_hint = [0.2, 0.08], pos_hint = {'botton': 0.1, 'x': 0.2}))
        telaCalendario.add_widget(self.calendario)
        t.add_widget(gerenciadorDeTelas)
        return t
    

ClienteKivyApp().run()