'''
import os  
# scanning the available Wi-Fi networks  
os.system('cmd /c "netsh wlan show networks"')  
# providing the Wi-Fi name as input  
router_name = input('Input Name/SSID of the Wi-Fi network we would like to connect: ')  
# connecting to the provided Wi-Fi network  
os.system(f"'cmd /c "netsh wlan connect name = {router_name}"')  
print("If the system is not connected yet, try reconnecting to an earlier connected SSID!")
'''

import os  
# defining the function to establish a new connection  
def create_new_connection(name, SSID, password):  
    config = """<?xml version=\"1.0\"?>  
<WLANProfile xmlns = "http://www.microsoft.com/networking/WLAN/profile/v1">  
    <name>""" + name + """</name>  
    <SSIDConfig>  
        <SSID>  
            <name>""" + SSID + """</name>  
        </SSID>  
    </SSIDConfig>  
    <connectionType> ESS </connectionType>  
    <connectionMode> auto </connectionMode>  
    <MSM>  
        <security>  
            <authEncryption>  
                <authentication> WPA2PSK </authentication>  
                <encryption> AES </encryption>  
                <useOneX> false </useOneX>  
            </authEncryption>  
            <sharedKey>  
                <keyType> passPhrase </keyType>  
                <protected> false </protected>  
                <keyMaterial>""" + password + """</keyMaterial>  
            </sharedKey>  
        </security>  
    </MSM>  
</WLANProfile>"""  
    wlan_command = "netsh wlan add profile filename =\"" + name + ".xml\"" + " interface = Wi-Fi"  
    with open(name + ".xml", 'w') as file:  
        file.write(config)  
    os.system(wlan_command)  
# defining function to connect to a network  
def wlan_connect(name, SSID):  
    wlan_command = "netsh wlan connect name =\"" + name + "\" ssid =\"" + SSID + "\" interface = Wi-Fi"  
    os.system(wlan_command)  
# defining function to display avavilabe Wi-Fi networks     
def display_available_networks():  
    wlan_command = "netsh wlan show networks interface = Wi-Fi"  
    os.system(wlan_command)  
# displaying the available netwroks  
display_available_networks()  
# inputing the Wi-Fi name and password  
name = input("Enter the Name of Wi-Fi: ")  
password = input("Enter the Password: ")   
# establishing a new connection  
create_new_connection(name, name, password)  
# connecting to the Wi-Fi network  
wlan_connect(name, name)  
print("If the system is not connected to this network, try connecting with the correct password!") 
