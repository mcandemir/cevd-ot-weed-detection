# CREATINY - IKA TESTER
    1-Resimler direkt images klasörüne yığıldıktan sonra menüden `yolo_multiimage.py` seçilip test edilebilir
    2-Realtime-test1 şimdilik sadece webcam'e bağlanıyor, USB kamera için ayarlanması lazım


## Dosya yapisi
    |-images
    |   |-weed1.jpg
    |   |-weed2.jpg
    |   |-...
    |
    |-src
    |   |-yolo_multiimage.py
    |   |-yolo_realtime_test1.py
    |   |-yolo_soloimage.py
    |
    |-yolo
    |   |-weed.cfg
    |   |-weed.names
    |   |-weed_best.weights
    |   |-weed_last.weights
    |
    |-main.py


## Gerekli Paketler (anaconda)
    conda install -c conda-forge opencv
    conda install -c conda-forge/label/gcc7 opencv
    conda install -c conda-forge/label/broken opencv
    conda install -c conda-forge/label/cf201901 opencv
    conda install -c conda-forge/label/cf202003 opencv


## images ve yolo dosya linkleri
[![Generic badge](https://img.shields.io/badge/IMAGES/-GoogleDrive-<COLOR>.svg)](https://drive.google.com/file/d/1ZAuyVN6UFelApcRQLQ4J6nI8ebtCtKBL/view?usp=sharing)
[![Generic badge](https://img.shields.io/badge/YOLO/-GoogleDrive-<COLOR>.svg)](https://drive.google.com/file/d/1x4VcRu4lpBmDB9Yzx8E2pUhQh-lzuG03/view?usp=sharing)


## Çalıştırma (anaconda)
    python main.py