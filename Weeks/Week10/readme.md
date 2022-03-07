# Week 10: Remote Sensing and Sentiment Analysis

# Final week!

# Albert Kochaphum
<img src="https://avatars.githubusercontent.com/u/8574425?v=4">

*   A conversation with Albert Kochaphum
   * UCLA Urban Planning alum
   * Former Campus GIS Coordinator for OARC
   * Currently a Digital Communications Administrator at Los Angeles Metro
   * Crazy github master https://github.com/albertkun  

## Agenda

*   This class will be recorded (remind me if I forget!)
*   A conversation with Albert
*   --break--
*   Log in to the class JupyterHub using the [UP206A Git Puller](https://jupyter.idre.ucla.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fyohman%2F21F-UP206A&urlpath=lab%2Ftree%2F21F-UP206A%2F&branch=master) to avoid the bottleneck
*   [Final project guidelines](../../Midterm%20and%20Finals/readme.md)
*   Useful labs that we won't cover in class
    * Web scraping
    * Remote sensing  
    * Sentiment analysis
*   The final phase: Publishing your work
    *   [A history of web maps at UCLA](https://docs.google.com/presentation/d/1FMFzxBifgu_DxXQ-L0KhlHV8zpneN3a_N380L8k7_k8/edit?usp=sharing)
*   A javascript teaser
    * download [sublime](https://www.sublimetext.com/)

# A javascript teaser

Open Sublime, and enter the following code. Then, save the file as `index.html`, and open it on a web browser (double clicking the file usually works).

```html
<!DOCTYPE html>
<html>
<head>
	<title>My first map</title>
	<meta charset="utf-8" />

	<!-- styles -->
	<style type="text/css">
		html {height: 100%}
		body {height: 100%;margin: 0;}
		#map {height: 100%;}
	</style>

	<!-- leaflet stylesheet-->
	<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>

	<!-- leaflet js library -->
	<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>

</head>
<body>
	<!-- map container -->
	<div id="map"></div>

	<script>
		// initiate map
		var map = L.map('map').setView([34.0744413,-118.4391512], 18);

		// basemap
		var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
			maxZoom: 18,
			attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
				'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
			id: 'mapbox/streets-v11',
			tileSize: 512,
			zoomOffset: -1
		}).addTo(map);

	</script>
</body>
</html>
```
