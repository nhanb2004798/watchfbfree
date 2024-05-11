import http.client as httplib

def download_web(server_ip, server_port, web_name):
    
    #tao noi ket noi http
    httpconn = httplib.HTTPConnection(server_ip, server_port)
    httpconn.request("GET","/index.html")
    resp = httpconn.getresponse()
    if resp.status == 200:
        content = resp.read()
        
        # Luu noi dung trang vao file
        with open(web_name, "wb") as file:
            file.write(content)
        print("Tai trang ve may thanh cong!!!!")
    else:
        print("Tai ve may khong thanh cong!!!")

ip = input('nhap dia cho can tai ve:')
port = 80
name = 'index.html'

download_web(ip, port, name)
