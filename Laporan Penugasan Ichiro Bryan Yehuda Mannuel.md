Nama : Bryan Yehuda Mannuel       
NRP : 05311940000021
Departemen : Teknologi Informasi (IT)       
Divisi : Programming

## Persiapan Sebelum Penugasan

 1. _OS Linux Ubuntu_ sudah terinstall                           
 2. _Webots_ sudah terinstall dan tutorial _Webots_ sudah selesai
 3. Sudah mempelajari dan familier dengan Syntax _Markdown_

 ## Tugas 1 : Install OpenCV Version 4.1.2     
 
 1. Buka Terminal pada _Linux Ubuntu_ agar bisa memasukkan command-command _Linux Ubuntu_ yang diperlukan
(**Selesai pada 20 November 2019, jam 17.00**)
2. Masuk ke prioritas Root pada Terminal dengan command :
```
sudo su
```
dan masukkan password               
(**Selesai pada 20 November 2019, jam 17.01**)    

3. Menginstall dependencies atau file-file yang dibutuhkan oleh _OpenCV_ dengan command :
```
sudo apt-get update  -y
sudo apt-get remove  -y  x264 libx264-dev
sudo apt-get install  -y  build-essential checkinstall cmake pkg-config yasm
sudo apt-get install  -y  git gfortran
sudo add-apt-repository  -y  "deb http://security.ubuntu.com/ubuntu xenial-security main"
sudo apt-get install  -y  libjpeg8-dev libjasper-dev libpng12-dev
sudo apt-get install  -y  libtiff5-dev
sudo apt-get install  -y  libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
sudo apt-get install  -y  libxine2-dev libv4l-dev
sudo apt-get install  -y  libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
sudo apt-get install  -y  qt5-default libgtk2.0-dev libtbb-dev
sudo apt-get install  -y  libatlas-base-dev
sudo apt-get install  -y  libfaac-dev libmp3lame-dev libtheora-dev
sudo apt-get install  -y  libvorbis-dev libxvidcore-dev
sudo apt-get install  -y  libopencore-amrnb-dev libopencore-amrwb-dev
sudo apt-get install  -y  x264 v4l-utils
sudo apt-get install  -y  libprotobuf-dev protobuf-compiler
sudo apt-get install  -y  libgoogle-glog-dev libgflags-dev
sudo apt-get install  -y  libgphoto2-dev libeigen3-dev libhdf5-dev doxygen
```
(**Selesai pada 20 November 2019, jam 17.42**)       

4. Melakukan Instalasi Python versi 2 dan 3 dengan command :
```
sudo apt-get install  -y  python-dev python-pip
sudo apt-get install  -y  python3-dev python3-pip
sudo apt-get install  -y  python-dev python-pip python3-dev python3-pip
sudo  -H  pip2 install  -U  pip numpy
sudo  -H  pip3 install  -U  pip numpy    
```
(**Selesai pada 20 November 2019, jam 18.01**)         

5. Install virtual environment untuk membedakan instalasi Python 2 dan 3 dengan command :
```
sudo pip2 install virtualenv virtualenvwrapper
sudo pip3 install virtualenv virtualenvwrapper 
```
(**Selesai pada 20 November 2019, jam 18.06**)         

6. Melakukan modify pada file _.bashrc_ dengan command :
```
echo  "# Virtual Environment Wrapper"  >>  ~/.bashrc
echo  "source /usr/local/bin/virtualenvwrapper.sh"  >>  ~/.bashrc
source  ~/.bashrc
```
(**Selesai pada 20 November 2019, jam 18.10**)

7. Membuat virtual environment untuk Python dan menginstall library basic untuk Python dengan command :
```
mkvirtualenv opencv_source_2  -p  python2
workon opencv_source_2
pip install numpy scipy matplotlib scikit-image scikit-learn ipython
mkvirtualenv opencv_source_3  -p  python3
workon opencv_source_3
pip install numpy scipy matplotlib scikit-image scikit-learn ipython      
```
(**Selesai pada 20 November 2019, jam 18.19**)

8. Mendownload OpenCV 4.1.2 dan OpenCV Contrib dengan command :
```
cd  ~/Desktop/
git clone https://github.com/opencv/opencv.git
cd  opencv
git checkout  4.1.2
cd  ..
git clone https://github.com/opencv/opencv_contrib.git
cd  opencv_contrib
git checkout  4.1.2
cd  ..
```
(**Selesai pada 20 November 2019, jam 18.54**)

9. Membuild library dengan Cmake dengan command :
```
cd  ~/Desktop/opencv
mkdir build
cd  build 
```

untuk Python 2 gunakan command berikut :
```
workon opencv_source_2

cmake  -D  CMAKE_BUILD_TYPE=RELEASE  \
       -D  CMAKE_INSTALL_PREFIX=/usr/local  \
       -D  INSTALL_C_EXAMPLES=ON  \
       -D  INSTALL_PYTHON_EXAMPLES=ON  \
       -D  WITH_TBB=ON  \
       -D  WITH_V4L=ON  \
       -D  WITH_QT=ON  \
       -D  WITH_OPENGL=ON  \
       -D  OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules  \
       -D  BUILD_EXAMPLES=ON  \
       -D  OPENCV_GENERATE_PKGCONFIG=YES  ..
```
untuk Python 3 gunakan command berikut :
```
workon opencv_source_3

cmake  -D  CMAKE_BUILD_TYPE=RELEASE  \
       -D  CMAKE_INSTALL_PREFIX=/usr/local  \
       -D  INSTALL_C_EXAMPLES=ON  \
       -D  INSTALL_PYTHON_EXAMPLES=ON  \
       -D  WITH_TBB=ON  \
       -D  WITH_V4L=ON  \
       -D  WITH_QT=ON  \
       -D  WITH_OPENGL=ON  \
       -D  OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules  \
       -D  BUILD_EXAMPLES=ON  \
       -D  OPENCV_GENERATE_PKGCONFIG=YES  ..
```
(**Selesai pada 20 November 2019, jam 19.20**)

10. Menggunakan make utility untuk membuild library dengan command :
```
nproc
make  -j8
sudo make install
sudo sh  -c  'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig
```
(**Selesai pada 20 November 2019, jam 20.43**)

11. Memodifikasi file _OpenCV4.pc_ dengan command :
```
cd  ~/Desktop/opencv/build/unix-install/
vi opencv4.pc 
```
dan ganti line :
```
prefix=/usr/local
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir_old=${prefix}/include/opencv4/opencv  <=  ganti line ini
includedir_new=${prefix}/include/opencv4
Name:  OpenCV
Description:  Open  Source Computer Vision Library
Version:  4.1.0

Libs:  -L${exec_prefix}/lib  -lopencv_gapi  -lopencv_stitching  -lopencv_aruco  -lopencv_bgsegm  -lopencv_bioinspired  -lopencv_ccalib  -lopencv_cvv  -lopencv_dnn_objdetect  -lopencv_dpm  -lopencv_face  -lopencv_freetype  -lopencv_fuzzy  -lopencv_hdf  -lopencv_hfs  -lopencv_img_hash  -lopencv_line_descriptor  -lopencv_quality  -lopencv_reg  -lopencv_rgbd  -lopencv_saliency  -lopencv_sfm  -lopencv_stereo  -lopencv_structured_light  -lopencv_phase_unwrapping  -lopencv_superres  -lopencv_optflow  -lopencv_surface_matching  -lopencv_tracking  -lopencv_datasets  -lopencv_text  -lopencv_dnn  -lopencv_plot  -lopencv_videostab  -lopencv_video  -lopencv_xfeatures2d  -lopencv_shape  -lopencv_ml  -lopencv_ximgproc  -lopencv_xobjdetect  -lopencv_objdetect  -lopencv_calib3d  -lopencv_features2d  -lopencv_highgui  -lopencv_videoio  -lopencv_imgcodecs  -lopencv_flann  -lopencv_xphoto  -lopencv_photo  -lopencv_imgproc  -lopencv_core
Libs.private:  -ldl  -lm  -lpthread  -lrt  -L/usr/lib/x86_64-linux-gnu  -lGL  -lGLU
Cflags:  -I${includedir_old}  -I${includedir_new}
```
dengan line berikut :
```
includedir_old=${prefix}/include/opencv4/opencv2
```
(**Selesai pada 20 November 2019, jam 20.55**)

12. Ubah lokasi file _OpenCV4.pc_ dengan command :
```
cd  /usr/local/lib/
mkdir pkgconfig
sudo cp  ~/Desktop/opencv/build/unix-install/opencv4.pc  /usr/local/lib/pkgconfig/
```
(**Selesai pada 20 November 2019, jam 21.02**)

13. Menambahkan file location ke _PKG_CONFIG_PATH Variable_ dan mengubah file _bash.rc_ dengan command :
```
sudo vi  ~/.bashrc
```
dan tambahkan line berikut ke bagian paling bawah :
```
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
export PKG_CONFIG_PATH
```
kemudian jalankan command berikut untuk memeriksa apakah sudah benar atau belum :
```
source  ~/.bashrc
echo  $PKG_CONFIG_PATH
```
(**Selesai pada 20 November 2019, jam 21.13**)

14. Melakukan verifikasi instalasi dengan c++ dengan menjalankan command berikut :
```
cd ~/Desktop
mkdir test_code
cd test_code
gedit test.cpp
```
dan masukkan code berikut :
```cpp
#include "opencv.hpp"
using  namespace  cv;
using  namespace  std;

int  main(  int  argc,  char**  argv  )
{
cout  <<  "OpenCV version : "  <<  CV_VERSION  <<  endl;
cout  <<  "Major version : "  <<  CV_MAJOR_VERSION  <<  endl;
cout  <<  "Minor version : "  <<  CV_MINOR_VERSION  <<  endl;
cout  <<  "Subminor version : "  <<  CV_SUBMINOR_VERSION  <<  endl;
}
```
lalu jalankan program dengan command berikut :
```
cd  ~/Desktop/test_code/
g++  -std=c++11  test.cpp  `pkg-config  --libs  --cflags opencv4`  -o  result
/.result
```
(**Selesai pada 20 November 2019, jam 21.23**)

15. Melakukan verifikasi instalasi dengan python 2 dengan menjalankan command berikut :
```
cd ~/Desktop
mkdir test_code
cd test_code
gedit test_2.py
```
dan masukkan code berikut :
``` 
import  cv2
print  "OpenCV version : {0}".format(cv2.__version__)
major_ver,  minor_ver,  subminor_ver  =  (cv2.__version__).split('.')
print  "Major version : {0}".format(major_ver)
print  "Minor version : {0}".format(minor_ver)
print  "Subminor version : {0}".format(subminor_ver)
```
lalu jalankan program dengan command berikut :
```
cd  ~/Desktop/test_code/
workon opencv_source_2
python test_2.py
```
(**Selesai pada 20 November 2019, jam 21.43**)

16. Melakukan verifikasi instalasi dengan python 3 dengan menjalankan command berikut :
```
cd ~/Desktop
mkdir test_code
cd test_code
gedit test_3.py
```
dan masukkan code berikut :
``` 
import  cv2
print  "OpenCV version : {0}".format(cv2.__version__)
major_ver,  minor_ver,  subminor_ver  =  (cv2.__version__).split('.')
print  "Major version : {0}".format(major_ver)
print  "Minor version : {0}".format(minor_ver)
print  "Subminor version : {0}".format(subminor_ver)
```
lalu jalankan program dengan command berikut :
```
cd  ~/Desktop/test_code/
workon opencv_source_3
python test_3.py
```
(**Selesai pada 20 November 2019, jam 21.53**)

17. Setelah dilakukan verifikasi, memang benar bahwa OpenCV Version 4.1.2 sudah terinstall dan siap untuk digunakan
