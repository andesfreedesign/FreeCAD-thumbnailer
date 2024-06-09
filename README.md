# FreeCAD-thumbnailer
Files and instructions to configure the thumbnail view of FreeCAD files in GNU/Linux Operating Systems (Free Desktop Environments), for those users who run the portable version (AppImage)

### Installation on Debian-based distributions

- Open a terminal
- Download the .zip file
```
wget https://github.com/andesfreedesign/FreeCAD-thumbnailer/archive/refs/heads/main.zip
```
- Unzip the downloaded file
```
unzip main.zip
```
- Change to unzipped folder
```
cd FreeCAD-thumbnailer-main
```
- Copy the executable file

```
sudo cp freecad-thumbnailer.py /usr/bin
```
- Give execution permissions
```
sudo chmod +x /usr/bin/freecad-thumbnailer.py
```
- Copy the thumbnailer file
```
sudo cp FreeCAD.thumbnailer /usr/share/thumbnailers
```
- Copy the icon file
```
sudo cp freecad.png /usr/share/icons/hicolor/48x48/apps
```
- Copy the  application/x-extension-fcstd MIME type file
```
sudo cp org.freecadweb.FreeCAD.xml /usr/share/mime/packages
```
- Update the MIME database
```
sudo update-mime-database /usr/share/mime
```
