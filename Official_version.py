import requests

#https://cdn9527.55661.cn:4433/73sm/asmr2/1688363827/hls.m3u8?token=3aa8a9f887d0c31cb1519908ce01efc4&t=1688608157&sid=6Z7eIW31wf&uid=26260


#https://cdn9527.55661.cn:4433/73sm/asmr/1687749950/hls.m3u8?token=0761fb9e631e78b9f1d7c7394ba8c2b3&t=1688609889&sid=XqvjTfMHI0&uid=26270
#https://cdn9527.55661.cn:4433/73sm/asmr/1687749950/vMgtn-hls-000.ts
#https://cdn9527.55661.cn:4433/73sm/asmr/1687749950/vMgtn-hls-001.ts

#https://cdn9527.55661.cn:4433/73sm/asmr2/1688363827/hls.m3u8?token=47607f644286d1e21792c90aedea1f12&t=1688615362&sid=D0l61yZWGp&uid=26270
#https://cdn9527.55661.cn:4433/73sm/asmr2/1688363827/z7Gds-hls-000.ts
def get_m3u8(url):
    #传入指向m3u8文件网址
    r = requests.get(url=url)
    with open('hls.m3u8','wb') as f:
        f.write(r.content)
    
def get_ts(ts_url, run_time):
    url_cut = ts_url.split('/')
    SecondHalfPart = url_cut.pop(-1)
    FristHalfPart = '/'.join(url_cut)
    SecondHalfPart = list(SecondHalfPart)
    del SecondHalfPart[-6:]
    SecondHalfPart = ''.join(SecondHalfPart)
    for i in range(run_time):
        url = FristHalfPart + '/' + SecondHalfPart + '%03d'%i + ".ts"
        r = requests.get(url=url)
        with open(SecondHalfPart + '%03d'%i + ".ts", 'wb') as f:
            f.write(r.content)

    return 



def file_handle(index):
    #处理m3u8文件，返回最后一个TS文件名
    with open(index,'r')  as f:
        m3u8_str = f.read()
        m3u8_list = m3u8_str.split('\n')
        return m3u8_list[-3]

#print(flie_handle("index.m3u8"))

def file_end(str):
    #处理文件名，得到文件数字
    str = int(str[-6:-3])
    return str

if __name__ == "__main__":
    url = input("m3u8 is>>> ")
    #url = "https://cdn9527.55661.cn:4433/73sm/asmr2/1688363827/hls.m3u8?token=3a9a5a1215308f9ddedc4f4fb32187b5&t=1688617550&sid=baiNqu5Mog&uid=26270"
    get_m3u8(url)
    str = file_handle("hls.m3u8")
    print(str)
    print(file_end(str))
    ts_url = input("ts is>>> ")
    #ts_url = "https://cdn9527.55661.cn:4433/73sm/asmr2/1688363827/z7Gds-hls-000.ts"
    get_ts(ts_url=ts_url,run_time=file_end(str)+1)
