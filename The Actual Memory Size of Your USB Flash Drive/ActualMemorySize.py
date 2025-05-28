def ms_USB_flash(ms: str):
    ams = float(ms[0:-2]) #actual memory size
    if ('GB' in ms) & (ams>=1.08): #ams for ms greater than 1.08GB still 1GB or greater
        ams = ams*.93
        return f'{ams:2.2f}'.rstrip('0').rstrip('.') + 'GB' #rstrip removes characters at the end of a string
    elif 'GB' in ms:
        ams = ams*.93*1e3
        return f'{ams:2.0f}MB'
    else:
        ams = ams*.93
        return f'{ams:2.0f}MB'
    
print(ms_USB_flash('500GB'))
print(ms_USB_flash('20GB'))
print(ms_USB_flash('1.09GB'))
print(ms_USB_flash('1.08GB'))
print(ms_USB_flash('1.07GB'))
print(ms_USB_flash('512MB'))