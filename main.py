import requests


def get_cookies():
    session = requests.Session()
    # send a get request to the server
    cookies = session.get(
        'https://sinhvien.huit.edu.vn/tra-cuu')
    a = session.cookies.get_dict()
    return a

cookies = get_cookies()

headers = {
    'Host': 'sinhvien.huit.edu.vn',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'vi-VN,vi;q=0.9',
    # 'Cookie': 'BNI_persistence=DkzC968nls1HLtZTkGxSMG8L0db1QszOVgH3Sej9HY5vt8bFx5TFhRUWpPizRFKPmOk4rkR4uYw-mlJ1_OB7Dg==; ASP.NET_SessionId=3ogkxoemrhebagepkrk3rlr5',
}

params = {
    'k': 'vE7Hp3zu1kykA91ICM7OY4gdbsFQwsIHMsBQo202cTY',
}

response = requests.get(
    'https://sinhvien.huit.edu.vn/tra-cuu/ket-qua-hoc-tap.html',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)

response2 = requests.get(
    'https://sinhvien.huit.edu.vn/tra-cuu/thong-tin-sinh-vien-by-qr-code.html',
    params=params,
    cookies=cookies,
    headers=headers
)

print(response2.text)

