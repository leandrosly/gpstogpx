import sys
import os
from datetime import datetime

def main():
    #arquivo = 'D:\Downloads\Arroio Grande GPS\export001.gps'
    arquivo_gps = sys.argv[1]
    arquivo_gpx = 'D:\Downloads\Arroio Grande GPS\export001.gpx'

    if not os.path.isfile(arquivo_gps):
        print('Arquivo {} nao existe. Encerrando..'.format(arquivo_gps))
        sys.exit()

    minlat =   90.0
    maxlat =  -90.0
    minlon =  180.0
    maxlon = -180.0

    with open(arquivo_gpx, "a") as gpx:
        #file_object.write("hello")

        with open(arquivo_gps) as gps:
            gpx.write('<trk>')
            gpx.write('<name>Percurso MapaRadar</name>')
            gpx.write('<trkseg>')
            for linha in gps:
                ponto = linha.split()
                minlat = ponto[1] if float(ponto[1]) < float(minlat) else minlat
                maxlat = ponto[1] if float(ponto[1]) > float(maxlat) else maxlat
                minlon = ponto[2] if float(ponto[2]) < float(minlon) else minlon
                maxlon = ponto[2] if float(ponto[2]) > float(maxlon) else maxlon
                gpx.write('<trkpt lat="{}" lon="{}">'.format(ponto[1],ponto[2]))
                gpx.write('<ele>{}</ele>'.format(ponto[7]))
                gpx.write('<time>{}</time>'.format(datetime.utcfromtimestamp(int(ponto[6])/1000).strftime('%Y-%m-%dT%H:%M:%SZ')))
                gpx.write('</trkpt>')
            gpx.write("</trkseg>")
            gpx.write("</trk>")

if __name__ == '__main__':
    main()
