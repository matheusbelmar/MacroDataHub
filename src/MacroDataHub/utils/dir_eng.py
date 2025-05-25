import os 


os.chdir(r"/home/mbelmar/Documentos/Programaçao - Projetos/Projetos/MacroDataHub/MacroDataHub")

folders=[
     'ingestion' 
    ,'pipelines' 
    ,'storage' 
    ,'datasets' 
    ,'visualizations' 
    ,'reports' 
    ,'models' 
    ,'config' 
    ,'utils' 
    ,'tests'
    ] 

for i in folders:
    os.mkdir(i)