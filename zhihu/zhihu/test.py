import requests

headers={
    "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}
cookies={
    "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49":"1581066366",
    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49":"1578478780,1580560726,1581056833",
    "KLBRSID":"b33d76655747159914ef8c32323d16fd|1581066365|1581056649",
    "__gads":"ID=e125432d03295875:T=1542635651:S=ALNI_Ma0Kkt3KeH4rH4ID5Xfhgl5RDYGFg",
    "_xsrf":"HClKhVQ62xS8QB6rFuaTap362GMa86Jd",
    "_zap":"241a92bb-2f37-4773-8ae6-e70650b7a754",
    "capsion_ticket":"2|1:0|10:1581063018|14:capsion_ticket|44:Y2M3MWJhMDFlNmU2NGU0M2FhYjA5M2M2MTAyZTI4OTE=|79c39eb76684f096647cadfd65c08ae3464be16bf55abb827f419d0e06c7c605",
    "d_c0":"AEBmOkSLIQ6PThIA-qi4zL33FQUHqBX7wko=|1535549268",
    "q_c1":"76bf8402efd145a7abf989bf0cca7ead|1573019589000|1564062247000",
    "tst":"r",
    "z_c0":"2|1:0|10:1581063018|14:capsion_ticket|44:Y2M3MWJhMDFlNmU2NGU0M2FhYjA5M2M2MTAyZTI4OTE=|79c39eb76684f096647cadfd65c08ae3464be16bf55abb827f419d0e06c7c605",
}

# url="https://www.zhihu.com/club/explore"
url="https://www.zhihu.com/api/v4/clubs/categories/1178345206151356416"
response=requests.get(url=url,headers=headers,cookies=cookies)
print(response.text)