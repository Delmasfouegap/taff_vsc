def somma_lista(lista):
    if not isinstance(lista, list):
        raise TypeError("il tipo non è lista ma {}".format(type(lista)))
    
    for i, element in enumerate(lista):
        if not  isinstance(element, int):
            raise TypeError("l'elemento {} non sono compatibile ai tipi ma piutosto : {}".format(type(i), type(element)))
        
    somma = 0
    for i in lista:
        somma += i
    return somma

mia_lista = [102,50,3,13]
result = somma_lista(mia_lista)
print(result)


 

#CONTROLO DEGLI IN PUT

Sesso = input("unserire il sesso !")
if Sesso.upper() not in ["M", "F"]:
    raise TypeError("il sesso deve essere sia Maschile (M) or Feminile (F)")
print("Bene ! informzione salvato: sesso = {} ".format(Sesso))






#----------------PRIMO COMPITO LAB-PROGRAMMAZIONE

#la class per stampare tutti gli elementi su una forma di lista di liste: 

##&& gestione degli input et eccezione:

class ExamEception(Exception):
    pass


class CSVTimesSeriesFiles:
    def __init__(self,my_files):
        self.name = my_files
        try:
            files = open(self.name, "r")
            files.close()
        except:
            raise ExamEception("ERRORE, impossibile aprire il file ! ")
        



    def get_data(self):
        with open(self.name, "r") as file:
            my_lista = []
            for linea in file:
                linea = linea.strip().split(",")
                if linea[0] != "date":
                    try:
                        linea[1] = float(linea[1])
                        if linea[1] < 0:
                            continue
                    except:
                        continue

                    my_lista.append(linea)
            return (my_lista)
          
time_series_files = CSVTimesSeriesFiles(r"C:\Users\delma\Downloads\data (1).csv")
time_series = time_series_files.get_data()
# print("\n")
# print ( time_series)

    

#2)-->la funzione per calcolare la variazione delle temperature 


def compute_variations(my_series_times, firstyear, lastyear, N):
    my_dictionary = {}
    for element in my_series_times:
        anno = element[0].split("-")
        valore = element[1]
        data = int(anno[0])
        if data not in my_dictionary:
            my_dictionary[data] = []
        my_dictionary[data].append(valore)
        
    ##return my_dictionary
    
    my_dictionary_2 = {}
    for item in my_dictionary.keys():
        for date in range(firstyear, lastyear +1):
            if item == date:
                my_dictionary_2[item] = my_dictionary[item]
    ##return my_dictionary_2
    dictionary = {}
    for elemento in my_dictionary_2.keys():
        media = sum(my_dictionary_2[elemento])/ len(my_dictionary_2[elemento])
        dictionary[elemento] = round(media,2)
    ##return dictionary
    yo = lastyear - firstyear
    if N >= (lastyear - firstyear ):
        raise ExamEception("Ci è stata un errore, la finestra  deve  essere strettamente minore di {} ".format(yo))
    
    for mia_data in dictionary.keys():
        table = []
        for i in range(N):

            try:
                table.append(dictionary[mia_data-i-1])
            except:
                continue

        try:
            if len(table) == 0:
                my_dictionary_2[mia_data] = 0
            else: 
                media_mobile = sum(table)/len(table)
                my_dictionary_2[mia_data] = media_mobile
        except:
                continue
    ##return my_dictionary_2
    dic_result = {}
    for delmas in my_dictionary_2.keys():
        styll = str(delmas)
        val = dictionary[delmas] - my_dictionary_2[delmas]
        dic_result[styll] = round(val,2)
    ##return dic_result


# #funzione per la lode

# def Lode_valori_fuori(lista, first_temp, last_temp):
#     count = 0
#     diz = {}
#     for item in lista:
#         data = item[0].split("-")
#         anno = int(data[0])
#         valore = item[1]
#         if not anno in diz.keys():
#             diz[anno] = []
#         diz[anno].append(valore)
#     ##return diz
#     if first_temp >= last_temp:
#         raise ExamEception ("ERRORE : IL volore al posto di {} deve essere minore di quella al posto di {}".format(first_temp, last_temp))
#     if first_temp < 0 or last_temp < 0:
#         raise ExamEception("ERRORE : gli estremi non possono esssere negativo !")
#     for item in diz.keys():
#         for element in diz[item]:
#             if element < first_temp or element > last_temp:
#                 count += 1
#                 break
#     print(len(diz))
#     return count
               
    


# result = Lode_valori_fuori(time_series, -117,138)

# print("\n")

# print(result)


#x = compute_variations(time_series, 1950, 1957,3)
#print("\n")
#print(x)


#FINE DEL PROVA#********


##---------------SECONDA PROVA-------->



##----------------------------------------------------------->

##ESERCITAZIONE-2



# class ExamException(Exception):
#     pass


# class CSVTimesSeriesFiles:
#     def __init__(self, my_files_Series):
#         self.name = my_files_Series
#         try:
#             file = open(self.name, "r")
#             file.close()
#         except:
#             raise ExamException("ERRORE: il file {} non è apribile".format(self.name))

#     def get_data(self):
#         with open (self.name, "r") as files:
#             my_lista = []
#             for linea in files:
#                 linea = linea.strip().split(",")
#                 try:
#                     linea[1] = int (linea[1])
#                 except:
#                     continue 

#                 if not isinstance(linea[1], int):
#                    raise ExamException ("Errore: c'è una valore che non è un itero") #non serve troppo perchè non funziona davvro
                
#                 if linea[0] != "date":
#                     my_lista.append(linea)
#             return my_lista

#          #tratamenti per la LODE (del secondo punto-->verificare l'ordinamento  ) 

#         for ordin in my_lista:
#             ordinato = ordin[0].split("-")#***********
            

           



# time_series_file = CSVTimesSeriesFiles(r"C:\Users\delma\Downloads\data (1).csv")
# time_series = time_series_file.get_data()
# print("\n")
# print(time_series)


# #ecco funzione compute varitation

# def compute_variations(my_times_seriesVaria, first_year, last_year):
#     my_dict = {}
#     for element_0 in my_times_seriesVaria:
#         anno = element_0[0].split("-")
#         valore = element_0[1]
#         data = int(anno[0])
#         if data not in my_dict.keys():
#             my_dict[data] = [] 
#         my_dict[data].append(valore) 

# # a questo livello il "return my_dict" qui sotto ci permette di avere il dizionario per chiavi ogni anno et valore i numeri di passaggi               
#     ##return my_dict

#     my_dict_media = {}  # il calcolo della media per ogni anno 
#     for item in my_dict.keys():
#         media = sum(my_dict[item]) / len(my_dict[item])
#         my_dict_media[item] = round(media,2)

# #a questo livello il "return my_dict_media" ci permette di avere il dizionario per chiavi ogni anno e il valore della media annuale
#     ##return my_dict_media
    
#     table_intervalli = []

#     #effettuamo il casting per trasformare gli estremi dell'intervallo in interi
#     first_year = int(first_year)
#     last_year = int (last_year)

#     #verifichiamo se gli estremi appartengono ai datti
#     if first_year not in  my_dict_media  or  last_year not in  my_dict_media:
#         raise ExamException("ERRORE: gli estremi dell'intervallo non sono contenuti nei dati")
    
#     for i in range(last_year +1 - first_year):
#         table_intervalli.append(first_year + i)
#     ##return table_intervalli
#     my_dict_intervalli = {}
#     for j in my_dict_media.keys():
#         for k in table_intervalli:
#             if j == k:
#                 my_dict_intervalli[k] = my_dict_media[j]
#     ##return my_dict_intervalli 

#     dictionary_fine_result = {}
#     for my_way in my_dict_intervalli.keys():
#         try:
#             dif = my_dict_intervalli[my_way] - my_dict_media [my_way-1]
#         except:
#             dif = my_dict_intervalli[my_way]
#         my_way_1 = str(my_way)
#         my_way_2 = str(my_way - 1)
#         my_way_tab = [my_way_2, my_way_1]
        
#         if my_way-1 not in my_dict_intervalli:
#             continue
#         else:
#             my_way_f = "-".join(my_way_tab)
           
#         dictionary_fine_result[my_way_f] = round(dif,2)
#     return dictionary_fine_result




# result = compute_variations(time_series, "1949", "1953" )
# print("\n")
# print(result)

# #---PARTE OPZIONALE PER LA LODE--->(già tratatto nel programma)







##---------------------------------------------##

#ESERCITAZIONE DI ESAME 1(MOVINGaVERAGE)

# class ExamException(Exception):
#     pass


# class MovingAverage:
#     def __init__(self, lunghezza):
#         self.lunghezza = lunghezza

#     def compute(self, my_list):
#         if self.lunghezza > len(my_list):
#             raise ExamException ("ERRORE: la lunghezza deve essere minore di {} ".format(len(my_list)))
#         if self.lunghezza < 0:
#             raise ExamException("ERRORE: la lunghezza non deve essere minore di 0 ! ")
#         if self.lunghezza == 0:
#             raise ExamException("ERRORE: la lunghezza non può essere nulla !")
        
#         lista_media_mobile = []
#         for i in range(len(my_list) - self.lunghezza +1):
#             media = sum(my_list[i: i + self.lunghezza ]) / self.lunghezza
#             lista_media_mobile.append(round(media,1))
#         return lista_media_mobile
        

# moving_average = MovingAverage(0) 
# result = moving_average.compute(([2,4,8,16]))
# print(result)


##--------------------------------------------------------------------------------------------------->
#ESERCIZIO D'APPLICAZIONE(SLIDE)

# def sum_csv(file_name):
#     tot_vendite = 0
#     with open (file_name) as file:
#         for linea in file:
#             linea = linea.strip().split(",")
#             #data = linea[0]
#             value = linea[1]
#             if linea[1] != "Sales":
#                 #try:
#                     value = float(value)
#                     tot_vendite += value
#                 #except:
#                    # pass
                
#         return round(tot_vendite,1)
    

# test = sum_csv(r"C:\Users\delma\Downloads\shampoo_sales.csv")
# print(test)

##-------------------------------------------------

#ALTRI ESERCIZI------>

#1)FUNZIONE PER CONTARE IL NUMERO DI OCCORENZA DI UNA PAROLA NEL UN FILE

# def count_volte(my_files, parola):
#     count = 0
#     with open(my_files, "r") as files:
#        for linea in files:
#            linea = linea.strip().split(",")
#            try:
#                 if linea[0] == parola or linea[1] == parola or linea[2] == parola:
#                     count += 1
#            except:
#                pass
#        return count

# test = count_volte(r"C:\Users\delma\Downloads\shampoo_sales.txt", "Shampooing")
# print(test)
#-----------
# #2

# def conta_ogni_volta(my_files):
#     lista = []
#     grandeLista = []
#     with open (my_files, "r") as files:
#         for linea in files:
#             linea = linea.strip().split(",")
#             lista.append(linea)
#         ##return lista
#         for element in lista:
#             for i in element:
#                 grandeLista.append(i)
#         #return grandeLista
#         num_vole = {} 
#         for j in grandeLista:
#             if j not in num_vole:
#                 num_vole[j] = 1
#             else:
#                 num_vole[j] += 1
#         return num_vole
    
# test = conta_ogni_volta(r"C:\Users\delma\Downloads\shampoo_sales.txt")
# print("\n")
# print(test)
#--------------------


#3

# def diz_maggiore(my_files):
#     tab= []
#     with open (my_files) as files:
#         for linea in files:
#             linea = linea.strip().split(",")
#             tab.append(linea)
#         ##return tab
#         table = []
#         for elemento in tab:
#             for i in elemento:
#                 table.append(i)
#         ##return table
#         dictionary = {}
#         for item in table:
#             val = item[0]
#             if val not in dictionary:
#                 dictionary[val] = []
#             dictionary[val].append(item)
#         ##return dictionary
#         my_dictionary = {}
#         for tink in dictionary.keys():
#             values = dictionary[tink]
#             massimo = max(values, key= len)
#             my_dictionary[tink] = massimo
#         return my_dictionary

# test = diz_maggiore(r"C:\Users\delma\Downloads\shampoo_sales.txt")
# print("\n")
# print(test)

#--------------------
#4)

# import re

# def conteggio (my_files):
#     lista = []
#     with open(my_files, "r") as files:
#         for linea in files:
#             linea = linea.strip()
#             linea = re.split(r"[.!?]", linea)
#             if linea != " ":
#                 lista.append(linea)
#         ##return lista
#         tab = []
#         for item in lista:
#             for i in item:
#                 if i == " ":
#                   continue
#                 tab.append(i)
#         ##return tab
#         my_dictionary = {}
#         for elemento in tab:
#             if elemento.strip() :
#                 if elemento[0].isupper():
#                     if elemento[0] not in my_dictionary:
#                         my_dictionary[elemento[0]] = []
#                     my_dictionary[elemento[0]].append(elemento)
#         return my_dictionary


    
    
# result = conteggio(r"C:\Users\delma\Downloads\shampoo_sales.txt")
# print("\n")
# print (result)
#---------------------------------------------NON FUNZIONA BENE-



#5)



            



                










