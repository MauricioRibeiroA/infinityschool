from tkinter import *

window = Tk()
window.title('Janela de testes')

txt = Label(
    text='Infinity School',
    foreground='red',
    background='white'
)

btn = Button(
    text='Clique aqui',
    width='25',
    height='5',
    fg='blue',
    bg='red'
)

campo = Entry(
    fg='#2A2A2A',
    bg='#F3E8E8',
    width=30
)

#para inserir a string Python no começo do campo
campo.insert(0, 'Digite aqui: ')
#para inserir ao final, caso já exista algum texto
campo.insert('end', 'Python')

#chamando os objetos com o método pack()
txt.pack()
btn.pack()
campo.pack()




window.mainloop()