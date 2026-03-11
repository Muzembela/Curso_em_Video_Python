
import math

angulo = float(input('Digite o angulo: '))
angulo_rad = math.radians(angulo)
seno = math.sin(angulo)
cos = math.cos(angulo)
tang = math.tan(angulo)

print('Angulo->{}\nSeno->{}\nCosceno->{}\nTangente->{}.'.format(angulo, seno, cos, tang))