from bokeh.plotting import figure, output_file, show ## importando de bokeh

if __name__ == '__main__':
    output_file('graficado_simple.html') ## nombre file de salida 
    fig = figure()
    
    total_vals = int(input('Cuantos valore quieres graficar?'))
    x_vals = list(range(total_vals)) ## valore en x oara grafico
    y_vals = []

    for i in x_vals:
        val = int(input(f'Valor "y" para {x_vals}'))
        y_vals.append(val) ## valore en y para cada x

    fig.line(x_vals, y_vals, line_width=2)
    show(fig) ## visualizador del grafico