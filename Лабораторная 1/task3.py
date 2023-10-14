informVolume = 1.44*1024**2
cntPage = 100
cntStrInPage = 50
cntSymbolsInPage = 25
bytesForSymb = 4

result = int(informVolume//(bytesForSymb * cntSymbolsInPage * cntStrInPage * cntPage))
print("Количество книг, помещающихся на дискету:", result)
