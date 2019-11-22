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

11. 
