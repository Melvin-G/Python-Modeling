from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


lons = np.array([-97.548, -116.693, -97.488, -95.1907, -97.5684, -92.2, -105.5464, -93.0723])
lats = np.array([36.808, 36.765, 36.605, 39.0561, 38.7745, 38.7441, 70.0329, 44.6781])

lons = np.reshape(lons, (-1, 2))
lats = np.reshape(lats, (-1, 2))

plt.figure(1)
m = Basemap(projection = 'mill',
	    llcrnrlat = 25,
	    llcrnrlon = -130,
	    urcrnrlat = 50,
	    urcrnrlon = -60,
	    resolution = 'l')

m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.drawmapboundary()
#m.fillcontinents(color='#cc9966',lake_color='#99ffff')

a74lat, a74lon = 36.808, -97.548
xpt , ypt = m(a74lon, a74lat)
m.plot(xpt, ypt, 'r*', label = 'A74')

adrlat, adrlon = 36.765, -116.693
xpt, ypt = m(adrlon,adrlat)
m.plot(xpt, ypt, 'rs', label = 'ADR')

armlat, armlon = 36.605, -97.488
xpt, ypt = m(armlon, armlat)
m.plot(xpt, ypt, 'r8', label = 'ARM')

kfslat, kfslon = 39.0561, -95.1907
xpt, ypt = m(kfslon, kfslat)
m.plot(xpt, ypt, 'rh', label = 'KFS')

klslat, klslon = 38.7745, -97.5684
xpt, ypt = m(klslon, klslat,)
m.plot(xpt, ypt, 'rx', label = 'KLS')

mozlat, mozlon = 38.7441, -92.2
xpt, ypt = m(mozlon, mozlat)
m.plot(xpt, ypt, 'rP', label = 'MOz')

nr1lat, nr1lon = 40.0329, -105.5464
xpt, ypt = m(nr1lon, nr1lat)
m.plot(xpt, ypt, 'rp', label = 'NR1')

ro4lat, ro4lon = 44.6781, -93.0723
xpt, ypt = m(ro4lon, ro4lat)
m.plot(xpt, ypt, 'rX', label = 'Ro4')

me2lat, me2lon = 44.4523, -121.607
xpt, ypt = m(me2lon, me2lat)
m.plot(xpt, ypt, 'rd', label = 'Me2')




plt.title('Station Locations')
plt.legend()
plt.savefig('/Users/melvingonsalves/csv_python/SAVED_IMAGES/Map_Image.png')
plt.show()
