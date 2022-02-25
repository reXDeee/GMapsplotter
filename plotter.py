import gmplot

# Create the map plotter:
API = 'AIzaSyB73trnExI_S-VeAK9exJ_woqjTgWopzHg'
# (your API key here)
gmap = gmplot.GoogleMapPlotter(28.457523, 77.026344, 14, apikey=API)
# Draw the map:
gmap.draw('map.html')
