

while True:
    import requests
    URL = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
      
    file = requests.get(URL, stream = True)
      
    with open("Python.pdf","wb") as pdf:
        for chunk in file.iter_content(chunk_size=1024):
      
             if chunk:
                 pdf.write(chunk)
