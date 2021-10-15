from flask import Flask, render_template, request, Response
import json
app = Flask(__name__, static_folder="./static", template_folder="./templates")


@app.route("/", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        data = request.form
        for key, value in data.items():
            if key == "Name of Corpus":
                dict = {value:[]}
                name_c = value
                first = True
            elif "title" in key:
                if first == False:
                    dict[name_c].append(dict_i)
                first = False
                dict_i = {"title": "",
                          "codex_name":"",
                          "manifest_link":"",
                          "images":{}
                          }
                dict_i.update({"title":value})
            elif "codex" in key:
                dict_i.update({"codex_name":value})
            elif "manifest" in key:
                dict_i.update({"manifest_link":value})
            elif "folio_name" in key:
                label_image = value
            elif "folio_link" in key:
                dict_i["images"].update({label_image:value})
        dict[name_c].append(dict_i)
        return Response(response=json.dumps(dict, ensure_ascii=False, indent='\t'), mimetype="dict/json",headers={"Content-disposition":"attachment; filename=" + name_c + ".json"})
    return render_template("formulaire.html")

if __name__ == "__main__":
    app.run(debug=True)
