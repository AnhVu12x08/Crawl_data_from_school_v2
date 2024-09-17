# import the requests library 
import requests
# initialize a session 
session = requests.Session()
# send a get request to the server 
cookies = session.get('https://sinhvien.huit.edu.vn/tra-cuu/ket-qua-hoc-tap.html?k=vE7Hp3zu1kykA91ICM7OY4gdbsFQwsIHMsBQo202cTY')
# print the response dictionary 
print(session.cookies.get_dict()) 