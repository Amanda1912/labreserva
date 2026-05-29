from flask import Flask, render_template, request, jsonify
from database import criar_tabela, conectar

app = Flask(__name__)

criar_tabela()

LABORATORIOS = [
    "Laboratório 01",
    "Laboratório 02",
    "Laboratório 03",
    "Laboratório 04",
    "Laboratório 05",
    "Laboratório 06",
    "Laboratório 07",
    "Laboratório 08"
]

HORARIOS = [
    "07:30 - 08:20",
    "08:20 - 09:10",
    "09:10 - 10:00",
    "10:00 - 10:50",
    "10:50 - 11:40",
    "11:40 - 12:40",
    "14:00 - 14:50",
    "14:50 - 15:40",
    "15:40 - 16:30",
    "16:30 - 17:20",
    "17:20 - 18:10",
    "18:10 - 18:30"
]

@app.route("/")
def index():
    return render_template("index.html", laboratorios=LABORATORIOS)


@app.route("/horarios-disponiveis")
def horarios_disponiveis():
    laboratorio = request.args.get("laboratorio")
    data = request.args.get("data")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT horario FROM reservas
        WHERE laboratorio = ? AND data = ?
    """, (laboratorio, data))

    horarios_reservados = [linha[0] for linha in cursor.fetchall()]
    conexao.close()

    disponiveis = [h for h in HORARIOS if h not in horarios_reservados]

    return jsonify(disponiveis)


@app.route("/reservar", methods=["POST"])
def reservar():
    dados = request.json

    professor = dados.get("professor")
    email = dados.get("email")
    laboratorio = dados.get("laboratorio")
    data = dados.get("data")
    horario = dados.get("horario")
    disciplina = dados.get("disciplina")

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO reservas 
            (professor, email, laboratorio, data, horario, disciplina)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (professor, email, laboratorio, data, horario, disciplina))

        conexao.commit()
        conexao.close()

        return jsonify({"mensagem": "Reserva realizada com sucesso!"}), 201

    except:
        return jsonify({"erro": "Esse horário já foi reservado para este laboratório."}), 400


@app.route("/reservas")
def listar_reservas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT professor, email, laboratorio, data, horario, disciplina
        FROM reservas
        ORDER BY data, horario
    """)

    reservas = cursor.fetchall()
    conexao.close()

    lista = []

    for r in reservas:
        lista.append({
            "professor": r[0],
            "email": r[1],
            "laboratorio": r[2],
            "data": r[3],
            "horario": r[4],
            "disciplina": r[5]
        })

    return jsonify(lista)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)