import paralleldots

paralleldots.set_api_key('nYD8udaOIf3bvPBLOyWSqrmAMePOtvYFbiJWNW9byXk')

def ner(text):
    ner = paralleldots.ner(text)
    return ner
def sentiment(text):
    sentiment = paralleldots.sentiment(text)
    return sentiment
def abuse(text):
    abuse=paralleldots.abuse(text)
    return abuse