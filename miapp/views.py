from django.shortcuts import render, HttpResponse, redirect

layout = """
<h1> Proyecto Web (LP3) | Jairo Daniel Mendoza Torres </h1>
<hr/>
<ul>
<li>
<a href="/inicio"> Inicio</a>
</li>
<li>
<a href="/saludo"> Mensaje de Saludo</a>
</li>
<li>
<a href="/rango"> Mostrar Números [a,b]</a>
    </li>
    <li>
<a href="/rango2/10/15"> Mostrar Números [10,15]</a>
    </li>
    <li>
</ul>
<hr/>
"""


def index(request):
    return render(request, "index.html")


def saludo(request):
    return render(request, "saludo.html")


def rango(request):
    a = 10
    b = 20
    resultado = f"""
    <h2> Números de [{a},{b}] </h2>
        Resultado: <br>
    <ul>
    """
    while a <= b:
        resultado += f"<li> {a} </li>"
        a += 1
        resultado += "</ul"
    return HttpResponse(layout + resultado)


def rango2(request, a, b):
    resultado = f"""
    <h2> Números de [{a},{b}] </h2>
    Resultado: <br>
    <ul>
    """
    while a <= b:
        resultado += f"<li> {a} </li>"
        a += 1
        resultado += "</ul"
    return HttpResponse(layout + resultado)


def rango2(request, a=0, b=100):
    resultado = f"""
    <h2> Números de [{a},{b}] </h2>
    Resultado: <br>
    <ul>
    """
    while a <= b:
        resultado += f"<li> {a} </li>"
        a += 1
        resultado += "</ul"
    return HttpResponse(layout + resultado)


def index(request):
    return render(
        request, "index.html", {"mensaje": "Proyecto web con Django (Desde el View)"}
    )


def saludo(request):
    return render(
        request,
        "saludo.html",
        {"titulo": "Saludo", "autor_saludo": "Jairo Daniel Mendoza Torres"},
    )


def index(request):
    estudiantes = [
        "Diana Quispe",
        "Armando Requejo",
        "Shantall Palomino",
        "Celia Torres",
    ]

    return render(
        request,
        "index.html",
        {
            "titulo": "Inicio",
            "mensaje": "Proyecto Web Con DJango",
            "estudiantes": estudiantes,
        },
    )


def rango(request):
    a = 10
    b = 20
    return render(
        request,
        "rango.html",
        {"titulo": "Rango", "a": a, "b": b, "numeros": range(a, b + 1)},
    )
