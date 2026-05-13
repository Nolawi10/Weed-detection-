
  ![image alt]([image-url-here](https://github.com/Nolawi10/Weed-detection-/blob/d96f5e3545e9db67f361cb003a5ee8518d089808/IMG_20260415_084027_015.jpg)

# 🌿 Django Weed Detection Application

A comprehensive Django-based web application for real-time weed detection using YOLO (You Only Look Once) deep learning model. The application supports multiple camera sources including built-in webcams, Android IP Webcam devices, and video file processing.

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Camera Sources](#-camera-sources)
- [Theme Support](#-theme-support)
- [API Endpoints](#-api-endpoints)
- [Future Enhancements](#-future-enhancements)
- [Technical Details](#-technical-details)
- [Troubleshooting](#-troubleshooting)

## ✨ Features

### Current Functionality

#### 🎥 **Multi-Source Camera Support**
- **Built-in Webcam**: Real-time detection using computer's webcam
- **Android IP Webcam**: Stream from Android devices over WiFi
- **Video File Processing**: Upload and process pre-recorded videos

#### 🎨 **Dual Theme Support**
- **Light Mode**: Clean, professional interface for bright environments
- **Dark Mode**: Modern dark interface for low-light conditions
- **Graceful Theme Switching**: Seamless transitions with active stream preservation

#### 🔄 **Smart Stream Management**
- **Mutual Exclusivity**: Only one camera source active at a time
- **Resource Protection**: Prevents conflicts between camera sources
- **Graceful Cleanup**: Proper resource management and thread termination

#### 📸 **Screenshot Functionality**
- **Server-Side Capture**: High-quality screenshot capture with detections
- **Automatic Download**: Instant download of captured frames
- **Timestamped Files**: Organized screenshot storage with timestamps

#### 📊 **Real-Time Information Panel**
- **Detection Statistics**: Live weed count and FPS monitoring
- **System Status**: Camera feed and AI model status indicators
- **Quick Actions**: Screenshot capture and info panel toggle
- **Detection Tips**: Best practices for optimal detection accuracy

#### 🛡️ **Advanced UI/UX**
- **Responsive Design**: Works on desktop and mobile devices
- **Accessibility**: Screen reader support and keyboard navigation
- **Visual Feedback**: Clear status indicators and loading states
- **Error Handling**: Comprehensive error messages and recovery options

## 🏗️ Architecture

### Backend Components

#### **Django Framework**
- **Views**: Handle HTTP requests, camera management, and stream processing
- **Models**: Session-based camera instance management
- **URLs**: RESTful routing for all application endpoints
- **Templates**: Jinja2-based HTML templates with theme support

#### **Camera Management System**
```python
# Core camera classes
VideoCamera          # Built-in webcam and video file processing
IPWebcamCamera      # Android IP Webcam HTTP stream handling
```

#### **AI/ML Pipeline**
- **YOLO Model**: Real-time object detection for weed identification
- **OpenCV**: Image processing and frame manipulation
- **Threading**: Concurrent video processing and web serving

### Frontend Components

#### **Responsive UI**
- **Tailwind CSS**: Modern, utility-first CSS framework
- **JavaScript**: Interactive features and AJAX functionality
- **Session Storage**: Client-side state management for theme switching

#### **Real-Time Features**
- **Live Video Streaming**: Server-sent video frames via HTTP
- **Dynamic Statistics**: Simulated real-time detection metrics
- **Interactive Controls**: Camera management and screenshot capture

## 🚀 Installation

### Prerequisites
```bash
# Python 3.8+
# Django 4.x
# OpenCV
# YOLO model files
# Android device with IP Webcam app (optional)
```

### Setup Steps
```bash
# 1. Clone the repository
git clone <repository-url>
cd Weed-Detection-django

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Start the development server
python manage.py runserver

# 5. Access the application
# Navigate to http://127.0.0.1:8000
```

### Required Dependencies
```txt
Django>=4.0
opencv-python
ultralytics
numpy
requests
Pillow
```

## 📖 Usage

### Getting Started

1. **Launch Application**: Navigate to `http://127.0.0.1:8000`
2. **Choose Theme**: Select Light or Dark mode on the landing page
3. **Select Camera Source**: Choose from three available options
4. **Start Detection**: Begin real-time weed detection
5. **Capture Screenshots**: Save detection frames for analysis

### Camera Source Options

#### **1. Real-Time Detection (Built-in Webcam)**
- Click "Start Webcam Feed"
- Grant camera permissions when prompted
- View live detection with bounding boxes around detected weeds

#### **2. Android IP Webcam**
- Install "IP Webcam" app on Android device
- Connect Android device to same WiFi network
- Find device IP address in the app interface
- Enter IP address (and optional port) in the web interface
- Click "Connect to IP Webcam"

#### **3. Video File Processing**
- Click "Choose File" to select a video
- Upload video file (MP4, AVI, MOV formats supported)
- Click "Upload and Process"
- View frame-by-frame detection results

## 🎥 Camera Sources

### Built-in Webcam
- **Protocol**: Direct OpenCV camera access
- **Latency**: Minimal (local processing)
- **Quality**: Depends on webcam specifications
- **Use Case**: Desktop/laptop real-time detection

### Android IP Webcam
- **Protocol**: HTTP/MJPEG streaming
- **Default Port**: 8080
- **Network**: WiFi (same network required)
- **Quality**: Configurable in Android app
- **Use Case**: Remote monitoring, mobile camera positioning

### Video File Upload
- **Formats**: MP4, AVI, MOV, and other OpenCV-supported formats
- **Processing**: Frame-by-frame analysis
- **Storage**: Temporary file storage during processing
- **Use Case**: Batch processing, analysis of recorded footage

## 🎨 Theme Support

### Light Theme
- **Design**: Clean, professional appearance
- **Colors**: White backgrounds, green accents
- **Use Case**: Bright environments, office settings

### Dark Theme
- **Design**: Modern dark interface
- **Colors**: Dark gray backgrounds, bright accents
- **Use Case**: Low-light environments, extended usage

### Theme Switching
- **Graceful Transitions**: Active streams preserved during theme changes
- **Session Persistence**: Theme choice remembered across sessions
- **Auto-Restart**: Streams automatically resume in new theme

## 🔗 API Endpoints

### Core Endpoints
```
GET  /                          # Landing page with theme selection
GET  /app/                      # Main application interface
GET  /app/?theme=dark           # Main interface with dark theme
POST /configure_ipwebcam/       # Configure Android IP Webcam
GET  /start_stream/<source>/    # Start camera stream (webcam/ipwebcam)
POST /upload_video/             # Upload and process video file
GET  /video_feed/               # Live video stream endpoint
GET  /stop_stream/              # Stop stream and redirect to home
GET  /stop_stream_only/         # Stop stream without redirect
POST /capture_screenshot/       # Capture detection frame screenshot
```

### Stream Management
- **Session-Based**: Each user session maintains independent camera instances
- **Thread-Safe**: Concurrent access protection with threading locks
- **Resource Cleanup**: Automatic cleanup on session end or stream stop

## 🚀 Future Enhancements

### 🌱 **Enhanced Weed Classification**

#### **Multi-Species Detection**
- **Broadleaf Weeds**: Dandelion, plantain, clover identification
- **Grassy Weeds**: Crabgrass, foxtail, annual bluegrass detection
- **Invasive Species**: Specialized detection for regional invasive plants
- **Confidence Scoring**: Probability scores for each detection

#### **Advanced AI Features**
- **Weed Growth Stage**: Seedling, mature, flowering stage classification
- **Severity Assessment**: Infestation density and coverage analysis
- **Treatment Recommendations**: Suggested herbicides and application methods
- **Seasonal Adaptation**: Model adjustments for different growing seasons

### 📊 **Analytics and Reporting**

#### **Detection Analytics**
- **Historical Data**: Track weed detection trends over time
- **Heat Maps**: Visualize weed distribution patterns
- **Growth Tracking**: Monitor weed population changes
- **Field Mapping**: GPS-based location tracking for outdoor use

#### **Reporting System**
- **PDF Reports**: Automated detection summary reports
- **CSV Export**: Raw detection data for further analysis
- **Email Notifications**: Alerts for high infestation levels
- **Dashboard**: Comprehensive analytics dashboard

### 🗄️ **Data Management**

#### **Database Integration**
- **Detection History**: Store all detection events with metadata
- **User Profiles**: Multiple user accounts with personalized settings
- **Field Management**: Organize detection sessions by field/location
- **Image Gallery**: Archive of captured screenshots and detections

#### **Cloud Integration**
- **Cloud Storage**: Backup detection data and images
- **Model Updates**: Automatic AI model updates from cloud
- **Sync Across Devices**: Multi-device access to detection data
- **API Integration**: Connect with farm management systems

### 📱 **Mobile and IoT**

#### **Mobile Application**
- **Native Mobile App**: iOS and Android companion apps
- **Offline Detection**: Local model inference without internet
- **GPS Integration**: Location-based detection logging
- **Camera Optimization**: Mobile-specific camera controls

#### **IoT Integration**
- **Drone Support**: Aerial weed detection and mapping
- **Sensor Networks**: Integration with soil and weather sensors
- **Automated Alerts**: Smart notifications based on detection patterns
- **Edge Computing**: Deploy models on edge devices for field use

### 🤖 **AI Model Improvements**

#### **Model Enhancements**
- **Custom Training**: Train on user-specific weed types
- **Transfer Learning**: Adapt to local weed species
- **Multi-Modal Input**: Combine visual and spectral data
- **Real-Time Learning**: Continuous model improvement from user feedback

#### **Performance Optimization**
- **Model Quantization**: Faster inference on limited hardware
- **GPU Acceleration**: CUDA support for high-performance detection
- **Batch Processing**: Efficient processing of multiple images
- **Edge Deployment**: Optimize for mobile and embedded devices

### 🔧 **System Features**

#### **Advanced Camera Support**
- **Multiple Cameras**: Simultaneous multi-camera monitoring
- **Camera Calibration**: Automatic camera parameter optimization
- **Night Vision**: Infrared and low-light detection support
- **PTZ Control**: Pan-tilt-zoom camera remote control

#### **Integration Features**
- **GIS Integration**: Geographic Information System support
- **Weather API**: Weather-based detection recommendations
- **Herbicide Database**: Treatment recommendation system
- **Equipment Integration**: Connect with spraying equipment

### 🛠️ **Development Features**

#### **Developer Tools**
- **API Documentation**: Comprehensive REST API documentation
- **SDK Development**: Software development kits for integration
- **Plugin System**: Extensible architecture for custom features
- **Testing Suite**: Automated testing for all components

#### **Deployment Options**
- **Docker Support**: Containerized deployment
- **Cloud Deployment**: AWS, Azure, GCP deployment guides
- **Load Balancing**: Multi-instance deployment support
- **Monitoring**: Application performance monitoring

## 🔧 Technical Details

### AI Model
- **Framework**: YOLO (You Only Look Once)
- **Input**: RGB images from camera sources
- **Output**: Bounding boxes with confidence scores
- **Performance**: ~8-11 FPS on standard hardware

### Session Management
- **Thread-Safe**: Concurrent user support
- **Resource Isolation**: Independent camera instances per session
- **Memory Management**: Automatic cleanup of inactive sessions

### Security
- **CSRF Protection**: Cross-site request forgery prevention
- **Session Security**: Secure session key management
- **Input Validation**: IP address and file upload validation

## 🐛 Troubleshooting

### Common Issues

#### **Camera Access Problems**
- **Permission Denied**: Grant camera permissions in browser
- **Camera Busy**: Close other applications using the camera
- **Poor Quality**: Check camera drivers and settings

#### **Android IP Webcam Issues**
- **Connection Failed**: Verify WiFi network and IP address
- **Stream Interrupted**: Check network stability and app settings
- **Port Conflicts**: Try different port numbers (8080, 8081, etc.)

#### **Performance Issues**
- **Low FPS**: Reduce video resolution or upgrade hardware
- **High CPU Usage**: Close unnecessary applications
- **Memory Leaks**: Restart application if performance degrades

### Debug Mode
```bash
# Enable Django debug mode
DEBUG = True  # in settings.py

# View detailed error messages
python manage.py runserver --verbosity=2
```

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Implement changes with tests
4. Submit pull request with detailed description

### Code Standards
- **PEP 8**: Python code style compliance
- **Type Hints**: Use type annotations where applicable
- **Documentation**: Comprehensive docstrings and comments
- **Testing**: Unit tests for new functionality

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **YOLO**: Ultralytics YOLO for object detection
- **Django**: Web framework for rapid development
- **OpenCV**: Computer vision and image processing
- **Tailwind CSS**: Modern CSS framework for styling

---

**Built with ❤️ for sustainable agriculture and precision farming**
