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

17. Setelah dilakukan verifikasi, memang benar bahwa OpenCV Version 4.1.2 untuk C++ dan Python 2 sudah terinstall dan siap untuk digunakan, namun untuk Python 3 masih belum bisa karena ada suatu bug sehingga file _cv2.so_ tidak bisa ditemukan padahal sudah ada file tersebut. Hal ini sudah saya cari dimana-mana dan ternyata fix untuk Python 3 ini hanya ada di _OS Windows_

## Tugas 2 : Kerjakan Tutorial OpenCV

### 1. Basic Drawing
1. Pada tutorial ini, kita akan belajar cara :
    * Membuat garis dengan fungsi line()
    * Membuat oval dengan fungsi ellipse()
    * Membuat bujur sangkar dengan fungsi rectangle()
    * Membuat lingkaran dengan fungsi circle()
    * Membuat segi banyak berisi dengan fungsi fillpoly()

2. Class point digunakan untuk mendefinisikan suatu titik di dalam gambar, dengan contoh penulisannya :
```cpp
Point pt;
pt.x= 10;
pt.y = 8;
```

3. Class scalar bisa digunakan untuk mendefinisikan value pixel yang mana pada tutorial kali ini akan digunakan untuk memberi warna, dengan contoh penulisannya :
```cpp
Scalar( a, b, c )
```

4. Buat file baru dengan nama basic_drawing.cpp dan copy-paste code berikut :
```cpp
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

#define w 400

using namespace cv;

/// Function headers
void MyEllipse( Mat img, double angle );
void MyFilledCircle( Mat img, Point center );
void MyPolygon( Mat img );
void MyLine( Mat img, Point start, Point end );

/**
 * @function main
 * @brief Main function
 */
int main( void ){

  //![create_images]
  /// Windows names
  char atom_window[] = "Drawing 1: Atom";
  char rook_window[] = "Drawing 2: Rook";

  /// Create black empty images
  Mat atom_image = Mat::zeros( w, w, CV_8UC3 );
  Mat rook_image = Mat::zeros( w, w, CV_8UC3 );
  //![create_images]

  /// 1. Draw a simple atom:
  /// -----------------------

  //![draw_atom]
  /// 1.a. Creating ellipses
  MyEllipse( atom_image, 90 );
  MyEllipse( atom_image, 0 );
  MyEllipse( atom_image, 45 );
  MyEllipse( atom_image, -45 );

  /// 1.b. Creating circles
  MyFilledCircle( atom_image, Point( w/2, w/2) );
  //![draw_atom]

  /// 2. Draw a rook
  /// ------------------

  //![draw_rook]
  /// 2.a. Create a convex polygon
  MyPolygon( rook_image );

  //![rectangle]
  /// 2.b. Creating rectangles
  rectangle( rook_image,
         Point( 0, 7*w/8 ),
         Point( w, w),
         Scalar( 0, 255, 255 ),
         FILLED,
         LINE_8 );
  //![rectangle]

  /// 2.c. Create a few lines
  MyLine( rook_image, Point( 0, 15*w/16 ), Point( w, 15*w/16 ) );
  MyLine( rook_image, Point( w/4, 7*w/8 ), Point( w/4, w ) );
  MyLine( rook_image, Point( w/2, 7*w/8 ), Point( w/2, w ) );
  MyLine( rook_image, Point( 3*w/4, 7*w/8 ), Point( 3*w/4, w ) );
  //![draw_rook]

  /// 3. Display your stuff!
  imshow( atom_window, atom_image );
  moveWindow( atom_window, 0, 200 );
  imshow( rook_window, rook_image );
  moveWindow( rook_window, w, 200 );

  waitKey( 0 );
  return(0);
}

/// Function Declaration

/**
 * @function MyEllipse
 * @brief Draw a fixed-size ellipse with different angles
 */
//![my_ellipse]
void MyEllipse( Mat img, double angle )
{
  int thickness = 2;
  int lineType = 8;

  ellipse( img,
       Point( w/2, w/2 ),
       Size( w/4, w/16 ),
       angle,
       0,
       360,
       Scalar( 255, 0, 0 ),
       thickness,
       lineType );
}
//![my_ellipse]

/**
 * @function MyFilledCircle
 * @brief Draw a fixed-size filled circle
 */
//![my_filled_circle]
void MyFilledCircle( Mat img, Point center )
{
  circle( img,
      center,
      w/32,
      Scalar( 0, 0, 255 ),
      FILLED,
      LINE_8 );
}
//![my_filled_circle]

/**
 * @function MyPolygon
 * @brief Draw a simple concave polygon (rook)
 */
//![my_polygon]
void MyPolygon( Mat img )
{
  int lineType = LINE_8;

  /** Create some points */
  Point rook_points[1][20];
  rook_points[0][0]  = Point(    w/4,   7*w/8 );
  rook_points[0][1]  = Point(  3*w/4,   7*w/8 );
  rook_points[0][2]  = Point(  3*w/4,  13*w/16 );
  rook_points[0][3]  = Point( 11*w/16, 13*w/16 );
  rook_points[0][4]  = Point( 19*w/32,  3*w/8 );
  rook_points[0][5]  = Point(  3*w/4,   3*w/8 );
  rook_points[0][6]  = Point(  3*w/4,     w/8 );
  rook_points[0][7]  = Point( 26*w/40,    w/8 );
  rook_points[0][8]  = Point( 26*w/40,    w/4 );
  rook_points[0][9]  = Point( 22*w/40,    w/4 );
  rook_points[0][10] = Point( 22*w/40,    w/8 );
  rook_points[0][11] = Point( 18*w/40,    w/8 );
  rook_points[0][12] = Point( 18*w/40,    w/4 );
  rook_points[0][13] = Point( 14*w/40,    w/4 );
  rook_points[0][14] = Point( 14*w/40,    w/8 );
  rook_points[0][15] = Point(    w/4,     w/8 );
  rook_points[0][16] = Point(    w/4,   3*w/8 );
  rook_points[0][17] = Point( 13*w/32,  3*w/8 );
  rook_points[0][18] = Point(  5*w/16, 13*w/16 );
  rook_points[0][19] = Point(    w/4,  13*w/16 );

  const Point* ppt[1] = { rook_points[0] };
  int npt[] = { 20 };

  fillPoly( img,
        ppt,
        npt,
        1,
        Scalar( 255, 255, 255 ),
        lineType );
}
//![my_polygon]

/**
 * @function MyLine
 * @brief Draw a simple line
 */
//![my_line]
void MyLine( Mat img, Point start, Point end )
{
  int thickness = 2;
  int lineType = LINE_8;

  line( img,
    start,
    end,
    Scalar( 0, 0, 0 ),
    thickness,
    lineType );
}
//![my_line]
```
(**Selesai pada 21 November 2019, jam 18.25**)

5. Lalu lakukan compile source code dengan command :
```
g++ basic_drawing.cpp -o basic_drawing `pkg-config --cflags --libs opencv`
```
(**Selesai pada 21 November 2019, jam 18.27**)

6. Dan jalankan source code dengan command :
```
cd Desktop/
cd test_code/
./basic_drawing
```
(**Selesai pada 21 November 2019, jam 18.29**)

7. Hasil dari Tutorial ini adalah seperti ini :

![Atom](https://docs.opencv.org/3.4.8/Drawing_1_Tutorial_Result_0.png)
Dimana, kita belajar untuk membuat bentuk-bentuk sederhana tersebut
(**Selesai pada 21 November 2019, jam 18.31**)

### 2. Smoothing Image

1. Pada tutorial ini, kita akan belajar cara :
    * Function blur()
    * Function GaussianBlur()
    * Function medianBlur()
    * Function bilateralFilter()
2. Smoothing atau bisa disebut blurring adalah salah satu bentuk image processing yang paling simple dan sering digunakan. Kita bisa menggunakan smoothing ini untuk mengurangi noise yang ada pada gambar kita dengan cara memberikan filter pada gambar kita (contoh filter linear)

3. ada 4 tipe filter dalam OpenCV yang bisa kita gunakan yaitu :
    * Normalized Box Filter : filter yang paling mudah dan paling simpel dimana setiap output pixel adalah rata-rata dari semua pixel kernel yang ada di dalam gambar tersebut
    * Gaussian Filter : adalah filter yang paling berguna meskipun bukan yang paling cepat, dimana setiap point pixel dalam gambar dimasukkan dalam sebuah array yang nanti akan dikalkulasi menurut Gaussian Kernel dan nanti akan dijumlahkan menjadi output pixelnya 
    * Median Filter : filter yang mengkalkulasi output filternya dengan cara menghitung nilai tengah dari setiap pixel yang ada di sekelilingnya
    * Bilateral Filter : hampir sama seperti Gaussian Filter, hanya saja bilateral filter tidak melakukan smoothing pada bagian pojok-pojok dari gambar kita 

5. Buat file baru dengan nama smoothing_image.cpp dan copy-paste code berikut :
```cpp
/**
 * file Smoothing.cpp
 * brief Sample code for simple filters
 * author OpenCV team
 */

#include <iostream>
#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"

using namespace std;
using namespace cv;

/// Global Variables
int DELAY_CAPTION = 1500;
int DELAY_BLUR = 100;
int MAX_KERNEL_LENGTH = 31;

Mat src; Mat dst;
char window_name[] = "Smoothing Demo";

/// Function headers
int display_caption( const char* caption );
int display_dst( int delay );


/**
 * function main
 */
int main( int argc, char ** argv )
{
    namedWindow( window_name, WINDOW_AUTOSIZE );

    /// Load the source image
    const char* filename = argc >=2 ? argv[1] : "lena.jpg";

    src = imread( filename , IMREAD_COLOR );
    if (src.empty())
    {
        printf(" Error opening image\n");
        printf(" Usage:\n %s [image_name-- default lena.jpg] \n", argv[0]);
        return EXIT_FAILURE;
    }

    if( display_caption( "Original Image" ) != 0 )
    {
        return 0;
    }

    dst = src.clone();
    if( display_dst( DELAY_CAPTION ) != 0 )
    {
        return 0;
    }

    /// Applying Homogeneous blur
    if( display_caption( "Homogeneous Blur" ) != 0 )
    {
        return 0;
    }

    //![blur]
    for ( int i = 1; i < MAX_KERNEL_LENGTH; i = i + 2 )
    {
        blur( src, dst, Size( i, i ), Point(-1,-1) );
        if( display_dst( DELAY_BLUR ) != 0 )
        {
            return 0;
        }
    }
    //![blur]

    /// Applying Gaussian blur
    if( display_caption( "Gaussian Blur" ) != 0 )
    {
        return 0;
    }

    //![gaussianblur]
    for ( int i = 1; i < MAX_KERNEL_LENGTH; i = i + 2 )
    {
        GaussianBlur( src, dst, Size( i, i ), 0, 0 );
        if( display_dst( DELAY_BLUR ) != 0 )
        {
            return 0;
        }
    }
    //![gaussianblur]

    /// Applying Median blur
    if( display_caption( "Median Blur" ) != 0 )
    {
        return 0;
    }

    //![medianblur]
    for ( int i = 1; i < MAX_KERNEL_LENGTH; i = i + 2 )
    {
        medianBlur ( src, dst, i );
        if( display_dst( DELAY_BLUR ) != 0 )
        {
            return 0;
        }
    }
    //![medianblur]

    /// Applying Bilateral Filter
    if( display_caption( "Bilateral Blur" ) != 0 )
    {
        return 0;
    }

    //![bilateralfilter]
    for ( int i = 1; i < MAX_KERNEL_LENGTH; i = i + 2 )
    {
        bilateralFilter ( src, dst, i, i*2, i/2 );
        if( display_dst( DELAY_BLUR ) != 0 )
        {
            return 0;
        }
    }
    //![bilateralfilter]

    /// Done
    display_caption( "Done!" );

    return 0;
}

/**
 * @function display_caption
 */
int display_caption( const char* caption )
{
    dst = Mat::zeros( src.size(), src.type() );
    putText( dst, caption,
             Point( src.cols/4, src.rows/2),
             FONT_HERSHEY_COMPLEX, 1, Scalar(255, 255, 255) );

    return display_dst(DELAY_CAPTION);
}

/**
 * @function display_dst
 */
int display_dst( int delay )
{
    imshow( window_name, dst );
    int c = waitKey ( delay );
    if( c >= 0 ) { return -1; }
    return 0;
}
```
(**Selesai pada 21 November 2019, jam 18.40**)

5. Lalu lakukan compile source code dengan command :
```
g++ smoothing_image.cpp -o smoothing_image `pkg-config --cflags --libs opencv`
```
(**Selesai pada 21 November 2019, jam 18.42**)

6. Download image lena.jpg dan simpan di dalam direktori yang sama dengan file hasil compile
(**Selesai pada 21 November 2019, jam 18.44**)

7. Dan jalankan source code dengan command :
```
cd Desktop/
cd test_code/
./smoothing_image lena.jpg
```
(**Selesai pada 21 November 2019, jam 18.46**)

8. Hasil dari Tutorial ini adalah seperti ini :

![lena](https://docs.opencv.org/3.4.8/Smoothing_Tutorial_Result_Median_Filter.jpg)
Dimana, kita belajar untuk mengapply berbagai macam filter pada sebuah gambar
(**Selesai pada 21 November 2019, jam 18.48**)

### 3. Eroding and Dilating

1. Pada tutorial ini, kita akan belajar cara :
    * Belajar cara mengunnakan 2 morphological operator yaitu erosion dan dilation
    * Function cv::erode
    * Function cv::dilate
    
2. Morphological operator adalah operator yang memproses gambar berdasarkan pada bentuknya. Morphological operator memberikan sebuah element structuring pada sebuag input image untuk menghasilkan output image

3. ada 2 tipe morphological operator dalam OpenCV yang bisa kita gunakan yaitu :
    * Dilate : adalah operator yang bisa digunakan untuk memperbesar benda dengan cara menghitung anchor point atau titik tengah dari suatu gambar dan mencari nilai maksimum yang bisa digunakan. Kemudian nilai maksimum itu dioutputkan pada tiap pixel sehingga gambar akan terlihat membesar
![awal](https://docs.opencv.org/3.4.8/Morphology_1_Tutorial_Theory_Original_Image.png)
Menjadi:
![dilation](https://docs.opencv.org/3.4.8/Morphology_1_Tutorial_Theory_Dilation.png)

    * Erode : adalah operator yang bisa digunakan untuk memperkecil benda dengan cara menghitung anchor point atau titik tengah dari suatu gambar dan mencari nilai minimum yang bisa digunakan. Kemudian nilai minimum itu dioutputkan pada tiap pixel sehingga gambar akan terlihat mengecil 
![awal](https://docs.opencv.org/3.4.8/Morphology_1_Tutorial_Theory_Original_Image.png)
Menjadi :
![erode](https://docs.opencv.org/3.4.8/Morphology_1_Tutorial_Theory_Erosion.png)

4. Buat file baru dengan nama erode.cpp dan copy-paste code berikut :
```cpp
/**

* @file Morphology_1.cpp

* @brief Erosion and Dilation sample code

* @author OpenCV team

*/

#include "opencv2/imgproc.hpp"

#include "opencv2/highgui.hpp"

#include <iostream>

using namespace cv;

using namespace std;

/// Global variables

Mat src, erosion_dst, dilation_dst;

int erosion_elem = 0;

int erosion_size = 0;

int dilation_elem = 0;

int dilation_size = 0;

int const max_elem = 2;

int const max_kernel_size = 21;

/** Function Headers */

void Erosion( int, void* );

void Dilation( int, void* );

/**

* @function main

*/

int main( int argc, char** argv )

{

/// Load an image

CommandLineParser parser( argc, argv, "{@input | LinuxLogo.jpg | input image}" );

src = imread(  parser.get<String>( "@input" ), IMREAD_COLOR );

if( src.empty() )

{

cout << "Could not open or find the image!\n" << endl;

cout << "Usage: " << argv[0] << " <Input image>" << endl;

return -1;

}

/// Create windows

namedWindow( "Erosion Demo", WINDOW_AUTOSIZE );

namedWindow( "Dilation Demo", WINDOW_AUTOSIZE );

moveWindow( "Dilation Demo", src.cols, 0 );

/// Create Erosion Trackbar

createTrackbar( "Element:\n 0: Rect \n 1: Cross \n 2: Ellipse", "Erosion Demo",

&erosion_elem, max_elem,

Erosion );

createTrackbar( "Kernel size:\n 2n +1", "Erosion Demo",

&erosion_size, max_kernel_size,

Erosion );

/// Create Dilation Trackbar

createTrackbar( "Element:\n 0: Rect \n 1: Cross \n 2: Ellipse", "Dilation Demo",

&dilation_elem, max_elem,

Dilation );

createTrackbar( "Kernel size:\n 2n +1", "Dilation Demo",

&dilation_size, max_kernel_size,

Dilation );

/// Default start

Erosion( 0, 0 );

Dilation( 0, 0 );

waitKey(0);

return 0;

}

//![erosion]

/**

* @function Erosion

*/

void Erosion( int, void* )

{

int erosion_type = 0;

if( erosion_elem == 0 ){ erosion_type = MORPH_RECT; }

else if( erosion_elem == 1 ){ erosion_type = MORPH_CROSS; }

else if( erosion_elem == 2) { erosion_type = MORPH_ELLIPSE; }

//![kernel]

Mat element = getStructuringElement( erosion_type,

Size( 2*erosion_size + 1, 2*erosion_size+1 ),

Point( erosion_size, erosion_size ) );

//![kernel]

/// Apply the erosion operation

erode( src, erosion_dst, element );

imshow( "Erosion Demo", erosion_dst );

}

//![erosion]

//![dilation]

/**

* @function Dilation

*/

void Dilation( int, void* )

{

int dilation_type = 0;

if( dilation_elem == 0 ){ dilation_type = MORPH_RECT; }

else if( dilation_elem == 1 ){ dilation_type = MORPH_CROSS; }

else if( dilation_elem == 2) { dilation_type = MORPH_ELLIPSE; }

Mat element = getStructuringElement( dilation_type,

Size( 2*dilation_size + 1, 2*dilation_size+1 ),

Point( dilation_size, dilation_size ) );

/// Apply the dilation operation

dilate( src, dilation_dst, element );

imshow( "Dilation Demo", dilation_dst );

}

//![dilation]
```
(**Selesai pada 21 November 2019, jam 18.58**)

5. Lalu lakukan compile source code dengan command :
```
g++ erode.cpp -o erode `pkg-config --cflags --libs opencv`
```
(**Selesai pada 21 November 2019, jam 19.00**)

6. Download gambar kucing, beri nama LogoLinux.jpg (karena di code kita memberi nama file gambarnya dengan nama LogoLinux.jpg), dan simpan di dalam direktori yang sama dengan file hasil compile
(**Selesai pada 21 November 2019, jam 19.02**)

7. Dan jalankan source code dengan command :
```
cd Desktop/
cd test_code/
./erode
```
(**Selesai pada 21 November 2019, jam 19.04**)

8. Hasil dari Tutorial ini adalah seperti ini :

![kochenk](https://docs.opencv.org/3.4.8/Morphology_1_Result.jpg)
Dimana, kita belajar untuk mengapply berbagai macam morphological operator pada sebuah gambar
(**Selesai pada 21 November 2019, jam 19.06**)

### 4. More Morphology Transformations
1. Pada tutorial ini, kita akan belajar cara :
    * Belajar cara mengunnakan 5 morphological transformations yaitu opening, closing, Morphological Gradient, Top Hat, Black Hat
    * Function cv::morphologyEx
    
2. Kali ini akan belajar 5 lagi morphological transformation yang mana mereka adalah gabungan dari morphological operator sebelumnya, yaitu Dilation dan Erode 

3. ada 5 tipe morphological transformation dalam OpenCV yang bisa kita gunakan yaitu :
    * Opening : adalah transformation dari erode diikuti oleh dilation yang berguna untuk menghilangkan benda-benda kecil yang tidak kita inginkan disekitar gambar
![opening](https://docs.opencv.org/3.4.8/Morphology_2_Tutorial_Theory_Opening.png)
    * Closing : adalah transformation dari dilation diikuti oleh erode yang berguna untuk menghilangkan lubang-lubang kecil yang tidak kita inginkan didalam gambar
![closing](https://docs.opencv.org/3.4.8/Morphology_2_Tutorial_Theory_Closing.png)
    * Morphological Gradient : adalah selisih dari dilation dan erode dari sebuah gambar, berguna untuk mencari garis luar dari sebuah gambar
![Gradient](https://docs.opencv.org/3.4.8/Morphology_2_Tutorial_Theory_Gradient.png)
    * Top Hat : selisih antara input image dengan opening
    ![Top Hat](https://docs.opencv.org/3.4.8/Morphology_2_Tutorial_Theory_TopHat.png)
    * Black Hat : selisih antara closing dengan input image
    ![Black Hat](https://docs.opencv.org/3.4.8/Morphology_2_Tutorial_Theory_BlackHat.png)

4. Buat file baru dengan nama morem.cpp dan copy-paste code berikut :
```cpp
/**
 * @file Morphology_2.cpp
 * @brief Advanced morphology Transformations sample code
 * @author OpenCV team
 */

#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace cv;

/// Global variables
Mat src, dst;

int morph_elem = 0;
int morph_size = 0;
int morph_operator = 0;
int const max_operator = 4;
int const max_elem = 2;
int const max_kernel_size = 21;

const char* window_name = "Morphology Transformations Demo";


/** Function Headers */
void Morphology_Operations( int, void* );

/**
 * @function main
 */
int main( int argc, char** argv )
{
  //![load]
  CommandLineParser parser( argc, argv, "{@input | baboon.jpg | input image}" );
  src = imread(  parser.get<String>( "@input" ) , IMREAD_COLOR );
  if (src.empty())
  {
    std::cout << "Could not open or find the image!\n" << std::endl;
    std::cout << "Usage: " << argv[0] << " <Input image>" << std::endl;
    return EXIT_FAILURE;
  }
  //![load]

  //![window]
  namedWindow( window_name, WINDOW_AUTOSIZE ); // Create window
  //![window]

  //![create_trackbar1]
  /// Create Trackbar to select Morphology operation
  createTrackbar("Operator:\n 0: Opening - 1: Closing  \n 2: Gradient - 3: Top Hat \n 4: Black Hat", window_name, &morph_operator, max_operator, Morphology_Operations );
  //![create_trackbar1]

  //![create_trackbar2]
  /// Create Trackbar to select kernel type
  createTrackbar( "Element:\n 0: Rect - 1: Cross - 2: Ellipse", window_name,
                  &morph_elem, max_elem,
                  Morphology_Operations );
  //![create_trackbar2]

  //![create_trackbar3]
  /// Create Trackbar to choose kernel size
  createTrackbar( "Kernel size:\n 2n +1", window_name,
                  &morph_size, max_kernel_size,
                  Morphology_Operations );
  //![create_trackbar3]

  /// Default start
  Morphology_Operations( 0, 0 );

  waitKey(0);
  return 0;
}

//![morphology_operations]
/**
 * @function Morphology_Operations
 */
void Morphology_Operations( int, void* )
{
  // Since MORPH_X : 2,3,4,5 and 6
  //![operation]
  int operation = morph_operator + 2;
  //![operation]

  Mat element = getStructuringElement( morph_elem, Size( 2*morph_size + 1, 2*morph_size+1 ), Point( morph_size, morph_size ) );

  /// Apply the specified morphology operation
  morphologyEx( src, dst, operation, element );
  imshow( window_name, dst );
}
//![morphology_operations]
```
(**Selesai pada 21 November 2019, jam 19.26**)

5. Lalu lakukan compile source code dengan command :
```
g++ morem.cpp -o morem `pkg-config --cflags --libs opencv`
```
(**Selesai pada 21 November 2019, jam 19.28**)

6. Download gambar monyet, beri nama baboon.jpg (karena di code kita memberi nama file gambarnya dengan nama baboon.jpg), dan simpan di dalam direktori yang sama dengan file hasil compile
(**Selesai pada 21 November 2019, jam 19.30**)

7. Dan jalankan source code dengan command :
```
cd Desktop/
cd test_code/
./morem
```
(**Selesai pada 21 November 2019, jam 19.32**)

8. Hasil dari Tutorial ini adalah seperti ini :

![Monyet](https://docs.opencv.org/3.4.8/Morphology_2_Tutorial_Result.jpg)
Dimana, kita belajar untuk mengapply berbagai macam morphological transformation pada sebuah gambar
(**Selesai pada 21 November 2019, jam 19.34**)

### 5. Basic Thresholding Operation
1. Pada tutorial ini, kita akan belajar cara :
    * Belajar melakukan operasi thresholding atau segmentasi dengan menggunakan function cv::threshold
    
2. Kali ini akan belajar cara melakukan segmentasi sederhana dengan cara threshold, dimana kita akan membedakan daerah dari gambar kita berdasarkan dengan perbedaan intensitas warna pixel sesuai dengan nilai yang akan kita tentukan. Lalu daerah yang kita inginkan ini nanti akan kita berikan nilai sesuai dengan keinginan kita untuk dilakukan proses lebih lanjut (contoh nilai 0 untuk hitam dam 255 untuk putih)

3. ada 5 tipe threshold atau segmentasi dalam OpenCV yang bisa kita gunakan yaitu :
    * Threshold awal : garis biru melambangkan titik thresh
![basic](https://docs.opencv.org/3.4.8/Threshold_Tutorial_Theory_Base_Figure.png)
    * Threshold Binary : semua daerah yang melebihi titik thresh diset ke nilai maksimum dan yang tidak melebihi diset ke nilai minimum
![threshold binary](https://docs.opencv.org/3.4.8/Threshold_Tutorial_Theory_Binary.png)
    * Threshold Binary Inverted : adalah kebalikan dari nilai Threshold Binary
![inverted](https://docs.opencv.org/3.4.8/Threshold_Tutorial_Theory_Binary_Inverted.png)
    * Truncate : semua nilai yang berada di atas titik thresh diset menjadi setara dengan titik thresh
![Truncate](https://docs.opencv.org/3.4.8/Threshold_Tutorial_Theory_Truncate.png)
    * Threshold to Zero: semua nilai dibawah titik thresh diset ke nilai minimum
    ![Threshold to Zero](https://docs.opencv.org/3.4.8/Threshold_Tutorial_Theory_Zero.png)
    * Threshold to Zero Inverted : kebalikan dari Threshold to Zero
    ![Threshold to Zero Inverted](https://docs.opencv.org/3.4.8/Threshold_Tutorial_Theory_Zero_Inverted.png)

4. Buat file baru dengan nama basict.cpp dan copy-paste code berikut :
```cpp
/**
 * @file Threshold.cpp
 * @brief Sample code that shows how to use the diverse threshold options offered by OpenCV
 * @author OpenCV team
 */

#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace cv;
using std::cout;

/// Global variables

int threshold_value = 0;
int threshold_type = 3;
int const max_value = 255;
int const max_type = 4;
int const max_binary_value = 255;

Mat src, src_gray, dst;
const char* window_name = "Threshold Demo";

const char* trackbar_type = "Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted";
const char* trackbar_value = "Value";

//![Threshold_Demo]
/**
 * @function Threshold_Demo
 */
static void Threshold_Demo( int, void* )
{
    /* 0: Binary
     1: Binary Inverted
     2: Threshold Truncated
     3: Threshold to Zero
     4: Threshold to Zero Inverted
    */
    threshold( src_gray, dst, threshold_value, max_binary_value, threshold_type );
    imshow( window_name, dst );
}
//![Threshold_Demo]

/**
 * @function main
 */
int main( int argc, char** argv )
{
    //! [load]
    String imageName("stuff.jpg"); // by default
    if (argc > 1)
    {
        imageName = argv[1];
    }
    src = imread( samples::findFile( imageName ), IMREAD_COLOR ); // Load an image

    if (src.empty())
    {
        cout << "Cannot read the image: " << imageName << std::endl;
        return -1;
    }

    cvtColor( src, src_gray, COLOR_BGR2GRAY ); // Convert the image to Gray
    //! [load]

    //! [window]
    namedWindow( window_name, WINDOW_AUTOSIZE ); // Create a window to display results
    //! [window]

    //! [trackbar]
    createTrackbar( trackbar_type,
                    window_name, &threshold_type,
                    max_type, Threshold_Demo ); // Create a Trackbar to choose type of Threshold

    createTrackbar( trackbar_value,
                    window_name, &threshold_value,
                    max_value, Threshold_Demo ); // Create a Trackbar to choose Threshold value
    //! [trackbar]

    Threshold_Demo( 0, 0 ); // Call the function to initialize

    /// Wait until the user finishes the program
    waitKey();
    return 0;
}
```
(**Selesai pada 21 November 2019, jam 19.54**)

5. Lalu lakukan compile source code dengan command :
```
g++ basict.cpp -o basict `pkg-config --cflags --libs opencv`
```
(**Selesai pada 21 November 2019, jam 19.56**)

6. Download gambar anjing, beri nama stuff.jpg (karena di code kita memberi nama file gambarnya dengan nama stuff.jpg), dan simpan di dalam direktori yang sama dengan file hasil compile
(**Selesai pada 21 November 2019, jam 19.58**)

7. Dan jalankan source code dengan command :
```
cd Desktop/
cd test_code/
./basict
```
(**Selesai pada 21 November 2019, jam 20.00**)

8. Hasil dari Tutorial ini adalah seperti ini :

Gambar awal anjing :
![anjing](https://docs.opencv.org/3.4.8/Threshold_Tutorial_Original_Image.jpg)

![binary threshold inverted](https://docs.opencv.org/3.4.8/Threshold_Tutorial_Result_Binary_Inverted.jpg)
Dimana, kita melakukan Binary Threshold Inverted yang mana semua daerah yang warnanya lebih besar/terang dari titik thresh akan menjadi hitam
![Threshold to Zero](https://docs.opencv.org/3.4.8/Threshold_Tutorial_Result_Zero.jpg)Dimana, kita melakukan Threshold to Zero yang mana semua daerah yang warnanya lebih gelap dari titik thresh akan menjadi gelap total dan yang nilainya lebih besar akan tetap nilainya
(**Selesai pada 21 November 2019, jam 20.06**)
