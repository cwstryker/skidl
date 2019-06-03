from skidl import SKIDL, TEMPLATE, Part, Pin, SchLib

SKIDL_lib_version = '0.0.1'

powerint = SchLib(tool=SKIDL).add_parts(*[
        Part(name='CAP002DG',dest=TEMPLATE,tool=SKIDL,keywords='CapZero Automatic Capacitor Discarger 1000V 5000nF',description='CapZero Automatic Capacitor Discarger, Vdss 1000V, Cmax 5000nF, SO8',ref_prefix='U',num_units=1,fplist=['SO-8*'],do_erc=True,aliases=['CAP003DG', 'CAP004DG', 'CAP005DG', 'CAP006DG', 'CAP007DG', 'CAP008DG', 'CAP009DG', 'CAP012DG', 'CAP013DG', 'CAP014DG', 'CAP015DG', 'CAP016DG', 'CAP017DG', 'CAP018DG', 'CAP019DG'],pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LNK302D',dest=TEMPLATE,tool=SKIDL,keywords='Lowest Component Count, Energy-Efficient Off-Line Switcher IC',description='LinkSwitch-TN Family, 360mA Output Current, SO-8C',ref_prefix='U',num_units=1,fplist=['SO-8B*'],do_erc=True,aliases=['LNK304D', 'LNK305D', 'LNK306D'],pins=[
            Pin(num='1',name='BP',do_erc=True),
            Pin(num='2',name='FB',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK302G',dest=TEMPLATE,tool=SKIDL,keywords='Lowest Component Count, Energy-Efficient Off-Line Switcher IC',description='LinkSwitch-TN Family, 360mA Output Current, SMD-8B',ref_prefix='U',num_units=1,fplist=['SMD-8B*'],do_erc=True,aliases=['LNK304G', 'LNK305G', 'LNK306G'],pins=[
            Pin(num='1',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='2',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='3',name='BP',do_erc=True),
            Pin(num='4',name='FB',do_erc=True),
            Pin(num='5',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK302P',dest=TEMPLATE,tool=SKIDL,keywords='Lowest Component Count, Energy-Efficient Off-Line Switcher IC',description='LinkSwitch-TN Family, 360mA Output Current, DIP-8B',ref_prefix='U',num_units=1,fplist=['PDIP-8B*'],do_erc=True,aliases=['LNK304P', 'LNK305P', 'LNK306P'],pins=[
            Pin(num='1',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='2',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='3',name='BP',do_erc=True),
            Pin(num='4',name='FB',do_erc=True),
            Pin(num='5',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK362D',dest=TEMPLATE,tool=SKIDL,keywords='Energy Effi cient, Low Power Off-Line Switcher IC',description='LinkSwitch-XT Family, 6W Output Power, SO-8C',ref_prefix='U',num_units=1,fplist=['SO-8C*'],do_erc=True,aliases=['LNK363D', 'LNK364D'],pins=[
            Pin(num='1',name='BP',do_erc=True),
            Pin(num='2',name='FB',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK362G',dest=TEMPLATE,tool=SKIDL,keywords='Energy Effi cient, Low Power Off-Line Switcher IC',description='LinkSwitch-XT Family, 6W Output Power, SMD-8B',ref_prefix='U',num_units=1,fplist=['SMD-8B*'],do_erc=True,aliases=['LNK363G', 'LNK364G'],pins=[
            Pin(num='1',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='2',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='3',name='BP',do_erc=True),
            Pin(num='4',name='FB',do_erc=True),
            Pin(num='5',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK362P',dest=TEMPLATE,tool=SKIDL,keywords='Energy Effi cient, Low Power Off-Line Switcher IC',description='LinkSwitch-XT Family, 6W Output Power, DIP-8B',ref_prefix='U',num_units=1,fplist=['PDIP-8B*'],do_erc=True,aliases=['LNK363P', 'LNK364P'],pins=[
            Pin(num='1',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='2',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='3',name='BP',do_erc=True),
            Pin(num='4',name='FB',do_erc=True),
            Pin(num='5',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK403EG',dest=TEMPLATE,tool=SKIDL,keywords='LED Driver IC, Single-Stage PFC and Primary-Side Constant Current Control',description='LinkSwitch-PH Family, 78W Output Power, eSIP-7C',ref_prefix='U',num_units=1,fplist=['sSIP-7C*'],do_erc=True,aliases=['LNK404EG', 'LNK405EG', 'LNK406EG', 'LNK407EG', 'LNK408EG', 'LNK409EG', 'LNK410EG', 'LNK413EG', 'LNK414EG', 'LNK415EG', 'LNK416EG', 'LNK417EG', 'LNK418EG', 'LNK419EG', 'LNK420EG'],pins=[
            Pin(num='1',name='R',do_erc=True),
            Pin(num='2',name='V',do_erc=True),
            Pin(num='3',name='FB',do_erc=True),
            Pin(num='4',name='BP',do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='D',func=Pin.OPENCOLL,do_erc=True)]),
        Part(name='LNK403LG',dest=TEMPLATE,tool=SKIDL,keywords='LED Driver IC, Single-Stage PFC and Primary-Side Constant Current Control',description='LinkSwitch-PH Family, 78W Output Power, eSIP-7F',ref_prefix='U',num_units=1,fplist=['eSIP-7F*'],do_erc=True,aliases=['LNK404LG', 'LNK405LG', 'LNK406LG', 'LNK407LG', 'LNK408LG', 'LNK409LG', 'LNK410LG', 'LNK413LG', 'LNK414LG', 'LNK415LG', 'LNK416LG', 'LNK417LG', 'LNK418LG', 'LNK419LG', 'LNK420LG'],pins=[
            Pin(num='1',name='R',do_erc=True),
            Pin(num='2',name='V',do_erc=True),
            Pin(num='3',name='FB',do_erc=True),
            Pin(num='4',name='BP',do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='D',func=Pin.OPENCOLL,do_erc=True)]),
        Part(name='LNK454D',dest=TEMPLATE,tool=SKIDL,keywords='LED Driver IC with TRIAC Dimming, Single-Stage PFC and Constant Current Control for Non-Isolated Applications',description='LinkSwitch-PL Family, 8W Output Power, SO-8C',ref_prefix='U',num_units=1,fplist=['SO-8C*'],do_erc=True,aliases=['LNK456D', 'LNK457D'],pins=[
            Pin(num='1',name='FB',do_erc=True),
            Pin(num='2',name='BP',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENCOLL,do_erc=True)]),
        Part(name='LNK457K',dest=TEMPLATE,tool=SKIDL,keywords='LED Driver IC with TRIAC Dimming, Single-Stage PFC and Constant Current Control for Non-Isolated Applications',description='LinkSwitch-PL Family, 16W Output Power, eSOP-12B',ref_prefix='U',num_units=1,fplist=['eSOP-12B*'],do_erc=True,aliases=['LNK458K', 'LNK460K'],pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='FB',do_erc=True),
            Pin(num='3',name='BP',do_erc=True),
            Pin(num='4',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='6',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='9',name='S',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='10',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='11',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='12',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='13',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK457V',dest=TEMPLATE,tool=SKIDL,keywords='LED Driver IC with TRIAC Dimming, Single-Stage PFC and Constant Current Control for Non-Isolated Applications',description='LinkSwitch-PL Family, 8W Output Power, eDIP-12B',ref_prefix='U',num_units=1,fplist=['eDIP-12B*'],do_erc=True,aliases=['LNK458V', 'LNK460V'],pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='FB',do_erc=True),
            Pin(num='3',name='BP',do_erc=True),
            Pin(num='4',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='6',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='9',name='S',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='10',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='11',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='12',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK562D',dest=TEMPLATE,tool=SKIDL,keywords='Energy Efficient Off-Line Switcher IC for Linear Transformer Replacement',description='LinkSwitch-LP Family, 3W Output Power, SO-8C',ref_prefix='U',num_units=1,fplist=['SO-8C*'],do_erc=True,aliases=['LNK563D', 'LNK564D'],pins=[
            Pin(num='1',name='BP',do_erc=True),
            Pin(num='2',name='FB',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK562G',dest=TEMPLATE,tool=SKIDL,keywords='Energy Efficient Off-Line Switcher IC for Linear Transformer Replacement',description='LinkSwitch-LP Family, 3W Output Power, SMD-8B',ref_prefix='U',num_units=1,fplist=['SMD-8B*'],do_erc=True,aliases=['LNK563G', 'LNK564G'],pins=[
            Pin(num='1',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='2',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='3',name='BP',do_erc=True),
            Pin(num='4',name='FB',do_erc=True),
            Pin(num='5',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK562P',dest=TEMPLATE,tool=SKIDL,keywords='Energy Efficient Off-Line Switcher IC for Linear Transformer Replacement',description='LinkSwitch-LP Family, 3W Output Power, DIP-8B',ref_prefix='U',num_units=1,fplist=['PDIP-8B*'],do_erc=True,aliases=['LNK563P', 'LNK564P'],pins=[
            Pin(num='1',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='2',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='3',name='BP',do_erc=True),
            Pin(num='4',name='FB',do_erc=True),
            Pin(num='5',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK603DG',dest=TEMPLATE,tool=SKIDL,keywords='Energy-Efficient, Accurate CV/CC Switcher for Adapters and Chargers',description='LinkSwitch-II Family, 6.1W Output Power, SO-8C',ref_prefix='U',num_units=1,fplist=['SO-8C*'],do_erc=True,aliases=['LNK604DG', 'LNK605DG', 'LNK606DG', 'LNK613DG', 'LNK614DG', 'LNK615DG', 'LNK616DG'],pins=[
            Pin(num='1',name='FB',do_erc=True),
            Pin(num='2',name='BP/M',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK603PG',dest=TEMPLATE,tool=SKIDL,keywords='Energy-Efficient, Accurate CV/CC Switcher for Adapters and Chargers',description='LinkSwitch-II Family, 6.1W Output Power, DIP-8C',ref_prefix='U',num_units=1,fplist=['PDIP-8C*'],do_erc=True,aliases=['LNK604PG', 'LNK605PG', 'LNK606PG', 'LNK613PG', 'LNK614PG', 'LNK615PG', 'LNK616PG'],pins=[
            Pin(num='1',name='FB',do_erc=True),
            Pin(num='2',name='BP/M',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK606GG',dest=TEMPLATE,tool=SKIDL,keywords='Energy-Efficient, Accurate CV/CC Switcher for Adapters and Chargers',description='LinkSwitch-II Family, 6.1W Output Power, SMD-8C',ref_prefix='U',num_units=1,fplist=['SMD-8C*'],do_erc=True,aliases=['LNK616GG'],pins=[
            Pin(num='1',name='FB',do_erc=True),
            Pin(num='2',name='BP/M',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK623DG',dest=TEMPLATE,tool=SKIDL,keywords='Energy-Efficient, Off-line Switcher with Accurate Primary-side Constant-Voltage Control',description='LinkSwitch-CV Family, 10W Output Power, SO-8C',ref_prefix='U',num_units=1,fplist=['SO-8C*'],do_erc=True,aliases=['LNK624DG', 'LNK625DG', 'LNK626DG'],pins=[
            Pin(num='1',name='FB',do_erc=True),
            Pin(num='2',name='BP',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK623PG',dest=TEMPLATE,tool=SKIDL,keywords='Energy-Efficient, Off-line Switcher with Accurate Primary-side Constant-Voltage Control',description='LinkSwitch-CV Family, 10W Output Power, DIP-8C',ref_prefix='U',num_units=1,fplist=['PDIP-8C*'],do_erc=True,aliases=['LNK624PG', 'LNK625PG', 'LNK626PG'],pins=[
            Pin(num='1',name='FB',do_erc=True),
            Pin(num='2',name='BP',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='LNK632DG',dest=TEMPLATE,tool=SKIDL,keywords='Energy-Efficient, Accurate CV Switcher With CC Control for Adapters and Chargers',description='LinkSwitch-II Family, 3.1W Output Power, SO-8C',ref_prefix='U',num_units=1,fplist=['SO-8C*'],do_erc=True,pins=[
            Pin(num='1',name='FB',do_erc=True),
            Pin(num='2',name='BP/M',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TNY263G',dest=TEMPLATE,tool=SKIDL,keywords='Enhanced, Energy Efficient, Low Power Off-line Switcher',description='TinySwitch-II Family, 15W Output Power, SMD-8B',ref_prefix='U',num_units=1,fplist=['SMD-8B*'],do_erc=True,aliases=['TNY264G', 'TNY265G', 'TNY266G', 'TNY267G', 'TNY268G'],pins=[
            Pin(num='1',name='BP',do_erc=True),
            Pin(num='2',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='3',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='4',name='EN/UV',do_erc=True),
            Pin(num='5',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TNY263P',dest=TEMPLATE,tool=SKIDL,keywords='Enhanced, Energy Efficient, Low Power Off-line Switcher',description='TinySwitch-II Family, 15W Output Power, DIP-8B',ref_prefix='U',num_units=1,fplist=['PDIP-8B*'],do_erc=True,aliases=['TNY264P', 'TNY265P', 'TNY266P', 'TNY267P', 'TNY268P'],pins=[
            Pin(num='1',name='BP',do_erc=True),
            Pin(num='2',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='3',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='4',name='EN/UV',do_erc=True),
            Pin(num='5',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TNY274G',dest=TEMPLATE,tool=SKIDL,keywords='Energy-Efficient, Off-Line Switcher With Enhanced Flexibility and Extended Power Range',description='TinySwitch-III Family, 28.5W Output Power, SMD-8C',ref_prefix='U',num_units=1,fplist=['SMD-8C*'],do_erc=True,aliases=['TNY275G', 'TNY276G', 'TNY277G', 'TNY278G', 'TNY279G', 'TNY280G'],pins=[
            Pin(num='1',name='EN/UV',do_erc=True),
            Pin(num='2',name='BP/M',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TNY274P',dest=TEMPLATE,tool=SKIDL,keywords='Energy-Efficient, Off-Line Switcher With Enhanced Flexibility and Extended Power Range',description='TinySwitch-III Family, 28.5W Output Power, DIP-8C',ref_prefix='U',num_units=1,fplist=['PDIP-8C*'],do_erc=True,aliases=['TNY275P', 'TNY276P', 'TNY277P', 'TNY278P', 'TNY279P', 'TNY280P'],pins=[
            Pin(num='1',name='EN/UV',do_erc=True),
            Pin(num='2',name='BP/M',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TNY284D',dest=TEMPLATE,tool=SKIDL,keywords='Energy-Efficient, Off-Line Switcher With Line Compensated Overload Power',description='TinySwitch-4 Family, 19.5W Output Power, SO-8C',ref_prefix='U',num_units=1,fplist=['SO-8C*'],do_erc=True,aliases=['TNY285D', 'TNY286D', 'TNY287D', 'TNY288D'],pins=[
            Pin(num='1',name='EN/UV',do_erc=True),
            Pin(num='2',name='BP/M',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TNY284K',dest=TEMPLATE,tool=SKIDL,keywords='Energy-Efficient, Off-Line Switcher With Line Compensated Overload Power',description='TinySwitch-4 Family, 28.5W Output Power, eSOP-12B',ref_prefix='U',num_units=1,fplist=['eSOP-12B*'],do_erc=True,aliases=['TNY285K', 'TNY286K', 'TNY287K', 'TNY288K', 'TNY289K', 'TNY290K'],pins=[
            Pin(num='1',name='EN/UV',do_erc=True),
            Pin(num='2',name='BP/M',do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='6',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='9',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='10',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='11',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='12',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='13',name='S',func=Pin.OPENCOLL,do_erc=True)]),
        Part(name='TNY284P',dest=TEMPLATE,tool=SKIDL,keywords='Energy-Efficient, Off-Line Switcher With Line Compensated Overload Power',description='TinySwitch-4 Family, 28.5W Output Power, PDIP-8C',ref_prefix='U',num_units=1,fplist=['PDIP-8C*'],do_erc=True,aliases=['TNY285P', 'TNY286P', 'TNY287P', 'TNY288P', 'TNY289P', 'TNY290P'],pins=[
            Pin(num='1',name='EN/UV',do_erc=True),
            Pin(num='2',name='BP/M',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TOP100YN',dest=TEMPLATE,tool=SKIDL,keywords='Three-terminal Off-line PWM Switch',description='TOPSwitch Family, 60W Max Output Power, TO-220',ref_prefix='U',num_units=1,fplist=['TO-220*'],do_erc=True,aliases=['TOP101YN', 'TOP102YN', 'TOP103YN', 'TOP104YN'],pins=[
            Pin(num='1',name='C',do_erc=True),
            Pin(num='2',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='3',name='D',func=Pin.OPENCOLL,do_erc=True)]),
        Part(name='TOP200YAI',dest=TEMPLATE,tool=SKIDL,keywords='Three-terminal Off-line PWM Switch',description='TOPSwitch Family, 42W Max Output Power, TO-220',ref_prefix='U',num_units=1,fplist=['TO-220*'],do_erc=True,aliases=['TOP201YAI', 'TOP202YAI', 'TOP203YAI', 'TOP204YAI', 'TOP214YAI'],pins=[
            Pin(num='1',name='C',do_erc=True),
            Pin(num='2',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='3',name='D',func=Pin.OPENCOLL,do_erc=True)]),
        Part(name='TOP209G',dest=TEMPLATE,tool=SKIDL,keywords='Three-terminal Off-line PWM Switch',description='TOPSwitch Family, 5W Max Output Power, SMD-8',ref_prefix='U',num_units=1,fplist=['SMD-8*'],do_erc=True,aliases=['TOP210G'],pins=[
            Pin(num='1',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='2',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='C',do_erc=True),
            Pin(num='5',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='6',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='7',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TOP209P',dest=TEMPLATE,tool=SKIDL,keywords='Three-terminal Off-line PWM Switch',description='TOPSwitch Family, 5W Max Output Power, DIP-8',ref_prefix='U',num_units=1,fplist=['PDIP-8*'],do_erc=True,aliases=['TOP210PFI'],pins=[
            Pin(num='1',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='2',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='C',do_erc=True),
            Pin(num='5',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='6',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='7',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TOP252EN',dest=TEMPLATE,tool=SKIDL,keywords='Eco Smart Off-Line Switcher, Extendend Power Range',description='TOPSwitch-HX Family, 254W Output Power',ref_prefix='U',num_units=1,fplist=['eSIP-7C*'],do_erc=True,aliases=['TOP252EG', 'TOP253EG', 'TOP253EN', 'TOP254EG', 'TOP254EN', 'TOP255EG', 'TOP255EN', 'TOP256EG', 'TOP256EN', 'TOP257EG', 'TOP257EN', 'TOP258EG', 'TOP258EN', 'TOP259EG', 'TOP259EN', 'TOP260EG', 'TOP260EN', 'TOP261EG', 'TOP261EN', 'TOP262EN'],pins=[
            Pin(num='1',name='V',do_erc=True),
            Pin(num='2',name='X',do_erc=True),
            Pin(num='3',name='C',do_erc=True),
            Pin(num='4',name='F',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='D',func=Pin.OPENCOLL,do_erc=True)]),
        Part(name='TOP252GN',dest=TEMPLATE,tool=SKIDL,keywords='Eco Smart Off-Line Switcher, Extendend Power Range',description='TOPSwitch-HX Family, 35W Output Power',ref_prefix='U',num_units=1,fplist=['SMD-8C*'],do_erc=True,aliases=['TOP253GN', 'TOP254GN', 'TOP255GN', 'TOP256GN', 'TOP257GN', 'TOP258GN'],pins=[
            Pin(num='1',name='M',do_erc=True),
            Pin(num='2',name='C',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TOP252MN',dest=TEMPLATE,tool=SKIDL,keywords='Eco Smart Off-Line Switcher, Extendend Power Range',description='TOPSwitch-HX Family, 35W Output Power',ref_prefix='U',num_units=1,fplist=['SDIP-10C*'],do_erc=True,aliases=['TOP253MN', 'TOP254MN', 'TOP255MN', 'TOP256MN', 'TOP257MN', 'TOP258MN'],pins=[
            Pin(num='1',name='V',do_erc=True),
            Pin(num='2',name='X',do_erc=True),
            Pin(num='3',name='C',do_erc=True),
            Pin(num='5',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='9',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='10',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TOP252PN',dest=TEMPLATE,tool=SKIDL,keywords='Eco Smart Off-Line Switcher, Extendend Power Range',description='TOPSwitch-HX Family, 35W Output Power',ref_prefix='U',num_units=1,fplist=['PDIP-8C*'],do_erc=True,aliases=['TOP253PN', 'TOP254PN', 'TOP255PN', 'TOP256PN', 'TOP257PN', 'TOP258PN'],pins=[
            Pin(num='1',name='M',do_erc=True),
            Pin(num='2',name='C',do_erc=True),
            Pin(num='4',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='6',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TOP254YN',dest=TEMPLATE,tool=SKIDL,keywords='Eco Smart Off-Line Switcher, Extendend Power Range',description='TOPSwitch-HX Family, 148W Output Power',ref_prefix='U',num_units=1,fplist=['TO-220-7C*'],do_erc=True,aliases=['TOP255YN', 'TOP256YN', 'TOP257YN', 'TOP258YN'],pins=[
            Pin(num='1',name='V',do_erc=True),
            Pin(num='2',name='X',do_erc=True),
            Pin(num='3',name='C',do_erc=True),
            Pin(num='4',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='5',name='F',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='D',func=Pin.OPENCOLL,do_erc=True)]),
        Part(name='TOP255LN',dest=TEMPLATE,tool=SKIDL,keywords='Eco Smart Off-Line Switcher, Extendend Power Range',description='TOPSwitch-HX Family, 177W Output Power',ref_prefix='U',num_units=1,fplist=['eSIP-7F*'],do_erc=True,aliases=['TOP256LN', 'TOP257LN', 'TOP258LN', 'TOP259LN', 'TOP260LN', 'TOP261LN', 'TOP262LN'],pins=[
            Pin(num='1',name='V',do_erc=True),
            Pin(num='2',name='X',do_erc=True),
            Pin(num='3',name='C',do_erc=True),
            Pin(num='4',name='F',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='D',func=Pin.OPENCOLL,do_erc=True)]),
        Part(name='TOP259YN',dest=TEMPLATE,tool=SKIDL,keywords='Eco Smart Off-Line Switcher, Extendend Power Range',description='TOPSwitch-HX Family, 254W Output Power',ref_prefix='U',num_units=1,fplist=['TO-220-7C*'],do_erc=True,aliases=['TOP260YN', 'TOP261YN'],pins=[
            Pin(num='1',name='V',do_erc=True),
            Pin(num='2',name='X',do_erc=True),
            Pin(num='3',name='C',do_erc=True),
            Pin(num='4',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='5',name='G',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='D',func=Pin.OPENCOLL,do_erc=True)]),
        Part(name='TOP264EG',dest=TEMPLATE,tool=SKIDL,keywords='Integrated Off-Line Switcher with EcoSmart™ Technology',description='TOPSwitch-JX Family, 177W Output Power, eSIP-7C',ref_prefix='U',num_units=1,fplist=['eSIP-7C*'],do_erc=True,aliases=['TOP265EG', 'TOP266EG', 'TOP267EG', 'TOP268EG', 'TOP269EG', 'TOP270EG', 'TOP271EG'],pins=[
            Pin(num='1',name='V',do_erc=True),
            Pin(num='2',name='X',do_erc=True),
            Pin(num='3',name='C',do_erc=True),
            Pin(num='4',name='F',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='7',name='D',func=Pin.OPENCOLL,do_erc=True)]),
        Part(name='TOP264KG',dest=TEMPLATE,tool=SKIDL,keywords='Integrated Off-Line Switcher with EcoSmart™ Technology',description='TOPSwitch-JX Family, 66W Output Power, eSOP-12B',ref_prefix='U',num_units=1,fplist=['eSOP-12B*'],do_erc=True,aliases=['TOP265KG', 'TOP266KG', 'TOP267KG', 'TOP268KG', 'TOP269KG', 'TOP270KG', 'TOP271KG'],pins=[
            Pin(num='1',name='V',do_erc=True),
            Pin(num='2',name='X',do_erc=True),
            Pin(num='3',name='C',do_erc=True),
            Pin(num='4',name='F',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='9',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='10',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='11',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='12',name='S',func=Pin.OPENEMIT,do_erc=True)]),
        Part(name='TOP264VG',dest=TEMPLATE,tool=SKIDL,keywords='Integrated Off-Line Switcher with EcoSmart™ Technology',description='TOPSwitch-JX Family, 177W Output Power, eDIP-12B',ref_prefix='U',num_units=1,fplist=['eDIP-12*'],do_erc=True,aliases=['TOP265VG', 'TOP266VG', 'TOP267VG', 'TOP268VG', 'TOP269VG', 'TOP270VG', 'TOP271VG'],pins=[
            Pin(num='1',name='V',do_erc=True),
            Pin(num='2',name='X',do_erc=True),
            Pin(num='3',name='C',do_erc=True),
            Pin(num='4',name='F',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='D',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='7',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='8',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='9',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='10',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='11',name='S',func=Pin.OPENEMIT,do_erc=True),
            Pin(num='12',name='S',func=Pin.OPENEMIT,do_erc=True)])])
