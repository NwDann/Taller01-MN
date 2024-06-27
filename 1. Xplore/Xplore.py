from collections import OrderedDict

def funcion(n, data):
    
    if n == len(data) and n != 0:
        x = {} #Diccionario que almacena el nombre del autor y un array de sus citaciones
        if n >= 2 and n <= 10000:
            for i in range(len(data)):
                names = [author["full_name"] for author in data[i]["authors"]["authors"]]
                count = data[i]["citing_paper_count"]
                
                for aux in range(len(names)):
                    if names[aux] not in x:
                        x[names[aux]] = [count]
                    else:
                        for aux1 in x.keys():
                            if aux1 == names[aux]:
                                x[aux1].append(count)
            
            for key, value in x.items():
                sorted_array = sorted(value, reverse=True)
                x[key] = sorted_array
                j = 0
                cont = 0
                for j in range(len(sorted_array)):
                    if sorted_array[j] >= j+1:
                        cont += 1
                x[key].append(cont) #El valor final del array es igual al h-index
            

            sorted_data = dict(sorted(x.items(), key=lambda item: (-item[1][-1], item[0])))
            for f in sorted_data:
                print(f"{f} {sorted_data[f][len(sorted_data[f])-1]}") 



        elif n == 1:
            names = [author["full_name"] for author in data[0]["authors"]["authors"]]
            for aux in range(len(names)):
                x[names[aux]] = 1
    
            orden = OrderedDict(sorted(x.items()))
            print(orden)
            for aux1 in orden:
                print(f"{aux1} {orden[aux1]}") 
    else:
        print("*******ERROR*********")

data = []
data.append({"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Echo"}, {"author_order": 2,"affiliation": "","full_name": "Bravo"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}]},"title": "Article Title 1","article_number": "1","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"})
data.append({"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Bravo"}]},"title": "Article Title 2","article_number": "2","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"})
data.append({"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Echo"}, {"author_order": 2,"affiliation": "","full_name": "Delta"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}, {"author_order": 4,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 3","article_number": "3","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"})
data.append({"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 4","article_number": "4","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"})
data.append({"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}]},"title": "Article Title 5","article_number": "5","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 5,"publisher": "IEEE"})
data.append({"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}]},"title": "Article Title 6","article_number": "6","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 6,"publisher": "IEEE"})
data.append({"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Delta"}]},"title": "Article Title 7","article_number": "7","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"})
data.append({"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 8","article_number": "8","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"})
data.append({"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Delta"}, {"author_order": 2,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 9","article_number": "9","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"})
data.append({"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Bravo"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}]},"title": "Article Title 10","article_number": "10","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 6,"publisher": "IEEE"})

funcion(10, data)    



    