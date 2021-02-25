import codecs
def retorno_html():
    file = codecs.open("emailpagenovo1.html", "r", "utf-8")
    html_readed = file.read()
    return html_readed



