from skidl import SKIDL, TEMPLATE, Part, Pin, SchLib

SKIDL_lib_version = '0.0.1'

relays = SchLib(tool=SKIDL).add_parts(*[
        Part(name='AZ850-x',dest=TEMPLATE,tool=SKIDL,keywords='Miniature Polarised Relay Dual Pole Bistable',description='Microminiature Polarised Dual Pole Relay Bistable',ref_prefix='RL',num_units=1,do_erc=True,aliases=['AZ850P1-x'],pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='9',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='10',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='AZ850P2-x',dest=TEMPLATE,tool=SKIDL,keywords='Miniature Polarised Relay Dual Pole Bistable',description='Microminiature Polarised Dual Pole Relay Bistable',ref_prefix='RL',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='9',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='10',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='FINDER-32.21-x300',dest=TEMPLATE,tool=SKIDL,keywords='Single Pole Relay SPST-NO',description='RELPOL RM50-xx21, Single Pole Relay SPST-NO, 6A',ref_prefix='RL',num_units=1,do_erc=True,aliases=['FINDER-36.11-4301', 'RM50-xx21'],pins=[
            Pin(num='11',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='A1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='A2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='14',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='FINDER-40.51',dest=TEMPLATE,tool=SKIDL,keywords='Single Pole Relay Sugar Cube',description='Single Pole Relay, Sugar Cube, 15A',ref_prefix='RL',num_units=1,do_erc=True,aliases=['FINDER-36.11.4001', 'FINDER-40.31', 'RM50-xx11'],pins=[
            Pin(num='11',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='A1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='12',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='A2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='14',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='FINDER-40.52',dest=TEMPLATE,tool=SKIDL,keywords='Dual Pole Relay',description='RELPOL RSM822, Dual Pole Relay, 5mm Pitch, 2A',ref_prefix='RL',num_units=1,do_erc=True,aliases=['FINDER-41.52', 'FINDER-44.52', 'FINDER-44.62', 'FINDER-30.22', 'RSM822', 'RM84'],pins=[
            Pin(num='11',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='21',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='A1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='12',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='22',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='A2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='14',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='24',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='FRT5',dest=TEMPLATE,tool=SKIDL,keywords='relay monostable',description='FRT5 relay',ref_prefix='K',num_units=1,fplist=['Relay_DPDT_FRT5'],do_erc=True,pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='9',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='10',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='FRT5_separated',dest=TEMPLATE,tool=SKIDL,keywords='relay monostable',description='FRT5 relay',ref_prefix='K',num_units=3,fplist=['Relay_DPDT_FRT5'],do_erc=True,pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='10',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='9',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='G5Q-1',dest=TEMPLATE,tool=SKIDL,keywords='Miniature Single Pole Relay',description='OMRON G5G-1, Miniature Single Pole Relay, SPDT, 10A',ref_prefix='RL',num_units=1,fplist=['Relay?SPDT?OMRON?G5Q*'],do_erc=True,pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='G5Q-1A',dest=TEMPLATE,tool=SKIDL,keywords='Miniature Single Pole Relay',description='G5G-1A, Miniature Single Pole Relay, SPST-NO, 10A',ref_prefix='RL',num_units=1,fplist=['Relay?SPST?NO?OMRON?G5Q*'],do_erc=True,pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='IM00',dest=TEMPLATE,tool=SKIDL,keywords='relay monostable',description='IM Relay, standard version, monostable, switching current 2/5A, power 60W/62.5VA, voltage 220VDC/250VAC',ref_prefix='K',num_units=1,do_erc=True,aliases=['IM01', 'IM02', 'IM03', 'IM04', 'IM05', 'IM06', 'IM07', 'IM08'],pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='IM11',dest=TEMPLATE,tool=SKIDL,keywords='relay monastable sensitive',description='IM Relay, sensitive version, monostable, switching current 2/5A, power 60W/62.5VA, voltage 220VDC/250VAC',ref_prefix='K',num_units=1,do_erc=True,aliases=['IM12', 'IM13', 'IM16', 'IM17'],pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='IM21',dest=TEMPLATE,tool=SKIDL,keywords='relay monastable sensitive',description='IM Relay, high sensitive version, monostable, switching current 2/5A, power 60W/62.5VA, voltage 220VDC/250VAC',ref_prefix='K',num_units=1,do_erc=True,aliases=['IM22', 'IM23', 'IM26'],pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='IM40',dest=TEMPLATE,tool=SKIDL,keywords='relay bistable',description='IM Relay, standard version, bistable, switching current 2/5A, power 60W/62.5VA, voltage 220VDC/250VAC',ref_prefix='K',num_units=1,do_erc=True,aliases=['IM41', 'IM42', 'IM43', 'IM44', 'IM45', 'IM46', 'IM47', 'IM48'],pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TIANBO-HJR-4102-L',dest=TEMPLATE,tool=SKIDL,keywords='Single Pole Relay',description='TIANBO HJR-4102-L, Single Pole Relay, 5mm Pitch, 3A',ref_prefix='RL',num_units=1,fplist=['Relay*HJR?4102*'],do_erc=True,pins=[
            Pin(num='5',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='12',name='~',func=Pin.PASSIVE,do_erc=True)])])
