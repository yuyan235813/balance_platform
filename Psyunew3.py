# -- coding: utf-8 --
import platform
from ctypes import *
import random
import os,sys

path = os.getcwd()
bit64 = ('64bit', 'WindowsPE')
bit32 = ('32bit', 'WindowsPE')
if 'Windows' in platform.system():
        if platform.architecture()==bit64:
           path = path+"\\rmf\\x64\Syunew3D.dll"
           Psyuunew=windll.LoadLibrary(path)
        elif platform.architecture()==bit32:
           path = path+"\\rmf\\x86\Syunew3D.dll"
           Psyuunew=windll.LoadLibrary(path)
        else:
            path = path + "\\rmf\\x64\Syunew3D.dll"
            Psyuunew = windll.LoadLibrary(path)
else:
       Psyuunew=cdll.LoadLibrary('libPsyunew3.so')        

##获到锁的版本
NT_GetIDVersion=Psyuunew.NT_GetIDVersion
NT_GetIDVersion.argtypes=(c_void_p,c_char_p)
NT_GetIDVersion.restypes=(c_int)


##获取锁的扩展版本
NT_GetVersionEx=Psyuunew.NT_GetVersionEx
NT_GetVersionEx.argtypes=(c_void_p,c_char_p)
NT_GetVersionEx.restypes=(c_int)

##写一个字节到加密锁中
YWrite=Psyuunew.YWrite
YWrite.argtypes=(c_byte ,c_short,c_char_p ,c_char_p,c_char_p )
YWrite.restypes=(c_int)

##从加密锁中读取一个字节
YRead=Psyuunew.YRead
YRead.argtypes=(c_void_p,c_short,c_char_p ,c_char_p,c_char_p )
YRead.restypes=(c_int)

##写一个字节到加密锁中
YWriteEx=Psyuunew.YWriteEx
YWriteEx.argtypes=(c_void_p,c_short,c_short,c_char_p,c_char_p,c_char_p )
YWriteEx.restypes=(c_int)

##从加密锁中读取一批字节
YReadEx=Psyuunew.YReadEx
YReadEx.argtypes=(c_void_p,c_short,c_short,c_char_p,c_char_p,c_char_p )
YReadEx.restypes=(c_int)

##查找加密锁
FindPort=Psyuunew.FindPort  
FindPort.argtypes=(c_int ,c_char_p)
FindPort.restypes=(c_int)

##获取锁的ID
GetID=Psyuunew.GetID  
GetID.argtypes=(c_void_p,c_void_p,c_char_p)
GetID.restypes=(c_int)

##从加密锁中读字符串
YReadString=Psyuunew.YReadString 
YReadString.argtypes=(c_char_p ,c_short,c_int ,c_char_p ,c_char_p,c_char_p)
YReadString.restypes=(c_int)

##写字符串到加密锁中
YWriteString=Psyuunew.YWriteString
YWriteString.argtypes=(c_char_p,c_short,c_char_p ,c_char_p,c_char_p )
YWriteString.restypes=(c_int)

##设置写密码
SetWritePassword=Psyuunew.SetWritePassword
SetWritePassword.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetWritePassword.restypes=(c_int)

##设置读密码
SetReadPassword=Psyuunew.SetReadPassword
SetReadPassword.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetReadPassword.restypes=(c_int)

##设置增强算法密钥一
SetCal_2=Psyuunew.SetCal_2
SetCal_2.argtypes=(c_char_p,c_char_p)
SetCal_2.restypes=(c_int)

##使用增强算法一对字符串进行加密
EncString=Psyuunew.EncString  
EncString.argtypes=(c_char_p,c_char_p,c_char_p)
EncString.restypes=(c_int)

##使用增强算法一对二进制数据进行加密
Cal=Psyuunew.Cal  
Cal.argtypes=(c_void_p,c_void_p,c_char_p)
Cal.restypes=(c_int)


##使用增强算法对字符串进行解密使用软件
##StrDec=Psyuunew.StrDec
##StrDec.argtypes=(c_char_p,c_char_p,c_char_p)
##StrDec.restypes=(c_void )
##
##StrEnc=Psyuunew.StrEnc  
##StrEnc.argtypes=(c_char_p,c_char_p,c_char_p)
##StrEnc.restypes=(c_void)
##
##EnCode=Psyuunew.EnCode    
##EnCode.argtypes=(c_void_p ,c_void_p ,  c_char_p )
##EnCode.restypes=(c_void)
##
##DeCode=Psyuunew.DeCode   
##DeCode.argtypes=(c_void_p , c_void_p , c_char_p  )
##DeCode.restypes=(c_void)
##使用增强算法对字符串进行解密使用软件)


##使用增强算法对二进制数据进行加密使用软件)
DecBySoft=Psyuunew.DecBySoft         
DecBySoft.argtypes=(c_void_p, c_void_p )

EncBySoft=Psyuunew.EncBySoft         
EncBySoft.argtypes=(c_void_p   ,  c_void_p   )
##使用增强算法对二进制数据进行加密使用软件)

##字符串及二进制数据的转换
##HexStringToc_byteArray=Psyuunew.HexStringToc_byteArray
##HexStringToc_byteArray.argtypes=(c_char_p ,c_void_p)
##HexStringToc_byteArray.restypes=(c_void)
##
##ByteArrayToHexString=Psyuunew.ByteArrayToHexString
##ByteArrayToHexString.argtypes=(c_void_p,c_char_p ,c_int )
##ByteArrayToHexString.restypes=(c_void)
##字符串及二进制数据的转换

 ##初始化锁函数,注意，初始化锁后，所有的数据为0，读写密码也为00000000-00000000，增强算法不会被初始化
ReSet=Psyuunew.ReSet
ReSet.argtypes=[c_char_p]
ReSet.restypes=(c_int)

##以下函数只限于带U盘的锁
##设置是否显示U盘部分盘符，真为显示，否为不显示
SetHidOnly=Psyuunew.SetHidOnly 
SetHidOnly.argtypes=( c_bool,c_char_p)
SetHidOnly.restypes=(c_int)

##设置U盘部分为只读状态，
SetUReadOnly=Psyuunew.SetUReadOnly 
SetUReadOnly.argtypes=[c_char_p]
SetUReadOnly.restypes=(c_int)
##以上函数只限于带U盘的锁

##以下函数只支持智能芯片的锁
##生成SM2密钥对
YT_GenKeyPair=Psyuunew.YT_GenKeyPair
YT_GenKeyPair.argtypes=(c_char_p ,c_char_p,c_char_p,c_char_p)
YT_GenKeyPair.restypes=(c_int)

##设置Pin码
YtSetPin=Psyuunew.YtSetPin
YtSetPin.argtypes=(c_char_p,c_char_p,c_char_p )
YtSetPin.restypes=(c_int)

##设置SM2密钥对及身份
Set_SM2_KeyPair=Psyuunew.Set_SM2_KeyPair
Set_SM2_KeyPair.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p,c_char_p )
Set_SM2_KeyPair.restypes=(c_int)

##返回加密锁的公钥
Get_SM2_PubKey=Psyuunew.Get_SM2_PubKey
Get_SM2_PubKey.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p)
Get_SM2_PubKey.restypes=(c_int)

##对二进制数据进行SM2加密
SM2_EncBuf=Psyuunew.SM2_EncBuf
SM2_EncBuf.argtypes=(c_void_p,c_void_p,c_int ,c_char_p)
SM2_EncBuf.restypes=(c_int)

##对二进制数据进行SM2解密
SM2_DecBuf=Psyuunew.SM2_DecBuf
SM2_DecBuf.argtypes=(c_void_p,c_void_p,c_int ,c_char_p ,c_char_p)
SM2_DecBuf.restypes=(c_int)

##对字符串进行SM2加密
SM2_EncString=Psyuunew. SM2_EncString
SM2_EncString.argtypes=(c_char_p,c_char_p,c_char_p)
SM2_EncString.restypes=(c_int)

##对字符串进行SM2解密
SM2_DecString=Psyuunew.SM2_DecString
SM2_DecString.argtypes=(c_char_p,c_char_p,c_char_p ,c_char_p)
SM2_DecString.restypes=(c_int)

##返回锁的硬件芯片唯一ID
GetChipID=Psyuunew.GetChipID 
GetChipID.argtypes=(c_char_p,c_char_p)
GetChipID.restypes=(c_int)
##以上函数只支持智能芯片的锁


if 'Linux' in platform.system():
	CloseUsbHandle=Psyuunew.CloseUsbHandle
	CloseUsbHandle.argtype=c_char_p
	CloseUsbHandle.restypes=(c_void_p)

def HexStringToByteArrayEx(InString):
    
    mylen=len(InString)
    array_data={}
    in_data=c_byte
    temp=''
    for n in range(0,mylen,2):
        temp=InString[n:2+n]
        temp='0x'+temp
        in_data=int(temp,16)
        array_data[n/2]=(in_data)
    return array_data

def StringToByteArray(InString):
    
    mylen=len(InString)
    array_data={}
    in_data=c_int
    temp=''
    for n in range(0,mylen):
        temp=InString[n:1+n]
        in_data=ord(temp)
        array_data[n]=(in_data)
    array_data[n+1]=0
    return array_data

def ByteArrayToString(InBuf):
    OutString=create_string_buffer('\0'*(len(InBuf)+1))
    for n in range(0,len(InBuf)):
        OutString[n]=chr(InBuf[n])
    return OutString.value
    

def ByteArrayToHexString(in_data,inlen):
    OutString=''
    temp=''
    for n in range(0,inlen):
        temp='%02X' % in_data[n]
        OutString=OutString+temp
    return OutString

def EnCode(InData,Key):
    KeyBuf=HexStringToByteArrayEx(Key)
    OutData=EncBySoft(InData,KeyBuf)	
    return OutData

def DeCode(InData,Key):
    KeyBuf=HexStringToByteArrayEx(Key)
    OutData=DecBySoft(InData,KeyBuf)
    return OutData


def EncBySoft(inb, KeyBuf,pos):
    bufArray=c_uint32*16
    buf=bufArray

    temp_string=''
    cnDelta = 2654435769
    _sum = 0
    a = 0
    b = 0
    c = 0
    d = 0
 
    for n in range(0,4):
        a = (KeyBuf[n] << (n * 8)) | a
        b = (KeyBuf[n + 4] << (n * 8)) | b
        c = (KeyBuf[n + 4 + 4] << (n * 8)) | c
        d = (KeyBuf[n + 4 + 4 + 4] << (n * 8)) | d 
    y = 0
    z = 0

    for n in range(0,4):
        temp = (inb[pos +n])
        y = (temp << (n * 8)) | y
        temp = (inb[pos +n + 4])
        z = (temp << (n * 8)) | z

    n = 32
    while  n > 0:
        _sum = (cnDelta + _sum) & 0xffffffff
        temp=(z << 4) & 0xffffffff
        temp=(temp+a)& 0xffffffff
        temp_1= (z + _sum) & 0xffffffff
        temp_2=((z >> 5) + b)& 0xffffffff
        temp=temp ^ temp_1 ^ temp_2
        y = (y+ temp)& 0xffffffff
        temp=(y << 4)& 0xffffffff
        temp=(temp + c)& 0xffffffff
        temp_1=(y + _sum)& 0xffffffff
        temp_2=((y >> 5) + d)& 0xffffffff
        temp=temp ^ temp_1 ^ temp_2
        z=(z+temp)& 0xffffffff
        n = n - 1

    outb={}
    for n in range(0,4):
        outb [n]= (y >> (n) * 8) & 255
        outb[n + 4] = (z >> (n) * 8) & 255

    return outb

def DecBySoft(inb, KeyBuf,pos):
    bufArray=c_uint32*16
    buf=bufArray
    temp_string=''
    cnDelta = 2654435769
    _sum = 0xC6EF3720
    a = 0
    b = 0
    c = 0
    d = 0
    for n in range(0,4):
        a = (KeyBuf[n] << (n * 8)) | a
        b = (KeyBuf[n + 4] << (n * 8)) | b
        c = (KeyBuf[n + 4 + 4] << (n * 8)) | c
        d = (KeyBuf[n + 4 + 4 + 4] << (n * 8)) | d
    y = 0
    z = 0
    for n in range(0,4):
        temp = (inb[pos +n])
        y = (temp << (n * 8)) | y
        temp = inb[pos +n + 4]
        z = (temp << (n * 8)) | z

    n = 32
    while  n > 0:
        temp=(y << 4)
        temp= ( temp+ c) & 0xffffffff
        temp_1=(y + _sum)& 0xffffffff
        temp_2=((y >> 5) + d)& 0xffffffff
        temp= temp ^ temp_1 ^ temp_2
        z=(z-temp) & 0xffffffff
        #z -= ((y << 4) + c) ^ (y + _sum) ^ ((y >> 5) + d)
        temp=(z << 4)& 0xffffffff
        temp=(temp+a)& 0xffffffff
        temp_1=(z + _sum)& 0xffffffff
        temp_2=((z >> 5) + b)& 0xffffffff
        temp= temp ^ temp_1 ^ temp_2
        y = (y -temp)& 0xffffffff
        _sum = (_sum -cnDelta)& 0xffffffff
        n = n - 1
    
    outb={}
    for n in range(0,4):
        outb[n] = (y >> (n) * 8) & 255
        outb[n + 4] = (z >> (n) * 8) & 255

    return outb

def StrDec(InString,Key):
   OutBuf={}
   mylen=len(InString)/2
   KeyBuf=HexStringToByteArrayEx(Key)
   InBuf=HexStringToByteArrayEx(InString)
   for n in range(0,(mylen-8)+1,8):
        tempBuf=DecBySoft(InBuf,KeyBuf,n)
        for i in range(0,8):
             OutBuf[i+ n] = tempBuf[i]
   if mylen>8:
       for n in range(len(OutBuf),mylen):
            OutBuf[n]=(InBuf[n])
   return ByteArrayToString(OutBuf)


def StrEnc(InString,Key):
    OutBuf={}
    InBuf={}
    temp_Buf=c_char_p(InString)
    mylen=len(InString)+1
    for n in range(0,mylen-1):
        InBuf[n]=ord(temp_Buf.value[n])
    InBuf[n+1]=(0)
    if mylen<8:
            for n in range(mylen,8):
                 InBuf[n]=(0)
            mylen=8
            
    KeyBuf=HexStringToByteArrayEx(Key)
    for n in range(0,(mylen-8)+1,8):
         tempBuf=EncBySoft(InBuf,KeyBuf,n)

         for i in range(0,8):
              OutBuf[i+ n] = tempBuf[i]
    if mylen>8:
       for n in range(len(OutBuf),mylen-1):
            OutBuf[n]=(InBuf[n])
       OutBuf[n+1]=0
    OutString=ByteArrayToHexString(OutBuf,mylen)
    return OutString

#使用增强算法一检查是否存在对应的加密�?
def CheckKeyByEncstring():
    DevicePath=create_string_buffer('\0'*260)
    outstring=''
    EncInString=["3251","15075","23807","10400","2011","7122","25339","15443","31689","21229","9455","24737","28776","28793","31251","30683","1729","14679","7107","15861","21246","6408","20344","19070","22121","13231","12492","12971","6508","6157",  \
"7033","19275","26001","4485","13657","2771","8067","6681","6246","2899","16651","27753","7355","11390","29458","13755","17040","21925","18340","26605","15425","22459","5098","11139","6215","28497","27182","29086","2876","26267",  \
"13275","9730","23001","22377","27512","271","25338","3374","30387","31175","18841","1787","8276","22477","16078","6531","12869","25955","27605","12567","12176","16747","31750","13226","11871","20838","18141","718","20987","21367",  \
"6644","7604","25808","4191","8963","25390","4712","11649","31204","29616","16748","7903","19092","13130","3494","14618","7978","27566","25087","25460","18914","3633","12931","27089","28436","5569","22107","28337","12092","2289",  \
"465","32054","28915","7156","24655","15140","19187","29340","20063","15067","3607","603","13228","27997","28502","5186","31998","13390","20942","26371","13889","5102","12471","28913","17534","1312","10602","16895","16351","26468",  \
"9571","1469","28078","4831","9275","9565","23125","2642","9644","2482","4959","19741","13200","32045","373","18757","3042","11745","25184","28010","27321","20352","25355","23246","29779","23899","22913","14165","16136","31845",  \
"7916","8063","32081","32047","2452","14447","18379","32237","1764","25062","1837","11375","21862","2120","32337","10280","24260","5780","29748","1065","12745","2158","32237","26916","7262","7192","26808","22381","25996","9331",  \
"17390","2292","10112","31490","2825","29515","18817","4583","28578","27045","6650","9699","17270","24276","2166","4186","604","18250","32668","14667","31823","6937","24378","10586","8042","30705","5689","15305","25061","25382",  \
"23712","28793","19484","11179","3484","24045","8840","27663","8566","17223","12226","11398","18328","14920","11911","9442","8333","2388","21421","7829","6141","5482","30769","30383","24244","29742","25389","16358","1179","7650",  \
"13274","1160","12987","16231","27537","10377","1345","11329","6095","27514","1396","28815","7210","2703","17343","790","7263","664","4524","5942","1608","29191","23525","3825","15325","6896","9269","3307","23865","1283",  \
"7045","9827","12951","16274","23518","13629","13903","17296","17005","18939","16093","30094","27000","15807","18650","18367","17005","25674","24832","31733","20435","24063","11817","1442","32597","2528","6992","3031","9151","6030",  \
"8589","2887","3832","14668","12828","6211","19466","30203","16469","16574","31009","6943","27572","3658","16774","20183","18898","10264","30627","16872","20585","5371","20227","434","24403","7525","13902","27191","27274","19814",  \
"20816","14362","17449","5812","4850","15005","1641","4765","30525","9634","7587","25620","23901","938","29266","14765","412","18391","13074","28568","5986","32748","16026","20904","826","9804","11717","32079","13519","5110",  \
"32141","25502","8425","4751","22796","27464","23412","3671","894","12958","20856","26671","25144","29075","8994","26524","9914","31672","7609","19647","6298","25153","21928","602","32658","13822","24697","28621","11647","26977",  \
"11991","27421","10328","21118","1675","19178","29752","19716","7294","6263","32089","31815","20156","24997","8727","11578","32365","11000","23784","22636","2526","400","3690","17426","26230","11567","26451","17916","23232","568",  \
"29312","9628","22631","21420","16107","7686","30259","1327","10668","32745","2577","15616","18431","29593","25351","13828","28988","23304","9026","12731","26847","21448","14859","2632","10369","22794","32204","25707","18908","1442",  \
"26128","394","4299","30206","25983","12707","5446","18997","25573","25946","3432","18422","22571","24561","14188","7315","603","2378","25514","16127"]
    EncOutString=["0CB0272CB9B82C09","7315021795F7EE43","B08CE43E50611EF4","E16540F5990AA972","F5B7EC0C868B90A0","CF95E994246BEEB6","8D8B8986D76E9C6B","CE2882367AAE7DFF","3094943446ED585F","2CF53AE0B201F3B0","8522AEDC64ED48E4","206E77306FD7CD7E","2F1D69BE73A44708","D6B53FFA30EE4591","A04AC6FC474C5BB5","401B1C670B309CD5","8530DE0B7D9B13B9","D2305C7BA26CB79C","12B832D8EA7C365B","629A8BE8CADFEDE8","A757FAA37B36A7CA","2776AA527EAA912E","BCD898D6C1227D08","E4668E07ECCA506E","BD4CB84509815983","9559DB55EEC3769D","FFC5B1A0B791BF1B","729E09E6F3507426","D51A0552625AD0B0","BFD1F4F7A2D819D7",  \
"98D2FD510FEBF943","3D401A76D216BC85","1A8165E92FCC02F5","3CF0A3435E4237F0","196A6CA4157EDB2A","1E57A2745DB9B76E","FD3EBF32C8F487B7","B436B5196C97CC14","E202C0056A850261","B0A22B11313CF31A","9CAD314B28EBBAD8","873F445D63351425","3054A037CF4BD177","E3B5C55D61A6C99A","8869BC5E018C6BB5","82960ADBA8B0E8FB","9427D7F99E20E24F","1243F6CDA82C56B0","07800B3449C48DEB","862F48E153C57B51","4761A1260EB4DC95","41AFD971A94926EF","46CF1ECD4E01EB84","44F673AB12582B7C","37591B251AFD4F5A","A531205245ED9796","A04B96C6B875A3A6","8E41F04DA15870E1","63CD597177A75221","9E4F71E297F383E9",  \
"599066CE049F060B","FA8EA96045AC2083","BCA14D17F4D1892C","828198326195216C","90BA8FBFAEDE3B7C","101557F86610D902","DD97C00B72A7EAF1","48F533054685290B","A10481C58AB5A439","6912179945FD6D65","106D4FD6880F94BC","10B8F18E9F9F324C","F3E4803ACF3AA6B7","2F2A866F448A5FC2","474666CF4D4AAB96","01524629918F95B8","A0E59AF98B7F8481","8F21724255E93FCE","93B1C6A96E601D54","05AF08FB90C5C553","D13B1DEF3971D1EB","079E7EA901AFAF8E","6F41300657FDC5B5","4A5DC4F2006464D6","C5F6439E863573C1","CF8319C937D64B06","144994D4ACEA5E7F","DB2CB282E6AA9BC5","73CCEC99BE4AC4CF","E9BB721B9394E597",  \
"BB18A548C07A7752","FC7C7459F19FC66D","58BA3E71BB7B5ABC","2A2CCFB0A80CEDA0","A08B43C39E327A2E","CD60506539448C20","7224B22E5BB2B9EB","5477584CD0E4FC91","6008AEC1C8B32E8E","7FF28358EF09D925","D428E43F44738E40","A7F68F4277F02FD9","D72A807127CB76B1","5C30B560D224E983","5B0924A233C099E1","ABBB19CF0D536CC0","04C83C9C7960FC45","9C25B5C642692433","D4EAC61A315E5D52","BE9BDD6383127173","E4E24443206596F6","EF18ABD7AC87217E","5BE9C735BC43CEA1","70258AD8237646A3","4CF979AFC0B5340D","7278AB3AFC1E2CA6","6CFEBEFFE7650815","99875CAB4CFE4133","3B6AC7AAA9F861A0","B60A9982EA6671B1",  \
"26047B08510568A4","4CCC5DABD81E58BC","C5C571D1BAE024F3","CAD9750BC26DD235","FF38F33D00F0FD9F","7FED4502FA3962BA","1EAAF895DC0ABE21","F293C50E40A1ACA0","E2AA39EA50339098","9AA345AEB523ACCD","6AA0B20EC5B05550","5B0970C9C1F5ED1B","51015C71873BBEFD","8F688025E5C92F59","C70AF806C7652024","DE8D344D00F66343","4B6223450B06ACF1","BFDACBAD57058289","224C39B6E96D5A66","D4FA52E66E4F0EC8","FDAFFE82C4D41464","E0F77EC4C741E65B","5B64A2BEF4A1BDD2","7121D96E954ECFA1","6B86485C9C661E94","6D432ED64A3C051A","E8BFE2D725C872E4","49178130327B4A57","150A66581DB7443A","8EE3BA0583DE9C68",  \
"2F730EC0DC962132","27453EE96FEE7DB3","10EE9BB12255B7FD","7B62CEF4464193E0","6FCE2AAE5BE8B1D7","D3B8E12BC66BF7F5","58C486B3492DD89E","77B06B0E91A194B5","CCA367978C0C0868","BD8A069634036FCA","EAB49CEB1FF72F79","D11426514458D27D","21DC831144FC12C2","FF59344D022C9293","9F59FF751E383E6E","C15990651CA99402","EBEAAEAB67B8D629","9A49AE33D75996C6","7468A3013183F22F","9DED1145476EBA4F","792EB3D840866B23","F2D568ECD362583F","31984D71CC347690","724F3F8BBB757C99","F6BB6EB1A6D801C6","8DF02ABACAE4FB63","C40BAFDFE072638D","B2D168D76F98B0FB","206C7F2E02C22C3B","5D8352C987E5502A",  \
"6AA2EFFADE035CE2","0E63FA8D79A4A02C","0F99ED6A0C206D58","907FC5430908AF1F","563F7583283DDCEE","D6CE43EB8D48A5F2","BBB9FB5ED362A493","8CDEFAFD9A19DD44","8D19639BC8001F54","054050B6CA4CC5CB","D6312520D97C1202","376F10A3378AD4B7","6651BECC22C404A8","AE762B3238079E84","C6E6BA4ED098EBAB","15B7404A57C80419","0E4A3ED562C1F91B","67A60BCEC1E7743E","CD8C2D9A9F35C089","47098509CD2497CF","03EA62BDC999E415","2AF1E9415C5A3BA6","8CDEFAFD9A19DD44","F0430567E91F7709","376AF8F8018374EF","AD5EE0BFD68220FE","4FA0832ED836E855","FF6A60088B19BC28","1FFFBFD7C2CA829C","AF242ED268353DAA",  \
"DAF5B8D367864D6D","52EAAB97D7E06002","D4F540F2D0A7E531","42F61EA0BCC420A2","69AE6BF1DC7346F5","5737DF5CF8ECA7E7","8C00B4B3F599F890","73947D0E12B15132","035666680C49E6B2","46A6C1319B279E65","20307EFACC456B7F","9E86D6B64F325B9D","36288239740DBCDE","2190949A37006A4F","6F84DEEF68C655C4","5C5D3B3DD3883330","6D83602C09A04C0A","2EB3B02186FB5D3E","7B4DA5D710EFE2E5","C691A2CA83BA953D","0EB3404F48413F21","8E56A1EC9C40A4BE","D20B4020417B30D5","5A84A057D5555C53","335F3D23FBC0FEE0","66F4F01BA571AA18","51BA19278B80F8C6","28213D819C332E1D","010070051FBAB3A4","254F7C0FAE93B6BF",  \
"528FD9E980A80A9F","D6B53FFA30EE4591","AB35DAE99EBF8CEB","2D6E207FEF04D64B","02DE6EFB4E2A8854","64DB8765BFB80E28","E12C8DB82481B38E","6F07EB5B364FAD30","98FE8A5A47ACC5F8","4174152278E3ADEE","3E16869A2A762EB7","68F58970701BE821","F7903D7DABAF4A7E","DAB573CC8ADB4738","2CDE66152A119A59","AA840A4614DD0878","AA5D07A2D187A858","D517B20D46A854CA","416690F74F8DFED2","760A6135FB6FF848","4ACBC8C54B0F486F","4E2634DBE47F98F8","C017A96523A9E388","3723BE1F789B8BEE","3AED338C23F502D1","598DB74FDA15F71A","656FD33109B0E84F","8C45B68480FE2BEE","6861B78D09BAEF58","582BA737CCA212E9",  \
"8E852558DC155B31","166320934A877A88","1B26EF01FD4E0EFB","9C6EECFF76E606AE","DAD0CD55CDC589A3","DC8AC73566AFD349","F4B77E8700CDDB4B","E825EC9F0D5E4A11","B4D3B25EB1522B2A","94DB92FD3A059A35","68121C3D62AAFC06","B646F1C792BD04B6","87F038013B9D9C4F","8DD8EC31612EE428","106E2A282972FFE3","277C1896D480C4E9","8D6C0A2A7AD1F0D6","73E317924056AA2A","E5BF2481133291FC","DDEF13F1133B04CF","A52FD9FBE9426A7C","0E991C423B20BA30","5D39865C778929E9","4B7F74D0988CB105","0B20E42FEFC87A86","178051FF81539C5F","21E7BAF53737C3E0","6EF11BA5FBF885DA","2BEC7FFCCA462BB2","5FC513074B5DF69E",  \
"EB7D198DCD3D30E4","CF5281B57A81F4B2","6E663E407FF03D16","4DC77679AB96B102","B9A2F83EAAF34E52","99BBFDBBC16D766B","3ABDC4118184D2D7","BA9FD2D370B592F7","F2D6D35BDF2EC314","EE6825516040F7CB","44DB5853064D667A","2F4D3566C8E5724C","7B57D53B6580102C","39BF0F16CEA425D4","2740AB37C7245906","FC22A6BD0580DFCE","F2D6D35BDF2EC314","DFA3E7C673B26F85","830EA6F2E163AE2D","7A58E3661C9A8B34","13330225052360F7","B4D6A0AA9B022614","72958701FF7E96A1","A648FE2017F86D63","CDE72F7015C24F2E","8363385EA2BE6540","6159C76A16DFD620","478C4CC53446D4DE","E1E73A6AE6F17E14","5474D2A85A130B8A",  \
"D9C1757F10939668","97833B3F6B334567","F33E24E9D1CF2879","16A069655F8D485C","99F2CC48F807BE8A","863C2A9FC9C054EC","D9DB5C075B986AD8","97DD409A02E6251F","77C0D39EAC049A37","CE69BF0CB26B8011","F57D066C149A21F7","FC3673D5F480A245","684978DF800F8432","AC54A663B6876569","2913891E1D75A068","3254C50948E91A5E","43EFFB431EF90538","7D85BB33BD62C565","3887EBCFFDE461D1","CC12D35E26389EA4","DD56DD2F03C36703","62DB842A0A90C724","A0DBFA4705EF42A9","2A8FC92E6BB96764","303694C6EB2B7EBA","7F2C9061EDA8A91F","8212432D8021E034","E06F75E44DF571B2","1168479DE207282D","4742E953A626AD16",  \
"5E6CB32BA0ADF039","D13335DE84A9008F","5B2CC82A134ECA7A","860BAEFF2614020B","69928D282580BFEB","BA6B114D7FDCC87C","8179F17295D41660","F076DF0367C1CCE0","8F4AEC4BADF5E3F5","0D6CD761F2D95632","467C0858F95610FB","46C7D2B58B6A8985","9CF80A28B281C15B","32BB8F92D441A634","9C39321722207391","1F8491156A44A5BA","9E74A579211C7534","2EBC7F4F9A222C43","70450185282F08DC","D1DDD6F7BBBAFB54","041C3A1B62708371","CD4511B18FD71121","0E0167F1D004969A","E0E10827926AE684","6AF9A54400A27D03","8EEA2E50345651D4","B997A2957E478E05","E3B978FD907C591F","CA6D471B2280B4D0","912D22557CBD3B0A",  \
"C5EBBE9565FBC5E2","960868E0ED1CADE9","DB5A7D2AC51BD6F9","1B044908B572E699","908190DE10D1494A","A19AEB448B6D99E4","77968D39B2BB13FD","800AA84AE2A1D0C8","B5301165864EAB61","42F7361CD3F6ECC8","D49A9761617537AB","83390792A9F215F7","A3B332ED88891936","717365D227664773","CF607BCD63AB1040","2A33F67CBDCA18F0","95F95A8A4356D321","A1F6789260011DE0","E9063D35852A7DD6","876BF9E8AB59F98A","4147342BD099444C","48B9B7AB609A9B5A","4CBD4EA6BED2AC83","CD4B361511E73BE1","BB2C43950648EEFB","412DBB411DC15923","0C053B0C7986E0A5","FFD60D9AC838AFEF","23C8315385D4F052","4FA6BB0A7209889C",  \
"2480DF58AFAF18EC","4D8AA0B0AF1E5739","43BA090CD315D45B","2D8D21BDAF1C31B5","F76C54744D42FF2C","11CA8C485F89F872","0A115973A94D87CE","BD60C09FA1C850AE","D6C913D846B761C4","1C56E07AD5F8F89F","AD690029FC909C2A","0222322391E5F0BD","BD83A2348C3AA6C1","FBA1FDA80D70B520","7163A7868B1AD7BC","84BFDDE1F48C0E35","8B613BB685010165","DC520C7691E4DDEB","5CAB7E9D4024A95F","A790EE9D085F499B","8D363EED08BDE6E4","EB1263F0B0DEE8D5","76B7C8EF8830C9B5","405DFF291CAE1528","6CBD6112EC0555CA","C384A2274C15D6E1","C4A9188EC2EC505B","697DE7F702B80CDB","9C93DED1F24300B5","D80737D802CEDD57",  \
"63086D40706B62D8","638AC09D147F6170","E9A541252A52D08A","24348A0EE436B470","D4F532E2F23A47D0","4C74DF9CB54FFB42","036D43A6E1F0F03D","20ED19A2BF201148","F940F3B0D868FA01","99FAEAF8EB8D2768","0D3A95AA7396191E","BE9FB0F80127DAA8","E6724F3D0B15551E","DC101D957C0DA330","DC82C25E916E71BE","8A045A58A3BD881A","3D76A733398A7F50","E5FC136B7E896B7C","072B1CB18FA26C8B","23D8D921E0B0BF29","93D3643042EADED4","98CC5ACF00A056A2","DE152FCB3BD47504","6791F90DD37AC8EF","736CD4C6FC464C0D","85BB0FC8CA5FCFE0","C7B1EA11ACB2CC21","B6A31394E35F1650","9ABCA01C15AD1C7D","A648FE2017F86D63",  \
"FCE79C41FEA50FF9","BB19EAB38E9121E1","092D366C8C04CB19","6C175BFE0AADD5B5","337A67BC1CE4B697","FF7041ECEBE5F5C7","DEEA899F4EFE59E7","4A4789A2302E3C19","17FB79BFFF8EF11F","4699DB0CFCD447E1","F38D32A62831B183","C5FEFC02A9120E11","1DCE76B054C33B38","8399D0AB423FA9D1","0CE70832C9A2E757","A6B3D517F8B8E4A4","5B0970C9C1F5ED1B","91C2CFFC5831E30D","32E71FF3ACB06FBD","FBB986AF048A34D2"]
#@NoUseNewKeyEx return 1 #如果没有使用这个功能，直接返�?
#@NoSupNewKeyEx return 2 #果该锁不支持这个功能，直接返�?
    myrnd=random.randint(1, (500 -1 ))
    mylen = len(EncInString[myrnd])+1
    if  mylen < 8 :
        mylen = 8
    outstring = create_string_buffer('\0'*(mylen* 2+1))#//注意，这里要�?一个长度，用于储存结束学符�?
    for n in range(0,255):
         ret=FindPort(n,DevicePath);
         if ret!=0:
             return ret
         ret=EncString(EncInString[myrnd], outstring,DevicePath)
         if outstring.value.lower()==EncOutString[myrnd].lower():
             return 0
    return -92



#//使用带长度的方法从指定的地址读取字符�?
def ReadStringEx(addr,DevicePath):
    InArray=c_ubyte*1
    blen = InArray(0)
#//先从地址0读到以前写入的字符串的长�?
    ret = YReadEx(blen, addr, 1, 'E62493CA', '812E861A', DevicePath)
    if ret != 0 :
        return ''
    outstring=create_string_buffer('\0'*blen[0])
#再从地址1读取指定长度的字符串
    ret = YReadString(outstring, addr+1, blen[0], 'E62493CA', '812E861A', DevicePath)
    if ret!=0:
        return ''
    return outstring.value


#//使用从储存器读取相应数据的方式检查是否存在指定的加密�?
def CheckKeyByReadEprom():
    DevicePath=create_string_buffer('\0'*260)
#@NoUseCode_data return 1 #如果没有使用这个功能，直接返�?
    for n in range(0,255):
        ret=FindPort(n,DevicePath)
        if ret!=0 :
              return ret
        outstring=ReadStringEx(0,DevicePath)
        if(outstring=='123456789'):
            return 0
    return -92