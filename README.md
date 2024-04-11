# ToolsApp V1.0
# Miniprogramas - Herramientas

* [Diferencia entre cadenas de texto](#diff)
* [Ficheros ZIP](#zip)
* [Comprobación de DNIs](#dni)
* [Generador de QRs](#qr)
* [Descarga de autio de YouTube](#youtube)
* [Eliminación de fondo en fotos](#background)
* [Arte ASCII: texto](#asciiart)
* [Arte ASCII: imágenes y videos](#asciiart2)
* [Grabación de audio](#soundrecord)
* [Transcripción de voz](#whisper)
* [Reconocimiento de caracteres (OCR)](#ocr)


## <a name="diff"></a>Diferencia entre cadenas de texto.

Muestra diferencias enrte dos cadenas (strings): [simplediff.py](simplediff.py)

## <a name="zip"></a>Ficheros ZIP

Lista los ficheros en un fichero comprimido con zip, y extráelos: [unzip.py](unzip.py)

## <a name="dni"></a>Comprobación de DNIs

Comprueba si la letra de un DNI está bien: [dni.py](dni.py)

## <a name="qr"></a>Generador de QRs

Genera un código QR para una url</a>: [qr.py](qr.py) 

* Dependencias: [pyqrcode](https://github.com/mnooner256/pyqrcode), [pypng](https://gitlab.com/drj11/pypng)
```commandline
pip install pyqrcode pypng
```

## <a name="youtube">Descarga de audio de YouTube</a>

Descarga el canal de audio de un video de YouTube: [ytaudio.py](ytaudio.py)

* Dependencias: [pytube](https://pytube.io)

```commandline
pip install pytube
```

* Explicación detallada: [Extract audio from a YouTube video](https://blog.balasundar.com/extract-audio-from-youtube-video-using-python)

## <a name="background"></a>Eliminación de fondo en fotos

Elimina los planos de fondo (background) de una foto: [background.py](background.py)

* Dependencias: [rembg](https://github.com/danielgatis/rembg)

```commandline
pip install rembg
```

o, si tienes GPU soportada:

```commandline
pip install rembg[gpu]
```

* Otros detalles de instalación: La primera vez que se ejecuta, el módulo `rembg` trata de descargarse el modelo de aprendizaje automático (machine learning) que utiliza. Su descarga puede fallar, porque se almacena en Google Drive, que tiene limitaciones para descarga. Si eso ocurre, se verá un error que incluye algo como:

```
Access denied with the following error:
...
You may still be able to access the file from the browser:

         https://drive.google.com/uc?id=1tCU5MM1LhRgGou5OpmpjBQbSrYIUoYab 

Traceback (most recent call last):
...
[...] Load model from ~/.u2net/u2net.onnx failed. File doesn't exist
```

Si esto ocurre, podemos descargar el fichero de modelo (`u2net.onnx`) manualmente, desde el navegador, y copiarlo al directorio donde `remgb` espera encontrarlo (`~/.u2net`). Por ejemplo, si se ha descargado a `~/Downloads`:

```commandline
cp ~/Downloads/u2net.onnx ~/.u2net/u2net.onnx
```

* Uso desde línea de comandos:

```commandline
rembg i misc/cafe.jpg misc/cafe-nobg.jpg
```

* Explicación detallada: [How to Remove Image Background Using Python](https://python.plainenglish.io/how-to-remove-image-background-using-python-6f7ffa8eab15)

* Curiosidad: con el mismo modelo de aprendizaje automático (U2net), se pueden realizar retratos "de trazos" a partir de fotos: [profu.ai/](http://profu.ai/)

## <a name="asciiart">Arte ASCII: texto</a>

Muestra imágenes de una línea o texto en formato cartel al estilo [ASCII Art](https://en.wikipedia.org/wiki/ASCII_art) [artdemo.py](artdemo.py).

* Dependencias: [art](https://github.com/sepandhaghighi/art#1-line-art)

```commandline
pip install art
```

* Listado de fonts disponibles:

```commandline
python -m art fonts
```

## <a name="asciiart2">Arte ASCII: imágenes y videos</a>

Convierte imágenes y videos al estilo [ASCII Art](https://en.wikipedia.org/wiki/ASCII_art) [artdemo2.py](artdemo2.py).

* Dependencias: [asciipixels](https://github.com/UmActually/asciipixels/). Necesita también ImageMagick (para imágeners) y FFmpeg (para videos), que vienen como paquetes en Debian y Ubuntu.

```commandline
pip install asciipixels
```

```commandline
sudo apt install ffmpeg imagemagick
```

## <a name="soundrecord">Grabación de audio</a>

Graba audio del micrófono: [sound_record.py](sound_record.py).

* Dependencias: [sounddevice](https://python-sounddevice.readthedocs.io/en/0.4.5/usage.html#recording). Necesita también [scipy](https://scipy.org/).

```commandline
pip install sounddevice scipy
```

## <a name="whisper">Transcripción de voz</a>

Transcribe a texto un fichero de audio con voz (en inglés, español, u otros idiomas): [transcribe.py](transcribe.py)

* Dependencias: [whisper](https://github.com/openai/whisper)

```commandline
pip install git+https://github.com/openai/whisper.git
```

## <a name="ocr">Reconociniento de caracteres (OCR)</a>

Reconoce caracteres en una imagen (en inglés y otros idiomas): [ocr.py](ocr.py)

* Dependencias: [EasyOCR](https://github.com/JaidedAI/EasyOCR)

```commandline
pip install easyocr
```

