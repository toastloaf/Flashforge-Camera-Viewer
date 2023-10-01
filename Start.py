import webview

with open('Write_IP_Address_Here.txt', 'r') as file:
    file_contents = file.read()

webview.create_window('Make sure your printers IP Address is set correctly in the txt file', f"http://{file_contents}:8080/?action=stream", zoomable=True)
webview.start()
