# coding: utf-8
# aluno:Genilson Mess
# prof: habib  
# usando funcoes
# comentada as ultimas linhas estava aprendendo a reportar a data atual do sistema :)
  

def converter_para_segundos(dias, horas, minutos, segundos):
   dias_segundo = dias * 24 * 60 * 60
   horas_segundo = horas * 60 * 60
   minutos_segundo = minutos * 60     
   return dias_segundo + horas_segundo + minutos_segundo + segundos
        
def converter_para_dias(total_segundos):
    total_minutos, segundos = divmod(total_segundos, 60)
    total_horas, minutos = divmod(total_minutos, 60)
    dias, horas = divmod(total_horas, 24)    
    return dias, horas, minutos, segundos
   
print ("digite os valores abaixo")
dd = input ("...quantidade de dias: ")
hr = input ("... quantidade de horas: ")
mn = input ("... quantidade minutos: ")
ss = input ("... quantidade de segundos: ")
print ("entre com outros valores para fazer o cauculo em dias hrs e minutos")
dds = input (" quantidade de dias: ")
hrs = input ("... quantidade de horas: ")
mns = input ("... quantidade de  minutos: ")
sss = input ("... quantidade de segundos: ")
    
data_1 = converter_para_segundos(dd, hr, mn, ss)
data_2 = converter_para_segundos(dds, hrs, mns, sss)
resultado = converter_para_dias(data_1 + data_2)
print ("%s Dias, %s Horas, %s Minutos, %s Segundos") % resultado

#from date.time import date
#hj = date.today()
#print ("data do seu sistema e:") hj
