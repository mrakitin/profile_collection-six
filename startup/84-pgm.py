from ophyd import Component as Cpt, Device, EpicsMotor, EpicsSignalRO, EpicsSignal

class PGM(PreDefinedPositions):
    cff = Cpt(EpicsMotor, '-Ax:9_Cff}Mtr')
    en = Cpt(EpicsMotor, '-Ax:9_Eng}Mtr')
    grx = Cpt(EpicsMotor, '-Ax:9_GT}Trans:Mtr')
    m2pit = Cpt(EpicsMotor, '-Ax:9_MP}Mtr')
    grpit = Cpt(EpicsMotor, '-Ax:9_GP}Mtr')

    gr500 = Cpt(EpicsSignalRO, '-Ax:9_GT}Trans:GT1Inp')
    gr1200 = Cpt(EpicsSignalRO, '-Ax:9_GT}Trans:GT2Inp')
    gr1800 = Cpt(EpicsSignalRO, '-Ax:9_GT}Trans:GT3Inp')

    groff = Cpt(EpicsSignal, '-Ax:9_GP}Mtr.OFF')
    m2off = Cpt(EpicsSignal, '-Ax:9_MP}Mtr.OFF')
    grlines = Cpt(EpicsSignal, '}:LINES')

    m3slt_hs = Cpt(EpicsMotor, prefix='XF:02IDC-OP{Mir:3-Slt:12_U_1-Ax:HS}Mtr')
    m3slt_ha = Cpt(EpicsMotor, prefix='XF:02IDC-OP{Mir:3-Slt:12_U_1-Ax:HA}Mtr')


class PGMjoe(Device):
    # cff = Cpt(EpicsMotor, '_Cff}Mtr')
    # en = Cpt(EpicsMotor, '_Eng}Mtr')
    grx = Cpt(EpicsMotor, '_GT}Trans:Mtr')
    m2pit = Cpt(EpicsMotor, '_MP}Mtr')
    grpit = Cpt(EpicsMotor, '_GP}Mtr')

    gr500 = Cpt(EpicsSignalRO, '_GT}Trans:GT1Inp')
    gr1200 = Cpt(EpicsSignalRO, '_GT}Trans:GT2Inp')
    gr1800 = Cpt(EpicsSignalRO, '_GT}Trans:GT3Inp')


# TODO changing gratign will require a plan + at least 1
# soft signal

class PGM_ES(Device):
    cff = Cpt(EpicsMotor, 'cff}Mtr')
    en = Cpt(EpicsMotor, 'E}Mtr')
    grx = Cpt(EpicsMotor, 'GXRaw}Mtr')
    m7pit = Cpt(EpicsMotor, 'MP}Mtr')
    grpit = Cpt(EpicsMotor, 'GP}Mtr')
    grxrb = Cpt(EpicsSignalRO,'GXEnc}Mtr.RBV')

pgm = PGM('XF:02IDB-OP{Mono:1', name='pgm', locations = {
         'mbg': ['m2off', 84.20549404, 'groff', 82.07813352 ,'grx', -63.0, 'grlines', 500, 'm3slt_hs', -37.5,
				 'm3slt_ha',-17.2], #'offset values changed on 08/11/2019 ['m2off', 84.20033028, 'groff', 82.0737638 ,'grx', -63.0, 'grlines', 500]
	 	 'ubg': ['m2off', 84.20861191, 'groff', 82.1055395916 , 'grx', -1,'grlines', 1800, 'm3slt_hs', -37.7,
				 'm3slt_ha',-17.8] }) #before 08/10/2019 'ubg': ['m2off', 84.20265344, 'groff', 82.1012242016 , 'grx', -1,'grlines', 1800] })
pgmjoe = PGMjoe('XF:02IDB-OP{Mono:1-Ax:9', name='pgmjoe')
espgm = PGM_ES('XF:02IDD-ES{Mono:2-Ax:',name='espgm')

# pgm = PGM('XF:02IDB-OP{Mono:1', name='pgm', locations = {
#           'mbg': ['m2off', 84.20549404, 'groff', 82.07813352 ,'grx', -63.0, 'grlines', 500], #'offset values changed on 08/11/2019 ['m2off', 84.20033028, 'groff', 82.0737638 ,'grx', -63.0, 'grlines', 500]
#  	       'ubg': ['m2off', 84.20861191, 'groff', 82.1055395916 , 'grx', -1,'grlines', 1800] }) #before 08/10/2019 'ubg': ['m2off', 84.20265344, 'groff', 82.1012242016 , 'grx', -1,'grlines', 1800] })


