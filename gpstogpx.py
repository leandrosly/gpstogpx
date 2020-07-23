# encoding: iso-8859-1
import sys
import os
from datetime import datetime

def main():
    if not len(sys.argv) > 1:
        print('Entrar com o arquivo .gps como parâmetro.')
        sys.exit()

    arquivo_gps = sys.argv[1]
    # arquivo_gps = 'D:\Documentos\GPS\Arroio Grande\export001.gps'

    if not os.path.isfile(arquivo_gps):
        print('Arquivo {} nao existe.'.format(arquivo_gps))
        sys.exit()

    # arquivo_gpx = 'D:\Downloads\Arroio Grande GPS\export001.gpx'
    # arquivo_gpx = 'D:\Documentos\GPS\Arroio Grande\export001.gpx'
    arquivo_gpx = arquivo_gps[:-3] + 'gpx'

    with open(arquivo_gpx, "a") as gpx:
        gpx.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
        gpx.write('<gpx xmlns="http://www.topografix.com/GPX/1/1" creator="GPStoGPX" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">\n')
        with open(arquivo_gps) as gps:
            gpx.write('<trk>\n')
            gpx.write('<name>Percurso MapaRadar</name>\n')
            gpx.write('<trkseg>\n')
            for linha in gps:
                ponto = linha.split()
                gpx.write('<trkpt lat="{}" lon="{}">\n'.format(ponto[1],ponto[2]))
                gpx.write('<ele>{}</ele>\n'.format(ponto[7]))
                gpx.write('<time>{}</time>\n'.format(datetime.utcfromtimestamp(int(ponto[6])/1000).strftime('%Y-%m-%dT%H:%M:%SZ')))
                gpx.write('</trkpt>\n')
            gpx.write('</trkseg>\n')
            gpx.write('</trk>\n')
        gpx.write('</gpx>\n')

if __name__ == '__main__':
    main()

# Descobrir o SO
# https://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python

# Caracteres
# https://pt.stackoverflow.com/questions/67604/encoding-utf-8-permite-acentos

# Argparse
# https://docs.python.org/3/howto/argparse.html