import calendar
from datetime import datetime

class MyCalendar():

    def count_weekday_in_year(self,year,weekday):
        c = calendar.Calendar(calendar.SUNDAY)
        self.__cont = 1
        self.__result = 0
        while self.__cont <= 12:
            for x in c.monthdays2calendar(year,self.__cont):
                for y in x:
                    if y[0] != 0 and y[1] == weekday:
                        self.__result+=1
            self.__cont+=1
        return self.__result

a = MyCalendar()


try:
    ano = int(input("Informe o ano no qual deseja ser contado: "))
    while ano < 1 or ano > 9999:
        ano = int(input("Informe o ano entre(1 até 9999): "))
    dia = int(input("Informe o dia (0)segunda, (6)domingo: "))
    while dia < 1 or dia > 6:
        dia = int(input("Informe um valor que esteja nos dias da semana: "))

    a = MyCalendar()
    b = datetime(1,1,dia+1)
    print("A quantidade de vezes que o dia:",datetime.strftime(b,"%A"),"Repetiu, foi de:",
          a.count_weekday_in_year(ano,dia),"vezes.")

except ValueError:
    print("Você informou um valor fora do padrão solicitado, tente novamente.")




