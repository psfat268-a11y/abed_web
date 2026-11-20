import os
from flask import Flask, request

app = Flask(__name__)


def clean_float(value, default=0.0):
  try:
    if value is None or str(value).strip() == "":
      return float(default)
    return float(value)
  except (ValueError, TypeError):
    return float(default)


def format_num(num):
  return int(num) if float(num).is_integer() else round(float(num), 2)


@app.route("/health")
def health():
  return {"status": "ok", "app": "abed-web-calculator-10"}


@app.route("/", methods=["GET", "POST"])
def calculator():
  result_html = ""

  if request.method == "POST":
    name = request.form.get("name", "").strip()
    name1 = request.form.get("name1", "").strip()
    material = request.form.get("material", "").strip()
    sur_note = clean_float(request.form.get("sur_note"), default=100.0)

    tr1 = clean_float(request.form.get("tr1"))
    note1 = clean_float(request.form.get("note1"))
    tr2 = clean_float(request.form.get("tr2"))
    note2 = clean_float(request.form.get("note2"))
    tr3 = clean_float(request.form.get("tr3"))
    note3 = clean_float(request.form.get("note3"))
    tr4 = clean_float(request.form.get("tr4"))
    note4 = clean_float(request.form.get("note4"))
    tr5 = clean_float(request.form.get("tr5"))
    note5 = clean_float(request.form.get("note5"))
    tr6 = clean_float(request.form.get("tr6"))
    note6 = clean_float(request.form.get("note6"))
    tr7 = clean_float(request.form.get("tr7"))
    note7 = clean_float(request.form.get("note7"))
    tr8 = clean_float(request.form.get("tr8"))
    note8 = clean_float(request.form.get("note8"))
    tr9 = clean_float(request.form.get("tr9"))
    note9 = clean_float(request.form.get("note9"))
    tr10 = clean_float(request.form.get("tr10"))
    note10 = clean_float(request.form.get("note10"))

    note12 = float(
        note1
        + note2
        + note3
        + note4
        + note5
        + note6
        + note7
        + note8
        + note9
        + note10
    )
    note13 = float(
        tr1 + tr2 + tr3 + tr4 + tr5 + tr6 + tr7 + tr8 + tr9 + tr10
    )

    if note13 > 0 and sur_note > 0:
      note1234 = float(sur_note / note13)
      note_final = float(note1234 * note12)
      note_final_rounded = round(note_final, 2)

      result_html = f"""
            <div class="result">
                <h3>welcome {name} {name1} ({material})</h3>
                <p>Total des contrôles : <strong>{format_num(note12)} / {format_num(note13)}</strong></p>
                <p>La total note de <strong>{name}</strong> est : <strong>{note_final_rounded} sur {format_num(sur_note)}</strong></p>
                <p>Good luck</p>
            </div>
            """
    else:
      result_html = '<div class="error">خطأ: مجموع العلامات القصوى (Control) والمجموع المطلوب يجب أن يكونا أكبر من صفر.</div>'

  return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Abed Web - Calculator</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f1f5f9;
                margin: 0;
                padding: 30px 15px;
            }}

            .container {{
                max-width: 560px;
                margin: auto;
                background: #ffffff;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
            }}

            h1 {{
                text-align: center;
                color: #1a73e8;
                margin-top: 0;
                margin-bottom: 22px;
            }}

            .row {{
                display: flex;
                gap: 10px;
                margin-bottom: 11px;
            }}

            input {{
                width: 100%;
                padding: 10px 11px;
                border: 1px solid #cbd5e1;
                border-radius: 8px;
                font-size: 14px;
                box-sizing: border-box;
            }}

            input:focus {{
                outline: none;
                border-color: #1a73e8;
            }}

            .sur-box {{
                border: 2px solid #1a73e8;
                background-color: #f8fbff;
            }}

            button {{
                width: 100%;
                padding: 13px;
                background-color: #1a73e8;
                color: #ffffff;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                margin-top: 10px;
            }}

            button:hover {{
                background-color: #1557b0;
            }}

            .result {{
                margin-top: 20px;
                padding: 15px;
                background-color: #e6f4ea;
                border-left: 5px solid #34a853;
                border-radius: 8px;
            }}

            .error {{
                margin-top: 20px;
                padding: 15px;
                background-color: #fce8e6;
                border-left: 5px solid #ea4335;
                border-radius: 8px;
                color: #c5221f;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>welcome to abed web</h1>
            <form method="POST">
                <div class="row">
                    <input type="text" name="name" placeholder="nom de etudiant" required>
                    <input type="text" name="name1" placeholder="nom de famille" required>
                </div>
                <div class="row">
                    <input type="text" name="material" placeholder="what the material" required>
                </div>
                <div class="row">
                    <input type="number" step="any" name="sur_note" class="sur-box" placeholder="Sur combien tu veux la note finale" required>
                </div>

                <div class="row">
                    <input type="number" step="any" name="tr1" placeholder="Control 1" required>
                    <input type="number" step="any" name="note1" placeholder="Note 1" required>
                </div>
                <div class="row">
                    <input type="number" step="any" name="tr2" placeholder="Control 2" required>
                    <input type="number" step="any" name="note2" placeholder="Note 2" required>
                </div>
                <div class="row">
                    <input type="number" step="any" name="tr3" placeholder="Control 3" required>
                    <input type="number" step="any" name="note3" placeholder="Note 3" required>
                </div>
                <div class="row">
                    <input type="number" step="any" name="tr4" placeholder="Control 4" required>
                    <input type="number" step="any" name="note4" placeholder="Note 4" required>
                </div>
                <div class="row">
                    <input type="number" step="any" name="tr5" placeholder="Control 5" required>
                    <input type="number" step="any" name="note5" placeholder="Note 5" required>
                </div>
                <div class="row">
                    <input type="number" step="any" name="tr6" placeholder="Control 6" required>
                    <input type="number" step="any" name="note6" placeholder="Note 6" required>
                </div>
                <div class="row">
                    <input type="number" step="any" name="tr7" placeholder="Control 7" required>
                    <input type="number" step="any" name="note7" placeholder="Note 7" required>
                </div>
                <div class="row">
                    <input type="number" step="any" name="tr8" placeholder="Control 8" required>
                    <input type="number" step="any" name="note8" placeholder="Note 8" required>
                </div>
                <div class="row">
                    <input type="number" step="any" name="tr9" placeholder="Control 9" required>
                    <input type="number" step="any" name="note9" placeholder="Note 9" required>
                </div>
                <div class="row">
                    <input type="number" step="any" name="tr10" placeholder="Control 10" required>
                    <input type="number" step="any" name="note10" placeholder="Note 10" required>
                </div>

                <button type="submit">Calculer la note</button>
            </form>
            {result_html}
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port, debug=True)
