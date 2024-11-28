import flet as ft
import sympy as sp

def main(page: ft.Page):
    page.title = "Evaluador de Funciones Matemáticas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Definir los elementos de la interfaz
    input_function = ft.TextField(label="Ingresa la función matemática", autofocus=True)
    input_point = ft.TextField(label="Ingresa el valor del punto para evaluar")
    output_result = ft.Column()

    def evaluate_function(e):
        # Leer la función y el punto
        func_str = input_function.value
        point_str = input_point.value

        try:
            # Parsear la función y el punto
            x = sp.symbols('x')
            func = sp.sympify(func_str)
            point = float(point_str)

            # Evaluar la función en el punto
            result = func.subs(x, point)
            output_result.controls.append(ft.Text(f"Resultado: {result}"))
        except Exception as ex:
            output_result.controls.append(ft.Text(f"Error: {ex}"))

        # Actualizar la interfaz
        page.update()

    # Botón para evaluar la función
    evaluate_button = ft.ElevatedButton("Evaluar", on_click=evaluate_function)

    # Organizar los elementos en la página
    page.add(
        input_function,
        input_point,
        evaluate_button,
        output_result,
    )

# Ejecutar la aplicación
ft.app(target=main)

