import nltk
class Analizador:
    
    def estructura():   
        estructura = """
        OracionSimple -> Pronombre verbo Predicado | Pronombre | Pronombre verbo Predicado Predicado | Pronombre verbo
        Pronombre -> Articulos Pro | Pro
        Predicado -> Articulos Sustantivo | Sustantivo | Articulos Sustantivo Adjetivos Preposicion 
        Articulos -> "las" | "le" | "los" | "la" |"una" | "el"
        Adjetivos -> "verde"
        Preposicion -> "con"
        Sustantivo -> 'pelota' | 'niña' | 'manzana' | 'pera' | 'cuchillo'
        Pro -> 'Juan' | 'Ana' | "niña" 
        verbo -> 'come' | 'salta' | 'pela' | 'persigue' | "corre"
        """
        return estructura

        


    def main(estructura):
        frase = input("Ingresa una frase, recuerda usar las palabras definidas: ")
        analisis = nltk.ChartParser(nltk.CFG.fromstring(estructura))
        txt=""
        print("-------------------------------")
        for palabra in analisis.parse(frase.split()):
            if palabra:
                txt +="Frase valida"

        if txt =="":
            print("Frase invalida")
        else:
            print(txt)
    
        print("-------------------------------")
    
Analizador.main(Analizador.estructura())
