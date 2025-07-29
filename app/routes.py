from flask import Blueprint, render_template, request
from .generator import generate_password

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    password = None

    # Valores por defecto
    length = 16
    use_symbols = False
    use_numbers = False
    use_uppercase = False
    use_lowercase = True  # ← por defecto marcado

    if request.method == 'POST':
        length = int(request.form.get('length', 16))
        use_symbols = 'symbols' in request.form
        use_numbers = 'numbers' in request.form
        use_uppercase = 'uppercase' in request.form
        use_lowercase = 'lowercase' in request.form
        if length < 4 or length > 128:
            password = "Error: longitud inválida (4–128 caracteres)"


        password = generate_password(
            length,
            symbols=use_symbols,
            numbers=use_numbers,
            uppercase=use_uppercase,
            lowercase=use_lowercase
        )

    return render_template(
        'index.html',
        password=password,
        length=length,
        use_symbols=use_symbols,
        use_numbers=use_numbers,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase
    )
