#Aula1 Colorização.ipynb


! git clone https://github.com/awarischool/data-science

#Baixando A Biblioteca

!wget clone https://raw.githubusercontent.com/awarischool/data-science/master/image-colorizer/deoldify_wrapper.py

#Importando a Biblioteca

from deoldify_wrapper import DeOldify

deoldify = DeOldify()

deoldify.colorize("https://i.pinimg.com/236x/40/83/3c/40833ca37dcab0246c67054bf8f65c23--black-white-photography-new-york-city.jpg")

